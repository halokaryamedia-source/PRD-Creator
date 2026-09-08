# PRD-Creator Context

Status: active production system  
Development branch: `develop`  
Verified integration baseline: `Local`  
Stable branch: `main`

PRD-Creator converts uneven project discussion/source material into one approved project model, development-ready PRD documentation, bounded Production Assets, and optional downstream Voice Production.

## Production model

Human-facing PRD structure:

```text
01 Overview
02 Gameplay Flow
03 Development
04 Production Assets
```

Canonical production sequence:

```text
Flow 1  Repository Boot & Project Memory
Flow 2  Source Intake & Requirement Recovery
Flow 3  Project Document / PRD Generation
Flow 4  PRD Validation & Team Handoff
Flow 5  Voice Requirement Extraction
Flow 6  Eleven v3 Performance Script Production
Flow 7  Voice Validation & Delivery
```

There is no canonical Flow 8. Non-Voice `04 Production Assets` is a bounded capability of the same PRD-Creator package. Voice begins only from accepted upstream PRD meaning.

## Authority shape

```text
current user instruction
+ approved decisions
+ authoritative project source
→ approved project model
   ├─ canonical PRD core 01–03
   └─ justified non-Voice 04 requirements
→ accepted PRD / handoff
→ optional Voice requirements
→ canonical Voice Production
→ derived HTML / context / evidence
```

Authority decreases downstream. Generated artifacts never repair or outrank canonical source. If a downstream step exposes missing upstream meaning, reopen only the affected owner.

## Branch model

```text
develop → active repository Development
Local   → verified integration baseline; one squash commit per approved update
main    → stable repository history
```

`develop → Local` requires Local Promotion Verify and squash. After promotion, synchronize `develop` to the resulting `Local` HEAD. `Local → main` requires explicit stable promotion and the Stable release gate. A stable main promotion is not automatically a versioned release; protected `v*` tags/releases are reserved for approved feature/capability changes.

## Product package

`kits/prd-creator/` owns Flow 2–7 plus bounded 04 execution:

```text
intake/             Flow 2 source + requirement recovery
document/           PRD meaning/design/Flow 4 acceptance
production-assets/  non-Voice 04 contract
voice/              Flow 5–7 Voice procedure/craft/evidence
shared/             strict machine schemas and shared primitives
renderer/           deterministic PRD + 04 rendering/delivery
validator/          PRD, HTML, handoff, and Voice mechanical gates
template/           one approved canonical Golden source
```

`shared/` centralizes machine behavior only; it does not become semantic authority. `template/golden-reference.html` is both approved Golden evidence and the default tracked runtime source; runtime preparation is derived temporarily through `TemplateAdapter`.

## Project-data boundary

The public repository owns the system, not live client/project production data. `workspace/active/` and `workspace/archive/` are ignored local/external mount conventions. Project packages may live locally or in another authorized location.

Do not commit credentials, private client material, live requirement state, or generated client output to this public repository without an explicit visibility decision.

## Golden boundary

The approved Golden artifact is binding for PRD-core representation until explicitly changed. It supplies structure/quality evidence only and never another project's gameplay facts, counts, timings, lore, scoring, speakers, or implementation decisions.

## Canonical output lifecycle

```text
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
        ↓
work/content.md
work/render-data.json
work/asset-requirements.md       # when required
        ↓
work/acceptance.md
state/handoff-state.yaml
        ↓
optional Voice work/state
        ↓
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

Generated output is replaceable projection; canonical state/work remains upstream.

## Repository map

```text
AGENTS.md            routing, authority, continuity, branch kernel
GITHUB_RULES.md      GitHub execution and repository mutation discipline
CONTEXT.md           this stable orientation
next-action.md       active continuation only
docs/foundation/     durable Flow policy
docs/knowledge/      decisions, ownership, evidence, historical context
.agents/skills/      reusable semantic judgment
kits/prd-creator/    product procedure + implementation
tests/ + tools/      deterministic verification/operator facade
.github/             CI and promotion gates
```

For a new Development session, read `docs/knowledge/next-action.md` after this file. For normal Production Execution, use the matching production skill and smallest project owner instead of broad-reading repository context.
