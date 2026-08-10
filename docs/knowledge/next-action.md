# Next Action

Updated: 2026-08-11

This is the single active-task snapshot.

## Current Status

`PRD_PRE_SAMPLE_AUDIT_COMPLETE_REAL_PROJECT_SAMPLE_NEXT`

Working branch: **`Local` only**.

## Golden Sample decision

The approved Golden Sample remains the required output authority for this gameplay-document family.

Preserve both:

```text
Hierarchy
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

and its reusable page composition/component language.

Golden remains the hierarchy, page composition, component language, and presentation foundation. It is not merely an HTML/CSS shell, and it is not a reason to copy Aftershock-specific project facts or fixed item counts into another project.

## PRD pre-sample audit — complete

The remaining user-facing PRD risks identified after Golden fidelity remediation have now been closed with bounded changes.

### 1. Adaptive Golden content distribution

Golden journey/flow components no longer assume Aftershock's exact item count on desktop.

```text
Overview journey
→ one column per item up to the Golden six-column capacity
→ larger sets wrap at the existing Golden maximum

Golden flow cards
→ one column per item up to the Golden four-column capacity
→ larger sets wrap at the existing Golden maximum
```

Existing Golden mobile behavior remains authoritative. No layout engine, template profile, visual score, or alternate document family was introduced.

### 2. Explicit document language availability

The renderer now distinguishes:

```text
["en"]
→ English-only document
→ EN/ID selector hidden

["en", "id"]
→ bilingual document
→ selector remains available
```

An explicit localized `en` / `id` value in bilingual output must provide both sides. The renderer no longer silently copies a missing localized language into the other side.

Scalar proper names, codes, numbers, formulas, IDs, and other intentionally shared values may remain identical. No translation service, translation memory, or localization framework was added.

### 3. Role-specific Terms Used

Package terms remain one glossary/tooltips source.

Visible package Terms Used now behaves as:

```text
roles omitted
→ Gameplay Overview only

roles explicitly include level_design / developer
→ visible on those named role pages

roles: []
→ glossary/tooltips only
```

This removes automatic repetition of every package term across Gameplay, Level Design, and Developer while keeping the shared glossary source intact.

### 4. Documentation alignment

Kit documentation now uses the current Golden composition model rather than the retired shell-only mental model.

`kits/project-document-generator/README.md` is aligned to kit version `1.5.0` and describes Golden hierarchy + composition + presentation foundation. `CONTENT-CONTRACT.md` and `RENDERING.md` record the bounded language, adaptive-grid, and role-specific Terms Used behavior.

## Implementation revision

Substantive implementation commit:

```text
41174b4f54a16b33f2b320aa520d9711e08b07a5
fix: close PRD pre-sample rendering gaps
```

Final verified implementation revision after restoring the pre-existing non-executable renderer file mode:

```text
e12ab42ee58d1768e1becd74f271c24b13fbadb8
```

## Verification evidence

```text
Repository Verify #48
run: 31416985727
head: e12ab42ee58d1768e1becd74f271c24b13fbadb8
result: PASS

Production Verify #17
run: 31416986247
head: e12ab42ee58d1768e1becd74f271c24b13fbadb8
result: PASS
job: 93548231114
```

Production Verify passed:

- locked dependency installation;
- Python source compilation;
- Project Document contracts, including the new focused PRD renderer cases;
- Voice Production contracts as downstream regression coverage;
- final verification enforcement.

## Boundaries intentionally unchanged

Do not reopen these without a concrete real-project defect:

- Golden hierarchy or template family;
- `content.md → render-data.json` architecture;
- Source Intake / requirement-recovery architecture;
- visual scoring / pixel-diff / screenshot baseline systems;
- translation-service or localization frameworks;
- BuildIT parity as an automatic backlog.

Handoff-state simplification remains deferred. Review it only together with the later PRD → Voice boundary if real project use shows friction there.

## Evidence boundary

Repository and production-contract verification are complete for this implementation revision.

**Actual visual quality on a new project is not yet claimed.** Golden browser/page behavior with a different project structure must be judged from the next real-project sample, not inferred from mechanical tests.

## Next Step

Run one real project through PRD Flow 2–4 using the current system, then inspect the actual generated Golden document for content recovery, layout distribution, language behavior, role readability, and visual quality. Fix only concrete defects exposed by that sample.
