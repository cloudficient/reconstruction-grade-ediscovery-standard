[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Status](https://img.shields.io/badge/Status-Draft%20v0.51-blue)
![Type](https://img.shields.io/badge/Type-Conformance%20Standard-darkgreen)

> ⚖️ A vendor-neutral architectural baseline for collaborative cloud evidence.

Reconstruction-Grade eDiscovery (RGR) is a vendor-independent conformance standard.

Cloudficient's Context-Aware eDiscovery platform is designed to meet and demonstrate conformance with this standard. Other implementations are possible.

# Reconstruction-Grade eDiscovery Standard (RGR)

This repository contains the working draft of the **Reconstruction-Grade eDiscovery (RGR) Standard** — a vendor-independent, testable architectural standard defining measurable criteria for preserving and reproducing **modern collaborative evidence** (e.g., cloud documents, shared links, version histories, evolving permissions, and identity changes) in a litigation- and investigation-grade manner.

The Standard is written to support independent evaluation and repeatable conformance testing.

---

## Download the Standard

| Format | Link |
|--------|------|
| **PDF** | [**Download RGR Standard v0.51-draft (PDF)**](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/releases/latest/download/rgr-standard-0.51-draft.pdf) |
| **HTML** | [**Read online (GitHub Pages)**](https://cloudficient.github.io/reconstruction-grade-ediscovery-standard/) |
| **Source** | Browse the [`/standard/`](standard/) directory in this repository |

---

## Canonical Source of Truth

**The Markdown content in this repository is the canonical source of truth for the Standard.**

All other formats (including website HTML publication and PDF editions) are **rendered artifacts** derived from this repository and may lag slightly behind the canonical text.

Tagged releases represent immutable reference editions suitable for citation.

---

## Status

- **Status:** Draft for standards discussion  
- **Current version:** v0.51-draft  
- **Version discipline:** Substantive edits MUST update `CHANGELOG.md` and bump the version in `VERSION`

This Standard is currently in draft phase and open for structured feedback.

While stewarded by Cloudficient, it is intended to remain **vendor-independent** and applicable across collaboration platforms and eDiscovery ecosystems.

---

## How to Read This Standard

The Standard is organized into sections (under `/standard`) and appendices. Requirements use RFC 2119-style normative language:

- **MUST / MUST NOT** — mandatory for conformance  
- **SHOULD / SHOULD NOT** — recommended; deviations require documented justification  
- **MAY** — optional  

Non-normative material (examples, commentary, implementation notes, toolkit resources) is clearly labeled as such.

---

## Repository Layout

| Path | Purpose |
|---|---|
| `/standard/` | The Standard's sections and appendices (canonical text) |
| `/standard/concepts/` | Core concept definition pages (Context Gap, Evidence Reconstruction, Modern Attachments, Identity Drift) |
| `/standard/toolkit/` | Non-normative toolkit resources (checklists, clause packs, templates) |
| `/standard/participate/` | Participation and governance information |
| `CHANGELOG.md` | Version history and notable changes |
| `VERSION` | Current version identifier (e.g., `0.51-draft`) |
| `CONTRIBUTING.md` | How to propose edits and provide feedback |
| `LICENSE.md` | Licensing terms (CC BY 4.0) |
| `.github/ISSUE_TEMPLATE/` | Issue templates for feedback, proposals, and participation |
| `.github/pull_request_template.md` | Pull request checklist |

---

## Contributing and Discussion

Discussion is welcome via GitHub Issues. Structured issue templates are provided for:

- [**Standard Feedback**](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/issues/new?template=standard-feedback.yml) — report unclear or incorrect content  
- [**Normative Change Proposal**](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/issues/new?template=normative-change-proposal.yml) — propose changes to MUST/SHOULD/MAY requirements  
- [**Toolkit Request**](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/issues/new?template=toolkit-request.yml) — suggest new non-normative resources  
- [**Working Group Participation**](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/issues/new?template=working-group-participation.yml) — express interest in the working group  

Feedback is particularly encouraged on:

- terminology and definitions  
- requirement clarity (testability and conformance measurability)  
- platform coverage (M365, Google Workspace, Slack, etc.)  
- export and reproducibility criteria  
- defensibility and auditability requirements  

Proposed clarifications, examples, and non-normative improvements may be submitted as Pull Requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution guide.

Normative requirement changes (MUST / SHOULD / MAY) are evaluated through the active working group process and steward review prior to acceptance. Substantive changes must clearly identify the affected section, describe rationale, and assess conformance impact.

---

## Participation and Working Group

The Reconstruction-Grade Standard is currently in draft phase. During this phase, select enterprises are participating in validation and conformance modeling.

The working group focuses on measurable criteria for collaborative evidence preservation and reconstruction, including:

- scale constraints  
- service throttling  
- identity systems and effective-dating  
- regulatory obligations  
- export reproducibility  
- operational defensibility  

Participating organizations evaluate requirements against real enterprise conditions and contribute to the development of a conformance test framework.

Vendors and service providers MAY also participate.

Conformance claims — by any party — SHOULD be evaluated against the published requirements and associated test criteria.

The objective is shared vocabulary, measurable baselines, and repeatable evaluation across collaboration platforms.

---

## Publishing Model

This repository supports two publication outputs:

1. **Canonical Standard (Markdown in Git)** — authoritative text and change history  
2. **Rendered artifacts** — website HTML and downloadable PDF (generated from tagged versions)  

Tagged releases represent immutable reference editions suitable for citation and procurement documentation.

---

## Citation

When citing the Standard, reference the specific version and section.

Example:

> Reconstruction-Grade eDiscovery Standard, v0.51-draft, Section 3.2, Cloudficient (2026).

---

## License

The text and original diagrams in this repository are licensed under the  
**[Creative Commons Attribution 4.0 International License (CC BY 4.0)](LICENSE.md)**.

See [LICENSE.md](LICENSE.md) for full terms including trademark carve-outs and attribution guidance.

---

## Disclaimer

This document is provided for standards discussion and architectural guidance.  
It does not constitute legal advice. Organizations should consult qualified counsel for matters involving legal defensibility, regulatory obligations, or litigation strategy.
