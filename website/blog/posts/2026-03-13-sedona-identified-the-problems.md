---
date: 2026-03-13
draft: false
authors:
  - peterkozak
categories:
  - Industry Analysis
tags:
  - eDiscovery
  - Sedona Conference
  - Collaboration Platforms
  - Reconstruction-Grade
---

# Sedona Identified the Problems. Here's the Architectural Answer.

*A reconstruction-grade response to The Sedona Conference's Commentary on Discovery Implications of Collaboration Platforms (October 2025)*

In October 2025, The Sedona Conference published what may be the most comprehensive analysis of why modern collaboration platforms are breaking traditional e-discovery. For each challenge it identifies, the RGR Standard offers an architectural answer.

<!-- more -->

## The Diagnosis

The *Commentary on Discovery Implications of Collaboration Platforms* catalogs — with extensive case law — the conceptual, technical, and practical challenges that arise when litigation meets Teams, Slack, and Google Workspace.

It is essential reading. Every practitioner dealing with collaborative evidence should study it closely.

But the Commentary is, by design, diagnostic. It identifies the problems. It proposes that parties discuss, negotiate, and improvise solutions on a case-by-case basis. It acknowledges that current tools often cannot do what courts expect. And it leaves a fundamental question unanswered:

**What would it actually look like to solve these problems architecturally, rather than procedurally?**

That's the question the Reconstruction-Grade eDiscovery Standard attempts to answer.

## Problem by Problem, Section by Section

What follows is not a critique of the Sedona Commentary — it's a response. For each challenge the Commentary identifies, we map the corresponding requirement from the RGR Standard (v0.51-draft) that addresses it.

---

### 1. "Not Every Document Is a Document"

**Sedona says:** Content on collaboration platforms may be structured data stored as JSON, rendered in real time. A document's history may be stored in timestamped name/value pairs. Each platform has its own unique process for storing data.

**The RGR Standard requires:** Deterministic version resolution (Section 3.3). Systems MUST resolve document state as-of an event timestamp — selecting the latest version where `lastModifiedDateTime <= message timestamp`. Version lineage is treated as evidentiary (Section 1.3), not as metadata to be discarded. File versions must be enumerated and preserved with stable identifiers, timestamps, and bytes.

**The shift:** From "collect what exists now" to "reconstruct what existed then."

---

### 2. Hyperlinks Are Not Attachments — But They Still Need to Be Evidence

**Sedona says:** Hyperlinked documents are stored outside the communication, may change over time, and matching the as-sent version to the message containing the hyperlink "can be difficult or impossible." Courts have limited parties to manually searching 200 hyperlinks as a proportionality compromise.

**The RGR Standard requires:** Explicit preservation of the Message-Link-File-Version relationship chain (Section 3.5). Export formats must include ParentId/ChildId relationship fields with typed bindings distinguishing modern attachments from hyperlinks. The "as-sent version" is formally defined (Section 3.2) as "the file version that existed at the time a communication was sent, deterministically resolved." Broken or unresolvable links generate structured exception records (Section 3.7) — never silent gaps.

**The shift:** From "try to find the right version manually" to "the system resolves it deterministically or tells you exactly why it couldn't."

---

### 3. The Custodian Model Doesn't Map to Shared Workspaces

**Sedona says:** Collaboration platforms are typically noncustodial sources. The traditional notion of a custodian may be inapplicable. Information may not relate to or be identified with a single individual.

**The RGR Standard requires:** Effective-dated identity tied to natural persons (Section 1.4, Section 3.1). People change roles, teams, access rights, and responsibilities. The standard models individuals independently of transient directory identifiers — preserving historical snapshots of role, department, manager, status, and group membership as-of specific dates. This isn't about abandoning custodians. It's about grounding identity in temporal reality.

**The shift:** From "custodians are static containers" to "natural persons with effective-dated identity."

---

### 4. Collection Is Fragmented Across Platforms and Applications

**Sedona says:** Data may be stored across SharePoint, OneDrive, Google Drive, document management systems, and external sources. Commercial tools may have limited capability, and APIs present their own challenges. The ability to collect may depend on license level.

**The RGR Standard requires:** A Collect-to-Preserve architecture (Section 5.2) with matter-scoped preservation into a dedicated system of record. Stable platform-native identifiers (Section 3.4) — siteId, driveId, itemId — must be preserved because URLs change. A single preserved object may have multiple contextual bindings without collapsing events (Section 4.3). Enterprise-scale constraints — API throttling, version proliferation, permission boundaries, audit retention windows — are explicitly addressed (Section 5.3) rather than treated as surprises.

**The shift:** From "hope the tools can handle it" to "architect for the constraints from the start."

---

### 5. Evidence Scattered Across Platforms Loses Its Relationships

**Sedona says:** Collaboration platforms operate as portals to other applications. Users may not realize documents are stored in separate systems. Communications may move across platforms mid-conversation.

**The RGR Standard requires:** Relationship integrity across platform boundaries (Appendix B, RGR-RL). Every exported record must have stable, unique identifiers supporting referential integrity (RGR-RL-007). The standard mandates preserving one authoritative object while retaining all contextual bindings (Section 4.3): "Deduplicating the bytes can be operationally correct. However, collapsing the events — who shared, where, when, which version — destroys context."

**The shift:** From "deduplicate everything" to "preserve once, bind many."

---

### 6. Authentication and Evidentiary Trustworthiness

**Sedona says:** Multiple users viewing and editing simultaneously complicates authentication. It may be difficult to identify the best person to authenticate a document or establish hearsay exceptions. Versioning makes it hard to confirm what was shared.

**The RGR Standard requires:** Reproducible exports with evidence manifests (Section 3.8) — the same scope and parameters generate the same outputs, with chain-of-custody support. Audit evidence is treated as first-class (Section 3.6): the standard explicitly distinguishes potential access (permissions) from observed access (audit logs). Systems MUST NOT substitute permission-based inference as a factual claim when audit evidence is unavailable. Immutability and auditability (Section 4.4) extend to workflow-level audit trails for scope decisions and exception handling.

**The shift:** From "inference is good enough" to "inference is not defensibility."

---

## What Comes Next

The Sedona Conference Commentary is a signal that the industry recognizes these challenges are real, pervasive, and growing. The Reconstruction-Grade eDiscovery Standard is an attempt to move from recognition to architecture — with testable, vendor-neutral conformance requirements that any platform, tool, or service provider can be measured against.

The public draft (v0.51) is available at [rgrstandard.org](https://rgrstandard.org). We welcome review, critique, and collaboration from the e-discovery community — including the Sedona Working Group members whose diagnostic work made the need so clear.
