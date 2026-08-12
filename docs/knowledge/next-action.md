# Next Action

Updated: 2026-08-12

## Current Status

`PRD_SIMPLE_CHAT_PREVIEW_GATE_LOCKED_CLOCKWORK_DECISIONS_PENDING`

Working branch: **`Local` only**.

## Current system state

The exact approved AFTERSHOCK Golden remains the canonical reference/runtime template, with the bidirectional fidelity model:

```text
Reference → Fill Map
Project Authority → Filled Golden
```

Flow 2 also performs bounded cross-surface consistency checks before production readiness, so a mature source is not assumed internally consistent merely because it is labelled authoritative.

The Flow 2 → Flow 3 boundary now includes a mandatory **Simple Chat Preview** for initial PRD production:

```text
Source
→ recover + safely complete meaning
→ detect / resolve material conflicts
→ Simple Chat Preview
→ user correction / approval
→ ready_for_prd
→ BUILD PRD
```

The preview is intentionally simple and objective-based:

```text
Project Overview
Objective N
  Tujuan
  Apa yang Player Lakukan
  Hasil
  Level Design
  Developer
  Perlu Konfirmasi — only when material unresolved meaning exists
```

It is not a new Flow and not a new project artifact. Internal requirement IDs, YAML, provenance, recovery classes, Golden DOM vocabulary, and validator output stay out of the normal preview.

Only a minimal continuity signal is added to Flow 2 state:

```yaml
preview_approved: false | true
```

Before initial approval, Flow 2 remains non-ready. After natural-language user approval, `preview_approved: true` accompanies `ready_for_prd: true`. Material corrections are persisted as authoritative user instructions and only affected objective/global slices are re-previewed.

The existing PRD validator now has one bounded mechanical guard: if a state explicitly says `preview_approved: false`, `ready_for_prd` validation fails. Existing historical/project fixtures that predate the field are not rewritten solely for this change; the active Flow 2 contract requires new initial production to persist the field explicitly.

For bounded revisions, the full project preview is not replayed. Only affected objective/global meaning is previewed when interpretation changed; an explicit user instruction that already states the complete intended bounded result may serve as approval for that slice.

## Real-source proof boundary

The real non-AFTERSHOCK forward-fill test remains **The Clockwork Vault - Adventure Map - Final Review.html**, whose authoritative hash matches the previous system-integration proof.

That test exposed five unresolved same-authority conflicts before regeneration:

1. Resonance Engine target timing/progression;
2. Broken Gallery checkpoint-vs-three-route collapse model;
3. Warden Halls Echo Pebble behavior on ceiling traps;
4. Gremlin’s Workshop permanent broken connection vs Elbow-rule inversion;
5. Ending reward name (`Clockwork Wayfinder` vs `Vault Explorer Banner`).

Those are correct preview-stage blockers. The generator must not choose one side silently merely to reach Golden rendering.

## Proof boundary

This change modifies only the Flow 2/kit procedure, high-level Flow 2→3 boundary, one bounded readiness guard in the existing validator, focused contract tests, package version/readme alignment, and this current-state owner. It does not add a preview renderer, preview document, new workflow status, new schema, or generic approval framework.

Static CI can prove the procedure/mechanical contract remains present. A real production run is still needed to prove user-facing preview usability in practice.

## Next Step

**Use the five Clockwork conflicts as the first live Simple Chat Preview decision bundle, capture the user's corrections/approval, then regenerate Clockwork through the approved Golden fill contract.**
