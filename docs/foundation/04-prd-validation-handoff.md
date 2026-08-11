# PRD Validation & Team Handoff

Status: active Flow 4 policy

## Purpose

Separate a generated PRD from a development-ready PRD and preserve concise revision-specific acceptance/handoff evidence.

```text
Flow 3 canonical content + Golden HTML
→ mechanical validation
→ one integrated source/requirement-to-PRD review
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

Mechanical validation proves structural/render/navigation contracts only. It does not prove source fidelity, production completeness, Golden functional depth, or human-readable prose.

Semantic development readiness requires the integrated production-role review to confirm that material/high-impact source/requirement meaning is actually represented on the correct PRD surfaces.

A PRD is not development-ready merely because every Golden section exists. If Level Design or Developer must reopen the original source to discover a material rule that belongs in the PRD, that is a **Major completeness finding**.

## Semantic quality threshold

The accepted PRD must satisfy these functional outcomes:

- Gameplay Flow reads as the chronological player journey with enough context, response, consequence, and transition for a new team member to understand the experience;
- every gameplay package states the correct **Objective Score or explicit No Objective Score** result model;
- internal scoring/result, player-facing display, and telemetry/export remain distinct when authority distinguishes them;
- Level Design carries complete material build-relevant meaning;
- Developer carries complete material runtime/state/scoring-or-result/data/interruption/reset/handoff meaning;
- Global Development keeps important shared ownership visible rather than collapsing it into vague summary text;
- narrative/explanatory prose is human-readable production language, while exact technical values remain precise;
- Golden is used as a functional quality floor without copying sample-specific project facts or enforcing arbitrary word/row counts.

## Blocking threshold

- Critical / Major → block development readiness/handoff;
- Minor → may remain only when meaning stays safe/implementable and the item is intentionally recorded;
- Suggestion → optional polish.

Do not restore Content Freeze/release ceremony. A later canonical meaning change reopens only the affected revision/review boundary.

## Visual proof economy

Default visual sanity is **desktop-only** unless mobile/responsive behavior is explicitly required or the current defect is mobile-specific.

A representative visual smoke test normally needs only:

```text
Overview
+ one Gameplay Flow page
+ one Level Design page
+ one dense Developer page
```

Do not routinely test every navigation item, every tab, theme persistence, Terms disclosure, mobile menu, or localStorage merely for ceremony. Visual fidelity is claimed only for what was actually inspected.

## Revision-specific handoff

Use the existing PRD `document.version` as the lightweight downstream revision token. `state/handoff-state.yaml` records `accepted_prd_version` plus the existing canonical/render/HTML/acceptance/handoff paths.

A later canonical meaning change that invalidates the accepted handoff advances `document.version` and resets handoff state to `pending_review`. After the affected scope is rerendered/reviewed, Flow 4 may restore `handoff_ready` for the new version.

Before Flow 5 starts, `kits/project-document-generator/validator/validate_handoff.py` must pass. The guard checks the existing handoff status/version/path lifecycle **and** compact `work/acceptance.md` truth. A handoff cannot authorize Flow 5 when acceptance says `needs_revision`, a required review lens fails, mechanical validation fails, visual sanity explicitly fails, or Critical/Major blockers are non-zero.

`Visual sanity: NOT PROVEN` remains an honest allowed state when no desktop browser/page proof is available; it is not silently upgraded to visual PASS.

This is still a lightweight lifecycle/acceptance consistency guard. It does not add a new hash chain, semantic scoring engine, word-count validator, row-count validator, or second approval workflow.

## Handoff meaning

`handoff_ready` means the accepted PRD is usable as a production reference for the defined scope, material source/requirement meaning has passed the integrated role review, the recorded accepted version is still current, and compact acceptance does not contradict that handoff.

It does not mean client approval, implementation completion, QA pass, release approval, completed Voice Production, or universal proof for every future project shape.

Flow 5 decides downstream Voice requirements.
