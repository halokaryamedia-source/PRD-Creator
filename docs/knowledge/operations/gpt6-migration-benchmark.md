# GPT-6 Migration Benchmark

Date: 2026-09-07  
Status: prepared; actual GPT-6 execution pending an available model endpoint  
Primary repository baseline: `develop@e66979487af8cf7456372edf17c7de6061b3696a`  
Optional historical isolation baseline: `159da625fc8f3d3af33c57e3ad79719d6a7e66ed`

## Purpose

Use a small, repeatable behavioral benchmark to decide whether PRD-Creator's current instruction architecture remains correct and efficient on GPT-6, and whether any further simplification is justified by evidence.

This benchmark targets the **model-sensitive semantic/routing layer**. It does not retest deterministic Golden/template/renderer behavior that is already owned by repository regression tests.

The benchmark answers four questions:

1. Does the model preserve repository/project authority without inventing missing facts?
2. Does it choose the correct first owner and avoid replaying unrelated workflow stages?
3. Does it solve supported ambiguity before asking the user while still surfacing real material decisions?
4. Does the newer model reduce unnecessary reading/questions/tool use without losing material requirements?

## Non-goals

Do not turn this benchmark into:

- a permanent model API dependency;
- a required CI gate;
- a new root skill;
- a generic evaluation framework;
- a benchmark of renderer/validator correctness;
- a reason to redesign Golden;
- an API-key or credential store;
- an excuse to add scoring/checksum/proof machinery to normal production.

If these eight scenarios do not expose a real model-dependent failure, stop. Do not expand the benchmark merely because more cases could be written.

## Candidates

Run the same current repository baseline against:

```text
A. GPT-5.6 Sol + current develop baseline
B. GPT-6 Astra   + current develop baseline
```

Use the historical pre-simplification commit only when a current GPT-6 run fails or behaves ambiguously and the older instruction shape could plausibly explain the difference:

```text
C. GPT-6 Astra + 159da625...   # diagnostic only, affected scenarios only
```

Do not run a full matrix by default. The historical candidate exists only to isolate whether the recent router simplification caused a specific regression.

## Execution protocol

Each scenario is a **clean-session, read-only decision probe**. It measures semantic judgment and routing, not GitHub mutation mechanics.

For every run:

1. Start a clean model session with no previous project scenario context.
2. Pin the repository to the candidate ref before the model reads owners.
3. Give the model the fixed execution wrapper plus exactly one scenario prompt below.
4. Allow normal repository reads required by current `AGENTS.md` / owner routing.
5. Do not preload historical reviews, Golden HTML, unrelated Flow owners, or hidden project facts.
6. Do not allow repository writes; the model must state the intended action/owner instead.
7. Record the exact model identifier and reasoning setting used.
8. Record owner files read, total tool calls, clarification questions, and token/latency/cost usage when the execution environment exposes them.
9. Run each candidate once first.
10. Only if a scenario fails or is genuinely ambiguous, rerun that candidate/scenario up to two additional times to distinguish stable behavior from sampling variance.

### Fixed execution wrapper

Prepend this text to every scenario prompt:

```text
This is a read-only PRD-Creator model-migration evaluation.
Follow the current repository rules and owners at the pinned ref.
Treat the synthetic case below as the complete project/task context for this probe.
Do not modify GitHub or create project artifacts.

Return only:
- Decision class / state
- First canonical owner
- Smallest next action
- User question, only if one is actually required
- Scope that must remain untouched

Do not explain generic PRD-Creator architecture unless it changes this decision.
```

## Common scoring

A scenario is **PASS** only when all scenario-specific hard gates pass.

Across every scenario, the following are hard failures:

- inventing a project fact that is not supported by the synthetic authority;
- choosing a downstream/derived artifact as authority over its canonical owner;
- opening/replaying unrelated Flows without a demonstrated dependency;
- asking the user a broad or unnecessary question when current authority supports a safe Completion;
- silently converting a material AI choice into an approved fact;
- continuing after the requested decision boundary is already resolved.

Record these efficiency counters but do not use arbitrary absolute thresholds on the first migration run:

| Metric | Record |
|---|---|
| Correct decision/state | pass/fail |
| Correct first owner | pass/fail |
| Unsupported invention | count + description |
| Unnecessary user questions | count |
| Material requirement loss | count + description |
| Unjustified scope expansion | count + description |
| Owner/source reads | count + paths |
| Total tool calls | count |
| Verification breadth | targeted / broad / none-required |
| Stop behavior | pass/fail |
| Input/output tokens | value if exposed |
| Latency | value if exposed |
| Cost | value if exposed |

### Migration acceptance

The current instruction baseline is behaviorally acceptable for a candidate model when:

```text
8 / 8 scenarios PASS
AND
0 unsupported material inventions
AND
0 unresolved Proposal is treated as approved
AND
0 real external-fact blocker is guessed
AND
0 technical-only defect is routed through unnecessary semantic replay
```

Efficiency is comparative evidence, not an independent quality gate. If GPT-6 preserves all hard gates while using fewer owner reads, fewer unnecessary questions, or fewer tool calls, that is a valid optimization signal. If it is more efficient but loses material meaning or authority discipline, it is a regression.

## Scenario 1 — Safe Completion instead of unnecessary question

### Synthetic case

```text
The project is a timed parkour trial.
Authoritative source says:
- the timer begins when the player crosses the start gate;
- the maximum run time is 120 seconds;
- the score is the number of seconds remaining when the run is completed;
- valid completion occurs when the player crosses the finish line.

The source does not separately state the sentence "the timer stops at the finish line".
The task is to complete the project model enough for PRD production.
```

### Expected

```text
Decision class: Completion
First owner: Flow 2 / intake/SOURCE-INTAKE.md
Next action: normalize the implied timer-stop rule as derived Completion, then include it in the reviewable project model
User question: none
Untouched: document design, Golden, Voice, unrelated project choices
```

### Hard gates

- Recognizes that remaining-time scoring plus valid finish implies stopping the run timer on valid finish.
- Does not ask the user to choose a timer-stop event.
- Does not invent grace periods, countdown presentation, rewards, VFX, or other mechanics.

## Scenario 2 — Material ambiguity must remain a Proposal

### Synthetic case

```text
The accepted concept says a boss becomes vulnerable only after three pylons are activated.
The current authoritative source explicitly says the three pylons may be activated either sequentially or simultaneously.
No current decision chooses between those two interaction models.
The task is to make the project model production-complete.
```

### Expected

```text
Decision class: Proposal / pending approval
First owner: Flow 2 / intake/SOURCE-INTAKE.md
Next action: choose one concrete responsible default as a Proposal, surface it once for approval/correction, and keep ready_for_prd false until resolved
User question: only the focused approval/correction boundary represented by the Proposal; no broad discovery interview
Untouched: Flow 3 rendering, Golden, downstream Voice
```

### Hard gates

- Does not call either interaction model an evidence-backed Completion.
- Produces one concrete Proposal rather than an open-ended list of possibilities.
- Does not mark the project ready for PRD before the material proposal is approved/corrected.

## Scenario 3 — Real external fact must Block

### Synthetic case

```text
A sponsor reward is required at valid completion.
The requirement says the voucher amount must exactly match the sponsor-approved value.
None of the current project sources, approved decisions, or instructions contains that amount.
The task is to finalize the player-facing reward requirement.
```

### Expected

```text
Decision class: Blocked / needs external decision
First owner: Flow 2 / project authority
Next action: request the missing sponsor-approved amount as one focused material fact
User question: ask only for the approved voucher value
Untouched: PRD rendering, asset styling, Voice, implementation details
```

### Hard gates

- Does not invent or estimate a voucher value.
- Does not replace the missing value with a vague placeholder and claim readiness.
- Does not broaden the question into unrelated sponsor/reward discovery.

## Scenario 4 — Bounded revision with selective downstream invalidation

### Synthetic case

```text
The project is already accepted.
Objective 2 currently has a 45-second limit.
The user now explicitly changes only Objective 2 to 60 seconds.

Current dependent state:
- canonical PRD Objective 2 says 45 seconds;
- the Objective 2 scoring formula uses elapsed time but remains structurally valid when the limit changes;
- one Voice requirement/script says "You have 45 seconds";
- no other objective refers to this timer.

The task is to apply the approved change.
```

### Expected

```text
Decision class: approved bounded revision
First owner: affected project/PRD canonical meaning for Objective 2
Next action: update the Objective 2 timer, propagate only affected scoring text and the affected Voice requirement/script, rerender once after canonical state is stable, then run targeted relevant validation
User question: none
Untouched: unrelated objectives, Golden/template, unrelated Voice moments, full source re-inventory
```

### Hard gates

- Detects that the Voice line is genuinely invalidated and must be reopened.
- Does not reopen all Voice work or all PRD packages.
- Does not treat the scoring system as a new design problem merely because its numeric input changed.
- Does not rerun the full source-intake workflow for an explicit approved change.

## Scenario 5 — Production Assets without decorative invention

### Synthetic case

```text
The approved project model requires:
- one custom physical pedestal that the player interacts with;
- exact HUD copy: "INSERT CORE" while the pedestal is waiting for interaction.

No source specifies a custom animation, particle effect, sound, lore inscription, material palette, or exact numeric dimensions.
The task is to determine required non-Voice Production Assets.
```

### Expected

```text
Decision class: supported 04 Production Asset extraction
First owner: production-assets/CONTRACT.md using the approved project model
Next action: require the pedestal MODEL resource and the UI / TEXT resource with the exact approved copy; omit unsupported optional decoration
User question: none
Untouched: gameplay behavior, Golden 01–03, Voice
```

### Hard gates

- Includes only resources actually required for production.
- Does not invent VFX, audio, animation, lore, exact size, or visual style merely to make the brief richer.
- Keeps gameplay/runtime rules in their existing semantic owners rather than disguising them as assets.

## Scenario 6 — Voice extraction must preserve scope, not write performance

### Synthetic case

```text
The current accepted PRD requires a narrator message at trial start.
The player must understand two facts before active play:
1. collect exactly five shards;
2. return to the central pedestal after collecting them.

The accepted project defines no other Voice moment for this objective.
The task is Flow 5 Voice Requirement Extraction.
```

### Expected

```text
Decision class: voice_requirements_ready for one justified moment
First owner: voice/EXTRACTION.md
Next action: define one Voice requirement with accepted Speaker/Channel/Trigger/Purpose and both Must communicate facts
User question: none unless an actually required Speaker/Channel fact is absent from the synthetic authority
Untouched: final dialogue wording, performance tags, actor selection, additional Voice moments
```

### Hard gates

- Preserves both required communication facts.
- Does not write final performance copy as the Flow 5 output.
- Does not create extra narration because a reference/example might contain more Voice.

## Scenario 7 — Voice writing must conserve communication

### Synthetic case

```text
Flow 5 is already accepted for VO-TRIAL-01.
Speaker: Narrator.
Purpose: brief the player before the trial begins.
Must communicate:
- collect exactly five shards;
- return to the central pedestal afterward.
Must not add:
- rewards;
- lore about the origin of the shards;
- new gameplay instructions.

The task is Flow 6 canonical Voice Production using Eleven v3 performance-writing rules.
```

### Expected

```text
Decision class: Flow 6 production-ready wording task
First owner: current Flow 6 policy + voice/PERFORMANCE-WRITING.md
Next action: write concise natural production copy that begins with valid performance direction, preserves both required facts, adds no prohibited project meaning, and records owned Flow 6 production metadata
User question: none when the accepted Voice contract is sufficient
Untouched: Voice scope/trigger/purpose, upstream PRD/gameplay meaning
```

### Hard gates

- Both communication requirements survive in the final wording.
- No reward/lore/new mechanic is invented.
- Does not return to Flow 5 merely to polish performance wording.
- Does not claim generated-audio quality without audio evidence.

## Scenario 8 — Technical defect must route to the implementation owner

### Synthetic case

```text
The canonical Production Asset requirement is correct and accepted.
The generated consolidated HTML renders two Production Asset cards with the same DOM id, breaking navigation.
The semantic requirement, resource type, wording, and objective mapping are all correct.
The task is to fix the defect in PRD-Creator itself.
```

### Expected

```text
Decision class: bounded technical Maintenance
First owner: nearest renderer/compositor implementation owner under kits/prd-creator/
Next action: reproduce the duplicate-id mechanics, fix the implementation source, add/update only the regression proof needed for that defect, and rerun the targeted PRD gate
User question: none
Untouched: Flow 2 project meaning, Production Asset semantics, Voice semantics, root skill count, Golden design unless evidence proves the template itself is wrong
```

### Hard gates

- Does not reopen source intake or semantic project approval.
- Does not create a new renderer/Python/root specialist.
- Does not redesign Production Assets to avoid fixing the duplicate-id implementation bug.
- Verification remains targeted unless the implementation change proves a broader surface is affected.

## Result sheet

Do not fill a model result from expectation or static inspection. Record only an actual isolated run.

| Scenario | GPT-5.6 Sol current | GPT-6 Astra current | Notes / actual divergence |
|---|---|---|---|
| 1 Safe Completion | NOT RUN | NOT RUN | |
| 2 Proposal | NOT RUN | NOT RUN | |
| 3 Blocked external fact | NOT RUN | NOT RUN | |
| 4 Bounded revision | NOT RUN | NOT RUN | |
| 5 Production Assets | NOT RUN | NOT RUN | |
| 6 Voice extraction | NOT RUN | NOT RUN | |
| 7 Voice writing | NOT RUN | NOT RUN | |
| 8 Technical routing | NOT RUN | NOT RUN | |

### Run summary template

```text
Model:
Exact model/version:
Reasoning setting:
Repository ref:
Date:

Hard PASS: X/8
Unsupported inventions: X
Unnecessary questions: X
Material-loss findings: X
Scope-expansion findings: X
Total owner/source reads: X
Total tool calls: X
Tokens/latency/cost: <record when exposed>

Observed strengths:
- ...

Observed regressions:
- ...

Recommendation:
KEEP CURRENT INSTRUCTIONS | TARGETED ADJUSTMENT | REVERT/COMPARE AFFECTED ROUTER SLICE
```

## Interpretation rule

Do not optimize for fewer tokens or fewer tool calls in isolation.

Use this ordering:

```text
authority correctness
→ material conservation
→ correct owner / dependency routing
→ responsible autonomy vs necessary question
→ targeted proof / stop behavior
→ efficiency
```

A faster model that invents one material project fact is worse. A slightly more expensive model that preserves all project meaning and removes unnecessary clarification loops may be better for this product.

If GPT-6 passes all eight scenarios, keep the current architecture and stop. Further prompt simplification then requires a separately observed failure or measurable efficiency problem, not the existence of a newer model.

If GPT-6 fails one or more scenarios, change only the smallest instruction owner implicated by those failures. Use the historical `159da625...` baseline only for the failing scenarios when that comparison can isolate whether the recent router simplification caused the behavior.

## Current evidence boundary

This file defines the benchmark and expected behavior. It does **not** claim that GPT-6 has passed it.

At creation time, this ChatGPT execution environment does not expose an installed GPT-6 model-execution endpoint. Therefore:

```text
benchmark definition   → COMPLETE
current repo baseline  → PINNED
deterministic repo CI  → separate existing evidence
GPT-5.6 isolated run   → NOT RUN
GPT-6 isolated run     → NOT RUN
cross-model conclusion → NOT YET PROVEN
```

Do not convert `NOT RUN` to PASS from model documentation, marketing claims, static repository inspection, or expected-answer review. Only actual isolated candidate runs may populate the result sheet.
