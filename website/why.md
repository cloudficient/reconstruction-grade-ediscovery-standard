---
title: Why This Standard Exists
description: The problem that created the need for a reconstruction-grade evidence standard, how it emerged from real-world implementation, and honest answers to the questions evaluators will ask.
schema: faq
faq:
  - q: "What is reconstruction-grade eDiscovery?"
    a: "An architectural classification describing whether an evidence system can produce a reproducible, point-in-time record of collaborative cloud activity — deterministically resolving what documents existed, who was involved, what was shared, and who accessed what — grounded in preserved fact rather than inference."
  - q: "What is the context gap in eDiscovery?"
    a: "The structural difference between how evidence is created in collaborative cloud platforms — through hyperlinks, version histories, and evolving identity states — and what traditional eDiscovery systems can reconstruct after the fact. This gap prevents systems from deterministically answering which document version existed at the time of communication."
  - q: "What is evidence reconstruction?"
    a: "The ability of a system to deterministically reproduce what actors experienced in a collaborative environment at a specific point in time, grounded in preserved fact rather than post-hoc inference. Reconstruction-grade systems capture the relationships and timelines required to recreate events as they occurred."
  - q: "What is identity drift in eDiscovery?"
    a: "The continuous change of a person's role, department, access rights, and organizational context over time, creating a mismatch between present-day directory snapshots and historical legal questions. When a litigation question asks who had access to a document six months ago, the current directory state may not reflect the answer."
  - q: "What are modern attachments in eDiscovery?"
    a: "Message-level references to live repository objects — delivered via hyperlink instead of embedded file bytes — where the document continues to change after the message is sent. The message does not carry the document state it originally referenced, so the exported bytes may not be the bytes the recipient saw."
  - q: "How does the RGR Standard apply to Microsoft 365, Teams, and Slack?"
    a: "These platforms operate by default on hyperlinked documents, co-authored files, evolving identity, and shared workspaces. Every standard eDiscovery collection from these environments encounters the context gap. The standard provides measurable evaluation criteria and a vendor scoring worksheet for assessing platform capabilities."
  - q: "What are the RGR conformance levels?"
    a: "The standard defines three tiers: RG-Core (baseline — deterministic point-in-time document resolution, stable identifier preservation, and reproducible manifests), RG-Plus (adds effective-dated identity reconstruction and audit-evidence ingestion), and RG-Max (adds accessed-version analysis, expanded artifact coverage, and advanced validation)."
---

# Why This Standard Exists

## The evidence model changed. The industry didn't.

When someone sends a message that links to a shared document instead of attaching a copy, the evidence problem changes fundamentally. The document lives in a repository, not the message. It keeps being edited after the message is sent. Permissions shift. Versions accumulate. The state that mattered at the moment of the conversation may no longer exist by the time anyone asks about it.

This is not an edge case. It is the default behavior of Microsoft 365, Google Workspace, and every major collaboration platform. Hyperlinks have replaced attachments. Co-authoring has replaced sequential editing. Cloud identity has replaced static directory snapshots. And most of the eDiscovery industry is still built around the assumption that evidence is a file someone sent.

The result is a structural gap: the tools and workflows designed to preserve and produce evidence were built for a world that no longer exists. When preservation means collecting the latest version of a file instead of the version that was referenced, when identity means a current directory lookup instead of a historical record, when relationships between messages and documents are inferred instead of preserved — the evidence is incomplete before legal review even begins.

## Enterprises are already discovering these requirements on their own

When sophisticated enterprises confront this problem at scale — tens of thousands of users, thousands of concurrent legal matters, petabytes of collaboration data — they arrive at remarkably consistent requirements:

- **Point-in-time fidelity.** Capture the version of a document as it existed at the moment of communication, not the latest available state.
- **Relationship integrity.** Maintain the link between a message and the document it referenced, even if that document is later moved, renamed, versioned, or deleted.
- **Identity history.** Know who was a member of a group, what department someone belonged to, and what access they had — at a specific point in time, not just today.
- **Exception transparency.** When something cannot be collected, record what was attempted, why it failed, and what remediation is possible.
- **Reproducible outputs.** The same scope and time range should produce the same evidence set, with manifests, hashes, and declared exceptions.

These requirements are not theoretical. They appear independently in enterprise procurement processes, in ESI protocol negotiations, and in the operational lessons of teams that have tried to produce collaborative evidence and discovered what was missing.

The problem is that each enterprise reinvents this vocabulary from scratch. There is no shared framework for articulating what "defensible preservation" means when evidence is collaborative, linked, versioned, and identity-dependent. Every RFP restates the same requirements in different language. Every protocol negotiation revisits the same gaps.

The Reconstruction-Grade eDiscovery standard exists to provide that shared framework. The [Risk Exposure Framework](risk-exposure-framework.md) maps these requirements to the documented legal, procedural, and operational consequences organizations face when evidence preservation falls below reconstruction-grade thresholds.

## How this standard emerged

This standard was not written from theory. It was extracted from implementation.

[Cloudficient](https://www.cloudficient.com) was founded in 2017 by the team behind Quadrotech, an enterprise cloud migration company later [acquired by Quest Software](https://www.quest.com). Decades of moving and governing unstructured data at enterprise scale across Microsoft environments led to a different approach to evidence preservation — starting from how the data actually works and building forward toward defensibility. The standard codifies what years of that work revealed about what defensible preservation actually requires. It is not a product description. It is the set of measurable requirements that any preservation system should be evaluated against, regardless of vendor.

## Where it stands

Transparency about the current state matters as much as transparency about the intent.

- **The standard** is at version 0.55-draft. It is published with full text, appendices, a glossary, evaluation toolkit, and governance process.
- **Cloudficient's products** are in production at enterprise scale. Core preservation and reconstruction capabilities are operational. Coverage of emerging Microsoft 365 content types (Loop, Copilot, and others) is in active development.
- **Formal conformance evaluation** — for Cloudficient or anyone else — requires a reference dataset and evaluation process that the founding working group has not yet created. Cloudficient does not self-certify against its own standard.
- **The standard was published now**, not when everything is complete, because the industry needs the framework today. Waiting for one vendor to finish every edge case before publishing would defeat the purpose of an open standard.

## Common questions about the standard

### What is reconstruction-grade eDiscovery?

An architectural classification describing whether an evidence system can produce a reproducible, point-in-time record of collaborative cloud activity — deterministically resolving what documents existed, who was involved, what was shared, and who accessed what — grounded in preserved fact rather than inference. [Read the full concept.](concepts/reconstruction-grade-ediscovery.md)

### What is the context gap?

The structural difference between how evidence is created in collaborative cloud platforms — through hyperlinks, version histories, and evolving identity states — and what traditional eDiscovery systems can reconstruct after the fact. This gap prevents systems from deterministically answering which document version existed at the time of communication, who had access at a given moment, or what actually occurred. [Read the full concept.](concepts/context-gap-ediscovery.md)

### What is evidence reconstruction?

The ability of a system to deterministically reproduce what actors experienced in a collaborative environment at a specific point in time, grounded in preserved fact rather than post-hoc inference. Reconstruction-grade systems capture the relationships and timelines — messages, linked documents, version histories, identity states, permissions, and audit events — required to recreate events as they occurred. [Read the full concept.](concepts/evidence-reconstruction.md)

### What is identity drift?

The continuous change of a person's role, department, access rights, and organizational context over time, creating a mismatch between present-day directory snapshots and historical legal questions. When a litigation question asks who had access to a document six months ago, the current directory state may not reflect the answer. [Read the full concept.](concepts/identity-drift.md)

### What are modern attachments?

Message-level references to live repository objects — delivered via hyperlink instead of embedded file bytes — where the document continues to change after the message is sent. The message does not carry the document state it originally referenced, so the exported bytes may not be the bytes the recipient saw. [Read the full concept.](concepts/modern-attachments.md)

### How does this apply to Microsoft 365, Teams, and Slack?

These platforms operate by default on hyperlinked documents, co-authored files, evolving identity, and shared workspaces. Every standard eDiscovery collection from these environments encounters the [context gap](concepts/context-gap-ediscovery.md) — the question is whether the workflow can resolve it or whether it silently produces an incomplete record. The standard provides [measurable evaluation criteria](06-evaluation-framework.md) and a [vendor scoring worksheet](appendix-h-vendor-scoring.md) for assessing platform capabilities.

### What are the conformance levels?

The standard defines three tiers: **RG-Core** (baseline — deterministic point-in-time document resolution, stable identifier preservation, and reproducible manifests), **RG-Plus** (adds effective-dated identity reconstruction and audit-evidence ingestion), and **RG-Max** (adds accessed-version analysis, expanded artifact coverage, and advanced validation). [Read the full definition.](concepts/reconstruction-grade-ediscovery.md#conformance-levels)

---

## Questions about credibility and governance

These are the questions a skeptical evaluator should ask. We answer them directly.

### Who wrote this?

The initial draft was authored by [Peter Kozak](https://www.linkedin.com/in/peter-kozak-1b591520) (Co-founder and CTO, Cloudficient) and [Brandon D'Agostino](https://www.linkedin.com/in/bdagostino/) (VP of Product and attorney, Cloudficient) — combining infrastructure-level understanding of how Microsoft 365 data behaves at scale with direct experience in legal and evidentiary requirements.

The standard is designed to evolve beyond its initial authors through open governance and working group participation.

### Is this just a Cloudficient marketing exercise?

The standard is published under [CC BY 4.0](license.md), with full source in a [public repository](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard), a documented [governance process](governance/index.md), and open [participation paths](participate/index.md). Normative changes follow a proposal-and-review process, not internal product decisions. The text can be scrutinized, forked, and challenged by anyone.

That said — Cloudficient originated the standard, and Cloudficient benefits from the industry adopting it. Both things are true. The question is whether the requirements are sound and the process is open. Evaluate the standard on its merits.

### Does Cloudficient conform to RGR?

Cloudficient's products are built toward the standard's requirements. But formal conformance requires a reference dataset and evaluation process that does not yet exist — those are artifacts the founding working group needs to develop. Cloudficient expects to be among the first evaluated, but not by itself.

### Why should I trust a vendor-originated standard?

Many widely adopted standards originated with vendors who had direct market interest: USB (Intel and others), PDF (Adobe), OAuth (Twitter), OpenDocument (Sun Microsystems). Vendor origin is common. What matters is whether the standard is openly governed, independently evaluable, and structured so that conformance is testable rather than self-declared.

RGR is designed with that structure: published requirements, conformance tests, scoring frameworks, and a governance process that is documented from the start. Judge it by the process, not the origin.

### How is this different from existing eDiscovery frameworks?

The EDRM provides a widely adopted reference model for the eDiscovery lifecycle. RGR does not replace or compete with the EDRM. It addresses a specific gap: what "defensible preservation" means when evidence is collaborative, linked, versioned, and identity-dependent. The EDRM describes *stages* of eDiscovery. RGR defines *measurable requirements* for one of those stages — preservation and reconstruction of collaborative evidence — where the shift to cloud collaboration has created problems that existing frameworks do not specifically address.

### Can competitors use or participate in this standard?

Yes. The standard is published under CC BY 4.0. Any vendor, service provider, enterprise, law firm, or individual can use, evaluate against, extend, or contribute to the standard. Participation paths are [documented](participate/index.md) and include feedback, normative change proposals, toolkit contributions, and working group membership. Early participation interest from both established eDiscovery providers and emerging companies is already in progress.

### What if the standard evolves beyond what Cloudficient can deliver?

That is the point of an open standard. If the working group adopts requirements that exceed any single vendor's current capabilities — including Cloudficient's — those requirements stand. The standard defines targets, not a product snapshot. Conformance levels (RG-Core, RG-Plus, RG-Max) exist specifically so that partial conformance can be declared honestly.

---

<div class="rgr-hero__actions" markdown="1">
[Read the Standard](front-matter.md){ .md-button .md-button--primary }
[Evaluate a Platform](toolkit/index.md){ .md-button }
[Join the Working Group](participate/index.md){ .md-button }
</div>
