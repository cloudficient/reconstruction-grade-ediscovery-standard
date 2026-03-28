---
description: "How to contribute to the Reconstruction-Grade eDiscovery Standard, including guidelines for normative changes, non-normative fixes, and style conventions."
---

# How to Contribute

This page summarizes the contribution process for the Reconstruction‑Grade eDiscovery Standard. For complete details, see [CONTRIBUTING.md](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/blob/main/CONTRIBUTING.md) in the repository root.

---

## Before you start

- The RGR Standard is **vendor‑neutral**. Contributions should not introduce product‑specific language into normative text.
- The standard is **not legal advice**. It defines architectural criteria for evidence preservation systems.
- The canonical text lives in the [`/standard/`](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/tree/main/standard) directory.

---

## Non‑normative contributions

These do **not** change MUST/SHOULD/MAY requirements:

- Typo corrections, grammar, formatting
- Clarifications that preserve existing meaning
- New examples, diagrams, or commentary
- Toolkit pages and implementation guidance
- Navigation improvements, cross‑links, metadata

**Process:** Open a Pull Request directly. Small fixes (typos, broken links) can be committed without a prior Issue.

---

## Normative contributions

These **do** change conformance requirements:

- Adding, removing, or rewording a MUST, SHOULD, or MAY requirement
- Adding or modifying conformance tests (T‑01 through T‑07+)
- Changing definitions that affect how conformance is evaluated

**Process:**

1. [Open a Normative Change Proposal](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/issues/new?template=normative-change-proposal.yml) issue first.
2. Include: proposed wording, rationale, conformance‑level impact, and testability.
3. Wait for steward review and working‑group discussion.
4. Submit a PR referencing the approved Issue.
5. Update `CHANGELOG.md` and bump `VERSION`.

---

## Style guidelines

| Guideline | Details |
|---|---|
| **Normative keywords** | MUST, SHOULD, MAY in UPPERCASE (RFC 2119) |
| **Testable language** | Prefer "the system MUST produce X" over vague intent |
| **Vendor neutrality** | No product names in normative text |
| **Cross‑references** | Use requirement codes (e.g., `RGR‑DS‑003`) and section numbers |
| **Non‑normative labels** | Clearly mark examples, commentary, and toolkit content |

---

## Running locally

```bash
pip install -r requirements.txt
mkdocs serve
```

The site builds from `mkdocs.yml` with `docs_dir: standard`.

---

## Questions?

Open a [Standard Feedback](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/issues/new?template=standard-feedback.yml) issue or start a [Discussion](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/issues).
