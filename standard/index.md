# Reconstruction‑Grade eDiscovery Standard (RGR)

**A vendor‑independent architectural standard for preserving and reproducing modern collaborative evidence with point‑in‑time fidelity — without relying on post‑hoc inference.**

- **Read the Standard:** [Front Matter & Executive Summary](front-matter.md)
- **Download PDF:** [v0.51‑draft](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/releases/latest/download/rgr-standard-0.51-draft.pdf)
- **Repository:** [canonical source (Markdown)](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/tree/main/standard)

## What is Reconstruction-Grade eDiscovery?

**Reconstruction-Grade eDiscovery (RGR)** is an architectural standard for preserving and reconstructing collaborative cloud evidence.

It defines measurable criteria for systems that must reproduce:

- the **state of documents at the time of communication**
- the **identity of actors over time**
- the **relationships between messages, links, files, and versions**
- **audit evidence of interaction**
- **reproducible exports with manifest traceability**

The goal is to eliminate reliance on inference when answering legal questions about:

- what happened
- when it happened
- who was involved
- what document version was relied upon.

## Why this exists: the [Context Gap](concepts/context-gap-ediscovery.md)

Modern evidence in Microsoft 365 and similar platforms is created through:

- hyperlinks instead of attachments
- continuous versioning instead of discrete drafts
- shared repositories instead of personal storage
- audit signals instead of permission inference

Traditional eDiscovery exports flatten this reality into files and messages, losing the context needed to defend "what happened, when, and what version was relied on."

→ [Read the full definition: The Context Gap in eDiscovery](concepts/context-gap-ediscovery.md)

## What "Reconstruction‑Grade" means (in one minute)

Reconstruction‑Grade is a **conformance target** (architectural classification).
Context‑Aware eDiscovery is an **operating approach** consistent with that target.

A Reconstruction‑Grade system preserves three pillars of context as evidence:

1. Identity over time (effective‑dated)
2. Behavior evidence (audit, explicitly bounded)
3. Document state & relationships (message ↔ link ↔ file ↔ version)

## How to use this standard

If you are evaluating platforms or designing a pilot:

1. Start with **[Minimum Conformance Tests (T‑01 … T‑07)](06-evaluation-framework.md#63-minimum-conformance-tests)**
2. Use **[Questions to Ask Vendors](appendix-g-vendor-questions.md)**
3. Score candidates using the **[Vendor Scoring Worksheet](appendix-h-vendor-scoring.md)**
4. Require a **[Conformance Declaration](toolkit/conformance-declaration-template.md)** against a specific standard version

## Quick links (most used)
- [Core Concepts](concepts/index.md) — Context Gap, Evidence Reconstruction, Modern Attachments, Identity Drift
- [What is the Context Gap in eDiscovery?](concepts/context-gap-ediscovery.md)
- [What is Evidence Reconstruction in eDiscovery?](concepts/evidence-reconstruction.md)
- [What is Reconstruction-Grade eDiscovery?](concepts/reconstruction-grade-ediscovery.md)
- [Front Matter & Executive Summary](front-matter.md)
- [Minimum Conformance Tests](06-evaluation-framework.md#63-minimum-conformance-tests)
- [Appendix G: Questions to Ask Vendors](appendix-g-vendor-questions.md)
- [Appendix H: Vendor Scoring Worksheet](appendix-h-vendor-scoring.md)
- [Appendix B: Requirements (RGR‑ID, RGR‑AU, RGR‑DS, RGR‑RL, RGR‑EX)](appendix-b-requirements.md)

## Participate
- [Open an Issue](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/issues/new/choose) with feedback (terminology, requirements clarity, platform coverage)
- [Propose non‑normative improvements](participate/how-to-contribute.md) via Pull Request
- [Join the working group](participate/governance-working-group.md) — or email [info@cloudficient.com](mailto:info@cloudficient.com)
