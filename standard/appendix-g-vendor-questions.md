# Appendix G: Questions to Ask Vendors

When evaluating platforms for Reconstruction-Grade conformance, enterprises should require substantive answers to the following questions. These questions are designed to distinguish systems that preserve collaborative evidence with reconstruction-grade fidelity from those that flatten it into files and messages that cannot support legal reasoning.

- When a message contains a modern attachment or link, can you export the as-sent version (latest version where lastModifiedDateTime ≤ message timestamp)?
- Do you preserve version identifiers and the actual file bytes for resolved versions?
- What stable identifiers do you persist (siteId, driveId, itemId, listItemUniqueId, versionId), and how do you canonicalize sharing links and redirects?
- Can you preserve and export explicit ParentId/ChildId relationship mappings for messages and linked content?
- Can you reconstruct group membership and identity attributes as-of date X, or do you rely on current directory state?
- Do you treat audit logs as evidence, and can you correlate observed access to preserved versions - with explicit coverage bounds?
- What is your exception model: do failures produce reason-coded records with retry history, or do failures silently drop evidence?
- Are exports reproducible? If we run the same scope twice, do we get the same set with the same hashes and manifests (subject to new preservation events)?
- How do you support interruption handling and resumption for long-running exports?
- How do you record scope decisions so proportionality arguments are supported by an immutable decision ledger?
