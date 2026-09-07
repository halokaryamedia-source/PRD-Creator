# PRD Validation & Team Handoff

`CONTENT-CONTRACT.md` owns semantic completeness. `DESIGN-CONTRACT.md` owns approved page/component grammar. This file owns the proof required to accept one current PRD revision.

Mechanical implementation routing:

- `../validator/api.py` → one complete PRD validation API;
- `../validator/prd_validation_engine.py` → source/projection/business-check orchestration;
- `../validator/html_contract.py` → derived HTML freshness/composition/navigation checks;
- `../shared/acceptance.py` → reusable acceptance label/SHA parsing primitives;
- `../validator/validate_handoff.py` → Flow 4→5 handoff gate.

These implementation modules do not replace the semantic acceptance policy in this file.

## Sequence

```text
current Flow 2 approval
+ content.md
+ strict render-data projection
+ required non-Voice 04 source when present
→ canonical mechanical validation
→ integrated semantic reconciliation/readiness
→ Material Conservation
→ targeted visual sanity when claimed
→ development_ready | handoff_ready
```

`development_ready` means the current PRD/required 04 meaning is accepted for implementation. `handoff_ready` additionally binds that accepted revision to the current versioned delivery and is required before Flow 5.

## 1. Mechanical validation

Run:

```bash
python kits/prd-creator/validator/validate.py \
  workspace/active/<project>/
```

`validator/api.py` is the one complete PRD validation API. Handoff validation calls the same API.

Mechanical validation proves deterministic facts including:

- Flow 2 approval hash still matches current requirement-register bytes;
- `render-data.approved_requirement_sha256` matches that exact approved Flow 2 revision;
- retained source hashes/provenance remain coherent;
- `content.md` has no unresolved placeholders;
- `render-data.json` satisfies the one strict projection schema;
- `canonical_content_sha256` matches exact current `content.md` bytes;
- scored/completion result mode is explicit and coherent;
- non-Voice 04 source is parseable and uses accepted Owner/Moment/Asset identity;
- generated HTML is bound to exact render-data and asset-requirements bytes;
- page order/IDs/navigation/component markers remain valid;
- scoring arithmetic and duplicate HTML IDs remain valid.

Mechanical PASS does not prove semantic fidelity or browser visual quality.

## 2. Integrated semantic readiness

Review once through relevant lenses:

| Lens | Ready when... |
|---|---|
| Source Fidelity | material claims remain supported by current authority/approved Proposal |
| Decision Completeness | implementation needs no new product decision |
| New Reader | journey/objective/result/recovery/transition are understandable |
| Level Designer | spaces/objects/relationships/constraints/functions are actionable |
| Developer | trigger/state/timing/result/reset/handoff behavior is actionable |
| Quantitative & Lifecycle | related values and lifecycle states agree |
| Cross-role | Gameplay, Level Design, Developer and required 04 describe one system |
| Content Purity | visible copy explains the project, not generator mechanics |
| Design Placement | meaning uses the approved presentation grammar |

Record only:

```text
Semantic Readiness: PASS | FAIL
```

Do not persist per-lens scores.

## 3. Semantic reconciliation

Compare material meaning across:

```text
approved requirement revision
→ content.md
→ strict render-data projection
→ visible PRD / required 04
```

Look for:

```text
LOSS
CONTRADICTION
UNSUPPORTED
AMBIGUOUS
CROSS-ROLE DRIFT
```

This is semantic comparison, not string parity or a requirement-to-sentence matrix.

## 4. Material Conservation

A readable document may still omit an independent rule. Verify changed/regenerated scope retains explicit representation for every resolved material condition, value, exception, recovery rule, result behavior, technical constraint, and role-owned requirement.

Record:

```text
Material Conservation: PASS | FAIL
```

Do not use word/card/row counts as a quality proxy.

## 5. Visual sanity

Visual `PASS` requires actual rendered/browser evidence. Static HTML inspection may only establish structure and freshness.

For ordinary content changes inspect representative/high-risk pages. Broaden visual QA only for template/CSS/JS/global composition changes, evidence of global breakage, or explicit user request.

## 6. Acceptance record

`work/acceptance.md` authorizes exact bytes, not merely a version number. Machine parsing of the labels/SHA fields is centralized in `shared/acceptance.py`; do not recreate another acceptance regex contract.

```text
# PRD Acceptance
Status: needs_revision | development_ready | handoff_ready
Mechanical: PASS | FAIL
Semantic Readiness: PASS | FAIL
Material Conservation: PASS | FAIL
Visual sanity: PASS | FAIL | NOT PROVEN
Findings: <only when findings exist>
Critical: N
Major: N
Accepted Render Data SHA256: <exact current work/render-data.json SHA-256>
Accepted Asset Requirements SHA256: <exact current work/asset-requirements.md SHA-256 | none>
```

Both binding lines are required for `handoff_ready`.

If `asset-requirements.md` is absent, record exactly:

```text
Accepted Asset Requirements SHA256: none
```

Any edit to render-data or non-Voice 04 source after review invalidates acceptance even if `document.version` is unchanged.

`document.version` is project/release metadata, not an edit counter.

## 7. Handoff

Only `handoff_ready` crosses into Flow 5.

Run:

```bash
python kits/prd-creator/validator/validate_handoff.py \
  workspace/active/<project>/
```

`state/handoff-state.yaml` is strict machine state. It contains only:

```yaml
status: handoff_ready
accepted_prd_version: <X.Y.Z>
content: work/content.md
render_data: work/render-data.json
html: output/v<X.Y.Z>/prd.html
context: output/v<X.Y.Z>/context.md
index: output/v<X.Y.Z>/index.json
acceptance: work/acceptance.md
handoff: output/README.md
```

All refs are canonical project-relative POSIX paths. Absolute paths, `..`, backslashes, aliases, and extra state fields are invalid.

Handoff validation proves:

- the canonical PRD validator still passes;
- version identity agrees across projection and delivery;
- all referenced artifacts exist at canonical paths;
- acceptance binds exact current render-data + asset-requirements bytes.

`output/README.md` is a resume navigator, not a second project-status database.

## Bounded revision

```text
approved change
→ first wrong owner
→ affected canonical/projection/04 source
→ full deterministic rerender
→ mechanical validation
→ integrated review only for invalidated meaning
→ visual check only where changed/high-risk
→ new exact-byte acceptance
→ stop
```

Do not replay unaffected intake/packages/Voice/Golden review for ceremony.
