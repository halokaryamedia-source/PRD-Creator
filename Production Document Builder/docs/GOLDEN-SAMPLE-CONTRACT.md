# Golden Sample Contract

The locked benchmark is the user-approved AFTERSHOCK V1.8 document, stored as
`golden-sample/aftershock-golden-sample-v1.0.html`.

## Exact Regression

Rerendering the Golden Sample must satisfy all of the following:

- 30 pages in the approved order;
- `01 — Overview`, `02 — Gameplay Flow`, and `03 — Development` hierarchy;
- full The Quarry Gameplay Overview, Level Design, and Developer benchmark;
- exact sidebar, controls, tooltip, Terms Used, CSS, JavaScript, and interactions;
- byte-identical output;
- SHA-256 `6af765b1c40100728b126fe219c88e5f0f734816f6c9a596d1cd90292c380901`.

## New Projects

New projects use the same visual/component system and profile-aware hierarchy,
but are not expected to be byte-identical because their content and page count are
different. They must still look like the same document family and pass Final HTML
Audit against the Golden Sample.

A generic fixture must never be described as a Golden parity artifact.
