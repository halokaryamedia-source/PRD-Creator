# Project Workspace

This folder stores project-specific production packages. Reusable behavior belongs under `kits/prd-creator/`; durable workflow policy belongs under `docs/foundation/`.

## Lifecycle

```text
current project          → workspace/active/<project>/
inactive retained project → workspace/archive/<project>/
```

A project moves to `archive/` only when its active production status actually ends. Do not move projects merely to make the repository look smaller.

Project packages grow only when the current production stage needs an artifact. Do not pre-create a full folder tree.

### Selecting an active project

Multiple projects may remain in `workspace/active/` at the same time.

```text
user explicitly names project
→ use that project

current conversation clearly establishes one project
→ continue that project

multiple active projects + request is ambiguous
→ ask which project before changing project state
```

Do not infer project focus from directory order, filename order, commit recency, or whichever package was opened most recently by a tool.

### Approved preview exception

`approved_preview` is an intentional **pre-handoff** retained state, not a synonym for `development_ready` or `handoff_ready`.

Use it only when the user explicitly approves a preview-stage deliverable or an existing project state already records that exception.

- `state/intake-state.yaml` must explicitly record the preview status/approval and identify the retained preview artifact when one exists.
- A preview package may retain canonical `state/` + `work/` material and the approved preview artifact without the formal versioned `output/` bundle or `state/handoff-state.yaml`.
- Existing project-specific preview packages may also retain explicitly approved supporting production/Voice notes created for that preview. Those files do **not** establish formal Flow 5 handoff by themselves.
- `approved_preview` never authorizes Flow 5 automatically. Formal downstream Voice handoff requires the normal `handoff_ready` state.
- New projects should follow the normal lifecycle unless the user explicitly requests a preview-only milestone.
- When a preview is formalized, create the normal acceptance/handoff/versioned-delivery artifacts and remove the old preview artifact only after it is genuinely superseded.

## Canonical Project Artifacts

```text
Flow 2
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml

Flow 3 — PRD core 01–03
work/content.md
work/render-data.json

04 Production Assets, when justified
work/asset-requirements.md

Flow 4
work/acceptance.md
state/handoff-state.yaml

Voice, only when used after formal handoff
state/voice-state.yaml
work/voice-requirements.md
work/voice-production.md
work/voice-acceptance.md

Versioned delivery
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

The normal delivery command is:

```bash
python kits/prd-creator/renderer/delivery.py \
  workspace/active/<project>/
```

PRD mechanical validation uses `kits/prd-creator/validator/validate.py`. PRD → Voice handoff uses `kits/prd-creator/validator/validate_handoff.py` only at that boundary. Voice mechanical validation uses `kits/prd-creator/validator/validate_voice.py` only when Voice scope exists.

Exact PRD, Production Assets, renderer, and Voice contracts remain in their named owners under `kits/prd-creator/`; this workspace guide does not redefine their field schemas.

## Retention and Repository Hygiene

Keep files because they preserve current production truth, required evidence, or an intentionally retained deliverable, not because they once existed during processing.

### Keep

- canonical project state and work required to reproduce current accepted meaning;
- source/originals when direct future inspection materially benefits from retaining the bytes;
- the current versioned delivery;
- older delivery versions only when they are intentionally retained milestones or approvals;
- a project-specific approved preview before formal handoff only while current project state explicitly references it.

### Remove after they are superseded

- transfer fragments, base64 payload chunks, `.regen-transfer/`, temporary loaders, helper manifests, and upload-only files;
- generated preview/cache files with no current approval or reproduction value;
- duplicate approval-marker or review-summary files when canonical project state/work already preserves the accepted meaning;
- obsolete generated deliveries that are neither the current version nor an intentionally retained milestone.

Never remove canonical source/state or approval evidence merely to reduce repository size. Never rewrite history to hide old generated files; clean the current tree and let Git history remain history.

Large static originals may remain externally retained when `intake/SOURCE-INTAKE.md` allows it and current production meaning/provenance is safely persisted.

## Version Rule

`document.version` is project/release metadata, not an edit counter.

```text
document.version: 1.0.0
→ output/v1.0.0/
```

A downstream-only 04 or Voice presentation refresh may regenerate the current version when accepted PRD meaning did not enter a new declared revision.

## 04 Production Assets and Voice

Production Asset needs come from the same approved project model as PRD core 01–03. Do not rediscover them by brainstorming over generated HTML.

- non-Voice 04 contract → `kits/prd-creator/production-assets/CONTRACT.md`
- Voice extraction/craft/validation → `kits/prd-creator/voice/`
- consolidated presentation → `kits/prd-creator/renderer/CONTRACT.md`

Voice stays canonical in its Voice project files and is not duplicated into `asset-requirements.md`.

When non-Voice 04 is required for the current project, materialize it before Flow 4 acceptance so PRD and 04 readiness are reviewed together. Flow 5 begins only from a formal `handoff_ready` PRD state.

## Authority Rule

```text
source evidence + current user instruction + approved decisions
→ approved project model
   ├─ canonical PRD core
   └─ optional non-Voice 04 requirements
→ PRD/04 acceptance
→ optional Voice requirements + canonical Voice Production
→ versioned derived delivery
```

Derived delivery may be regenerated. Never patch `prd.html`, `context.md`, or `index.json` as source truth; fix the canonical owner and regenerate only the invalidated projection.
