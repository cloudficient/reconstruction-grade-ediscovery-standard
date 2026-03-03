# ESI Protocol Addendum — Starter Language

!!! warning "Non‑Normative"
    This page is **non‑normative** and is **not legal advice**.
    The language below is **starter text only** — a starting point for attorneys
    drafting ESI protocols that address modern collaborative evidence.
    **Consult qualified counsel. Adapt to your jurisdiction, governing rules, and case‑specific requirements.**

---

## Purpose

Traditional ESI protocols often assume static files attached to emails. Modern collaboration platforms (Microsoft 365, Google Workspace, Slack, etc.) produce evidence that is **dynamic, linked, versioned, and relationship‑dependent**.

This addendum provides sample protocol language aligned with the [Reconstruction‑Grade eDiscovery Standard](../index.md) to address:

1. As‑sent version resolution
2. Relationship overlay preservation
3. Exception overlay requirements
4. Export manifest and hash requirements
5. Audit evidence boundedness

---

## Sample protocol provisions

### 1. As‑sent version resolution

> For any electronically stored information that includes modern attachments, cloud links, or embedded references to shared documents, the Producing Party shall preserve and produce the version of the linked or referenced document whose last‑modified timestamp is less than or equal to the timestamp of the referring communication (the "as‑sent version").
>
> Where the as‑sent version cannot be determined, the Producing Party shall document the reason and produce the earliest available version with a notation.

### 2. Relationship overlay

> The Producing Party shall produce a relationship overlay (or equivalent structured metadata) that preserves the explicit parent–child and sibling relationships between communications and their referenced objects, including but not limited to:
>
> - Message → linked document (with version identifier)
> - Message → modern attachment
> - Document → version history entries
>
> Relationship data shall use stable platform identifiers (e.g., siteId, driveId, itemId) rather than URLs alone.

### 3. Exception overlay

> For any item within the agreed scope that cannot be fully preserved or produced, the Producing Party shall generate an exception record that includes:
>
> - The item's stable identifier (or best available reference)
> - A structured reason code (e.g., permission denied, throttled, deleted, unavailable)
> - Retry history (number of attempts, timestamps, outcomes)
> - A deterministic end‑state classification (succeeded, failed‑permanent, failed‑transient)
>
> Silent omission of in‑scope items (i.e., items dropped without a corresponding exception record) is not acceptable.

### 4. Export manifest and hashes

> Each production shall be accompanied by an export manifest that includes, at minimum:
>
> - Manifest identifier and generation timestamp
> - Scope definition reference
> - Item counts (parent items, child items, versions, relationships, exceptions)
> - Cryptographic hash algorithm and per‑item hashes
> - Tool and schema version used
>
> See [Appendix C — Export Manifest](../appendix-c-export-manifest.md) for the full recommended field set.

### 5. Audit evidence boundedness

> Where audit log evidence is produced or relied upon to support claims about user behavior (e.g., "who viewed this document"), the Producing Party shall:
>
> - Identify the audit data sources and their coverage windows
> - Explicitly differentiate **potential access** (based on permissions) from **observed access** (based on audit records)
> - State the bounds of audit coverage (e.g., "audit logs available from date X; events before date X are not covered")
> - **Not infer** behavior beyond what the audit evidence supports

---

## Adaptation notes

- **Jurisdiction:** Adapt terminology to local rules (e.g., Federal Rules of Civil Procedure, state rules, or foreign equivalents).
- **Proportionality:** These provisions may be narrowed or expanded based on proportionality considerations under applicable rules.
- **Platform specifics:** Consider adding platform‑specific schedules if the matter involves multiple collaboration environments.
- **Agreed format:** Coordinate with opposing counsel on load‑file formats, relationship overlay schemas, and exception record structures.

---

## See also

- [Section 3 — Defining Reconstruction‑Grade eDiscovery](../03-defining-reconstruction-grade.md)
- [Section 4 — The Preservation System of Record](../04-preservation-system-of-record.md)
- [Appendix C — Export Manifest](../appendix-c-export-manifest.md)
- [Appendix J — Exception Taxonomy](../appendix-j-exception-taxonomy.md)
