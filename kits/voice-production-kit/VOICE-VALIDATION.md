# Voice Validation & Delivery Procedure

Flow 7 validates the current Flow 6 script/DOCX revision and decides whether it is ready to hand to the Voice/ElevenLabs production workflow.

## Entry

Start from `state/voice-state.yaml: voice_script_ready` for the current Voice Requirements revision.

Read in this order:

1. `VOICE-VALIDATION.md`;
2. `work/voice-requirements.md`;
3. `work/voice-production.md`;
4. `DOCX-FORMAT.md`;
5. accepted PRD only when a project fact/term needs verification.

## Step 1 — Mechanical validator

Run:

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

A pass proves parity/integrity only. It does not approve wording, pronunciation, pacing, layout, or audio.

## Step 2 — Requirement-by-requirement review

For each Voice ID, compare the canonical performance text to its Flow 5 requirement.

PASS only when:

- Purpose is satisfied;
- all material `Must communicate` facts are present in spoken form;
- `Must not add/repeat` guardrails are respected;
- Type is correct;
- approved speaker/channel/trigger remain compatible with the wording;
- no project fact was invented during script polish.

Do not demand literal sentence matching. Meaning and production function are the test.

## Step 3 — Terminology / pronunciation

Audit official project terms across the full script.

Create pronunciation notes only for material risk. For high-risk names/terms, record one of:

- `confirmed` — explicit approved pronunciation evidence exists;
- `accepted_as_written` — creative owner intentionally accepts the written form for production;
- `needs_confirmation` — do not call delivery ready yet.

Do not claim a spelling guarantees ElevenLabs pronunciation.

## Step 4 — speaker/channel/trigger continuity

Check that dialogue perspective and wording remain plausible for the approved speaker/channel/trigger.

Examples of blockers:

- a direct NPC line written as if received remotely when no channel exists;
- one character suddenly refers to themselves as a different identity;
- a warning states an event has happened before its approved trigger;
- multi-speaker production cannot determine who should perform a line from the final package.

Route the fix to the correct upstream owner instead of inventing metadata in the audit.

## Step 5 — performance continuity

Review the whole project, not each line in isolation.

Check:

- consistent narrator/character identity;
- scene-appropriate energy progression;
- direction vocabulary is concise and compatible;
- no contradictory directions inside one entry;
- CAPS is selective;
- ellipses/line breaks are purposeful;
- Main Story and Radio remain differentiated by gameplay function;
- duration labels remain estimates rather than audio claims.

## Step 6 — DOCX visual QA

Render `output/Voice Production.docx` using the standard DOCX render workflow and inspect **every page**.

Record page count and result in `work/voice-acceptance.md`.

If layout fails, fix the canonical/builder owner and rebuild. Never patch the DOCX manually as the authoritative fix.

## Step 7 — audio evidence (optional unless required by task)

If no audio is supplied:

```text
Audio Evidence: not_provided
```

This does not block script/DOCX delivery. It only blocks claims about generated-audio quality.

If audio is part of the requested delivery scope, review the actual files and record what was actually heard. Do not convert script confidence into an audio-quality claim.

## Acceptance file

Create `work/voice-acceptance.md` using the compact format defined by `docs/foundation/07-voice-validation-delivery.md`.

Use Critical/Major/Minor/Suggestion severities. Critical or Major always blocks delivery.

## State transition

When the gate passes:

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
next_step: system_integration_proof
```

If findings remain, use `needs_revision` and name the owning upstream file/flow. Do not use the audit file as a place to rewrite the canonical script.

## Final boundary

`voice_delivery_ready` means the accepted **script + DOCX scope** is ready for the downstream production user.

It does not mean:

- generated ElevenLabs audio has been heard unless audio evidence says so;
- voice/model/settings are universally correct;
- client sign-off occurred;
- implementation/QA/release work is complete.
