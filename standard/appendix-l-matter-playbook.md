---
description: Collect-to-preserve matter playbook for eDiscovery, covering legal hold triggers, scope definition, custodian identity resolution, and production workflows.
---

# Appendix L: Collect-to-Preserve Matter Playbook

Collect-to-Preserve is an operating discipline. The playbook below describes what 'good' looks like when a matter triggers preservation.

## L.1 Matter Trigger and Scope Definition

- Create an immutable scope definition: custodians, repositories, time bounds, and rationale.
- Resolve custodian identities to natural persons; capture effective-dated identity snapshots for the relevant period.
- Identify collaboration spaces where work occurred (teams, channels, sites) using evidence-based signals where possible.

## L.2 Preservation Actions

- Preserve custodial repositories and relevant shared repositories within scope.
- Enumerate and preserve version lineage for in-scope objects per policy.
- Resolve modern attachments and links referenced by communications; preserve as-sent versions and relationship bindings.

## L.3 Validation and Exception Triage

- Run referential integrity checks: every message-linked reference resolves or produces an exception record.
- Review exception dashboard; prioritize remediation for permission-denied and throttling classes.
- Lock preservation artifacts as immutable evidence once validated.

## L.4 Export and Reproducibility

- Generate export package with manifest, hashes, load/overlay files, and exception overlays.
- Verify reproducibility by rerunning export under identical scope definition and comparing manifests/hashes.
- Provide downstream teams with relationship mappings and provenance fields to avoid re-flattening context.
