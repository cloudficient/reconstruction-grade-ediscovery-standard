# Appendix K: Enterprise Implementation Roadmap

Reconstruction-Grade adoption is best approached as a program, not a single ingestion project. The goal is to establish a Preservation System of Record that delivers immediate matter value while expanding coverage over time.

Table 13. Illustrative implementation roadmap

| Phase | Theme | Deliverables (illustrative) |
| --- | --- | --- |
| Phase 0 | IT and security alignment | Define roles, permissions, key management, audit access, and operational controls; establish decision ledger and governance. |
| Phase 1 (0-6 months) | Foundational Collect-to-Preserve + core exports | Deliver end-to-end matter workflows (Identify → Preserve → Search → Export) for custodial repositories; establish export profiles, manifests, hashes, and exception handling. |
| Phase 2 (6-12 months) | Modern attachments depth + Teams export maturity + version policies | Expand deterministic resolution for modern attachments at scale; mature Teams coverage; define version retention and preservation policy choices by risk. |
| Phase 3 (12-18 months) | Historical membership + metadata lineage maturity | Increase identity-over-time fidelity (historical group membership); improve metadata lineage; strengthen relationship integrity validation. |
| Phase 4 (18-24 months) | Emerging artifacts and expanded workload coverage | Address emerging collaboration artifacts (Loop, Copilot-era objects) and extend coverage across additional workloads while maintaining conformance tests. |

## K.1 Program Guardrails

- Start with matters: success is measured by time-to-usable export for real cases, not by total backfilled volume.
- Preserve context early: prioritize audit and identity pipelines to prevent context decay.
- Make limitations explicit: unsupported artifacts and gaps MUST be recorded as structured exceptions, not hidden.
- Instrument everything: measure throughput, throttling behavior, exception rates, and reproducibility.
- Treat scope as evidence: maintain an immutable ledger of what was included/excluded and why.

## K.2 Practical Pilot Design

A pilot should be designed to prove Reconstruction-Grade properties with controlled scenarios and one or two real matters. A minimal pilot typically includes modern attachment resolution, identity as-of queries, audit correlation, and reproducible exports with manifests.
1. Select two matters with known hyperlink usage and meaningful timeline questions.
1. Define conformance tests (Appendix G) and success metrics (Appendix E).
1. Run parallel: compare legacy export results to Reconstruction-Grade outputs for as-sent versions and relationship integrity.
1. Document scope decisions and exceptions from day one; validate reproducibility with repeated exports.
1. Review results with litigation support and compliance architects; incorporate findings into standard requirements.
