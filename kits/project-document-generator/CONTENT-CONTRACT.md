# Canonical PRD Content Contract

`work/content.md` is the human-readable source of truth. `render-data.json` and `final.html` are derived.

## Golden output contract

The approved Golden Sample defines both hierarchy and reusable page composition. Projects replace facts, not document language.

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

Keep the role pages even when local work is small; keep them concise and reference shared/global rules instead of inventing filler.

## Golden composition matrix

| Surface | Required rhythm | Optional when meaningful |
|---|---|---|
| Overview | project context → key production facts → full journey → shared systems | Terms Used |
| Gameplay Flow | stage/context → ordered narrative beats → result/transition | Terms Used |
| Global Development | title/subtitle → shared tabs → context → grouped production requirements | flow cards, note cards, Terms |
| Gameplay Overview | package title/label → 1/2/3 tabs → Context / Main Objective / Result → Gameplay Information → player flow | Terms |
| Level Design | package title/label → tabs → overview → Golden Build Requirements table | Design Flow, note cards, role Terms |
| Developer | package title/label → tabs → overview → grouped Golden Development Requirements | Development Flow, inline score/completion, reset/interruption, notes, role Terms |

A generic card/table body inside Golden CSS is not sufficient fidelity.

### Gameplay Information

Use only project-relevant rows from this family:

- Game Purpose;
- Gameplay Time;
- Starting Condition;
- End Condition;
- Fail Condition;
- Scoring Criteria or completion behavior.

Do not add empty/meaningless rows. Player flow is chronological experience, not developer trigger/data specification.

### Level Design table

Golden columns:

```text
No. | Object | Area Size | Build and Visual Requirements | Gameplay Function
```

Preserve the difference between **what is built** and **why gameplay needs it**. `Area Size` may remain unspecified/neutral if no authority defines it. Group/child rows may preserve meaningful hierarchy; do not flatten everything into generic requirement rows.

### Developer table

Golden columns:

```text
No. | Setup | Development Requirements | Gameplay Function
```

Preserve meaningful groups such as Mechanic Setup, Gameplay Setup, Scoring/Completion, and Reset only where the project has those concerns. Score/completion belongs inside the requirement hierarchy, not as an unrelated appendix table.

## Content authority and role ownership

1. **Source fidelity first.** Only source, supported recovery, and approved decisions define project meaning.
2. **Context before detail.** New readers understand the experience before implementation detail.
3. **One rule, one meaning.** Local reminders are allowed; semantic duplication/drift is not.
4. **Gameplay / Level Design / Developer stay separate.** Gameplay = intended player experience; Level Design = what must be built; Developer = runtime behavior/data/result.
5. **Local role usability.** A production role can work from its package plus relevant global rules without inventing product decisions.
6. **No filler.** Fixed Golden structure never authorizes invented metrics, architecture, dimensions, mechanics, tracking, lore, or decoration.
7. **No hidden decisions.** Material unresolved choices return to Flow 2.

## Flow 2 handoff boundary

`ready_for_prd` means Flow 3 receives project meaning that is already resolved enough to draft. Flow 3 may organize, clarify, and present approved meaning; it may not become the first place that these material issues are decided:

- package order, global/local ownership, transitions, or final result;
- required mechanic lifecycle behavior;
- contradictory counts/timing/scoring values;
- vague wording that would allow materially different product behavior;
- silent conflict between a shared/global rule and a local package exception;
- conflict with an authoritative known project/platform/production constraint;
- missing Gameplay / Level Design / Developer implications;
- removed/excluded behavior or terminology ambiguity;
- any other material product/design choice.

If drafting exposes one of these, return the affected requirement to Flow 2. Do not hide it with polished prose, a guessed value, a generic best practice, or a convenient renderer representation.

Qualitative direction is allowed when it is intentionally qualitative and production roles can act on it safely. Flow 3 must not invent metrics merely to make wording appear more precise.

## Information density

Keep a detail only when it:

- explains context needed to understand the work;
- changes what Level Design builds;
- changes what Developer implements/records;
- defines trigger, condition, quantity, timing, score, handoff, reset, or acceptance;
- prevents a production role from guessing.

Otherwise omit/compress it or reference the existing shared/global rule. Do not repeat global rules in full across packages or fill optional components just because visual space exists.

## PRD writing quality

Write plain production prose.

- state concrete behavior, condition, action, and consequence;
- remove promotional/inflated wording and fake-analysis tails that add no meaning;
- keep approved terminology stable instead of synonym cycling;
- do not force rhetorical patterns/rule-of-three phrasing;
- make the minimum effective edit and leave already-clear technical text alone;
- never style-edit IDs, official names, numbers, coordinates, timings, formulas, weights, triggers, conditions, state names, code/API names, or other authoritative values;
- apply prose cleanup mainly to narrative/explanation, not tables/formulas/configuration/code.

Example:

```text
Avoid: This objective serves as a pivotal moment that enhances the player experience and ensures a seamless transition.
Prefer: Completing this objective opens the next area and starts the following phase.
```

Clarity never outranks source fidelity.

## Document language

- English-only is default unless intentional EN + ID output is approved/produced.
- Expose Indonesian selection only when actual bilingual content exists.
- A localized `en`/`id` value in bilingual output must contain both sides; never silently copy the available language into the missing one.
- Proper names, IDs, codes, numbers, formulas, and intentionally language-neutral values may remain scalar.

Do not build translation-memory/localization machinery for this boundary.

## Scoring

If a package produces a score, define only facts the product needs:

- score name/scale when defined;
- components/weights when weighted scoring is used;
- target/success basis when relevant;
- bonus/reduction behavior when relevant;
- timer start/stop/excluded time when relevant;
- invalid/no-score condition;
- recorded data/duplicate prevention only when genuinely required;
- relationship to package/final result;
- exact formula only when product-critical.

Numeric component weights total 100% unless an approved model explicitly says otherwise.

## Non-scoring completion

Do not invent a score for a non-scoring package. Define actual completion behavior:

- `produces_score: false`;
- valid completion condition;
- recorded completion/progress data only when needed;
- interruption/duplicate prevention when relevant;
- handoff result.

Do not invent analytics, counters, persistence, or duplicate-prevention systems to fill a surface.

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
- scoring weights/inputs;
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
- each role surface has enough local context without filler;
- scoring/completion is explicit where relevant;
- explanatory prose is plain/concrete;
- no material Proposal/Blocked item affects requested scope;
- no unresolved placeholder remains.

A semantically correct document that cannot be projected into the Golden composition is not finished Flow 3 content for this document family.
