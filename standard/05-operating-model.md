---
description: Preservation operating model and architectural constraints for defensible evidence systems, including conforming postures and enterprise design patterns.
---

# 5. Preservation Operating Model and Architectural Constraints

Reconstruction-Grade eDiscovery requires more than correct data structures. It requires a preservation operating model that delivers defensible legal outcomes under real-world enterprise constraints. This section defines the architectural requirements for that operating model, presents conforming preservation postures, and specifies the constraints under which all postures operate.

The governing design question is not whether data can be retained. It is: which operating model delivers a defensible, reproducible evidentiary record soonest under the constraints imposed by collaborative cloud platforms?

## 5.1 Architectural Role of the Preservation System of Record

Section 4 defines the Preservation System of Record as an explicit architectural layer. This section specifies how the operating model interacts with that layer.

A conforming operating model MUST route preservation actions through a Preservation System of Record (or equivalent) that satisfies the following properties:
- Evidence graph maintenance. The system MUST maintain a linked record of people, identities, events, artifacts, versions, and audit signals with stable identifiers.
- Decision ledger. The system MUST record scope definitions, preservation triggers, queries, and exceptions as an immutable, auditable ledger.
- Deterministic capture. The system MUST perform deterministic capture of content and relationships for in-scope matters, including as-sent version resolution and explicit relationship bindings.
- Reproducible export. The system MUST produce reproducible exports with manifests, hashes, and complete exception traceability (see Section 3.8).

The operating model determines when and how evidence enters the Preservation System of Record. The System of Record determines what properties that evidence carries once preserved.

## 5.2 Preservation Postures

Enterprises typically operate under one or more preservation postures. Each posture has distinct architectural properties that affect Reconstruction-Grade conformance. A conforming implementation MUST document which posture or combination of postures is in use and MUST satisfy all applicable requirements from Sections 3 and 4 regardless of posture.

### Posture A - Preserve-in-Place (Policy-Based Holds)

Content remains within the collaboration platform under retention or legal hold policies that prevent deletion.

Architectural properties:
- Minimal data movement; rapid activation.
- Lower immediate storage duplication.

Reconstruction-Grade limitations:
- Preserves existence but does not freeze point-in-time document state at event time.
- Does not preserve explicit message ↔ link ↔ version bindings as first-class records.
- Does not arrest audit log retention decay.
- Scope is custodian-bounded; collaborative dependencies outside the custodian boundary MAY not be preserved.

Preserve-in-Place is an important compliance control. It is not, by itself, a Reconstruction-Grade preservation mechanism. A system relying solely on Preserve-in-Place MUST document which Reconstruction-Grade requirements (Section 3, Appendix B) are not satisfied and MUST NOT claim conformance at any level unless all applicable MUST requirements are met through supplementary mechanisms.

### Posture B - Collect-to-Preserve (Reconstruction-Focused Baseline)

Matter-scoped preservation into a dedicated Preservation System of Record with deterministic resolution and explicit relationship bindings.

Architectural properties:
- Preserves point-in-time document state with deterministic as-sent version resolution.
- Maintains version lineage and stable identifiers.
- Preserves explicit relationship bindings (message ↔ link ↔ file ↔ version).
- Records exceptions deterministically with reason codes and retry histories.
- Enables reproducible export from the Preservation System of Record.

Tradeoffs:
- Requires scoped ingestion effort per matter.
- Requires architectural discipline in scope definition and preservation orchestration.

Collect-to-Preserve aligns preservation effort directly to legal relevance. Scope is defined by matter context, custodian and repository relevance, and time bounds. Preservation then captures precisely what is required with deterministic version and relationship fidelity. This approach avoids the common anti-pattern of requiring multi-year tenant backfill before legal teams can rely on the system.

Collect-to-Preserve is the recommended baseline posture for Reconstruction-Grade conformance because it satisfies all core architectural requirements (Sections 3 and 4) by design, while scaling preservation in proportion to legal demand rather than total tenant size.

### Posture C - Always-On Capture (Defined Populations)

Continuous preservation for designated high-risk roles, repositories, or custodian populations.

Architectural properties:
- Reduces context-decay risk for designated cohorts by preserving evidence before a matter arises.
- Enables incremental footprint expansion governed by policy.
- Requires governance clarity: which populations, which artifact types, which retention depth.

Always-On Capture is often deployed in combination with Collect-to-Preserve. The combination allows enterprises to maintain standing preservation for high-risk populations while using matter-scoped collection for all other custodians and repositories.

### Posture D - Full-Tenant Archive

Enterprise-wide continuous capture intended to support broad searchability across all users and repositories.

Architectural properties:
- Broadest preservation coverage when fully operational.
- MAY be justified when regulatory or operational mandates require comprehensive, standing capture.

Reconstruction-Grade constraints:
- Highest storage and indexing footprint, amplified non-linearly by version history, metadata normalization, and resiliency requirements.
- Longest lead time to complete initial backfill; time-to-operational-state is bounded by platform service limits and ingestion constraints (see Section 5.3), not by archive platform capacity.
- Before ingestion stabilizes, legal teams may be unable to rely on the archive for active matters, creating a gap between deployment and defensible time-to-use.

A Full-Tenant Archive that satisfies all Reconstruction-Grade requirements is conforming. However, enterprises SHOULD evaluate whether the time-to-defensible-outcome under this posture meets operational needs relative to Collect-to-Preserve or hybrid approaches.

## 5.3 Enterprise Scale Constraints

All preservation postures operate under the same structural constraints imposed by collaborative cloud platforms. These constraints are inherent properties of the operating environment. A conforming implementation MUST document how it addresses each constraint class.

Platform service limits. Microsoft 365 and similar platforms impose API throttling, rate limits, and concurrency ceilings that bound effective sustained throughput. Time-to-ingest for any preservation posture is governed by these limits, not by archive platform capacity. Implementations MUST account for throttling in capacity planning and MUST NOT assume unthrottled access.

Version proliferation. SharePoint and OneDrive version history, metadata normalization, relationship indexes, and resiliency requirements (e.g., geo-redundant immutable storage) can multiply the preserved footprint non-linearly relative to the latest-version corpus. Implementations SHOULD document the effective version multiplier and total footprint assumptions for capacity planning.

Permissions boundaries. Preservation actions require application-level permissions that may not be granted uniformly across all repositories. Permission remediation cycles are a common source of delay and exception volume. Implementations MUST treat permission-denied conditions as structured exceptions (see Section 3.7) and MUST provide remediation workflows.

Audit retention windows. Audit logs in Microsoft 365 are subject to retention limits that vary by license tier and configuration. Once audit records age out, behavioral evidence is permanently lost. Implementations that depend on audit evidence (RG-Plus and above) MUST document the effective audit retention window and MUST preserve audit records within that window. The system MUST represent audit coverage bounds explicitly (see Section 3.6).

Network and egress constraints. Large-scale data movement is bounded by network bandwidth, egress costs, and geographic data residency requirements. These constraints affect time-to-completion for any preservation posture and are particularly acute for Full-Tenant Archive deployments.

## 5.4 Time-to-Defensible-Outcome as the Governing Metric

The critical operational metric for a Reconstruction-Grade preservation operating model is not total volume preserved. It is time-to-defensible-outcome: the elapsed time from matter trigger to a reproducible, export-ready evidentiary record that satisfies all applicable conformance requirements.

This metric reflects a practical reality: legal teams cannot defer active matters until a preservation system reaches full operational state. A conforming operating model SHOULD be evaluated against the following:
- Time-to-first-defensible-export. How quickly can the system produce a conforming export for a new matter?
- Scope-to-preservation latency. What is the elapsed time from scope definition to completed deterministic capture?
- Exception resolution cadence. How quickly are structured exceptions triaged and remediated?
- Incremental matter onboarding. Can additional matters be onboarded without waiting for tenant-wide backfill to complete?

Enterprises SHOULD select the preservation posture (or combination) that minimizes time-to-defensible-outcome for their risk profile and regulatory obligations.

## 5.5 Throttling, Retries, and Deterministic Outcomes

At enterprise scale, failures are normal: permission errors, API throttling backoff, transient service faults, file moves and renames, and object lifecycle events are expected operating conditions. Reconstruction-Grade systems MUST treat these conditions as first-class workflow states.

The standard expectation is not perfection. It is determinism and auditability. Every referenced object MUST resolve to one of the following deterministic end states:
- Preserved content. The object was successfully collected with stable identifiers, version metadata, and relationship bindings.
- Structured exception record. The object could not be collected. The system has recorded the original reference, stable identifiers (if resolvable), a normalized reason code, complete retry history, and a deterministic end-state classification.

There are no silent drops. When preservation outcomes are explicit and reproducible, defensibility becomes an architectural property of the system rather than a function of operator narrative.
