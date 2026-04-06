# Changelog

All notable changes to the Reconstruction-Grade eDiscovery (RGR) Standard are documented in this file.

The format loosely follows Keep a Changelog principles and uses semantic-style versioning:

- v0.x → Draft phase (structure and requirements may evolve)
- v1.0 → First stable baseline
- v1.x → Clarifications and non-breaking refinements
- v2.0 → Architectural or normative shifts

---

## [0.54-draft] – 2026-04-06

### Added
- **RG-Aware adoption tier** — pre-conformance tier beneath RG-Core/Plus/Max formalizing the minimum transparent posture for organizations dealing with modern collaborative evidence. Requires: collect linked content from same-tenant storage, disclose limitations through ESI protocols, generate structured exceptions, document matter-level gaps. Defined in Section 6.2 and Appendix B, Section B.0.
- **Adoption Pathway** section in front-matter executive summary — explains the structured path from RG-Aware through RG-Core to RG-Max.
- RG-Aware glossary entry in Appendix A.
- Explicit statement in Appendix B: "An organization's inability to achieve RG-Core does not excuse failure to attempt reasonable collection and disclosure of linked content within its current capabilities."
- Conformance Declaration updated to address RG-Aware documentation expectations.
- Blog post: "The Dog, the Tail, and the Staircase" — response to Craig Ball's assessment of the standard.
- Blog cover images (WebP) and horizontal card layout for blog listing page.
- Blog categories enabled with label styling.

### Changed
- Version references updated site-wide (homepage, about, why, README, standard/README) from 0.52-draft to 0.54-draft.
- Blog excerpt layout redesigned: horizontal cards with thumbnail left, content right. Excerpts tightened to single paragraph.

---

## [0.52-draft] – 2026-03-27

### Added
- **Risk Exposure Framework** — standalone analytical page mapping seven evaluation categories and conformance tests to documented legal, procedural, and operational consequences when evidence preservation falls below reconstruction-grade thresholds. Non-normative; no changes to requirements or conformance levels. Grounded in Sedona Conference findings, emerging case law (FRCP/FRE), and this standard's analytical framework.
- Homepage Risk Assessment section with link to the new framework.
- Forward-reference in Section 2.5 (Context Collapse) to the Risk Exposure Framework.
- Cross-reference in "Why This Exists" page.

### Changed
- **Design refinements** — improved spacing throughout the site (cards, sections, panels, headings), softened card borders to subtle shadows, brightened accent blue, swapped body font to Inter, lightened header/tab bar.
- Risk Exposure Framework link added to homepage "Standard text" quick links.

---

## [0.51-draft] – 2026-03-03

### Added
- **Core Concepts section** (`/concepts/`) — short, authoritative, vendor-neutral definition pages designed for analyst and AI citation:
  - `concepts/index.md` — concept index with summary table
  - `concepts/context-gap-ediscovery.md` — moved from root; updated cross-links
  - `concepts/evidence-reconstruction.md` — moved from root; updated cross-links
  - `concepts/reconstruction-grade-ediscovery.md` — moved from `what-is-reconstruction-grade-ediscovery.md`; updated cross-links
  - `concepts/modern-attachments.md` — **new** definition page for modern attachments / hyperlinked files
  - `concepts/identity-drift.md` — **new** definition page for identity drift and the static custodian myth
- Added `Modern Attachment / Hyperlinked File` and `Identity Drift` to Appendix A glossary

### Changed
- `mkdocs.yml` — replaced three top-level concept nav entries with a "Core Concepts" section containing all five concept pages plus index
- `standard/index.md` — updated Quick Links to include Core Concepts hub; all concept links now point to `concepts/` paths
- `standard/front-matter.md` — updated concept links to `concepts/` paths
- `standard/01-structural-shift.md` — updated Context Gap link to `concepts/` path
- `standard/02-context-collapse.md` — updated reconstruction and Context Gap links to `concepts/` paths
- `standard/appendix-a-glossary.md` — updated existing concept links to `concepts/` paths

### Removed
- `standard/context-gap-ediscovery.md` — replaced by `standard/concepts/context-gap-ediscovery.md`
- `standard/evidence-reconstruction.md` — replaced by `standard/concepts/evidence-reconstruction.md`
- `standard/what-is-reconstruction-grade-ediscovery.md` — replaced by `standard/concepts/reconstruction-grade-ediscovery.md`

### Notes
- No normative requirements added or changed. This is a structural/non-normative change.
- All internal cross-references updated; no broken links.

---

## [0.5-draft] – 2026-02-28

### Added
- Initial public draft of the Reconstruction-Grade eDiscovery Standard
- Formal requirement domains:
  - RGR-ID (Identity Over Time)
  - RGR-AU (Audit and Behavior Evidence)
  - RGR-DS (Document State and Deterministic Resolution)
  - RGR-RL (Relationship Integrity)
  - RGR-EX (Export and Reproducibility)
- Operating Model section
- Terminology definitions and architectural framing
- Normative language alignment (MUST / SHOULD / MAY)

### Notes
- This version represents the first structured draft suitable for standards discussion.
- Terminology may evolve based on industry feedback.
- Conformance testing criteria are not yet fully formalized.

---

## Versioning Policy

- All substantive normative changes MUST:
  - Update this changelog
  - Update the `VERSION` file
  - Be merged via Pull Request
- Minor editorial corrections (typos, grammar, formatting) MAY be merged without version bump if they do not affect meaning.
- Any change affecting normative requirements (MUST/SHOULD/MAY) requires a version increment.