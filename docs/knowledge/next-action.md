# Next Action

## Current Status

`CONTENT_QUALITY_AUDIT_ACTIVE`

The unified `kits/prd-creator/` migration and Clockwork browser visual QA are complete. The user has approved a new bounded phase focused on improving **document content quality** by studying representative sample content before changing the production system.

## Active Boundary

This phase is **Content Audit / Content Quality Research**, not immediate renderer or contract implementation.

The user will provide one or more sample documents/content pieces. Treat those samples as reference evidence for content quality, organization, writing, hierarchy, information density, and production usefulness. Do not treat sample-specific facts as project authority for Clockwork or any other project.

Until the audit identifies and the user approves concrete improvements:

- do not change gameplay/project meaning;
- do not change Voice requirements or production wording;
- do not change Golden/template/renderer merely to imitate a sample;
- do not redesign repository architecture;
- do not alter current accepted Clockwork output;
- do not promote conditional backlog items.

## Audit Goal

Determine what makes the supplied sample content produce a stronger professional document, then translate only justified patterns into a clear improvement proposal for PRD-Creator.

Audit dimensions include, as supported by the samples:

```text
information hierarchy
section purpose and ordering
content completeness
clarity and specificity
writing density / concision
rule and requirement readability
separation of overview vs actionable detail
use of tables, lists, callouts, and prose
terminology consistency
reader orientation / scanability
handoff usefulness for builders, developers, designers, and production teams
repetition vs necessary reinforcement
content that feels generic, vague, inflated, or AI-written
```

The audit should distinguish:

```text
sample fact
→ belongs only to that sample

sample presentation/content pattern
→ candidate reusable principle

current PRD-Creator weakness
→ must be proven by comparison with current owners/output

recommended improvement
→ proposal until explicitly approved
```

## Existing Accepted Baseline

The previous visual acceptance remains valid and is not reopened by this audit:

```text
Golden/runtime template Git blob
2050b965768489feda98373c2920bbee8c7093b3

Clockwork prd.html Git blob
3267b2f97e7335418a43edd6b0e81f6077aeeb51

Project HTML Visual: PASS
```

Content audit may later recommend changes to content generation/contract behavior, but only after the sample comparison establishes a concrete quality gap and the user approves the direction.

## Expected Audit Output

After enough samples are provided, produce a structured audit covering:

1. what each sample does well;
2. recurring high-quality content patterns across samples;
3. weak/irrelevant patterns that should **not** be copied;
4. comparison against current PRD-Creator content behavior;
5. prioritized content-quality gaps;
6. proposed improvement principles and exact owner(s) that would need changes;
7. implementation scope only after user approval.

Do not implement during the observation pass unless the user explicitly moves from audit to implementation.

## Next Step

**Receive and study the user-provided sample content. Audit the content itself first—structure, hierarchy, clarity, completeness, density, specificity, scanability, and handoff usefulness—without changing PRD-Creator yet. Accumulate evidence across samples, then present the reusable quality patterns and gaps for user approval before implementation.**
