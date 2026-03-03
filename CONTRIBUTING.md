# Contributing to the Reconstruction‑Grade eDiscovery Standard

Thank you for your interest in improving the **Reconstruction‑Grade eDiscovery Standard (RGR)**.

The RGR Standard is a **vendor‑neutral architectural standard** that defines measurable criteria for preserving and reproducing modern collaborative evidence. It is **not legal advice**. Organizations should consult qualified counsel for matters involving legal defensibility, regulatory obligations, or litigation strategy.

The canonical text lives in the [`/standard/`](standard/) directory of this repository. All contributions should preserve the standard's vendor‑neutral framing.

---

## Types of contributions

### A. Non‑normative changes

These include:

- Typo corrections, grammar fixes, formatting
- Clarifications that do not alter the meaning of a requirement
- New or improved examples, diagrams, and commentary
- Toolkit pages, implementation guidance, and cross‑links
- Navigation, metadata, and build improvements

**Workflow:** Open a Pull Request directly. Small fixes (typos, broken links) may be committed without a prior Issue.

### B. Normative changes

These alter the meaning or scope of a conformance requirement:

- Adding, removing, or rewording a **MUST**, **SHOULD**, or **MAY** requirement
- Adding or modifying conformance tests (T‑01 through T‑07+)
- Changing definitions that affect how conformance is evaluated

**Workflow:**

1. **Open an Issue first** using the [Normative Change Proposal](../../issues/new?template=normative-change-proposal.yml) template.
2. Describe the proposed wording, rationale (tied to threat model, defensibility, or reproducibility), conformance‑level impact, and testability.
3. Wait for steward review and working‑group discussion before submitting a PR.
4. The PR must reference the approved Issue.

---

## Versioning discipline

| Change type | Version bump required? | CHANGELOG update? |
|---|---|---|
| Typo / formatting only | No | Optional |
| Non‑normative clarification | No (minor bump encouraged) | Yes |
| New toolkit or guidance page | No | Yes |
| Normative requirement change | **Yes — required** | **Yes — required** |

- The current version is tracked in [`VERSION`](VERSION).
- All substantive changes must update [`CHANGELOG.md`](CHANGELOG.md).
- Major versions (e.g., 1.0 → 2.0) indicate breaking conformance changes.
- Minor versions (e.g., 1.0 → 1.1) add requirements or tests without invalidating existing claims.

---

## Style guidance

1. **Normative keywords** — Keep `MUST`, `SHOULD`, `MAY`, `MUST NOT`, `SHOULD NOT` in UPPERCASE per [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119).
2. **Testable language** — Every requirement should be verifiable: prefer "the system MUST produce X" over "the system should try to do X."
3. **Vendor neutrality** — Do not mention specific product or vendor names in normative text. Use generic terms ("the system," "the platform," "the export tool").
4. **Section references** — Use requirement codes (e.g., `RGR‑DS‑003`) and section numbers when cross‑referencing.
5. **Non‑normative labels** — Clearly mark examples, commentary, and toolkit content as non‑normative.

---

## Running the site locally

```bash
# Install dependencies
pip install -r requirements.txt

# Serve locally with hot-reload
mkdocs serve

# Build static site
mkdocs build
```

The site configuration is in [`mkdocs.yml`](mkdocs.yml) with `docs_dir: standard`.

---

## Pull Request checklist

Before submitting, confirm:

- [ ] This PR is **non‑normative** OR links to an approved Normative Change Issue
- [ ] If normative: `CHANGELOG.md` updated
- [ ] If normative: `VERSION` bumped
- [ ] `mkdocs build` passes without errors
- [ ] No broken internal links

---

## Code of conduct

Be constructive, specific, and respectful. The goal is a shared, measurable standard — not a venue for product positioning.

---

## License

By contributing, you agree that your contributions will be licensed under [CC BY 4.0](LICENSE.md).
