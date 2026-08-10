# Rendering Contract

The Approved Template is the presentation authority. Flow 3 adapts project content without redesigning the shared visual system.

## Rendering model

```text
work/content.md                    canonical project meaning
        ↓
work/render-data.json              derived rendering projection
        ↓
template/approved-document.html    approved presentation shell
        ↓
renderer/render.py
        ↓
output/final.html                  derived presentation artifact
```

`render-data.json` and `final.html` are derived. When canonical content changes, regenerate the projection and render again. Do not add a second revision/checksum protocol just to track derived files.

## What the renderer may replace

Only project-owned content surfaces:

- browser/document title and project metadata;
- sidebar project brand text;
- navigation entries and targets;
- generated document pages inside `.document-main`;
- project glossary data used by the inherited tooltip script;
- project-specific local-storage namespace.

The renderer preserves the approved template's CSS, JavaScript behavior, responsive/print behavior, controls, and shared component vocabulary.

## Basic input contract

`render-data.json` contains:

```json
{
  "document": {},
  "overview": {},
  "gameplay_flow": [],
  "global_development": [],
  "packages": []
}
```

Each generated collection item uses a stable lowercase kebab-case `id`. Each gameplay package contains `gameplay`, `level_design`, and `developer`. Developer data must provide scoring or completion data as required by the current document contract.

## Glossary safety

Package `terms[]` may define aliases as either:

```json
["Alias One", "Alias Two"]
```

or:

```json
{
  "en": ["English Alias"],
  "id": ["Alias Indonesia"]
}
```

Malformed alias shapes fail before rendering.

Glossary data is inserted into an executable `<script>` block, so the renderer serializes it safely for script context. Literal `<`, `>`, `&`, U+2028, and U+2029 are escaped; project text such as `</script>` remains data.

This is a focused script-safety rule, not a general sanitizer framework.

## Approved shell contract

The renderer only checks shell markers that it actually mutates. Required unique surfaces include:

- sidebar brand anchor;
- `<nav class="sidebar-nav">`;
- `<main class="document-main">`;
- glossary JavaScript assignment anchor;
- document `<title>`;
- description metadata;
- specification-version metadata.

The inherited local-storage namespace tokens used by the approved shell must also remain available for project namespacing.

Do not expand this into a full-template snapshot contract.

## Renderer checks

The renderer blocks on concrete invalid input such as:

- missing required root structures;
- invalid/duplicate stable IDs;
- missing package role objects;
- missing scoring/completion data where required;
- unsupported glossary alias shape;
- unresolved placeholder tokens;
- broken generated navigation targets;
- missing/ambiguous shell markers that the renderer must mutate.

These checks protect generation mechanics. They do not replace Flow 4 semantic review or browser visual QA.

## Commands

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

Optional alternate approved template:

```bash
python kits/project-document-generator/renderer/render.py \
  <render-data.json> <final.html> \
  --template <approved-template.html>
```

## Boundary

The renderer may organize approved content into existing component families, but it may never invent missing project facts, resolve open decisions, change scoring/completion meaning, or patch `final.html` as the source of truth.

If content changes, fix canonical content/projection and render again. If shared presentation mechanics fail, fix the template/renderer owner. Keep the flow simple: **input → render → validate**.
