# Rules

## 0. Preserve source provenance

- Keep original source files unchanged inside the active project package.
- Record every source in `state/source-inventory.yaml` before using it as authority.
- Distinguish authoritative project source, supporting material, reference/golden material, and prior generated output.
- A previous generated document may help recover context but does not automatically outrank its underlying source or approved decisions.
- Never silently resolve a material source conflict. If explicit supersession or authority does not resolve it, classify the affected requirement as Blocked and surface the conflict.
- Do not ask the user for information that is already recoverable from available source or approved state.

## 1. Preserve project intent

- Clarify and complete documentation without replacing the original intent.
- Do not silently change gameplay, mechanics, scoring, progression, learning objectives, or win conditions.
- Put every design-changing suggestion in Proposal.

## 2. Complete supported gaps

- Fill missing information when it follows directly from the source and surrounding context.
- Keep terminology, constraints, sequence, and scope consistent with the source.
- Do not invent unsupported facts or mechanics.
- Use Blocked when a reliable completion requires a user decision.

## 3. Approval boundary

- Clarification and Completion may be included in the review as ready-to-apply content.
- Proposal must not enter Canonical Content or final HTML before explicit user approval.
- Blocked items stop the affected section until resolved.
- Never treat the model's own proposal as approved.

## 4. The Approved Template is fixed

- Clone the Approved Template. Do not recreate it.
- Preserve its DOM structure, CSS, JavaScript, class names, navigation, sidebar, typography, spacing, page composition, component order, tables, flow components, and print behavior.
- Do not redesign, modernize, simplify, optimize, or replace the presentation.
- Adapt content to the template. Do not adapt the template to the content.

## 5. Replace project-specific content only

The following may change:

- project title and metadata;
- story and project context;
- gameplay and flow content;
- objective count and objective-specific content;
- Level Designer and Developer content;
- required data, scoring, reset, and acceptance content;
- project-specific images and diagrams;
- navigation labels, targets, and page numbering required by dynamic objectives.

Everything else remains inherited from the Approved Template.

## 6. Preserve the Objective Package

- Identify the complete Objective Package in the Approved Template.
- Duplicate that package for each objective.
- Preserve the page types, hierarchy, component order, and placement used by the template.
- Do not remove required components because the source is incomplete; classify and complete the gap instead.
- If the template includes scoring for an objective, the corresponding objective must retain that scoring component.

## 7. Preserve reading structure

- A reference table remains a table.
- A reference flow remains a flow.
- A reference note remains a note.
- Do not compress a structured page into one paragraph.
- Match the reference page's content grouping and component density without forcing identical word counts.

## 8. No hidden decisions

Every meaningful addition must be traceable to:

- the Source;
- an approved Completion;
- or an approved Proposal.

Do not silently introduce decisions during rendering.

## 9. Keep outputs minimal

- Produce only requested deliverables.
- Do not add validators, reports, metrics, checksums, manifests, changelogs, or release files.
- Do not add a feature unless it directly improves content accuracy or template fidelity.
