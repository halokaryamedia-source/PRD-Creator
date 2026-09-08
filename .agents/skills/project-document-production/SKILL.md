---
name: project-document-production
description: Semantic/product-contract specialist for PRD-Creator Flow 2–4 plus bounded non-Voice 04 Production Assets. Use when source recovery, project-model completion, canonical PRD meaning, 04 requirement meaning, or PRD readiness/handoff semantics are the actual problem. Presentation-only Golden questions route to the design owner.
---

# Project Document Production

Own **semantic judgment**. Detailed procedure, visual mechanics, and executable routing stay with the nearest package owner.

## Authority

```text
originals + current user instruction + approved decisions
→ recovered current project model
   ├─ canonical PRD meaning
   └─ justified non-Voice 04 requirements
→ acceptance / handoff
```

Generated output never becomes project authority. Golden/reference material supplies representation/quality evidence, not another project's facts.

## Use when

Semantic judgment is required for:

- source/requirement authority or completeness;
- Completion vs Proposal vs Blocked;
- whether a material choice genuinely needs user approval;
- canonical PRD meaning vs non-Voice 04 meaning;
- production-role actionability;
- PRD readiness/handoff;
- distinguishing missing meaning from a presentation defect.

Do not load this skill merely because a task mentions HTML, JSON, renderer, validator, ElevenLabs, or template.

## Detailed owners

```text
Flow 2 source recovery / completion / conditional review
→ kits/prd-creator/intake/SOURCE-INTAKE.md

PRD semantic completeness
→ kits/prd-creator/document/CONTENT-CONTRACT.md

Golden page/component grammar
→ kits/prd-creator/document/DESIGN-CONTRACT.md

non-Voice 04 meaning
→ kits/prd-creator/production-assets/CONTRACT.md

ElevenLabs non-dialogue Sound Effects craft / generation
→ kits/prd-creator/production-assets/SOUND-EFFECTS.md

Flow 4 semantic reconciliation / handoff
→ kits/prd-creator/document/VALIDATION.md

normal end-to-end execution
→ kits/prd-creator/SKILL.md
```

## Judgment rules

### Source / model completion

```text
current authority settles it
→ recover and continue

one necessary evidence-backed result exists
→ Completion and continue

multiple plausible material answers exist
→ one concrete Proposal → user review

no responsible proposal can be formed
→ Blocked / direct decision
```

Material AI Proposals require approval. Authoritative facts and evidence-backed Completions do not require a redundant review round-trip. Routine wording, grouping, ordering, decomposition, and production prompting are not project decisions.

### Canonical PRD

Flow 3 preserves current Flow 2 meaning without inventing product decisions or deleting independently actionable rules.

Semantic cardinality follows meaning. Preserve the actual number of distinct steps/items; do not compress or add filler to imitate a reference.

Stable product questions remain represented where required, including Gameplay Context, Main Objective, Result, and the six Gameplay Information concerns.

### Design / 04 / readiness

- If meaning is correct but visible Golden grammar is wrong, route to `document/DESIGN-CONTRACT.md`; do not alter project truth to fit presentation.
- Non-Voice 04 requirements come from the same current project model as the PRD; generated PRD pages are not a second brainstorming source.
- Non-dialogue `AUDIO` remains a normal 04 asset. ElevenLabs SFX prompt/settings decisions may interpret an approved Audio Brief but may not invent a new sound event, source, timing rule, or gameplay meaning.
- Voice semantics remain downstream Voice ownership. Do not put spoken dialogue into the SFX lane merely because an SFX model can emit voice-like audio.
- Mechanical PASS does not prove semantic completeness or visual/audio quality. Flow 4 reconciles current Flow 2 meaning → canonical content → projection → visible PRD.
- If a production role must reopen source for already-resolved PRD-scope meaning, readiness is defective.

## Routing boundary

```text
semantic meaning wrong
→ this specialist + nearest semantic owner

approved non-dialogue AUDIO meaning correct; ElevenLabs SFX craft/generation weak
→ production-assets/SOUND-EFFECTS.md

meaning correct; approved visual grammar wrong
→ document/DESIGN-CONTRACT.md

semantic + design contracts correct; executable behavior wrong
→ kits/prd-creator/AGENTS.md → exact implementation owner
```

## Proof economy

- start with the smallest current semantic owner/source;
- expand only for a dependency that can change the result;
- do not load full Golden/generated HTML for ordinary semantic review;
- do not substitute sample counts, word counts, similarity scores, checksums, or snapshots for semantic judgment;
- do not reconfirm already-authoritative facts;
- stop when the requested semantic boundary is correct and sufficiently proven.

## Boundary

This skill owns PRD/source/04/readiness **semantic judgment** only. Detailed procedure and executable mechanics stay with package owners; Voice stays downstream; generated `prd.html` is never source truth.
