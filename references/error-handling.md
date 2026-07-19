# Error Handling

## Required Error Response

Always explain:

1. What failed?
2. Why did it fail?
3. What is the impact?
4. What should happen next?

Do not hide a blocker or invent data to make the process appear successful.

## Error Groups

- Source Error
- Decision Error
- State Error
- Content Error
- Validation Error
- Artifact Error
- Rendering Error
- Delivery Error

Also classify recoverable, requires user decision, blocking, or non-blocking.

## Source Errors

For incomplete sources, record confirmed information, identify the first blocker,
recommend a simple initial structure, and discuss only three to five high-impact
decisions. For vague references, locate the exact value/reference or create an
open question. Multiple versions are not automatically ordered by timestamp;
status such as approved/draft/obsolete matters.

## Decision Errors

When source conflicts with an approved decision, show both rules, affected
sections, recommendation, and request explicit approval. Two conflicting approved
decisions are Critical. A recommendation accidentally used as approval must be
removed from final content and returned to assumptions/open decision state.

## State Errors

Do not continue from missing/corrupt state silently. Recover only directly
supported facts, mark reconstructed state `needs_confirmation`, validate version
and artifact metadata, and restore one active flow/next step.

## Content and Validation Errors

Required missing sections, critical data, unresolved placeholders, invalid
scoring, incomplete completion data, glossary conflicts, consistency failures, or
schema violations block the relevant gate. Fix the source-of-truth layer, not
only the output.

## Artifact Errors

Search current conversation/workspace/library and Artifact History. Do not invent
file paths. HTML without Structured Content is recovery input only; reconstruct
content, mark it for confirmation, and audit. Preserve the last valid artifact.

## Scope and Profile Errors

A changed scope/profile requires impact analysis, user approval, content remap,
and re-audit. Do not delete excluded content automatically.

## Render Errors

Final HTML before Content Freeze is blocked. A visual prototype is allowed only by
explicit request and must be non-final. Missing template/Golden files block final
render. Structural, tooltip, responsive, print, or translation failures produce
`needs_revision`, not final delivery.

A created file without Final HTML Audit remains `audit_required`.

## Delivery Errors

Critical or Major HTML findings block delivery. Verify HTML and ZIP actually
exist and paths are real. User rejection starts Update mode and reopens affected
content/template/renderer state.

## Hard Stops

Stop for unresolved profile, source/decision conflict, missing completion or
critical quantity, invalid scoring, blocking interruption/reset, change to Frozen
content, missing source-of-truth artifact, unsafe state recovery, or final delivery
based on unconfirmed assumptions.

## Safe Automatic Recovery

May repair formatting, duplicate text, labels, navigation from valid hierarchy,
clear metadata references, transient validation, ZIP generation, and non-content
template bugs. Must not choose product rules, quantities, weights, completion,
handoff, reset, profile, or approval.

## Resolution

After an error resolves, report completed repair, synchronized impact, restored
progress, and the single next step from Project State.
