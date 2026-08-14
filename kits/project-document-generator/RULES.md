# Rules

This file keeps only kit-wide invariants. Detailed Flow 2–4 procedure belongs to `SOURCE-INTAKE.md`, `CONTENT-CONTRACT.md`, `RENDERING.md`, and `VALIDATION.md`.

## 1. Preserve authority and provenance

- Record every material source/instruction in `state/source-inventory.yaml` before relying on it as durable authority.
- Keep a supplied original in `source/originals/` when repository retention materially helps continuity or the source is needed for later direct inspection.
- Do **not** duplicate a large/static source in Git only for ceremony. External retention is allowed when the exact source identity/provenance needed for continuity is recorded (for file sources, normally filename plus SHA-256 when available) and recovered project meaning is fully persisted upstream.
- Distinguish authoritative, supporting, reference, and generated material.
- Never silently choose between conflicting material claims.
- Do not ask the user for information already recoverable from current authority/approved state.

## 2. Preserve project intent and approval boundaries

- Clarification improves explanation without changing meaning.
- Completion may fill a missing answer only when one evidence-backed/necessary result is implied.
- When the system must choose among plausible product/design/development answers, use a concrete **Proposal**. It is pending until the user approves/corrects the relevant Simple Chat Preview.
- A Proposal may include gameplay, scoring, progression, quantities, timing, build expectations, runtime behavior, or implementation rules at PRD abstraction level; it must never be mislabeled as source fact.
- Use `Blocked` only when no responsible proposal can be formed from current authority and known constraints.
- After preview approval, promote represented pending proposals into approved requirement/project state before Flow 3.
- A material AI-chosen Proposal is represented only when its chosen default appears once in the Simple Chat Preview `Saran AI` block. Do not hide timing, quantity, scoring, fail/recovery, progression, reward, build-scope, or runtime-behavior choices inside otherwise natural preview prose.

## 3. Canonical meaning stays upstream

```text
source evidence + current user instruction + approved decisions
→ requirement state
→ work/content.md
→ work/render-data.json
→ output/v<document.version>/prd.html
→ acceptance / handoff
```

`content.md` owns PRD meaning. Render projection and HTML are derived and may not introduce new project facts or decisions.

If Flow 3/4 exposes a real unresolved product/design decision, return only that affected slice to Flow 2.

## 4. Follow the single content contract

`CONTENT-CONTRACT.md` owns the gameplay PRD family: hierarchy, mandatory-slot meaning, role separation, scoring/result behavior, glossary semantics, material-detail conservation, Humanize quality, and Golden visible composition.

Do not maintain a second Golden checklist or project-specific exception list in another rule file.

## 5. Exact Golden template, no derived patching

The approved Golden is preserved through two intentional paths:

```text
template/golden-reference.html     canonical reference evidence
template/runtime-template.html runtime template alias
```

Both must remain byte-identical unless the user explicitly approves a Golden revision.

- Project rendering may bind project-owned metadata, pages, navigation, glossary data, package scope, and project storage namespace.
- Stable presentation components are changed only at the template/renderer owner when the Golden contract itself is intentionally revised or a real implementation defect exists.
- Do not add reference-project facts to another project.
- Do not manually patch `output/v<document.version>/prd.html`.

## 6. Preserve package role ownership

Production-relevant gameplay packages use:

```text
Gameplay Overview
→ Level Design
→ Developer
```

Reference-project mechanics/counts/content do not transfer to another project. Missing role-owned meaning is a recovery/content problem, not permission to silently remove the surface.

## 7. Mechanical proof cannot replace semantic or visual proof

Renderer/validator may expose deterministic defects but may not define product meaning.

Flow 4 records the minimum independent proof channels:

```text
Mechanical
Semantic Readiness
Material Conservation
Visual sanity
```

Critical/Major findings block `development_ready` / `handoff_ready`.

`Semantic Readiness` is one integrated review result; do not persist separate PASS fields for New Reader, Level Designer, Developer, Project Consistency, Acceptance, Content Purity semantics, or Golden Placement.

Visual PASS requires actual rendered/browser evidence. Static HTML inspection is not a visual PASS.

## 8. Keep document versions stable

`document.version` is project/release metadata, not an edit counter.

Keep the same version through normal drafting, clarification, Humanize, rendering, review correction, representative testing, and documentation-only system cleanup. Change it only when:

- the user explicitly requests a new version;
- an authoritative source declares a new project/document revision;
- the team intentionally establishes a new release/handoff milestone.

When accepted PRD meaning changes, reopen handoff state, regenerate/review affected scope, and restore readiness only after acceptance. Do not add a revision/checksum registry for this.

## 9. Keep the system minimal

- Produce only artifacts required by the active Flow/task.
- Reuse existing owners before creating schemas, profiles, stages, reports, or frameworks.
- Use the cheapest proof that can falsify the active claim; do not replay unchanged checks for ceremony.
- Do not revive archived parity/remediation programs without a concrete current defect.
- `No change required` is valid.
