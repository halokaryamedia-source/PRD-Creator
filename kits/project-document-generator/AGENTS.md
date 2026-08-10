# Project Document Generator Agent Rules

Root `AGENTS.md` remains authoritative for work mode, proof, skill budget, repository continuity, and the semantic-vs-technical ownership rule. This file narrows behavior only inside `kits/project-document-generator/`.

## Module Structure

```text
kits/project-document-generator/
├─ AGENTS.md
├─ SKILL.md
├─ SOURCE-INTAKE.md
├─ CONTENT-CONTRACT.md
├─ RENDERING.md
├─ VALIDATION.md
├─ RULES.md
├─ WORKFLOW.md
├─ GLOSSARY.md
├─ renderer/
│  ├─ core.py
│  ├─ pages.py
│  └─ render.py
├─ template/
│  └─ approved-document.html
└─ validator/
   └─ validate.py
```

`tests/test_prd_contracts.py` is the focused repository regression owner for high-risk generic renderer/validator contracts.

## Flow Routing

Start from the current project/state and identify the active Flow before opening kit documents.

- **Flow 2 — Source Intake & Requirement Recovery**
  - read `SOURCE-INTAKE.md`;
  - read `RULES.md` only when a kit-wide recovery rule is relevant;
  - read `GLOSSARY.md` only when terminology is unclear.
- **Flow 3 — PRD Generation**
  - read `CONTENT-CONTRACT.md`;
  - read `RENDERING.md` only when projection/rendering is in scope;
  - inspect `template/approved-document.html` only when template fidelity matters.
- **Flow 4 — PRD Validation & Team Handoff**
  - read `VALIDATION.md`;
  - inspect renderer/content only when a finding points back to those owners.

Use `WORKFLOW.md` only when end-to-end sequencing or Flow ownership is unclear. Do not load every kit document by default.

## Canonical Boundary

```text
project originals + approved decisions
→ requirement state
→ work/content.md                 canonical PRD meaning
→ work/render-data.json           derived projection
→ output/final.html               derived presentation
→ work/acceptance.md              revision-specific evidence
→ state/handoff-state.yaml
→ output/team-handoff.md
```

Never patch a derived artifact to hide a defect in an upstream owner.

## Semantic vs Technical Ownership

Use the root `project-document-production` specialist when the wrong behavior is a **Flow 2–4 semantic/product-contract** problem, including:

- source authority / requirement recovery;
- canonical PRD meaning;
- what the render projection/pages must represent;
- approved-template product contract;
- PRD readiness/handoff semantics.

When semantics are already correct and the defect is purely executable mechanics, Maintenance may route directly here without loading a root specialist.

Technical owners:

- rendering helpers/layout data mechanics → `renderer/core.py` / `renderer/pages.py`;
- deterministic template projection/output → `renderer/render.py`;
- approved shell mechanics → `template/approved-document.html` only when the shell itself is the cause;
- mechanical Flow 4 checks → `validator/validate.py`.

Do not call a Python/tooling specialist merely because these files are Python.

## Contributor Rules

### Renderer

- `work/content.md` remains canonical project meaning; renderer code cannot invent or repair missing project facts.
- `work/render-data.json` is derived projection, not another authority layer.
- preserve deterministic template markers, stable IDs, navigation reachability, and placeholder rejection.
- change `pages.py` / `core.py` only when the representation helper actually owns the defect.
- change `render.py` only when projection/template/output mechanics own the defect.
- do not hand-edit `output/final.html` as the fix.

### Template

- preserve the approved shell by default;
- do not redesign presentation during unrelated Flow work;
- a template edit needs a shell-level requirement or proven template defect;
- Golden/reference content never becomes project facts.

### Validator

- mechanical validation must fail closed on the contract it claims to check;
- do not make semantic development-readiness claims from mechanical checks alone;
- if the validator exposes an upstream content/render defect, fix that upstream owner rather than weakening the check.

## Verification Commands

Run from repository root.

### Focused contract suite

```text
python -m unittest tests.test_prd_contracts -v
```

This executes the real renderer and real Flow 4 mechanical validator against minimal generic fixtures.

### Compile check

```text
python -m compileall -q kits/project-document-generator tests/test_prd_contracts.py
```

### Direct renderer

```text
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

### Direct validator

```text
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>
```

For repository-side production changes, `Production Verify` is the canonical repeatable CI gate. Run only the checks invalidated by the active change when working locally.

## Maintenance

For a concrete defect:

1. establish whether the first wrong owner is source/recovery, canonical content, render projection, renderer/template mechanics, validator mechanics, or acceptance evidence;
2. if semantic/product contract is wrong, route to `project-document-production`;
3. if semantics are correct and mechanics are wrong, fix the exact implementation owner here;
4. regenerate only invalidated derived artifacts;
5. run the minimum useful proof;
6. browser/visual PASS still requires actual browser/visual evidence when that level is claimed.

Maintenance does not automatically invoke `development-brief` or a root specialist.

## Boundaries

- This kit owns Flow 2–4 only.
- Voice scope/writing/DOCX belongs to `kits/voice-production-kit/`.
- Repository-wide dependency/test/CI ownership belongs to root `requirements.lock.txt`, `tests/`, `tools/`, and `.github/workflows/`.
- Golden/reference material demonstrates approved structure/quality only; it does not define project facts.
- Do not recreate retired schema/profile/freeze/package architecture without a proved current requirement.
