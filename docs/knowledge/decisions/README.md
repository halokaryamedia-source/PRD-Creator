# Decision Register

Use this note only for durable decisions whose reasons must survive future sessions. Active task status belongs in `next-action.md`.

## Current Decisions

### Consolidated Production Assets preserves accepted PRD navigation identity

- **Decision:** downstream Production Assets extends the existing accepted PRD sidebar instead of rebuilding it. Gameplay/objective sections remain nested under `03 Development`; `04 Production Assets` is additive; existing PRD package/page codes are not shifted. Current Voice navigation uses one `VOICE` category and one link per gameplay Voice section, with section title + exact accepted PRD package label. The existing Flow 5 Trigger may be projected as developer-facing Context without becoming a new Flow 6 field.
- **Reason:** developers need to identify the owning Objective immediately without memorizing order, while a second navigation implementation created hierarchy drift and made downstream Voice presentation alter accepted PRD identity.
- **Boundary:** this changes presentation/composition only. PRD gameplay meaning, canonical Voice wording, Voice scope, Golden template bytes, and audio evidence are unchanged. DOCX remains optional export; consolidated project HTML is the default Voice operator/developer surface.
- **Supersedes/refines:** supersedes the 2026-08-10 decision that Flow 7 default delivery is script/DOCX scope and refines the earlier DOCX-centric acceptance wording below.
- **Owners:** `CONTEXT.md`, `kits/project-document-generator/RENDERING.md`, `kits/voice-production-kit/`, `docs/foundation/06-elevenlabs-script-production.md`, `docs/foundation/07-voice-validation-delivery.md`.
- **Date:** 2026-08-13

### Repository navigation uses explicit domain naming

- **Decision:** domain folders use `README.md` as their index/register; cross-domain files use explicit names such as `work-routing.md`, `ownership.md`, and `source-authority.md`. Historical proof belongs under `reviews/`; `operations/` contains only active/future operational notes. Old navigation aliases are retired rather than preserved as compatibility files.
- **Reason:** the previous mix of `map`, `graph`, `log`, `index`, `minimal-nav`, `flow`, and `flows/` made multiple files appear to own the same question.
- **Boundary:** production semantics, project artifact contracts, Golden bytes, Voice output contracts, and accepted Clockwork content are unchanged.
- **Date:** 2026-08-13

### Exact Golden artifact is also the runtime template; material detail is conserved

- **Decision:** keep `kits/project-document-generator/template/golden-reference.html` and `template/runtime-template.html` byte-identical to the exact approved PRD artifact. The renderer may apply project-specific metadata/storage/navigation/content/glossary binding only to a temporary render copy. Flow 3 must conserve every independently actionable material rule; Flow 4 requires `Semantic Readiness: PASS` (including Golden Placement) plus `Material Conservation: PASS` before new handoff, while Visual sanity remains a separate evidence channel.
- **Reason:** AFTERSHOCK v2.4 proved two separate drift modes: a matching page/CSS shell can still lose dense source meaning, and a cleaned/generic runtime reconstruction can silently rename Golden IDs/classes/components while its own tests certify the reconstruction instead of the Approved document.
- **Boundary:** Golden remains presentation/structure/runtime-DOM authority only and never supplies project-specific mechanics or facts. Exact Golden names (`flow-start`, `shared-*`, `phase-*`, `quarry-*`, `data-phase`) are representation requirements; temporary project metadata/storage namespacing is non-visual runtime binding.
- **Supersedes/refines:** supersedes both the old shorthand “Approved PRD template is preserved as a shell” and the initial 2026-08-12 idea that the exact Golden and a separate cleaned runtime shell could coexist. Refines “Golden Samples are references, not project requirements” so it remains true for project facts but not for explicitly approved visible composition/runtime behavior/information-density requirements.
- **Owner:** `docs/knowledge/decisions/golden-reference-fidelity.md`.
- **Date:** 2026-08-12

### P0.2 keeps three root semantic skills and moves pure technical mechanics to smaller owners

- **Decision:** keep `development-brief`, `project-document-production`, and `voice-production` as the only root repository skills. Narrow the two production specialists to semantic/product-contract ownership. Pure renderer/template/validator/builder mechanics route to nearest kit `AGENTS.md` + exact implementation owner; shared dependency/test/CI mechanics route to `requirements.lock.txt`, `tests/`, `tools/`, and workflows.
- **Reason:** P0.1 proved shared repository engineering without proving a distinct cross-kit artifact/runtime specialist. PRD HTML and Voice DOCX mechanics differ materially, while a Python/tooling skill would be selected by implementation technology rather than the first wrong contract.
- **Skill audit:** candidate Python / production-tooling / artifact-engineering root skill = `DROP AS ROOT SKILL + MOVE TO MODULE-LOCAL / REPOSITORY ENGINEERING`.
- **Boundary:** a mechanical change that alters what an artifact is required to represent/accept becomes semantic/product-contract work again and routes to the matching root specialist.
- **Owner:** `docs/knowledge/decisions/technical-ownership-boundary.md`.
- **Date:** 2026-08-10

### Review bodies preserve captured evidence; review graph owns current interpretation

- **Decision:** dedicated review/audit bodies are time-captured evidence and are not rewritten merely because later implementation changes their status. `docs/knowledge/reviews/README.md` owns the current interpretation (`active evidence`, `implemented`, `historical`, `superseded`, etc.).
- **Reason:** rewriting old reviews destroys reasoning provenance and can make historical findings appear to describe current source.
- **Boundary:** active work order remains in `next-action.md`; durable choices move to the decision owner rather than remaining only in review prose.
- **Date:** 2026-08-10

### Maintenance is root-cause-first and does not automatically use development-brief

- **Decision:** bug/regression/cleanup work follows `docs/knowledge/workflows/maintenance.md`; it starts from observed drift/root cause and uses the smallest owner. `development-brief` remains mandatory for non-trivial Developing work, not Maintenance by default.
- **Reason:** forcing create/change ceremony onto every defect increases context and risks turning repair into redesign.
- **P0.2 refinement:** a pure technical Maintenance task may use no root specialist when nearest module rules + exact implementation owner are sufficient.
- **Date:** 2026-08-10

### Module map, source map, and implementation map have separate jobs

- **Decision:** `module-map.md` routes repository-area ownership, `source-map.md` routes claim/source authority, and `implementation-map.md` points to exact current code/procedure locations.
- **Reason:** one giant ownership/source document would become another broad state system and duplicate current owners.
- **Rule:** maps link owners; they do not copy full source content or become higher authority than the owners they reference.
- **Date:** 2026-08-10

### Formal coordinated change notes require a real cross-owner threshold

- **Decision:** ordinary bounded work does not create OpenSpec-style/formal change machinery. A durable coordinated change note is justified only when several semantic owners, migration phases, or compatibility promises must change as one contract and existing state/decision owners cannot represent it clearly.
- **Reason:** preserve BuildIT's cross-cutting-change discipline without reintroducing planning ceremony for local edits.
- **Owner:** `docs/knowledge/decisions/recording-policy.md`.
- **Date:** 2026-08-10

### Context boot efficiency is measured by scenarios, not assumed from documentation

- **Decision:** `docs/knowledge/operations/boot-baseline.md` records expected routes and measurement fields, but an unrun scenario stays unverified.
- **Reason:** having good routing documents does not prove agents actually reach the correct owner efficiently in real tasks.
- **Date:** 2026-08-10

### Production completion and BuildIT-style operating parity are separate milestones

- **Decision:** completing Flow 1–7, real-project integration, and retired-builder migration does not mean PRD-Creator has achieved BuildIT-style agent operating parity.
- **Reason:** the production pipeline answers how project artifacts are produced; BuildIT-style operating architecture also requires work-mode routing, semantic skill ownership, pre-implementation contracts, root-cause/proof discipline, review/ownership lifecycle, and executable engineering enforcement.
- **Result:** overall relevant parity remains a separate ordered remediation track.
- **Date:** 2026-08-10

### Root skill architecture is three semantic/product-contract owners after P0.2 re-audit

- **Decision:** canonical repository-wide skill root remains `.agents/skills/` with exactly `development-brief`, `project-document-production`, and `voice-production`.
- **Reason:** these remain the smallest reusable root procedures after P0.2. Product/representation semantics stay with root production specialists; pure renderer/template/validator/builder mechanics stay module-local; shared dependency/test/CI mechanics stay repository-engineering owned.
- **Supersedes:** the Phase 1 wording that renderer/validator/DOCX builder mechanics automatically belonged to the semantic specialist whenever those files were involved.
- **Freeze:** do not rename/split/merge/add a root skill unless repeated work proves a reusable ownership/procedure gap that cannot be represented by root policy, foundation, nearest kit procedure/AGENTS, repository engineering, or one current specialist.
- **Owners:** `docs/knowledge/skills/README.md`, `docs/knowledge/skills/activation-matrix.md`, `docs/knowledge/decisions/technical-ownership-boundary.md`.
- **Date:** 2026-08-10

### Developing uses a mandatory brief plus at most one specialist

- **Decision:** every non-trivial create/change task uses `development-brief`; it may add at most one semantic specialist.
- **Reason:** goal/method/reference separation, Build/Acceptance POV, minimal scope, acceptance criteria, and proof budget are cross-cutting baseline needs; specialist stacking increases context and blurs ownership.
- **Fast path:** trivial unambiguous changes may keep the visible brief minimal but still obey the same goal/scope/proof gate.
- **Date:** 2026-08-10

### Root skills route semantic work; kit SKILL/AGENTS files remain production/contributor procedures

- **Decision:** `.agents/skills/` and `kits/*/SKILL.md` / nearest `AGENTS.md` are different layers and must not be merged mechanically.
- **Reason:** root skills own reusable semantic work judgment; kit-local files own detailed Flow procedure plus module-local contributor/technical rules.
- **Date:** 2026-08-10

### Evidence status is baseline behavior, not a standalone skill

- **Decision:** material evidence uncertainty uses root labels `CURRENT-PROJECT VERIFIED`, `AUTHORITATIVE-SOURCE VERIFIED`, `LOCAL PROOF REQUIRED`, `UNSUPPORTED`, and `UNKNOWN`.
- **Reason:** evidence classification applies across owners and should not consume the single specialist slot or create another routing layer.
- **Date:** 2026-08-10

### Production Document Builder v0.2.0 is retired from the live tree

- **Decision:** remove `Production Document Builder/` from `Local` after final retirement audit.
- **Reason:** real Flow 2→7 integration proof passed; every material archive category is mapped to an active owner or intentionally retired; no active runtime dependency remains.
- **Golden safety:** archived and active approved HTML use identical Git blob `e1dccd77d7a5335213caea7a09d74ba78b2ae8e1`.
- **Historical access:** Git history remains the recovery mechanism; do not keep a live duplicate solely for archaeology.
- **Owner:** `docs/knowledge/operations/archived-retirement-audit.md`.
- **Date:** 2026-08-10

### Old multi-profile/schema/freeze/packaging architecture is intentionally retired

- **Decision:** do not migrate the old generic document-profile framework, JSON Schema state stack, Content Freeze ceremony, ZIP/render-report/checksum pipeline, or old browser validator as compatibility layers.
- **Reason:** they validate/operate the retired v0.2.0 architecture, are not active dependencies, and would reintroduce complexity the current product deliberately removed. Future capabilities are added only when a real project proves a concrete need.
- **Date:** 2026-08-10

### Real integration proof validates the Flow 2–7 replacement pipeline

- **Decision:** The Clockwork Vault is the first canonical real-project System Integration Proof for the replacement architecture.
- **Evidence:** 129 recovered requirements → 29-page PRD render → `handoff_ready` → 21 voice requirements → 21 exact-parity scripts → rebuilt/validated 8-page Voice Production DOCX → `voice_delivery_ready`.
- **Authority guard:** legacy Voice Production v2 remained generated/reference-only and did not supply upstream facts.
- **Audio boundary:** `audio_evidence: not_provided`; the proof validates script/DOCX delivery, not generated-audio quality.
- **Owner:** `docs/knowledge/operations/system-integration-proof.md`.
- **Date:** 2026-08-10

### DOCX sections use heading page-break-before, not inserted break paragraphs

- **Decision:** Flow 6 section starts use `Heading 1.paragraph_format.page_break_before = True` rather than an explicit `add_page_break()` paragraph before later sections.
- **Reason:** real Flow 7 visual QA found that explicit break paragraphs can create a blank page when the prior section naturally ends at a page boundary.
- **Proof:** The Clockwork Vault initially rendered a blank page before Ending; after the root fix, the rebuilt DOCX rendered as 8 nonblank pages and passed full reinspection + mechanical revalidation.
- **Owner:** `kits/voice-production-kit/builder/build_docx.py`.
- **Date:** 2026-08-10

### Flow 7 delivery readiness is script/DOCX scope by default

- **Status:** superseded by the 2026-08-13 consolidated Production Assets decision above.
- **Previous decision:** `voice_delivery_ready` meant the accepted canonical performance script and derived DOCX were ready for downstream production unless the current task explicitly included generated audio.
- **Reason at the time:** the kit's core deliverable was script/document and audio quality could not be inferred without audio evidence.
- **Current replacement:** canonical Voice Production + current consolidated project HTML is the default non-audio delivery; DOCX is optional export.
- **Date:** 2026-08-10

### Flow 7 uses one final acceptance gate

- **Status:** refined by the current Flow 7 consolidated project-HTML contract.
- **Decision:** keep one final acceptance gate rather than multiple freeze/release ceremonies. Current gate uses Mechanical + Communication Conservation + integrated Voice Script Readiness + Project HTML Visual when claimed, with optional DOCX/audio evidence only when those scopes exist.
- **Reason:** mechanical success or attractive presentation alone is insufficient evidence of production correctness, while duplicated review ceremonies add process without value.
- **Date:** 2026-08-10

### Pronunciation is evidence-based, not guessed as verified

- **Decision:** only material pronunciation risks are tracked; unusual/high-risk terms require confirmation or intentional acceptance before delivery. Ordinary terms do not require a large pronunciation catalog.
- **Reason:** spelling alone is not proof of generated pronunciation, and unnecessary pronunciation bureaucracy would overcomplicate production.
- **Date:** 2026-08-10

### Flow 6 canonical performance wording stays human-readable; DOCX is derived

- **Decision:** `work/voice-production.md` owns final spoken wording/performance notation; `output/Voice Production.docx` is generated presentation only.
- **Date:** 2026-08-10

### Flow 6 cannot change Flow 5 voice scope silently

- **Decision:** every Flow 5 Voice ID appears exactly once with the same Type in Flow 6 unless Flow 5 is explicitly reopened.
- **Date:** 2026-08-10

### Aftershock Voice Production reference is audited and codified, not duplicated

- **Decision:** use the original v1.0.0 `Voice Production.docx` as audited Flow 6 layout/performance benchmark and record SHA-256 instead of making runtime depend on the binary.
- **SHA-256:** `c76ce2562ee1839ae9174373f510b26da09e7b05f90e43a3e1de820633c34020`.
- **Date:** 2026-08-10

### Legacy paired Aftershock Gameplay HTML is not duplicated into active Voice kit

- **Decision:** current accepted project PRD is factual upstream authority; stale paired V1.2 gameplay reference is not duplicated into active Voice implementation.
- **Date:** 2026-08-10

### Flow 4 uses one development-readiness gate instead of Content Freeze ceremony

- **Decision:** generated PRD becomes development-ready only after mechanical + four-perspective audit passes with Critical=0 and Major=0.
- **Date:** 2026-08-10

### `Local` is the permanent development branch

- **Decision:** normal work continues directly on `Local`; no routine per-flow PRs to `main`.
- **Date:** 2026-08-10

### Repository is project memory

- **Decision:** repository owners are authoritative for continuity; chat is supporting context only.
- **Date:** 2026-08-10

### Project Document Generator and Voice Production remain separate owners

- **Decision:** upstream project definition/PRD work stays separate from downstream voice production.
- **Date:** 2026-08-10

### Source intake uses one slim persistent recovery model

- **Decision:** Flow 2 uses originals + Source Inventory + Requirement Register + Intake State + concise review.
- **Date:** 2026-08-10

### Canonical PRD stays human-readable; renderer projection is derived

- **Decision:** `work/content.md` owns PRD meaning; `work/render-data.json` is derived only.
- **Date:** 2026-08-10

### Approved PRD template is preserved as a shell

- **Status:** superseded by `docs/knowledge/decisions/golden-reference-fidelity.md`.
- **Previous decision:** preserve the approved HTML presentation shell and regenerate only project-owned content surfaces.
- **Date:** 2026-08-10

### Golden Samples are references, not project requirements

- **Status:** refined by `docs/knowledge/decisions/golden-reference-fidelity.md`.
- **Decision:** Golden/reference content never supplies project-specific facts; however the explicitly approved PRD Golden artifact is binding for visible document composition, runtime behavior/DOM vocabulary, and demonstrated information-density/fidelity requirements until the user approves a new design.
- **Date:** 2026-08-10

### Adopt BuildIT principles, not BuildIT domain structure 1:1

- **Decision:** reuse ownership/continuity/validation/minimal-navigation/skill-routing principles without copying irrelevant MCP/Blockbench domain architecture.
- **Date:** 2026-08-10
