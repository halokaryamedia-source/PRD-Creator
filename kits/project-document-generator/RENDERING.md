# Rendering Contract

The approved Golden Sample is the presentation and page-composition authority for this PRD family. The renderer reproduces that document language with project-specific facts; it does not redesign the document.

## Normal production path

```text
work/content.md                    canonical meaning
→ work/render-data.json            compact derived projection bound to current content
→ renderer                         deterministic HTML composition
→ template/approved-document.html  Golden runtime input
→ output/final.html                derived PRD
```

The template and final HTML are runtime artifacts. **Normal authoring does not require loading either large file into model context.**

Use `CONTENT-CONTRACT.md` for the Golden hierarchy/page-composition meaning. Use this file only for projection and renderer rules.

## Context-efficient HTML generation

- Do not hand-author or patch `final.html`.
- Do not copy Golden HTML/CSS/JS into prompts, notes, or canonical content.
- Do not read `approved-document.html` in full during normal project production; the renderer reads it directly at runtime.
- Do not read `final.html` in full merely to review semantics; the mechanical validator reads it directly.
- When HTML source investigation is necessary, search for the exact page ID/class/marker/component and inspect only the smallest relevant area.
- For visual quality, inspect the actual rendered page/browser when available rather than treating source review as visual proof.

## Projection economy

`render-data.json` is a structured projection, not a second semantic document.

Root shape:

```json
{
  "canonical_content_sha256": "<sha256 of current work/content.md>",
  "document": {},
  "overview": {},
  "gameplay_flow": [],
  "global_development": [],
  "packages": []
}
```

`canonical_content_sha256` is derived revision binding only. When the projection is written or regenerated, calculate SHA-256 over the exact bytes of the current `work/content.md` and store the lowercase 64-character digest. It does not carry project meaning. Flow 4 rejects a missing/invalid digest or a digest that no longer matches canonical content, so an older projection cannot silently validate after `content.md` changes.

Each package keeps `gameplay`, `level_design`, and `developer`.

Initial production should project once after canonical content is stable enough to render. During a bounded revision, change only the affected subtree plus required cross-references and refresh `canonical_content_sha256`; do not recreate unchanged packages.

Do not copy commentary/provenance/internal reasoning into render data. Carry only values required by the Golden surfaces plus the canonical-content revision binding above.

## Compact value conventions

### English-only

Default document language is:

```json
"languages": ["en"]
```

Use scalar strings for ordinary English values when there is no bilingual output requirement:

```json
"title": "Core Trial"
```

Do not expand this into duplicated localized data merely for renderer symmetry:

```json
{"en": "Core Trial", "id": "Core Trial"}
```

unless the value is intentionally represented as localized content.

### Bilingual

For intentional EN + ID output:

```json
"languages": ["en", "id"]
```

Every user-visible textual value must use an explicit localized object containing both values. Missing translations and ordinary scalar display text fail before rendering; the renderer does not silently copy English into Indonesian.

If a displayed proper name is intentionally unchanged, make that intent explicit:

```json
{"en": "Core Trial", "id": "Core Trial"}
```

Scalar strings remain valid only for renderer-defined non-linguistic/structural values: stable `id`/`key`/`code`, version/brand mark, language/role tokens, numeric scoring weight, step/row identifiers, `canonical_content_sha256`, and an exact formula. Numeric/boolean values remain unchanged.

This is a strict language-availability contract, not a translation framework.

## Role-specific Terms Used

Package terms remain one glossary/tooltips source.

Optional `roles` values are:

```text
gameplay
level_design
developer
```

- omitted `roles` → visible on Gameplay Overview only;
- explicit roles → visible only on those pages;
- `roles: []` → glossary/tooltips only.

Omit role metadata when default Gameplay visibility is correct. Do not repeat every package term across all role pages.

## Content-driven Golden grids

Golden component language stays fixed while item distribution follows actual content.

- Overview Journey: one desktop column per item up to six; items beyond six wrap to later rows with an explicit row separator and no false left-edge divider on the first item of each wrapped row.
- Golden Flow cards: one desktop column per item up to four; items beyond four use the same wrapped-row separator/reset behavior.
- Existing Golden mobile behavior remains authoritative.

This uses bounded CSS variables/selectors only; do not create layout profiles, scoring, or another responsive system. Static contract proof can verify the wrap mechanics exist, but actual visual fidelity still requires rendered/browser inspection.

## Renderer ownership

- `renderer/core.py` → reusable Golden helpers.
- `renderer/pages.py` → project data → Golden page composition.
- `renderer/render.py` → validation of render-data boundary, template mutation, project metadata/navigation/glossary/language/grid mechanics, final write.
- `template/approved-document.html` → edit only when a proven defect belongs to the Golden template itself.

The renderer may omit optional blocks with no meaningful project data. It may not invent facts or replace Golden composition with unrelated generic markup.

## Template mutation boundary

The renderer may mutate only project-owned surfaces already required by this document family:

- project title/metadata/brand;
- navigation;
- generated pages inside `.document-main`;
- glossary data;
- project local-storage namespace;
- bounded language availability;
- bounded content-driven Golden grid variables.

Do not add template copies, renderer profiles, snapshot systems, or generalized HTML schemas without a concrete need.

## Mechanical fidelity

Flow 4 validator owns structural checks such as Flow 2 readiness, canonical-content/projection revision binding, page IDs/order, navigation reachability, duplicate IDs, placeholders, scoring/completion invariants, and the small Golden composition-marker set. The renderer itself owns bilingual input-shape rejection because invalid localization must fail before HTML is produced.

Do not duplicate those checks in authoring instructions. Structural PASS is not visual PASS.

## Command

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

Use another template only when the user explicitly approves a different document family.

## Boundary

```text
canonical PRD
→ compact Golden projection bound to that canonical revision
→ deterministic render
→ validate
```

Renderer code may organize approved meaning; it may never repair missing product definition, approve unresolved decisions, or make `final.html` a source of truth.
