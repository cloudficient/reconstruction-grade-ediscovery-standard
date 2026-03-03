---
description: >-
  The Context Gap in eDiscovery is the structural difference between how
  evidence is created in collaborative cloud platforms and what traditional
  eDiscovery systems can reconstruct after the fact.
---

# The Context Gap in eDiscovery

> **Context Gap (eDiscovery):**
> The structural difference between collaborative cloud evidence behavior and the final-state file exports typically produced by traditional eDiscovery systems.

## Definition

The **Context Gap** in eDiscovery refers to the structural difference between:

1. **How evidence is created in collaborative cloud platforms**, and
2. **What traditional eDiscovery systems can reconstruct after the fact.**

Modern collaboration environments (such as Microsoft 365, Google Workspace, and Slack) generate evidence through **hyperlinks, shared repositories, version histories, and evolving identity states**.

Traditional eDiscovery workflows typically export **final-state files and messages**, losing the contextual signals required to reproduce what actually occurred.

This gap creates a situation where the preserved evidence cannot deterministically answer questions about:

- which document version existed at the time of communication
- who had access at a given moment
- what version informed a decision
- what interactions actually occurred.

[Reconstruction-Grade eDiscovery](reconstruction-grade-ediscovery.md) addresses the Context Gap through [evidence reconstruction](evidence-reconstruction.md) — preserving context as first-class evidence.

## How the Context Gap Manifests

The Context Gap is not a single failure. It is a pattern of structural mismatches between what collaborative platforms produce and what legacy evidence models expect.

**Figure — The Context Gap**

![The Context Gap: collaborative evidence behavior has outpaced legacy evidence models](../images/context-gap-diagram.png)

### Legacy assumptions vs collaborative reality

| Evidence Dimension | Legacy Assumption | Collaborative Reality |
|---|---|---|
| Unit of evidence | File or attachment | Activity + link + shared repository object |
| Evidence capture | Final-state collection | Point-in-time resolution per event |
| Custodians | Static containers | Natural persons with effective-dated identity |
| Access | Inferred from permissions | Observed via audit evidence where available |
| Versioning | Minor or ignored | Continuous; version lineage is evidentiary |
| Messages | Immutable email | Threaded, editable, multi-modal conversations |

When evidence systems collect only today's file state, they produce a **time-shifted record**. The exported bytes are not the bytes that informed a decision at the time.

### What the gap looks like in practice

- A Teams message links to a OneDrive document. The file is edited after the message is sent. A traditional export collects the current file bytes—not the version that informed the decision.
- A custodian changes roles mid-matter. The exported identity reflects who they are today, not who they were during the relevant period.
- Permissions say a person *could* have accessed a file. But there is no audit evidence showing they *did*.
- Audit logs age out of retention. The behavioral evidence needed to answer "who saw what, when" no longer exists.

These are not edge cases. They are the **default behavior** of collaborative cloud platforms.

## Related Concepts

The Context Gap is closely related to several structural challenges in modern eDiscovery:

- **[Modern Attachments / Hyperlinked Files](modern-attachments.md)** — Messages reference live repository objects via hyperlinks instead of embedding file bytes. The message does not carry the document state it references.

- **[Version Lineage Evidence](../01-structural-shift.md#13-version-lineage-is-now-evidentiary)** — Files are continuously revised. Version lineage is the audit trail of authorship, evolution, and reliance. Ignoring version history means ignoring the evidentiary record.

- **[Identity Drift](identity-drift.md)** — People change roles, teams, access rights, and reporting lines. Legal questions are temporal, but directory snapshots are not.

- **[Permission vs Observed Access](../01-structural-shift.md#15-permissions-are-not-proof-of-behavior)** — Permissions describe potential access. Audit logs record observed behavior. Substituting one for the other is inference, not evidence.

- **[Reproducible Evidence Exports](reconstruction-grade-ediscovery.md#conformance-levels)** — An export where the same scope definition and parameters produce the same outputs, with manifests, hashes, and exception traceability.

- **[Context Collapse](../02-context-collapse.md)** — The flattening of collaborative evidence into disconnected files and messages, making reconstruction dependent on inference rather than preserved fact.

## How Reconstruction-Grade eDiscovery Addresses the Context Gap

The [Reconstruction-Grade eDiscovery Standard (RGR)](../front-matter.md) was created specifically to close the Context Gap. It defines measurable, testable criteria for evidence systems that preserve context as first-class evidence across three pillars:

1. **Identity over time** — Effective-dated identity correlated to a natural person, including role, department, manager, status, and group membership as of any historical date.

2. **Behavior and activity evidence** — Audit and activity records treated as first-class evidence to establish interaction and timing, explicitly bounded by upstream availability, licensing, and retention.

3. **Document state and relationships** — Deterministic point-in-time file resolution using stable platform-native identifiers. Explicit message ↔ link ↔ file ↔ version bindings preserved so that every communication can be reconnected to the document state it referenced.

These three pillars are formally defined in [Section 3: Defining Reconstruction-Grade eDiscovery](../03-defining-reconstruction-grade.md).

The standard does not treat inference as defensibility. When context cannot be grounded in preserved fact, it is represented as *unknown*—not assumed.

## Further Reading

- [What Is Reconstruction-Grade eDiscovery?](reconstruction-grade-ediscovery.md) — Full definition of the architectural classification
- [What Is Evidence Reconstruction?](evidence-reconstruction.md) — The capability that closes the Context Gap
- [Modern Attachments](modern-attachments.md) — How hyperlinked files drive the Context Gap
- [Identity Drift](identity-drift.md) — How changing custodian identity creates temporal evidence gaps
- [Section 1: The Structural Shift in Evidence Behavior](../01-structural-shift.md) — The evidence model changes that created the Context Gap
- [Section 2: The Context Collapse Problem](../02-context-collapse.md) — Failure modes that result from the Context Gap
- [Section 3: Defining Reconstruction-Grade eDiscovery](../03-defining-reconstruction-grade.md) — The evidence model that closes the gap
- [Appendix A: Glossary](../appendix-a-glossary.md) — Key terms used throughout the standard

---

<small>

**About this standard.** The Reconstruction-Grade eDiscovery Standard is an open, vendor-neutral specification maintained at [github.com/cloudficient/reconstruction-grade-ediscovery-standard](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard) and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Read the full standard:** [Reconstruction-Grade eDiscovery Standard →](../front-matter.md)

</small>
