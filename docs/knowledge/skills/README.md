# Skill Catalog

Use this note for the **current root skill inventory and ownership boundary**. Historical consolidation rationale belongs in the linked decision/review records; do not replay it during normal routing.

## Canonical root skills

All repository-wide agent skills live under `.agents/skills/`:

| Skill | Function |
|---|---|
| `development-brief` | mandatory front door for non-trivial repository/system Development; grounds goal, authority, minimal scope, acceptance criteria and proof budget |
| `project-document-production` | reusable semantic/product-contract judgment for Flow 2–4 plus bounded non-Voice 04 completion |
| `voice-production` | reusable semantic/product-contract judgment for Flow 5–7 |

The canonical root set is intentionally small.

## Relationship to the unified production package

```text
root AGENTS / development-brief
→ decide work mode + semantic vs technical boundary
→ optional one root semantic specialist
→ kits/prd-creator/SKILL.md or AGENTS.md
→ smallest categorized domain / implementation owner
```

### Project / PRD domain

`project-document-production` owns reusable PRD/source/04/readiness **semantic judgment**.

`kits/prd-creator/SKILL.md` routes detailed normal Production Execution. `kits/prd-creator/AGENTS.md` owns module/file routing and pure technical Maintenance. Exact Flow contracts live in:

```text
kits/prd-creator/intake/SOURCE-INTAKE.md
kits/prd-creator/document/CONTENT-CONTRACT.md
kits/prd-creator/production-assets/CONTRACT.md
kits/prd-creator/renderer/CONTRACT.md
kits/prd-creator/document/VALIDATION.md
```

### Voice domain

`voice-production` owns reusable Voice **semantic judgment**.

The same unified root `SKILL.md` routes Flow 5–7 while exact Voice procedure/craft remains in:

```text
kits/prd-creator/voice/EXTRACTION.md
kits/prd-creator/voice/PERFORMANCE-WRITING.md
kits/prd-creator/voice/VALIDATION.md
```

Project/PRD and Voice are not merged semantically merely because they share one product package.

## Repository engineering is not a production skill

Shared engineering is owned directly by:

```text
requirements.lock.txt
tests/
tools/
.github/workflows/
```

Dependency, test, CI, and repository-invariant mechanics do not consume the single semantic specialist slot.

## Skill freeze rule

Do not add/rename/split a root skill because:

- another file format or programming language appears;
- another renderer/validator exists;
- another Production Asset type appears;
- a project has unique content;
- a one-off technical bug needs repair;
- a generic helper would be convenient.

Change the root skill set only when repeated work proves a distinct reusable semantic owner/procedure that existing root policy, foundation, `kits/prd-creator/` procedure/AGENTS, repository engineering, and current specialists cannot represent cleanly.

## Historical rationale

Current three-skill architecture and semantic-vs-technical separation are preserved in:

- `../decisions/technical-ownership-boundary.md`
- `../reviews/history/technical-ownership-refinement-audit.md`

Those records explain **why** the architecture exists. They are not required boot material.

## Related

- [Activation Matrix](activation-matrix.md)
- [Work Routing](../work-routing.md)
- [Repository Ownership](../ownership.md)
