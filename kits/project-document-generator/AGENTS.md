# Project Document Generator Agent Rules

Root `AGENTS.md` owns repository mode, proof, skill budget, continuity, and semantic-vs-technical routing. This file owns only PRD kit routing/mechanics.

## Open only the active owner

- Flow 2 → `SOURCE-INTAKE.md`
- Flow 3 content → `CONTENT-CONTRACT.md`
- Flow 3 projection/HTML → `RENDERING.md` only when needed
- Flow 4 → `VALIDATION.md`
- `WORKFLOW.md` → sequence only when the active Flow is unclear
- `GLOSSARY.md` / `RULES.md` → only for a specific terminology/kit-wide invariant question

Do not broad-read the whole kit by default.

## HTML context budget

Normal production must not load `template/approved-document.html` or generated `final.html` in full into model context.

- renderer/validator may read large files directly at runtime;
- canonical meaning review uses `content.md`;
- projection investigation uses only the affected `render-data.json` subtree;
- HTML source is inspected only for a concrete component/marker/runtime defect and only in the smallest useful range;
- visual claims require actual rendered/browser/page evidence.

## Canonical boundary

```text
project originals + approved decisions
→ requirement state
→ content.md
→ render-data.json
→ final.html
→ acceptance / handoff evidence
```

Never patch a derived artifact to hide an upstream defect.

## Implementation ownership

- `renderer/core.py` → reusable PRD rendering helpers/primitives
- `renderer/pages.py` → render data → PRD page composition
- `renderer/render.py` → deterministic template projection/output mechanics
- `template/approved-document.html` → generic stable PRD presentation/browser runtime
- `validator/validate.py` → mechanical Flow 4 checks
- `validator/validate_handoff.py` → narrow Flow 4 → Flow 5 handoff-entry consistency

Renderer/validator code may organize/check approved meaning; it may not invent project facts or decisions.

## Efficient production

Initial build:

```text
finish canonical meaning
→ derive compact projection
→ render
→ validate/review
```

Bounded revision:

```text
approved delta
→ affected content + cross-references
→ affected projection
→ rerender
→ targeted review
```

Do not reread/rewrite unchanged packages. English-only data should not be duplicated into fake bilingual objects.

## Semantic vs technical

- source/canonical/PRD representation/readiness meaning wrong → root `project-document-production` + smallest semantic owner;
- semantic contract correct but renderer/validator/template mechanics wrong → exact implementation owner here.

Do not load a semantic specialist solely as an HTML/Python wrapper.

## Verification and maintenance

For a concrete defect:

```text
observe failure
→ identify first wrong owner
→ smallest complete fix
→ regenerate invalidated derived output
→ cheapest proof that can falsify the fix
→ stop
```

`Production Verify` is the canonical CI gate for affected production contracts. Do not repeatedly run local/manual project checks during an unfinished refinement batch.

Browser/visual PASS still requires actual browser/visual evidence.

Do not create renderer profiles, HTML schemas, snapshot systems, template copies, debug artifacts, generic parsers, or new skills without a concrete current need.

## Boundary

This kit owns Flow 2–4. Voice belongs to `kits/voice-production-kit/`; shared dependencies/tests/CI belong to repository engineering.
