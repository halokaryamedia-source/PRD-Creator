# Voice Production DOCX Format

`output/Voice Production.docx` is a derived production artifact built from `work/voice-production.md`. The Markdown script owns wording; the DOCX owns presentation only.

## Approved reference

Audited source benchmark: original Voice Production Kit v1.0.0 `Voice Production.docx` (not duplicated into the active repository binary).

Reference SHA-256:

`c76ce2562ee1839ae9174373f510b26da09e7b05f90e43a3e1de820633c34020`

The reference demonstrates hierarchy, spacing, script-panel treatment, type labels, duration labels, and readable performance notation. It does not define project-specific voice counts or content.

## Visible operator contract

The DOCX is a compact production reference, not a duplicate of Voice Requirements.

```text
Cover
  Project Voice Production
  Version

Section
  01. <Gameplay Section>
  <actual Voice types present>

Entry
  TYPE · Speaker: <speaker>
  <VOICE-ID> - <Title>
  Estimated Duration: ...
  <Performance Script panel>
```

Every entry exposes only stable information the operator needs to identify and perform the line:

- Voice Type;
- exact Speaker;
- stable Voice ID + title;
- Estimated Duration;
- exact Performance Script.

Do not add Flow 5 planning metadata such as Trigger, Channel, Purpose, Must communicate, Must not add/repeat, source refs, WPM calculations, performance maps, voice-fit ratings, or QA commentary to the DOCX by default.

Generation settings such as selected commercial voice, Stability, Surface, or temporary UI controls remain operator/session context unless a concrete project requirement later justifies durable presentation.

## Section subtitle

Do not claim a Voice type that is absent. Derive the subtitle from actual section content:

- `Main Story`;
- `Radio Communication`;
- `Main Story and Radio Communication`;
- or the explicit supported types actually present.

## Reference styling contract

The builder reproduces the demonstrated reference style rather than copying project text:

- Letter page size;
- compact margins;
- blue Aptos/Aptos Display hierarchy;
- section headings begin on a new page;
- Type is blue/uppercase and Speaker shares the same compact metadata row;
- title is prominent and dark;
- duration is small, gray, and italic;
- Performance Script uses a monospaced font;
- standalone bracketed performance directions are blue italic;
- Main Story script panels use a pale blue background;
- Radio/other script panels use a neutral light background;
- script panels preserve canonical line breaks.

## Builder

`builder/build_docx.py` is deterministic presentation tooling. It must not rewrite spoken wording, infer a Speaker, or invent duration/tags.

The builder validates:

- required Markdown structure;
- unique Voice IDs;
- required Type, Speaker, Estimated Duration, and performance text;
- no visible unresolved placeholder;
- when `--requirements` is supplied, exact Voice ID parity plus matching Type **and Speaker** against Flow 5 requirements.

If the builder exposes a content problem, fix `work/voice-production.md` or the upstream requirement. Do not patch the DOCX as the source of truth.

## Visual QA

For actual project production, DOCX generation is not considered visually verified until rendered to page images and inspected.

Check:

- no clipped text;
- Type/Speaker metadata remains attached to the correct title/script;
- no orphaned labels;
- readable section hierarchy;
- script panels remain legible across page breaks;
- line breaks reflect the canonical script;
- no missing glyphs;
- consistent spacing and shading.

Flow 6 may establish the builder with synthetic/reference tests, but Flow 7 owns final current-project voice delivery acceptance.
