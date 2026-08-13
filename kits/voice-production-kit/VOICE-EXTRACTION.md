# Voice Requirement Extraction

Flow 5 converts an accepted PRD revision into a traceable set of justified voice moments that are **ready for SoundMaker to write without inventing project meaning**. It does not write performance scripts.

## Entry gate

Start only when the current project has:

- `state/handoff-state.yaml` with `status: handoff_ready`;
- `accepted_prd_version` matching the current `work/render-data.json → document.version`;
- accepted `work/content.md` for that same PRD version;
- `work/acceptance.md` and `output/team-handoff.md` at the recorded handoff paths;
- no unresolved upstream decision affecting current Voice scope.

Before extraction, run:

```bash
python kits/project-document-generator/validator/validate_handoff.py \
  workspace/active/<project>/
```

If accepted PRD meaning changes later, mark affected Voice requirements stale and reopen only the invalidated Flow 5 scope before Flow 6 continues.

## Authority

Use this order:

1. accepted `work/content.md` — canonical project meaning;
2. `state/requirement-register.yaml` — approved requirement traceability;
3. `output/team-handoff.md` — navigation/scope aid;
4. `output/final.html` — presentation aid;
5. approved Voice Production reference — structure/quality evidence only.

Reference projects never supply new project facts, speakers, channels, triggers, or Voice moments.

## Extraction sequence

```text
current handoff guard PASS
↓
identify the approved player-facing communication system
↓
scan overview + gameplay flow + package-local gameplay
↓
inspect developer/global detail only when needed for player-facing state/trigger
↓
identify candidate Voice moments
↓
remove redundant / UI-only / unsupported moments
↓
classify Type + Function + Necessity
↓
normalize each moment into the Flow 5 → Flow 6 interface contract
↓
trace to accepted PRD evidence
↓
work/voice-requirements.md
↓
voice_requirements_ready
```

## Voice types

### Main Story

Use for player-facing narrative/mission communication whose primary job is to establish or advance the experience, for example briefing, arrival, transition, reveal, major completion, reward, or farewell.

Main Story is not a license to narrate every mechanic.

### Radio Communication

Use only when the accepted project defines a communicator, remote NPC voice, radio, intercom, or equivalent channel.

Typical functions are warning, progress, urgency, encouragement, reminder, or setback/recovery guidance. Radio should remain concise during active play and must not replay a complete Main Story briefing.

### Other Supported Voice

Use only when the accepted project explicitly defines another speaker/channel such as direct NPC dialogue, announcer, PA, or AI system. Do not use a generic `Other` bucket.

## Function and necessity

Use one primary Function when applicable:

```text
briefing | arrival | transition | reveal | warning | progress | urgency
encouragement | reminder | setback_recovery | completion | reward | farewell
```

Function describes the **communication job**, not an ElevenLabs Audio Tag.

Necessity:

- `required` — the experience depends on this communication or the player would miss a required fact/state;
- `supporting` — the approved Voice system materially improves clarity/pacing/feedback, while the required fact is also safely communicated elsewhere.

Do not create a Voice moment merely because a gameplay section exists.

## Candidate filter

Keep a candidate only when:

1. it is player-facing;
2. its Purpose is supported by accepted project meaning;
3. Speaker and Channel are known/approved;
4. Trigger is tied to a concrete gameplay/story state;
5. it adds useful information, acknowledgement, warning, or progression at that moment;
6. it does not duplicate another Voice moment without a distinct Trigger/Function reason.

Reject developer telemetry, hidden implementation state, decorative unsupported narration, duplicate UI reading, invented lore/mechanics/rewards/triggers, and forced symmetry across packages.

A package may legitimately have zero Voice moments.

## Duplicate guard

Related information may appear twice only when the communication job or Trigger materially differs.

```text
Main Story briefing → objective/stakes once
Radio warning       → live hazard warning
Radio reminder      → minimum actionable fact after a justified delay/setback
```

Do not convert the briefing into several paraphrased reminders.

# Flow 5 → Flow 6 interface contract

Flow 5 should give SoundMaker enough **authoritative communication intent** to fill Voice Intent Completeness without inventing product meaning. Do not solve performance craft in Flow 5.

## Field meaning

### Function

State the primary communication job. Avoid vague labels such as `information` when a concrete function like `warning`, `transition`, or `completion` is known.

### Speaker / Channel

Use exact approved identities. These are project facts, not production guesses.

### Trigger

Describe the actual event/state that causes the line and include the **listener/player state when it materially changes delivery**.

Prefer:

```text
Collapse begins while the player is crossing Checkpoint 3.
```

rather than:

```text
Objective 2 trigger.
```

Trigger is not a script or timing estimate; it is the production context needed to understand when the communication happens.

### Purpose

State what the communication must accomplish **for the listener**.

Prefer:

```text
Warn the player that collapse has started and make the immediate crossing action clear.
```

rather than:

```text
Provide warning dialogue.
```

Purpose should make the intended listener outcome recoverable: what they should know, do, understand, or acknowledge after hearing the line.

### Must communicate

Store material facts as separate concise bullets when they are independently actionable. Do not pre-write dialogue.

Good:

```text
- Collapse has started.
- The player must keep moving across the current route.
```

Avoid one dense prose bullet that hides several independent instructions.

### Must not add/repeat

Record the material exclusions that protect scope, continuity, and anti-repetition. This can include facts the line must not invent and information already delivered elsewhere that should not be re-briefed.

### Timing Constraint — optional, authoritative only

Use an optional field only when accepted project authority defines a material Voice/timeline constraint, for example:

```text
- Timing Constraint: Must complete before the 10-second collapse window ends.
```

or:

```text
- Timing Constraint: Fixed 12-second cinematic slot.
```

Rules:

- this is **not** `Estimated Duration`;
- do not invent a timing target in Flow 5;
- omit the field when no authoritative line/window/sync constraint exists;
- absence means Flow 6 may plan a reasonable Estimated Duration but must not treat a hard source limit as known.

### Source refs

Keep enough traceability to verify project meaning. Source refs are not operator-facing prompt content.

## What stays in Flow 6

Do **not** add Flow 5 fields for:

- final spoken wording;
- emotional/performance arc chosen by SoundMaker;
- landing wording;
- Audio Tags;
- CAPS/punctuation/pause strategy;
- Target Voice Profile or commercial ElevenLabs voice;
- Stability / Surface / Enhance settings;
- Estimated Duration when it is only a production estimate.

`Performance Shape` and `Landing` are normally production interpretation derived by SoundMaker from Function, Trigger, Purpose, required facts, Speaker context, and any authoritative Timing Constraint.

## Flow 6 readiness check

Before `voice_requirements_ready`, each included Voice moment must let a competent Flow 6 reader recover, without product-level guessing:

```text
communication job  ← Function + Purpose
listener state     ← Trigger + Channel + minimal accepted context
information load   ← Must communicate
listener outcome   ← Purpose
speaker owner      ← Speaker
hard timing truth  ← optional Timing Constraint when authoritative
scope exclusions   ← Must not add/repeat
```

If a material listener state, communication outcome, Speaker/Channel/Trigger, or authoritative timing rule is genuinely unresolved and different answers would change the asset materially, return upstream instead of hiding the decision in SoundMaker.

# Canonical output

Create `work/voice-requirements.md` as the Flow 5 source of truth.

```text
# Voice Requirements

Source PRD revision: <accepted document.version>
Voice system: <speaker/channel summary>

## <Gameplay Section>

### VO-<SECTION>-01 — <Functional title>
- Type: Main Story | Radio Communication | <explicit supported type>
- Function: briefing | warning | ...
- Necessity: required | supporting
- Speaker: <approved speaker>
- Channel: <approved channel>
- Trigger: <approved gameplay/story event + relevant listener state>
- Purpose: <listener-facing communication outcome>
- Timing Constraint: <authoritative limit/sync only; omit when none>
- Must communicate:
  - <one material fact/action per bullet where practical>
- Must not add/repeat:
  - <scope / continuity guardrail>
- Source refs:
  - <requirement ID and/or content.md section>
```

Do not include final performance wording, tags, emphasis, pause punctuation, production-estimated duration, ElevenLabs settings, or voice selection.

# Voice state

Maintain `state/voice-state.yaml`:

```yaml
flow: 5
status: voice_requirements_ready
source_handoff: state/handoff-state.yaml
source_revision: <accepted document.version>
canonical_prd: work/content.md
requirements: work/voice-requirements.md
unresolved_upstream: 0
next_step: flow_6_elevenlabs_script_production
```

Allowed statuses:

```text
pending_extraction | needs_upstream_decision | voice_requirements_ready
no_voice_required | blocked
```

`no_voice_required` remains valid when accepted upstream evidence justifies no Voice production.

## Upstream return rule

Use `needs_upstream_decision` when a material Voice requirement depends on unresolved project meaning such as Speaker, Channel, Trigger, story/result/reward, contradictory terminology/sequence, or an authoritative communication/timing constraint that cannot responsibly be recovered.

Do not solve those decisions through performance writing.

## Flow 5 completion

Flow 5 is complete when either:

- `voice_requirements_ready` — every included moment is justified, traceable, non-duplicative, and complete enough for SoundMaker to fill Voice Intent Completeness without inventing project meaning; or
- `no_voice_required` — accepted upstream evidence supports no Voice production for current scope.

Stop before writing any performance script.
