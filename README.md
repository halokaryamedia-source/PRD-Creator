# Skill Development

Repository untuk mendokumentasikan, mengembangkan, menguji, dan mengarsipkan reusable ChatGPT Skills milik Halo Karya Media.

## Available Skills

### Production Document Builder

Production Document Builder membantu mengubah source document yang belum lengkap menjadi production document terstruktur melalui workflow berikut:

```text
Project Intake
→ Source Audit
→ Guided Discussion
→ Decision Consolidation
→ Structured Content Draft
→ Multi-Perspective Content Audit
→ Consistency Audit
→ User Approval
→ Content Freeze
→ HTML Generation
→ Final HTML Audit
→ Delivery
```

Source lengkap tersedia di [`skills/production-document-builder`](skills/production-document-builder).

ZIP yang siap di-upload langsung ke ChatGPT tersedia di:

[`releases/production-document-builder-chatgpt-skill-v0.2.0.zip`](releases/production-document-builder-chatgpt-skill-v0.2.0.zip)

## Current Release

| Item | Status |
|---|---|
| Skill version | `v0.2.0` |
| Golden Sample | AFTERSHOCK V1.8 / Golden Sample v1.0 |
| Schema tests | 27/27 passed |
| Renderer tests | 11/11 passed |
| Golden Sample exact regression | Passed |
| End-to-end acceptance | Passed |
| Real-project trial | Postponed |

## Repository Structure

```text
Skill-Development/
├── README.md
├── CONTRIBUTING.md
├── docs/
│   └── REPOSITORY-GUIDE.md
├── releases/
│   ├── production-document-builder-chatgpt-skill-v0.2.0.zip
│   └── production-document-builder-chatgpt-skill-v0.2.0.zip.sha256
└── skills/
    └── production-document-builder/
        ├── SKILL.md
        ├── references/
        ├── schemas/
        ├── templates/
        ├── golden-sample/
        ├── scripts/
        ├── tests/
        ├── examples/
        └── docs/
```

## Installation

1. Download the release ZIP from `releases/`.
2. Open Skills in ChatGPT.
3. Choose Create or New Skill.
4. Upload the ZIP without extracting it.
5. Review the scanned contents and install it.

## Verification

From the `releases` directory:

```bash
sha256sum -c production-document-builder-chatgpt-skill-v0.2.0.zip.sha256
```

## Maintenance Rules

- Do not replace the approved Golden Sample without a deliberate version update.
- A generated document may only be called Golden Sample-compatible after exact regression passes.
- Product decisions, schema changes, template changes, and generated HTML use separate version tracks.
- Update source files and tests rather than patching generated HTML manually.

See [`skills/production-document-builder/OPEN-FIRST.md`](skills/production-document-builder/OPEN-FIRST.md) and [`skills/production-document-builder/ACCEPTANCE-REPORT.md`](skills/production-document-builder/ACCEPTANCE-REPORT.md) for operational details.
