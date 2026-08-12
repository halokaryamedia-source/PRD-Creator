# Eleven v3 Performance Script Production

Status: active Flow 6 policy

## Purpose

Convert `voice_requirements_ready` into canonical spoken/performance wording for **Eleven v3** and a reference-styled `Voice Production.docx` without changing upstream Voice scope or project meaning.

Flow 6 owns:

- final spoken wording for approved Voice IDs;
- SoundMaker v3 performance quality;
- emotional/performance beat construction;
- concise audible performance directions;
- purposeful punctuation, selective CAPS, pause/line structure;
- Estimated Duration ranges;
- deterministic DOCX presentation based on the approved Voice Production reference.

Flow 6 does **not** own:

- adding/removing Voice moments without reopening Flow 5;
- changing speaker/channel/trigger/project facts;
- Sound Effects generation;
- claiming generated-audio quality without actual audio evidence;
- final revision acceptance, which remains Flow 7.

## Canonical sequence

```text
state/voice-state.yaml = voice_requirements_ready
↓
work/voice-requirements.md
↓
SoundMaker v3 quality pass per Voice ID
↓
write canonical work/voice-production.md
↓
Voice ID / Type parity + placeholder checks
↓
build reference-styled output/Voice Production.docx
↓
state/voice-state.yaml = voice_script_ready
↓
Flow 7
```

## Authority

`work/voice-production.md` is the Flow 6 source of truth for final spoken wording and performance notation.

`SOUNDMAKER.md` is the one-entry-at-a-time v3 quality/execution procedure inside Flow 6. It is not a second source of truth.

`output/Voice Production.docx` is derived presentation and may not be patched as the content owner.

## Scope parity

Every Flow 5 Voice ID must appear exactly once in Flow 6 unless Flow 5 scope is explicitly reopened. Flow 6 may refine wording, but it may not:

- create/drop Voice IDs;
- change Voice Type;
- move a trigger by implication;
- invent speaker/channel;
- add unsupported lore/mechanics/rewards.

The builder enforces ID/type parity mechanically when given Flow 5 requirements.

## SoundMaker v3 quality contract

For each entry, construct performance in this order:

```text
requirement meaning
→ target duration first when specified
→ voice fit
→ performance arc
→ spoken wording
→ beat architecture
→ punctuation / line structure
→ selective CAPS
→ minimal Audio Tags
→ pronunciation safety
```

Rules:

- Eleven v3 is the model scope; do not auto-fallback to another model family;
- emotional changes need a scene/communication reason;
- script must remain understandable without Audio Tags;
- a flat script is not repaired by tag stacking;
- reactions are treated as timeline events;
- Eleven v3 does not use SSML `<break>` tags;
- when timing matters, plan word budget before final wording rather than compressing afterward.

Detailed execution procedure: `kits/voice-production-kit/SOUNDMAKER.md`.

Evidence-backed technique: `kits/voice-production-kit/references/elevenlabs/README.md`.

## Actual generation and canonical sync

Audio generation is optional unless requested.

When actual ElevenLabs generation occurs:

- work one Voice ID at a time;
- show one best paste-ready prompt by default;
- if the user edits the prompt before generation, the exact prompt actually used supersedes the assistant draft;
- after approval, synchronize the exact generated prompt back into `work/voice-production.md`;
- if canonical wording changed after DOCX/acceptance was produced, rebuild/reopen only the affected derived scope.

Do not claim current script/audio alignment while canonical wording differs from the approved generated prompt.

## Performance notation

Square-bracket directions, punctuation, selective CAPS, ellipses/em dashes, and line breaks are allowed only when they improve spoken delivery.

Directions describe audible performance, not project events. Do not use them as a hidden way to introduce facts.

Estimated Duration is always an estimate until actual audio exists.

## DOCX presentation

The audited original Aftershock Voice Production DOCX remains the demonstrated layout benchmark. Its SHA-256 and derived contract are recorded in `kits/voice-production-kit/references/aftershock/README.md` and `DOCX-FORMAT.md`.

Reuse hierarchy and visual treatment, not project-specific content/counts.

## Flow 6 gate

Set `voice_script_ready` only when:

- Flow 5 status was `voice_requirements_ready` for the same accepted PRD revision;
- all required Voice IDs are present exactly once;
- Types match Flow 5;
- every entry has title, Estimated Duration, and Performance Script;
- SoundMaker v3 pre-generation quality was applied;
- no unresolved placeholder remains;
- no known upstream fact is missing/contradicted;
- DOCX successfully builds from canonical Markdown when DOCX is in scope;
- current project DOCX receives visual QA during actual production.

Flow 6 stop does not equal generated-audio approval. Flow 7 remains required for current-revision acceptance.
