# Voice Production Kit Agent Rules

Root `AGENTS.md` remains authoritative for work mode, proof, skill budget, repository continuity, and semantic-vs-technical ownership. This file narrows behavior only inside `kits/voice-production-kit/`.

## Module Structure

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
│  └─ build_docx.py
├─ validator/
│  └─ validate.py
├─ references/
│  ├─ aftershock/
│  └─ elevenlabs/
└─ requirements.txt
```

`tests/test_voice_contracts.py` remains the focused regression owner for generic builder/validator contracts. Root `requirements.lock.txt` owns the exact CI dependency environment.

## Flow Routing

Start from current accepted project/Voice state and identify the active Flow before opening procedures.

- **Flow 5 — Voice Requirement Extraction**
  - read `VOICE-EXTRACTION.md`;
  - accepted PRD → `work/voice-requirements.md`.
- **Flow 6 — Eleven v3 Performance Script + DOCX**
  - read `SCRIPT-PRODUCTION.md`;
  - for an actual one-line Eleven v3 prompt/revision, read `SOUNDMAKER.md`;
  - read only the relevant `references/elevenlabs/` page when production-technique evidence is needed;
  - read `DOCX-FORMAT.md` only when DOCX presentation/build mechanics are in scope;
  - Voice requirements → SoundMaker quality pass → canonical `work/voice-production.md` → derived DOCX.
- **Flow 7 — Voice Validation & Delivery**
  - read `VOICE-VALIDATION.md`;
  - current script/DOCX/audio evidence → acceptance/delivery evidence.

Do not load every Voice or ElevenLabs document by default.

## Canonical Boundary

```text
accepted PRD
→ work/voice-requirements.md        canonical Voice scope
→ SoundMaker v3 quality pass         execution procedure only
→ work/voice-production.md          canonical spoken/performance wording
→ output/Voice Production.docx      derived presentation artifact
→ work/voice-acceptance.md          revision-specific evidence
→ state/voice-state.yaml
```

SoundMaker never becomes a parallel source of truth.

If the exact prompt actually generated/approved differs from canonical wording, synchronize it back into `work/voice-production.md` before claiming current alignment. If that change invalidates a derived DOCX/acceptance state, rebuild/reopen only the affected scope.

## SoundMaker Rules

- model scope is **Eleven v3 only**;
- one active Voice ID at a time for real generation/revision;
- user-facing output is one best paste-ready prompt by default;
- duration is planned before final wording when specified;
- build emotion through scene-driven performance beats, not random tag changes;
- spoken wording and punctuation/line structure come before extra tags;
- a flat script is not repaired by stacking emotional synonyms;
- reactions are timeline events;
- no SSML `<break>` for v3;
- environment/SFX prompts stay outside the voice lane;
- do not claim audio quality, pronunciation, or measured duration without actual evidence.

## Semantic vs Technical Ownership

Use the root `voice-production` specialist when the wrong behavior is a **Flow 5–7 semantic/product-contract** problem, including:

- which Voice moments exist;
- Voice ID/Type/speaker/channel/trigger scope;
- final spoken/performance wording;
- SoundMaker quality behavior that changes what a production-ready v3 prompt must represent;
- what the DOCX/delivery artifact is required to represent;
- delivery-readiness/evidence semantics.

When semantics are already correct and the defect is purely executable mechanics, Maintenance may route directly here without loading a root specialist.

Technical owners:

- Markdown parser / DOCX generation / pagination / paragraph/XML mechanics → `builder/build_docx.py`;
- intentional DOCX presentation contract → `DOCX-FORMAT.md`;
- mechanical requirements/script/DOCX parity checks → `validator/validate.py`.

Do not create/select a Python, DOCX, tag, or ElevenLabs root specialist merely because those surfaces appear.

## Contributor Rules

### Flow 5 / Flow 6 semantics

- Flow 5 owns Voice scope; Flow 6 cannot silently add/remove/retype Voice IDs.
- `work/voice-production.md` owns final wording; DOCX and generated audio never become editable upstream meaning authority.
- speaker/channel/trigger/project facts come from accepted upstream authority, not from performance convenience.

### SoundMaker / Eleven v3

- use `SOUNDMAKER.md` for actual v3 prompt quality;
- use `references/elevenlabs/README.md` as evidence-backed technique, not a project-fact source;
- preserve exact user-generated prompt if the user edited it before approval;
- project-calibrated approved audio can guide later performance decisions but never changes upstream facts.

### DOCX builder

- regenerate from canonical Markdown; never hand-edit DOCX as the source fix;
- parser/build failures must fail clearly rather than silently dropping entries;
- later section headings use `page_break_before`, not inserted page-break paragraphs;
- builder success alone is not visual acceptance.

### Validator

- exact Voice ID and Type parity is fail-closed;
- DOCX must contain current script entries/sections/durations/performance text at the mechanical level claimed;
- mechanical PASS never substitutes for semantic review, rendered-page inspection, pronunciation evidence, or actual audio review.

## Dependency Contract

Kit-level runtime requirement:

```text
python-docx==1.2.0
```

Repository verification uses exact transitive pins from root `requirements.lock.txt`.

Do not broaden/update dependency versions casually. A dependency change must run `Voice Verify` and remain compatible with builder/validator contracts.

## Verification Commands

Run from repository root.

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

For repository-side production changes, `Voice Verify` is the canonical repeatable CI gate. Run only checks invalidated by the active change when working locally.

## Flow 7 Acceptance Boundary

For Flow 7:

- require a valid current voice state;
- run `validator/validate.py` before semantic acceptance;
- compare every Voice ID/Type to Flow 5 requirements;
- review terminology/pronunciation risk, speaker/channel/trigger consistency, and whole-project performance continuity;
- render DOCX and inspect every page before visual acceptance;
- if actual audio exists, verify it was generated from/synchronized with current canonical prompt before approving audio scope;
- do not claim generated-audio quality without actual review.

## Maintenance

For a concrete Voice defect:

1. classify the first wrong owner: requirement / SoundMaker-script semantics / builder mechanics / validator mechanics / acceptance evidence;
2. if semantic/product contract is wrong, route to `voice-production`;
3. if semantics are correct and mechanics are wrong, fix the exact implementation owner here;
4. rebuild only invalidated derived artifacts;
5. rerun the minimum proof invalidated by the change;
6. rendered-page or audio success still requires actual evidence.

## Boundaries

- This kit owns Flow 5–7 only; SoundMaker is inside Flow 6, not Flow 8.
- SoundMaker production model scope is Eleven v3 only.
- Project definition/PRD belongs to `kits/project-document-generator/`.
- SFX generation remains a separate production lane.
- Repository-wide dependency/test/CI ownership belongs to root `requirements.lock.txt`, `tests/`, `tools/`, and `.github/workflows/`.
- actual generated audio is evidence/output only when supplied; it never becomes upstream project authority.
