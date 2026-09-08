#!/usr/bin/env python3
"""Verify a rendered PRD in a real headless Chrome session without extra dependencies."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import shutil
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


class BrowserVerifyError(RuntimeError):
    """Raised when the real-browser verification contract cannot be proven."""


def _driver_path() -> str:
    candidates: list[str] = []
    configured = os.environ.get("CHROMEWEBDRIVER", "").strip()
    if configured:
        configured_path = Path(configured)
        candidates.append(str(configured_path / "chromedriver") if configured_path.is_dir() else str(configured_path))
    discovered = shutil.which("chromedriver")
    if discovered:
        candidates.append(discovered)
    candidates.extend(
        [
            "/usr/local/share/chromedriver-linux64/chromedriver",
            "/usr/bin/chromedriver",
        ]
    )
    for candidate in candidates:
        if Path(candidate).is_file():
            return candidate
    raise BrowserVerifyError("ChromeDriver is required for browser verification")


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def _request(base: str, method: str, path: str, payload: dict[str, Any] | None = None) -> Any:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        f"{base}{path}",
        data=data,
        method=method,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            body = response.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError) as exc:
        raise BrowserVerifyError(f"WebDriver request failed: {method} {path}: {exc}") from exc
    decoded = json.loads(body) if body else {}
    value = decoded.get("value") if isinstance(decoded, dict) else None
    if isinstance(value, dict) and value.get("error"):
        raise BrowserVerifyError(f"WebDriver error: {value.get('error')}: {value.get('message')}")
    return value


def _wait_driver(base: str, process: subprocess.Popen[str]) -> None:
    deadline = time.monotonic() + 10
    while time.monotonic() < deadline:
        if process.poll() is not None:
            stderr = process.stderr.read() if process.stderr is not None else ""
            raise BrowserVerifyError(f"ChromeDriver exited before startup: {stderr.strip()}")
        try:
            value = _request(base, "GET", "/status")
            if isinstance(value, dict) and value.get("ready") is True:
                return
        except BrowserVerifyError:
            time.sleep(0.1)
    raise BrowserVerifyError("ChromeDriver did not become ready")


def _execute(base: str, session_id: str, script: str, args: list[Any] | None = None) -> Any:
    return _request(
        base,
        "POST",
        f"/session/{session_id}/execute/sync",
        {"script": script, "args": args or []},
    )


def _browser_logs(base: str, session_id: str) -> list[dict[str, Any]]:
    value = _request(base, "POST", f"/session/{session_id}/se/log", {"type": "browser"})
    if not isinstance(value, list):
        raise BrowserVerifyError("ChromeDriver did not return browser console logs")
    return [item for item in value if isinstance(item, dict)]


def _snapshot(base: str, session_id: str) -> bytes:
    value = _request(base, "GET", f"/session/{session_id}/screenshot")
    if not isinstance(value, str):
        raise BrowserVerifyError("ChromeDriver did not return a screenshot")
    try:
        image = base64.b64decode(value, validate=True)
    except ValueError as exc:
        raise BrowserVerifyError("ChromeDriver screenshot was not valid base64") from exc
    if not image.startswith(b"\x89PNG\r\n\x1a\n") or len(image) < 5_000:
        raise BrowserVerifyError("Rendered screenshot is missing or implausibly small")
    return image


DOM_AUDIT = r"""
const ids = [...document.querySelectorAll('[id]')].map(node => node.id).filter(Boolean);
const seen = new Set();
const duplicateIds = [];
for (const id of ids) {
  if (seen.has(id) && !duplicateIds.includes(id)) duplicateIds.push(id);
  seen.add(id);
}
const hashLinks = [...document.querySelectorAll('a[href^="#"]')];
const missingTargets = hashLinks
  .map(link => link.getAttribute('href'))
  .filter(href => href && href.length > 1 && !document.getElementById(href.slice(1)));
const invalidTabGroups = [...document.querySelectorAll('.package-tabs')].map((group, index) => {
  const links = [...group.querySelectorAll('.section-tab-link')];
  const current = links.filter(link => link.getAttribute('aria-current') === 'page');
  const active = links.filter(link => link.classList.contains('is-active'));
  return current.length === 1 && active.length === 1 && current[0] === active[0] ? null : index;
}).filter(value => value !== null);
const unnamedInteractive = [...document.querySelectorAll('a,button,input,select,textarea')].filter(node => {
  if (node.hasAttribute('hidden') || node.getAttribute('aria-hidden') === 'true') return false;
  const name = (node.getAttribute('aria-label') || node.getAttribute('title') || node.textContent || '').trim();
  return !name && !(node instanceof HTMLInputElement && (node.value || node.placeholder));
}).map(node => node.outerHTML.slice(0, 160));
const docWidth = Math.max(document.documentElement.scrollWidth, document.body ? document.body.scrollWidth : 0);
const viewportWidth = window.innerWidth;
const i18nNodes = [...document.querySelectorAll('.i18n-text')];
const emptyI18n = i18nNodes.filter(node => !(node.textContent || '').trim()).length;
return {
  readyState: document.readyState,
  title: document.title,
  language: document.documentElement.lang,
  sheetCount: document.querySelectorAll('.sheet').length,
  duplicateIds,
  missingTargets,
  invalidTabGroups,
  unnamedInteractive,
  horizontalOverflowPx: Math.max(0, docWidth - viewportWidth),
  i18nNodeCount: i18nNodes.length,
  emptyI18n,
};
"""

INTERACTION_AUDIT = r"""
const links = [...document.querySelectorAll('a[href^="#"]')].filter(link => {
  const href = link.getAttribute('href');
  return href && href.length > 1 && document.getElementById(href.slice(1));
});
const failures = [];
for (const link of links.slice(0, 24)) {
  const href = link.getAttribute('href');
  link.click();
  if (window.location.hash !== href) failures.push(href);
}
const languageFailures = [];
const controls = [...document.querySelectorAll('.language-panel [data-lang], .language-panel [data-language]')];
for (const control of controls) {
  const expected = control.dataset.lang || control.dataset.language;
  if (!expected) continue;
  control.click();
  if (document.documentElement.lang !== expected) languageFailures.push(expected);
}
return {testedHashLinks: Math.min(links.length, 24), hashFailures: failures, languageControls: controls.length, languageFailures};
"""


def verify(html_path: Path, screenshot_path: Path | None = None) -> dict[str, Any]:
    html_path = html_path.resolve()
    if not html_path.is_file():
        raise BrowserVerifyError(f"Rendered PRD not found: {html_path}")

    port = _free_port()
    base = f"http://127.0.0.1:{port}"
    process = subprocess.Popen(
        [_driver_path(), f"--port={port}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )
    session_id = ""
    try:
        _wait_driver(base, process)
        session = _request(
            base,
            "POST",
            "/session",
            {
                "capabilities": {
                    "alwaysMatch": {
                        "browserName": "chrome",
                        "goog:chromeOptions": {
                            "args": [
                                "--headless=new",
                                "--no-sandbox",
                                "--disable-gpu",
                                "--allow-file-access-from-files",
                                "--window-size=1440,1200",
                            ]
                        },
                        "goog:loggingPrefs": {"browser": "ALL"},
                    }
                }
            },
        )
        if not isinstance(session, dict) or not isinstance(session.get("sessionId"), str):
            raise BrowserVerifyError("ChromeDriver did not create a valid session")
        session_id = session["sessionId"]
        _request(base, "POST", f"/session/{session_id}/url", {"url": html_path.as_uri()})

        deadline = time.monotonic() + 10
        ready = False
        while time.monotonic() < deadline:
            ready = _execute(base, session_id, "return document.readyState === 'complete';") is True
            if ready:
                break
            time.sleep(0.05)
        if not ready:
            raise BrowserVerifyError("Rendered PRD did not reach document.readyState=complete")

        dom = _execute(base, session_id, DOM_AUDIT)
        interaction = _execute(base, session_id, INTERACTION_AUDIT)
        if not isinstance(dom, dict) or not isinstance(interaction, dict):
            raise BrowserVerifyError("Browser audit scripts did not return structured results")

        severe_logs = [
            item for item in _browser_logs(base, session_id) if str(item.get("level", "")).upper() == "SEVERE"
        ]
        screenshot = _snapshot(base, session_id)
        if screenshot_path is not None:
            screenshot_path.parent.mkdir(parents=True, exist_ok=True)
            screenshot_path.write_bytes(screenshot)

        errors: list[str] = []
        if dom.get("readyState") != "complete":
            errors.append("document did not finish loading")
        if not str(dom.get("title") or "").strip():
            errors.append("document title is empty")
        if int(dom.get("sheetCount") or 0) < 1:
            errors.append("no rendered .sheet pages found")
        if dom.get("duplicateIds"):
            errors.append(f"duplicate DOM ids: {dom['duplicateIds']}")
        if dom.get("missingTargets"):
            errors.append(f"missing hash navigation targets: {dom['missingTargets']}")
        if dom.get("invalidTabGroups"):
            errors.append(f"package tab groups lack exactly one matching active/current tab: {dom['invalidTabGroups']}")
        if dom.get("unnamedInteractive"):
            errors.append(f"interactive controls without accessible names: {dom['unnamedInteractive'][:5]}")
        if int(dom.get("horizontalOverflowPx") or 0) > 2:
            errors.append(f"document has horizontal viewport overflow: {dom['horizontalOverflowPx']}px")
        if int(dom.get("emptyI18n") or 0) > 0:
            errors.append(f"empty localized text nodes: {dom['emptyI18n']}")
        if interaction.get("hashFailures"):
            errors.append(f"hash navigation interaction failed: {interaction['hashFailures']}")
        if interaction.get("languageFailures"):
            errors.append(f"language controls failed to update document language: {interaction['languageFailures']}")
        if severe_logs:
            errors.append(
                "browser console contains SEVERE entries: "
                + "; ".join(str(item.get("message") or "")[:240] for item in severe_logs[:5])
            )

        return {
            "status": "pass" if not errors else "fail",
            "errors": errors,
            "html": html_path.as_posix(),
            "dom": dom,
            "interaction": interaction,
            "severe_console_count": len(severe_logs),
            "screenshot_sha256": hashlib.sha256(screenshot).hexdigest(),
            "screenshot_bytes": len(screenshot),
        }
    finally:
        if session_id:
            try:
                _request(base, "DELETE", f"/session/{session_id}")
            except BrowserVerifyError:
                pass
        process.terminate()
        try:
            process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=3)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="rendered prd.html to verify")
    parser.add_argument("--screenshot", type=Path, help="optional PNG evidence path")
    args = parser.parse_args()
    try:
        result = verify(args.html, args.screenshot)
    except (BrowserVerifyError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "fail", "errors": [str(exc)]}, indent=2), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
