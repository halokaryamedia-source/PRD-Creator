# Voice Production Kit Agent Rules

Root `AGENTS.md` remains authoritative for work mode, proof, repository continuity, and semantic-vs-technical ownership. This file narrows behavior only inside `kits/voice-production-kit/`.

## Active module structure

```text
kits/voice-production-kit/
├─ AGENTS.md
├─ README.md
├─ SKILL.md
├─ VOICE-EXTRACTION.md
├─ SOUNDMAKER.md
├─ DOCX-FORMAT.md
├─ VOICE-VALIDATION.md
├─ builder/
├─ validator/
├─ references/
└─ requirements.txt
```

Flow 6 lifecycle/output is owned by this kit `README.md` plus `docs/foundation/06-elevenlabs-script-production.md`. The former duplicate `SCRIPT-PRODUCTION.md` owner is retired in v1.11.2.

## Routing

- Flow 5 → `VOICE-EXTRACTION.md`.
- Flow 6 lifecycle/static output → kit `README.md` + Flow 6 foundation policy.
- Flow 6 writing/performance detail → `SOUNDMAKER.md`.
- Flow 7 → `VOICE-VALIDATION.md`.
- optional DOCX export → `DOCX-FORMAT.md` + builder.
- deep Eleven v3 evidence → only the matching reference file when needed.

Do not broad-read every Voice/reference file by default. Recover current project facts before asking the user.

## Canonical boundary

```text
accepted project / PRD meaning
→ work/voice-requirements.md
→ work/voice-production.md
→ output/v<document.version>/prd.html
   → 04 Production Assets
      → matching gameplay moment
         → AUDIO
→ work/voice-acceptance.md
→ state/voice-state.yaml
```

- PRD/project authority owns gameplay/story truth and the fact that a Voice asset is required.
- Flow 5 owns Voice scope, Speaker/Channel/Trigger/Purpose, required communication, exclusions, and source timing truth when present.
- `work/voice-production.md` owns canonical production content, Estimated Duration, and selected actor voice when known.
- `output/v<document.version>/prd.html` is the default derived operator presentation; it is not wording authority.
- DOCX is optional export only.

## Static output contract

Production Assets extends the existing accepted PRD navigation. It must not rebuild Development or renumber PRD package/page identity.

```text
03 Development
   global development pages
   gameplay/objective sections

04 Production Assets
   <gameplay section title>
      <accepted PRD package label>
```

Voice does not own a separate sidebar category and does not create an `Audio → Voice Production` sub-dashboard.

Each canonical line is rendered in its matching natural gameplay moment as:

```text
AUDIO
<Character> — <Line Title>

Function
<communication/story purpose>

Voice Preset
<selected actor voice>

ElevenLabs Model
Eleven v3

Estimated Duration
<duration>

Prompt
<exact canonical performance payload>
```

Character identity in the title replaces a separate visible Speaker field. Flow 5 Trigger/Context, line counts, Primary Speaker summaries, Voice Setup blocks, Purpose, `Must communicate`, `Must not add/repeat`, source refs, reasoning, and QA remain outside the visible reader-first 04 resource unless another current owner explicitly needs them.

Performance directions are visually distinct; copied Prompt bytes remain canonical.

## Semantic vs technical ownership

Use the root `voice-production` specialist for semantic/product-contract defects. When semantics are already correct, route mechanics directly:

- objective/moment-first Production Assets composition/navigation → `kits/project-document-generator/renderer/production_assets_objective.py`;
- Voice-specific Production Assets parsing/presentation primitives → `kits/project-document-generator/renderer/production_assets.py`;
- optional DOCX generation/pagination → `builder/build_docx.py`;
- optional DOCX presentation contract → `DOCX-FORMAT.md`;
- Voice mechanical parity → `validator/validate.py`;
- shared dependency/test/CI → repository-engineering owners.

## Validator / builder rules

- exact Voice ID, Type, and Speaker parity are fail-closed in canonical sources;
- when the current versioned `prd.html` exists, validator checks Voice section/prompt identity and exact canonical payload parity;
- current visible 04 AUDIO field/layout behavior is owned by the Project Document 04 compositor regression, not duplicated as a second Voice HTML schema;
- when optional DOCX exists, validator checks that export too;
- builder/validator PASS does not establish semantic or visual quality;
- never hand-edit `prd.html` or DOCX as the source fix.

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
python kits/project-document-generator/renderer/delivery.py \
  workspace/active/<project>/
```

Direct Voice validator:

```text
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>
```

Use `Voice Verify` for changed Voice semantic/validator contracts and `PRD Verify` when the Production Assets compositor changes.

## Boundaries

- kit owns Flow 5–7 only;
- project definition/PRD belongs to Project Document Generator;
- Production Assets pages are downstream presentation, not a new PRD semantic owner;
- non-dialogue AUDIO remains owned by the Project Document Production Assets contract, not this Voice kit;
- DOCX remains optional compatibility/export, not the default operator surface;
- do not add a second Voice HTML, generic asset framework, or extra workflow layer without a concrete need.
