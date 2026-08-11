# Production + Operating Validation Report

Updated: 2026-08-11

This file owns the **current evidence state** for PRD-Creator. Historical project proof remains useful evidence, but it must not be presented as proof that a later repository revision was re-executed on the same real project.

## Evidence boundary

Keep these evidence classes separate:

- **Current repository/static proof** — current `Local` code, documentation, regression contracts, and GitHub Actions prove the stated repository contract.
- **Current representative real-project proof** — the current Flow 2–4 implementation was exercised against one real project source through production recovery, rendering, semantic review, visual sanity, and handoff.
- **Historical real-project proof** — an earlier repository revision was exercised on a real project; useful for continuity but not proof of later changed contracts.
- **Current DOCX/audio proof** — requires the current Voice/DOCX/audio behavior to be exercised in its real downstream medium.

Static proof must not be upgraded into runtime/visual/audio proof, and one representative project must not be presented as universal proof for every possible project shape.

## Current revision status

Current working branch: `Local`.

The audited PRD-side Flow 1–4 contract set now has both **repository/static/regression proof** and **one current representative real-project/browser proof** using `Aftershock-Adventure-Map FINAL v2.4` as authoritative project source.

| Flow | Current evidence state | Current note |
|---|---|---|
| 1. Repository Boot & Project Memory | **current repository/static proof** | Current-state owners separate current, representative, and historical evidence; CI bookkeeping uses stable proof anchors instead of chasing every docs-only run. |
| 2. Source Intake & Requirement Recovery | **current representative real-project proof + current static contract proof** | A fresh source inventory, requirement register, and truthful `ready_for_prd` state were produced from AFTERSHOCK FINAL v2.4. |
| 3. PRD Generation | **current representative real-project/browser proof + current static contract proof** | Current canonical content projected through the exact current renderer/template into a 28-page Golden HTML document and passed current mechanical validation. |
| 4. PRD Validation & Handoff | **current representative real-project/browser proof + current static contract proof** | The semantic review found real source-fidelity omissions on its first pass, they were corrected at the canonical owner, and the final mechanical/semantic/visual/handoff pass succeeded. |
| 5. Voice Requirement Extraction | **historical real-project proof** | Current Voice requirement completeness remains the next audited weak boundary. |
| 6. Voice Script + DOCX | **historical real-project proof** | Earlier Voice ID/Type parity and DOCX generation were exercised. |
| 7. Voice Validation & Delivery | **historical real-project proof** | Earlier real DOCX visual QA found/fixed the blank-page defect. Audio evidence for that proof remained `not_provided`. |

## Representative current-project proof — AFTERSHOCK FINAL v2.4

### Input and execution boundary

Authoritative project source:

```text
Aftershock-Adventure-Map FINAL v2.4
Minecraft Bedrock / Minecraft Education
```

The proof used the exact current `Local` implementation/template blobs:

```text
renderer/core.py                6debf7968778d7598bb70c19ea8feff435d676b9
renderer/pages.py               9a633a98dbce1d4ba1691da510fd2002384a09ec
renderer/render.py              b9c583e59fa9f32579fe1cb8799a5c3604992f94
validator/validate.py           f1c340323260d42bbd24bd56e0714d165d551d3b
validator/validate_handoff.py   2fd8b46d0a7e8ddf4828f77e0a3e9a45aa765337
template/approved-document.html e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

The representative project was executed in a temporary local workspace and was **not committed into the repository**.

### Flow 2 result

A fresh repository-backed state was built with:

```text
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml → ready_for_prd: true
```

The current Flow 2 contradiction guard passed with required persisted evidence present and no current explicit blocker.

### Flow 3 mechanical result

The current renderer produced:

```text
28 generated document pages
7 Gameplay Flow pages
2 Global Development pages
6 Gameplay Packages × Gameplay Overview / Level Design / Developer
```

The final current mechanical validator result was:

```text
status: pass
errors: []
warnings: []
```

It passed Flow 2 state/evidence, content→projection binding, required Golden hierarchy/content, projection→HTML binding, page set/order, duplicate IDs, Golden composition markers, fragment navigation, and browser title checks.

### Flow 4 semantic result

The first semantic multi-lens pass did **not** simply accept the mechanical PASS. It identified source-fidelity omissions in the produced PRD, including under-specification of:

- Brann demonstrating every Docks tutorial action and the lever door's animation/sound feedback;
- Quarry's explicit scripted-deposit/no-vanilla-hopper boundary and the no-pressure optional stretch rule;
- Ascent's mandatory expectation that players still experience harmless failure rather than tuning falls away;
- Beacon storms continuing on game-time while idle and remaining unmistakably external to children;
- shared short-line/visual guidance and station-specific Adventure Mode permissions.

These findings belonged to the current project requirement/content/projection owners. They were corrected there, then the affected projection was regenerated and revalidated. **No new generic validator rule, schema, checksum, or framework was added.**

Final integrated review:

```text
New Reader: PASS
Level Designer: PASS
Developer: PASS
Project Consistency: PASS
Critical: 0
Major: 0
```

This is important evidence for the intended architecture: deterministic guards catch deterministic defects, while source-fidelity/production judgment remains in Flow 2/4 semantic review.

### Browser visual sanity

The exact generated `final.html` was rendered in headless Chromium at desktop `1440×1000` and mobile `390×844` viewports.

Observed final browser sanity:

- no Chromium console errors or page errors;
- no document-level horizontal overflow at desktop or mobile;
- Overview/sidebar rendered correctly;
- single-language document correctly hid the language selector;
- sidebar package navigation reached the intended Beacon Gameplay/Developer pages after smooth scrolling;
- package tabs reached Level Design;
- Terms Used disclosure opened correctly;
- theme and Overview/Full Detail controls changed UI state;
- dense Beacon Developer table fit desktop without overflow;
- mobile dense tables used their bounded internal scroll wrapper without forcing document-level overflow;
- mobile Menu opened the sidebar from its off-canvas position.

The execution sandbox blocked direct HTTP/file URL navigation, so the exact generated HTML was loaded into Chromium through Playwright `set_content`. The document is self-contained and its inline JavaScript executed during this proof, but URL-origin/localStorage persistence across a real navigation/reload was **not** proven by this run. That boundary does not invalidate the recorded visual/layout/interaction sanity.

### Handoff result

After final semantic + browser acceptance, the representative project recorded:

```text
Status: handoff_ready
Mechanical: PASS
Visual sanity: PASS
New Reader: PASS
Level Designer: PASS
Developer: PASS
Project Consistency: PASS
Critical: 0
Major: 0
```

Current `validate_handoff.py` then passed status, current PRD version `2.4`, current artifact references, and acceptance truth with no errors.

## Historical real-project proof

The Clockwork Vault remains historical evidence that the broader Flow 1–7 model was exercised on an earlier revision. It does not replace the current AFTERSHOCK proof above and does not make later Voice changes automatically current-project verified.

## Stable repository proof anchors

The executable PRD-side contract set remains anchored by:

```text
3ccbf5196d3d3e4c173c440f0a2b5e0d2211a671
Repository Verify #104 — PASS
Production Verify #56 — PASS
Project Document contracts — PASS
```

The aligned canonical validation procedure at:

```text
207f8c9e4aa0d0602b74c60c13c6c69fccdcc7e7
Repository Verify #105 — PASS
Production Verify #57 — PASS
```

These are proof anchors. Live GitHub Actions owns newer execution history; this report is updated when the evidence class, protected claim, or known limitation changes rather than when a later docs-only commit increments a run number.

## Anti-overdevelopment decision — confirmed by real-project proof

The representative run did **not** reveal a need for another PRD guard framework.

The two existing SHA boundaries remain narrow stale-derivation guards:

```text
content.md → render-data.json
render-data.json → final.html
```

The first does not prove semantic equivalence; the representative run directly demonstrated why semantic review remains necessary. No SHA was added for Flow 2 state, acceptance, handoff, or Voice.

Do not extend the PRD guard/checksum architecture without a new concrete defect.

## Known current limitations

Current proof still does not establish:

- universal Flow 2 recovery quality for every source/project shape from one representative project;
- direct URL-origin/localStorage persistence because sandbox browser navigation was blocked;
- operator mistakes that change accepted PRD meaning without advancing the existing `document.version` lifecycle;
- Flow 5 requirement completeness at the executable parser boundary;
- current Voice requirement/script/DOCX revision integrity beyond existing historical checks;
- current generated-audio quality without supplied/reviewed audio.

## Current boundary

The latest PRD Flow 1–4 audit is closed through both **static/regression proof and one representative current real-project/browser proof**. The representative run found production-level omissions, and the existing semantic workflow corrected them without requiring more PRD architecture.

Further PRD guard work should now be driven only by another concrete defect. The next audited system boundary is Flow 5 Voice Requirement Extraction completeness.
