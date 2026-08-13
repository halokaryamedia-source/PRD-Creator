# Voice Production DOCX Format

`output/Voice Production.docx` is an **optional derived export** built from `work/voice-production.md`.

The canonical Markdown owns wording/cast. The default human-facing production surface is now `output/final.html → Production Assets → Voice`. DOCX exists only when a portable document is explicitly requested or materially useful.

## Approved reference

Audited source benchmark: original Voice Production Kit v1.0.0 `Voice Production.docx` (not duplicated into the active repository binary).

Reference SHA-256:

`c76ce2562ee1839ae9174373f510b26da09e7b05f90e43a3e1de820633c34020`

The reference demonstrates hierarchy, spacing, script-panel treatment, type labels, duration labels, and readable performance notation. It does not define project-specific Voice counts/content and does not override the consolidated project HTML presentation.

## Visible export contract

When DOCX is produced:

```text
Cover
  Project Voice Production
  Version

Section
  <Gameplay Section>

Entry
  TYPE · Speaker: <speaker>
  <VOICE-ID> - <Title>
  Estimated Duration: ...
  <Performance Script panel>
```

Keep the export compact. Do not add Flow 5 Trigger, Channel, Purpose, Must communicate, Must not add/repeat, source refs, WPM calculations, Performance Fill Map reasoning, QA commentary, or other internal state.

The consolidated HTML owns the simple Voice Cast display. DOCX does not need to become a second cast/settings database.

## Styling contract

The builder keeps the demonstrated reference style:

- Letter page size;
- compact margins;
- blue Aptos/Aptos Display hierarchy;
- section headings begin on a new page;
- Type and Speaker share the compact metadata row;
- title is prominent and dark;
- duration is small/gray/italic;
- Performance Script uses a monospaced font;
- standalone bracketed performance directions are blue italic;
- Main Story script panels use pale blue;
- Radio/other script panels use neutral light background;
- canonical line breaks are preserved.

## Builder

```bash
python kits/voice-production-kit/builder/build_docx.py \
  workspace/active/<project>/work/voice-production.md \
  workspace/active/<project>/output/Voice\ Production.docx \
  --requirements workspace/active/<project>/work/voice-requirements.md
```

The builder must not rewrite wording, infer a Speaker, choose actor voices, or invent duration/tags.

It validates required Markdown structure, unique Voice IDs, Type/Speaker/Estimated Duration/performance presence, unresolved placeholders, and Flow 5 Voice ID/Type/Speaker parity when requirements are supplied.

The optional `Voice Cast:` header is ignored by the DOCX entry parser because actor selection is shown once in the consolidated HTML rather than repeated throughout this export.

## Visual QA

Only claim DOCX visual readiness when the export actually exists and has been rendered/inspected.

Check clipping, Type/Speaker association, hierarchy, script-panel readability, line breaks, glyphs, spacing, shading, and pagination.

A DOCX defect is fixed in canonical source or builder and regenerated. Never patch the DOCX as source truth.

## Boundary

No DOCX is required for normal Voice Preparation/Delivery when the consolidated project HTML is current and accepted for the requested non-audio scope.
