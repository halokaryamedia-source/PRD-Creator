# Eleven v3 Performance Script Production

Flow 6 converts approved Flow 5 Voice Requirements into canonical Eleven v3 wording and a production-ready DOCX. It does not add Voice scope or upstream project facts.

## Entry gate

Start only when `state/voice-state.yaml` has:

```yaml
status: voice_requirements_ready
```

The referenced Voice Requirements and accepted PRD revision must still be current.

## Authority

Use:

1. `work/voice-requirements.md` — normal Flow 5 → Flow 6 interface and required meaning;
2. accepted `work/content.md` — only when the requirement does not already carry enough delivery-relevant context;
3. current `work/voice-production.md` — canonical wording when revising;
4. `SOUNDMAKER.md` — Eleven v3 preparation/generation procedure;
5. `references/elevenlabs/` — deep technical reference only when needed;
6. `DOCX-FORMAT.md` + Aftershock reference — presentation only.

Recover available facts before asking the user. Do not reopen the full PRD by default when the Flow 5 requirement is already complete enough to author responsibly.

Production technique may shape **how** approved meaning is performed. It may not create a new project fact, Voice ID, Speaker, Channel, Trigger, mechanic, reward, outcome, or authoritative timing rule.

## Working modes

### Preparation Mode — default for script/DOCX work

```text
all current Voice Requirements
→ Voice Intent Completeness / Performance Fill Map
→ SoundMaker authoring per Voice ID
→ Communication Conservation
→ integrated Voice Script Readiness
→ canonical work/voice-production.md
→ derived DOCX when requested
```

Batch preparation is allowed. Do not force audio generation/testing or per-line approval loops.

### Generation Mode — only when actual ElevenLabs work is requested

```text
one active Voice ID
→ exact reviewed prompt
→ generate / revise / approve
→ synchronize approved prompt back to canonical script
```

Generation remains one Voice ID at a time to preserve prompt/settings/evidence clarity.

# Output contract

Keep canonical script, operator handoff, and DOCX distinct. Do not create another handoff artifact merely to duplicate them.

## Canonical script

`work/voice-production.md` owns only stable production metadata plus the exact Eleven v3 wording:

```text
# <Project> Voice Production
Version: <script version>
Source Voice Requirements: <revision/reference>

## 01. <Gameplay Section>

### <VOICE-ID> — <Title>
Type: <exact Flow 5 type>
Speaker: <exact Flow 5 speaker>
Estimated Duration: <range>

```performance
<exact Eleven v3 text>
```
```

Required entry fields are exactly:

- stable Voice ID + title;
- `Type`;
- `Speaker`;
- `Estimated Duration`;
- exact `performance` block.

Do not duplicate Channel, Trigger, Purpose, `Timing Constraint`, `Must communicate`, `Must not add/repeat`, source refs, Performance Fill Map reasoning, WPM math, voice-fit ratings, or QA notes into the canonical script. Those remain in their owning Flow 5/internal context.

Every Flow 5 Voice ID must appear exactly once unless Flow 5 is explicitly reopened. `Type` and `Speaker` must match Flow 5 exactly.

## Operator handoff

Derive a concise operator view from current authority. State shared speaker/setup once when useful, then show each active Voice ID with Speaker, Estimated Duration, and exact prompt. Show an external production note only when the operator must take an additional action such as pronunciation setup, an authoritative hard/fixed timing requirement, Fixed Duration, or Studio routing.

## DOCX

`output/Voice Production.docx` is derived presentation. It exposes `Type · Speaker`, Voice ID/Title, Estimated Duration, and Performance Script. It is not a settings database, requirement register, or wording authority.

# Flow 5 → Flow 6 intent mapping

Use the Flow 5 entry as the normal source for Voice Intent Completeness:

```text
Communication Job   ← Function + Purpose
Listener State      ← Trigger + Channel
Information Payload ← Must communicate
Listener Outcome    ← Purpose
Speaker Owner       ← Speaker
Hard Timing Truth   ← optional Timing Constraint
Scope Guardrails    ← Must not add/repeat
```

Only reopen accepted PRD context when a delivery-relevant detail cannot responsibly be recovered from this interface.

Rules:

- `Purpose` supplies the listener-facing communication result, not performance prose;
- `Trigger` supplies the event/state and relevant listener condition when material;
- `Must communicate` is authoritative payload and must not be treated as optional inspiration;
- optional `Timing Constraint` is upstream truth only when explicitly present;
- Flow 6 `Estimated Duration` is a production estimate and must not overwrite or masquerade as a Flow 5 timing constraint;
- Performance Shape and Landing remain SoundMaker interpretation unless upstream authority actually constrains them.

If the Flow 5 entry lacks a material listener state, listener outcome, Speaker/Channel/Trigger, required fact, or authoritative timing truth needed to build the correct asset, return only that issue to Flow 5/upstream instead of improvising.

# Authoring contract

Use `SOUNDMAKER.md` as the single operational quality procedure. Do not duplicate its detailed v3 writing rules here.

For each Voice ID:

1. complete the **Voice Intent** from the Flow 5 interface first;
2. honor any authoritative timing constraint, then plan Estimated Duration when timing is material;
3. write the performance using approved meaning and speaker identity;
4. run **Communication Conservation** against Flow 5;
5. mark the line script-ready only when SoundMaker's per-line gate passes.

### Voice Intent Completeness

Flow 6 must be able to resolve, as applicable:

```text
communication job
listener state
information payload
listener outcome
speaker identity
timing envelope
performance shape
landing
```

These are internal reasoning questions, not new persisted Flow 6 fields.

### Communication Conservation

After rewriting, shortening, or performance-polishing a line:

- every independently actionable `Must communicate` fact that belongs in the moment remains clearly represented;
- `Must not add/repeat` guardrails remain respected;
- approved names, mechanics, result/state, sequence, and terminology preserve meaning;
- any authoritative Flow 5 `Timing Constraint` remains respected by the planned wording/timing approach;
- duration compression does not silently remove required communication;
- no new project fact is introduced.

Concision may merge equivalent phrasing. It may not thin material communication.

No persisted requirement-to-sentence matrix is created.

# Integrated Voice Script Readiness

After per-line authoring, review the current prepared scope **once** using these lenses:

| Lens | Ready when... |
|---|---|
| Communication | Required meaning is clear and conserved. |
| Listener | Each line fits the player's current state and information need. |
| Character | Recurring speakers remain coherent without becoming mechanically templated. |
| Performance | Emotional/beat/textual direction serves the scene. |
| Timing | Estimated density is plausible, authoritative timing constraints are honored, and required meaning was not sacrificed. |
| Continuity | Information progresses and accidental cross-line template repetition is absent. |
| Operator | Speaker ownership, duration, exact prompt, and special actions are unambiguous. |

Treat this as one semantic decision: **Voice Script Readiness: PASS | FAIL**. Do not create seven independent gates, scores, or artifacts.

`Communication Conservation` remains explicit because a script can read well while still omit a required fact.

## First wrong owner

Fix the earliest owner that is actually wrong:

```text
project/gameplay/story fact → upstream PRD authority
Voice moment/Speaker/Channel/Trigger/Purpose/required communication/timing truth → Flow 5
wording/performance/Estimated Duration → Flow 6 / SoundMaker
DOCX-only presentation defect → builder / DOCX-FORMAT.md
audio-only defect with correct script → Generation Mode evidence/settings/voice
```

Do not repair upstream defects by making prompts more elaborate.

## Bounded revision

Revise only invalidated scope.

A line-specific wording/timing-estimate change normally reopens that Voice ID plus adjacent/project continuity only when materially affected. A change to authoritative Voice timing truth reopens Flow 5 for that requirement first. A speaker-wide identity change may reopen all lines for that speaker. Do not replay unaffected Voice IDs for ceremony.

# Duration and pronunciation

Every entry requires an `Estimated Duration` range. It remains planning evidence until actual audio exists.

When Flow 5 includes an authoritative `Timing Constraint`:

```text
Flow 5 Timing Constraint
→ fixed/hard source boundary
→ Flow 6 word-budget/performance planning
→ Estimated Duration compatible with that boundary
```

When Flow 5 has no `Timing Constraint`, do not invent a hard source limit. Use `references/elevenlabs/v3-duration-planning.md` only when timing is material.

Preparation Mode identifies material pronunciation risk but does not pretend it is verified. Use the smallest appropriate spoken-form / inline IPA / project-note-or-dictionary approach described by SoundMaker.

# Generation / approval sync

When Generation Mode is requested:

1. use one active Voice ID;
2. present one exact reviewed prompt using the operator contract;
3. if the user/UI changes the prompt before generation, treat that exact generated version as the new revision;
4. after approval, synchronize it into `work/voice-production.md`;
5. rebuild/revalidate only affected derived scope.

Do not claim current script/audio alignment while canonical wording differs from the approved generated prompt.

## Section ordering

Keep gameplay sections in accepted project order. Within a section, order entries by approved Trigger sequence.

# Mechanical gate

Before building DOCX:

- every Flow 5 Voice ID appears exactly once;
- no extra Voice ID exists;
- `Type` matches Flow 5;
- `Speaker` matches Flow 5;
- title, Estimated Duration, and performance block are present;
- no unresolved placeholder remains;
- no required fact is knowingly omitted;
- no new upstream fact is introduced.

Build:

```bash
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  workspace/active/<project>/output/Voice\ Production.docx \
  --requirements workspace/active/<project>/work/voice-requirements.md
```

## Voice state after Flow 6

Keep the existing state schema:

```yaml
flow: 6
status: voice_script_ready
source_prd_revision: <accepted PRD revision>
requirements: work/voice-requirements.md
script: work/voice-production.md
docx: output/Voice Production.docx
unresolved_upstream: 0
next_step: flow_7_voice_validation_delivery
```

Allowed statuses remain:

- `script_drafting`
- `needs_upstream_decision`
- `voice_script_ready`
- `blocked`

`no_voice_required` from Flow 5 bypasses Flow 6.

# Stop gate

Preparation Mode stops when:

- every required Voice ID is script-ready;
- Communication Conservation passes for current prepared/changed scope;
- integrated Voice Script Readiness passes;
- mechanical parity passes;
- requested derived artifacts are current;
- material pronunciation risks are represented honestly;
- no generated-audio or measured-duration claim is made without evidence.

Stop after readiness. Do not add optional tags, schemas, artifacts, review layers, or speculative hardening without a concrete defect.
