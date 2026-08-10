# Voice Validation & Delivery

Status: active Flow 7 policy

## Purpose

Flow 7 decides whether the current `voice_script_ready` revision is safe to deliver as a Voice Production script/DOCX. It validates the exact relationship between accepted Voice Requirements, canonical performance wording, and the derived DOCX.

Flow 7 does **not** assume that generated ElevenLabs audio exists or sounds correct. Audio is reviewed only when actual audio evidence is supplied and explicitly included in delivery scope.

## Canonical sequence

```text
voice_script_ready
↓
mechanical parity / DOCX integrity
↓
requirement coverage + factual fidelity
↓
terminology / pronunciation risk
↓
speaker / channel / trigger consistency
↓
performance continuity / pacing / notation
↓
DOCX render + visual QA
↓
optional actual-audio evidence review
↓
voice_delivery_ready | needs_revision | blocked
```

## Entry gate

Use the same current revision of:

- `work/voice-requirements.md`;
- `work/voice-production.md`;
- `output/Voice Production.docx`;
- `state/voice-state.yaml`.

If PRD meaning or Flow 5 voice scope changed after Flow 6, do not validate stale artifacts. Reopen the owning upstream flow first.

## Mechanical validation

Run:

```bash
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation checks:

- required files exist;
- unresolved placeholder tokens are absent;
- Flow 5 and Flow 6 Voice ID sets match exactly;
- voice Type matches for every Voice ID;
- script entries have Type, Estimated Duration, and Performance Script;
- DOCX opens successfully;
- section headings and Voice IDs expected from the script exist in the DOCX;
- each Voice ID appears once in the DOCX;
- duration/performance content is preserved into the DOCX;
- no extra Voice ID appears in the DOCX;
- the DOCX retains the active Letter-page contract.

Mechanical pass is necessary but cannot establish semantic or visual quality by itself.

## Semantic acceptance

### 1. Requirement coverage and factual fidelity

For every Voice ID, verify that the spoken text:

- fulfills its Flow 5 Purpose;
- communicates every required fact that belongs in the moment;
- respects every `Must not add/repeat` guardrail;
- preserves approved names, sequence, mechanic, result, reward, trigger, and state;
- does not introduce a new voice moment or upstream project fact.

Paraphrase is allowed. Changed meaning is not.

### 2. Terminology and pronunciation risk

Verify official terminology is consistent with the accepted PRD and Voice Requirements.

Do not create a large pronunciation catalog for ordinary words. Flag only material risk such as:

- invented/fantasy proper nouns;
- unusual abbreviations/acronyms;
- multilingual phrases;
- names with genuinely ambiguous pronunciation;
- terminology whose spoken form affects production consistency.

High-risk pronunciation that cannot be inferred reliably must be confirmed or intentionally accepted before delivery. Never claim pronunciation is verified without evidence.

### 3. Speaker, channel, and trigger consistency

Compare each line with Flow 5:

- speaker identity;
- direct/radio/communicator/PA/other channel;
- trigger timing;
- communication function.

The script does not need to repeat these metadata fields visibly when the production context is unambiguous. If a multi-speaker/channel project would make the final DOCX ambiguous to the production team, that is a blocking format/script-production finding owned by Flow 6.

### 4. Performance continuity, pacing, and notation

Across the complete project, verify:

- one speaker does not accidentally read like different characters without an approved reason;
- direction vocabulary is coherent and not contradictory;
- energy progression follows scene/trigger needs rather than random escalation;
- CAPS is selective;
- ellipses are purposeful;
- line breaks help phrasing/breath;
- Radio remains concise/actionable;
- Main Story carries only the context needed by its approved function;
- Estimated Duration is plausible as an estimate and not presented as measured audio.

Flow 7 may correct a Flow 6 wording/notation defect by reopening the canonical `work/voice-production.md`; it must not patch the DOCX directly.

## DOCX visual QA

Render the current project DOCX to page images and inspect every page.

Check:

- no clipping/overlap;
- no orphaned Type/title/duration labels separated from their script panel;
- section/page hierarchy is readable;
- script panels remain legible across page boundaries;
- canonical line breaks are preserved;
- no missing glyphs;
- spacing/shading remains consistent;
- the document is immediately usable for production.

A successful `python-docx` load is not visual proof.

## Audio evidence

Default product delivery scope is **script + DOCX for ElevenLabs use**. Audio is not required to set `voice_delivery_ready` unless the current task explicitly includes generated audio delivery.

Record one audio evidence state in the acceptance record:

- `not_provided` — no actual audio was supplied; no audio-quality claim is made;
- `partial_review` — only some generated audio was reviewed;
- `reviewed_passed` — the supplied audio for the accepted scope was actually reviewed and passed;
- `reviewed_with_findings` — actual audio was reviewed and has unresolved findings.

Do not infer generated-audio quality from script quality, tags, reference examples, or estimated duration.

## Severity

- **Critical** — wrong/missing Voice ID, wrong project fact, wrong speaker/channel/trigger, missing required communication, or artifact drift that would produce incorrect voice output.
- **Major** — material wording/continuity/pronunciation/layout problem that makes production unsafe or requires the producer to invent/guess a decision.
- **Minor** — delivery remains correct and usable, but clarity/notation/layout can improve without changing meaning.
- **Suggestion** — optional polish.

Critical and Major block `voice_delivery_ready`.

## Finding ownership

Fix the root owner:

- voice-moment scope/purpose/speaker/channel/trigger defect → Flow 5 `work/voice-requirements.md`;
- wording/performance/duration defect → Flow 6 `work/voice-production.md`;
- DOCX presentation defect → Flow 6 builder / `DOCX-FORMAT.md`, then rebuild;
- upstream project fact defect → PRD/requirement owner;
- actual-audio-only defect with correct script → audio generation/voice/model/settings evidence, not a silent script rewrite.

Never edit final DOCX or audio as the canonical source of project meaning.

## Acceptance record

Create/update `work/voice-acceptance.md`:

```text
# Voice Acceptance
Status: needs_revision | voice_delivery_ready
Reviewed revision: <revision/reference>
Delivery scope: script_docx | script_docx_audio

## Mechanical Validation
PASS / FAIL

## Requirement Coverage
PASS / FAIL + findings

## Terminology / Pronunciation
PASS / FAIL + material risks

## Speaker / Channel / Trigger
PASS / FAIL + findings

## Performance Continuity / Pacing / Notation
PASS / FAIL + findings

## DOCX Visual QA
PASS / FAIL + rendered page evidence

## Audio Evidence
not_provided | partial_review | reviewed_passed | reviewed_with_findings

## Findings
ID | Severity | Owner | Location | Finding | Resolution Status

## Gate
Critical: N
Major: N
Minor: N
Result: ...
```

Keep this concise; do not duplicate the full script.

## Voice state

After acceptance, update `state/voice-state.yaml`:

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

Allowed Flow 7 statuses:

- `voice_validation`
- `needs_revision`
- `voice_delivery_ready`
- `blocked`

`no_voice_required` remains a valid upstream terminal outcome and does not require an empty script/DOCX.

## Delivery gate

Set `voice_delivery_ready` only when:

- mechanical validation passes;
- requirement coverage/factual fidelity passes;
- terminology/pronunciation risks are resolved or explicitly accepted;
- speaker/channel/trigger consistency passes;
- performance continuity/pacing/notation passes;
- current DOCX visual QA passes;
- Critical = 0;
- Major = 0;
- no stale upstream revision is being delivered;
- audio evidence state is recorded truthfully.

If delivery scope explicitly includes generated audio, actual audio must be available and reviewed before that audio scope can be called ready.

## Revisions after delivery-ready

Any change to Voice Requirements, canonical script, or DOCX-builder behavior invalidates the previous acceptance for affected content:

```text
change
→ reopen owning flow
→ regenerate/rebuild affected artifacts
→ state = voice_validation
→ re-run affected checks
→ issue new acceptance state
```

Do not keep an old `voice_delivery_ready` state against a newer script/DOCX revision.
