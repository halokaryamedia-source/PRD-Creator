# Canonical Production Flow

Status: active architecture

```text
Flow 1  Repository Boot & Project Memory
Flow 2  Source Intake, Project Completion & Preview Approval
Flow 3  Project Document / PRD Generation
Flow 4  PRD Validation & Team Handoff
Flow 5  Voice Requirement Extraction
Flow 6  ElevenLabs Performance Script Production
Flow 7  Voice Validation & Delivery
```

There is no canonical Flow 8. The Simple Chat Preview is the final user-facing checkpoint inside Flow 2.

## End-to-end authority and revision chain

```text
current instruction + approved decisions + source evidence
→ source-inventory.yaml
→ requirement-register.yaml
→ Simple Chat Preview
→ approved_requirement_sha256
→ work/content.md
→ render-data.canonical_content_sha256
→ strict render-data projection
→ deterministic PRD core
→ work/asset-requirements.md when required
→ exact render-data + asset-requirements acceptance
→ development_ready | handoff_ready
→ Flow 5 only from handoff_ready
→ work/voice-requirements.md + stable Owner/Moment/VO identity
→ work/voice-production.md + exact Voice Requirements SHA
→ consolidated project HTML + exact Voice source SHA metadata
→ work/voice-acceptance.md + exact Voice Production SHA
→ voice_delivery_ready
```

Authority decreases downstream. Generated HTML/delivery may represent canonical meaning but never become source truth.

## Flow ownership

- **Flow 1** — recover current repository/project continuity without asking the user to reconstruct known state.
- **Flow 2** — inspect current evidence, recover material requirements/provenance, complete material gaps/conflicts through evidence-backed Completion or explicit Proposal, propagate one coherent cross-role model including real 04 needs, show one compact Simple Chat Preview, then bind approval to the exact approved requirement-register revision.
- **Flow 3** — author canonical `work/content.md`, derive one strict render-data projection bound to those exact content bytes, and render the approved 01–03 design grammar without adding project meaning.
- **Flow 4** — validate Flow 2 approval freshness, content→projection fidelity, deterministic HTML, required non-Voice 04, semantic readiness, Material Conservation, and exact-byte acceptance. `development_ready` accepts implementation meaning; only `handoff_ready` may enter Flow 5.
- **Flow 5** — derive only justified player-facing Voice requirements from the current accepted handoff. Flow 5 owns Voice scope/context and stable Owner/Moment identity; it does not write final performance wording.
- **Flow 6** — preserve Flow 5 identity/scope while producing canonical Eleven v3 wording/performance. The production source binds the exact current Voice Requirements bytes.
- **Flow 7** — validate revision identity, requirement→production parity, consolidated HTML freshness, communication/readiness evidence, and final exact Voice Production acceptance. Audio quality is separate evidence and is reviewed only when actual audio is in scope.

## 04 Production Assets boundary

04 is a normal PRD-Creator capability, not a separate numbered Flow.

```text
approved Flow 2 project model
├─ PRD core 01–03 meaning
└─ concrete Production Asset needs
```

When non-Voice assets are required:

```text
Flow 2 approved model
→ Flow 3 content + projection + PRD core
→ materialize work/asset-requirements.md from the same approved model
→ Flow 4 validates/accepts PRD + 04 together
```

Do not use generated 01–03 as a brainstorming source for new 04 scope. Resource meaning must already follow from the approved project model.

Machine identity for 04 is:

```text
Owner ID
→ Moment ID
→ AST-... / VO-... resource ID
```

Display titles are presentation, never primary machine identity.

## Proposal boundary

Flow 2 may choose concrete project-consistent defaults when evidence does not settle a material question, but those choices remain Proposals until represented in the preview and approved/corrected by the user.

Routine reversible wording/grouping/decomposition is authoring craft and does not create approval ceremony.

Golden/reference material supplies representation questions/grammar only. It never supplies another project's gameplay facts, counts, lore, timings, assets, or implementation details.

## Revision rule

A version number alone never proves freshness.

Current machine transitions are bound by exact source bytes where stale reuse would be unsafe:

```text
requirement approval  → requirement-register SHA
projection            → content.md SHA
Flow 4 acceptance     → render-data + asset-requirements SHA
Flow 6 source         → voice-requirements SHA
Flow 7 acceptance     → voice-production SHA
```

If bound upstream bytes change, downstream approval/acceptance becomes stale even when the semantic version string is unchanged.

## First-wrong-owner rule

```text
wrong project fact / scope
→ Flow 2 / PRD authority

correct meaning + invalid projection
→ Flow 3 projection owner

correct PRD + wrong non-Voice resource contract/presentation
→ 04 owner

wrong Voice scope/context/Owner/Moment identity
→ Flow 5

correct Voice requirement + weak wording/performance
→ Flow 6

correct canonical sources + stale/wrong derived HTML/delivery
→ renderer/delivery owner

actual generated-audio-only defect
→ audio evidence/generation scope
```

Fix the earliest owner that is actually wrong. Do not use downstream polish or compatibility fallback to hide upstream drift.

Detailed policy/procedure lives in the matching `docs/foundation/`, `kits/prd-creator/`, and shared machine-contract owner. This file owns only the canonical sequence.
