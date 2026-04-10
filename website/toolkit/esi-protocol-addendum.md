---
description: "Starter ESI protocol language for modern collaborative evidence, with tier-labeled provisions spanning RG-Aware through RG-Plus — conformance declaration, structured adoption, as-sent versioning, relationship overlays, exception handling, export manifests, and audit bounds."
---

# ESI Protocol Addendum — Starter Language

!!! warning "Non‑Normative"
    This page is **non‑normative** and is **not legal advice**.
    The language below is **starter text only** — a starting point for attorneys
    drafting ESI protocols that address modern collaborative evidence.
    **Consult qualified counsel. Adapt to your jurisdiction, governing rules, and case‑specific requirements.**

---

## Purpose

Traditional ESI protocols often assume static files attached to emails. Modern collaboration platforms (Microsoft 365, Google Workspace, Slack, etc.) produce evidence that is **dynamic, linked, versioned, and relationship‑dependent**.

This addendum provides sample protocol language aligned with the [Reconstruction‑Grade eDiscovery Standard](../index.md). The language is organized around the standard's conformance architecture so drafters can select provisions matching the producing party's current capability:

1. Conformance tier declaration
2. Structured adoption at the RG‑Aware tier (collect, disclose, exceptions, document)
3. As‑sent version resolution (RG‑Core)
4. Relationship overlay preservation (RG‑Core)
5. Exception overlay requirements (RG‑Aware minimum / RG‑Core complete)
6. Export manifest and hash requirements (RG‑Core)
7. Audit evidence boundedness (RG‑Plus)

!!! note "How to use this addendum"
    Each sample provision is labeled with the Reconstruction‑Grade conformance tier at which it becomes applicable. The Conformance Declaration clause (§ 1) is appropriate regardless of tier. The Structured Adoption clause (§ 2) establishes the minimum posture for producing parties operating at RG‑Aware, and remains applicable at higher tiers as a default fallback rule. Provisions § 3 through § 6 apply at RG‑Core and above. Provision § 7 applies at RG‑Plus and above. Drafters should include the provisions that match the producing party's declared tier plus any provisions the parties agree to pursue as a matter of case‑specific negotiation.

---

## Sample protocol provisions

### 1. Conformance tier declaration

> The Producing Party shall identify the Reconstruction‑Grade conformance tier at which its preservation and production workflow is currently operating for the data sources within scope — **RG‑Aware** (adoption tier), **RG‑Core** (baseline), **RG‑Plus** (identity and behavior), or **RG‑Max** (expanded reconstruction depth) — and shall disclose any known capability gaps relative to the next tier.
>
> The declared tier identifies which of the following provisions apply as minimum obligations under this Protocol. A declaration of RG‑Aware invokes the obligations set forth in § 2 (Structured Adoption). A declaration of RG‑Core or above invokes the obligations set forth in § 3 through § 6. A declaration of RG‑Plus or above also invokes the obligations set forth in § 7.
>
> A declaration at a given tier does not excuse the Producing Party from reasonable steps to preserve, collect, search, and produce responsive content under applicable rules of procedure.

### 2. Structured adoption (RG‑Aware)

> Where the Producing Party cannot achieve deterministic as‑sent version resolution for modern attachments or hyperlinked content, the Producing Party shall nevertheless:
>
> (a) **Collect** hyperlinked and modern attachment content from same‑tenant storage identified during preservation workflows, rather than limiting collection to the custodian container. Where the As‑Sent Version cannot be deterministically resolved, the earliest available version shall be collected with a notation of the determination gap;
>
> (b) **Disclose**, through this Protocol or at a Rule 26(f) conference (or equivalent), (i) whether the preservation workflow identifies linked content residing outside the custodian container, and (ii) whether collected versions of linked content can be verified as contemporaneous to the referring communication;
>
> (c) **Generate structured Exception Records** under § 5 (Exception Overlay) when linked content within scope cannot be collected, rather than allowing silent omission; and
>
> (d) **Document** known preservation and context gaps at the matter level, including the categories of linked content, audit evidence, or identity state that are not preserved for the matter.
>
> The foregoing does not constitute Reconstruction‑Grade conformance. It establishes a transparent minimum posture consistent with reasonable steps obligations under the applicable rules of procedure. The collection obligation in § 2(a) is not conditioned on the parent communication being independently responsive — linked content within scope shall be collected and searched on its own terms.

### 3. As‑sent version resolution (RG‑Core)

> For any electronically stored information that includes modern attachments, cloud links, or embedded references to shared documents, a Producing Party operating at RG‑Core or above shall preserve and produce the version of the linked or referenced document whose last‑modified timestamp is less than or equal to the timestamp of the referring communication (the "As‑Sent Version").
>
> Where the As‑Sent Version cannot be deterministically resolved, the Producing Party shall document the reason and apply the fallback rule set forth in § 2(a) (Structured Adoption).

### 4. Relationship overlay (RG‑Core)

> The Producing Party shall produce a relationship overlay (or equivalent structured metadata) that preserves the explicit parent–child and sibling relationships between communications and their referenced objects, including but not limited to:
>
> - Message → linked document (with version identifier)
> - Message → modern attachment
> - Document → version history entries
>
> Relationship data shall use stable platform identifiers (e.g., siteId, driveId, itemId) rather than URLs alone.

### 5. Exception overlay (RG‑Aware minimum / RG‑Core complete)

> For any item within the agreed scope that cannot be fully preserved or produced, the Producing Party shall generate an exception record that includes:
>
> - The item's stable identifier (or best available reference)
> - A structured reason code (e.g., permission denied, throttled, deleted, unavailable)
> - Retry history (number of attempts, timestamps, outcomes)
> - A deterministic end‑state classification (succeeded, failed‑permanent, failed‑transient)
>
> Silent omission of in‑scope items (i.e., items dropped without a corresponding exception record) is not acceptable. This provision applies at RG‑Aware as the minimum exception‑handling obligation; deterministic end‑state classification is required at RG‑Core and above.

### 6. Export manifest and hashes (RG‑Core)

> Each production shall be accompanied by an export manifest that includes, at minimum:
>
> - Manifest identifier and generation timestamp
> - Scope definition reference
> - Item counts (parent items, child items, versions, relationships, exceptions)
> - Cryptographic hash algorithm and per‑item hashes
> - Tool and schema version used
>
> See [Appendix C — Export Manifest](../appendix-c-export-manifest.md) for the full recommended field set.

### 7. Audit evidence boundedness (RG‑Plus)

> Where audit log evidence is produced or relied upon to support claims about user behavior (e.g., "who viewed this document"), the Producing Party shall:
>
> - Identify the audit data sources and their coverage windows
> - Explicitly differentiate **potential access** (based on permissions) from **observed access** (based on audit records)
> - State the bounds of audit coverage (e.g., "audit logs available from date X; events before date X are not covered")
> - **Not infer** behavior beyond what the audit evidence supports

---

## Definitions Schedule

!!! note "How to use this section"
    Copy the definitions below into your ESI protocol as a "Definitions" exhibit or schedule. Definitions are alphabetical. Adapt bracketed placeholders and cross‑references to match your protocol's numbering and jurisdiction.

The following terms have the meanings set forth below when used in this Protocol and its exhibits:

**"As‑Sent Version"** means, with respect to any communication that includes a cloud link, embedded reference, or shared‑document reference, the version of the linked or referenced document whose last‑modified timestamp is less than or equal to the timestamp of the referring communication. Where the As‑Sent Version cannot be deterministically resolved, the fallback rule set forth in § [__] (Structured Adoption) shall apply.

**"Audit Coverage Window"** means the period of time for which Audit Evidence is available and from which factual assertions about user behavior may be drawn. Events falling outside the Audit Coverage Window shall not be asserted as observed facts without additional evidentiary support.

**"Audit Evidence"** means records generated by a platform's audit subsystem that document discrete events (e.g., file viewed, file downloaded, permission changed, message sent) at the level of individual user actions, as distinguished from permission or configuration state alone.

**"Conformance Tier"** means one of the Reconstruction‑Grade conformance classifications defined in Section 6.2 of the Standard: (a) **RG‑Aware** — a pre‑conformance adoption tier requiring structured collection of linked content, Limitation Disclosure, structured exception generation, and matter‑level documentation of gaps, but not deterministic reconstruction; (b) **RG‑Core** — the baseline Reconstruction‑Grade conformance level requiring deterministic as‑sent version resolution, stable identifier preservation, relationship integrity, deterministic exception handling, and reproducible export manifests; (c) **RG‑Plus** — RG‑Core plus effective‑dated identity reconstruction and audit‑evidence ingestion and correlation with explicit coverage bounds; and (d) **RG‑Max** — RG‑Plus plus accessed‑version analysis, expanded artifact coverage, and advanced validation. A declaration of RG‑Aware does not constitute Reconstruction‑Grade conformance.

**"Deterministic End‑State Classification"** means a classification assigned to each exception record indicating whether the preservation or production attempt for an item reached a definitive conclusion: (a) **Succeeded** — item was fully captured; (b) **Failed‑Permanent** — item cannot be captured due to a condition that will not resolve (e.g., item permanently deleted, access permanently denied); or (c) **Failed‑Transient** — item was not captured due to a condition that may be retryable (e.g., service throttling, temporary unavailability).

**"ESI"** has the meaning given under the applicable rules of procedure (e.g., Fed. R. Civ. P. 34(a)(1)(A) or equivalent) and includes, without limitation, all documents, data, and metadata stored in or generated by modern collaboration platforms.

**"Exception Record"** means a structured record generated for any in‑scope item that could not be fully preserved or produced, containing at minimum: (a) the item's stable platform identifier or best available reference; (b) a reason code drawn from a defined taxonomy; (c) retry history; and (d) a Deterministic End‑State Classification. Silent omission — i.e., dropping an in‑scope item without a corresponding Exception Record — is not acceptable.

**"Export Manifest"** means a structured artifact produced alongside each production that documents: (a) a manifest identifier and generation timestamp; (b) the Scope Definition used; (c) item counts by type (parent items, child items, versions, relationships, exceptions); (d) the cryptographic hash algorithm applied and per‑item hash values; and (e) the tool name and schema version used to generate the production. The Export Manifest serves as the chain‑of‑custody record for the production.

**"Limitation Disclosure"** means the structured acknowledgment required under § [__] (Structured Adoption) identifying: (a) whether the Producing Party's preservation workflow can identify linked content residing outside the custodian container; (b) whether collected versions of linked content can be verified as contemporaneous to the referring communication; and (c) any known categories of linked content, Audit Evidence, or identity state that are not preserved for the matter.

**"Modern Attachment"** means content referenced or shared within a communication through a cloud link, inline preview, or embedded reference to a file stored on a shared platform, as distinguished from a traditional file attachment transmitted as a binary payload within the communication itself.

**"Observed Access"** means access to a document or resource that is documented by a specific Audit Evidence record indicating an affirmative user action (e.g., a view or download event). Observed Access shall not be inferred from permissions or from the absence of evidence alone.

**"Potential Access"** means access to a document or resource that a user could have obtained based on their permissions or role at a given point in time, without regard to whether access was actually exercised. Potential Access shall be clearly distinguished from Observed Access in any assertion about user behavior.

**"Producing Party"** means the party obligated under this Protocol or applicable rules to preserve, collect, process, and produce ESI.

**"Reconstruction‑Grade eDiscovery Standard" or "RGR"** means the open architectural standard published at [https://github.com/cloudficient/reconstruction-grade-ediscovery-standard](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard) that defines an adoption tier (RG‑Aware) and three conformance levels (RG‑Core, RG‑Plus, RG‑Max) for preserving modern collaborative evidence with point‑in‑time fidelity. References to a specific version (e.g., v0.54‑draft) mean that edition of the standard.

**"Relationship Overlay"** means a structured metadata artifact that maps explicit parent–child and sibling relationships between communications and their associated objects, including: (a) message → linked document (with version identifier); (b) message → Modern Attachment; and (c) document → version history entries. A Relationship Overlay uses Stable Platform Identifiers rather than display names or URLs alone.

**"Scope Definition"** means the agreed written description of the custodians, date ranges, data sources, and subject‑matter filters that define what ESI is subject to preservation and production obligations under this Protocol.

**"Stable Platform Identifier"** means a persistent, non‑display identifier assigned by a collaboration platform to uniquely reference an object (e.g., a file, site, or drive) independently of its display name, URL path, or sharing link. Examples include siteId, driveId, and itemId in Microsoft 365; fileId in Google Drive; and equivalent identifiers in other platforms.

---

## Adaptation notes

- **Tier selection:** Start with the Conformance Declaration (§ 1). If the producing party cannot yet meet § 3 through § 6 in full, begin with § 2 (RG‑Aware) and document a maturity path toward RG‑Core. Advancement through tiers should be negotiated in good faith as tooling and operational capabilities develop.
- **Jurisdiction:** Adapt terminology to local rules (e.g., Federal Rules of Civil Procedure, state rules, or foreign equivalents).
- **Proportionality:** These provisions may be narrowed or expanded based on proportionality considerations under applicable rules.
- **Platform specifics:** Consider adding platform‑specific schedules if the matter involves multiple collaboration environments.
- **Agreed format:** Coordinate with opposing counsel on load‑file formats, relationship overlay schemas, and exception record structures.

---

## See also

- [Section 3 — Defining Reconstruction‑Grade eDiscovery](../03-defining-reconstruction-grade.md)
- [Section 4 — The Preservation System of Record](../04-preservation-system-of-record.md)
- [Section 6.2 — Conformance Levels](../06-evaluation-framework.md#62-conformance-levels)
- [Appendix B — Reconstruction‑Grade Requirements](../appendix-b-requirements.md)
- [Appendix C — Export Manifest](../appendix-c-export-manifest.md)
- [Appendix J — Exception Taxonomy](../appendix-j-exception-taxonomy.md)
