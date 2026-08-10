# Voice Production DOCX Format

`output/Voice Production.docx` is a derived production artifact built from `work/voice-production.md`. The Markdown script owns wording; the DOCX owns presentation only.

## Approved reference

Audited source benchmark: original Voice Production Kit v1.0.0 `Voice Production.docx` (not duplicated into the active repository binary).

Reference SHA-256:

`c76ce2562ee1839ae9174373f510b26da09e7b05f90e43a3e1de820633c34020`

The reference demonstrates hierarchy, spacing, script-panel treatment, type labels, duration labels, and readable performance notation. It does not define project-specific voice counts or content.

## Document hierarchy

```text
Cover
  Project Voice Production
  Version
  ElevenLabs-ready performance scripts

Section
  01. <Gameplay Section>
  <actual voice types present>

Entry
  TYPE
  <VOICE-ID> - <Title>
  Estimated Duration: ...
  <shaded Performance Script panel>
```

Each entry exposed in the final DOCX contains only:

- Title (including its stable Voice ID);
- Estimated Duration;
- Performance Script.

The visible `TYPE` label is grouping/context, not an additional script field.

## Section subtitle

Do not claim a voice type that is absent. Derive the subtitle from the actual section content:

- `Main Story`
- `Radio Communication`
- `Main Story and Radio Communication`
- or the explicit supported types actually present.

## Reference styling contract

The builder reproduces the demonstrated reference style rather than copying project text:

- Letter page size;
- compact margins;
- blue Aptos/Aptos Display hierarchy;
- section headings begin on a new page;
- type labels are blue and uppercase;
- title is prominent and dark;
- duration is small, gray, and italic;
- Performance Script uses a monospaced font;
- bracketed performance directions are blue italic;
- Main Story script panels use a pale blue background;
- Radio/other script panels use a neutral light background;
- script panels have comfortable internal paragraph spacing.

## Builder

`builder/build_docx.py` is deterministic presentation tooling. It must not rewrite spoken wording or invent duration/tags.

The builder validates:

- required Markdown structure;
- unique Voice IDs;
- no visible unresolved placeholder;
- non-empty performance text;
- when `--requirements` is supplied, exact Voice ID parity and matching type against Flow 5 requirements.

If the builder exposes a content problem, fix `work/voice-production.md` or the upstream requirement. Do not patch the DOCX as the source of truth.

## Visual QA

For actual project production, DOCX generation is not considered visually verified until rendered to page images and inspected. Check:

- no clipped text;
- no orphaned labels separated from their title/script panel;
- readable section hierarchy;
- script panels remain legible across page breaks;
- line breaks reflect the canonical script;
- no missing glyphs;
- consistent spacing and shading.

Flow 6 may establish the builder with synthetic/reference tests, but Flow 7 owns final current-project voice delivery acceptance.
