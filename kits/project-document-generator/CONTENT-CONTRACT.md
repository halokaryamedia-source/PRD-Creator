# Canonical PRD Content Contract

`work/content.md` is the human-readable source of truth. `render-data.json` and `final.html` are derived.

## Golden output contract

The approved Golden Sample defines both hierarchy and reusable page composition **and acts as the functional quality floor for this gameplay PRD family**. Projects replace facts, not document function.

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

A project does not copy Golden-specific mechanics, counts, wording, lore, or scoring. It must preserve what each surface accomplishes for its reader. Keep the role pages even when local work is small; keep them concise only after all material production meaning is present.

**No filler does not mean minimal document.** The target is complete material information with no useless repetition.

## Golden composition matrix

| Surface | Required rhythm | Optional when meaningful |
|---|---|---|
| Overview | project context → key production facts → full journey → shared systems | Terms Used |
| Gameplay Flow | player/stage context → chronological player-story beats → system/NPC/environment response → result/transition | Terms Used |
| Global Development | title/subtitle → shared tabs → context → grouped production requirements | flow cards, note cards, Terms |
| Gameplay Overview | package title/label → 1/2/3 tabs → Context / Main Objective / Result → Gameplay Information → player flow | Terms |
| Level Design | package title/label → tabs → overview → Golden Build Requirements table | Design Flow, note cards, role Terms |
| Developer | package title/label → tabs → overview → grouped Golden Development Requirements including Scoring/Result | Development Flow, reset/interruption, notes, role Terms |

A generic card/table body inside Golden CSS is not sufficient fidelity. A visually correct page that omits material source meaning is not Golden-quality output.

## Golden quality floor

Use the Golden Sample as a **functional comparison**, not a word-count target.

For the corresponding project surface, ask:

```text
Does this page give its reader the same level of production understanding
that the Golden page gives its reader,
using only current-project supported meaning?
```

Do not enforce arbitrary minimum words, paragraphs, rows, or notes. Those create filler. Instead preserve every material requirement that changes player experience, build scope, runtime behavior, scoring/result, data, interruption/reset, or handoff.

If the Golden page demonstrates an important type of information that also exists in the current project, that current-project information must not disappear merely because the source is being summarized.

## Gameplay Flow = chronological player journey

Gameplay Flow is the **story of what the player experiences**, written for a production team. It is not a developer task list, abstract flowchart caption, or three-step summary.

A good Gameplay Flow normally preserves this sequence where applicable:

```text
where the player comes from / current situation
→ what the player sees or understands
→ NPC / instruction / system cue
→ what the player does
→ how the environment or system responds
→ what changes because of that action
→ what the player now carries / knows / can access
→ result and transition into the next beat
```

Use enough narrative beats to explain the actual experience. Important feedback, setbacks, recovery, visible state change, NPC response, item handoff, and route opening/closing belong here when they materially shape what the player experiences.

Keep it production prose rather than novel prose. Do not invent dialogue, cinematic detail, animation, lore, or mechanic behavior merely to make the flow feel richer.

## Gameplay Information

Use project-relevant rows from this family:

- Game Purpose;
- Gameplay Time;
- Starting Condition;
- End Condition;
- Fail / Retry / Blocked Condition;
- **Scoring / Result behavior**.

The Scoring / Result row is always meaningful for a gameplay package because the production team must know whether the package creates an Objective Score or explicitly does not.

Do not add empty/meaningless rows. Player flow is chronological player experience, not developer trigger/data specification.

## Scoring / Result contract — required for every package

Every gameplay package must state its result model explicitly.

### Scored package

Define only facts the product needs:

- Objective Score name/scale when defined;
- components/weights when weighted scoring is used;
- target/success basis when relevant;
- bonus/reduction behavior when relevant;
- timer start/stop/excluded time when relevant;
- invalid/no-score condition;
- recorded score/result data and duplicate prevention only when genuinely required;
- relationship to package/final result;
- exact formula only when product-critical.

Numeric component weights total 100% unless an approved model explicitly says otherwise.

### Non-scored package

Do **not** omit the scoring/result section. State explicitly:

```text
No Objective Score
```

and define the actual completion/result behavior:

- `produces_score: false`;
- valid completion condition;
- recorded completion/progress data only when needed;
- interruption/duplicate prevention when relevant;
- handoff result;
- relationship to final result, including that the package does not contribute an Objective Score when applicable.

### Keep three concerns separate

Never collapse these into one meaning unless authority explicitly does so:

```text
1. Internal scoring/result
   Does the package calculate/store an Objective Score or only completion?

2. Player-facing display
   Is score/result shown to the player?

3. Telemetry/export
   Is score/result included in raw events, exported data, reports, or another downstream payload?
```

`Do not display score` does **not** mean `No Objective Score`.

`Do not export score` does **not** mean `No Objective Score`.

A source that hides score from players or telemetry may still require internal Objective Score calculation and final-total contribution.

## Level Design table

Golden columns:

```text
No. | Object | Area Size | Build and Visual Requirements | Gameplay Function
```

Preserve the difference between **what is built** and **why gameplay needs it**. `Area Size` may remain unspecified/neutral if no authority defines it. Group/child rows may preserve meaningful hierarchy; do not flatten everything into generic requirement rows.

### Level Design completeness

Carry all material build-relevant meaning supported by the project, including when applicable:

- required areas and sub-areas;
- objects/machines/markers/hazards;
- route and spatial relationships;
- sightlines/readability/visible destination;
- known dimensions or size constraints;
- safe landing/recovery areas;
- interaction placement and player access;
- entry/exit/reset boundaries;
- build/visual requirements;
- gameplay function;
- important notes that prevent a materially wrong build.

Do not compress several distinct build requirements into one vague row when a Level Designer would need to reopen the source to understand what to build.

## Developer table

Golden columns:

```text
No. | Setup | Development Requirements | Gameplay Function
```

Preserve meaningful groups such as Mechanic Setup, Gameplay Setup, Scoring/Result, Data, Interruption/Reset, and Handoff where those concerns apply. Scoring/result belongs inside the requirement hierarchy, not as an unrelated appendix table.

### Developer completeness

Carry all material runtime meaning supported by the project, including when applicable:

- activation / preconditions;
- interaction behavior;
- progression/state changes;
- quantities and timing;
- success/completion;
- Objective Score **or explicit No Objective Score**;
- score/result relationship to the final result;
- player-facing score/result display rules;
- telemetry/export/data rules;
- invalid/no-score behavior;
- interruption/disconnect/pause;
- retry/reset/cleanup;
- transition/handoff;
- important implementation notes that prevent materially wrong behavior.

A shared/global rule may be referenced instead of repeated, but the package page must still make clear **which shared rule applies and what local behavior depends on it**. A generic “follow global rules” reference is insufficient when the developer must search elsewhere to discover a material local implication.

## Global Development completeness

Global Development owns project-wide behavior that multiple packages depend on. Do not collapse several distinct shared systems into a short summary merely to reduce page count.

Keep separate shared ownership when it materially helps production understand concerns such as:

- session / arena ownership;
- shared player state and permissions;
- timing/pause/rejoin behavior;
- shared score/final-result aggregation;
- shared telemetry/data/export rules;
- global reset/cleanup;
- common gameplay-package lifecycle or handoff behavior.

Combine only when one coherent shared system genuinely owns the rules. Page count is not a goal.

## Content authority and role ownership

1. **Source fidelity first.** Current user instruction, approved decisions, and authoritative source define project meaning through the repository authority chain.
2. **Do not over-broaden exclusions.** A prohibition on display/export is not a prohibition on internal scoring or storage unless authority says so.
3. **Context before detail.** New readers understand the experience before implementation detail.
4. **One rule, one meaning.** Local reminders are allowed; semantic duplication/drift is not.
5. **Gameplay / Level Design / Developer stay separate.** Gameplay = intended player experience; Level Design = what must be built; Developer = runtime behavior/data/result.
6. **Local role usability.** A production role can work from its package plus clearly referenced global rules without reopening original source to recover omitted material requirements.
7. **No filler.** Fixed Golden structure never authorizes invented metrics, architecture, dimensions, mechanics, tracking, lore, or decoration.
8. **No hidden decisions.** Material unresolved choices return to Flow 2.

## Flow 2 handoff boundary

`ready_for_prd` means Flow 3 receives project meaning that is already resolved enough to draft. Flow 3 may organize, clarify, and present approved meaning; it may not become the first place that these material issues are decided:

- package order, global/local ownership, transitions, or final result;
- required mechanic lifecycle behavior;
- contradictory counts/timing/scoring values;
- distinction between internal score, player-facing display, and telemetry/export when source statements could be confused;
- vague wording that would allow materially different product behavior;
- silent conflict between a shared/global rule and a local package exception;
- conflict with an authoritative known project/platform/production constraint;
- missing Gameplay / Level Design / Developer implications;
- removed/excluded behavior or terminology ambiguity;
- any other material product/design choice.

If drafting exposes one of these, return the affected requirement to Flow 2. Do not hide it with polished prose, a guessed value, a generic best practice, or a convenient renderer representation.

Qualitative direction is allowed when it is intentionally qualitative and production roles can act on it safely. Flow 3 must not invent metrics merely to make wording appear more precise.

## Information density

Use this rule:

```text
complete material information
+
no useless repetition
```

Keep a detail when it:

- explains context needed to understand the work;
- changes what the player experiences;
- changes what Level Design builds;
- changes what Developer implements/records;
- defines trigger, condition, quantity, timing, score/result, display/export rule, handoff, reset, or acceptance;
- prevents a production role from guessing or reopening the original source.

Otherwise omit/compress it or reference the existing shared/global rule. Do not repeat global rules in full across packages or fill optional components just because visual space exists.

## PRD Humanize pass

After the canonical meaning is complete and before projection, apply one bounded Humanize pass to narrative and explanatory prose.

### Humanize should

- use natural production English;
- explain context before instructions;
- prefer cause → action → response → consequence order;
- split comma-stacked requirement dumps into readable sentences when that improves comprehension;
- keep paragraphs scannable without turning them into fragments;
- use stable project terminology;
- make Gameplay Flow feel like a clear account of the player journey;
- make Level Design and Developer overviews explain the work before the tables provide dense detail.

### Humanize must not

- change official names/terminology;
- change quantities, timings, coordinates, formulas, scoring weights, triggers, conditions, state names, code/API names, or other authoritative values;
- soften uncertainty or approval state;
- add cinematic/lore detail unsupported by authority;
- inflate simple requirements with promotional or theatrical language;
- rewrite tables/formulas/configuration merely for style.

Example:

```text
Avoid:
Implement custom-ore breaking, one-item drops, scripted deposits, station-restricted inventory, meter progression, unlocks, and reset.

Prefer:
The Quarry controls the complete mining loop. Breaking an active ore block gives exactly one matching ore item and prevents the tool from affecting the surrounding environment. Depositing that ore at the Forge updates the approved progression state and unlocks the next stage when its requirement is met.
```

Clarity never outranks source fidelity.

## Document language

- English-only is default unless intentional EN + ID output is approved/produced.
- Expose Indonesian selection only when actual bilingual content exists.
- In intentional bilingual output, every user-visible textual value must explicitly provide both `en` and `id`; never treat an ordinary scalar sentence/label/name as an implicit translation.
- If a displayed proper name is intentionally identical in both languages, state it explicitly as the same `en` and `id` value.
- Scalar strings remain valid only for non-linguistic/structural values the renderer defines as language-neutral, such as stable IDs/keys/codes, version/brand mark, language/role tokens, numeric weights, step/row identifiers, canonical revision hash, and an exact formula.

Do not build translation-memory/localization machinery for this boundary.

## Terms Used

Use Terms only for project-specific/production-critical terminology. Each term has a stable key, label, concise definition, and optional aliases.

Package terms share one glossary/tooltips source:

- default visible block → Gameplay Overview;
- Level Design / Developer visibility → only when that role benefits;
- glossary/tooltips-only → valid when no visible role block needs it.

Do not repeat the same visible glossary block across all role pages by default.

## Critical information

When relevant, treat these as critical:

- player/session/arena count;
- package/stage order;
- important quantities/dimensions;
- target time/timer boundaries;
- Objective Score vs explicit No Objective Score;
- scoring weights/inputs and final-result relationship;
- player-facing score/result display rules;
- telemetry/export rules when source distinguishes them;
- completion and invalid/no-score conditions;
- handoff items/state;
- interruption/disconnect behavior;
- reset behavior;
- final-result rules.

If required critical information remains unresolved, return it to Flow 2 rather than hiding the gap behind vague text or polished layout.

## Canonical-content gate

`content.md` is ready for projection when:

- Flow 2 is truthfully `ready_for_prd`;
- material statements trace to source/recovery/approved decisions;
- no Flow 2 handoff issue above was silently decided during drafting;
- Golden hierarchy/page composition is represented;
- Golden functional quality is preserved for the current project without copying sample facts;
- Gameplay Flow explains the chronological player journey rather than only task steps;
- every package has an explicit Scoring / Result contract;
- each role surface contains complete material role-owned meaning without filler;
- a Level Designer or Developer does not need the original source to recover a material rule that belongs in the PRD;
- explanatory prose has received the bounded Humanize pass;
- no material Proposal/Blocked item affects requested scope;
- no unresolved placeholder remains.

A semantically correct document that cannot be projected into the Golden composition is not finished Flow 3 content for this document family. A structurally complete document that omits material production meaning is also not finished.
