# Voice Production Kit Agent Rules

Root `AGENTS.md` remains authoritative for work mode, proof, skill budget, repository continuity, and the semantic-vs-technical ownership rule. This file narrows behavior only inside `kits/voice-production-kit/`.

## Module Structure

```text
kits/voice-production-kit/
├─ AGENTS.md
├─ SKILL.md
├─ VOICE-EXTRACTION.md
├─ SCRIPT-PRODUCTION.md
├─ DOCX-FORMAT.md
├─ VOICE-VALIDATION.md
├─ builder/
│  └─ build_docx.py
├─ validator/
│  └─ validate.py
└─ requirements.txt
```

`tests/test_voice_contracts.py` is the focused repository regression owner for high-risk generic builder/validator contracts. Root `requirements.lock.txt` owns the exact CI dependency environment.

## Flow Routing

Start from the current accepted project/Voice state and identify the active Flow before opening procedures.

- **Flow 5 — Voice Requirement Extraction**
  - read `VOICE-EXTRACTION.md`;
  - accepted PRD → `work/voice-requirements.md`.
- **Flow 6 — Performance Script + DOCX**
  - read `SCRIPT-PRODUCTION.md`;
  - read `DOCX-FORMAT.md` when DOCX presentation/build mechanics are in scope;
  - Voice requirements → canonical `work/voice-production.md` → derived DOCX.
- **Flow 7 — Voice Validation & Delivery**
  - read `VOICE-VALIDATION.md`;
  - current script/DOCX → acceptance/delivery evidence.

Do not load every Voice document by default.

## Canonical Boundary

```text
accepted PRD
→ work/voice-requirements.md        canonical Voice scope
→ work/voice-production.md          canonical spoken/performance wording
→ output/Voice Production.docx      derived presentation artifact
→ work/voice-acceptance.md          revision-specific evidence
→ state/voice-state.yaml            lifecycle/readiness state
```

`work/voice-production.md` also declares the current `work/voice-requirements.md` normalized-text SHA-256 as mechanical revision evidence. The derived DOCX carries both current requirements + script fingerprints in its core identifier. These hashes prove mechanical freshness only; they do not change authority order.

Never patch the DOCX, state file, or acceptance report to hide a defect in an upstream owner.

## Semantic vs Technical Ownership

Use the root `voice-production` specialist when the wrong behavior is a **Flow 5–7 semantic/product-contract** problem, including:

- which Voice moments exist;
- Voice ID/Type/speaker/channel/trigger scope;
- final spoken/performance wording;
- what the DOCX/delivery artifact is required to represent;
- delivery-readiness/evidence semantics.

When those semantics are already correct and the defect is purely executable mechanics, Maintenance may route directly here without loading a root specialist.

Technical owners:

- Markdown parser / DOCX generation / revision identifier / pagination / paragraph/XML mechanics → `builder/build_docx.py`;
- intentional DOCX presentation contract → `DOCX-FORMAT.md`;
- mechanical requirements/script/DOCX revision, parity, and per-entry checks → `validator/validate.py`.

Do not create/select a Python or DOCX root specialist merely because those implementation technologies appear.

## Contributor Rules

### Flow 5 / Flow 6 semantics

- Flow 5 owns Voice scope; Flow 6 cannot silently add/remove/retype Voice IDs.
- `work/voice-production.md` owns final wording; DOCX never becomes editable wording authority.
- speaker/channel/trigger/project facts come from accepted upstream authority, not from formatting convenience.
- canonical Flow 6 script must declare `Source Voice Requirements SHA-256` for the current requirements text; stale metadata is a mechanical blocker, not a hint to accept old downstream output.

### DOCX builder

- `--requirements` is required for the canonical build path;
- reject the build before writing DOCX when the script-declared requirements fingerprint differs from the current requirements file;
- regenerate from canonical Markdown; never hand-edit the DOCX as the source fix;
- embed current requirements + current script fingerprints in the DOCX core identifier so Flow 7 can prove downstream freshness;
- parser/build failures must fail clearly rather than silently dropping entries;
- later section headings use `page_break_before`, not inserted page-break paragraphs;
- keep presentation changes consistent with `DOCX-FORMAT.md`;
- builder success alone is not visual acceptance.

### Validator

- current requirements fingerprint must equal the hash declared by the canonical script;
- DOCX revision identifier must equal the current requirements + current script fingerprints;
- exact Voice ID and Type parity is fail-closed;
- parse the builder's current visible section/entry structure and validate each Voice entry as one bound unit: section + Type + Voice ID/title + duration + performance;
- section and entry order must match the canonical script;
- global token presence is not sufficient proof of per-entry binding;
- mechanical PASS never substitutes for semantic review, rendered-page inspection, pronunciation evidence, or actual audio review.

## Dependency Contract

Kit-level runtime requirement:

```text
python-docx==1.2.0
```

Repository verification uses exact transitive pins from root `requirements.lock.txt`.

Do not broaden or update dependency versions casually. A dependency change must run `Production Verify` and remain compatible with builder/validator contracts.

## Verification Commands

Run from repository root.

### Install exact verification environment

```text
python -m pip install --disable-pip-version-check --no-deps -r requirements.lock.txt
python -m pip check
```

### Focused contract suite

```text
python -m unittest tests.test_voice_contracts -v
```

This executes the real DOCX builder and real Voice validator against minimal generic fixtures, including:

- Voice ID/Type parity failures;
- section page-break regression;
- stale requirements declaration rejection;
- requirements/script/DOCX revision freshness;
- per-entry DOCX binding when global tokens still exist.

### Compile check

```text
python -m compileall -q kits/voice-production-kit tests/test_voice_contracts.py
```

### Direct builder

```text
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  "workspace/active/<project>/output/Voice Production.docx" \
  --requirements workspace/active/<project>/work/voice-requirements.md
```

### Direct validator

```text
python kits/voice-production-kit/validator/validate.py \
  workspace/active/<project>
```

For repository-side production changes, `Production Verify` is the canonical repeatable CI gate. Run only checks invalidated by the active change when working locally.

## Flow 7 Acceptance Boundary

For Flow 7:

- require a valid current voice state;
- run `validator/validate.py` before semantic acceptance;
- require current requirements/script/DOCX revision integrity;
- compare every Voice ID/Type to Flow 5 requirements;
- review terminology/pronunciation risk, speaker/channel/trigger consistency, and whole-project performance continuity;
- render the DOCX and inspect every page before visual acceptance;
- treat actual audio as optional evidence unless the task explicitly includes audio delivery;
- do not claim generated-audio quality without actually reviewing audio.

## Maintenance

For a concrete Voice defect:

1. classify the first wrong owner: requirement / script / builder mechanics / validator mechanics / acceptance evidence;
2. if semantic/product contract is wrong, route to `voice-production`;
3. if semantics are correct and mechanics are wrong, fix the exact implementation owner here;
4. rebuild only invalidated derived artifacts;
5. rerun the minimum proof invalidated by the change;
6. rendered-page or audio success still requires that actual evidence.

Maintenance does not automatically invoke `development-brief` or a root specialist.

## Boundaries

- This kit owns Flow 5–7 only.
- Project definition/PRD belongs to `kits/project-document-generator/`.
- Repository-wide dependency/test/CI ownership belongs to root `requirements.lock.txt`, `tests/`, `tools/`, and `.github/workflows/`.
- actual generated audio is evidence/output only when supplied; it never becomes upstream authority.
