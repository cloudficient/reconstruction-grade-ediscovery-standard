# Appendix B: Reconstruction-Grade Requirements (RGR)

This appendix defines the normative requirements for Reconstruction-Grade conformance.

A system may claim conformance only if it satisfies all MUST requirements applicable to the declared conformance level.

## B.0 Conformance Levels

To support incremental adoption while maintaining architectural rigor, this standard defines three conformance levels.

RG-Core (Baseline Reconstruction-Grade)

A system qualifies as RG-Core only if it satisfies all MUST requirements in the following domains:

Deterministic document state resolution

Stable identifier preservation

Explicit relationship preservation

Deterministic exception handling

Reproducible exports with manifest and hashes

Immutable preservation and scope ledger

RG-Core establishes deterministic reconstruction without requiring advanced identity or audit correlation.

RG-Plus (Identity + Behavior Conformance)

RG-Plus requires all RG-Core requirements plus:

Effective-dated identity reconstruction

Historical membership reconstruction (bounded by available data)

Audit ingestion and correlation

Explicit differentiation between potential access and observed access

RG-Plus enables defensible "who was responsible" and "who saw what" claims within bounded audit coverage.

RG-Max (Expanded Reconstruction Depth)

RG-Max requires RG-Plus plus:

Accessed-version correlation where audit permits

Expanded artifact coverage (pages, lists, Loop, etc.)

Referential integrity validation

Multi-profile export without semantic drift

Operational coverage metrics and gap reporting

RG-Max represents mature, enterprise-scale Reconstruction-Grade programs.

## B.1 Identity Over Time (RGR-ID)

| Code | Level | Requirement | Verification |
| --- | --- | --- | --- |
| RGR-ID-001 | RG-Plus MUST | Model individuals as natural persons independent of transient directory identifiers (e.g., UPN changes). | Demonstrate identity correlation across renames and account lifecycle changes. |
| RGR-ID-002 | RG-Plus MUST | Preserve effective-dated identity snapshots from authoritative sources and record provenance (source system, snapshot time). | Show as-of reconstruction for a user across role/department changes. |
| RGR-ID-003 | RG-Plus MUST | Support as-of queries for role, department, manager, status, and key scoping attributes. | Run queries for date X and date Y and produce differing outputs consistent with change history. |
| RGR-ID-004 | RG-Plus SHOULD | Preserve historical group membership and role-based access membership as-of specific dates. | Demonstrate group membership timeline and as-of resolution. |
| RGR-ID-005 | RG-Plus MUST | Persist identifiers required to link identity records to collaboration artifacts and retain historical mapping. | Demonstrate linkage between message actor and identity state as-of event time. |
| RGR-ID-006 | RG-Plus SHOULD | Maintain identity drift audit (UPN, display name, manager, department, employment status changes). | Produce identity change log and show reconstruction use. |
| RGR-ID-007 | RG-Core MUST | Record custodian and repository scoping decisions with timestamps and approver identifiers. | Provide immutable decision ledger entries for scope changes. |
| RGR-ID-008 | RG-Max MAY | Ingest HR and directory data to support "hidden custodian" discovery workflows. | Demonstrate behavioral signals suggesting additional actors. |

## B.2 Audit and Behavior Evidence (RGR-AU)

| Code | Level | Requirement | Verification |
| --- | --- | --- | --- |
| RGR-AU-001 | RG-Plus SHOULD | Ingest audit records relevant to collaboration behavior (view, edit, share, access) and treat them as evidence. | Demonstrate ingestion pipeline and immutability controls. |
| RGR-AU-002 | RG-Plus MUST | Correlate audit events to preserved objects using stable identifiers, not URLs. | Demonstrate correlation for moved/renamed items. |
| RGR-AU-003 | RG-Plus MUST | Preserve audit evidence with provenance (source, retrieval time, query parameters). | Provide audit ingestion manifest and reproducibility documentation. |
| RGR-AU-004 | RG-Plus SHOULD | Support audit preservation strategies aligned to retention windows to avoid context loss. | Demonstrate capture-before-expiry and coverage reporting. |
| RGR-AU-005 | RG-Plus MUST | Explicitly differentiate potential access (permissions) from observed access (audit). | Show separate fields and explainability in export. |
| RGR-AU-006 | RG-Plus MUST | Represent audit-based claims with explicit coverage bounds (time range, licensing, availability). | Demonstrate "unknown" classification when audit coverage is incomplete. |
| RGR-AU-007 | RG-Core MUST | Maintain immutable audit trail of preservation triggers and actions. | Show end-to-end chain-of-custody across preserve and export. |
| RGR-AU-008 | RG-Max SHOULD | Enable accessed-version analysis by correlating audit events to version timelines. | Demonstrate accessed-version output for controlled scenario. |

## B.3 Document State and Deterministic Resolution (RGR-DS)

| Code | Level | Requirement | Verification |
| --- | --- | --- | --- |
| RGR-DS-001 | RG-Core MUST | Preserve file bytes for each preserved version and compute cryptographic hashes. | Validate hash stability across repeated exports. |
| RGR-DS-002 | RG-Core MUST | Persist version identifiers, timestamps, and lineage metadata. | Demonstrate version list with stable IDs. |
| RGR-DS-003 | RG-Core MUST | Deterministically resolve an as-of version for modern attachments using event timestamp (latest version where lastModifiedDateTime ≤ message timestamp). | Demonstrate deterministic resolution rule. |
| RGR-DS-004 | RG-Core MUST | Apply deterministic tie-breaker when multiple versions share same timestamp. | Show consistent tie-breaker behavior. |
| RGR-DS-005 | RG-Core MUST | Record fallback rules when version history incomplete or unavailable. | Demonstrate explicit fallback documentation. |
| RGR-DS-006 | RG-Core MUST | Canonicalize and resolve sharing links and redirects to underlying repository objects. | Demonstrate resolution across redirect scenarios. |
| RGR-DS-007 | RG-Core MUST | Persist stable platform identifiers (siteId, driveId, itemId, listItemUniqueId, versionId) where applicable. | Inspect preserved metadata and re-resolve content after move. |
| RGR-DS-008 | RG-Plus SHOULD | Support preservation of full version lineage for in-scope repositories where feasible. | Demonstrate policy-based version capture. |
| RGR-DS-009 | RG-Max MAY | Preserve additional metadata required for advanced filtering (createdBy, modifiedBy, file path history). | Demonstrate completeness in export metadata. |
| RGR-DS-010 | RG-Core MUST | Support deterministic resolution even if referenced file is moved, renamed, permission-changed, or deleted within retention bounds. | Demonstrate stability via stable identifiers and exception records. |

## B.4 Relationship Integrity (RGR-RL)

| Code | Level | Requirement | Verification |
| --- | --- | --- | --- |
| RGR-RL-001 | RG-Core MUST | Preserve explicit message ↔ link ↔ file ↔ version bindings as first-class records. | Show relationship table with stable IDs. |
| RGR-RL-002 | RG-Core MUST | Export relationships using explicit fields (ParentId/ChildId, RelationshipType) without re-attaching binaries. | Demonstrate export overlay reconstruction. |
| RGR-RL-003 | RG-Core MUST | Allow single preserved object to have multiple contextual bindings without collapsing events. | Demonstrate many-to-one event bindings. |
| RGR-RL-004 | RG-Plus SHOULD | Preserve repository context (site/channel/team identifiers) per event binding. | Demonstrate contextual export metadata. |
| RGR-RL-005 | RG-Core MUST | Preserve timestamps for relationship events (send time, share time, access time where available). | Show reconstructed timeline. |
| RGR-RL-006 | RG-Max MAY | Preserve conversation threading relationships. | Demonstrate thread grouping and ordering. |
| RGR-RL-007 | RG-Core MUST | Ensure stable, unique identifiers for every exported record (referential integrity). | Demonstrate referential integrity validation. |
| RGR-RL-008 | RG-Max SHOULD | Support relationship integrity validation (detect broken or orphaned links). | Demonstrate validation report. |

## B.5 Export and Reproducibility (RGR-EX)

| Code | Level | Requirement | Verification |
| --- | --- | --- | --- |
| RGR-EX-001 | RG-Core MUST | Produce exports consisting of native files plus standard load/overlay files including provenance, relationships, and hashes. | Demonstrate export package compatibility. |
| RGR-EX-002 | RG-Core MUST | Include export manifest capturing counts, scope parameters, time ranges, tool versions, and exceptions. | Provide sample manifest. |
| RGR-EX-003 | RG-Core MUST | Support reproducible exports (same scope definition → stable outputs and hashes, subject to new preservation events). | Run export twice and compare manifests/hashes. |
| RGR-EX-004 | RG-Core SHOULD | Support resumable exports with retry and full auditability. | Demonstrate interruption and resumption. |
| RGR-EX-005 | RG-Core MUST | Preserve and export exception records alongside content. | Show exception overlay records. |
| RGR-EX-006 | RG-Max MAY | Support multiple export profiles without altering evidence graph semantics. | Demonstrate alternate schema profile. |
| RGR-EX-007 | RG-Max SHOULD | Provide export validation routines (hash verification, referential integrity checks). | Demonstrate automated validation report. |

## B.6 Exception Determinism (RGR-ER)

| Code | Level | Requirement | Verification |
| --- | --- | --- | --- |
| RGR-ER-001 | RG-Core MUST | Generate structured exception record for any attachment or linked item that cannot be collected. | Demonstrate exception object creation. |
| RGR-ER-002 | RG-Core MUST | Exception records MUST include original reference, normalized reason code, retry history, and timestamps. | Inspect exception schema and audit trail. |
| RGR-ER-003 | RG-Core MUST | Exception records MUST remain associated with parent communications and intended targets. | Demonstrate linkage visibility in export. |
| RGR-ER-004 | RG-Core SHOULD | Implement controlled backoff and bounded retry policies for transient failures. | Demonstrate throttling retry behavior. |
| RGR-ER-005 | RG-Core SHOULD | Enable reprocessing after remediation while preserving attempt history. | Demonstrate re-queue and updated tracking. |
| RGR-ER-006 | RG-Core MUST | Reach deterministic end state for every preservation job (success or explicit failure). | Demonstrate job completion criteria and reporting. |
| RGR-ER-007 | RG-Max MAY | Provide exception analytics to quantify risk and remediation priority. | Demonstrate exception dashboards. |

## Conformance Declaration

A system claiming Reconstruction-Grade conformance MUST:

Declare its conformance level (RG-Core / RG-Plus / RG-Max).

Satisfy all MUST requirements for that level.

Provide demonstrable evidence via minimum conformance tests.

Provide documentation describing boundedness where upstream evidence (e.g., audit logs) is incomplete.
