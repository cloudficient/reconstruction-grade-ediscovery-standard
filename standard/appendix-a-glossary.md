---
description: >-
  Glossary of key eDiscovery terms defined by the Reconstruction-Grade eDiscovery Standard — including Context Gap, Preservation Gap, Identity Drift, Modern Attachments, and Evidence Reconstruction.
---

# Appendix A: Glossary

Key terms used throughout the Reconstruction-Grade eDiscovery Standard. Each linked term has a dedicated definition page with detailed explanation, practical examples, and references to the normative sections of the standard.

---

**Collaborative evidence:** Evidence created and used in cloud-native collaboration environments where artifacts are link-based, shared, and continuously revised.

**Collect-to-Preserve:** An operating model where preservation is triggered by legal relevance and scope — collecting specific evidence objects at the point of identification rather than relying on custodian-scoped holds or full-tenant archive-first backfill. Addresses the [Preservation Gap](concepts/preservation-gap.md) by operating at the evidence level instead of the container level.

**[Context Gap](concepts/context-gap-ediscovery.md):** The structural difference between how evidence is created in collaborative cloud platforms and what traditional eDiscovery systems can reconstruct after the fact. The Context Gap means preserved evidence cannot deterministically answer questions about document versions, access, timing, and reliance. See [The Context Gap in eDiscovery](concepts/context-gap-ediscovery.md).

**Deterministic end state:** A completed preservation or export workflow where all references resolve or are captured as structured exceptions, with no silent drops.

**Evidence graph:** A structured representation of evidence objects and their relationships with stable identifiers, timestamps, and provenance.

**[Identity Drift](concepts/identity-drift.md):** The continuous change of a person's role, department, access rights, and organizational context over time, creating a mismatch between present-day directory snapshots and historical legal questions. See [Identity Drift](concepts/identity-drift.md).

**[Modern Attachment / Hyperlinked File](concepts/modern-attachments.md):** A message-level reference to a repository object via hyperlink or platform-managed pointer, where file bytes are not embedded in the message. Modern attachments break the legacy assumption that a message carries its own evidence. See [Modern Attachments](concepts/modern-attachments.md).

**[Preservation Gap](concepts/preservation-gap.md):** The structural gap between what an organization's litigation hold system can reach and where modern evidence actually resides. Litigation holds are custodian-scoped, but collaborative evidence is relationship-scoped — hyperlinks in a held custodian's email may reference documents in non-custodian storage governed by separate retention policies. The Preservation Gap causes evidence to expire silently while the hold system reports full compliance. See [The Preservation Gap in eDiscovery](concepts/preservation-gap.md).

**[Reconstruction](concepts/evidence-reconstruction.md):** The process of deterministically resolving what actors experienced at a specific time, including document state, identity state, and access behavior. See [Evidence Reconstruction](concepts/evidence-reconstruction.md).
