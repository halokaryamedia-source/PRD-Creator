# Rendering Guide

## Golden Sample Contract

The approved AFTERSHOCK V1.8 file is locked as Golden Sample v1.0.

```text
AFTERSHOCK Golden Sample = visual, structural, navigation, and interaction benchmark
The Quarry Objective 1 = content-quality benchmark across all three package pages
```

The Golden Sample file must not be edited during normal project rendering.

## Two Rendering Paths

### 1. Golden Exact Regression

Used only to prove the approved Golden Sample can be reproduced unchanged. It
must validate the exact 30-page inventory and then pass byte-for-byte and SHA-256
comparison. No output may claim Golden parity without this evidence.

### 2. Semantic Project Rendering

Used for new schema-valid Frozen Structured Content. It uses the same Golden CSS,
component vocabulary, sidebar/control system, package hierarchy, bilingual
behavior, tooltip, Terms Used, responsive, and print rules. Text and page count
may differ because the project differs.

Generic fixtures are profile tests, not Golden parity artifacts.

## Render Gate

Requires Frozen Content, explicit approval, Critical/Major content findings=0,
blockers=0, scoring/completion/glossary/consistency validation passed, valid
profile, and available template/schema/Golden versions.

## Renderer Responsibilities

Build metadata, hierarchy, sidebar, pages, section tabs, EN/ID content, theme,
View Mode, glossary matching, global tooltip, Terms Used, responsive/print rules,
structural validation, HTML, ZIP, and render report.

The renderer must never change approved meaning, invent data, resolve open
questions, alter scoring, hide critical information, or redesign the template.

## Golden Component Contract

Use the established components and classes:

- document shell and sidebar
- Overview page
- storytelling Gameplay Flow page
- four Global Development pages
- package tabs
- Gameplay Overview information table
- Level Design flow and build requirements
- Developer flow, requirements, scoring/completion, reset, notes
- collapsible Terms Used
- global tooltip
- footer hierarchy and page codes

Create a new component only for a genuinely different reusable information
function, with impact review, template version update, and regression tests.

## Controls and Interactions

Preserve Theme and Language controls directly above View Mode; desktop sidebar
collapse; mobile drawer; EN/ID switch; Light/Dark mode; View Mode; hash navigation;
keyboard-accessible controls; global tooltip at body level; Terms Used closed by
default and independently toggleable.

## Glossary Rendering

Process longer terms before shorter terms, include approved aliases, avoid nested
markup, avoid scripts/styles/controls/definitions, render matched terms bold, and
use the active-language definition. On mobile use a viewport-safe panel.

## Responsive and Print

Audit desktop 16:9, laptop, tablet, mobile, 125% zoom, and 150% zoom. Prevent page
horizontal overflow; allow table wrappers to scroll when necessary. Print hides
controls/sidebar, expands Terms Used, avoids tooltip layers, preserves contrast,
and uses sensible breaks.

## Versioning

- Content Version: project meaning changes.
- Template Version: shared UI/behavior changes.
- Schema Version: structured field/validation changes.
- Golden Sample Version: official benchmark changes.
- HTML Version: a new rendered delivery is generated.

Project State stores values/history; this guide defines increment conditions.

## Final HTML Audit

1. Compare rendered content to Frozen Structured Content.
2. Verify profile hierarchy, sidebar, tabs, headers, footers, and reachability.
3. Compare typography, spacing, table density, controls, and page family to the Golden Sample.
4. Test interactions and keyboard behavior.
5. Test responsive and zoom viewports.
6. Test print behavior.

Critical examples: wrong/missing content, changed score/quantity, wrong navigation,
or language meaning mismatch. Major examples: widespread tooltip failure, clipped
tables, unusable sidebar, unreadable mode, broken mobile, or missing Terms Used.
Critical/Major block delivery.

## Fix Classification

- Content fix → update Structured Content and content version.
- Template fix → update shared template and template version.
- Renderer fix → update rendering logic and relevant tool/template version.

Never patch final HTML without updating its source of truth.

## Regression Requirements

Every release runs schema tests, profile renderer tests, Golden exact regression,
and an end-to-end pipeline test. Template/renderer changes must test Golden Sample
and at least one secondary profile.
