---
description: Export manifest specification and chain-of-custody profile for reconstruction-grade eDiscovery, ensuring reproducible evidentiary transactions and audit trails.
---

# Appendix C: Export Manifest and Chain-of-Custody Profile

A Reconstruction-Grade export is not merely a file transfer. It is a reproducible evidentiary transaction. The manifest is the bridge between scope definition and downstream defensibility.

Table 8. Example export manifest fields

| Field | Purpose |
| --- | --- |
| ManifestId | Unique identifier for the export job and its manifest artifact. |
| GeneratedAt (UTC) | Timestamp when the export package was assembled. |
| ScopeDefinitionId | Identifier referencing the immutable scope definition (custodians, repositories, time bounds, queries). |
| ScopeParameters | Human-readable summary of scope parameters (matter identifier, date range, filters). |
| SourceWorkloads | Workloads included (e.g., Exchange, Teams, SharePoint, OneDrive) and their coverage windows. |
| ResolutionPolicy | Document state resolution policy (as-sent rule, tie-breakers, fallback rules). |
| HashAlgorithm | Hash algorithm used for files and records (e.g., SHA-256). |
| ExportProfile | Export schema profile used (load file formats, relationship representation). |
| Counts | Counts of exported parent items, child items, versions, relationship records, audit records. |
| ExceptionsSummary | Counts by reason code; list of high-severity gaps; pointer to exception overlay. |
| ToolVersion | Tool and schema versions used to generate export (supports reproducibility). |
| Operator | Actor identity who initiated the export and approvals (if applicable). |
| IntegrityChecks | Results of referential integrity checks and hash verification. |
| ReproducibilityNotes | Notes required to reproduce (queries, paging tokens, snapshot identifiers). |

Export packages SHOULD include the manifest as a signed or otherwise integrity-protected artifact alongside the native files and load/overlay files.
