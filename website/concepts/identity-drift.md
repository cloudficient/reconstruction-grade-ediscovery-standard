---
description: >-
  Identity Drift in eDiscovery is the continuous change of a person's role,
  department, access rights, and organizational context over time — and why
  static custodian snapshots fail under temporal legal questions.
chat_prompts:
  - "How does identity drift affect my litigation hold process?"
  - "Can my eDiscovery system reconstruct who had access six months ago?"
  - "What does RGR require for historical identity resolution?"
  - "How does identity drift interact with the Context Gap?"
---

# Identity Drift (eDiscovery)

> **Identity Drift:**
> The continuous change of a person's role, department, manager, access rights, group membership, and organizational context over time — creating a structural mismatch between present-day directory snapshots and historical legal questions.

## Definition

**Identity Drift** refers to the fact that custodians are not directory objects frozen in time. People change roles, teams, reporting lines, access rights, and responsibilities throughout the lifecycle of any matter.

Legal questions are temporal. Discovery requests are drafted around **historical periods**, not present-day org charts. When evidence systems capture only the current identity state, they answer the wrong question: *who is this person today?* instead of *who were they during the relevant period?*

Identity Drift creates a gap between:

1. **What the directory says now** — current role, department, manager, group membership, status.
2. **What was true at the time** — the effective-dated identity state during the period under investigation.

This gap becomes legally significant when:

- a custodian's **role or department** changed during the relevant period
- **access rights** were granted, modified, or revoked
- **group membership** (distribution lists, Teams membership, SharePoint site membership) changed
- a custodian **left the organization** or transferred between entities
- **reporting lines** shifted, affecting supervision and oversight questions

## Why Static Custodian Snapshots Fail

Traditional eDiscovery treats custodians as static containers — a name, an email address, and a mailbox. This model was sufficient when evidence lived in personal storage and custodian boundaries were stable.

In collaborative cloud environments, identity is a **multi-dimensional, time-varying record**:

| Identity Dimension | Static Model | Effective-Dated Model |
|---|---|---|
| Role / Title | Present-day value | Historical value as of each relevant date |
| Department | Present-day value | Historical value with effective dates |
| Manager | Present-day value | Historical chain of supervision |
| Group membership | Current memberships | Membership timeline (join/leave dates) |
| Access rights | Current permissions | Permission history correlated to audit evidence |
| Employment status | Active / Inactive | Full status timeline (active, leave, transfer, termination) |

When identity is captured only at collection time, the exported record cannot answer:

- What department was this person in when they sent the message?
- Who was their manager when the decision was made?
- Were they a member of the relevant team during the investigation period?
- Did their access rights change before or after the event in question?

These are not edge cases. They are the **default questions** in employment litigation, regulatory investigations, internal investigations, and any matter with a historical scope.

## How Identity Drift Manifests in Practice

- **Role change during matter period.** A custodian moves from Compliance to Sales mid-matter. Their relevance, access patterns, and supervisory relationships change — but a static snapshot shows only their current role.

- **Group membership changes.** A custodian is removed from a SharePoint site or Teams channel. The present-day directory shows no membership. Without historical group records, the evidence cannot establish that they had access during the relevant period.

- **Manager change.** A regulatory investigation involves supervisory oversight. The custodian's current manager is not the manager who had oversight during the relevant period. Static identity cannot answer the oversight question.

- **Departure and backfill.** A custodian leaves the organization. Their directory record is disabled or deleted. Identity signals needed to correlate their historical activity to their organizational context are lost unless preserved with effective dates.

## How Reconstruction-Grade Systems Address Identity Drift

The [Reconstruction-Grade eDiscovery Standard](reconstruction-grade-ediscovery.md) treats identity as a **first-class evidence dimension** — not metadata.

Specifically, Reconstruction-Grade systems:

1. **Preserve effective-dated identity** — a historical record of who a person was during the relevant period, including role, department, manager, status, and group membership as of any historical date.

2. **Correlate identity to a natural person** — identity is tied to a natural person, not a mailbox or directory object. When a person has multiple accounts, aliases, or organizational entities, the identity record links them.

3. **Bound identity claims by availability** — where historical identity records are incomplete (e.g., directory snapshots were not retained), the system represents the gap explicitly rather than substituting present-day values.

4. **Support temporal identity queries** — the preserved record can answer "who was this person as of date X?" — not only "who are they today?"

These requirements are part of the **Identity over time** pillar, formally defined in:

- [Section 3.1: The Reconstruction-Grade Evidence Model](../03-defining-reconstruction-grade.md#31-the-reconstruction-grade-evidence-model) — Identity over time as the first pillar
- [Section 1.4: Identity Drift and the Static Custodian Myth](../01-structural-shift.md#14-identity-drift-and-the-static-custodian-myth) — The structural shift that created the problem
- [Appendix B: Reconstruction-Grade Requirements](../appendix-b-requirements.md) — RGR-ID requirement family for identity preservation

At the **RG-Plus** conformance level and above, systems must demonstrate effective-dated identity reconstruction including historical role, department, manager, and group membership.

## Related Concepts

- **[The Context Gap](context-gap-ediscovery.md)** — Identity Drift is one of several dimensions of the Context Gap. When identity is captured as a present-day snapshot, the evidence cannot answer temporal questions about organizational context.

- **[Evidence Reconstruction](evidence-reconstruction.md)** — Reconstructing events requires knowing who actors were at the time — not who they are today. Identity reconstruction is one of the three pillars of evidence reconstruction.

- **[Modern Attachments](modern-attachments.md)** — Document access and sharing questions depend on identity state. Who had access to a linked document at the time of communication is an identity question as much as a permissions question.

- **[Permission vs Observed Access](../01-structural-shift.md#15-permissions-are-not-proof-of-behavior)** — Permissions describe potential access based on identity and group membership. But permissions change as identity drifts. Without effective-dated identity, permission-based claims are anchored to the wrong point in time.

- **[Context Collapse](../02-context-collapse.md)** — When identity drift is ignored, the evidence record collapses temporal distinctions into a single present-day state. This is a form of context collapse.

## Further Reading

- [What Is Reconstruction-Grade eDiscovery?](reconstruction-grade-ediscovery.md) — The architectural classification that requires effective-dated identity
- [What Is the Context Gap in eDiscovery?](context-gap-ediscovery.md) — The structural problem that Identity Drift contributes to
- [Section 1.4: Identity Drift and the Static Custodian Myth](../01-structural-shift.md#14-identity-drift-and-the-static-custodian-myth) — The structural shift analysis
- [Section 3: Defining Reconstruction-Grade eDiscovery](../03-defining-reconstruction-grade.md) — Formal definition of the identity pillar
- [Appendix A: Glossary](../appendix-a-glossary.md) — Key terms used throughout the standard

---

<small>

**About this standard.** The Reconstruction-Grade eDiscovery Standard is an open, vendor-neutral specification maintained at [github.com/cloudficient/reconstruction-grade-ediscovery-standard](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard) and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Read the full standard:** [Reconstruction-Grade eDiscovery Standard →](../front-matter.md)

</small>
