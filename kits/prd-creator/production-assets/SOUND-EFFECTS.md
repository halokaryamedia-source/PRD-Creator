# ElevenLabs Sound Effects Production

Status: active Production Assets AUDIO procedure. This is the coordinator; load references selectively.

## Authority and scope

`work/asset-requirements.md` owns required non-dialogue AUDIO meaning under existing Owner / Moment / AST identity. Read the matching requirement first, then only missing accepted context or approved same-project audio evidence. Do not invent required states, materials, gameplay timing, or new AST IDs for temporary production layers.

Spoken dialogue/narration stays in Voice Requirements → Voice Production → Voice Delivery. This capability remains inside Production Assets, not a new root skill, numbered workflow, canonical manifest, or lifecycle schema. Prompt/settings, family notes, and audio files are execution evidence, not new project truth.

## Read only what changes the decision

Start here. For a simple approved sound, use the matching archetype section; do not load the entire reference collection. Before paid execution, also read the execution/budget owner and the relevant verified surface contract. Reuse that context for the batch; revisit sources only for a material conflict or changed surface/account.

| Need | Exact reference |
|---|---|
| Product facts, source conflicts, supported controls | [Contracts and sources](sfx/references/elevenlabs-contracts-and-sources.md) |
| Translate an audible brief into a prompt | [Prompting archetypes](sfx/references/prompting-archetypes.md) |
| Recurring source, states, reuse and variation | [Families and variation](sfx/references/families-and-variation.md) |
| Sync, loops, layers, source versus playback space | [Timing, loops and layering](sfx/references/timing-loops-and-layering.md) |
| Any paid request, executor, budget or retry | [Execution and cost control](sfx/references/execution-and-cost-control.md) |
| Candidate diagnosis, file QA, evidence or delivery | [Validation and delivery](sfx/references/validation-and-delivery.md) |
| Explicit Minecraft Bedrock target only | [Bedrock delivery](sfx/references/minecraft-bedrock-delivery.md) |

## Preparation Mode

Default for research, writing, implementation, review, or tests: **zero paid requests**. Implementing this skill does not authorize generation.

```text
approved AUDIO intent
→ inspect reusable approved assets
→ choose audible archetype and independent production dimensions
→ family baseline only when needed
→ one exact prompt + intentional settings
→ readiness review / operator handoff
```

Choose these dimensions independently, not as mutually exclusive modes:

| Dimension | Choices |
|---|---|
| Temporal form | one-shot / loop / sequence |
| Relationship | standalone / family state |
| Composition | single source / layered |

A machine idle can be a loop, a family state, and a layered effect simultaneously. Keep these as reasoning context, not schema fields. Separate required timing from a reversible production duration choice.

Before API execution, use `tools/prd.py sfx-check` on the exact native request and current batch counters; command details are in the execution reference. It is offline and read-only. Its PASS does not reserve allowance, authorize spending, or replace semantic/audio review.

## Generation Mode

**No paid request without explicit generation authorization and a finite approved batch budget.** Prompt approval is not spend approval. Do not renew the budget after a context reset or quality approval.

```text
recover approved scope + budget + prior attempts
→ preflight surface, rights, parameters and output path
→ reserve next request within all limits
→ generate one candidate unit
→ retain file / reconcile cost and request outcome
→ listen and compare existing candidates
→ accept OR diagnose / edit before considering another paid request
```

Validate one representative family state before expanding costly dependent states. Default to serial execution. Every retry counts; an unknown timeout stays reserved until reconciled. Never auto-top-up, upgrade plans, or switch to another paid service to bypass a limit.

## Quality and revision rules

Describe the event/source first, then only relevant material, time shape, perspective, and character. A short prompt is not automatically a cheaper ElevenLabs request. Preserve intent and editability rather than filling a character limit.

Use current documented defaults as a starting point, not universal quality presets. Text instructions cannot guarantee exact identity, timing, silence, or looping. Keep requested settings distinct from measured results.

Diagnose the first actual defect:

- wrong requirement → Production Assets;
- correct requirement, mistranslated prompt → prompt craft;
- correct brief/prompt, isolated bad output → compare existing candidates;
- valid sound with repairable silence, level or edit point → edit a copy;
- recurring audible defect → one justified variable-class change within remaining budget.

Do not spend again merely to establish repetition when a configuration error is already clear. One improved stochastic take does not establish a universal prompting rule. Accepted candidate = stop, even with unused budget. Reopen only invalidated scope.

## Evidence and stop boundary

Keep exact prompt/settings, AST ID, selected file/take, attempt/remaining-budget note and useful measurements in the existing project execution evidence. No duplicate asset database. Preserve approved originals and distinguish edited derivatives. Recover this evidence before continuing another session.

**SFX Production Readiness: PASS** means ready to generate, not audio approval or permission to spend. Distinguish prepared, generated-unreviewed, audio-accepted, and target-verified evidence; these descriptions do not add lifecycle values. Heard quality requires heard evidence; in-game behavior requires in-game evidence.

Budget exhausted, ambiguous charge, missing authorization, unavailable executor, or no review capability for further iteration → stop paid work and return the prepared/partial result with the exact unresolved boundary. Do not lower quality requirements to manufacture a PASS.

This is an agent/operator policy, not an executable billing firewall. Static tests protect documentation contracts; they do not enforce provider spending or prove acoustic quality. Core runtime dependencies, Voice, Golden UI, and canonical parsers remain unchanged.
