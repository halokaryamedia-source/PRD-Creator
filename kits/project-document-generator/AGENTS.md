# Project Document Generator Agent Rules

Root `AGENTS.md` owns repository mode, proof, skill budget, continuity, and semantic-vs-technical routing. This file owns only PRD kit routing/mechanics.

## Open only the active owner

- Flow 2 → `SOURCE-INTAKE.md`
- Flow 3 content → `CONTENT-CONTRACT.md`
- Flow 3 projection/HTML → `RENDERING.md` only when needed
- Flow 4 → `VALIDATION.md`
- `WORKFLOW.md` → sequencing reference only when the active Flow is unclear
- `GLOSSARY.md` / `RULES.md` → only for a specific terminology/kit-wide rule question

Do not load the whole kit by default.

## HTML context budget

Normal production must not load `template/approved-document.html` or `output/final.html` in full into model context.

- Renderer/validator may read large files directly at runtime.
- Canonical meaning review uses `content.md`.
- Projection investigation uses only the affected `render-data.json` subtree.
- HTML source is inspected only for a concrete page/class/marker/component defect and only in the smallest useful range.
- Visual claims require actual rendered/browser/page inspection when available; source inspection is not visual proof.

## Canonical boundary

```text
project originals + approved decisions
→ requirement state
→ content.md                 canonical meaning
→ render-data.json           derived projection
→ final.html                 derived presentation
→ acceptance/handoff evidence
```

Never patch a derived artifact to hide an upstream defect.

## Implementation ownership

- `renderer/core.py` → reusable Golden helpers/primitives
- `renderer/pages.py` → render data → Golden page composition
- `renderer/render.py` → deterministic template mutation/output mechanics
- `template/approved-document.html` → only when the Golden template itself is proven wrong
- `validator/validate.py` → mechanical Flow 4 checks, including the narrow explicit Flow 2 persisted-state contradiction guard
- `validator/validate_handoff.py` → narrow Flow 4 → Flow 5 handoff-entry consistency check using existing `document.version` + `handoff-state.yaml`; it must not grow into a generic artifact manifest/revision framework

Renderer/validator code may organize/check approved meaning; it may not invent project facts or decisions.

## Efficient production

Initial BUILD:

```text
finish canonical meaning
→ derive compact projection once
→ render
→ validate/review
```

Bounded revision:

```text
approved delta
→ affected content + cross-references
→ affected projection subtree
→ rerender
→ targeted review
```

Do not reread/rewrite unchanged packages. English-only data should not be duplicated into fake bilingual objects. Optional metadata stays omitted when the default meaning is sufficient.

## Semantic vs technical

- source/canonical/Golden representation/readiness meaning wrong → root `project-document-production` + smallest semantic owner;
- semantic contract correct, executable mechanics wrong → exact implementation owner here.

Do not load a root semantic specialist solely as an HTML/Python wrapper.

## Verification and Maintenance

For a concrete defect:

```text
observe failure
→ identify first wrong owner
→ smallest fix
→ regenerate invalidated derived output
→ cheapest proof that can falsify the fix
→ stop
```

Focused repository proof:

```text
python -m unittest tests.test_prd_contracts tests.test_prd_handoff_contracts tests.test_prd_flow2_state_contracts -v
python -m compileall -q kits/project-document-generator tests/test_prd_contracts.py tests/test_prd_handoff_contracts.py tests/test_prd_flow2_state_contracts.py
```

`Production Verify` is the canonical CI gate for affected production contracts. Do not repeatedly run manual/local project tests during an unfinished refinement batch. Browser/visual PASS still requires actual browser/visual evidence.

Do not create renderer profiles, HTML schemas, snapshot systems, template copies, debug artifacts, generic parsers, or new skills without a concrete current need.

## Boundary

This kit owns Flow 2–4. Voice belongs to `kits/voice-production-kit/`; shared dependencies/tests/CI belong to repository engineering.
