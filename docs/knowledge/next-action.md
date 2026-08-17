# Next Action

## Current Status

`MAP_COMPOSITION_AUDIT_WAITING_FOR_READABLE_SAMPLES`

The unified `kits/prd-creator/` migration and Clockwork browser visual QA are complete. The user has approved a new bounded audit phase focused on understanding the **professional composition of a finished/developed map** from representative real development samples before changing PRD-Creator.

## Active Boundary

This phase is **Map Composition Audit / Content Audit**, not immediate renderer, Golden, contract, or architecture implementation.

The official sample set for this audit is the user upload:

```text
ChoosenSamples (2).zip
~508 MB
```

The earlier mistakenly uploaded Clockwork responsive-fix ZIP is explicitly excluded from the audit.

Current tool evidence can see the official ZIP as an intact attachment, but the Files layer does not expose or index the archive members as readable documents, and the current local/container runtime cannot unpack the ZIP. Therefore the actual development contents have **not yet been audited**. Do not infer findings from the archive name, size, or unrelated prior files.

## Audit Goal

Determine, from the actual development samples, **what concrete components together make the map a finished playable product** and what information a professional production document should represent so another team can understand, build, implement, test, maintain, or hand off that map.

The audit is not limited to prose/document quality. It should inspect every relevant development artifact and recover the real production anatomy of the map, including only categories actually supported by the samples.

Potential categories to test against the evidence include:

```text
project / map identity and scope
player experience and intended flow
gameplay rules and objective progression
level / environment design
coordinates, zones, checkpoints, spawn and teleport points
logic / scripting / state machines / triggers
entities, NPCs, mobs and behavior
items, blocks, structures and interactables
UI, text, hints, tutorials and feedback
audio, voice, music and sound effects
visual effects / particles / animation / camera
resource-pack / behavior-pack / data dependencies
models, textures and other production assets
scoring, timers, rewards, progression and persistence
multiplayer/session/arena behavior when present
reset, retry, fail, recovery and edge-case behavior
configuration / tuning values
testing / QA / known issues / acceptance evidence
build/developer handoff information
packaging / delivery / versioning where present
```

These are **audit hypotheses**, not assumed requirements. A category becomes part of the professional map model only when the sample evidence supports it or when a later explicit product decision approves it.

## Audit Method

For each sample:

```text
inventory actual files/artifacts
→ identify what each artifact contributes to the map
→ map dependencies between artifacts
→ reconstruct the player-facing flow
→ reconstruct the implementation-facing flow
→ identify data/configuration needed to reproduce behavior
→ identify QA/proof needed to know the map is actually complete
```

Then compare across samples:

```text
sample-specific content
vs
recurring professional map component
vs
optional/specialized component
vs
redundant/noisy development artifact
```

The audit must distinguish:

```text
sample fact
→ directly evidenced by supplied development output

inference
→ derived from relationships between supplied artifacts

professional synthesis
→ reusable model proposed from recurring evidence

PRD-Creator requirement
→ remains a proposal until explicitly approved
```

## Expected Audit Output

After the development samples are readable, produce:

1. an inventory of what each sample actually contains;
2. a professional **Map Anatomy / Map Production Model** showing the components that make a map complete;
3. which components are core vs optional/specialized;
4. the dependency chain between design, implementation, assets, runtime logic, and QA;
5. what information a professional PRD/handoff should capture for each component;
6. which current PRD-Creator sections already cover those needs;
7. which information is currently missing, too vague, duplicated, or stored in the wrong place;
8. prioritized improvement proposals, without implementation until user approval.

## Existing Accepted Baseline

The previous visual acceptance remains valid and is not reopened by this audit:

```text
Golden/runtime template Git blob
2050b965768489feda98373c2920bbee8c7093b3

Clockwork prd.html Git blob
3267b2f97e7335418a43edd6b0e81f6077aeeb51

Project HTML Visual: PASS
```

## Protected Boundary

Until the actual sample artifacts are readable and audited:

- do not change gameplay/project meaning;
- do not change Voice requirements or wording;
- do not change Golden/template/renderer to imitate assumptions;
- do not redesign repository architecture;
- do not change accepted Clockwork output;
- do not promote conditional backlog items;
- do not turn theoretical categories above into mandatory schema/requirements.

## Next Step

**Read/unpack the official chosen development sample set, inventory every relevant artifact, and reconstruct what concrete design, implementation, asset, runtime, and QA components together make each map a finished product. Do not modify PRD-Creator until the evidence has been synthesized and the user approves the resulting improvement proposal.**
