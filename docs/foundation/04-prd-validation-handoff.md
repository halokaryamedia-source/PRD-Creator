# Flow 4 — PRD Validation & Team Handoff

Status: active durable policy

## Purpose

Separate a generated PRD from a production-ready PRD and preserve concise revision-specific handoff evidence.

## Canonical owners

- mandatory gameplay PRD content/quality → `kits/project-document-generator/CONTENT-CONTRACT.md`;
- detailed validation procedure → `kits/project-document-generator/VALIDATION.md`;
- lifecycle state → `state/handoff-state.yaml`;
- compact acceptance → `work/acceptance.md`;
- team handoff → `output/team-handoff.md`.

This page does not maintain another Golden checklist.

## Flow 4 sequence

```text
current canonical PRD + generated HTML
→ mechanical validation once
→ one integrated semantic review
→ targeted desktop visual sanity when available
→ Critical/Major?
     yes → fix first wrong owner and recheck invalidated scope
     no  → development_ready / handoff_ready
```

Mechanical validation proves deterministic repository/render contracts only. It does not prove source fidelity, role completeness, Humanize quality, or Golden functional depth.

Semantic acceptance applies the four lenses defined in `VALIDATION.md` against the mandatory contract in `CONTENT-CONTRACT.md`.

A production role having to reopen original source to recover a material rule that belongs in the PRD is a **Major** completeness failure.

## Handoff boundary

Use the existing `document.version` / `accepted_prd_version` lifecycle. Before Flow 5 starts, `validate_handoff.py` must confirm that the current accepted revision, artifact paths, and compact acceptance record agree.

`handoff_ready` means the PRD is usable as a production reference for the accepted scope. It does not mean client approval, implementation completion, gameplay QA, release approval, or completed Voice Production.

## Proof economy

Default visual proof is targeted desktop-only unless mobile/responsive behavior is explicitly required or is the active defect.

For a bounded revision, re-run only invalidated mechanical/semantic/visual checks. Do not replay unchanged source intake, unrelated packages, Voice tests, or mobile QA merely for ceremony.
