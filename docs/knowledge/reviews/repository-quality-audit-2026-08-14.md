# Repository Quality / AI-Slop Audit — 2026-08-14

Status: selected active remediation complete; conditional backlog remains
Branch audited: `Local`
Audit scope: repository routing, PRD/Voice semantic owners, renderer/validator architecture, delivery/versioning, tests/CI, and current project handoff behavior.

This review records the complete finding set so remediation does not depend on chat memory. `docs/knowledge/next-action.md` owns the one active step; `docs/knowledge/operations/backlog.md` owns later non-active work. Historical review bodies are not rewritten.

## Summary

The repository had strong intent and substantially better ownership/routing than a typical AI-assisted codebase, but current policy had moved ahead of parts of the implementation. The main audited risk was **split-brain current context**: newer versioned-delivery rules coexisted with legacy unversioned assumptions, old compositor behavior, and current-facing docs/tests that could certify each other while remaining inconsistent with the real handoff path.

The remediation rule remains: fix proven current-context/correctness defects first, record the rest, and do not turn this audit into a broad refactor program.

## Findings

| ID | Priority | Finding | Risk | Current state |
|---|---|---|---|---|
| RQ-01 | P0 | Flow 4 mechanical validator previously resolved the retired unversioned output while current delivery is `output/v<document.version>/prd.html`. | False FAIL/PASS and broken real handoff validation. | FIXED — versioned path resolution + integration proof |
| RQ-02 | P1 | Active semantic/procedure owners still taught retired unversioned HTML naming and, in Voice kit material, retired separate `VOICE` sidebar behavior. | New AI/developer could follow stale authority despite routing cleanup. | FIXED — current owners synchronized and guarded |
| RQ-03 | P1 | Decision memory mixed current and historical language, including retired graph/map routing and old Voice navigation wording. | Wrong-context contamination from files that look authoritative. | FIXED — history-aware register + current routing correction |
| RQ-04 | P1 | Flow 2 could choose material Proposal defaults while `Saran AI` remained optional. | A polished AI guess could become approved project truth without the user noticing which material facts were AI-chosen. | FIXED — every material AI-chosen Proposal is disclosed once before approval |
| RQ-05 | P1 | Development and Production Assets page codes could both produce `04A`, `04B`, etc. | Human/developer page references became ambiguous. | FIXED — Production Assets footer codes use `PA-01`, `PA-02`, ... |
| RQ-06 | P1 | Base PRD HTML was bound to `render-data.json`, but non-Voice `asset-requirements.md` freshness was not equivalently proven. | Asset requirements could change while a stale consolidated `prd.html` still appeared coherent. | FIXED — one current-source hash binding validated by Flow 4 |
| RQ-07 | P1/P2 | `production_assets.py` retained the retired Voice-only compositor/navigation in addition to primitives used by `production_assets_objective.py`. | Dead architecture could attract future AI edits to the wrong owner/path. | FIXED — retired compositor removed; only consumed Voice primitives remain |
| RQ-08 | P2 | Current validator behavior was layered by monkey-patching `_engine.py` from `validate.py`. | Patch accumulation made current ownership easy to miss. | FIXED — current Golden/readiness mechanics live directly in `_engine.py`; wrapper only adds purity/CLI |
| RQ-09 | P2 | Renderer adapts the exact Golden path by temporarily mutating `_engine.STORAGE_PREFIX_TOKEN`. | Global mutable compatibility-style behavior is non-reentrant and obscures the real current renderer contract. | OPEN — conditional maintenance |
| RQ-10 | P2 | Golden semantic contract requires exact 4/5/4 flow/note counts in several surfaces. | AI may create filler/paraphrase content only to fill fixed slots, increasing AI-SLOP. | OPEN — explicit design approval required |
| RQ-11 | P2 | YAML/state and production Markdown are parsed manually in several owners. | Format variation can be misread; duplicated parsing logic can drift. | OPEN — conditional maintenance; no schema/framework requested |
| RQ-12 | P2 | `tests/test_prd_content_purity.py` existed but was not executed by `PRD Verify`. | Anti-AI-SLOP regression test could silently rot. | FIXED — included in compile + unittest PRD gate |
| RQ-13 | P3 | Production Assets page IDs were position-based (`production-assets-1`, `-2`, ...). | Adding an earlier section could move deep-link identities inside the same PRD version. | FIXED — semantic shared/journey/package DOM identities |
| RQ-14 | P3 | Several page codes use `chr(65 + index)` with no explicit >26 guard. | Hidden edge-case produces invalid/non-letter page codes for unusually large projects. | OPEN — only when a real >26 need exists |
| RQ-15 | P0 | Clockwork semantic-version migration changed canonical content metadata without refreshing `canonical_content_sha256`. | Current real project fails projection-freshness validation despite unchanged gameplay meaning. | FIXED — canonical binding refreshed from current content bytes |
| RQ-16 | P0 | Flow 4 page-set validation treated the PRD-core page set as the complete HTML page set and rejected valid additive Production Assets pages. | Real downstream projects could fail Flow 4 despite valid core/compositor output. | FIXED — exact PRD-core prefix + Production Assets-only downstream pages |

## Evidence anchors

The bullets below preserve **capture-time defect evidence**. They intentionally describe what was wrong when the audit was taken; the Findings table and remediation updates above/below record current status after fixes.

### RQ-01 — validator/delivery split

At capture time:

- current delivery owner was `kits/project-document-generator/renderer/delivery.py` → `output/v<document.version>/prd.html`;
- the mechanical engine still bound `html_path` to the retired unversioned output;
- `tests/test_prd_contracts.py` still rendered/read that same retired output, so the fixture did not exercise the real package path.

### RQ-15 / RQ-16 — real Clockwork proof exposed additional current defects

The first bounded remediation was tested against the real `workspace/active/the-clockwork-vault` package instead of trusting fixture tests alone. The unit suite passed after the provisional versioned-path fix, but real Flow 4 validation still failed for two independent reasons:

1. `render_data_matches_canonical_content` reported that `render-data.json` was stale relative to `content.md`.
2. `generated_page_set_matches_current_render_data` expected only the PRD core while the real consolidated HTML correctly contained six appended Production Assets pages.

Commit history identified the RQ-15 cause: `feat: add versioned AI-ready PRD delivery` changed Clockwork `content.md` from `Version: Final Review` to `Version: 1.0.0` and changed render-data document version in the same migration, but did not refresh `canonical_content_sha256`. This was a migration binding defect, not evidence that Clockwork gameplay meaning should be regenerated.

RQ-16 was fixed without accepting arbitrary extra HTML sections: the validator requires the exact PRD-core prefix/order and permits only downstream sections that satisfy the current Production Assets page contract.

### RQ-02 — stale active owners

At capture time the following current-facing owners still contained retired output/navigation wording:

- `.agents/skills/project-document-production/SKILL.md`
- `.agents/skills/voice-production/SKILL.md`
- `kits/project-document-generator/SKILL.md`
- `kits/project-document-generator/WORKFLOW.md`
- `kits/project-document-generator/RULES.md`
- `kits/project-document-generator/CONTENT-CONTRACT.md`
- `kits/voice-production-kit/SKILL.md`

They have since been synchronized; historical audits/changelogs remain capture-time evidence.

### RQ-03 — decision-memory contamination

At capture time:

- `docs/knowledge/decisions/README.md` mixed historical/superseded wording under a heading that implied current authority;
- `docs/knowledge/decisions/recording-policy.md` routed current implementation ownership through retired implementation-map/modules terminology.

Current decision routing now uses the consolidated ownership/source-authority structure.

### RQ-05 / RQ-13 — Production Assets identity

At capture time:

- Gameplay Development page codes were derived from `code = 4 + index` in `renderer/pages.py`;
- Production Assets independently emitted `04A`, `04B`, ...;
- Production Assets DOM IDs were generated from list position rather than stable semantic section identity.

The current compositor keeps Development identities untouched, uses `PA-##` for Production Assets footer codes, and uses stable shared/journey/package DOM identities.

### RQ-06 — downstream freshness

At capture time `render-data-sha256` proved base PRD projection freshness, while non-Voice Production Assets had no equivalent source-freshness proof. The current compositor/Flow 4 path now uses one bounded `asset-requirements-sha256` binding only when `work/asset-requirements.md` exists; it is not a manifest or checksum registry.

### RQ-07 / RQ-08 / RQ-09 — layered legacy mechanics

At capture time:

- the active objective-first compositor reused Voice primitives from a module that still also retained an alternate Voice-only compositor;
- `validator/validate.py` overrode selected `_engine` functions at runtime;
- `renderer/render.py` temporarily changed `_engine.STORAGE_PREFIX_TOKEN` while adapting the exact Golden template.

RQ-07 and RQ-08 are fixed. RQ-09 remains conditional because no current defect justifies another renderer refactor by itself.

### RQ-10 — fixed-count pressure

`CONTENT-CONTRACT.md` and `renderer/pages.py` require exact four-card/four-note and five-beat shapes for multiple surfaces. The visual prototype may remain fixed, but semantic cardinality should be reconsidered only with explicit Golden-design approval; do not silently loosen it during maintenance.

## Remediation update — P0 validator/delivery tranche

RQ-01, RQ-15, and RQ-16 were closed together because real Clockwork proof showed they shared one current validation boundary: resolve the versioned PRD, keep canonical content/projection binding current, and distinguish exact PRD core from valid additive Production Assets pages.

## Remediation update — current-context tranche

RQ-02, RQ-03, and RQ-12 were closed without introducing another navigation or quality framework. Current semantic/procedure owners point to the versioned PRD delivery, the decision register explicitly distinguishes history from current routing, retired map paths no longer own current changes, and the existing content-purity regression executes in `PRD Verify`.

## Remediation update — RQ-04 material Proposal visibility

The solve-first Flow 2 model is preserved. The change is only the approval boundary: when AI chooses a material default that changes gameplay or production scope, that chosen value must appear once in the compact `Saran AI` disclosure before blanket preview approval can promote it. This adds no artifact, stage, or option-by-option questionnaire.

## Remediation update — RQ-06 non-Voice asset freshness

The objective-first compositor embeds one exact binding for `work/asset-requirements.md` only when that source exists. Flow 4 compares it to the current source and also rejects a stale binding after source removal. This is intentionally one freshness proof, not a checksum registry, manifest, or asset framework.

## Remediation update — RQ-05/RQ-13 Production Assets identity

Production Assets still owns top-level section `04`, but its page footer codes use a separate `PA-##` namespace and its DOM IDs derive from semantic shared/journey/package identity. Accepted PRD Development page codes/IDs are unchanged. This removes human code ambiguity and position-based deep-link drift without a registry.

## Remediation update — RQ-07 retired Voice compositor

The current objective-first compositor remains the sole Production Assets compositor. `production_assets.py` contains only Voice parsing/presentation primitives actually consumed by that owner; the old Voice-only page/navigation/augmentation entrypoints were deleted instead of preserved as a fallback.

## Remediation update — RQ-08 validator layering

The validator was not rewritten. The three current overrides were moved into the existing mechanical engine and runtime monkey-patch assignments were removed. `validate.py` remains a narrow content-purity/CLI wrapper. This closes the patch-on-patch ownership defect without introducing hooks, profiles, or another validator layer.

## Visual proof update — RQ-05/RQ-13

The visible `PA-##` footer-code change received actual Chromium layout proof at 1500×1000 and 1000×1000 on the current Clockwork delivery. Production Assets navigation/page activation, footer-code placement, and horizontal overflow checks passed at both widths. RQ-05/RQ-13 are mechanically and visually closed for the claimed desktop scope.

## Ordered remediation

Completed selected active remediation is preserved above. Remaining work is intentionally limited to the conditional/design-sensitive items in `docs/knowledge/operations/backlog.md`; promote only one when real evidence or explicit design intent justifies it.

## Stop rule

This audit is **not** permission to refactor everything. A remediation item closes only when its concrete failure/risk is fixed at the first wrong owner and the cheapest relevant proof passes. Do not add Obsidian/Graphify, schema registries, generic asset frameworks, compatibility aliases, new root skills, or additional workflow layers as a response to these findings.
