# Changelog

All notable changes to the Reconstruction-Grade eDiscovery (RGR) Standard are documented in this file.

The format loosely follows Keep a Changelog principles and uses semantic-style versioning:

- v0.x → Draft phase (structure and requirements may evolve)
- v1.0 → First stable baseline
- v1.x → Clarifications and non-breaking refinements
- v2.0 → Architectural or normative shifts

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