from __future__ import annotations

import re

from .core import esc

SIDEBAR_BRAND_RE = re.compile(
    r'<a\s+aria-label="[^"]* overview"\s+class="sidebar-brand"\s+href="#summary">.*?</a>',
    re.S,
)
TITLE_RE = re.compile(r"<title>.*?</title>", re.S | re.I)
DESCRIPTION_META_RE = re.compile(r'<meta\s+content="[^"]*"\s+name="description"\s*/?>', re.I)
SPEC_VERSION_META_RE = re.compile(r'<meta\s+content="[^"]*"\s+name="specification-version"\s*/?>', re.I)
GLOSSARY_ASSIGN_RE = re.compile(r"const glossary = .*?;\n\s*const tooltip =", re.S)
HTML_TAG_RE = re.compile(r"<html\b[^>]*>", re.I)

# Legacy identifiers are quarantined here because the approved Golden shell is byte-locked.
# Generic renderer modules must not depend on reference-project vocabulary.
_REFERENCE_SPEC_MARKER = "aftershock-v0.2"
_REFERENCE_META_NAMES = (
    "golden-sample-id",
    "golden-sample-version",
    "source-document",
    "template-extraction-version",
)
_REFERENCE_STORAGE_KEYS = {
    "aftershock-document-theme": "document-theme",
    "aftershock-document-view": "document-view",
    "aftershock-document-language": "document-language",
    "aftershock-sidebar-collapsed": "sidebar-collapsed",
}


class TemplateAdapter:
    """The one mutation boundary for the byte-locked Golden HTML shell."""

    def __init__(self, source: str) -> None:
        self.source = source

    @classmethod
    def prepare_reference_shell(
        cls,
        source: str,
        *,
        namespace: str,
        runtime_token: str,
    ) -> "TemplateAdapter":
        """Convert the exact historical Golden artifact into the generic runtime shell.

        This is the only location allowed to know the retained reference-project marker
        and localStorage keys. It changes presentation plumbing only; no project content.
        """

        for meta_name in _REFERENCE_META_NAMES:
            source = re.sub(
                rf'<meta\b[^>]*\bname=["\']{re.escape(meta_name)}["\'][^>]*>\s*',
                "",
                source,
                flags=re.I,
            )
        for old_key, suffix in _REFERENCE_STORAGE_KEYS.items():
            source = source.replace(old_key, f"prd-{namespace}-{suffix}")
        if source.count(_REFERENCE_SPEC_MARKER) != 1:
            raise ValueError(
                "Approved Golden reference must contain exactly one retained specification marker"
            )
        source = source.replace(_REFERENCE_SPEC_MARKER, runtime_token, 1)
        return cls(source)

    def require_once(self, marker: str, label: str) -> None:
        count = self.source.count(marker)
        if count != 1:
            raise ValueError(f"Template requires exactly one {label}; found {count}")

    def replace_regex_once(self, pattern: re.Pattern[str], replacement: str, label: str) -> None:
        matches = list(pattern.finditer(self.source))
        if len(matches) != 1:
            raise ValueError(f"Template requires exactly one {label}; found {len(matches)}")
        self.source = pattern.sub(lambda _: replacement, self.source, count=1)

    def replace_inner(self, marker: str, tag: str, inner: str, label: str) -> None:
        start, end = self._element_range(marker, tag, label)
        self.source = self.source[:start] + inner + self.source[end:]

    def set_document_languages(self, languages: list[str]) -> None:
        matches = list(HTML_TAG_RE.finditer(self.source))
        if len(matches) != 1:
            raise ValueError(f"Template requires exactly one html tag; found {len(matches)}")
        opening = matches[0].group(0)
        if "data-document-languages=" in opening:
            raise ValueError("Template html tag must not define project language availability")
        language_value = ",".join(languages)
        updated = opening[:-1] + f' data-document-languages="{esc(language_value)}">'
        self.source = self.source[: matches[0].start()] + updated + self.source[matches[0].end() :]

    def set_sidebar_brand(self, html: str) -> None:
        self.replace_regex_once(SIDEBAR_BRAND_RE, html, "sidebar brand marker")

    def set_navigation(self, html: str) -> None:
        self.replace_inner('<nav class="sidebar-nav">', "nav", html, "sidebar navigation marker")

    def set_document_main(self, html: str) -> None:
        self.replace_inner('<main class="document-main">', "main", html, "document main marker")

    def set_glossary_assignment(self, json_text: str) -> None:
        self.replace_regex_once(
            GLOSSARY_ASSIGN_RE,
            f"const glossary = {json_text};\n  const tooltip =",
            "glossary script assignment marker",
        )

    def set_title(self, title: str) -> None:
        self.replace_regex_once(TITLE_RE, f"<title>{esc(title)}</title>", "document title marker")

    def set_description(self, description: str) -> None:
        self.replace_regex_once(
            DESCRIPTION_META_RE,
            f'<meta content="{esc(description)}" name="description"/>',
            "description metadata marker",
        )

    def set_specification_version(self, value: str) -> None:
        self.replace_regex_once(
            SPEC_VERSION_META_RE,
            f'<meta content="{esc(value)}" name="specification-version"/>',
            "specification-version metadata marker",
        )

    def replace_token(self, token: str, value: str, label: str) -> None:
        self.require_once(token, label)
        self.source = self.source.replace(token, value, 1)

    def inject_head(self, html: str) -> None:
        self.require_once("</head>", "head closing marker")
        self.source = self.source.replace("</head>", html + "\n</head>", 1)

    def inject_body(self, html: str) -> None:
        self.require_once("</body>", "body closing marker")
        self.source = self.source.replace("</body>", html + "\n</body>", 1)

    def _element_range(self, marker: str, tag: str, label: str) -> tuple[int, int]:
        self.require_once(marker, label)
        start = self.source.find(marker)
        open_end = self.source.find(">", start) + 1
        depth = 0
        for match in re.finditer(rf"</?{tag}\b[^>]*>", self.source[start:], re.I):
            depth += -1 if match.group(0).startswith("</") else 1
            if depth == 0:
                return open_end, start + match.start()
        raise ValueError(f"Closing tag not found for {label}")
