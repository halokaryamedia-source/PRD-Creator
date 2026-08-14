#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "workspace" / "active" / "the-clockwork-vault"
HTML = PROJECT / "output" / "v1.0.0" / "prd.html"
TMP_HTML = Path("/tmp/clockwork-production-assets-visual-proof.html")


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=False)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def browser() -> str:
    for name in ("google-chrome", "chromium", "chromium-browser"):
        path = shutil.which(name)
        if path:
            return path
    raise RuntimeError("No Chromium browser is available on the runner")


def inject_probe() -> None:
    source = HTML.read_text(encoding="utf-8")
    require(source.count("</body>") == 1, "Expected exactly one </body> marker")
    probe = r'''<script id="temporary-browser-proof">
window.addEventListener('load', function () {
  setTimeout(function () {
    const nav = document.querySelector('.production-assets-nav');
    const links = nav ? Array.from(nav.querySelectorAll('a[data-target]')) : [];
    const pages = [];
    links.forEach(function (link) {
      link.click();
      const id = link.getAttribute('data-target');
      const page = document.getElementById(id);
      if (!page) {
        pages.push({id: id, missing: true});
        return;
      }
      const pageRect = page.getBoundingClientRect();
      const code = page.querySelector('.footer-code');
      const codeRect = code ? code.getBoundingClientRect() : {left: 0, right: 0, bottom: 0, width: 0};
      const risky = Array.from(page.querySelectorAll('.pa-summary,.pa-group,.pa-card,.voice-script-card,.voice-script-display'));
      pages.push({
        id: id,
        visible: pageRect.width > 0 && pageRect.height > 0 && getComputedStyle(page).display !== 'none',
        footerCode: code ? code.textContent.trim() : '',
        footerInside: !!code && codeRect.width > 0 && codeRect.left >= pageRect.left - 1 && codeRect.right <= pageRect.right + 1 && codeRect.bottom <= pageRect.bottom + 1,
        pageOverflow: page.scrollWidth > page.clientWidth + 1,
        riskyOverflow: risky.some(function (node) { return node.scrollWidth > node.clientWidth + 1; })
      });
    });
    const navLinks = nav ? Array.from(nav.querySelectorAll('a')) : [];
    const result = {
      width: window.innerWidth,
      height: window.innerHeight,
      navPresent: !!nav,
      navLinkCount: navLinks.length,
      navOverflow: !!nav && (nav.scrollWidth > nav.clientWidth + 1 || navLinks.some(function (node) { return node.scrollWidth > node.clientWidth + 1; })),
      documentOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
      pages: pages
    };
    const pre = document.createElement('pre');
    pre.id = 'visual-proof-result';
    pre.textContent = JSON.stringify(result);
    document.body.appendChild(pre);
  }, 350);
});
</script>'''
    TMP_HTML.write_text(source.replace("</body>", probe + "\n</body>", 1), encoding="utf-8")


def inspect_width(chrome: str, width: int) -> dict[str, object]:
    result = run(
        chrome,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--hide-scrollbars",
        "--allow-file-access-from-files",
        f"--window-size={width},1000",
        "--virtual-time-budget=2500",
        "--dump-dom",
        TMP_HTML.as_uri(),
    )
    require(result.returncode == 0, f"Chromium failed at {width}px: {result.stderr[-1200:]}")
    match = re.search(r'<pre id="visual-proof-result">(.*?)</pre>', result.stdout, re.S)
    require(match is not None, f"Browser proof result missing at {width}px")
    payload = json.loads(html.unescape(match.group(1)))
    require(payload["navPresent"], f"Production Assets navigation missing at {width}px")
    require(payload["navLinkCount"] >= 1, f"No Production Assets navigation links at {width}px")
    require(not payload["navOverflow"], f"Production Assets navigation overflows at {width}px")
    require(not payload["documentOverflow"], f"Document horizontally overflows at {width}px")
    require(payload["pages"], f"No Production Assets pages inspected at {width}px")
    for page in payload["pages"]:
        require(not page.get("missing"), f"Missing Production Assets target at {width}px: {page}")
        require(page["visible"], f"Production Assets page did not become visible at {width}px: {page['id']}")
        require(re.fullmatch(r"PA-\d{2}", page["footerCode"]) is not None, f"Unexpected footer code at {width}px: {page}")
        require(page["footerInside"], f"Footer code falls outside page bounds at {width}px: {page}")
        require(not page["pageOverflow"], f"Production Assets page overflows at {width}px: {page}")
        require(not page["riskyOverflow"], f"Production Assets content overflows at {width}px: {page}")
    return payload


def record_proof() -> None:
    validation = ROOT / "docs" / "knowledge" / "reviews" / "current-validation.md"
    text = validation.read_text(encoding="utf-8")
    section = """## Refreshed Production Assets browser proof

After RQ-05/RQ-13 changed Production Assets page identity/footer codes, the current Clockwork `v1.0.0/prd.html` was regenerated and inspected in actual headless Chromium layout at **1500×1000** and **1000×1000**. Every Production Assets navigation target became visible, every page exposed the expected `PA-##` footer code inside page bounds, Production Assets navigation had no horizontal overflow, the document had no horizontal viewport overflow, and the scanned Production Assets summary/card/Voice surfaces had no horizontal content overflow.

Result: `Production Assets visual sanity: PASS` for the RQ-05/RQ-13 identity change at the two claimed desktop widths. This proof does not broaden the claim to unrelated mobile widths or later visual changes.

"""
    if "## Refreshed Production Assets browser proof" not in text:
        marker = "## Browser proof\n"
        require(marker in text, "current-validation Browser proof marker missing")
        text = text.replace(marker, section + marker, 1)
        validation.write_text(text, encoding="utf-8")

    audit = ROOT / "docs" / "knowledge" / "reviews" / "repository-quality-audit-2026-08-14.md"
    text = audit.read_text(encoding="utf-8")
    note = """## Visual proof update — RQ-05/RQ-13

The visible `PA-##` footer-code change received actual Chromium layout proof at 1500×1000 and 1000×1000 on the current Clockwork delivery. Production Assets navigation/page activation, footer-code placement, and horizontal overflow checks passed at both widths. RQ-05/RQ-13 are mechanically and visually closed for the claimed desktop scope.

"""
    if "## Visual proof update — RQ-05/RQ-13" not in text:
        marker = "## Ordered remediation\n"
        require(marker in text, "audit Ordered remediation marker missing")
        text = text.replace(marker, note + marker, 1)
        audit.write_text(text, encoding="utf-8")

    next_action = ROOT / "docs" / "knowledge" / "next-action.md"
    next_action.write_text(
        """# Next Action

## Current Status

`REPOSITORY_QUALITY_ACTIVE_REMEDIATION_COMPLETE`

The complete audit remains durable at `docs/knowledge/reviews/repository-quality-audit-2026-08-14.md`. All proven active/current-context defects selected for this remediation are closed through RQ-08, and the visible RQ-05/RQ-13 Production Assets identity change has refreshed Chromium visual proof at 1500px and 1000px desktop widths.

Remaining findings in `docs/knowledge/operations/backlog.md` are conditional or design-sensitive: RQ-09/RQ-11 should be touched only with a concrete same-owner need, RQ-10 requires explicit Golden-design approval, and RQ-14 needs a real >26-page-code use case. They are not a mandate for speculative cleanup.

## Next Step

Proceed to the next real PRD/PRD-Creator work. Promote a remaining repository-quality backlog item only when real usage exposes the matching defect or the user explicitly chooses the design-sensitive change.
""",
        encoding="utf-8",
    )


def main() -> int:
    delivered = run(sys.executable, "kits/project-document-generator/renderer/delivery.py", str(PROJECT))
    require(delivered.returncode == 0, delivered.stderr or delivered.stdout)
    require(HTML.is_file(), f"Missing current Clockwork PRD: {HTML}")
    inject_probe()
    chrome = browser()
    results = [inspect_width(chrome, width) for width in (1500, 1000)]
    print(json.dumps(results, indent=2))
    record_proof()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"VISUAL PROOF FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
