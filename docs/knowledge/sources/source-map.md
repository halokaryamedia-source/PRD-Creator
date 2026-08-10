# Source Authority Map

Updated: 2026-08-10

Use this note to route a question or claim to its current authority. It links owners; it must not copy their full content or become a parallel source of truth.

## Repository Authority Routing

| Need | Current owner |
|---|---|
| Agent behavior, work modes, proof boundary | `AGENTS.md` |
| Stable product context / terminology | `CONTEXT.md` |
| Active task/status/next step | `docs/knowledge/next-action.md` |
| Durable production policy | `docs/foundation/` |
| Agent work-routing | `docs/knowledge/flow.md` |
| Root skill routing | `.agents/skills/` + `docs/knowledge/skills/` |
| Repository/module ownership | `docs/knowledge/modules/module-map.md` + `implementation-map.md` |
| Current PRD production behavior | `kits/project-document-generator/` source/procedure + relevant proof |
| Current Voice production behavior | `kits/voice-production-kit/` source/procedure + relevant proof |
| Project-specific material | `workspace/active/<project>/` current source/state/canonical work |
| Historical review/evidence meaning | `docs/knowledge/reviews/review-graph.md` |
| Historical retired implementation | Git history only |

## Project-Specific Authority Chain

For project meaning, use the most upstream valid owner:

```text
current user task intent
→ approved project decisions
→ authoritative project originals
→ requirement register / intake state
→ accepted canonical PRD
→ accepted Voice Requirements
→ canonical Voice Production wording
→ derived HTML/DOCX/audio/evidence
```

Derived artifacts do not repair or outrank an upstream owner.

## Flow-Specific Sources

### Flow 2–4

Start from the project package, then the smallest relevant owner:

- originals/provenance → `source/originals/` + source inventory;
- normalized requirements → requirement register / intake state;
- canonical project meaning → `work/content.md`;
- rendering rules → Project Document Generator renderer + `RENDERING.md`;
- acceptance/handoff → Flow 4 acceptance/handoff files + `VALIDATION.md`.

### Flow 5–7

- accepted upstream facts → current handoff-ready PRD;
- Voice scope → `work/voice-requirements.md`;
- final spoken wording → `work/voice-production.md`;
- DOCX → derived output only;
- final Voice evidence → `work/voice-acceptance.md` + `state/voice-state.yaml`;
- actual audio → evidence/delivery only when supplied.

## Reference / Golden Samples

A reference can establish demonstrated presentation, structure, tone, or performance quality only within its recorded contract.

It cannot by itself establish:

- current project facts;
- objective count;
- mechanics/scoring;
- Voice count/type;
- speaker/channel/trigger;
- current-project correctness.

## Historical Evidence

Reviews, old outputs, retired branches, and Git history explain lineage. They do not override current `Local` policy/source unless a new explicit decision reactivates them.

Use `docs/knowledge/reviews/review-graph.md` to understand whether an old review is active evidence, implemented, historical, superseded, or still awaiting proof.

## Conflict Rule

If two material authorities conflict and precedence does not resolve them safely:

```text
UNKNOWN
→ identify both claims
→ identify affected owner/output
→ resolve explicitly
```

Never choose silently because one source is newer-looking or more polished.

## Related

- [Module Map](../modules/module-map.md)
- [Implementation Map](../implementation-map.md)
- [Review Graph](../reviews/review-graph.md)
