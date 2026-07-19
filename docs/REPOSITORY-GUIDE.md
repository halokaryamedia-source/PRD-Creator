# Repository Guide

## Purpose

This repository keeps the editable skill source, approved Golden Sample, automated validators, renderer, tests, and ready-to-upload ChatGPT release in one auditable location.

## Source of Truth

| Area | Source |
|---|---|
| Skill controller | `skills/production-document-builder/SKILL.md` |
| Workflow phases | `references/workflow.md` |
| Document profiles | `references/document-profiles.md` |
| Discussion behavior | `references/discussion-guide.md` |
| Project state | `references/project-state-guide.md` |
| Content contracts | `references/content-contract.md` |
| Content audit | `references/audit-guide.md` |
| HTML rendering | `references/rendering-guide.md` |
| Error handling | `references/error-handling.md` |
| Structured validation | `schemas/` and `scripts/validate_package.py` |
| Approved visual benchmark | `golden-sample/aftershock-golden-sample-v1.0.html` |
| ChatGPT upload artifact | `releases/production-document-builder-chatgpt-skill-v0.2.0.zip` |

## Versioning

Track versions separately:

- Content Version
- Template Version
- Schema Version
- Golden Sample Version
- HTML Version
- Skill Release Version

## Release Procedure

1. Run schema and semantic tests.
2. Run renderer regression tests.
3. Run Golden Sample exact regression.
4. Run end-to-end acceptance tests.
5. Rebuild the ChatGPT-ready ZIP with `SKILL.md` at archive root.
6. Generate the SHA-256 file.
7. Update `CHANGELOG.md`, `VERSION`, and release documentation.
8. Commit source and release artifact together.
