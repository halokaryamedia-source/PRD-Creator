# Source Authority

Use this note only when source/authority routing is unclear. Detailed Flow 2 behavior lives in `kits/project-document-generator/SOURCE-INTAKE.md`.

## Repository routing

| Need | Current owner |
|---|---|
| Agent behavior / work modes / proof | `AGENTS.md` |
| Stable product context | `CONTEXT.md` |
| Active continuation | `docs/knowledge/next-action.md` |
| Durable production policy | `docs/foundation/` |
| PRD production behavior | `kits/project-document-generator/` + relevant proof |
| Voice production behavior | `kits/voice-production-kit/` + relevant proof |
| Project-specific meaning | `workspace/active/<project>/` current source/state/canonical work |
| Historical evidence meaning | `docs/knowledge/reviews/README.md` |

## Project authority chain

Use the most upstream valid owner:

```text
current user instruction
→ approved project decisions
→ authoritative project source
→ requirement register / intake state
→ accepted canonical PRD
→ accepted Voice Requirements
→ canonical Voice Production wording
→ derived HTML/DOCX/audio/evidence
```

Derived artifacts do not repair or outrank upstream meaning.

## Material user instructions

A material user instruction is authoritative even when it arrives only in chat. Persist it as a non-file `SRC-###` entry with a concise summary instead of leaving chat history as the only durable evidence or creating a fake file.

Do not create one source entry per sentence; group one coherent material instruction/decision set when practical.

## Partial supersession

Use source-level `superseded` only when the whole source is replaced. If a later instruction changes only one claim/section, keep the original source available and resolve the affected requirement at claim level using current provenance/resolution.

Never use file date or polish to silently select a winner.

## Flow 2–4 project sources

- originals/provenance/inspection coverage → source inventory;
- explicit + recovered requirements/exclusions/topology/terminology → requirement register;
- intake readiness → intake state;
- canonical project meaning → `work/content.md`;
- derived render data/HTML → never project authority;
- acceptance/handoff → Flow 4 owner.

## Reference / Golden Samples

References can establish demonstrated presentation, structure, tone, or quality only within their recorded contract. They cannot by themselves establish current project facts, objective count, mechanics/scoring, quantities, speaker/Voice rules, or current-project correctness.

## Conflict rule

If material authorities conflict and precedence does not resolve them safely:

```text
UNKNOWN
→ identify both claims
→ identify affected requirement/output
→ resolve explicitly
```

Never choose silently because one source is newer-looking or more polished.
