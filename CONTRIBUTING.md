# Contributing

## Change Types

Classify every change before editing:

- **Content change** — modifies production-document meaning or approved requirements.
- **Template change** — modifies shared visual or interaction behavior.
- **Schema change** — modifies required structured fields or validation rules.
- **Renderer change** — modifies mapping from structured content to HTML.
- **Golden Sample change** — replaces the official approved benchmark.

## Required Checks

Before merging a change:

```bash
python tests/run_schema_tests.py
python tests/run_renderer_tests.py
python tests/run_golden_regression_test.py
python tests/run_acceptance_tests.py
```

A release is blocked by any Critical or Major finding.

## Golden Sample

The approved AFTERSHOCK Golden Sample is locked. Do not edit it as an ordinary template file. Changes require:

1. documented rationale;
2. explicit approval;
3. Golden Sample version update;
4. exact regression baseline update;
5. acceptance test rerun.

## Releases

ChatGPT-ready ZIP files belong in `releases/`. Keep the matching `.sha256` file beside each archive.
