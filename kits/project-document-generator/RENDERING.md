# Rendering Contract

The Approved Template is the presentation authority. Flow 3 must adapt project content without redesigning the shared visual system.

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
output/final.html                  presentation artifact
```

`render-data.json` is not a second PRD. It exists only because deterministic HTML rendering needs structured page data. If `content.md` changes, regenerate the projection before rendering.

The renderer also embeds a deterministic SHA-256 fingerprint of the current render-data into `final.html`. Flow 4 mechanical validation uses that fingerprint only to prove **current projection → current HTML** freshness; it does not prove that the projection is semantically equivalent to canonical `content.md`.

## What the renderer preserves

The renderer clones the approved HTML and preserves its shared:

- `<head>` presentation assets;
- CSS and class vocabulary;
- JavaScript behavior;
- theme control;
- language control;
- View Mode;
- sidebar shell;
- responsive behavior;
- print behavior;
- glossary tooltip implementation;
- shared page/component styling.

The renderer does **not** reconstruct the presentation system from scratch.

## What the renderer may replace

Only project-owned content surfaces:

- browser/document title and project metadata;
- sidebar project brand text;
- navigation entries and targets;
- generated document pages inside `.document-main`;
- project glossary data used by the inherited tooltip script;
- project-specific local-storage namespace;
- generated `render-data-sha256` revision metadata.

Inherited internal class names such as `quarry-*` may remain because they are part of the approved template's presentation vocabulary. They do not make Quarry content a requirement for another project.

## Rendering projection

`render-data.json` uses a compact structure:

```json
{
  "document": {
    "title": {"en": "Project", "id": "Project"},
    "subtitle": {"en": "Gameplay & Development Specification", "id": "Spesifikasi Gameplay & Pengembangan"},
    "document_type": {"en": "Adventure Map", "id": "Map Petualangan"},
    "version": "1.0"
  },
  "overview": {},
  "gameplay_flow": [],
  "global_development": [],
  "packages": []
}
```

Text fields may be a string or `{ "en": "...", "id": "..." }`. When only one language is available, the renderer mirrors it as a presentation fallback; Flow 4 decides whether requested language coverage is acceptable for delivery.

### `gameplay_flow[]`

Each entry requires a stable lowercase kebab-case `id` and may contain:

- `title`;
- `narrative_context`;
- `player_experience`;
- `main_obstacle_or_change`;
- `player_result`;
- `next_destination`;
- `terms`.

### `global_development[]`

Each entry requires `id`, `title`, and `overview`, with optional:

- `flow[]`;
- grouped `requirements[]`;
- `notes[]`;
- `terms[]`.

### `packages[]`

Each package requires:

- stable `id`;
- `title`;
- `package_label` (Introduction, Objective N, Ending, Stage N, etc.);
- `gameplay` object;
- `level_design` object;
- `developer` object;
- optional `estimated_time`;
- optional `terms[]`.

The renderer creates A/B/C pages for each package and regenerates the matching sidebar hierarchy automatically.

### Package glossary aliases

Package `terms[]` feed both visible Terms Used content and the inherited glossary tooltip runtime.

When `aliases` is supplied, use only one of the supported shapes:

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

The `en`/`id` object may provide one or both languages, but every supplied language value must be an array of strings. Malformed alias shapes are rejected before rendering rather than being allowed to fail later in browser JavaScript.

## Script-context safety

Glossary data is inserted into an executable classic `<script>` block. The renderer must serialize that JSON for **script context**, not merely ordinary JSON context.

At minimum, serialized glossary text escapes characters that could terminate or alter the enclosing script context, including literal `<`, `>`, `&`, U+2028, and U+2029. Project text such as `</script>` must therefore remain data and must never create a new executable script boundary.

This is a mechanical rendering-safety rule. It is not a general HTML sanitizer and does not authorize arbitrary user-authored HTML/JavaScript in project content.

## Approved shell marker contract

The renderer mutates a small required set of approved-shell surfaces. Each unique marker must exist exactly once where uniqueness is required; missing or ambiguous markers fail the render instead of being ignored.

Required unique surfaces include:

- sidebar brand anchor;
- `<nav class="sidebar-nav">`;
- `<main class="document-main">`;
- glossary JavaScript assignment anchor;
- document `<title>`;
- description metadata;
- specification-version metadata;
- closing `</head>` insertion point.

The approved shell must also retain the inherited local-storage namespace tokens that the renderer replaces with the current project namespace.

Do not expand this into a full-template snapshot contract. CSS/layout/content elsewhere in the approved shell remains presentation authority and is reviewed visually when that evidence level is required.

## Renderer input checks

The renderer blocks when:

- required root structures are missing;
- stable IDs are invalid;
- package IDs are duplicated;
- a package does not contain Gameplay, Level Design, and Developer objects;
- Developer contains neither scoring nor completion data;
- package glossary aliases use a shape unsupported by the runtime;
- visible unresolved placeholder tokens remain;
- generated navigation points to a page that does not exist;
- the approved template shell markers cannot be found exactly as required.

These are rendering safety checks, not a substitute for Flow 4 content/development-readiness validation.

## Renderer command

From repository root:

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

An alternate approved template may be supplied only when the current task explicitly selects it:

```bash
python kits/project-document-generator/renderer/render.py \
  <render-data.json> <final.html> \
  --template <approved-template.html>
```

Renderer contract failures return a controlled non-zero CLI result. A failed render must not be reported as a valid generated artifact.

## Important boundary

The renderer may organize approved content into existing Golden Sample component families, but it may never:

- invent missing project facts;
- resolve Proposal/Blocked decisions;
- change scoring or completion meaning;
- add a mechanic because the Golden Sample has one;
- remove required content because it does not fit nicely;
- patch `final.html` as the source of truth.

If the rendered output exposes a content problem, fix `content.md`, regenerate `render-data.json`, and render again. If it exposes a shared presentation problem, treat that as a template/renderer issue rather than hiding it in project content.
