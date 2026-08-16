# Source Authority

Use this note only when **source/state precedence for a claim is unclear**. Repository/file ownership lives in `ownership.md`; work-mode routing lives in root `AGENTS.md`.

Detailed Flow 2 source recovery behavior lives in `kits/project-document-generator/SOURCE-INTAKE.md`.

## Project authority chain

Use the most upstream valid owner:

```text
current explicit user instruction
→ approved project decisions
→ authoritative project source
→ normalized requirement state / approved project model
   ├─ accepted canonical PRD core 01–03
   └─ accepted non-Voice 04 Production Asset requirements when present
→ accepted Voice requirements
→ canonical Voice Production wording
→ derived HTML / optional DOCX / audio / evidence
```

Authority decreases downstream. Generated/derived artifacts do not repair or outrank upstream meaning.

Generated 01–03 is not the normal discovery authority for 04. PRD-core meaning and non-Voice 04 resource needs are separate canonical projections of the same approved project model.

## Material user instructions

A material user instruction is authoritative even when it arrives only in chat. Persist it in the existing project source/requirement model so future sessions do not depend on chat history alone.

Do not create a fake source file for a chat instruction. Do not create one source entry per sentence; group one coherent material instruction/decision set when practical.

## Source classes

Treat source material according to its actual role:

- **authoritative** — may establish current project facts within its scope;
- **approved decision/state** — resolves or supersedes project meaning within its scope;
- **supporting** — provides context/evidence but does not outrank authority;
- **reference/Golden** — demonstrates approved structure/quality only within its recorded contract;
- **generated/derived** — presentation/projection/evidence only, never upstream project authority.

A polished filename, newer-looking formatting, or generated output does not silently outrank higher authority.

## Partial supersession

Use source-level `superseded` only when the whole source is replaced. If a later instruction changes one claim/section, keep the original source available and resolve only the affected requirement/claim using current provenance/resolution.

Never discard unrelated valid meaning merely because one part changed.

## Flow 2–4 source/state roles

```text
originals / provenance / inspection coverage
→ source inventory

explicit + recovered requirements / exclusions / topology / terminology
→ requirement register / approved project model

intake readiness
→ intake state

canonical PRD-core meaning
→ work/content.md

canonical non-Voice 04 resource requirements when present
→ work/asset-requirements.md under PRODUCTION-ASSETS.md

render-data / HTML / AI side projections
→ derived only

acceptance / handoff
→ Flow 4 owners
```

## Voice source/state roles

```text
accepted project / PRD meaning
→ upstream project authority

work/voice-requirements.md
→ Voice scope / communication requirements

work/voice-production.md
→ canonical Voice production wording/performance

project HTML / optional DOCX
→ derived presentation

voice acceptance/state
→ readiness / continuation evidence
```

Downstream Voice work may not invent or silently repair missing project/gameplay truth.

## Reference / Golden boundary

References can establish demonstrated presentation, structure, tone, or quality only within their recorded contract. They cannot by themselves establish current project facts, objective count, mechanics/scoring, quantities, speaker rules, asset style/lore, or current-project correctness.

The approved PRD Golden is binding for the explicitly approved PRD-core representation contract, not for reference-project content.

## Conflict rule

If material authorities conflict and precedence does not resolve them safely:

```text
UNKNOWN
→ identify both claims
→ identify affected requirement/output
→ resolve through the correct current owner
```

Never choose silently because one source looks newer, more complete, or more polished.
