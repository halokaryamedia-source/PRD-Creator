# Rendering Contract

The approved Golden Sample is the presentation and document-structure authority for this PRD family. It is intentionally preserved because it defines the output style, layout behavior, section foundation, navigation behavior, and component vocabulary the user wants future projects to reproduce.

Do **not** treat the Golden Sample as legacy baggage that should be reduced into a different minimal template.

## Rendering model

```text
work/content.md                    canonical project meaning
        ↓
work/render-data.json              derived rendering projection
        ↓
template/approved-document.html    approved Golden Sample template authority
        ↓
renderer/render.py
        ↓
output/final.html                  derived project document
```

`render-data.json` and `final.html` are derived. When canonical content changes, regenerate the projection and render again. Do not add a second revision/checksum protocol just to track derived files.

## Golden Sample preservation rule

For this document family, preserve the Golden Sample foundation unless the user explicitly approves a different template family.

This includes the approved behavior and visual foundation such as:

- overall document hierarchy and page rhythm;
- Overview / Gameplay Flow / Global Development / Gameplay Package organization;
- Gameplay Overview → Level Design → Developer package structure;
- sidebar/navigation behavior;
- shared typography, spacing, colors, tables, cards, callouts, tabs, glossary interactions, controls, responsive behavior, and print behavior;
- bilingual interaction behavior when the project supplies the relevant language content;
- the established visual density and professional presentation style.

Efficiency work must focus on **how project content is produced and projected into this template**, not on redesigning, extracting, or pruning the Golden Sample simply to make the template file smaller.

A template cleanup is justified only when there is a proven template defect that changes or breaks the approved output. File size or unused-looking CSS alone is not a product defect.

## What the renderer may replace

Only project-owned content surfaces:

- browser/document title and project metadata;
- sidebar project brand text;
- navigation entries and targets;
- generated document pages inside `.document-main`;
- project glossary data used by the inherited tooltip script;
- project-specific local-storage namespace.

The renderer must preserve the Golden Sample's approved shared structure and behavior while replacing project-specific meaning.

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

Each generated collection item uses a stable lowercase kebab-case `id`.

Each gameplay package preserves the approved three-role structure:

```text
gameplay
level_design
developer
```

Developer data uses scoring for a scoring package or completion data for a non-scoring package according to the content contract. Do not use these surfaces to invent metrics or persistence that the project does not require.

## Projection efficiency

`render-data.json` should be produced as part of the BUILD PRD step, not treated as a separate user-facing phase.

Projection rules:

- copy only meaning already present in canonical `content.md`;
- omit empty optional rows/components where the renderer supports omission;
- do not repeat a global rule in full when the local page only needs its local implication;
- do not add text merely to fill Golden Sample visual space;
- preserve the fixed page/role structure while keeping local content concise where appropriate.

The renderer may organize approved content into existing component families, but it may never invent missing project facts, resolve open decisions, change scoring/completion meaning, or patch `final.html` as the source of truth.

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

## Approved template mechanics

The renderer checks only template surfaces it actually mutates. Required unique surfaces include:

- sidebar brand anchor;
- `<nav class="sidebar-nav">`;
- `<main class="document-main">`;
- glossary JavaScript assignment anchor;
- document `<title>`;
- description metadata;
- specification-version metadata.

The inherited local-storage namespace tokens used by the approved template must also remain available for project namespacing.

Do not expand this into a full-template snapshot or attempt to normalize the Golden Sample into a different visual system.

## Renderer checks

The renderer blocks on concrete invalid input such as:

- missing required root structures;
- invalid/duplicate stable IDs;
- missing package role objects required by the Golden Sample structure;
- missing scoring/completion data where the document contract requires it;
- unsupported glossary alias shape;
- unresolved placeholder tokens;
- broken generated navigation targets;
- missing/ambiguous template markers that the renderer must mutate.

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

Use an alternate template only when that template is explicitly approved for the project/document family.

## Boundary

If content changes, fix canonical content/projection and render again. If shared presentation mechanics fail, fix the template/renderer owner.

Keep the user-facing process simple:

```text
canonical PRD
→ derive projection internally
→ render through Golden Sample
→ validate
```

Do not simplify the process by changing the final Golden Sample foundation the user expects.
