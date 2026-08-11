# Production + Operating Validation Report

Updated: 2026-08-11

This file owns the **current evidence state** for PRD-Creator.

## Evidence boundary

Keep these evidence classes separate:

- **Current repository/static proof** — current `Local` contracts/regressions/GitHub Actions prove the stated repository mechanics.
- **Representative diagnostic project evidence** — a real project run may expose where the current authoring/review method succeeds or fails, but it is not semantic-quality proof when later review finds material omissions.
- **Current representative semantic/browser proof** — requires the current semantic contract to be exercised on a real project and accepted at the current quality threshold.
- **Historical real-project proof** — earlier revisions remain continuity evidence only.
- **Current DOCX/audio proof** — requires current downstream Voice/DOCX/audio execution.

One project is never universal proof for every source/project shape.

## Current revision status

Current working branch: `Local`.

The earlier AFTERSHOCK representative run is now classified as **diagnostic evidence, not accepted PRD-quality proof**.

The generated artifact did prove that current mechanical renderer/validator/browser plumbing could produce and open a complete Golden hierarchy. However, direct user review of the final sample identified material semantic-quality failures:

- Objective scoring was incorrectly reduced because `score is not displayed/exported` was misread as `No Objective Score`;
- Gameplay Flow was compressed into task summaries instead of the chronological player story/context needed by the team;
- Level Design, Developer, and Global Development content lost material detail compared with what the project/Golden-quality output required;
- explanatory prose remained too compressed/database-like and was not sufficiently humanized;
- the final semantic acceptance threshold was too permissive and declared PASS before source-to-PRD coverage was deep enough.

Therefore the previous `New Reader / Level Designer / Developer / Project Consistency: PASS` record must **not** be used as evidence that Flow 2–4 semantic quality was complete.

## What remains valid from the prior run

The prior AFTERSHOCK execution remains useful evidence only for these bounded claims:

- current renderer/template could generate the required Golden hierarchy;
- mechanical validation could run against a real project workspace;
- generated HTML could render in Chromium;
- handoff mechanics could execute on the produced project state;
- the run exposed that mechanical PASS alone is insufficient for production quality.

The browser/mobile portion of that run is not a continuing default requirement. Current policy is desktop-only visual proof unless mobile/responsive behavior is explicitly required.

## Root cause established by audit

The problem was not primarily the HTML renderer. The first wrong owners were semantic:

```text
authority interpretation
→ Flow 2 recovery
→ Flow 3 content-depth/writing contract
→ Flow 4 semantic acceptance threshold
```

The previous contract over-emphasized `minimum sufficient detail`, concision, and structural presence. That allowed:

```text
complete-looking Golden skeleton
+
valid mechanical checks
+
materially incomplete production meaning
```

The audit also established that these are distinct concepts:

```text
internal Objective Score / result
player-facing score/result display
telemetry/export payload
```

A prohibition on display/export does not erase internal scoring.

## Current semantic contract correction

The active Flow 2–4 semantic owners now require:

### Flow 2

- negative statements are not broadened beyond their actual scope;
- a source/file labelled `FINAL` does not automatically override higher-authority current instruction/approved decisions;
- every gameplay package resolves its Scoring / Result model as **Objective Score** or explicit **No Objective Score**;
- internal score/result, player-facing display, and telemetry/export stay separate when authority distinguishes them.

### Flow 3

- the target is **minimum complete production detail**, not minimal output;
- Golden is a **functional quality floor**, not only a hierarchy/template;
- Gameplay Flow is the chronological player journey with context, action, response, consequence, and transition;
- Level Design carries complete material build-relevant meaning;
- Developer carries complete material runtime/state/scoring-or-result/data/interruption/reset/handoff meaning;
- Global Development must not collapse important shared systems into vague summary text;
- every package keeps an explicit Scoring / Result contract;
- narrative/explanatory prose receives one bounded Humanize pass before projection.

### Flow 4

- semantic review performs a bounded material **source/requirement → PRD coverage** check;
- if Level Design or Developer must reopen the original source to discover a material requirement that belongs in the PRD, that is a **Major** finding;
- Golden quality is reviewed by production function, not word count or row count;
- default visual proof is **desktop-only** and targeted;
- normal visual smoke is limited to Overview + one Gameplay Flow + one Level Design + one dense Developer page unless a defect requires more.

## Mechanical proof remains separate

Existing mechanical contracts still cover deterministic concerns such as persisted Flow 2 state, hierarchy presence, scoring numeric sanity, generated page IDs/order, navigation, current HTML/render-data binding, and handoff-state consistency.

Those checks must not be presented as semantic completeness proof.

The current correction deliberately did **not** add:

- word-count validation;
- minimum row/note counts;
- semantic similarity scoring;
- generic schema/traceability framework;
- additional hash/checksum chain;
- mobile QA as a default requirement.

## Verification economy

Current direction:

```text
semantic/product change
→ inspect changed semantic owners
→ repository/CI gate if automatically applicable
→ one representative source-to-PRD review
→ one targeted desktop visual smoke only when needed
→ stop
```

Do not routinely replay mobile QA, every navigation interaction, every Terms disclosure, theme/localStorage behavior, unchanged Voice tests, or full-document rereads merely for ceremony.

The existing `content.md → render-data.json` SHA remains a candidate for later simplification because it catches stale bytes but does not prove semantic equivalence. No change to that mechanism is claimed in this semantic-contract correction.

## Current proof state by flow

| Flow | Current evidence state | Current note |
|---|---|---|
| 1. Repository Boot & Project Memory | **current repository/static proof** | Current evidence owner corrected; weak semantic PASS is no longer claimed. |
| 2. Source Intake & Requirement Recovery | **current semantic contract revised; new representative proof required** | Scoring/result authority interpretation and completeness threshold changed after user audit. |
| 3. PRD Generation | **current semantic contract revised; new representative proof required** | Golden functional quality floor, narrative Gameplay Flow, Development completeness, and PRD Humanize are now required. |
| 4. PRD Validation & Handoff | **current semantic contract revised; new representative proof required** | Source-to-PRD coverage and stricter role usability now block false semantic PASS. |
| 5–7. Voice | **unchanged** | Do not start Voice hardening until revised PRD quality is re-proven. |

## Current boundary

PRD Flow 2–4 is **not closed yet**.

The semantic contract has been corrected based on a concrete failed sample review, but a new representative PRD must still prove that the revised method produces a complete, human-readable, Golden-consistent production document.

That next proof should be desktop-only and targeted. Do not add more mechanical validation unless the new representative run exposes a specific deterministic defect.
