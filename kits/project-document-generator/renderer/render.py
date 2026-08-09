#!/usr/bin/env python3
"""Render derived PRD JSON into the approved HTML shell without redesigning it."""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0, str(HERE))
from core import esc, i18n, slug, txt  # noqa: E402
from pages import flow_pages, global_pages, glossary, navigation, overview, package_pages  # noqa: E402

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
OPEN_RE = re.compile(r"\b(?:TBD|TODO|FIXME|INSERT\s+(?:TEXT|VALUE)|USE\s+APPROVED\s+AMOUNT)\b|\[OPEN\]", re.I)


def validate(data: dict) -> None:
    if not isinstance(data, dict) or not isinstance(data.get("document"), dict) or not txt(data["document"].get("title"))["en"].strip(): raise ValueError("document.title is required")
    if not isinstance(data.get("overview"), dict): raise ValueError("overview is required")
    for key in ("gameplay_flow", "global_development", "packages"):
        if key in data and not isinstance(data[key], list): raise ValueError(f"{key} must be an array")
    for group in (data.get("gameplay_flow", []), data.get("global_development", []), data.get("packages", [])):
        for item in group:
            if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not ID_RE.match(item["id"]): raise ValueError(f"Invalid stable id: {item.get('id')!r}")
    pids = [p["id"] for p in data.get("packages", [])]
    if len(pids) != len(set(pids)): raise ValueError("Duplicate package id")
    for pkg in data.get("packages", []):
        for key in ("gameplay", "level_design", "developer"):
            if not isinstance(pkg.get(key), dict): raise ValueError(f'Package {pkg["id"]} requires {key}')
        if not pkg["developer"].get("scoring") and not pkg["developer"].get("completion_data"): raise ValueError(f'Package {pkg["id"]} developer requires scoring or completion_data')
    if OPEN_RE.search(json.dumps(data, ensure_ascii=False)): raise ValueError("Render data contains unresolved placeholder text")


def element_range(src: str, marker: str, tag: str) -> tuple[int, int]:
    start = src.find(marker)
    if start < 0: raise ValueError(f"Template marker not found: {marker}")
    open_end, depth = src.find(">", start) + 1, 0
    for match in re.finditer(rf"</?{tag}\b[^>]*>", src[start:], re.I):
        depth += -1 if match.group(0).startswith("</") else 1
        if depth == 0: return open_end, start + match.start()
    raise ValueError(f"Closing tag not found for {marker}")


def replace_inner(src: str, marker: str, tag: str, inner: str) -> str:
    a, b = element_range(src, marker, tag)
    return src[:a] + inner + src[b:]


def render(template: Path, render_data: Path, output: Path) -> None:
    if not template.is_file(): raise FileNotFoundError(f"Approved template not found: {template}")
    data = json.loads(render_data.read_text(encoding="utf-8")); validate(data)
    src = template.read_text(encoding="utf-8")
    pages = [overview(data)] + flow_pages(data) + global_pages(data) + package_pages(data)
    nav = navigation(data)

    title = txt(data["document"]["title"]); mark = str(data["document"].get("brand_mark") or title["en"][:1] or "P").upper()
    brand = f'<a aria-label="{esc(title["en"])} overview" class="sidebar-brand" href="#summary"><span class="brand-mark">{i18n(mark)}</span><span class="brand-copy"><strong>{i18n(title)}</strong><small>{i18n(data["document"].get("document_type", "Production Specification"))}</small></span></a>'
    src, count = re.subn(r'<a\s+aria-label="[^"]* overview"\s+class="sidebar-brand"\s+href="#summary">.*?</a>', brand, src, count=1, flags=re.S)
    if count != 1: raise ValueError("Sidebar brand marker not found deterministically")
    src = replace_inner(src, '<nav class="sidebar-nav">', "nav", nav)
    src = replace_inner(src, '<main class="document-main">', "main", "".join(pages))

    g = json.dumps(glossary(data), ensure_ascii=False, separators=(",", ":"))
    src, count = re.subn(r"const glossary = .*?;\n\s*const tooltip =", f"const glossary = {g};\n  const tooltip =", src, count=1, flags=re.S)
    if count != 1: raise ValueError("Glossary marker not found deterministically")

    doc, namespace = data["document"], slug(title["en"])
    page_title = f'{title["en"]} — {txt(doc.get("subtitle", "Production Specification"))["en"]}'
    src, count = re.subn(r"<title>.*?</title>", f"<title>{esc(page_title)}</title>", src, count=1, flags=re.S)
    if count != 1: raise ValueError("Template title not found")
    desc = txt(doc.get("description") or data["overview"].get("project_context") or page_title)["en"]
    src = re.sub(r'<meta\s+content="[^"]*"\s+name="description"\s*/?>', f'<meta content="{esc(desc)}" name="description"/>', src, count=1, flags=re.I)
    src = re.sub(r'<meta\s+content="[^"]*"\s+name="specification-version"\s*/?>', f'<meta content="prd-{namespace}-v{esc(doc.get("version", "1.0"))}" name="specification-version"/>', src, count=1, flags=re.I)
    src = src.replace("aftershock-document-", f"prd-{namespace}-").replace("aftershock-sidebar-collapsed", f"prd-{namespace}-sidebar-collapsed")

    ids = set(re.findall(r'<section\b[^>]*\bid="([^"]+)"', src)); targets = set(re.findall(r'data-target="([^"]+)"', nav))
    missing = sorted(targets - ids)
    if missing: raise ValueError(f"Navigation targets missing from generated pages: {missing}")
    if OPEN_RE.search("".join(pages)): raise ValueError("Generated pages contain unresolved placeholders")
    output.parent.mkdir(parents=True, exist_ok=True); output.write_text(src, encoding="utf-8")


def main() -> None:
    default = HERE.parent / "template" / "approved-document.html"
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("render_data", type=Path); parser.add_argument("output", type=Path); parser.add_argument("--template", type=Path, default=default)
    args = parser.parse_args(); render(args.template, args.render_data, args.output); print(args.output)

if __name__ == "__main__": main()
