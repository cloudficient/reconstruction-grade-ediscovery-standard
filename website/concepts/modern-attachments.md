---
description: >-
  Modern Attachments in eDiscovery are message-level references to live
  repository objects via hyperlinks instead of embedded file bytes — and why
  they break legacy evidence models.
chat_prompts:
  - "How do modern attachments break traditional eDiscovery workflows?"
  - "What version of a hyperlinked document gets preserved?"
  - "How does the Preservation Gap apply to hyperlinked files?"
  - "What does RGR require for modern attachment resolution?"
---

# Modern Attachments (eDiscovery)

> **Modern Attachment / Hyperlinked File:**
> A message-level reference to a repository object (typically via hyperlink or platform-managed pointer) where the file bytes are not embedded in the message.

## Definition

A **Modern Attachment** (also called a **hyperlinked file** or **cloud attachment**) is a message-level reference to a live object in a shared repository, delivered via hyperlink instead of embedded file bytes.

In legacy email, an attachment was inseparable from the message: the bytes were embedded and fixed at send time. The message *was* the evidence container.

In collaborative cloud platforms (Microsoft 365, Google Workspace, Slack), the message contains a **link to a repository object**. The object continues to change after the message is sent. The message does not carry the document state it references.

This shift means:

- The message and the document are **separate evidence objects** with separate lifecycles.
- The version that existed at send time is **not preserved by default**.
- Traditional exports collect the **current file state**, not the state that informed a decision.
- The exported bytes may not be the bytes that the recipient saw.

Modern attachments are the default behavior in Microsoft 365 (OneDrive/SharePoint sharing links in Teams messages and Outlook emails), Google Workspace (Drive links in Gmail and Chat), and Slack (file and link sharing).

## Why Modern Attachments Break Legacy Evidence Models

Legacy eDiscovery assumes that a message and its attachment form an atomic unit: the file bytes are embedded, immutable, and contemporaneous with the communication. This assumption underpins collection, deduplication, hashing, and review workflows.

Modern attachments violate this assumption in four ways:

| Dimension | Legacy Attachment | Modern Attachment |
|---|---|---|
| File bytes | Embedded in the message | Stored in a shared repository; linked by reference |
| Immutability | Fixed at send time | Object continues to change after the message is sent |
| Version state | The version *is* the attachment | The version must be resolved against the event timestamp |
| Evidence boundary | Message = container | Message + link + file + version = reconstructed evidence |

When evidence systems collect only the current file state, they produce a **time-shifted record**: the exported bytes are not the bytes that informed the decision at the time.

### Example: Hyperlinked decision memo

A Teams message links to a OneDrive document used to approve a high-impact decision. The file is edited after the message is sent. A traditional export collects the current file bytes. The exported bytes are not the bytes that informed the decision at the time. Without deterministic point-in-time resolution, reconstruction becomes narrative-driven.

## How Reconstruction-Grade Systems Handle Modern Attachments

The [Reconstruction-Grade eDiscovery Standard](reconstruction-grade-ediscovery.md) requires that systems preserve the **relationship between the communication and the referenced document state** — not just the file as it exists today.

Specifically, Reconstruction-Grade systems:

1. **Resolve the as-sent version** — the file version that existed when the communication was sent, determined as the latest version whose `lastModifiedDateTime ≤ message timestamp`.

2. **Preserve stable identifiers** — platform-native identifiers (siteId, driveId, itemId, versionId) that can re-resolve content over time, independent of URL changes.

3. **Maintain explicit relationship bindings** — message ↔ link ↔ file ↔ version mappings that preserve the evidentiary chain from communication to document state.

4. **Record structured exceptions** — when a referenced object cannot be resolved (deleted, out of retention, permission denied), the system produces a structured exception record rather than silently dropping the reference.

These requirements are formally specified in:

- [Section 3.2: Key Definitions](../03-defining-reconstruction-grade.md#32-key-definitions) — formal definition of modern attachment / hyperlinked file
- [Section 3.3: Deterministic Version Resolution](../03-defining-reconstruction-grade.md#33-deterministic-version-resolution) — the as-sent version selection rule
- [Section 3.5: Relationship Preservation](../03-defining-reconstruction-grade.md) — message ↔ link ↔ file ↔ version bindings (§3.5)

## Related Concepts

- **[The Context Gap](context-gap-ediscovery.md)** — Modern attachments are a primary driver of the Context Gap. When the message and the document are separate objects, traditional exports lose the contextual binding between them.

- **[Evidence Reconstruction](evidence-reconstruction.md)** — Reconstructing the evidentiary meaning of a modern attachment requires resolving the document state as-of the event timestamp — not collecting the file as it exists today.

- **[Version Lineage Evidence](../01-structural-shift.md#13-version-lineage-is-now-evidentiary)** — Files are continuously revised. Version lineage is the audit trail that reconstruction depends on. Without it, modern attachment resolution is impossible.

- **[Identity Drift](identity-drift.md)** — The same communication may reference a document that has changed hands, moved repositories, or been accessed under different identity states. Modern attachment resolution and identity reconstruction are interdependent.

- **[Context Collapse](../02-context-collapse.md)** — When modern attachments are flattened into current-state file exports, the result is context collapse: the evidence cannot explain what version informed which decision.

## Further Reading

- [What Is Reconstruction-Grade eDiscovery?](reconstruction-grade-ediscovery.md) — The architectural classification for systems that handle modern attachments correctly
- [What Is the Context Gap in eDiscovery?](context-gap-ediscovery.md) — The structural problem that modern attachments create
- [Section 1.2: Hyperlinks Replaced Attachments](../01-structural-shift.md#12-hyperlinks-replaced-attachments) — The structural shift from embedded to linked evidence
- [Section 3: Defining Reconstruction-Grade eDiscovery](../03-defining-reconstruction-grade.md) — Formal requirements for modern attachment handling
- [Appendix D: Reconstruction Scenarios](../appendix-d-reconstruction-scenarios.md) — Worked examples including modern attachment resolution
- [Appendix A: Glossary](../appendix-a-glossary.md) — Key terms used throughout the standard

---

<small>

**About this standard.** The Reconstruction-Grade eDiscovery Standard is an open, vendor-neutral specification maintained at [github.com/cloudficient/reconstruction-grade-ediscovery-standard](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard) and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Read the full standard:** [Reconstruction-Grade eDiscovery Standard →](../front-matter.md)

</small>
