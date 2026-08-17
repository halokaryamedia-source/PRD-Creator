# Unified PRD Creator Kit — M3 Runtime Path Proof

Updated: 2026-08-17
Status: M3 complete; no executable code change required
Migration plan: `unified-prd-creator-kit-migration.md`
M0 inventory: `unified-prd-creator-kit-m0-inventory.md`
M1 candidate: `unified-prd-creator-kit-m1-candidate.md`
M2 root consolidation: `unified-prd-creator-kit-m2-root-consolidation.md`
Current Local baseline for this proof: `5212db728486fa2572ee9c170e4998f3c824afb4`
Executable candidate source: detached M2 commit `e1523e22f90a666ec14bf4f0d260bb9238305537`
Unified package subtree: `e56566a73ea9d2729f671411abae06d467206337`

## Purpose

M3 answers one narrow question before repository-wide routing is changed:

> Does the existing renderer/validator implementation require Python refactoring merely because it moves from the two historical kit roots into `kits/prd-creator/`?

Result: **no**.

The moved Python already resolves its local dependencies from sibling directories/files. The target package preserves that topology, so there is no justified compatibility wrapper, import framework, package shim, or relocation-specific Python patch to add.

## Actual candidate topology inspected

### Renderer entrypoint

Current candidate `renderer/render.py` resolves its own directory with:

```python
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _engine
import production_assets_objective as production_assets
```

Its default template is resolved relative to the new package root:

```python
default_template = HERE.parent / "template" / "runtime-template.html"
```

Therefore after relocation:

```text
kits/prd-creator/renderer/render.py
                     │
                     ├─ sibling _engine.py
                     ├─ sibling production_assets_objective.py
                     └─ ../template/runtime-template.html
```

No literal dependency on `kits/project-document-generator` is needed by this entrypoint.

### Renderer dependency chain

The moved renderer dependency chain remains local:

```text
renderer/_engine.py
→ adds renderer HERE to sys.path
→ imports sibling core.py + pages.py

renderer/pages.py
→ imports sibling core.py

renderer/production_assets.py
→ imports sibling core.py

renderer/production_assets_objective.py
→ imports sibling core.py
→ imports sibling production_assets.py
```

The target M2 subtree preserves all of these files inside the same `renderer/` directory.

### Delivery entrypoint

`renderer/delivery.py` imports the renderer lazily by adding its own `HERE` and importing sibling `render`:

```python
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import render as html_renderer
```

It also resolves the default template through:

```python
template = HERE.parent / "template" / "runtime-template.html"
```

The target layout preserves exactly that relationship.

### PRD validator

`validator/validate.py` resolves its own directory and imports sibling `_engine.py`:

```python
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import _engine
```

No relocation-specific edit is required.

### Handoff validator

`validator/validate_handoff.py` imports sibling `_engine` directly. Normal CLI execution with:

```text
python kits/prd-creator/validator/validate_handoff.py <project>
```

places the script directory on Python's import path, preserving the existing sibling import behavior.

No wrapper or import alias is justified.

### Voice validator

The moved Voice validator is now collision-safe at:

```text
kits/prd-creator/validator/validate_voice.py
```

It is standalone Python and has no dependency on the former `voice-production-kit` directory name. The rename is therefore sufficient; no internal Python change is required.

## Executable topology smoke proof

Because the container cannot resolve GitHub over the network, M3 did not substitute GitHub Actions as a remote shell. Instead, an isolated local topology smoke reproduced the exact directory relationships and import strategy used by the inspected candidate source:

```text
/tmp/prd-m3-smoke/kits/prd-creator/
├─ renderer/
│  ├─ core.py
│  ├─ pages.py
│  ├─ _engine.py
│  ├─ production_assets.py
│  ├─ production_assets_objective.py
│  ├─ render.py
│  └─ delivery.py
├─ validator/
│  ├─ _engine.py
│  ├─ validate.py
│  ├─ validate_handoff.py
│  └─ validate_voice.py
└─ template/
   └─ runtime-template.html
```

Proof executed:

```text
python -m compileall -q <smoke>/kits/prd-creator
python <smoke>/kits/prd-creator/renderer/render.py
python <smoke>/kits/prd-creator/renderer/delivery.py
python <smoke>/kits/prd-creator/validator/validate.py
python <smoke>/kits/prd-creator/validator/validate_handoff.py
python <smoke>/kits/prd-creator/validator/validate_voice.py
```

Observed output:

```text
render-import=PASS
render-template=<smoke>/kits/prd-creator/template/runtime-template.html

delivery-import=PASS
delivery-template=<smoke>/kits/prd-creator/template/runtime-template.html

prd-validator-import=PASS
handoff-validator-import=PASS
voice-validator-standalone=PASS
```

This smoke proves the relocation mechanics being changed by M3: sibling imports and `HERE.parent/template` resolution remain valid under the approved target directory shape.

## M3 decision

**NO EXECUTABLE CODE CHANGE REQUIRED.**

M3 therefore does not create a new renderer/validator blob or a compatibility layer. The executable portion of the unified package remains byte-identical to the M2 candidate.

M2 remains the executable construction baseline:

```text
candidate commit
 e1523e22f90a666ec14bf4f0d260bb9238305537

kits/prd-creator subtree
 e56566a73ea9d2729f671411abae06d467206337
```

Protected Golden/runtime blobs also remain unchanged:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

## Proof boundary

M3 proves **path/import/template-resolution viability**, not full product correctness.

The following are intentionally not claimed here:

- full PRD regression suite through new repository test constants;
- actual Clockwork mechanical PRD PASS through the final migrated repository;
- actual Clockwork handoff PASS through the final migrated repository;
- actual Clockwork Voice PASS through the final migrated repository;
- workflow path-filter correctness;
- repository verifier correctness after old-root retirement.

Those require M4/M5 final routing and are part of M6 full proof. M3 does not falsely claim them from a topology smoke.

## Preservation boundary

M3 changes no:

- Python implementation bytes;
- Golden/runtime bytes;
- PRD 01–03 semantics or presentation;
- Production Assets contract;
- Voice requirements, wording, performance, or evidence;
- Clockwork project files/output;
- tests/workflows/tools;
- current repository routing;
- old package roots.

## Recovery rule

If a session resumes after M3:

1. pin current `Local`;
2. read `next-action.md`, migration plan, M0, M1, M2, and this M3 note;
3. do not invent a Python relocation patch—the current M3 result is no code change required unless new source evidence contradicts it;
4. reuse M2 unified package subtree `e56566a73ea9d2729f671411abae06d467206337` as the package implementation baseline;
5. proceed to M4 repository routing synchronization;
6. keep both old package roots until M5.

## M4 entry contract

M4 owns current repository consumers of the package path, not renderer/validator behavior.

Synchronize live current references to `kits/prd-creator/`, including the necessary root/foundation/knowledge/semantic-skill/workspace routing, test path constants, PRD/Voice/Repository workflow filters/compile targets, and `tools/verify_repository.py` architecture invariants.

Also remove the currently observed stale DOCX wording from current-authority docs while preserving genuine historical evidence.

Do not retire the two old package roots until all live consumers are synchronized and the final candidate is internally coherent.