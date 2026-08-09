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
- project-specific local-storage namespace.

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

## Renderer input checks

The renderer blocks when:

- required root structures are missing;
- stable IDs are invalid;
- package IDs are duplicated;
- a package does not contain Gameplay, Level Design, and Developer objects;
- Developer contains neither scoring nor completion data;
- visible unresolved placeholder tokens remain;
- generated navigation points to a page that does not exist;
- the approved template shell markers cannot be found deterministically.

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

## Important boundary

The renderer may organize approved content into existing Golden Sample component families, but it may never:

- invent missing project facts;
- resolve Proposal/Blocked decisions;
- change scoring or completion meaning;
- add a mechanic because the Golden Sample has one;
- remove required content because it does not fit nicely;
- patch `final.html` as the source of truth.

If the rendered output exposes a content problem, fix `content.md`, regenerate `render-data.json`, and render again. If it exposes a shared presentation problem, treat that as a template/renderer issue rather than hiding it in project content.
