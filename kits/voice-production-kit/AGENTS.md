# Voice Production Kit Agent Rules

Root `AGENTS.md` remains authoritative for work mode, proof, repository continuity, and semantic-vs-technical ownership. This file narrows behavior only inside `kits/voice-production-kit/`.

## Module structure

```text
kits/voice-production-kit/
├─ AGENTS.md
├─ SKILL.md
├─ VOICE-EXTRACTION.md
├─ SCRIPT-PRODUCTION.md
├─ SOUNDMAKER.md
├─ DOCX-FORMAT.md
├─ VOICE-VALIDATION.md
├─ builder/
├─ validator/
├─ references/
│  ├─ aftershock/
│  └─ elevenlabs/
└─ requirements.txt
```

## Routing

- Flow 5 → `VOICE-EXTRACTION.md`.
- Flow 6 lifecycle/full-project preparation → `SCRIPT-PRODUCTION.md` + `SOUNDMAKER.md`.
- Actual Eleven v3 generation/revision → `SOUNDMAKER.md` Generation Mode.
- DOCX presentation/build mechanics → `DOCX-FORMAT.md` + builder.
- Flow 7 → `VOICE-VALIDATION.md`.
- Deep Eleven v3 evidence → only the matching file under `references/elevenlabs/`.

Do not broad-read every Voice/reference file by default. Recover current project facts before asking the user.

## Canonical boundary

```text
accepted PRD
→ work/voice-requirements.md
→ SoundMaker v3 preparation/generation quality
→ work/voice-production.md
→ output/Voice Production.docx
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

- Flow 5 owns Voice scope.
- SoundMaker is an execution procedure, not a wording authority.
- `work/voice-production.md` owns final wording.
- DOCX is derived presentation.
- audio is optional evidence/output only when actually in scope.

If the exact generated/approved prompt differs from canonical wording, synchronize it into `work/voice-production.md` before claiming current alignment.

## SoundMaker modes

SoundMaker is **Eleven v3 only** and stays inside Flow 6.

### Preparation Mode

- may process the full current Voice scope in one bounded pass;
- apply per-line construction plus project-level speaker continuity/anti-repetition;
- do not require audio generation/testing;
- do not require `APPROVED` per line;
- keep duration/pronunciation as planned evidence until real proof exists.

### Generation Mode

- use only when actual ElevenLabs work is requested;
- one active Voice ID;
- one exact reviewed prompt;
- feedback/approval loop + canonical sync.

Do not duplicate detailed prompting rules here. Durable guardrails are:

- duration before wording when timing matters;
- voice fit before compensating with more direction;
- spoken beats before punctuation/CAPS/tags;
- Enhance OFF by default on already-directed prompts;
- Speech Synthesis normally; Studio v3 only when long-form instability makes that surface useful;
- no audio-quality claim without heard evidence.

## Semantic vs technical ownership

Use the root `voice-production` specialist for semantic/product-contract defects such as:

- Voice ID/Type/speaker/channel/trigger scope;
- final wording/performance meaning;
- SoundMaker quality behavior;
- artifact/delivery semantics.

When semantics are already correct, route pure mechanics directly:

- Markdown/DOCX generation/pagination → `builder/build_docx.py`;
- presentation contract → `DOCX-FORMAT.md`;
- mechanical parity → `validator/validate.py`;
- shared dependency/test/CI → root repository-engineering owners.

## Builder / validator rules

- regenerate DOCX from canonical Markdown; never hand-edit it as the source fix;
- parser/build failures must fail clearly;
- exact Voice ID and Type parity is fail-closed;
- builder/validator PASS does not establish semantic, visual, pronunciation, or audio quality;
- the known blank-page regression remains guarded by `page_break_before`, not inserted page-break paragraphs.

## Dependency contract

Kit runtime requirement:

```text
python-docx==1.2.0
```

Repository verification uses exact pins from root `requirements.lock.txt`.

## Verification

Run from repository root as applicable:

```text
python -m pip install --disable-pip-version-check --no-deps -r requirements.lock.txt
python -m pip check
python -m unittest tests.test_voice_contracts -v
python -m compileall -q kits/voice-production-kit tests/test_voice_contracts.py
```

Direct builder:

```text
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  "workspace/active/<project>/output/Voice Production.docx" \
  --requirements workspace/active/<project>/work/voice-requirements.md
```

Direct validator:

```text
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>
```

Use `Voice Verify` as the repeatable repository-side gate for changed Voice contracts.

## Boundaries

- kit owns Flow 5–7 only;
- SoundMaker is not Flow 8;
- project definition/PRD belongs to Project Document Generator;
- SFX generation remains a separate lane;
- actual audio never becomes upstream project authority.
