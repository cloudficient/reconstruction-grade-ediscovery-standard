# RFP Clause Pack

!!! warning "Non‑Normative"
    This page is **non‑normative** and is **not legal advice**.
    These sample clauses are starting points for procurement and outside counsel.
    Adapt to your organization's requirements, jurisdiction, and contracting standards.
    Consult qualified counsel before incorporating into binding agreements.

---

## Purpose

These clauses help enterprises require **Reconstruction‑Grade conformance** when evaluating preservation, collection, and processing vendors. They are derived from the [Evaluation Framework (Section 6)](../06-evaluation-framework.md) and [Requirements (Appendix B)](../appendix-b-requirements.md).

---

## Sample RFP clauses

### 1. Declared conformance level

> Vendor SHALL declare which Reconstruction‑Grade conformance level (RG‑Core, RG‑Plus, or RG‑Max) the proposed system satisfies, as defined in the Reconstruction‑Grade eDiscovery Standard, [Section 6.2](../06-evaluation-framework.md#62-conformance-levels) and [Appendix B, Section B.0](../appendix-b-requirements.md#b0-conformance-levels).
>
> Vendor SHALL identify any requirements within the declared level that are not fully satisfied, with documented rationale.

### 2. Conformance test demonstration

> Vendor SHALL demonstrate conformance by executing controlled tests T‑01 through T‑07 as defined in [Section 6.3](../06-evaluation-framework.md#63-minimum-conformance-tests) of the standard, using representative data from the Buyer's environment or an agreed substitute.
>
> Test results SHALL be documented and made available for review prior to contract execution.

### 3. Explicit exception handling

> The system SHALL produce structured, reason‑coded exception records for every evidence item that cannot be fully preserved, including retry history and deterministic end‑state classification.
>
> Silent evidence drops (items omitted without a corresponding exception record) SHALL be treated as non‑conformant.

### 4. Reproducible exports with manifests and hashes

> Exports SHALL be reproducible: re‑running the same scope definition SHALL produce the same set of items with matching cryptographic hashes and a complete export manifest as described in [Appendix C](../appendix-c-export-manifest.md).
>
> The manifest SHALL include scope parameters, item counts, exception summaries, hash algorithm, and tool version.

### 5. As‑sent version resolution

> For modern attachments and linked content, the system SHALL resolve and export the document version whose `lastModifiedDateTime` is ≤ the referring message's timestamp (the "as‑sent" version).

### 6. Identity and audit evidence (if RG‑Plus or higher)

> If the Buyer requires RG‑Plus conformance, the Vendor SHALL demonstrate effective‑dated identity reconstruction and audit‑evidence correlation with explicit coverage bounds.

---

## Scoring guidance

Use [Appendix H — Vendor Scoring Worksheet](../appendix-h-vendor-scoring.md) to evaluate responses against these clauses. A simple scoring approach:

| Rating | Meaning |
|---|---|
| **Full** | Requirement met; demonstrated with evidence |
| **Partial** | Requirement partially met; gaps documented |
| **Not met** | Requirement not satisfied |
| **N/A** | Not applicable to declared conformance level |

---

## See also

- [Buyer Checklist](buyer-checklist.md) — 10 essential questions
- [Appendix G — Questions to Ask Vendors](../appendix-g-vendor-questions.md) — detailed question set
- [Conformance Declaration Template](conformance-declaration-template.md) — template for vendor self‑declaration
