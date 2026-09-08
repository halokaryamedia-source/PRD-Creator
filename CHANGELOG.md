# Changelog

PRD-Creator tracks two separate version domains:

- published repository releases use protected Git tags such as `v0.1` on `main`;
- the PRD-Creator product/package version is owned by `kits/prd-creator/README.md` and follows product/contract semantics.

A repository tag/GitHub Release is created only when an approved feature/capability change is promoted to stable release state. Repository hygiene, CI, governance, ruleset, documentation, and maintenance-only updates may remain untagged.

## Unreleased

### Repository maintenance — unversioned

- keep stable release/tag policy separate from package contract versioning;
- preserve explicit branch-governance and clean-history boundaries;
- keep repository/CI guidance aligned with the current package architecture.

The latest published repository release remains `v0.1` until a later approved capability release is promoted/published.

## Package 3.1.1 — 2026-09-08

Backward-compatible Voice naturalness correction focused on reducing stiff, document-like, or over-directed Eleven v3 output without changing Voice IDs, lifecycle state, accepted PRD meaning, or the Golden presentation.

### Natural spoken-language craft

- add a dedicated `v3-naturalness.md` craft reference for speechification, register-aware dialogue/narration, thought-group prosody, natural sentence variation, and stiffness diagnosis;
- make Flow 6 explicitly preserve approved communication meaning rather than accidental PRD sentence syntax, allowing context-aware compression, contractions, sentence regrouping, and listener-first wording when appropriate;
- add a text-only Naturalness gate so a prepared line must sound plausibly speakable for its Speaker/Trigger/register before generation is considered ready;
- clarify that naturalness does not mean automatic casualness, filler words, slang, fragments, or manufactured hesitation.

### Optional direction instead of tag boilerplate

- retire the repository-only rule that every `performance` block must begin with an Audio Tag;
- make zero-tag Eleven v3 prompts mechanically valid when voice fit, wording, punctuation, and context already imply the desired delivery;
- treat Audio Tags as local interventions for a concrete audible state/reaction rather than mandatory prompt decoration;
- reject over-direction conceptually through naturalness review instead of forcing `[calm]`, `[clear]`, `[natural]`, `[conversational]`, or synonymous tag stacks onto every line.

### Narration and generation continuity

- add current TTS `previous_text` / `next_text` and neighboring `previous_request_ids` / `next_request_ids` guidance for connected same-speaker narration that must be generated in separate clips;
- preserve canonical `VO-...` wording while using generation-only context to improve prosodic continuity, especially when regenerating a middle segment;
- route short connected lines toward relevant context rather than audible filler, and retain Text to Dialogue for response-dependent multi-speaker continuity.

### Voice foundation and settings

- deepen Voice Design guidance around language/dialect, timbre/persona, pacing, delivery, and preview-text alignment so the baseline actor is closer to the intended performance before per-line direction;
- keep Stability at `Natural` by default and make Speed surface-aware with `1.0`/unchanged as the natural baseline when exposed;
- prioritize voice fit → spoken wording → thought groups → continuity → punctuation/tags before attempting to repair stiffness with Stability or Speed.

## Package 3.1.0 — 2026-09-08

Additive ElevenLabs production-quality update. Existing Asset/Voice machine schemas, stable IDs, accepted Golden presentation, and Flow 2–7 lifecycle remain backward-compatible.

### Voice generation quality

- route independent Voice IDs to Eleven v3 Text to Speech and conversationally dependent multi-speaker Voice IDs in the same approved Moment to Eleven v3 Text to Dialogue;
- preserve every existing `VO-...` as canonical and keep Dialogue grouping ephemeral instead of introducing a parallel Dialogue schema;
- add current Dialogue request-limit, candidate-selection, seed/language/pronunciation/normalization, and `with-timestamps` guidance;
- prefer candidate comparison/same-content regeneration before rewriting otherwise-correct prompts after one nondeterministic weak take;
- update long-form routing to current ElevenCreative Studio and retire deprecated Voiceover Studio Fixed Duration as current policy;
- clarify standard Eleven v3 TTS Speed availability vs Studio-specific production controls.

### Sound Effects production

- add `production-assets/SOUND-EFFECTS.md` as the detailed ElevenLabs `eleven_text_to_sound_v2` execution owner for existing non-dialogue `AUDIO` requirements;
- keep `work/asset-requirements.md` as the only canonical SFX meaning source while deriving prompt/settings/candidate evidence during production;
- add prompt construction, layering, duration/loop/prompt-influence, candidate review, troubleshooting, output, and approval discipline without creating a new numbered Flow or SFX manifest;
- maintain a hard boundary between non-dialogue SFX and Voice dialogue/narration.

### Source and verification freshness

- refresh Eleven v3 source authority to current Text to Dialogue, timestamps, and ElevenCreative Studio documentation as of 2026-09-08;
- make Voice Verify trigger on Voice skill/foundation/procedure/reference changes rather than Python-only Voice paths.

## Package 3.0.0 — 2026-09-07

End-to-end contract synchronization. Package 3 removes the remaining parallel machine vocabularies and makes readiness/identity/freshness explicit from Flow 2 through Flow 7.

### Flow 2 authority and approval

- make `status` the single Flow 2 readiness truth and retire duplicate `ready_for_prd`, `next_step`, and similar state aliases;
- bind Simple Chat Preview approval to exact current `state/requirement-register.yaml` bytes through `approved_requirement_sha256`;
- add strict source-inventory and requirement-register parsing with unique IDs, current provenance checks, Proposal approval rules, retained-source hash verification, and duplicate-safe YAML;
- reject stale approval automatically after a same-file requirement edit;
- add safe project-relative path normalization for persisted state refs.

### Strict PRD projection

- make `work/render-data.json` a single strict projection vocabulary instead of a tolerant compatibility format;
- bind projection to exact current `work/content.md` bytes through `canonical_content_sha256`;
- introduce explicit `gameplay.result_model.mode = scored | completion_only` plus upstream-owned result summary;
- require Developer scoring/completion data to match the explicit Gameplay result mode;
- remove renderer-side semantic recovery and historical field aliases;
- enforce bilingual numeric/percentage/stable-ID invariants in addition to en/id presence.

### Production Assets identity

- extend stable identity to `Owner ID → Moment ID → Resource ID`;
- add `MOM-...` identity shared by non-Voice and Voice resources;
- retire human-readable `Flow:` / numbered Gameplay Flow metadata as machine ordering keys;
- reject unknown/duplicate/legacy 04 fields instead of silently accepting them;
- merge 04 resources deterministically by accepted Owner topology + Moment identity;
- extract Production Assets CSS/JavaScript into renderer static resources while preserving standalone inlined HTML delivery.

### Exact acceptance chain

- bind Flow 4 acceptance to exact current `render-data.json` and `asset-requirements.md` bytes (`none` when no non-Voice source exists);
- make handoff state strict and path-safe;
- bind Flow 6 production to exact current Voice Requirements bytes;
- bind final Flow 7 acceptance to exact current `voice-production.md` bytes;
- verify consolidated HTML against exact current Asset/Voice source SHA bindings.

### Voice lifecycle

- make Flow 5 own Owner ID + Moment ID because placement is project topology rather than performance craft;
- use one Voice lifecycle vocabulary across Flow 5–7 and reject retired fields;
- make Voice validation lifecycle-aware so `voice_requirements_ready` can be mechanically checked before Flow 6 creates a script;
- require final Voice delivery to have a selection/profile for every represented speaker and current exact-production acceptance;
- validate Voice resources on the exact Owner page + Moment ID group.

### Source architecture and delivery

- centralize retained Golden/reference shell compatibility in `renderer/template_adapter.py`;
- remove reference-project vocabulary from generic renderer orchestration;
- move internal renderer/validator modules toward package-relative imports with CLI bootstrap only at executable boundaries;
- add structured validation issue metadata and a line-aware parser-error primitive;
- publish complete version directories transactionally with rollback instead of replacing bundle files independently;
- keep one schema owner per machine contract and shorten duplicated procedure/instruction documentation for lower model context usage.

Package 3.0 is intentionally incompatible with Package 2.0 machine-authored project state/artifacts. Active projects should regenerate/update Flow 2 state, strict render projection, non-Voice Moment IDs, Voice Moment IDs, Flow 4 acceptance, and final Voice acceptance using the 3.0 contracts. The protected Golden visual artifact remains unchanged.

## Package 2.0.0 — 2026-09-07

Source-code and machine-identity hardening for a stricter professional production boundary.

### Correctness and identity

- make `validator/api.py` the single complete PRD validation entrypoint and route handoff through the same content-purity/freshness checks;
- bind Flow 4 acceptance to the exact reviewed `work/render-data.json` SHA-256 so same-version regeneration cannot reuse stale acceptance evidence;
- parse machine-owned YAML through pinned PyYAML instead of regex/line emulation;
- require stable Production Asset Owner IDs and non-Voice `AST-...` resource IDs;
- require stable Owner IDs on canonical Voice Production sections and join 04 presentation by those IDs rather than display titles;
- reject duplicate/missing/unknown identities instead of silently collapsing or guessing them.

### Source architecture

- retire ambiguous renderer/validator `_engine.py` module names in favor of domain-specific engine names;
- centralize typed Voice requirements/production parsing in `shared/voice.py`;
- centralize machine-state parsing in `shared/state.py`;
- reduce semantic fallback behavior in the 04 compositor so renderer code presents owned meaning rather than inventing defaults;
- stage versioned delivery before replacing current output files.

### Engineering quality

- separate runtime and development dependency locks;
- add Ruff static lint, mypy checks for shared typed parsers/state, and coverage reporting to active gates;
- pin GitHub Actions references in active workflows to immutable commit SHAs;
- strengthen regression coverage for exact acceptance binding, content-purity handoff, quoted YAML, duplicate IDs/owners, and stable asset/Voice identity.

This is a major package contract because existing `asset-requirements.md` / `voice-production.md` internal sources must be regenerated or updated with explicit stable Owner/Asset IDs. Golden/runtime template bytes and accepted PRD semantic/design boundaries remain unchanged.

## Package 1.16.0 — 2026-09-07

Semantic/design separation and adaptive PRD composition while preserving the exact Golden artifact and deterministic renderer architecture.

### Semantic / design ownership

- split PRD semantic completeness into `document/CONTENT-CONTRACT.md` and Golden presentation grammar into `document/DESIGN-CONTRACT.md`;
- keep page family, navigation, stable component vocabulary, meaningful fixed summary slots, and exact Golden/runtime template bytes protected;
- record the durable Adaptive Semantic Composition decision as a refinement of the earlier Golden fidelity decision.

### Adaptive composition

- stop treating AFTERSHOCK sample counts such as four flow cards, four note cards, or five compact gameplay steps as universal project semantics;
- preserve project-driven child cardinality inside existing approved Flow / Note / Sequence component families;
- prohibit both filler items added merely to reach a sample count and destructive merging done merely to reduce to it;
- add focused adaptive-composition regression coverage proving non-sample counts render and mechanically validate through the same Golden component grammar.

## Package 1.15.0 — 2026-09-07

Model-readiness and semantic-quality improvement for stronger reasoning models while preserving the current Golden renderer/output contract.

### Semantic production quality

- add integrated provisional cross-role synthesis in Flow 2 before the Simple Chat Preview;
- distinguish routine reversible AI craft decisions from material project Proposals;
- add progressive context expansion for real cross-cutting dependencies;
- add explicit Flow 4 semantic reconciliation across approved source/requirements → canonical content → render projection → visible PRD;
- strengthen semantic readiness around source fidelity, decision completeness, role actionability, quantitative/lifecycle coherence, and cross-role consistency;
- preserve Material Conservation as a separate omission gate without numeric semantic scorecards.

### Verification quality

- make PRD CI discover every canonical `tests/test_prd_*.py` contract module automatically.

## Repository v0.1 — 2026-08-30

First stable repository baseline of the professionalized PRD-Creator workflow.

### Repository professionalization

- establish the three-tier `develop → Local → main` promotion model;
- isolate active repository development from the verified `Local` baseline;
- prevent live project-package subdirectories from being tracked in the public system repository;
- add explicit project-data/security guidance;
- add Local integration and stable main promotion gates;
- add CODEOWNERS and a pull-request template;
- remove renderer module-global mutation while preserving Golden rendering behavior;
- simplify the public README/front-door orientation.

Repository release `v0.1` does not change the PRD-Creator product/package contract version.

## Package 1.14.0

Previous package baseline before the later reasoning-quality, adaptive-composition, and source-code hardening releases. Earlier contract history remains recoverable from durable decisions, audits, package owners, and Git history.