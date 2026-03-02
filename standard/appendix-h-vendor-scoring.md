# Appendix H: Vendor Scoring Worksheet

This worksheet provides a structured way to score solutions against Reconstruction-Grade criteria. Scores are illustrative; enterprises should adjust weights based on risk profile.

Table 11. Scoring worksheet (fill-in)

| Criterion | Weight (1-3) | Vendor Score (0-3) | Notes / Evidence |
| --- | --- | --- | --- |
| Point-in-time as-sent resolution | 3 |  | Demonstrated deterministic resolution and documented fallback rules. |
| Stable identifier preservation | 3 |  | Persists platform IDs; resilient to moves/renames/redirects. |
| Relationship integrity (Parent/Child mappings) | 3 |  | Exports explicit relationships without collapsing context. |
| Identity over time (effective-dated) | 3 |  | As-of identity and membership reconstruction. |
| Audit evidence ingestion and correlation | 2 |  | Observed access correlated to preserved objects/versions. |
| Deterministic exceptions and retry audit | 2 |  | Reason-coded exceptions; full retry history; deterministic end state. |
| Reproducible exports with manifests + hashes | 3 |  | Repeatable outputs; integrity validation. |
| Operational monitoring at scale | 2 |  | Throughput, throttling backoff, exception tracking, SLA reporting. |
| Data portability and evidence longevity | 2 |  | Supports export profiles and long-term reusability. |
