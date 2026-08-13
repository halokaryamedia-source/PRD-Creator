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
- Flow 6 lifecycle/static output/full-project preparation → `SCRIPT-PRODUCTION.md` + `SOUNDMAKER.md`.
- actual Eleven v3 generation/revision → `SOUNDMAKER.md` Generation Mode.
- Flow 7 → `VOICE-VALIDATION.md`.
- optional DOCX export → `DOCX-FORMAT.md` + builder.
- deep Eleven v3 evidence → only the matching file under `references/elevenlabs/`.

Do not broad-read every Voice/reference file by default. Recover current project facts before asking the user.

## Canonical boundary

```text
accepted PRD
→ work/voice-requirements.md
→ SoundMaker preparation/generation quality
→ work/voice-production.md
→ output/final.html → Production Assets → Voice
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

- PRD owns project/gameplay truth and the fact that a Voice asset is required.
- Flow 5 owns Voice scope, Speaker/Channel/Trigger/Purpose, required communication, exclusions, and source timing truth when present.
- `work/voice-production.md` owns final wording, Estimated Duration, and selected actor voice in one optional `Voice Cast:` header.
- `output/final.html` is the default derived operator presentation; it is not wording authority.
- DOCX is optional export only.
- audio is optional evidence/output only when actually in scope.

If exact generated/approved prompt or actor selection differs from canonical production, synchronize it into `work/voice-production.md` and rerender the same project HTML before claiming alignment.

## SoundMaker modes

SoundMaker is **Eleven v3 only** and stays inside Flow 6.

### Preparation Mode

- may process the full current Voice scope in one bounded pass;
- actual commercial voice selection may wait if a clear Target Voice Profile exists;
- apply per-line construction plus integrated project-level continuity/anti-template review;
- do not require audio generation/testing;
- do not require `APPROVED` per line;
- keep measured duration/pronunciation/audio evidence unclaimed until proof exists.

### Generation Mode

- use only when actual ElevenLabs work is requested;
- one active Voice ID;
- exact project Speaker known;
- actual actor voice/settings selected;
- one exact reviewed prompt;
- feedback/approval loop + canonical sync + rerender when canonical production changed.

## Static output contract

Canonical production may contain:

```text
Voice Cast:
- <Speaker>: <selected ElevenLabs voice>
```

once before gameplay sections.

Each Voice entry remains:

```text
Voice ID + Title
Type
Speaker
Estimated Duration
exact performance block
```

The project HTML shows only Voice Cast once, gameplay-ordered title/Actor/Estimated Duration, exact prompt, and Copy Text.

Internal Channel, Trigger, Purpose, requirement bullets, source refs, WPM math, Performance Fill Map, voice-fit ratings, and QA notes stay in their owners and do not leak into the visible production page.

Do not create a separate Voice HTML or Asset Requirement HTML by default.

## Semantic vs technical ownership

Use the root `voice-production` specialist for semantic/product-contract defects such as:

- Voice ID/Type/Speaker/Channel/Trigger/Purpose scope;
- Flow 5→6 intent completeness;
- final wording/performance/actor selection meaning;
- SoundMaker quality behavior;
- Voice artifact/delivery semantics.

When semantics are already correct, route mechanics directly:

- same-HTML Production Assets composition → `kits/project-document-generator/renderer/production_assets.py`;
- optional DOCX generation/pagination → `builder/build_docx.py`;
- optional DOCX presentation contract → `DOCX-FORMAT.md`;
- Voice mechanical parity → `validator/validate.py`;
- shared dependency/test/CI → repository-engineering owners.

## Validator / builder rules

- exact Voice ID, Type, and Speaker parity are fail-closed;
- when consolidated `final.html` exists, validator checks exact canonical prompt parity in Voice Production panels;
- when optional DOCX exists, validator checks that export too;
- builder/validator PASS does not establish semantic, visual, pronunciation, or audio quality;
- never hand-edit `final.html` or DOCX as the source fix.

## Verification

Run from repository root as applicable:

```text
python -m pip install --disable-pip-version-check --no-deps -r requirements.lock.txt
python -m pip check
python -m unittest tests.test_voice_contracts -v
python -m compileall -q kits/voice-production-kit tests/test_voice_contracts.py
```

Consolidated project HTML is generated with the normal PRD command:

```text
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

Optional DOCX:

```text
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  "workspace/active/<project>/output/Voice Production.docx" \
  --requirements workspace/active/<project>/work/voice-requirements.md
```

Direct Voice validator:

```text
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>
```

Use `Voice Verify` for changed Voice contracts and `PRD Verify` when the Production Assets compositor changes.

## Boundaries

- kit owns Flow 5–7 only;
- SoundMaker is not Flow 8;
- project definition/PRD belongs to Project Document Generator;
- Production Assets pages are downstream presentation, not a new PRD semantic owner;
- SFX generation remains a separate lane until explicitly developed;
- actual audio never becomes upstream project authority;
- DOCX remains optional compatibility/export, not the default operator surface.
