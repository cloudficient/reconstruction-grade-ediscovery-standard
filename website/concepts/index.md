---
description: >-
  Core concepts introduced by the Reconstruction-Grade eDiscovery Standard
  for reasoning about collaborative evidence preservation and reconstruction.
---

# Core Concepts

The **[Reconstruction-Grade eDiscovery Standard](../front-matter.md)** introduces several concepts for reasoning about collaborative evidence — how it is created, how it decays, and what systems must do to preserve it with point-in-time fidelity.

These definition pages are intended to be short, authoritative, and vendor-neutral. Each links back into the normative sections and appendices of the standard where the concept is formally specified.

## Concept Index

| Concept | Summary |
|---|---|
| **[Context Gap](context-gap-ediscovery.md)** | The structural difference between how evidence is created in collaborative cloud platforms and what traditional eDiscovery systems can reconstruct after the fact. |
| **[Preservation Gap](preservation-gap.md)** | The structural gap between what litigation hold systems can reach and where modern evidence actually resides — causing evidence to expire silently outside hold scope. |
| **[Evidence Reconstruction](evidence-reconstruction.md)** | The ability of a system to deterministically reproduce what actors experienced in a collaborative environment at a specific point in time. |
| **[Reconstruction-Grade eDiscovery](reconstruction-grade-ediscovery.md)** | An architectural classification for evidence systems that can produce a reproducible, point-in-time record of collaborative activity without relying on inference. |
| **[Modern Attachments](modern-attachments.md)** | Message-level references to live repository objects via hyperlinks instead of embedded file bytes — and why they break legacy evidence models. |
| **[Identity Drift](identity-drift.md)** | The continuous change of a person's role, department, access rights, and organizational context over time — and why static custodian snapshots fail under temporal legal questions. |

## How to Use These Pages

- **Evaluating a system?** Start with [Reconstruction-Grade eDiscovery](reconstruction-grade-ediscovery.md) for the definition and conformance levels.
- **Understanding the problem?** Start with the [Context Gap](context-gap-ediscovery.md) and [Preservation Gap](preservation-gap.md) — the two structural failure modes — then see [Evidence Reconstruction](evidence-reconstruction.md) for the solution.
- **Investigating a specific dimension?** See [Modern Attachments](modern-attachments.md) or [Identity Drift](identity-drift.md) for focused definitions.

Each concept page links to the relevant normative sections, appendices, and evaluation criteria in the full standard.

---

<small>

**About this standard.** The Reconstruction-Grade eDiscovery Standard is an open, vendor-neutral specification maintained at [github.com/cloudficient/reconstruction-grade-ediscovery-standard](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard) and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Read the full standard:** [Reconstruction-Grade eDiscovery Standard →](../front-matter.md)

</small>
