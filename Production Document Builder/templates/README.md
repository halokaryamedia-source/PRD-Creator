# Template Extraction v0.1

This directory contains a fidelity-first extraction from the locked AFTERSHOCK Golden Sample.

## Canonical Runtime Assets

- `styles/golden-sample.css` — exact combined CSS from the locked HTML.
- `scripts/document-controls.js` — navigation, language, theme, and View Mode runtime.
- `scripts/glossary-tooltip.js` — glossary matching and global tooltip runtime.
- `scripts/sidebar.js` — repaired desktop collapse and mobile drawer behavior.

## Semantic CSS Slices

`tokens.css`, `layout.css`, `components.css`, `themes.css`, `responsive.css`, and `print.css` are automatically classified slices for the next renderer-refactoring phase. The exact combined CSS remains the v0.1 fidelity source.

## Templates

- `aftershock-regression-template.html` reproduces the Golden Sample with external assets.
- `base.html` defines the reusable renderer shell.
- `components/` contains reusable markup contracts derived from the Golden Sample classes.

The component templates use Jinja-style placeholders as a renderer contract. The semantic renderer is not included in this package.
