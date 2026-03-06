# Conformance Declaration Template

!!! warning "Non‑Normative"
    This page is **non‑normative** and is **not legal advice**.
    This template is a convenience aid for organizations declaring conformance
    to the Reconstruction‑Grade eDiscovery Standard. Conformance claims are
    evaluated against the [normative requirements in Appendix B](../appendix-b-requirements.md).

---

## Instructions

Copy the template below and fill in all fields. Attach or link supporting evidence for each conformance test. Submit the completed declaration alongside vendor responses, RFP evaluations, or internal assessments.

---

## Conformance Declaration

### System information

| Field | Value |
|---|---|
| **System / product name** | ___________________ |
| **System version** | ___________________ |
| **Declaration date** | ___________________ |
| **Declaring organization** | ___________________ |
| **Contact** | ___________________ |

### Standard reference

| Field | Value |
|---|---|
| **Standard version** | Reconstruction‑Grade eDiscovery Standard v0.5‑draft |
| **Standard URL** | <https://cloudficient.github.io/reconstruction-grade-ediscovery-standard/> |

### Conformance level claimed

Select one:

- [ ] **RG‑Core** — Baseline Reconstruction‑Grade
- [ ] **RG‑Plus** — Identity + Behavior Conformance
- [ ] **RG‑Max** — Expanded Reconstruction Depth

See [Section 6.2](../06-evaluation-framework.md#62-conformance-levels) and [Appendix B § B.0](../appendix-b-requirements.md#b0-conformance-levels) for level definitions.

### Conformance test results

| Test | Description | Result | Evidence link |
|---|---|---|---|
| **T‑01** | As‑sent resolution | Pass / Fail / Partial | _link_ |
| **T‑02** | Link canonicalization | Pass / Fail / Partial | _link_ |
| **T‑03** | Relationship integrity | Pass / Fail / Partial | _link_ |
| **T‑04** | Identity as‑of | Pass / Fail / Partial / N/A | _link_ |
| **T‑05** | Access evidence (bounded) | Pass / Fail / Partial / N/A | _link_ |
| **T‑06** | Exception determinism | Pass / Fail / Partial | _link_ |
| **T‑07** | Export reproducibility | Pass / Fail / Partial | _link_ |

Tests T‑04 and T‑05 are N/A for RG‑Core declarations.
See [Section 6.3](../06-evaluation-framework.md#63-minimum-conformance-tests) for test definitions.

### Known limitations and boundedness

Describe any known limitations, coverage gaps, or boundary conditions:

| Area | Description |
|---|---|
| **Audit retention window** | ___________________ |
| **Workload coverage** | ___________________ |
| **Platform / version constraints** | ___________________ |
| **Identity data sources** | ___________________ |
| **Other** | ___________________ |

### Attestation

> I attest that the information provided in this declaration is accurate to the best of my knowledge as of the declaration date. This declaration is based on testing performed against the referenced version of the Reconstruction‑Grade eDiscovery Standard.
>
> **Name:** ___________________
>
> **Title:** ___________________
>
> **Date:** ___________________

---

## See also

- [Conformance Tests Quick Guide](conformance-tests-quick-guide.md) — setup and expected outcomes for T‑01 through T‑07
- [Appendix B — Requirements](../appendix-b-requirements.md) — full normative requirement tables
- [Appendix H — Vendor Scoring Worksheet](../appendix-h-vendor-scoring.md)
