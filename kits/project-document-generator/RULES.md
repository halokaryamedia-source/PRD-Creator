# Rules

## 0. Preserve source provenance

- Keep original source files unchanged inside the active project package.
- Record every source in `state/source-inventory.yaml` before using it as authority.
- Distinguish authoritative source, supporting material, reference/golden material, and prior generated output.
- Never silently resolve a material source conflict.
- Do not ask the user for information already recoverable from source or approved state.

## 1. Preserve project intent

- Clarify/complete documentation without replacing original intent.
- Do not silently change gameplay, mechanics, scoring, progression, learning objectives, win conditions, quantities, or runtime behavior.
- Every design-changing addition is Proposal until explicitly approved.

## 2. Complete supported gaps

- Fill only what strong source/context supports without changing design intent.
- Keep terminology, constraints, sequence, and scope aligned with source authority.
- Use Completion only when one reliable evidence-backed result exists at the needed abstraction.
- When multiple product/design choices remain, use the Flow 2 Resolution Ladder: responsible Proposal when one or a small tradeoff set can be formed; Blocked when evidence is insufficient/conflicting and no responsible proposal can be made.
- Do not invent metrics merely to make qualitative intent appear precise.

## 3. Approval boundary

- Supported Clarification/Completion may enter canonical content.
- Proposal may not enter canonical content/final HTML before approval.
- Blocked stops the affected required scope.
- The model never self-approves a Proposal.

## 4. Canonical content owns meaning

- `work/content.md` is the Flow 3/4 source of truth for PRD meaning.
- Follow `CONTENT-CONTRACT.md` for hierarchy, role separation, scoring/completion, and critical information.
- Do not use polished prose to hide unresolved critical information.
- If Flow 3 discovers a material topology/lifecycle/numeric/clarity/global-local/known-constraint/product-decision gap, return it to Flow 2 instead of deciding it during drafting.

## 5. Rendering projection is derived

- `work/render-data.json` exists only to render canonical content deterministically.
- It must not add a fact, requirement, mechanic, quantity, score rule, or approval.
- Canonical-content changes require projection regeneration before rerendering.

## 6. Approved Template is fixed

- Preserve shared CSS, JavaScript, class vocabulary, controls, sidebar shell, typography, spacing, responsive, and print behavior.
- Project navigation/pages/glossary may be regenerated using the approved component vocabulary.
- Do not redesign the visual system during project rendering.

## 7. Preserve Gameplay Package role ownership

- Production-relevant packages use Gameplay Overview → Level Design → Developer.
- Do not force Aftershock-specific objective count, characters, mechanics, or page count onto another project.
- Missing role information is a content/recovery problem, not permission to remove the role surface silently.

## 8. No hidden decisions during rendering or validation

- Renderer/validator may expose defects but may not define product meaning.
- A missing or conflicting product decision discovered in Flow 4 returns to Flow 2.
- Flow 4 may fix wording only when the approved underlying meaning is already clear.
- Never patch `final.html` to make an audit pass; fix its real canonical owner and rerender.

## 9. Development-ready requires semantic evidence

- Mechanical validation alone cannot issue `development_ready`.
- Flow 4 must audit New Reader, Level Designer, Developer, and Project Consistency perspectives.
- Critical and Major findings block development-ready/team handoff.
- Minor may remain only when meaning remains safe/implementable and the open item is recorded intentionally.

## 10. Handoff status is revision-specific

- `state/handoff-state.yaml` must point to the exact accepted content/render/acceptance/handoff artifacts.
- A later canonical meaning change reopens status to `pending_review` until affected dependencies are rerendered/re-audited.
- `handoff_ready` does not imply client approval, implementation completion, QA completion, release approval, or Voice Production readiness.

## 11. Keep outputs minimal

- Produce only files required by the current flow/task.
- Do not revive Archived builder schemas, Content Freeze ceremony, release reports, ZIP packaging, or multi-profile infrastructure without a concrete current need.
- `No change required` remains valid.
