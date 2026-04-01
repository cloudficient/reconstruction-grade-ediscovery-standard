---
description: Concrete reconstruction scenarios for eDiscovery, including hyperlinked edits, identity drift, version resolution, and collaborative evidence challenges.
---

# Appendix D: Reconstruction Scenarios

The following scenarios illustrate why Reconstruction-Grade capabilities are not theoretical. They are the minimum to answer modern questions about behavior, reliance, and timing.

## D.1 Hyperlinked Attachment After-the-Fact Edits

Question:

What exact document state informed a decision communicated at time t0?

What is required to answer:
- Message timestamp (t0) and immutable message content
- Stable resolution of linked object and full version timeline
- Deterministic as-sent version selection rule
- Preserved bytes and version identifier for the resolved version

What legacy models produce:
- Current file bytes (time-shifted)
- No explicit binding between message and specific version
- Reviewer interpretation of "closest version"

What a Reconstruction-Grade record produces:
- As-sent version bytes (latest version where lastModifiedDateTime ≤ t0) with versionId
- Explicit message ↔ link ↔ file ↔ version binding exported and reproducible
- Manifest documenting resolution policy and tie-breakers

## D.2 Identity Drift and Historical Responsibility

Question:

Who was responsible for a repository during the relevant period, and who approved access?

What is required to answer:
- Effective-dated identity snapshots and change history
- Historical group membership and access assignment events
- Repository ownership and governance metadata as-of period

What legacy models produce:
- Current directory attributes substituted for historical state
- Org-chart interviews used as primary evidence
- Ambiguous mapping between person and role at the time

What a Reconstruction-Grade record produces:
- As-of identity record (department, manager, role) with provenance
- As-of group membership and access events tied to the natural person
- Defensible explanation without narrative substitution

## D.3 Permissions vs Observed Access

Question:

Did a person actually access a sensitive document during the relevant period?

What is required to answer:
- Audit evidence showing open/view/edit events and timestamps
- Correlation between audit events and preserved object identifiers
- Version timeline to determine which version was accessed

What legacy models produce:
- Permissions lists used as proxy for access
- No proof of actual behavior
- Inability to differentiate exposure from interaction

What a Reconstruction-Grade record produces:
- Observed access evidence ("who saw what, when") correlated to the preserved object
- Accessed-version analysis tied to preserved version identifiers
- Clear separation of potential access vs observed interaction

## D.4 Broken Links, Redirects, and File Moves

Question:

Can you still produce the evidence when links change or objects move?

What is required to answer:
- Canonicalization of sharing links and redirects
- Stable platform identifiers (siteId/driveId/itemId/versionId)
- Evidence of resolution at ingest time plus re-resolution capability

What legacy models produce:
- Brittle URL-based capture that breaks on rename/move
- Silent failures where linked content is not collected
- No record of what was attempted or why it failed

What a Reconstruction-Grade record produces:
- Stable resolution independent of URL changes using platform IDs
- Structured exception records when resolution fails, with reason codes and retries
- Deterministic end state and auditability for every link

## D.5 Cross-Custodian Link Expiry

Question:

Can your workflow detect and preserve linked content that resides in a non-custodian's storage before retention expiry destroys it?

Scenario:

User B sends User A an email containing a hyperlink to a document in B's OneDrive. User A is later identified as a custodian and placed on legal hold. User B is not a custodian and is not placed on hold. The document in B's OneDrive reaches its retention limit and is permanently purged.

What is required to answer:
- Detection that the preserved email contains a hyperlink to content outside the current hold scope
- Identification that the link target resides in same-tenant storage under a different retention policy
- Collection and preservation of the specific linked object before retention expiry
- Structured exception record if the content has already expired or cannot be collected

What legacy models produce:
- The email in A's mailbox is preserved with the hyperlink intact
- The hold system does not parse, resolve, or traverse the hyperlink
- No mechanism alerts legal teams that linked content is outside hold scope
- The document expires silently; the preserved email contains a dead link
- No exception record is generated because the system was unaware of the dependency

What a Reconstruction-Grade record produces:
- Detection at preservation time that the hyperlink targets same-tenant content outside the active hold scope
- Collection and preservation of the specific linked document (at the version contemporaneous to the message) without expanding custodian hold scope to the content owner
- Structured exception record if the target has already expired, documenting the gap with original reference, reason code, and timestamps
- Explicit message ↔ link ↔ file binding preserved regardless of whether the content owner is a custodian

Implementation note: The architecturally correct response is targeted object collection (collect-to-preserve), not custodian hold expansion. A conforming system collects the specific linked document without placing the content owner on litigation hold. Cascading custodian-scoped holds to follow hyperlinks creates an unbounded scope expansion problem — in a large organization, two hops of link traversal can place a significant fraction of the tenant on hold. Collect-to-preserve operates at the evidence relationship level, preserving the specific artifact without affecting the content owner's custodian status or storage.

## D.6 Export Reproducibility Under Scrutiny

Question:

Can you reproduce the same export later and defend chain-of-custody?

What is required to answer:
- Immutable scope definition and decision ledger
- Export manifest with counts, hashes, tool versions, and exceptions
- Resumable export mechanism with full audit trail

What legacy models produce:
- Ad hoc exports that depend on current state and operator judgement
- Missing manifests or incomplete hashing
- Inability to explain discrepancies across export attempts

What a Reconstruction-Grade record produces:
- Reproducible exports with matching manifests and hash evidence
- Full audit trail for scope decisions and exceptions
- Integrity verification and referential integrity checks
