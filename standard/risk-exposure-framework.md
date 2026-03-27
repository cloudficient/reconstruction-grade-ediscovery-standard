---
title: Risk Exposure Framework
description: Analytical mapping of evaluation categories and conformance tests to documented legal, procedural, and operational consequences when evidence preservation falls below reconstruction-grade thresholds.
---

# Risk Exposure Framework

The failure modes described in [Section 2](02-context-collapse.md) are not theoretical. They produce measurable consequences in litigation, regulatory response, and internal investigations. When context collapse is not addressed architecturally, downstream legal processes inherit the gap.

!!! note "Analytical, not normative"
    This framework is analytical, not normative. It does not introduce new requirements beyond those defined in [Appendix B](appendix-b-requirements.md). It maps the evaluation categories and conformance tests defined in [Section 6](06-evaluation-framework.md) to their documented legal, procedural, and operational consequences when those tests are not met. The requirements themselves are defined in Appendix B. The test procedures are defined in Section 6.3.

This framework draws on published findings from [The Sedona Conference](https://thesedonaconference.org/), the Federal Rules of Civil Procedure, [emerging case law](judicial-signals.md), and observed patterns in enterprise evidence preservation. The standard does not create these risks. It names risks that already exist and maps them to measurable thresholds.

## Why this framework exists

Collaboration platforms have fundamentally changed the nature of electronically stored information. The Sedona Conference's 2025 Commentary on Discovery Implications of Collaboration Platforms confirms that current tools cannot meet judicial expectations for preserving and producing collaborative evidence. The gap between what courts require and what organizations can produce is widening as collaboration platforms accelerate the shift toward dynamic, hyperlinked, continuously versioned content.

Organizations evaluating their evidence preservation posture need a structured way to assess exposure. Each risk category below corresponds to an evaluation category defined in [Section 6](06-evaluation-framework.md), is testable against conformance requirements in [Appendix B](appendix-b-requirements.md), and is grounded in documented third-party findings — not assertions originating from this standard.

---

## Risk categories

### Version Fidelity Risk

**Evaluation reference:** [Section 6](06-evaluation-framework.md), Category 1 (Point-in-time resolution); Test T-01

**Threshold gap:** When a system cannot deterministically resolve the document version that existed at the time a communication was sent, the exported record reflects current state, not historical state.

**Documented signals:**

- The Sedona Conference's 2025 Commentary on collaboration platforms identifies the inability to match a message to the "as-sent" version as a structural limitation of current tools.
- In *In re Insulin Pricing Litigation* (D.N.J., 2024), the court found it "not feasible, practicable, or proportionate" to produce hyperlinked family groups — a direct consequence of the version resolution gap. See [Judicial Signals](judicial-signals.md).

**Exposure profile:**

- *Evidentiary:* The produced record does not reflect what was communicated or relied upon. Opposing counsel can demonstrate that the document post-dates the communication, undermining the relevance of the production.
- *Procedural:* Courts may exclude time-shifted evidence or require costly re-collection targeting specific versions.
- *Operational:* Without automated resolution, legal teams must manually correlate versions to messages — a process that does not scale and introduces human error.

**Testable predicate:** This risk is present when Test T-01 (as-sent resolution) does not pass.

---

### Evidentiary Fragmentation Risk

**Evaluation reference:** [Section 6](06-evaluation-framework.md), Category 3 (Relationship integrity); Test T-03

**Threshold gap:** When explicit message-to-document relationship bindings are not preserved, communications and their referenced objects become disconnected evidence items. The relationship that gave each meaning is lost.

**Documented signals:**

- The Sedona Commentary notes that evidence scattered across platforms loses relationships, and that current tools cannot reliably reconstruct linkage between messages and the objects they reference.
- In *In re StubHub Refund Litigation* (N.D. Cal., 2023–2024), the court initially enforced protocol language requiring linked document production, then modified the requirement after finding full compliance not technologically possible — accepting a narrower, targeted approach. See [Judicial Signals](judicial-signals.md).

**Exposure profile:**

- *Evidentiary:* A message referencing a document cannot be authenticated as a complete record if the referenced object is absent or decoupled. Authenticity challenges under Rule 901 become procedural rather than substantive — the record itself cannot demonstrate its own completeness.
- *Procedural:* Opposing counsel may move to compel production of referenced objects, triggering supplemental collections and production delays.
- *Operational:* Review teams encounter messages with broken references and no systematic way to identify or prioritize which references are evidentiarily significant.

**Testable predicate:** This risk is present when Test T-03 (relationship integrity) does not pass.

---

### Identity Attribution Risk

**Evaluation reference:** [Section 6](06-evaluation-framework.md), Category 4 (Identity over time); Test T-04

**Threshold gap:** When identity is represented only as current-state directory data, temporal questions — who was in which role, department, or reporting line during the relevant period — cannot be answered from the preserved record.

**Documented signals:**

- [Section 1.4](01-structural-shift.md) of this standard documents that custodians change roles, teams, and access rights continuously. Legal questions are temporal; directory snapshots are not.
- The Sedona Commentary identifies the custodian model as inadequate for shared workspaces where relevant content resides outside custodian-owned spaces and organizational context changes over time.

**Exposure profile:**

- *Evidentiary:* Scope decisions made on present-day org charts may miss actors who held relevant roles during the historical period. Produced identity metadata may misattribute responsibility.
- *Procedural:* Opposing counsel can challenge scope adequacy when identity evidence does not reflect the relevant time period. Proportionality arguments weaken when the producing party cannot demonstrate evidence-based custodian selection.
- *Operational:* Legal teams resort to manual HR research to reconstruct historical identity — a process that is slow, incomplete, and not reproducible.

**Testable predicate:** This risk is present when Test T-04 (identity as-of) does not pass.

---

### Silent Loss Risk

**Evaluation reference:** [Section 6](06-evaluation-framework.md), Category 6 (Deterministic exceptions); Test T-06

**Threshold gap:** When items that cannot be collected are dropped without structured exception records, the production appears complete but is not. The absence is invisible to the producing party, opposing counsel, and the court.

**Documented signals:**

- [Section 5](05-operating-model.md) of this standard defines failures as first-class workflow states and requires deterministic end states for every preservation attempt. The absence of this discipline is the mechanism through which spoliation exposure accumulates silently.
- The [Buyer Checklist](toolkit/buyer-checklist.md) identifies "failures are logged internally" — where exceptions are not visible as structured records in the production — as a red flag indicating sub-reconstruction-grade architecture.

**Exposure profile:**

- *Evidentiary:* The producing party cannot demonstrate completeness. When opposing counsel identifies gaps, the absence of exception records means the producing party cannot explain what was attempted, what failed, or why.
- *Procedural:* Rule 37(e) exposure increases directly. Courts evaluate whether the party took reasonable steps to preserve. Silent drops are the opposite of reasonable steps — they are the absence of any step at all.
- *Operational:* Without exception tracking, remediation is impossible. The organization cannot identify what was lost, prioritize recovery, or demonstrate good faith effort.

**Testable predicate:** This risk is present when Test T-06 (exception determinism) does not pass.

---

### Access Inference Risk

**Evaluation reference:** [Section 6](06-evaluation-framework.md), Category 5 (Behavior evidence); Test T-05

**Threshold gap:** When audit evidence is not ingested and correlated to preserved objects, access claims rest on permission configuration rather than observed behavior. "Could have accessed" is substituted for "did access."

**Documented signals:**

- [Section 1.5](01-structural-shift.md) of this standard establishes that permissions describe potential, not proof. [Section 3](03-defining-reconstruction-grade.md) requires that audit-based claims carry explicit coverage bounds and that unknown access be represented as unknown rather than inferred.
- The Sedona Commentary identifies authentication and evidentiary trustworthiness as a distinct challenge area, noting that current approaches cannot reliably establish who interacted with collaborative content.

**Exposure profile:**

- *Evidentiary:* Claims about who saw or modified a document rest on inference rather than evidence. Under cross-examination, permission-based assertions are easily challenged: "You are saying she *could* have seen it — can you show she *did*?"
- *Procedural:* Courts may require additional forensic analysis to establish actual access, increasing cost and extending timelines.
- *Operational:* Without audit correlation, legal teams cannot prioritize review based on actual interaction patterns, leading to over-inclusive review populations.

**Testable predicate:** This risk is present when Test T-05 (access evidence, bounded) does not pass.

---

### Resolution Persistence Risk

**Evaluation reference:** [Section 6](06-evaluation-framework.md), Category 2 (Stable identifiers); Test T-02

**Threshold gap:** When stable platform-native identifiers are not preserved, objects that are moved, renamed, or re-shared cannot be re-resolved to their original evidence context. Links decay into unresolvable references.

**Documented signals:**

- [Section 3](03-defining-reconstruction-grade.md) of this standard defines the stable identifiers (siteId, driveId, itemId, listItemUniqueId, versionId) that must be preserved for re-resolution.
- In *In re StubHub Refund Litigation*, the court's compromise of manual hyperlink review was driven in part by the inability of existing tools to resolve links to their referenced objects at scale. See [Judicial Signals](judicial-signals.md).

**Exposure profile:**

- *Evidentiary:* A link that cannot be resolved to its target object is a broken evidentiary chain. The communication references something; the production cannot show what.
- *Procedural:* Re-collections become necessary when original link resolution fails — often months or years later, when the underlying objects may have been further modified, moved, or deleted.
- *Operational:* Each unresolvable reference requires manual investigation, consuming forensic and legal resources disproportionate to the underlying evidence value.

**Testable predicate:** This risk is present when Test T-02 (link canonicalization) does not pass.

---

### Defensibility Fragility Risk

**Evaluation reference:** [Section 6](06-evaluation-framework.md), Category 7 (Reproducible exports); Test T-07

**Threshold gap:** When the same scope definition produces different outputs on re-export, the reliability of the entire production is open to challenge. Defensibility becomes a function of timing rather than architecture.

**Documented signals:**

- [Section 4](04-preservation-system-of-record.md) of this standard requires that the Preservation System of Record produce reproducible exports with manifests, hashes, and complete exception traceability.
- The [Buyer Checklist](toolkit/buyer-checklist.md) identifies "re-running an export may produce different results" as a red flag indicating sub-reconstruction-grade architecture.

**Exposure profile:**

- *Evidentiary:* Opposing counsel can run a simple challenge: "Produce this set again. Did you get the same result?" If the answer is no — or if the producing party cannot demonstrate equivalence — the reliability of the original production is undermined.
- *Procedural:* Courts may order re-production, appoint technical neutrals, or impose heightened scrutiny on future productions from the same system.
- *Operational:* Non-reproducible exports create cascading uncertainty. Legal teams cannot rely on prior productions as baselines, and each new matter requires de novo validation.

**Testable predicate:** This risk is present when Test T-07 (export reproducibility) does not pass.

---

## Risk exposure summary

Table 1. Risk Exposure Categories and Evaluation Mapping

| Risk Category | Evaluation Category ([Section 6](06-evaluation-framework.md)) | Conformance Test | Primary FRCP Exposure |
| --- | --- | --- | --- |
| Version Fidelity | Point-in-time resolution | T-01 | Authenticity (Rule 901); Proportionality (Rule 26(b)) |
| Evidentiary Fragmentation | Relationship integrity | T-03 | Completeness; Authenticity (Rule 901) |
| Identity Attribution | Identity over time | T-04 | Scope adequacy; Proportionality (Rule 26(b)) |
| Silent Loss | Deterministic exceptions | T-06 | Spoliation (Rule 37(e)); Sanctions |
| Access Inference | Behavior evidence | T-05 | Authenticity; Weight of evidence |
| Resolution Persistence | Stable identifiers | T-02 | Completeness; Re-collection burden |
| Defensibility Fragility | Reproducible exports | T-07 | Reliability of production; Judicial confidence |

Each risk category is independently testable. Organizations can evaluate their current exposure by applying the conformance tests defined in [Section 6.3](06-evaluation-framework.md). Where a test does not pass, the corresponding risk category is present regardless of the system, vendor, or architecture in use.

The [Reconstruction-Grade Requirements](appendix-b-requirements.md) (Appendix B) define the normative capabilities that address each risk category. The [Exception Taxonomy](appendix-j-exception-taxonomy.md) (Appendix J) defines the operational failure modes that, when unhandled, contribute to Silent Loss and Resolution Persistence risk.

---

## Assessing organizational exposure

The risk categories above are designed to support structured self-assessment. For each category, the threshold gap defines a testable condition. Organizations can begin evaluation with the following questions, mapped from the [Buyer Checklist](toolkit/buyer-checklist.md):

| Risk Category | Assessment Question |
| --- | --- |
| Version Fidelity | Can your system export the as-sent version of a modern attachment — the version that existed when the message was sent? |
| Evidentiary Fragmentation | Does your system preserve and export explicit parent-child relationship mappings between messages and referenced objects? |
| Identity Attribution | Can your system reconstruct group membership and identity attributes as-of a historical date? |
| Silent Loss | What is your exception model — reason-coded structured records, or silent drops? |
| Access Inference | Does your system treat audit logs as evidence and correlate observed access with explicit coverage bounds? |
| Resolution Persistence | What stable identifiers does your system persist, and how does it canonicalize sharing links? |
| Defensibility Fragility | Are exports reproducible? Does the same scope produce the same hashes and manifests? |

These questions do not require the full conformance test suite. They provide an initial signal of where reconstruction-grade thresholds are or are not being met.

---

## Relationship to other standard sections

This framework connects to other parts of the standard as follows:

- **[Section 2: The Context Collapse Problem](02-context-collapse.md)** — Defines the failure modes that produce these risks.
- **[Section 6: Measurable Evaluation Framework](06-evaluation-framework.md)** — Defines the evaluation categories and conformance tests referenced by each risk category.
- **[Appendix B: Reconstruction-Grade Requirements](appendix-b-requirements.md)** — Defines the normative requirements (MUST/SHOULD/MAY) that address each risk category.
- **[Appendix J: Exception Taxonomy](appendix-j-exception-taxonomy.md)** — Defines the operational exception types that, when unhandled, contribute to Silent Loss and Resolution Persistence risk.
- **[Judicial Signals](judicial-signals.md)** — Documents emerging case law referenced in the documented signals for each risk category.

---

!!! info "Feedback and participation"
    This framework reflects the current state of documented signals from The Sedona Conference, published case law, and the Federal Rules of Civil Procedure. If you believe a risk category is overstated, understated, or missing, the standard welcomes feedback through its [participation process](participate/index.md).
