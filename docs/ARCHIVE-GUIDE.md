# Archive Guide

## What Must Be Preserved Together

The following items form one working Skill and should not be separated:

- `SKILL.md`
- `references/`
- `schemas/`
- `scripts/`
- `templates/`
- `golden-sample/`
- `tests/`
- `requirements.txt`
- `manifest.yaml`

## Canonical Visual Source

`golden-sample/aftershock-golden-sample-v1.0.html`

SHA-256: `6af765b1c40100728b126fe219c88e5f0f734816f6c9a596d1cd90292c380901`

Do not replace this file with a generic rendered fixture. A changed hash means
the Golden Sample is no longer the approved locked artifact.

## Backup Recommendation

Store the ZIP and its `.sha256` file together. After copying or uploading it,
verify the archive with:

```bash
sha256sum -c production-document-builder-v0.2.0.zip.sha256
```

On Windows PowerShell:

```powershell
Get-FileHash .\production-document-builder-v0.2.0.zip -Algorithm SHA256
```
