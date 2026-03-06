---
description: >-
  Evidence Reconstruction in eDiscovery is the ability of a system to
  deterministically reproduce what actors experienced in a collaborative
  environment at a specific point in time — without relying on inference.
---

# What Is Evidence Reconstruction in eDiscovery?

> **Evidence Reconstruction (eDiscovery):**
> The ability of a system to deterministically reproduce what actors experienced
> in a collaborative environment at a specific point in time, grounded in
> preserved fact rather than post-hoc inference.

## Definition

**Evidence Reconstruction** refers to the ability of a system to deterministically reproduce what actors experienced in a collaborative environment at a specific point in time.

In modern cloud collaboration platforms, evidence is not a static artifact. It is the result of interactions between:

- messages
- linked documents
- version histories
- identity states
- permissions
- audit events

Traditional eDiscovery systems capture **files and messages**.

Reconstruction-Grade systems capture the **relationships and timelines required to reconstruct events**.

The goal of evidence reconstruction is to answer questions such as:

- What version of a document existed when a message was sent?
- Who had access at that moment?
- Who actually interacted with the document?
- What state informed a decision?

Evidence reconstruction replaces inference with preserved fact.

## Why Reconstruction Matters

### Evidence is evaluated under adversarial conditions

Court challenges to authenticity, completeness, proportionality, and chain of custody assume that any ambiguous or non-reproducible claim will be contested. A system capable of evidence reconstruction produces records designed to withstand that scrutiny.

### Inference is not defensibility

When critical context is inferred after the fact — who had access, which version was relied upon, whether a document was actually seen — it becomes contestable, non-reproducible, and dependent on narrative. Evidence reconstruction requires that context be preserved *while it exists*, not assembled after the fact.

### Context decays over time

People leave organizations. Repositories are repurposed. Links break. Audit logs age out. Traditional eDiscovery begins after this loss has occurred. Evidence reconstruction treats waiting as the fundamental mistake: if context will be needed later, it must be preserved now.

## The Evidence Graph

Reconstruction-Grade systems model evidence as an interconnected graph of **objects, relationships, and timelines** — not a set of independent files.

**Figure — Evidence Graph: Objects and Relationships Preserved for Reconstruction**

![Evidence Graph: Reconstruction requires objects, relationships, and timelines to be preserved as a coherent record](../images/evidence-graph-objects-relationships.png)

The evidence graph is built on three pillars:

1. **Identity over time.**
   Authoritative, effective-dated identity correlated to a natural person — including role, department, manager, status, and group membership as of any historical date.

2. **Behavior and activity evidence.**
   Audit and activity records treated as first-class evidence to establish interaction (view, edit, share, access) and timing. Behavioral claims are explicitly bounded by upstream availability, licensing, and retention. Where audit evidence does not exist, the system represents observed access as *unknown* — it does not substitute permission-based inference.

3. **Document state and relationships.**
   Deterministic point-in-time file resolution using stable platform-native identifiers (siteId, driveId, itemId, versionId). Explicit message ↔ link ↔ file ↔ version bindings are preserved so that every communication can be reconnected to the document state it referenced.

These three pillars are formally defined in [Section 3: Defining Reconstruction-Grade eDiscovery](../03-defining-reconstruction-grade.md).

## Key Reconstruction Concepts

- **As-sent version** — the file version that existed when a communication was sent, resolved as the latest version whose `lastModifiedDateTime ≤ message timestamp`.

- **Accessed version** — the file version a specific actor actually opened, derived from audit evidence. If audit evidence is unavailable, the accessed-version claim must be represented as unknown.

- **Deterministic exception record** — a structured record capturing every reference that could not be resolved, with reason codes, retry history, and parent-communication association.

- **Reproducible export** — an export where the same scope definition and parameters produce the same outputs, supported by manifests, hashes, and full exception traceability.

## Related Concepts

Evidence Reconstruction is closely related to several structural challenges and capabilities in modern eDiscovery:

- **[The Context Gap](context-gap-ediscovery.md)** — The structural difference between collaborative cloud evidence behavior and legacy eDiscovery exports. Evidence reconstruction is the capability that closes the Context Gap.

- **[Context Collapse](../02-context-collapse.md)** — When collaborative evidence is flattened into disconnected files and messages, reconstruction fails. Context collapse is the failure mode; evidence reconstruction is the countermeasure.

- **[Reconstruction-Grade eDiscovery](reconstruction-grade-ediscovery.md)** — The architectural classification for systems capable of evidence reconstruction. A system is Reconstruction-Grade when it can deterministically answer questions about document state, identity, relationships, and access.

- **[Modern Attachments](modern-attachments.md)** — Messages reference live repository objects via hyperlinks. Evidence reconstruction requires resolving the document state as-of the event timestamp for each modern attachment.

- **[Identity Drift](identity-drift.md)** — Custodians change roles, teams, and access rights over time. Evidence reconstruction requires effective-dated identity — not present-day directory snapshots.

- **[The Preservation System of Record](../04-preservation-system-of-record.md)** — The architectural layer that holds reconstructed evidence. Neither collaboration platforms nor review tools are designed to serve as litigation-grade systems of record.

- **[Conformance Levels (RG-Core, RG-Plus, RG-Max)](reconstruction-grade-ediscovery.md#conformance-levels)** — Three levels that define incremental reconstruction depth, from baseline document-state reconstruction to full identity, behavior, and expanded artifact coverage.

- **[Version Lineage Evidence](../01-structural-shift.md#13-version-lineage-is-now-evidentiary)** — Version history is not a storage feature. It is the audit trail of authorship, evolution, and reliance that reconstruction depends on.

## Reconstruction vs Traditional Collection

| Dimension | Traditional Collection | Evidence Reconstruction |
|---|---|---|
| What is preserved | Final-state files and messages | Objects, relationships, and timelines |
| Document state | Today's version | Version as-of the event timestamp |
| Identity | Present-day directory snapshot | Effective-dated identity over time |
| Access evidence | Inferred from permissions | Observed from audit records (bounded) |
| Unresolvable references | Silently dropped | Structured exception records |
| Exports | One-time extraction | Reproducible with manifests and hashes |

## Further Reading

- [What Is Reconstruction-Grade eDiscovery?](reconstruction-grade-ediscovery.md) — The architectural classification for evidence reconstruction systems
- [What Is the Context Gap in eDiscovery?](context-gap-ediscovery.md) — The structural problem that evidence reconstruction addresses
- [Modern Attachments](modern-attachments.md) — How hyperlinked files require reconstruction
- [Identity Drift](identity-drift.md) — How changing identity states require temporal reconstruction
- [Section 1: The Structural Shift in Evidence Behavior](../01-structural-shift.md) — The evidence model changes that make reconstruction necessary
- [Section 2: The Context Collapse Problem](../02-context-collapse.md) — Failure modes when reconstruction is not possible
- [Section 3: Defining Reconstruction-Grade eDiscovery](../03-defining-reconstruction-grade.md) — Formal definition of the three-pillar evidence model
- [Section 4: The Preservation System of Record](../04-preservation-system-of-record.md) — The architectural layer for reconstruction
- [Appendix D: Reconstruction Scenarios](../appendix-d-reconstruction-scenarios.md) — Worked examples of evidence reconstruction in practice
- [Appendix A: Glossary](../appendix-a-glossary.md) — Key terms used throughout the standard

---

<small>

**About this standard.** The Reconstruction-Grade eDiscovery Standard is an open, vendor-neutral specification maintained at [github.com/cloudficient/reconstruction-grade-ediscovery-standard](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard) and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Read the full standard:** [Reconstruction-Grade eDiscovery Standard →](../front-matter.md)

</small>
