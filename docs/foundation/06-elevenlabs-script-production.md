# ElevenLabs Performance Script Production

Status: active Flow 6 policy

## Purpose

Convert `voice_requirements_ready` into canonical spoken/performance wording and a reference-styled `Voice Production.docx` without changing upstream voice scope or project meaning.

Flow 6 owns:

- final spoken wording for approved Voice IDs;
- concise performance directions;
- selective spoken emphasis;
- purposeful pause/line-break structure;
- Estimated Duration ranges;
- deterministic DOCX presentation based on the approved Voice Production reference.

Flow 6 does **not** own:

- adding/removing voice moments without reopening Flow 5;
- changing speaker/channel/trigger/project facts;
- audio generation quality;
- final continuity/pronunciation/delivery approval.

## Canonical sequence

```text
state/voice-state.yaml = voice_requirements_ready
↓
work/voice-requirements.md
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

`output/Voice Production.docx` is a derived presentation artifact and may not be patched as the content owner.

## Scope parity

Every Flow 5 Voice ID must appear exactly once in Flow 6 unless Flow 5 scope is explicitly reopened. Flow 6 may refine wording, but it may not:

- create a new Voice ID;
- drop a required Voice ID;
- change Main Story ↔ Radio/other type;
- move a trigger by implication;
- invent a speaker/channel;
- add unsupported lore/mechanics/rewards.

The builder enforces ID/type parity mechanically when given the Flow 5 requirements file.

## Performance notation

Square-bracket directions, selective CAPS, ellipses, and line breaks are allowed only when they improve spoken delivery.

Directions describe performance, not project events. Do not use them as a hidden way to introduce new facts.

Estimated Duration is always an estimate until audio exists.

## DOCX presentation

The audited original Aftershock Voice Production DOCX is the primary demonstrated layout/performance benchmark. Its SHA-256 and derived contract are recorded in `kits/voice-production-kit/references/aftershock/README.md` and `DOCX-FORMAT.md`; the active builder does not require a copied binary. Reuse the demonstrated hierarchy and visual treatment, not its project-specific content or counts.

The active builder:

- creates Letter pages with compact margins;
- uses reference-like title/section/type hierarchy;
- styles bracketed directions separately from spoken text;
- uses pale blue Main Story panels and neutral Radio/other panels;
- preserves canonical line breaks;
- starts each gameplay section on a new page.

## Flow 6 gate

Set `voice_script_ready` only when:

- Flow 5 status was `voice_requirements_ready` for the same accepted PRD revision;
- all required Voice IDs are present exactly once;
- types match Flow 5;
- every entry has title, Estimated Duration, and Performance Script;
- no visible unresolved placeholder remains;
- no known upstream fact is missing or contradicted;
- DOCX successfully builds from canonical Markdown;
- current project DOCX receives visual QA when an actual production deliverable is being produced.

Flow 6 stop does not equal final delivery approval. Flow 7 remains required for final voice acceptance.
