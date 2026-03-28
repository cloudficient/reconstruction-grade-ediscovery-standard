---
description: "How the Reconstruction-Grade eDiscovery Standard is governed, how normative changes are evaluated, and how to participate in the open working group."
---

# Governance & Working Group

This page describes how the Reconstruction‑Grade eDiscovery Standard is governed, how normative changes are evaluated, and how the working group operates. It operationalizes the principles in [Section 7 — Standard Governance and Adoption](../07-governance-adoption.md).

---

## Stewardship

The standard is currently stewarded by **Cloudficient** as the originating author. The steward role encompasses:

- Maintaining the canonical repository and publication pipeline
- Reviewing and merging contributions
- Coordinating working‑group activities
- Managing version releases and change control

The steward does **not** unilaterally adopt normative changes. Normative changes follow the review process described below.

---

## Versioning and change control

The standard follows the versioning discipline defined in [Section 7.3](../07-governance-adoption.md#73-standard-versioning-and-change-control):

| Version type | Trigger | Conformance impact |
|---|---|---|
| **Major** (e.g., 1.0 → 2.0) | Breaking changes to conformance requirements | Existing claims MUST be re‑evaluated |
| **Minor** (e.g., 1.0 → 1.1) | New requirements, tests, or artifact coverage | Existing claims remain valid |
| **Patch / editorial** | Typos, formatting, non‑normative clarifications | No conformance impact |

Every version MUST include a change log entry in [`CHANGELOG.md`](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/blob/main/CHANGELOG.md). Conformance claims MUST reference a specific standard version.

---

## Normative change process

Normative changes — any modification to MUST, SHOULD, or MAY requirements, conformance tests, or definitions that affect conformance evaluation — follow a structured review:

### 1. Proposal

A [Normative Change Proposal](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/issues/new?template=normative-change-proposal.yml) issue is opened. The proposal must include:

- Proposed wording (with MUST/SHOULD/MAY keywords)
- Rationale tied to threat model, defensibility, or reproducibility
- Conformance‑level impact (RG‑Core / RG‑Plus / RG‑Max)
- Testability: how would you prove it?
- Backward compatibility assessment

### 2. Working‑group review

The proposal is discussed by the working group. Review considers:

- **Necessity:** Does this address a real gap or threat?
- **Testability:** Can conformance be objectively measured?
- **Proportionality:** Is the requirement achievable at enterprise scale?
- **Backward compatibility:** Does it invalidate existing conformance claims?

### 3. Steward decision

The steward accepts, requests revision, or declines the proposal with documented rationale. Accepted proposals are assigned to a version milestone.

### 4. Implementation

A Pull Request is submitted referencing the approved Issue. The PR must update `CHANGELOG.md` and bump `VERSION`.

---

## Working group

### Purpose

The working group validates requirements against real enterprise conditions and contributes to the conformance test framework. Focus areas include:

- Scale constraints and service throttling
- Identity systems and effective‑dating
- Regulatory obligations
- Export reproducibility
- Operational defensibility

### Composition

Participation is open to:

- **Enterprises** — legal operations, IT, compliance
- **Law firms** — litigation support, eDiscovery practice groups
- **Service providers** — managed review, consulting
- **Vendors** — platform developers, processing tool providers
- **Individual practitioners** — researchers, consultants

### How to join

[Express interest via the Working Group Participation form →](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/issues/new?template=working-group-participation.yml)

### Operating principles

- Discussions focus on **measurable criteria**, not product positioning.
- Vendor participants contribute on equal footing; conformance claims by any party are evaluated against published requirements.
- The objective is **shared vocabulary, measurable baselines, and repeatable evaluation** across collaboration platforms.

---

## See also

- [Section 7 — Standard Governance and Adoption](../07-governance-adoption.md)
- [How to Contribute](how-to-contribute.md)
- [License](../license.md)
