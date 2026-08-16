# Skill Catalog

Use this note for the **current root skill inventory and ownership boundary**. Historical consolidation rationale belongs in the linked decision/review records; do not replay it during normal routing.

## Canonical root skills

All repository-wide agent skills live under `.agents/skills/`:

| Skill | Function |
|---|---|
| `development-brief` | mandatory front door for non-trivial repository/system Developing; grounds goal, authority, minimal scope, acceptance criteria and proof budget |
| `project-document-production` | reusable semantic/product-contract judgment for Flow 2–4 plus bounded non-Voice 04 completion |
| `voice-production` | reusable semantic/product-contract judgment for Flow 5–7 |

The canonical root set is intentionally small.

## Relationship to production kits

```text
root AGENTS / development-brief
→ decide work mode + semantic vs technical boundary
→ optional one root semantic specialist
→ nearest kit procedure / kit AGENTS
→ exact implementation/project owner
```

### Project Document Generator

`project-document-production` owns reusable PRD/source/04/readiness **semantic judgment**.

`kits/project-document-generator/SKILL.md` owns detailed normal Production Execution procedure. Kit `AGENTS.md` owns module/file routing and pure technical Maintenance. Exact Flow contracts remain in `SOURCE-INTAKE.md`, `CONTENT-CONTRACT.md`, `PRODUCTION-ASSETS.md`, `RENDERING.md`, and `VALIDATION.md`.

### Voice Production Kit

`voice-production` owns reusable Voice **semantic judgment**.

`kits/voice-production-kit/SKILL.md` owns detailed Flow 5–7 Production Execution procedure. Kit `AGENTS.md` owns module/file routing and pure technical Maintenance. Exact craft/validation contracts remain in `VOICE-EXTRACTION.md`, `SOUNDMAKER.md`, `VOICE-VALIDATION.md`, and related current owners.

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
- another renderer/validator/builder exists;
- another Production Asset type appears;
- a project has unique content;
- a one-off technical bug needs repair;
- a generic helper would be convenient.

Change the root skill set only when repeated work proves a distinct reusable semantic owner/procedure that existing root policy, foundation, kit procedure/AGENTS, repository engineering, and current specialists cannot represent cleanly.

## Historical rationale

Current three-skill architecture and semantic-vs-technical separation are preserved in:

- `../decisions/technical-ownership-boundary.md`
- `../reviews/technical-ownership-refinement-audit.md`

Those records explain **why** the architecture exists. They are not required boot material.

## Related

- [Activation Matrix](activation-matrix.md)
- [Work Routing](../work-routing.md)
- [Repository Ownership](../ownership.md)
