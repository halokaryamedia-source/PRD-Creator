# Voice Validation & Delivery Procedure

Flow 7 validates the exact current Flow 6 revision and decides whether the requested delivery scope is ready.

## Entry

Start from `state/voice-state.yaml: voice_script_ready` for the current Voice Requirements revision.

Read only:

1. `work/voice-requirements.md`;
2. `work/voice-production.md`;
3. `SOUNDMAKER.md` when v3 performance/audio quality is in scope;
4. `DOCX-FORMAT.md` when DOCX presentation is in scope;
5. accepted PRD only when a project fact/term needs verification.

## 1. Mechanical validation

Run:

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

Mechanical PASS proves parity/integrity only. It does not approve wording, pronunciation, v3 performance, layout, or audio.

## 2. Requirement coverage

For every Voice ID, verify that canonical wording:

- satisfies Flow 5 Purpose;
- communicates all material required facts;
- respects `Must not add/repeat` guardrails;
- preserves approved Type, speaker, channel, trigger, terminology, sequence, mechanics, outcomes, and rewards;
- introduces no unsupported project fact.

Paraphrase is allowed. Changed meaning is not.

## 3. Terminology / pronunciation

Audit only material pronunciation risk.

Use when needed:

- `confirmed` — approved pronunciation evidence exists;
- `accepted_as_written` — creative owner intentionally accepts the written form;
- `needs_confirmation` — do not claim pronunciation-ready.

Preparation-only delivery may retain honest unresolved pronunciation evidence when the downstream producer is expected to confirm it later; do not relabel it as verified.

## 4. Project performance continuity

Review the whole project for:

- coherent narrator/character identity;
- scene-driven energy/emotional movement;
- no repeated template that makes nearby lines feel mechanically identical;
- information progression: briefing introduces, reminders compress, success lines acknowledge rather than re-brief;
- concise compatible directing;
- plausible duration estimates;
- no unsupported v3 notation such as SSML `<break>`.

Detailed one-line construction belongs to `SOUNDMAKER.md`; do not duplicate its prompting checklist here.

## 5. DOCX visual QA

When DOCX is in scope, render and inspect every page for clipping, hierarchy, panel legibility, line breaks, glyphs, spacing, and other visible defects.

Fix the canonical/builder owner and rebuild; never patch the DOCX as the source fix.

## 6. Audio evidence

If audio is not supplied:

```text
Audio Evidence: not_provided
```

This blocks audio-quality claims, not script/DOCX delivery or Preparation Mode completion.

When audio is in scope:

1. identify the exact generated prompt;
2. synchronize any user/UI-edited generated wording into `work/voice-production.md`;
3. identify the actual voice/surface/Stability when relevant;
4. review the heard take using the **After generation** quality/diagnosis section in `SOUNDMAKER.md`;
5. record only what was actually reviewed.

Use audio evidence states:

- `partial_review`;
- `reviewed_passed`;
- `reviewed_with_findings`.

Do not infer immersion from tag count or prompt appearance.

## 7. Acceptance file

Create/update `work/voice-acceptance.md` using the compact structure owned by `docs/foundation/07-voice-validation-delivery.md`.

Critical or Major findings block delivery.

## 8. State transition

For script + DOCX only:

```yaml
flow: 7
status: voice_delivery_ready
requirements: work/voice-requirements.md
script: work/voice-production.md
docx: output/Voice Production.docx
acceptance: work/voice-acceptance.md
mechanical: passed
coverage: passed
terminology_pronunciation: passed
speaker_channel_trigger: passed
performance_continuity: passed
docx_visual: passed
audio_evidence: not_provided
delivery_scope: script_docx
next_step: complete_or_soundmaker_v3_generation
```

If audio is included, readiness additionally requires canonical prompt ↔ exact generated prompt alignment and actual heard-audio review.

## Final boundary

`voice_delivery_ready` means only the **current requested delivery scope** is ready. It does not imply generated-audio approval, client sign-off, implementation completion, or release.
