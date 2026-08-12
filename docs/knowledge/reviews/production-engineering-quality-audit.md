# Production Engineering Quality Audit — P1

Updated: 2026-08-10
Status: **Active execution evidence — audit complete, remediation required before parity can advance**

## Purpose

Audit the current executable PRD-Creator production engine after P0.1 added repeatable contract execution and P0.2 clarified semantic-vs-technical ownership.

This review asks:

> Does the current renderer / validator / DOCX builder / Voice validator fail closed on the contracts it claims to own, and can the repository prove that derived artifacts belong to the current canonical revision?

The audit intentionally does **not** modify production source. It records evidence and converts it into ordered bounded remediation.

## Verdict

P0.1 materially improved repository-side verification, but the executable production engine is **not yet at the relevant BuildIT trust level**.

Current strengths:

- exact verification dependency environment;
- real renderer + validator execution in CI;
- real DOCX builder + Voice validator execution in CI;
- focused negative contracts for scoring/completion conflict, bad numeric total, Voice ID parity, Voice Type parity, and the known DOCX section-break regression;
- fail-closed CI aggregation;
- semantic / browser / rendered-page / audio proof boundaries remain separate.

Material remaining problems are concentrated in:

- derived-artifact freshness / revision identity;
- malformed-input failure handling;
- generated HTML script-data safety;
- DOCX entry binding validation;
- Voice revision traceability;
- a few unhandled parser/builder edge states;
- regression-suite discoverability as the suite grows.

No evidence justifies a generic production-tooling root skill. P0.2 ownership remains current.

---

# Review Method

Primary source inspected:

```text
kits/project-document-generator/renderer/core.py
kits/project-document-generator/renderer/pages.py
kits/project-document-generator/renderer/render.py
kits/project-document-generator/template/approved-document.html
kits/project-document-generator/validator/validate.py
kits/project-document-generator/CONTENT-CONTRACT.md
kits/project-document-generator/RENDERING.md
kits/project-document-generator/VALIDATION.md

kits/voice-production-kit/VOICE-EXTRACTION.md
kits/voice-production-kit/SCRIPT-PRODUCTION.md
kits/voice-production-kit/DOCX-FORMAT.md
kits/voice-production-kit/VOICE-VALIDATION.md
kits/voice-production-kit/builder/build_docx.py
kits/voice-production-kit/validator/validate.py

tests/test_prd_contracts.py
tests/test_voice_contracts.py
requirements.lock.txt
.github/workflows/prd-verify.yml
tools/verify_repository.py
```

Acceptance lens:

- current canonical owner must be identifiable;
- invalid/malformed input must not produce a false PASS or uncontrolled crash at a boundary that claims mechanical validation;
- derived artifacts must not be accepted as current merely because names/page IDs still match;
- project text must not escape its intended HTML/JS context;
- a mechanical validator must compare the relationship it claims, not only global presence of tokens;
- CI must run the focused contracts that exist without silently ignoring new contract tests;
- visual/audio/semantic judgement must remain outside static CI where appropriate.

---

# Findings

## P1-F01 — MAJOR — PRD `final.html` freshness is not mechanically tied to current `render-data.json`

Owner:

```text
kits/project-document-generator/validator/validate.py
+ renderer metadata/fingerprint contract if needed
```

Observed behavior:

- Flow 4 policy requires the same current revision of canonical content, render-data, and rendered HTML.
- The validator reads current `content.md` and current `render-data.json`, but it only compares the HTML through title, expected page IDs, duplicate IDs, and fragment reachability.
- It does not prove that the text/content in `final.html` was generated from the current render-data revision.
- It also checks only that expected generated page IDs are present, not that the rendered generated-page set is exactly current.

False-pass scenario:

```text
render project A
→ edit content.md / render-data.json text while retaining project title + package IDs
→ do NOT rerender final.html
→ mechanical validator can still PASS
```

This directly conflicts with the Flow 4 rule: do not audit an old HTML artifact against newer canonical content.

Impact:

- stale presentation can be handed forward with a mechanical PASS;
- same-project revisions are especially vulnerable because title and IDs commonly remain stable;
- old extra generated sections can survive if expected current pages are also present.

Required direction:

- add the smallest deterministic render revision/fingerprint contract;
- validator must compare current render-data identity to the rendered artifact;
- compare the generated section/page set exactly enough to reject stale extras;
- do not attempt to automate semantic `content.md` → render-data meaning parity; that remains Flow 4 semantic review unless a safe narrow projection contract exists.

## P1-F02 — MAJOR — PRD mechanical validator can crash on malformed render-data instead of returning structured FAIL

Owner:

`kits/project-document-generator/validator/validate.py`

Observed behavior:

`expected_page_ids()` directly indexes:

```text
item["id"]
pkg["id"]
```

for `gameplay_flow`, `global_development`, and `packages`.

Before that call, the validator does not fully establish:

- that `gameplay_flow` is a list of objects with valid IDs;
- that `global_development` is a list of objects with valid IDs;
- that every package is an object with a usable ID for later page calculation.

The package loop can record an error for a malformed package and later still call `expected_page_ids()` on the same malformed raw structure.

Impact:

- a validator whose job is fail-closed mechanical reporting may raise `KeyError` / `TypeError` instead of returning its JSON failure shape;
- malformed or partially-written render data becomes an uncontrolled validator failure;
- P0.1 does not cover this path because the PRD fixture shape is valid.

Required direction:

- complete root/list/item/ID preflight before any downstream page calculation;
- return structured validation errors for malformed types/IDs;
- add focused malformed-shape regressions rather than a broad schema framework.

## P1-F03 — MAJOR — Project glossary JSON can escape the HTML `<script>` context

Owner:

```text
kits/project-document-generator/renderer/pages.py
kits/project-document-generator/renderer/render.py
```

Observed behavior:

- `glossary(data)` carries project-owned labels, definitions, and aliases into a Python object.
- `render.py` serializes it with `json.dumps(..., ensure_ascii=False)` and inserts the result directly into the template JavaScript expression `const glossary = ...`.
- Ordinary page text is escaped through `i18n()` / HTML escaping, but the glossary JSON has no HTML-script-context escaping.

A glossary string containing a literal `</script>` remains `</script>` after normal `json.dumps`, allowing the browser HTML parser to terminate the script element before JavaScript parsing.

Additional shape risk:

- aliases are normalized only when the whole `aliases` value is a list;
- a malformed alias dictionary such as `{ "en": "Alias" }` reaches the browser, where the template expects an array and calls `.forEach()`.

Impact:

- project/source text can break the generated interactive document;
- a crafted glossary value can inject markup/script into the generated HTML context;
- malformed aliases can create a client-side runtime failure that current renderer/validator tests do not detect.

Required direction:

- serialize glossary data safely for an HTML `<script>` context (for example escape `<` / script-closing sequences deterministically);
- validate the small alias shape required by the inherited glossary runtime;
- add focused regression for script-closing text and malformed aliases;
- do not introduce a generic sanitizer framework.

## P1-F04 — MAJOR — Voice revision identity is not mechanically enforced across requirements → script → DOCX/state

Owner:

```text
kits/voice-production-kit/builder/build_docx.py
kits/voice-production-kit/validator/validate.py
state/voice-state.yaml contract
```

Observed behavior:

- Flow 6 policy requires current Voice Requirements and accepted PRD revision.
- `parse_script()` reads `Source Voice Requirements:` but does not require it and the builder does not use it to validate revision identity.
- the builder parity check proves only Voice ID + Type equality.
- the Flow 7 validator checks `voice-state.yaml` only for an allowed `status`; it does not verify source revision/path identity.
- Flow 7 mechanical comparison also proves ID/Type but cannot detect a requirements revision that changed speaker, channel, trigger, purpose, `Must communicate`, or guardrails while retaining the same IDs/Types.

False-pass class:

```text
requirements revision changes material requirement facts
IDs and Types remain unchanged
→ old script/DOCX can still pass current mechanical ID/Type checks
```

Semantic Flow 7 review may catch the content difference, but the repository currently has no mechanical evidence that the artifact set belongs to one revision.

Required direction:

- introduce the smallest revision/fingerprint link across current Voice Requirements, script metadata/state, and derived DOCX validation;
- do not make DOCX the revision authority;
- preserve semantic requirement review for meaning changes.

## P1-F05 — MAJOR — Voice DOCX validator checks global token presence, not entry binding

Owner:

`kits/voice-production-kit/validator/validate.py`

Observed behavior:

The validator concatenates all DOCX paragraphs and then checks:

- each expected Voice ID appears once somewhere;
- each duration appears somewhere;
- each performance text appears somewhere;
- section names appear somewhere.

It does not prove that:

- a given Voice ID is paired with its own title;
- its Type label is correct in the DOCX;
- its duration belongs to that Voice ID;
- its performance paragraph belongs to that Voice ID;
- the entry remains under the correct section.

A corrupted/generated DOCX containing all expected IDs, durations, and scripts but with two entry bodies swapped can satisfy the current global-presence checks.

Impact:

- mechanical PASS can overstate DOCX integrity;
- a future builder regression that mis-associates entry content may survive the current validator.

Required direction:

- parse the derived DOCX sequentially into section/entry blocks using the existing visible structure;
- compare each entry as a bound tuple: section + Type + Voice ID/title + duration + performance text;
- add a focused swapped-entry negative regression;
- rendered-page visual QA remains separate.

## P1-F06 — MEDIUM — Empty Voice section can cause uncontrolled builder `IndexError`

Owner:

`kits/voice-production-kit/builder/build_docx.py`

Observed behavior:

- the script parser accepts `## <section>` headings even when no Voice entries follow;
- empty sections are retained in `VoiceDocument.sections`;
- `section_subtitle()` handles one or two types, otherwise uses `types[-1]`;
- an empty section has zero types and therefore reaches `types[-1]`.

This becomes an uncaught `IndexError`. `main()` catches `OSError` and `ValueError`, not `IndexError`.

Impact:

- malformed canonical script causes a traceback rather than the builder's controlled `VOICE DOCX BUILD FAILED` path;
- Flow 5 explicitly permits gameplay packages with zero voice moments, so empty-section representation must be either deliberately rejected or safely handled rather than accidental.

Required direction:

- decide the canonical Flow 6 rule: omit zero-entry sections or reject them explicitly;
- enforce that rule during parse/preflight with a controlled `ValueError`;
- add one focused regression.

## P1-F07 — MEDIUM — PRD shell/metadata contract is only partially enforced

Owner:

```text
kits/project-document-generator/renderer/render.py
kits/project-document-generator/template/approved-document.html
kits/project-document-generator/validator/validate.py
```

Observed behavior:

- renderer checks deterministic replacement for sidebar brand, nav, main, glossary marker, and `<title>`;
- renderer also attempts to replace `description` and `specification-version` meta tags but does not check replacement count;
- the approved template head currently does not expose those two meta markers in its initial head block, so those substitutions may be silent no-ops;
- Flow 4 validator does not verify retained shell controls/scripts/style markers; a severely stripped HTML containing the right title and section IDs can satisfy the current mechanical checks.

Impact:

- documented “project metadata” behavior is weaker than source suggests;
- shell degradation can false-pass at the mechanical level unless caught manually/visually.

Required direction:

- define a **small stable shell invariant set** actually required for generated artifact usability;
- either require/insert the intended meta markers or remove the dead replacement contract;
- test only stable shell markers, not the entire 794 KB template byte-for-byte.

## P1-F08 — MEDIUM — Production Verify enumerates current test modules explicitly

Owner:

`.github/workflows/prd-verify.yml`

Observed behavior:

The gate runs:

```text
python -m unittest tests.test_prd_contracts -v
python -m unittest tests.test_voice_contracts -v
```

A future focused regression file under `tests/test_*.py` triggers the workflow because `tests/**` changed, but it will not execute unless the workflow is also manually edited to name it.

Impact:

- the test directory can grow while CI silently ignores a newly-added contract module;
- this is a gate-maintenance false-confidence risk, not a current P0.1 failure.

Required direction:

- use deterministic unittest discovery for the repository contract suite, or another small mechanism that makes every canonical `test_*.py` module executable by default;
- preserve useful PRD/Voice reporting if possible without duplicating execution.

## P1-F09 — LOW/MEDIUM — Derived artifact writes are not atomic

Owners:

```text
kits/project-document-generator/renderer/render.py
kits/voice-production-kit/builder/build_docx.py
```

Observed behavior:

- renderer writes directly to the final output path with `write_text()`;
- builder saves directly to the final DOCX path with `doc.save()`.

All content validation happens before the write, which is good. However an I/O/process interruption during the final write can replace a previously good artifact with a partial/corrupt file.

Impact:

- failure-state recoverability is weaker than it could be;
- risk is lower than the false-pass findings above and does not justify a framework.

Required direction:

- after higher-priority contract fixes, consider temp-file + same-directory atomic replace for derived artifacts;
- add only if the implementation remains small and cross-platform enough for current use.

---

# Concrete Non-Findings / Boundaries To Preserve

## HTML text escaping

Normal rendered text passes through `i18n()` / `esc()` and is escaped for HTML text/attribute use. The identified script-context issue is specifically the glossary JSON injection path, not all renderer text.

## P0.1 negative contracts remain useful

The current PRD and Voice tests exercise real CLIs and correctly protect the specific contracts they claim. They should be extended surgically rather than replaced by a broad coverage project.

## Dependency environment

`requirements.lock.txt` exactly pins the current Python 3.11 verification environment, `Production Verify` installs it with `--no-deps`, and `pip check` verifies dependency consistency. No dependency-version change is justified by this audit.

## Semantic / visual / audio proof must remain outside CI

Do **not** automate these into static/mechanical PASS:

- whether `content.md` faithfully expresses project source/requirements;
- whether a PRD is actually usable by New Reader / Level Designer / Developer;
- browser visual quality of the current PRD;
- DOCX page composition/clipping/orphaning;
- pronunciation/performance quality;
- generated audio quality.

These remain Flow 4 / Flow 7 evidence boundaries.

## No generic parser/schema framework

The audit found concrete parser/shape gaps, but no evidence supports reviving the retired generic schema/profile/freeze package. Fix the bounded input contracts at their current owners.

---

# Priority Order

| Order | Finding(s) | Why first |
|---|---|---|
| 1 | P1-F01 + P1-F02 | Flow 4 mechanical trust: stale artifact false-PASS + malformed-input uncontrolled failure |
| 2 | P1-F03 + P1-F07 | renderer/template safety and shell integrity |
| 3 | P1-F04 + P1-F05 | Voice current-revision identity + derived entry binding |
| 4 | P1-F06 | controlled Voice parser/build failure |
| 5 | P1-F08 | CI discovers every focused contract module |
| 6 | P1-F09 | derived-output atomicity if still justified after higher-risk work |

The exact implementation slices are owned by `docs/knowledge/operations/production-engineering-remediation-plan.md`.

## Final Audit Decision

**P1 audit complete; source remediation required.**

Do not resume parity-finalization or broad module/operations polish until the ordered material production findings are repaired and re-proven.

The next bounded slice is **P1.1 — PRD Mechanical Revision Integrity**.
