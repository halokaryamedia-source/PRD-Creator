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

## Handoff meaning

`handoff_ready` means the accepted PRD is usable as a production reference for the defined scope. It does not mean client approval, implementation completion, QA pass, release approval, or completed Voice Production.

Flow 5 decides downstream Voice requirements.
