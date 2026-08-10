# Project Production Workspace

A repository-first production workspace for turning incomplete project direction into development-ready project documentation, then deriving validated ElevenLabs-ready Voice Production deliverables.

The repository is project memory. Chat history is supporting context, not the authority for current state.

## Branch Model

- `Local` — permanent working/development authority.
- `main` — stable baseline; change only when explicitly requested.
- routine per-flow branches/PRs are not used.

## Production Flow

```text
Flow 1 — Repository Boot & Project Memory             ✓ implemented
    ↓
Flow 2 — Source Intake & Requirement Recovery         ✓ implemented
    ↓
Flow 3 — Project Document / PRD Generation            ✓ implemented
    ↓
Flow 4 — PRD Validation & Team Handoff                ✓ implemented
    ↓
Flow 5 — Voice Requirement Extraction                 ✓ implemented
    ↓
Flow 6 — ElevenLabs Performance Script Production     ✓ implemented
    ↓
Flow 7 — Voice Validation & Delivery                  ✓ implemented
```

Project Document Generator owns Flow 2–4 under `kits/project-document-generator/`.

Voice Production Kit owns Flow 5–7 under `kits/voice-production-kit/`: accepted PRD → traceable voice requirements → canonical performance script → derived `Voice Production.docx` → final script/DOCX acceptance.

The replacement Flow 2–7 pipeline has now passed one real-project integration proof using **The Clockwork Vault**. `Production Document Builder/` remains **Archived** and non-authoritative until the final retirement audit confirms that no useful dependency still requires it.

## Mandatory Session Boot

1. read `AGENTS.md`;
2. read `CONTEXT.md`;
3. read `docs/knowledge/next-action.md`;
4. open only the relevant foundation/kit/project owner.

## Repository Map

- `AGENTS.md` — repository-wide rules, branch policy, authority, proof, anti-slop baseline.
- `CONTEXT.md` — stable purpose, terminology, boundaries.
- `docs/foundation/` — durable production policy.
- `docs/knowledge/` — current state, decisions, navigation, ownership, backlog.
- `kits/project-document-generator/` — PRD intake/generation/validation.
- `kits/voice-production-kit/` — Voice extraction/script/DOCX/final acceptance.
- `workspace/active/` — active project packages.
- `workspace/saved/` — retained project packages.
- `Production Document Builder/` — Archived historical reference.

## Core Rule

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance ≠ Voice Requirements ≠ Voice Production Script ≠ DOCX ≠ Voice Acceptance ≠ Audio
```

Generated artifacts and successful tooling never silently become higher authority than the canonical work/evidence that produced them.

## Current Proof State

`docs/knowledge/operations/system-integration-proof.md` records the first full real-project Flow 2→7 run, including a real DOCX builder defect, root-owner fix, rebuild, and revalidation cycle. The next active boundary is the final Archived-package retirement audit.
