#!/usr/bin/env python3
"""Render derived PRD JSON into the approved HTML shell without redesigning it."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from core import esc, i18n, slug, txt  # noqa: E402
from pages import flow_pages, global_pages, glossary, navigation, overview, package_pages  # noqa: E402

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
OPEN_RE = re.compile(r"\b(?:TBD|TODO|FIXME|INSERT\s+(?:TEXT|VALUE)|USE\s+APPROVED\s+AMOUNT)\b|\[OPEN\]", re.I)
SIDEBAR_BRAND_RE = re.compile(r'<a\s+aria-label="[^"]* overview"\s+class="sidebar-brand"\s+href="#summary">.*?</a>', re.S)
TITLE_RE = re.compile(r"<title>.*?</title>", re.S | re.I)
DESCRIPTION_META_RE = re.compile(r'<meta\s+content="[^"]*"\s+name="description"\s*/?>', re.I)
SPEC_VERSION_META_RE = re.compile(r'<meta\s+content="[^"]*"\s+name="specification-version"\s*/?>', re.I)
GLOSSARY_ASSIGN_RE = re.compile(r"const glossary = .*?;\n\s*const tooltip =", re.S)
HEAD_CLOSE_RE = re.compile(r"</head>", re.I)


def render_data_fingerprint(data: dict) -> str:
    canonical = json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def script_safe_json(value: Any) -> str:
    """Serialize JSON for direct insertion into a classic HTML <script> block."""
    text = json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
    return (
        text.replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def validate_aliases(aliases: Any, context: str) -> None:
    if aliases is None:
        return
    if isinstance(aliases, list):
        if not all(isinstance(alias, str) for alias in aliases):
            raise ValueError(f"{context}.aliases must be an array of strings")
        return
    if isinstance(aliases, dict):
        supported = [language for language in ("en", "id") if language in aliases]
        if not supported:
            raise ValueError(f"{context}.aliases object must define en and/or id")
        for language in supported:
            values = aliases[language]
            if not isinstance(values, list) or not all(isinstance(alias, str) for alias in values):
                raise ValueError(f"{context}.aliases.{language} must be an array of strings")
        return
    raise ValueError(f"{context}.aliases must be an array of strings or an en/id object")


def validate(data: dict) -> None:
    if not isinstance(data, dict):
        raise ValueError("render data root must be an object")
    if not isinstance(data.get("document"), dict) or not txt(data["document"].get("title"))["en"].strip():
        raise ValueError("document.title is required")
    if not isinstance(data.get("overview"), dict):
        raise ValueError("overview is required")

    collections: dict[str, list[dict[str, Any]]] = {}
    for key in ("gameplay_flow", "global_development", "packages"):
        raw = data.get(key, [])
        if not isinstance(raw, list):
            raise ValueError(f"{key} must be an array")
        items: list[dict[str, Any]] = []
        for index, item in enumerate(raw):
            if not isinstance(item, dict):
                raise ValueError(f"{key}[{index}] must be an object")
            item_id = item.get("id")
            if not isinstance(item_id, str) or not ID_RE.fullmatch(item_id):
                raise ValueError(f"{key}[{index}] has invalid stable id: {item_id!r}")
            items.append(item)
        collections[key] = items

    packages = collections["packages"]
    pids = [pkg["id"] for pkg in packages]
    if len(pids) != len(set(pids)):
        raise ValueError("Duplicate package id")

    for pkg in packages:
        for key in ("gameplay", "level_design", "developer"):
            if not isinstance(pkg.get(key), dict):
                raise ValueError(f'Package {pkg["id"]} requires {key}')
        if not pkg["developer"].get("scoring") and not pkg["developer"].get("completion_data"):
            raise ValueError(f'Package {pkg["id"]} developer requires scoring or completion_data')

        terms = pkg.get("terms", [])
        if not isinstance(terms, list):
            raise ValueError(f'Package {pkg["id"]}.terms must be an array')
        for index, term in enumerate(terms):
            if not isinstance(term, dict):
                raise ValueError(f'Package {pkg["id"]}.terms[{index}] must be an object')
            validate_aliases(term.get("aliases"), f'Package {pkg["id"]}.terms[{index}]')

    if OPEN_RE.search(json.dumps(data, ensure_ascii=False)):
        raise ValueError("Render data contains unresolved placeholder text")


def require_exact_once(src: str, marker: str, label: str) -> None:
    count = src.count(marker)
    if count != 1:
        raise ValueError(f"Template requires exactly one {label}; found {count}")


def replace_regex_once(src: str, pattern: re.Pattern[str], replacement: str, label: str) -> str:
    matches = list(pattern.finditer(src))
    if len(matches) != 1:
        raise ValueError(f"Template requires exactly one {label}; found {len(matches)}")
    return pattern.sub(lambda _: replacement, src, count=1)


def element_range(src: str, marker: str, tag: str, label: str) -> tuple[int, int]:
    require_exact_once(src, marker, label)
    start = src.find(marker)
    open_end = src.find(">", start) + 1
    depth = 0
    for match in re.finditer(rf"</?{tag}\b[^>]*>", src[start:], re.I):
        depth += -1 if match.group(0).startswith("</") else 1
        if depth == 0:
            return open_end, start + match.start()
    raise ValueError(f"Closing tag not found for {label}")


def replace_inner(src: str, marker: str, tag: str, inner: str, label: str) -> str:
    a, b = element_range(src, marker, tag, label)
    return src[:a] + inner + src[b:]


def require_namespace_tokens(src: str) -> None:
    for token, label in (
        ("aftershock-document-", "document local-storage namespace token"),
        ("aftershock-sidebar-collapsed", "sidebar local-storage namespace token"),
    ):
        if token not in src:
            raise ValueError(f"Template missing required {label}: {token}")


def render(template: Path, render_data: Path, output: Path) -> None:
    if not template.is_file():
        raise FileNotFoundError(f"Approved template not found: {template}")
    data = json.loads(render_data.read_text(encoding="utf-8"))
    validate(data)
    fingerprint = render_data_fingerprint(data)
    src = template.read_text(encoding="utf-8")
    require_namespace_tokens(src)

    pages = [overview(data)] + flow_pages(data) + global_pages(data) + package_pages(data)
    nav = navigation(data)

    title = txt(data["document"]["title"])
    mark = str(data["document"].get("brand_mark") or title["en"][:1] or "P").upper()
    brand = (
        f'<a aria-label="{esc(title["en"])} overview" class="sidebar-brand" href="#summary">'
        f'<span class="brand-mark">{i18n(mark)}</span>'
        f'<span class="brand-copy"><strong>{i18n(title)}</strong>'
        f'<small>{i18n(data["document"].get("document_type", "Production Specification"))}</small></span></a>'
    )
    src = replace_regex_once(src, SIDEBAR_BRAND_RE, brand, "sidebar brand marker")
    src = replace_inner(src, '<nav class="sidebar-nav">', "nav", nav, "sidebar navigation marker")
    src = replace_inner(src, '<main class="document-main">', "main", "".join(pages), "document main marker")

    glossary_json = script_safe_json(glossary(data))
    src = replace_regex_once(
        src,
        GLOSSARY_ASSIGN_RE,
        f"const glossary = {glossary_json};\n  const tooltip =",
        "glossary script assignment marker",
    )

    doc = data["document"]
    namespace = slug(title["en"])
    page_title = f'{title["en"]} — {txt(doc.get("subtitle", "Production Specification"))["en"]}'
    src = replace_regex_once(src, TITLE_RE, f"<title>{esc(page_title)}</title>", "document title marker")

    desc = txt(doc.get("description") or data["overview"].get("project_context") or page_title)["en"]
    src = replace_regex_once(
        src,
        DESCRIPTION_META_RE,
        f'<meta content="{esc(desc)}" name="description"/>',
        "description metadata marker",
    )
    src = replace_regex_once(
        src,
        SPEC_VERSION_META_RE,
        f'<meta content="prd-{namespace}-v{esc(doc.get("version", "1.0"))}" name="specification-version"/>',
        "specification-version metadata marker",
    )

    revision_meta = f'<meta content="{fingerprint}" name="render-data-sha256"/>'
    src = replace_regex_once(
        src,
        HEAD_CLOSE_RE,
        revision_meta + "\n</head>",
        "head closing marker",
    )

    src = src.replace("aftershock-document-", f"prd-{namespace}-")
    src = src.replace("aftershock-sidebar-collapsed", f"prd-{namespace}-sidebar-collapsed")

    ids = set(re.findall(r'<section\b[^>]*\bid="([^"]+)"', src))
    targets = set(re.findall(r'data-target="([^"]+)"', nav))
    missing = sorted(targets - ids)
    if missing:
        raise ValueError(f"Navigation targets missing from generated pages: {missing}")
    if OPEN_RE.search("".join(pages)):
        raise ValueError("Generated pages contain unresolved placeholders")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(src, encoding="utf-8")


def main() -> int:
    default = HERE.parent / "template" / "approved-document.html"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("render_data", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--template", type=Path, default=default)
    args = parser.parse_args()
    try:
        render(args.template, args.render_data, args.output)
        print(args.output)
        return 0
    except (OSError, ValueError) as exc:
        print(f"PRD RENDER FAILED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
