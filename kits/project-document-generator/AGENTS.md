# Project Document Generator Agent Rules

Root `AGENTS.md` owns repository work mode, proof, skill budget, continuity, and semantic-vs-technical routing. This file narrows behavior inside `kits/project-document-generator/`.

## Flow routing

Start from current project/state and open only the active owner.

- **Flow 2** → `SOURCE-INTAKE.md`; `RULES.md` only for a kit-wide recovery rule; `GLOSSARY.md` only when terminology is unclear.
- **Flow 3 content** → `CONTENT-CONTRACT.md`.
- **Flow 3 projection/rendering** → `RENDERING.md` only when render-data shape/HTML behavior is in scope.
- **Flow 4** → `VALIDATION.md`.
- `WORKFLOW.md` is only for end-to-end sequencing when ownership is unclear.

Do not load every kit document by default.

## Context budget for HTML work

The Golden template and generated PRD can be very large. Runtime file access and model context are different things.

### Normal production

- Never load `template/approved-document.html` in full merely to create a PRD. The deterministic renderer can read the Golden file at runtime without placing its contents in model context.
- Never load `output/final.html` in full for routine semantic review.
- Do not copy Golden HTML/CSS/JS into working notes or prompts.
- Use `CONTENT-CONTRACT.md` as the compressed semantic/page-composition authority for normal authoring.
- Use `RENDERING.md` as the bounded projection/mechanics reference only when needed.

### Targeted inspection

Inspect template/generated HTML source only after a concrete defect identifies a likely HTML owner. Search for the exact section ID, class, marker, script, or component and read the smallest useful range.

For visual acceptance, prefer actual rendered/browser/page inspection when available. Reading HTML source is not a substitute for visual proof.

## Canonical boundary

```text
project originals + approved decisions
→ requirement state
→ work/content.md                 canonical PRD meaning
→ work/render-data.json           derived projection
→ output/final.html               derived presentation
→ acceptance/handoff evidence
```

Never patch a derived artifact to hide an upstream defect.

## Renderer ownership

- `renderer/core.py` → reusable Golden helpers and bounded presentation primitives.
- `renderer/pages.py` → Golden page composition from render data.
- `renderer/render.py` → deterministic template projection/output mechanics.
- `template/approved-document.html` → edit only when the template itself is proven to own the defect.
- `validator/validate.py` → mechanical Flow 4 checks.

Renderer code may organize approved meaning; it may not invent missing facts or product decisions.

## Production efficiency

Initial BUILD:

```text
finish/reconcile canonical content
→ derive compact render projection once
→ render once
→ validate/review
```

Do not regenerate a full projection after every prose edit during drafting.

Bounded revision:

```text
approved delta
→ affected content + cross-references
→ affected render-data subtree
→ rerender
→ targeted review
```

Do not reread/rewrite unchanged packages.

For English-only output, prefer scalar render-data strings rather than duplicated localized objects. For package terms, omit optional role metadata when default Gameplay visibility is sufficient.

## Semantic vs technical ownership

Use root `project-document-production` when the wrong contract is source meaning, canonical PRD meaning, Golden representation requirements, or readiness semantics.

When those semantics are already correct and the problem is executable renderer/template/validator mechanics, Maintenance routes directly to the exact owner here. Do not load a semantic specialist solely as a Python/HTML wrapper.

## Verification

Repository-side renderer/contract changes use the focused existing proof:

```text
python -m unittest tests.test_prd_contracts -v
python -m compileall -q kits/project-document-generator tests/test_prd_contracts.py
```

`Production Verify` is the canonical CI gate. Run only checks invalidated by the coherent change; do not repeatedly run local/manual project tests during an unfinished refinement batch.

Browser/visual PASS still requires actual browser/visual evidence.

## Maintenance

```text
observe concrete defect
→ identify first wrong owner
→ fix smallest owner
→ regenerate invalidated derived output
→ cheapest proof that can falsify the fix
→ stop
```

Do not create new renderer profiles, HTML schemas, snapshot frameworks, template copies, debug artifacts, or generic parsers without a concrete current requirement.

## Boundaries

This kit owns Flow 2–4. Voice belongs to `kits/voice-production-kit/`. Shared dependencies/tests/CI belong to repository engineering owners.
