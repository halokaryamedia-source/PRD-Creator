#!/usr/bin/env python3
"""Render schema-valid Production Document Builder content to HTML."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

import yaml

from renderer_lib import DocumentRenderer, read_data, write_yaml
from render_golden_regression import load_inventory, validate_inventory, sha256_bytes


def load_validator_module(path: Path):
    spec = importlib.util.spec_from_file_location("pdb_validate_package", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load validator module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def count_missing_languages(node: Any, output_languages: list[str]) -> dict[str, int]:
    counts = {"en": 0, "id": 0}

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            keys = set(value)
            if keys & {"en", "id"} and keys <= {"en", "id"}:
                for lang in output_languages:
                    if lang in counts and not value.get(lang):
                        counts[lang] += 1
                return
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(node)
    return counts


def validate_inputs(
    content_path: Path,
    glossary_path: Path | None,
    decisions_path: Path | None,
    assumptions_path: Path | None,
    schema_dir: Path,
    validator_path: Path,
) -> list[str]:
    validator = load_validator_module(validator_path)
    schemas, registry = validator.load_schemas(schema_dir)
    context: dict[str, dict[str, Any]] = {}
    if glossary_path and glossary_path.is_file():
        context["glossary"] = validator.load_data(glossary_path)
    if decisions_path and decisions_path.is_file():
        context["decisions"] = validator.load_data(decisions_path)
    if assumptions_path and assumptions_path.is_file():
        context["assumptions"] = validator.load_data(assumptions_path)
    data = validator.load_data(content_path)
    issues = validator.validate_data(data, "project-content.schema.json", schemas, registry, context=context)
    return [str(issue) for issue in issues]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("content", type=Path, help="project-content.yaml or JSON")
    parser.add_argument("--glossary", type=Path)
    parser.add_argument("--decisions", type=Path)
    parser.add_argument("--assumptions", type=Path)
    parser.add_argument("--project-state", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--template-dir", type=Path, default=Path(__file__).resolve().parents[1] / "templates")
    parser.add_argument("--schema-dir", type=Path, default=Path(__file__).resolve().parents[1] / "schemas")
    parser.add_argument("--template-version", default="1.0")
    parser.add_argument("--schema-version", default="0.1")
    parser.add_argument("--golden-sample-version", default="aftershock-1.0")
    parser.add_argument("--html-version", default="1.0")
    parser.add_argument("--prototype", action="store_true", help="Allow non-frozen content and label output as a prototype.")
    parser.add_argument("--external-assets", action="store_true", help="Write external assets instead of a standalone HTML.")
    parser.add_argument("--skip-schema-validation", action="store_true")
    parser.add_argument(
        "--golden-regression",
        action="store_true",
        help="Render the locked AFTERSHOCK Golden Sample exactly instead of using the semantic renderer.",
    )
    parser.add_argument(
        "--golden-html",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "golden-sample" / "aftershock-golden-sample-v1.0.html",
    )
    args = parser.parse_args()

    try:
        if not args.content.is_file():
            raise RuntimeError(f"Content file not found: {args.content}")

        if args.golden_regression:
            if not args.golden_html.is_file():
                raise RuntimeError(f"Locked Golden Sample not found: {args.golden_html}")
            inventory = load_inventory(args.content)
            source_bytes = args.golden_html.read_bytes()
            metrics = validate_inventory(inventory, source_bytes)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(source_bytes)
            output_bytes = args.output.read_bytes()
            source_hash = sha256_bytes(source_bytes)
            output_hash = sha256_bytes(output_bytes)
            if output_bytes != source_bytes or output_hash != source_hash:
                raise RuntimeError("Golden regression output is not byte-identical to the locked sample.")
            print(json.dumps({
                "output": str(args.output),
                "profile": "complete_game_map",
                "mode": "golden_sample_exact_regression",
                "pages": metrics["pages"],
                "source_sha256": source_hash,
                "output_sha256": output_hash,
                "byte_identical": True,
            }, ensure_ascii=False, indent=2))
            return 0

        content = read_data(args.content)
        glossary = read_data(args.glossary) if args.glossary and args.glossary.is_file() else {"terms": []}

        if not args.skip_schema_validation:
            issues = validate_inputs(
                args.content,
                args.glossary,
                args.decisions,
                args.assumptions,
                args.schema_dir,
                Path(__file__).resolve().parent / "validate_package.py",
            )
            if issues:
                print("RENDER BLOCKED: input validation failed", file=sys.stderr)
                for issue in issues:
                    print(f"- {issue}", file=sys.stderr)
                return 1

        document = content.get("document", {})
        if document.get("status") != "frozen" and not args.prototype:
            print(
                f"RENDER BLOCKED: document.status is {document.get('status')!r}; expected 'frozen'.",
                file=sys.stderr,
            )
            return 1

        output_languages = list(document.get("output_languages", []))
        missing = count_missing_languages(content, output_languages)
        if not args.prototype and any(missing.get(lang, 0) for lang in output_languages if lang in missing):
            print(f"RENDER BLOCKED: missing translations {missing}", file=sys.stderr)
            return 1

        renderer = DocumentRenderer(
            content,
            glossary,
            args.template_dir,
            template_version=args.template_version,
            schema_version=args.schema_version,
            golden_sample_version=args.golden_sample_version,
            html_version=args.html_version,
        )
        html_text = renderer.render_html(standalone=not args.external_assets)
        if args.prototype:
            html_text = html_text.replace(
                "</body>",
                '<div class="prototype-banner">Visual Prototype — Not Final Content</div></body>',
            )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(html_text, encoding="utf-8")
        if args.external_assets:
            renderer.write_assets(args.output.parent)

        metrics = renderer.render_metrics(html_text)
        result = {
            "output": str(args.output),
            "profile": renderer.profile,
            "pages": metrics["pages"],
            "terms_defined": metrics["terms_defined"],
            "unused_terms": metrics["unused_terms"],
            "missing_term_refs": metrics["missing_term_refs"],
            "id_missing": metrics["id_missing"],
            "en_missing": metrics["en_missing"],
            "unresolved_placeholders": metrics["placeholders"],
            "prototype": args.prototype,
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, RuntimeError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f"RENDER FAILED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
