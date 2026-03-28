---
description: Definition of reconstruction-grade eDiscovery, the three-pillar evidence model, and conformance levels for reproducible point-in-time evidence collection.
---

# 3. Defining Reconstruction-Grade eDiscovery

Reconstruction-Grade eDiscovery is an architectural classification. It describes whether an evidence system can produce a reproducible, point-in-time record of collaborative activity without relying on hindsight or inference.

Normative language: This document uses MUST, SHOULD, and MAY in their standards sense (see Section 0.4).

## 3.1 The Reconstruction-Grade Evidence Model

A Reconstruction-Grade evidentiary record is constructed from three pillars. Weaknesses in any pillar forces downstream inference.

Identity over time: Authoritative, effective-dated identity correlated to a natural person (role, department, manager, status, group membership).

Behavior and activity evidence: Audit and activity records treated as evidence to establish interaction (view, edit, share, access) and timing - explicitly bounded by availability and retention.

Document state and relationships: Deterministic point-in-time file resolution and explicit message ↔ link ↔ file ↔ version bindings preserved using stable identifiers and lineage metadata.

**Figure 3 — Evidence Graph: Objects and Relationships Preserved for Reconstruction**

![Evidence Graph: Reconstruction requires objects, relationships, and timelines to be preserved as a coherent record](images/evidence-graph-objects-relationships.png)

## 3.2 Key Definitions

Modern attachment / Hyperlinked file - A message-level reference to a repository object (typically via hyperlink or platform-managed pointer) where the bytes are not embedded in the message.

As-sent version - The file version that existed at the time a communication was sent; deterministically resolved as the latest version whose lastModifiedDateTime is not later than the message timestamp.

Accessed version - The file version that a specific actor actually opened or interacted with, derived from audit evidence where available and correlated to preserved version timelines. If audit evidence is unavailable or out of retention, the accessed-version claim MUST be represented as unknown rather than inferred.

Evidence graph - A structured record linking people, identities, events, artifacts, versions, and audit signals with stable identifiers and timestamps.

Deterministic end state - A processing outcome in which every discovered reference either resolves to preserved content or results in a structured exception record with traceable reasons and retry history.

## 3.3 Deterministic Version Resolution

Reconstruction-Grade systems MUST be able to resolve document state as-of an event timestamp deterministically. For modern attachments, the event timestamp is typically the send time of the message containing the link.

A minimal deterministic selection rule is:

- Enumerate all available versions and their timestamps for the referenced object.
- Select the latest version where lastModifiedDateTime ≤ message timestamp.
- If multiple versions share the same timestamp, select the highest version identifier under a deterministic ordering.
- If version history is unavailable or incomplete, record the applied fallback rule and outcome explicitly.

## 3.4 Stable Identifiers and Canonicalization

Because URLs can change (sharing links, redirects, file moves), Reconstruction-Grade systems MUST preserve stable platform-native identifiers sufficient to re-resolve content over time.

At minimum, where applicable, systems MUST persist:

- siteId
- driveId
- itemId
- listItemUniqueId
- versionId

Canonicalized SharePoint/OneDrive URLs (as an aid, not as the primary key)

## 3.5 Relationship Preservation: Message ↔ Link ↔ File ↔ Version

Relationships are evidentiary. If relationships are lost or collapsed during processing, the record can no longer explain reliance and transmission. Reconstruction-Grade systems MUST preserve explicit parent-child relationship mappings between communications and referenced objects.

Recommended export representations include ParentId/ChildId relationship fields with RelationshipType values that distinguish modern attachments, hyperlinks, embedded objects, and other bindings.

## 3.6 Audit Evidence and the Access Question

Reconstruction-Grade practice distinguishes between:

- Potential access (permissions and sharing configuration), and
- Observed access (behavioral evidence from audit logs where available).

Permissions describe what could have happened; they do not prove what did happen. Where audit logs exist, systems SHOULD ingest them, treat them as evidence, and correlate them to preserved objects and version timelines to support defensible answers to "who saw what, when."

Boundedness requirement: Because audit coverage is dependent on upstream availability, licensing, and retention windows, a Reconstruction-Grade system MUST represent audit-based claims with explicit coverage bounds. If audit evidence does not exist for the relevant timeframe, the system MUST represent observed access as unknown and MUST NOT substitute permission-based inference as a factual claim.

## 3.7 Deterministic Exception Records

Not every referenced object can be collected. Reconstruction-Grade systems MUST make this explicit rather than silent.

A structured exception record SHOULD include:

- Original link reference as extracted from the parent communication
- Normalized reason code (permission denied, item deleted/outside retention, throttling, transient service error, unknown)
- Complete retry history (attempt count, outcomes, timestamps)
- Association to the parent communication and to the attempted target identifiers

## 3.8 Reproducible Exports and Evidence Manifests

Reconstruction-Grade systems MUST support reproducible exports. The same scope definition and parameters should generate the same outputs, with manifests that support chain-of-custody and defensibility.

A Reconstruction-Grade export package SHOULD include:

- Native files and communications
- Standard load/overlay files (e.g., DAT/CSV) containing metadata, relationship identifiers, provenance fields, and hashes
- An export manifest capturing counts, scope queries, time ranges, tool versions, exceptions, and retry outcomes
- Resumable export jobs with full auditability
