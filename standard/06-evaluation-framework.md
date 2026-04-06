---
description: Measurable evaluation framework for assessing reconstruction-grade eDiscovery platforms, with scoring categories, conformance tests, and grading criteria.
---

# 6. Measurable Evaluation Framework

A new category only matters if it can be evaluated. This section provides a practical framework for assessing whether a platform is Reconstruction-Grade.

## 6.1 Evaluation Categories

Point-in-time resolution Can the system deterministically resolve document state at or before an event timestamp (e.g., message send time)?

Stable identifiers Does the system preserve platform-native IDs sufficient to re-resolve objects despite URL changes, moves, or renames?

Relationship integrity Does the system preserve explicit message ↔ link ↔ file ↔ version relationships and export them without collapsing context?

Identity over time Can the system reconstruct role, department, manager, and group membership as-of a historical date?

Behavior evidence Does the system ingest audit evidence and correlate observed interaction to preserved objects and versions, with explicit boundedness?

Deterministic exceptions Are failures explicit, reason-coded, and auditable with retry histories and deterministic end states?

Reproducible exports Are exports repeatable with manifests, hashes, and complete traceability of scope and exceptions?

## 6.2 Conformance Levels

To support incremental adoption, this document defines an adoption tier and three conformance levels.

RG-Aware (Adoption Tier — Transparency and Collection)

RG-Aware is a pre-conformance adoption tier. It does not constitute Reconstruction-Grade conformance but establishes a structured, transparent entry point for organizations that acknowledge the Preservation Gap and Context Gap and take action within their current capabilities.

An organization operating at RG-Aware:

1. Collects hyperlinked and modern attachment content from same-tenant storage when identified during preservation workflows, rather than limiting collection to the custodian container.
2. Discloses, through Rule 26(f) conferences, ESI protocols, or equivalent mechanisms, whether its preservation workflow can identify linked content outside the custodian container and whether collected versions reflect communication-time state.
3. Generates structured exception records when linked content cannot be collected (permission denied, content expired, out-of-scope storage) rather than allowing silent loss.
4. Documents known limitations explicitly in matter-level records rather than treating unpreserved linked content as a non-issue.

RG-Aware does not require deterministic as-sent version resolution (T-01), identity reconstruction, or audit correlation. It requires transparency about what is and is not preserved, and active collection of linked content within reach.

RG-Aware is intended as a transitional posture. Organizations operating at RG-Aware SHOULD establish a maturity path toward RG-Core conformance as tooling and operational capabilities develop.

RG-Core (Baseline Reconstruction-Grade) A system qualifies for RG-Core only if it satisfies deterministic point-in-time resolution, stable identifier preservation, relationship export integrity, deterministic exception handling, and reproducible export manifests.

RG-Plus (Identity + Behavior Conformance) RG-Plus adds effective-dated identity reconstruction and audit-evidence ingestion/correlation with explicit boundedness reporting.

RG-Max (Expanded Reconstruction Depth) RG-Max adds accessed-version analysis (where audit supports it), expanded artifact coverage (pages/lists/Loop/etc.), and advanced validation routines (referential integrity scoring, coverage gap alerting, and multi-profile export without semantic drift).

Enterprises may adopt RG-Aware as an immediate transparency baseline, require RG-Core as the minimum conformance target, and treat RG-Plus/RG-Max as maturity goals.

Note: Conformance levels are formally specified with full requirement mappings in Appendix B, Section B.0. The descriptions above are informative summaries. RG-Aware is specified as an adoption tier, not a conformance level; it does not carry MUST requirements from Appendix B but establishes the minimum structured adoption posture for organizations that have not yet achieved RG-Core.

## 6.3 Minimum Conformance Tests

Enterprises should require a small battery of conformance tests. Reconstruction-Grade claims should be demonstrable with controlled scenarios.

T-01 As-sent resolution Create a document with multiple versions; send a Teams/email link at t0; modify at t1; export must produce v≤t0.

T-02 Link canonicalization Use sharing links, redirect patterns, and renamed/moved objects; export must still resolve using stable IDs.

T-03 Relationship integrity Single message references multiple objects; export must preserve parent-child mappings and relationship types.

T-04 Identity as-of Change a user's department and group membership; as-of queries must reflect historical state.

T-05 Access evidence (bounded) Generate view/edit events; system must correlate audit events to objects/versions and report coverage bounds.

T-06 Exception determinism Force a permission denial; system must produce a structured exception record with retries and reason code.

T-07 Export reproducibility Run export twice; manifests and hashes must match and exceptions must be stable and explainable.
