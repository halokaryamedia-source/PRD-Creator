# Repository Quality / AI-Slop Audit — 2026-08-14

Status: active remediation evidence
Branch audited: `Local`
Audit scope: repository routing, PRD/Voice semantic owners, renderer/validator architecture, delivery/versioning, tests/CI, and current project handoff behavior.

This review records the complete finding set so remediation does not depend on chat memory. `docs/knowledge/next-action.md` owns the one active step; `docs/knowledge/operations/backlog.md` owns later non-active work. Historical review bodies are not rewritten.

## Summary

The repository has strong intent and substantially better ownership/routing than a typical AI-assisted codebase, but current policy is ahead of parts of the implementation. The main risk is **split-brain current context**: newer versioned-delivery rules coexist with legacy `final.html` assumptions, old compositor behavior, and current-facing docs/tests that can certify each other while remaining inconsistent with the real handoff path.

The cleanup rule is: fix proven current-context/correctness defects first, record the rest, and do not turn this audit into a broad refactor program.

## Findings

| ID | Priority | Finding | Risk | State at capture |
|---|---|---|---|---|
| RQ-01 | P0 | Flow 4 mechanical validator previously resolved the retired unversioned output while current delivery is `output/v<document.version>/prd.html`. | False FAIL/PASS and broken real handoff validation. | FIXED — versioned path resolution + integration proof |
| RQ-02 | P1 | Active semantic/procedure owners still taught retired unversioned HTML naming and, in Voice kit material, retired separate `VOICE` sidebar behavior. | New AI/developer could follow stale authority despite routing cleanup. | FIXED — current owners synchronized and guarded |
| RQ-03 | P1 | Decision memory mixed current and historical language, including retired graph/map routing and old Voice navigation wording. | Wrong-context contamination from files that look authoritative. | FIXED — history-aware register + current routing correction |
| RQ-04 | P1 | Flow 2 could choose material Proposal defaults while `Saran AI` remained optional. | A polished AI guess could become approved project truth without the user noticing which material facts were AI-chosen. | FIXED — every material AI-chosen Proposal is disclosed once before approval |
| RQ-05 | P1 | Development and Production Assets page codes could both produce `04A`, `04B`, etc. | Human/developer page references became ambiguous. | FIXED — Production Assets footer codes use `PA-01`, `PA-02`, ... |
| RQ-06 | P1 | Base PRD HTML was bound to `render-data.json`, but non-Voice `asset-requirements.md` freshness was not equivalently proven. | Asset requirements could change while a stale consolidated `prd.html` still appeared coherent. | FIXED — one current-source hash binding validated by Flow 4 |
| RQ-07 | P1/P2 | `production_assets.py` retained the retired Voice-only compositor/navigation in addition to primitives used by `production_assets_objective.py`. | Dead architecture could attract future AI edits to the wrong owner/path. | FIXED — retired compositor removed; only consumed Voice primitives remain |
| RQ-08 | P2 | Current validator behavior is layered by monkey-patching functions in `validator/_engine.py` from `validator/validate.py`; the old engine still carries stale assumptions. | Patch accumulation makes legacy assumptions easy to miss and hard to retire. | OPEN |
| RQ-09 | P2 | Renderer adapts the exact Golden path by temporarily mutating `_engine.STORAGE_PREFIX_TOKEN`. | Global mutable compatibility-style behavior is non-reentrant and obscures the real current renderer contract. | OPEN |
| RQ-10 | P2 | Golden semantic contract requires exact 4/5/4 flow/note counts in several surfaces. | AI may create filler/paraphrase content only to fill fixed slots, increasing AI-SLOP. | OPEN — design decision required before change |
| RQ-11 | P2 | YAML/state and production Markdown are parsed manually in several owners. | Format variation can be misread; duplicated parsing logic can drift. | OPEN — no schema/framework requested |
| RQ-12 | P2 | `tests/test_prd_content_purity.py` existed but was not executed by `PRD Verify`. | Anti-AI-SLOP regression test could silently rot. | FIXED — included in compile + unittest PRD gate |
| RQ-13 | P3 | Production Assets page IDs were position-based (`production-assets-1`, `-2`, ...). | Adding an earlier section could move deep-link identities inside the same PRD version. | FIXED — semantic shared/journey/package DOM identities |
| RQ-14 | P3 | Several page codes use `chr(65 + index)` with no explicit >26 guard. | Hidden edge-case produces invalid/non-letter page codes for unusually large projects. | OPEN — do not overfix without need |
| RQ-15 | P0 | Clockwork semantic-version migration changed canonical content metadata without refreshing `canonical_content_sha256`. | Current real project fails projection-freshness validation despite unchanged gameplay meaning. | FIXED — canonical binding refreshed from current content bytes |
| RQ-16 | P0 | Flow 4 page-set validation treated the PRD-core page set as the complete HTML page set and rejected valid additive Production Assets pages. | Real downstream projects could fail Flow 4 despite valid core/compositor output. | FIXED — exact PRD-core prefix + Production Assets-only downstream pages |

## Evidence anchors

### RQ-01 — validator/delivery split

- Current delivery owner: `kits/project-document-generator/renderer/delivery.py` → `output/v<document.version>/prd.html`.
- Current mechanical engine: `kits/project-document-generator/validator/_engine.py` still binds `html_path = project / "output" / "final.html"`.
- `tests/test_prd_contracts.py` still renders/reads `output/final.html`, so the test fixture does not exercise the current package path.

### RQ-15 / RQ-16 — real Clockwork proof exposed additional current defects

The first bounded remediation was tested against the real `workspace/active/the-clockwork-vault` package instead of trusting fixture tests alone. The unit suite passed after the provisional versioned-path fix, but real Flow 4 validation still failed for two independent reasons:

1. `render_data_matches_canonical_content` reported that `render-data.json` is stale relative to `content.md`.
2. `generated_page_set_matches_current_render_data` expected only the PRD core but the real consolidated HTML correctly contained six appended `production-assets-*` pages.

Commit history identifies the RQ-15 cause: `feat: add versioned AI-ready PRD delivery` changed Clockwork `content.md` from `Version: Final Review` to `Version: 1.0.0` and changed render-data document version in the same migration, but did not refresh `canonical_content_sha256`. This is a migration binding defect, not evidence that Clockwork gameplay meaning should be regenerated.

RQ-16 must not be "fixed" by accepting arbitrary extra HTML sections. The validator should require the exact PRD-core prefix/order and permit only downstream sections that satisfy the current Production Assets page contract.

### RQ-02 — stale active owners

Current-facing files observed with retired output/navigation wording include:

- `.agents/skills/project-document-production/SKILL.md`
- `.agents/skills/voice-production/SKILL.md`
- `kits/project-document-generator/SKILL.md`
- `kits/project-document-generator/WORKFLOW.md`
- `kits/project-document-generator/RULES.md`
- `kits/project-document-generator/CONTENT-CONTRACT.md`
- `kits/voice-production-kit/SKILL.md`

The fix must update only current routing/procedure meaning; historical audits/changelogs remain capture-time evidence.

### RQ-03 — decision-memory contamination

- `docs/knowledge/decisions/README.md` includes historical/superseded wording under a heading that implies everything is current.
- `docs/knowledge/decisions/recording-policy.md` still routes current implementation ownership through retired `implementation-map.md` / `modules/` terminology.

### RQ-05 / RQ-13 — Production Assets identity

- Gameplay Development page codes are derived from `code = 4 + index` in `renderer/pages.py`.
- Production Assets page codes are independently emitted as `04A`, `04B`, ... in `renderer/production_assets_objective.py`.
- Production Assets DOM IDs are generated from current list position rather than a stable semantic section key.

### RQ-06 — downstream freshness

`render-data-sha256` proves base PRD projection freshness. Current Flow 4 handoff checks file/version presence for the versioned bundle, but non-Voice Production Assets do not yet have an equivalent current-input parity check.

### RQ-07 / RQ-08 / RQ-09 — layered legacy mechanics

- `renderer/render.py` correctly imports `production_assets_objective`, but that module imports `production_assets` for Voice helpers while the latter still retains its own old compositor/navigation functions.
- `validator/validate.py` overrides selected functions on `_engine` rather than being the single current validator owner.
- `renderer/render.py` temporarily changes `_engine.STORAGE_PREFIX_TOKEN` while adapting the exact Golden template.

### RQ-10 — fixed-count pressure

`CONTENT-CONTRACT.md` and `renderer/pages.py` require exact four-card/four-note and five-beat shapes for multiple surfaces. The visual prototype may remain fixed, but semantic cardinality should be reconsidered only with explicit Golden-design approval; do not silently loosen it during maintenance.


## Remediation update — P0 validator/delivery tranche

RQ-01, RQ-15, and RQ-16 are staged for closure together because the real Clockwork proof showed they are one current validation boundary: resolve the versioned PRD, keep canonical content/projection binding current, and distinguish exact PRD core from valid additive Production Assets pages.

The proof for this tranche must include the normal PRD unit contracts plus real Clockwork Flow 4/handoff validation after deterministic delivery regeneration.


## Remediation update — current-context tranche

RQ-02, RQ-03, and RQ-12 are closed without introducing another navigation or quality framework. Current semantic/procedure owners now point to the versioned PRD delivery, the decision register explicitly distinguishes history from current routing, retired map paths no longer own current changes, and the already-existing content-purity regression executes in `PRD Verify`.

## Remediation update — RQ-04 material Proposal visibility

The solve-first Flow 2 model is preserved. The change is only the approval boundary: when AI chooses a material default that changes gameplay or production scope, that chosen value must appear once in the compact `Saran AI` disclosure before blanket preview approval can promote it. This adds no artifact, stage, or option-by-option questionnaire.

## Remediation update — RQ-06 non-Voice asset freshness

The objective-first compositor now embeds one exact binding for `work/asset-requirements.md` only when that source exists. Flow 4 compares it to the current source and also rejects a stale binding after source removal. This is intentionally one freshness proof, not a checksum registry, manifest, or asset framework.

## Remediation update — RQ-05/RQ-13 Production Assets identity

Production Assets still owns top-level section `04`, but its page footer codes now use a separate `PA-##` namespace and its DOM IDs derive from semantic shared/journey/package identity. Accepted PRD Development page codes/IDs are unchanged. This removes human code ambiguity and position-based deep-link drift without a registry.

## Remediation update — RQ-07 retired Voice compositor

The current objective-first compositor remains the sole Production Assets compositor. `production_assets.py` now contains only Voice parsing/presentation primitives actually consumed by that owner; the old Voice-only page/navigation/augmentation entrypoints were deleted instead of preserved as a fallback.

## Ordered remediation

1. **RQ-01 + RQ-15 + RQ-16** — align Flow 4 with versioned delivery, repair the Clockwork migration binding without changing gameplay meaning, and validate exact PRD-core pages plus only valid additive Production Assets pages. Prove against the real Clockwork package, not fixture tests alone.
2. **RQ-02 + RQ-03 + RQ-12** — synchronize current-facing owners/decision routing and ensure the existing content-purity test actually runs in PRD CI.
3. **RQ-04** — make every material AI-chosen Proposal visible once in the Simple Chat Preview without turning preview into a decision questionnaire.
4. **RQ-06** — prove consolidated non-Voice Production Assets are current with their canonical requirements using one bounded mechanism, not a checksum registry/framework.
5. **RQ-05 + RQ-13** — give Production Assets an unambiguous page code and stable semantic DOM IDs; preserve existing PRD Development page identities.
6. **RQ-07** — retire the unused Voice-only compositor path while keeping only Voice primitives actually consumed by the objective-first compositor.
7. **RQ-08** — after the above current behavior is stable, remove validator monkey-patch layering incrementally; do not rewrite the validator wholesale.
8. **RQ-09 / RQ-11 / RQ-14** — address only with a concrete maintenance need or while touching the same owner for a proven defect.
9. **RQ-10** — separate visual Golden capacity from semantic filler pressure only after explicit design approval and real project evidence.

## Stop rule

This audit is **not** permission to refactor everything. A remediation item closes only when its concrete failure/risk is fixed at the first wrong owner and the cheapest relevant proof passes. Do not add Obsidian/Graphify, schema registries, generic asset frameworks, compatibility aliases, new root skills, or additional workflow layers as a response to these findings.
