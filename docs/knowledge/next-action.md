# Next Action

## Current Status

`CONTENT_QUALITY_AUDIT_WAITING_FOR_READABLE_SAMPLES`

The unified `kits/prd-creator/` migration and Clockwork browser visual QA are complete. The user has approved a new bounded phase focused on improving **document content quality** by studying representative sample content before changing the production system.

## Active Boundary

This phase is **Content Audit / Content Quality Research**, not immediate renderer or contract implementation.

The official sample set for this audit is the user upload:

```text
ChoosenSamples (2).zip
~508 MB
```

The earlier mistakenly uploaded Clockwork responsive-fix ZIP is explicitly excluded from the audit.

Current tool evidence can see the official ZIP as an intact attachment, but the Files layer does not expose or index the archive members as readable documents, and the current local/container runtime cannot unpack the ZIP. Therefore the sample contents have **not yet been audited**. Do not infer quality findings from the archive name, file size, or prior unrelated files.

Until the actual sample documents are readable and audited:

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

## Expected Audit Output

After the sample documents are readable, produce a structured audit covering:

1. what each sample does well;
2. recurring high-quality content patterns across samples;
3. weak/irrelevant patterns that should **not** be copied;
4. comparison against current PRD-Creator content behavior;
5. prioritized content-quality gaps;
6. proposed improvement principles and exact owner(s) that would need changes;
7. implementation scope only after user approval.

Do not implement during the observation pass unless the user explicitly moves from audit to implementation.

## Next Step

**Obtain the chosen sample documents in a directly readable form (individual files or an archive that the current runtime can unpack), then audit their actual content before making any PRD-Creator quality recommendation or implementation change.**
