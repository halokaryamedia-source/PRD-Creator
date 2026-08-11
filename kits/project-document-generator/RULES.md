# Rules

This file keeps only kit-wide invariants. Detailed Flow 2–4 procedure belongs to `SOURCE-INTAKE.md`, `CONTENT-CONTRACT.md`, `RENDERING.md`, and `VALIDATION.md`.

## 1. Preserve authority and provenance

- Keep original project sources unchanged.
- Record material evidence in `state/source-inventory.yaml` before relying on it as authority.
- Distinguish authoritative, supporting, reference, and generated material.
- Never silently choose between conflicting material claims.
- Do not ask the user for information already recoverable from current authority/approved state.

## 2. Preserve project intent

- Clarification/Completion may improve documentation without changing project behavior.
- A material design/product choice is a Proposal until explicitly approved.
- Blocked material scope remains blocked; renderer/validator cannot solve it downstream.
- Do not invent gameplay, scoring, progression, quantities, timing, architecture, or implementation behavior to make the document look complete.

## 3. Canonical meaning stays upstream

```text
source + approved decisions
→ requirement state
→ work/content.md
→ work/render-data.json
→ output/final.html
```

`content.md` owns PRD meaning. Render projection and HTML are derived and may not add new project facts or decisions.

If Flow 3/4 discovers a material product gap, return it to Flow 2.

## 4. Follow the single content contract

`CONTENT-CONTRACT.md` owns the gameplay PRD family: hierarchy, mandatory-slot meaning, role separation, scoring/result behavior, glossary semantics, and Humanize quality.

Do not maintain a second Golden checklist or project-specific exception list in another rule file.

## 5. Generic template, no derived patching

`template/approved-document.html` is generic PRD presentation/runtime infrastructure.

- Project rendering may replace project-owned metadata, pages, navigation, glossary data, package scope, and project storage namespace.
- Stable presentation components are edited at the template/renderer owner when genuinely wrong.
- Do not add reference-project names or internal iteration/version labels to active component names.
- Do not manually patch `final.html`.

## 6. Preserve package role ownership

Production-relevant gameplay packages use:

```text
Gameplay Overview
→ Level Design
→ Developer
```

Reference-project mechanics/counts/content do not transfer to another project. Missing role-owned meaning is a recovery/content problem, not permission to silently remove the surface.

## 7. Mechanical proof cannot replace semantic review

Renderer/validator may expose deterministic defects but may not define product meaning.

`development_ready` / team handoff requires Flow 4 semantic review. Critical/Major findings block readiness.

Visual PASS requires actual visual/browser evidence; static HTML inspection is not a visual PASS.

## 8. Handoff is revision-specific

`document.version` is the existing PRD revision used by downstream handoff.

When an accepted PRD's **meaning** changes materially:

```text
advance document.version
→ reopen handoff state to pending review
→ rerender/review affected revision
→ restore handoff_ready only after acceptance
```

Do not add another revision/checksum/manifest framework for this boundary.

`handoff_ready` means only that the current accepted PRD revision may enter the next production flow. It does not imply client approval, implementation completion, QA completion, release approval, or Voice readiness.

## 9. Keep the system minimal

- Produce only artifacts required by the active flow/task.
- Reuse existing owners before creating new schemas, profiles, stages, reports, or frameworks.
- Do not revive archived ceremony without a concrete current need.
- `No change required` is valid.
