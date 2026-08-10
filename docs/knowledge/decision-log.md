# Decision Log

Use this note only for durable decisions whose reasons must survive future sessions. Active task status belongs in `next-action.md`.

## Current Decisions

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

- **Decision:** `voice_delivery_ready` means the accepted canonical performance script and derived DOCX are ready for downstream ElevenLabs production unless the current task explicitly includes generated audio.
- **Reason:** this kit's core deliverable is the production script/document. Audio quality cannot be inferred when no audio exists.
- **Audio rule:** record `not_provided`, `partial_review`, `reviewed_passed`, or `reviewed_with_findings`; never claim more evidence than exists.
- **Owners:** `docs/foundation/07-voice-validation-delivery.md`, `kits/voice-production-kit/VOICE-VALIDATION.md`.
- **Date:** 2026-08-10

### Flow 7 uses one final acceptance gate

- **Decision:** mechanical integrity + requirement coverage + terminology/pronunciation + speaker/channel/trigger + performance continuity + current DOCX visual QA must pass with Critical=0 and Major=0 before `voice_delivery_ready`.
- **Reason:** a successful builder or attractive DOCX is insufficient evidence of production correctness, while multiple freeze/release ceremonies would add process without value.
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

- **Decision:** preserve the approved HTML presentation shell and regenerate only project-owned content surfaces.
- **Date:** 2026-08-10

### Golden Samples are references, not project requirements

- **Decision:** samples demonstrate quality/structure only where explicitly defined.
- **Date:** 2026-08-10

### Adopt BuildIT principles, not BuildIT domain structure 1:1

- **Decision:** reuse ownership/continuity/validation/minimal-navigation principles without copying irrelevant MCP/Blockbench architecture.
- **Date:** 2026-08-10
