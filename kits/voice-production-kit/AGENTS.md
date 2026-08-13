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
└─ requirements.txt
```

## Routing

- Flow 5 → `VOICE-EXTRACTION.md`.
- Flow 6 lifecycle/static output → `SCRIPT-PRODUCTION.md` + `SOUNDMAKER.md`.
- Flow 7 → `VOICE-VALIDATION.md`.
- optional DOCX export → `DOCX-FORMAT.md` + builder.
- deep Eleven v3 evidence → only the matching reference file when needed.

Do not broad-read every Voice/reference file by default. Recover current project facts before asking the user.

## Canonical boundary

```text
accepted PRD
→ work/voice-requirements.md
→ work/voice-production.md
→ output/final.html → Production Assets → Voice
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

- PRD owns project/gameplay truth and the fact that a Voice asset is required.
- Flow 5 owns Voice scope, Speaker/Channel/Trigger/Purpose, required communication, exclusions, and source timing truth when present.
- `work/voice-production.md` owns canonical wording and Estimated Duration.
- `output/final.html` is the default derived operator presentation; it is not wording authority.
- DOCX is optional export only.

## Static output contract

Production Assets extends the existing accepted PRD navigation. It must not rebuild Development or renumber PRD package/page identity.

```text
03 Development
   global development pages
   gameplay/objective sections

04 Production Assets
   VOICE
   <gameplay section title>
   <accepted PRD package label>
```

`VOICE` appears once. Each linked section uses the gameplay/section title plus the accepted PRD label, and long text wraps naturally instead of being truncated.

Each Voice section page shows gameplay title, accepted PRD package label/context, Voice line count, Primary Speaker, and compact Voice Setup.

Each Voice line shows:

```text
title
→ <PRD package label> · Voice Line X/Y
→ Context = exact Flow 5 Trigger
→ Speaker + Estimated Duration
→ exact canonical prompt
→ Copy Prompt
```

The visible developer `Context` is a direct presentation of the existing Flow 5 Trigger. Do not duplicate it into the canonical Flow 6 entry. Purpose, `Must communicate`, `Must not add/repeat`, source refs, WPM math, reasoning, and QA notes remain internal.

`Copy Prompt` copies only the exact canonical performance payload.

## Semantic vs technical ownership

Use the root `voice-production` specialist for semantic/product-contract defects such as:

- Voice ID/Type/Speaker/Channel/Trigger/Purpose scope;
- Flow 5→6 intent completeness;
- canonical wording/performance meaning;
- Voice artifact/delivery semantics.

When semantics are already correct, route mechanics directly:

- same-HTML Production Assets composition/navigation → `kits/project-document-generator/renderer/production_assets.py`;
- optional DOCX generation/pagination → `builder/build_docx.py`;
- optional DOCX presentation contract → `DOCX-FORMAT.md`;
- Voice mechanical parity → `validator/validate.py`;
- shared dependency/test/CI → repository-engineering owners.

## Validator / builder rules

- exact Voice ID, Type, and Speaker parity are fail-closed;
- when consolidated `final.html` exists, validator checks section/page parity, developer Context, and exact canonical prompt parity;
- when optional DOCX exists, validator checks that export too;
- builder/validator PASS does not establish semantic or visual quality;
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

Direct Voice validator:

```text
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>
```

Use `Voice Verify` for changed Voice contracts and `PRD Verify` when the Production Assets compositor changes.

## Boundaries

- kit owns Flow 5–7 only;
- project definition/PRD belongs to Project Document Generator;
- Production Assets pages are downstream presentation, not a new PRD semantic owner;
- SFX generation remains separate until explicitly developed;
- DOCX remains optional compatibility/export, not the default operator surface;
- do not add a second Voice HTML, generic asset framework, or extra workflow layer without a concrete need.
