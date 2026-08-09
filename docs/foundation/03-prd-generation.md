# Flow 3 — Project Document / PRD Generation

Status: active durable policy

## Purpose

Turn a Flow 2 project state marked `ready_for_prd` into practical canonical PRD content and a deterministic HTML presentation without reintroducing the Archived builder's process ceremony.

## Authority chain

```text
Original Source + Approved Decisions
            ↓
Requirement Register / ready_for_prd
            ↓
work/content.md
            ↓
work/render-data.json
            ↓
Approved HTML Template Shell
            ↓
output/final.html
```

Authority decreases downstream. Rendering cannot introduce new project meaning.

## Canonical content

`work/content.md` is the human-readable PRD source of truth for Flow 3.

Use `kits/project-document-generator/CONTENT-CONTRACT.md` for required content shape. The current gameplay-production family follows:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

Page count and package count follow the project, not the Golden Sample.

## Rendering projection

`work/render-data.json` is a disposable/derived structured projection used to render dynamic navigation and package pages. It must not contain facts absent from `content.md`.

The active renderer intentionally does not use the Archived builder's JSON Schema stack or Content Freeze machinery. It performs only structural safety checks required to render reliably.

## Template adaptation

The active renderer:

- clones `template/approved-document.html`;
- preserves shared head/CSS/JS/controls/sidebar shell/responsive/print behavior;
- replaces project brand/metadata;
- regenerates sidebar navigation from current flow/global/package data;
- replaces `.document-main` project pages using the approved component vocabulary;
- replaces project glossary data used by the inherited tooltip system;
- uses a project-specific local-storage namespace.

It does not redesign the template.

## Adopted from the Archived builder

Retained because they materially improve output quality:

- context before detail;
- explicit critical production data;
- Gameplay Overview → Level Design → Developer package separation;
- scoring vs completion-data distinction;
- renderer must never change approved meaning;
- dynamic hierarchy/navigation rather than hand-editing every objective;
- stable bilingual text support and inherited glossary interactions.

Not adopted by default:

- schema registry and broad validator suite;
- mandatory Guided Discussion rounds;
- section-by-section Content Freeze ceremony;
- generic multi-profile infrastructure;
- release/ZIP/render-report/checksum packaging;
- exact Golden regression as a gate for every project render.

Those remain Archived unless a future concrete need proves otherwise.

## Flow 3 completion

Flow 3 completes when:

- Flow 2 is `ready_for_prd`;
- canonical `content.md` satisfies the content contract;
- derived render data passes structural renderer checks;
- `output/final.html` is generated through the approved shell;
- generated navigation resolves to generated pages;
- no required placeholder remains.

This does **not** mean the PRD has passed development-readiness/team-handoff acceptance. Flow 4 owns that decision.
