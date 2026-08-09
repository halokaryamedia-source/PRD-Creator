# PRD Validation & Team Handoff

Status: active Flow 4 policy

## Purpose

Separate **generated PRD** from **development-ready PRD** and create one concise production handoff only after the actual content is usable by its downstream roles.

```text
Flow 3 generated content + HTML
↓
mechanical validation
↓
New Reader audit
Level Designer audit
Developer audit
Project Consistency audit
↓
Critical/Major findings?
  yes → fix canonical owner → rerender → re-audit
  no  → development_ready
↓
concise team-handoff.md
↓
handoff_ready
```

## Canonical owner

Detailed procedure: `kits/project-document-generator/VALIDATION.md`.

Project state: `workspace/active/<project>/state/handoff-state.yaml`.

Human acceptance record: `workspace/active/<project>/work/acceptance.md`.

Team navigation handoff: `workspace/active/<project>/output/team-handoff.md`.

## Evidence rule

Structural tool success is not semantic acceptance. `validator/validate.py` can prove file/render/navigation invariants, but only the four-perspective content audit can establish development-readiness.

## Blocking threshold

- Critical: blocks handoff.
- Major: blocks handoff.
- Minor: may remain only when meaning is still safe/implementable and the open item is recorded intentionally.
- Suggestion: non-blocking.

## No Content Freeze ceremony

Flow 4 does not restore the Archived builder's multi-stage Content Freeze/release process. The current revision is accepted by recording exactly which canonical content + rendered artifact were audited. A later meaning change reopens the state to `pending_review` and requires targeted re-audit.

## Handoff meaning

`handoff_ready` means the PRD is usable as a production reference for the defined scope. It does not mean:

- client approval;
- implementation completed;
- QA passed;
- release approved;
- Voice Production already extracted.

Flow 5 decides whether/what voice requirements should be derived from the accepted PRD.
