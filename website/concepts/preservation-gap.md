---
description: >-
  The Preservation Gap in eDiscovery is the structural gap between what
  litigation hold systems can reach and where modern collaborative evidence
  actually resides — causing linked documents to expire silently outside hold scope.
chat_prompts:
  - "How does the Preservation Gap affect my M365 legal holds?"
  - "Can my hold system detect cross-custodian link targets?"
  - "What's the difference between the Context Gap and the Preservation Gap?"
  - "What does collect-to-preserve mean for my workflow?"
---

# The Preservation Gap in eDiscovery

> **Preservation Gap (eDiscovery):**
> The structural gap between what an organization's litigation hold system can reach and where modern collaborative evidence actually resides. Litigation holds are custodian-scoped, but collaborative evidence is relationship-scoped — hyperlinks in a held custodian's messages may reference documents in non-custodian storage governed by separate retention policies.

## Definition

The **Preservation Gap** in eDiscovery refers to the structural gap between:

1. **What a litigation hold system preserves** (the custodian's mailbox, site, or OneDrive), and
2. **What the custodian's evidence actually references** (documents in other users' storage, shared repositories, or locations outside the hold scope).

Modern collaboration platforms encourage sharing by reference — hyperlinks to live documents — rather than embedding file copies. When a custodian is placed on hold, the hold system preserves the custodian's *container*. It does not parse, resolve, or traverse the hyperlinks within the custodian's messages. If the linked content resides in a non-custodian's storage, it remains governed by that storage location's retention policy — ticking toward expiry while the hold system reports full compliance.

The result: the email is preserved, the link is preserved, but the evidence the link pointed to is gone. The hold did everything it was designed to do. It just was not designed for evidence that crosses custodian boundaries.

## How the Preservation Gap Manifests

The Preservation Gap is not a collection failure or a processing error. It is a **scope failure** — the hold system's boundary does not match the evidence's boundary.

### The core scenario

1. **User B** sends **User A** an email containing a hyperlink to a document in B's OneDrive.
2. **User A** is identified as a custodian and placed on legal hold.
3. **User B** is not a custodian. No hold is placed on B or B's storage.
4. The document in B's OneDrive reaches its retention limit and is permanently purged.
5. A's preserved email now contains a dead link. The evidence it referenced no longer exists anywhere in the organization.

### Why traditional holds cannot close this gap

| Hold System Behavior | Evidence Reality |
|---|---|
| Holds are **custodian-scoped** — they preserve a container (mailbox, OneDrive, site) | Evidence is **relationship-scoped** — a single message may reference content across multiple storage locations |
| Holds do not parse message content for hyperlinks | Hyperlinks are the primary sharing mechanism on modern platforms |
| Holds do not traverse links to identify referenced content | Referenced content may reside in non-custodian storage with independent retention |
| Hold compliance reports reflect container status | Container compliance does not reflect evidence completeness |

The organization has administrative control over both storage locations. The platform provides APIs to preserve specific items. The **capability exists** — but the hold workflow does not trigger it, because the hold system operates at the custodian level and the evidence relationship crosses a custodian boundary.

### The spiderweb problem

The intuitive response — "just extend the hold to cover the linked content" — creates a cascading scope problem. Placing User B on hold to preserve one linked document means holding *all* of B's content. B's mailbox contains links to content in C, D, and E's storage. Within two hops, a significant fraction of the organization could be on litigation hold. For a company with 60,000 users, custodian-scoped hold expansion is not a viable preservation strategy for relationship-scoped evidence.

This is why the architecturally correct response is **collect-to-preserve**: collect the specific linked object at the point of identification, without expanding the custodian hold scope to the content owner. The unit of preservation is the evidence relationship, not the custodian container.

## The Preservation Gap vs. the Context Gap

The Preservation Gap and the [Context Gap](context-gap-ediscovery.md) are related but distinct failure modes:

| Dimension | Context Gap | Preservation Gap |
|---|---|---|
| **What fails** | Evidence fidelity — the preserved record does not reflect what was experienced | Evidence completeness — the referenced content is not preserved at all |
| **Root cause** | Final-state collection captures the wrong version | Custodian-scoped holds cannot reach cross-boundary content |
| **Symptom** | The document exists but reflects a different point in time | The document no longer exists — the link is dead |
| **Detection** | Requires version comparison (often invisible to reviewers) | Visible only when someone follows the link and finds nothing |
| **Common root** | Both arise because hold systems are custodian-scoped while evidence is relationship-scoped |

Together, they define the diagnostic framework for modern evidence preservation:

- The **Context Gap** tells you what was *damaged in transit* — the preserved version does not match the communicated version.
- The **Preservation Gap** tells you what *never made it onto the truck* — the linked content was outside hold scope and expired before anyone collected it.

Both point to the same architectural solution: evidence-level preservation that follows relationships across custodian boundaries.

## Rule 37(e) Implications

Under [FRCP Rule 37(e)](https://www.law.cornell.edu/rules/frcp/rule_37), sanctions for lost ESI require that the party failed to take **reasonable steps** to preserve. The Preservation Gap raises a direct question: if a party knows its custodians share evidence via hyperlinks to content in other users' storage, and the hold system does not traverse those links, is the hold alone a reasonable step?

The factors that make this question increasingly difficult to dismiss:

- **The Sedona Conference** acknowledged in its 2025 Commentary that collaboration platform data creates distinct preservation challenges, including cross-system storage and hyperlinked content.
- **Carvana** demonstrated that courts are now ordering capability tests — directing parties to run specific forensic tools and demonstrate what can and cannot be recovered from hyperlinked content.
- **The technical capability exists.** The linked content resides in same-tenant storage under the organization's administrative control. APIs exist to identify and collect it. The gap is in the workflow, not the platform's capability.

No court has held that cross-custodian link traversal is required by Rule 37(e). But the convergence of industry guidance, developing case law, and known technical gaps makes the Preservation Gap harder to defend as an acceptable risk in matters involving collaborative, hyperlinked evidence.

For detailed case law analysis, see [Judicial Signals and Case Developments](../judicial-signals.md). For the Rule 37(e) analysis of reasonable steps in the collaboration platform context, see [What FRCP Rule 37(e) Means for Modern Collaboration Platforms](../blog/posts/2026-03-31-what-frcp-rule-37e-means-for-modern-collaboration-platforms.md).

## How Reconstruction-Grade eDiscovery Addresses the Preservation Gap

The [Reconstruction-Grade eDiscovery Standard](../front-matter.md) addresses the Preservation Gap through specific normative requirements:

- **RGR-RL-009** (RG-Core MUST): When preserving a message containing a hyperlink to same-tenant content, identify whether the link target is within an active preservation scope. If not, generate a structured exception identifying the at-risk content and its storage location.

- **RGR-RL-010** (RG-Plus SHOULD): Collect and preserve the specific linked object (at the version contemporaneous to the message) without expanding custodian hold scope to the content owner.

These requirements implement the **collect-to-preserve** model at the evidence relationship level: detect the gap, collect the specific artifact, preserve the binding between the message and the document version it referenced — without cascading custodian holds across the organization.

The standard also addresses the related [Context Gap](context-gap-ediscovery.md) through deterministic version resolution (RGR-DS-003), relationship integrity (RGR-RL-001), and exception transparency (RGR-ER-001 through RGR-ER-006).

## Related Concepts

- **[Context Gap](context-gap-ediscovery.md)** — The fidelity problem: preserved evidence does not reflect what was experienced. The Preservation Gap is the completeness problem: referenced evidence was never preserved.

- **[Modern Attachments / Hyperlinked Files](modern-attachments.md)** — The sharing mechanism that creates cross-custodian evidence dependencies. When messages reference live documents by hyperlink, the evidence relationship spans storage boundaries that holds do not traverse.

- **[Identity Drift](identity-drift.md)** — Evidence about who had access changes over time. The Preservation Gap compounds identity drift: if the linked document is lost, the access and authorship history associated with it may also be irrecoverable.

- **[Evidence Reconstruction](evidence-reconstruction.md)** — Reconstruction requires that the evidence relationship is preserved end-to-end. The Preservation Gap breaks the chain at the link target, making reconstruction of the communicated document state impossible.

## Further Reading

- [What Is Reconstruction-Grade eDiscovery?](reconstruction-grade-ediscovery.md) — Full definition of the architectural classification
- [The Context Gap in eDiscovery](context-gap-ediscovery.md) — The related fidelity problem in evidence preservation
- [Modern Attachments](modern-attachments.md) — How hyperlinked files create cross-custodian evidence dependencies
- [What FRCP Rule 37(e) Means for Modern Collaboration Platforms](../blog/posts/2026-03-31-what-frcp-rule-37e-means-for-modern-collaboration-platforms.md) — Rule 37(e) analysis for collaborative evidence
- [Judicial Signals and Case Developments](../judicial-signals.md) — Developing case law on preservation obligations
- [Appendix B: Requirements](../appendix-b-requirements.md) — Normative requirements including RGR-RL-009 and RGR-RL-010
- [Appendix D: Reconstruction Scenarios](../appendix-d-reconstruction-scenarios.md) — Scenario D.5: Cross-Custodian Link Expiry
- [Appendix A: Glossary](../appendix-a-glossary.md) — Key terms used throughout the standard

---

<small>

**About this standard.** The Reconstruction-Grade eDiscovery Standard is an open, vendor-neutral specification maintained at [github.com/cloudficient/reconstruction-grade-ediscovery-standard](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard) and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Read the full standard:** [Reconstruction-Grade eDiscovery Standard →](../front-matter.md)

</small>
