# PRD Validation & Team Handoff

Status: active Flow 4 policy

## Purpose

Separate a generated PRD from a development-ready PRD and preserve concise revision-specific acceptance/handoff evidence.

```text
Flow 3 canonical content + Golden HTML
→ mechanical validation
→ one integrated multi-lens review
     New Reader / Player Context
     Level Designer
     Developer
     Project Consistency
→ Critical/Major finding?
     yes → fix first wrong owner → rerender/re-review invalidated scope
     no  → development_ready
→ current concise handoff boundary
```

The four lenses are perspectives inside one review, not four approval rounds or four mandatory rereads.

## Canonical owners

- detailed review procedure → `kits/project-document-generator/VALIDATION.md`;
- project lifecycle state → `state/handoff-state.yaml`;
- compact acceptance evidence → `work/acceptance.md`;
- current team navigation handoff → `output/team-handoff.md` under the existing downstream boundary.

## Evidence rule

Mechanical validation proves structural/render/navigation contracts only. Semantic development readiness requires the integrated production-role review. Visual fidelity is claimed only when actual rendered/page inspection supports it.

## Blocking threshold

- Critical / Major → block development readiness/handoff;
- Minor → may remain only when meaning stays safe/implementable and the item is intentionally recorded;
- Suggestion → optional polish.

Do not restore Content Freeze/release ceremony. A later canonical meaning change reopens only the affected revision/review boundary.

## Revision-specific handoff

Use the existing PRD `document.version` as the lightweight downstream revision token. `state/handoff-state.yaml` records `accepted_prd_version` plus the existing canonical/render/HTML/acceptance/handoff paths.

A later canonical meaning change that invalidates the accepted handoff advances `document.version` and resets handoff state to `pending_review`. After the affected scope is rerendered/reviewed, Flow 4 may restore `handoff_ready` for the new version.

Before Flow 5 starts, `kits/project-document-generator/validator/validate_handoff.py` must pass. This is a version/status/path consistency guard only; it does not add a new hash chain or replace semantic review.

## Handoff meaning

`handoff_ready` means the accepted PRD is usable as a production reference for the defined scope and the recorded accepted version is still current. It does not mean client approval, implementation completion, QA pass, release approval, or completed Voice Production.

Flow 5 decides downstream Voice requirements.
