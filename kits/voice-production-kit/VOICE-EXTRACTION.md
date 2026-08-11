# Voice Requirement Extraction

Flow 5 converts an accepted PRD revision into a traceable set of justified voice moments. It does **not** write performance scripts.

## Entry gate

Start only when the current project has:

- `state/handoff-state.yaml` with `status: handoff_ready`;
- `accepted_prd_version` matching the current `work/render-data.json → document.version`;
- accepted `work/content.md` for that same PRD version;
- `work/acceptance.md` and `output/team-handoff.md` present at the paths recorded by the handoff state;
- no unresolved upstream decision affecting the voice scope.

Before extraction, run:

```bash
python kits/project-document-generator/validator/validate_handoff.py \
  workspace/active/<project>/
```

Do not start Flow 5 when this guard fails. It is a lightweight lifecycle check using the existing PRD `document.version`; it does not add a new hash/checksum chain and does not replace semantic PRD acceptance.

If accepted PRD meaning changes after extraction, the PRD revision must advance upstream and the existing voice requirements become stale. Reset Flow 5 to `pending_extraction` and re-check affected moments before Flow 6.

## Authority

Use this order:

1. accepted `work/content.md` — canonical project meaning;
2. `state/requirement-register.yaml` — traceability and approved requirement state;
3. `output/team-handoff.md` — navigation/scope aid only;
4. `output/final.html` — presentation aid only;
5. approved Voice Production reference — structure/quality evidence only.

Do not extract a new project fact from the Aftershock sample.

## Extraction sequence

```text
current handoff guard PASS
↓
handoff_ready PRD
↓
identify player-facing story / communication system
↓
scan overview + gameplay flow + package-local gameplay
↓
inspect developer/global pages only for player-facing triggers/state when needed
↓
identify candidate voice moments
↓
remove redundant / UI-only / unsupported moments
↓
classify type + function + necessity
↓
trace each moment to accepted PRD evidence
↓
work/voice-requirements.md
↓
state/voice-state.yaml
```

## Voice types

### Main Story

Use for player-facing narrative or mission communication whose primary job is to establish or advance the experience, for example:

- mission/context briefing;
- arrival or section introduction;
- major transition;
- important reveal or story-state change;
- major objective completion when narrative acknowledgement matters;
- ending, reward, or farewell.

Main Story is not a license to narrate every mechanic.

### Radio Communication

Use only when the accepted project defines a communicator, remote NPC voice, radio, intercom, or equivalent channel.

Radio should be brief and useful while the player is actively playing. Typical functions:

- warning;
- progress update;
- urgency;
- encouragement;
- concise reminder;
- setback/recovery guidance.

Radio must not repeat a full Main Story briefing or restate the complete objective.

### Other Supported Voice

Use only when the PRD explicitly defines a different speaker/channel such as an announcer, PA system, AI system, or direct NPC dialogue that does not fit the two standard types.

Do not use a generic `Other` bucket. Record the explicit source-defined type/speaker/channel. If that information is missing but required, return upstream instead of inventing it.

## Functional classification

A voice moment may use one primary function:

- `briefing`
- `arrival`
- `transition`
- `reveal`
- `warning`
- `progress`
- `urgency`
- `encouragement`
- `reminder`
- `setback_recovery`
- `completion`
- `reward`
- `farewell`

The function describes what the communication must achieve. It is not an ElevenLabs performance tag.

## Necessity

Use:

- `required` — the accepted experience explicitly depends on this voice communication or the player would otherwise miss a required narrative/feedback fact;
- `supporting` — the voice system is approved and the moment materially improves clarity/pacing/feedback, but the same required fact is also safely communicated another way.

Do not create voice solely because a section exists.

## Candidate filter

Keep a candidate only when all are true:

1. it is player-facing;
2. its purpose is supported by the accepted PRD;
3. the speaker/channel is known or explicitly defined by the project;
4. the trigger/timing can be tied to an approved gameplay/story state;
5. it adds information, acknowledgement, warning, or emotional progression that is useful at that moment;
6. it does not duplicate another voice moment without a distinct gameplay reason.

Reject candidates that are only:

- developer telemetry/save/reset internals;
- hidden implementation state;
- decorative narration with no project support;
- a duplicate reading of UI/objective text;
- an invented lore/mechanic/reward/trigger;
- a forced voice entry added to make every package look symmetrical.

A package may legitimately have zero voice moments.

## Duplicate guard

Two moments may communicate related facts only when their functions or triggers are materially different.

Example:

```text
Main Story briefing → explains the objective and stakes once
Radio warning       → warns about a live hazard during play
Radio reminder      → repeats only the minimum actionable fact after a meaningful delay/setback
```

Do not copy the briefing into radio form.

## Canonical output

Create `work/voice-requirements.md` as the Flow 5 source of truth.

Use one section per gameplay package/scene and one entry per justified moment:

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
- Channel: <direct / communicator / radio / PA / ...>
- Trigger: <approved gameplay/story trigger>
- Purpose: <what this communication must achieve>
- Must communicate:
  - <required fact>
- Must not add/repeat:
  - <guardrail>
- Source refs:
  - <requirement ID and/or content.md section>
```

Do **not** include:

- final spoken wording;
- square-bracket performance directions;
- CAPS emphasis decisions;
- pause punctuation strategy;
- estimated duration;
- ElevenLabs settings;
- voice model selection.

Those belong to Flow 6.

## Voice state

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

- `pending_extraction`
- `needs_upstream_decision`
- `voice_requirements_ready`
- `no_voice_required`
- `blocked`

`no_voice_required` is valid when the accepted PRD does not define or justify a voice system/moment. Do not invent a narrator merely to continue the pipeline.

## Upstream return rule

Set `needs_upstream_decision` when a required voice moment depends on an unresolved project choice such as:

- who is speaking;
- whether a communicator/radio exists;
- when a story event actually triggers;
- what reward/outcome is canonical;
- contradictory terminology or sequence.

Record the affected source/requirement and return the decision to the correct upstream owner. Do not solve it in Flow 5.

## Flow 5 completion

Flow 5 is complete when either:

- `voice_requirements_ready` — every included voice moment is justified, traceable, non-duplicative, and ready for script production; or
- `no_voice_required` — accepted upstream evidence supports no voice production for the current scope.

Stop before writing any performance script.
