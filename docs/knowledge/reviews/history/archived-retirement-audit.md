# Final Retirement Audit — Production Document Builder v0.2.0

Status: `SAFE_TO_DELETE`
Audit date: 2026-08-10
Archived package reviewed: `Production Document Builder/`
Inventory baseline: 120 files

## Decision

The live `Production Document Builder/` tree is no longer required by the active PRD + Voice Production system and is safe to remove from `Local`.

This decision is based on two gates:

1. the replacement Flow 2→7 pipeline has been exercised end-to-end on the real **The Clockwork Vault** project, including a real defect → root fix → rebuild → revalidation cycle;
2. every material capability/category in the Archived 120-file package is mapped below to either an active owner or an explicit retirement decision.

Deletion removes the live duplicate/obsolete tree only. Git history remains the historical recovery mechanism if forensic comparison is ever needed.

## Inventory Evidence

Archived package inventory reports:

- 120 total files;
- JSON schemas, YAML project state/examples, modular templates, renderer/validator scripts, tests/fixtures, package manifests/checksums, and the Aftershock Golden Sample;
- Golden Sample SHA-256 `6af765b1c40100728b126fe219c88e5f0f734816f6c9a596d1cd90292c380901`.

The archived Golden HTML and active `kits/project-document-generator/template/approved-document.html` share the exact same Git blob SHA:

`e1dccd77d7a5335213caea7a09d74ba78b2ae8e1`

Therefore deleting the Archived Golden copy does not remove the approved presentation authority.

## Capability Mapping

| Archived category | Archived behavior/assets | Current owner / decision | Retirement result |
|---|---|---|---|
| Boot / workflow / continuation | 12-phase Intake → Discussion → Freeze → Delivery workflow; one active flow; resume state | Root `AGENTS.md`, `CONTEXT.md`, `next-action.md`, canonical Flow 1–7 architecture | **Migrated**, with heavy ceremony intentionally reduced |
| Source audit / provenance | source classification, conflict visibility, do-not-reask known facts | Flow 2 `SOURCE-INTAKE.md`, Source Inventory, Requirement Register, Intake State | **Migrated** |
| Decision / assumption / project state | decision-log YAML, assumptions YAML, project-state YAML, section/freeze statuses | requirement state + approved decisions + concise per-flow state files; repository continuity owners | **Migrated in simpler form**; old generalized state schema intentionally retired |
| Content contract | context-first hierarchy, critical data, Gameplay / Level Design / Developer separation, scoring/completion distinction | Flow 3 `CONTENT-CONTRACT.md` | **Migrated** |
| Multi-perspective audit | New Reader, Level Designer, Developer, consistency; Critical/Major/Minor | Flow 4 `VALIDATION.md` and Flow 7 `VOICE-VALIDATION.md` | **Migrated** |
| Golden Sample | locked Aftershock HTML and exact-regression reference | Active approved template is byte/Git-blob identical; Golden use rules remain active | **Migrated; archived duplicate redundant** |
| Semantic HTML renderer | modular renderer, sidebar/page/component generation | Active shell-preserving renderer under `kits/project-document-generator/renderer/` | **Replaced** |
| Modular template fragments/CSS/JS | separate base/component/style/script files | Approved HTML shell is the active presentation authority; project rendering reuses its component vocabulary | **Intentionally retired as a parallel presentation system** |
| JSON Schema stack | project-state/content/scoring/completion/glossary/render-report schemas | current renderer + PRD validator + Voice builder/validator enforce concrete invariants actually used by the active pipeline | **Intentionally retired**; no active runtime dependency |
| Document Profiles | complete map, multi-stage, single gameplay, module, specialized profiles | active product currently uses the approved gameplay-production document family; materially different document families are treated as a new scoped decision instead of prebuilding a generic profile framework | **Intentionally retired** |
| Examples / profile fixtures | complete-game-map and multi-stage YAML examples | active contracts + synthetic tests + real The Clockwork Vault proof | **Retired**; fixtures validate the old profile/schema model |
| Golden/schema/profile tests | 27 schema cases, 11 renderer/profile cases, exact Golden regression | exact active template identity is directly preserved; active validators plus synthetic proof plus real end-to-end proof cover current contracts | **Retired with old architecture** |
| Browser/HTML audit automation | Playwright responsive/translation/print/browser validation | not an active runtime dependency; current Flow 4 separates mechanical/semantic acceptance and records browser evidence honestly. The old tool is coupled to retired Frozen/schema/render-report pipeline. If future real HTML defects require browser automation, implement it against the active renderer rather than resurrecting v0.2.0. | **Intentionally retired**, evidence-driven replacement only if future need appears |
| ZIP / render report / checksums / manifest | delivery ZIP, render report, package hashes, manifest validation | active workflow produces only requested deliverables/evidence and relies on Git/repository state for history | **Intentionally retired as unnecessary packaging ceremony** |
| `.pyc`, logs, historical result JSON | cached/generated test evidence | no active authority or runtime need | **Delete** |
| Archived install dependencies | PyYAML, jsonschema, BeautifulSoup, Playwright | no active tool imports this archived dependency bundle; active Voice kit separately owns `python-docx` | **Delete** |

## Real-Project Proof Comparison

The Archived package's own `REAL-PROJECT-TRIAL-STATUS.md` says its DAIGON Circuit trial stopped after Intake/Source Audit and did not complete user-experience validation.

The replacement system has stronger current evidence:

- real Flow 2 source intake/recovery;
- real Flow 3 generation;
- real Flow 4 handoff acceptance;
- real Flow 5 requirement extraction;
- real Flow 6 performance/DOCX production;
- real Flow 7 delivery validation;
- real visual defect found after mechanical PASS;
- root builder fix;
- rebuild + all-page reinspection + mechanical revalidation.

Canonical evidence: `docs/knowledge/operations/system-integration-proof.md`.

## Remaining-Risk Review

### `INT-001` — Area Size presentation

The active renderer currently preserves Area Size inside Build & Visual rather than in a dedicated column. This is non-blocking and no source meaning is lost. It does not justify retaining the Archived renderer/template stack.

### HTML browser automation

The current container cannot provide reliable headless Chromium/DBus execution, so current project browser visual proof is explicitly unclaimed. Keeping an obsolete browser validator tied to retired schemas does not solve that environment constraint. Future browser QA should be implemented against current owners only if a real project demonstrates the need.

### Historical recovery

Deleting the live folder does not erase Git history. The old package can still be inspected from pre-retirement commits if a future forensic comparison is genuinely needed.

## Dependency Conclusion

No active kit, state owner, renderer, validator, Voice builder, or production flow requires a file under `Production Document Builder/`.

All useful behavior is either:

- **migrated** into current Flow 1–7 owners; or
- **intentionally retired** because it belongs to the old generalized/schema/freeze/packaging architecture and is not part of the current product contract.

There is no remaining blocker that justifies keeping the live Archived tree.

## Retirement Action

Approved action for this migration:

```text
remove Production Document Builder/ from Local
retain active Project Document Generator + Voice Production Kit
retain this retirement audit + System Integration Proof
use Git history for any future forensic access to v0.2.0
```

After deletion, do not recreate the old package as a compatibility layer. If a future project exposes a missing capability, add the smallest evidence-backed behavior to the appropriate active owner.
