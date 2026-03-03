# Buyer Checklist

!!! warning "Non‑Normative"
    This page is **non‑normative** and is **not legal advice**.
    It summarizes key evaluation criteria from the standard for convenience.
    Always refer to the [canonical requirements](../appendix-b-requirements.md) for definitive conformance language.

---

## If you only ask 10 questions…

These questions map to the core evaluation categories in [Section 6.1](../06-evaluation-framework.md#61-evaluation-categories) and the vendor questions in [Appendix G](../appendix-g-vendor-questions.md).

| # | Question | Maps to |
|---|---|---|
| 1 | Can you export the **as‑sent version** of a modern attachment (version ≤ message timestamp)? | RG‑Core — point‑in‑time resolution |
| 2 | What **stable identifiers** do you persist (siteId, driveId, itemId, versionId), and how do you canonicalize sharing links? | RG‑Core — stable identifiers |
| 3 | Do you preserve and export **explicit parent↔child relationship mappings** for messages and linked content? | RG‑Core — relationship integrity |
| 4 | What is your **exception model** — do failures produce reason‑coded records with retry history, or do they silently drop evidence? | RG‑Core — deterministic exceptions |
| 5 | Are **exports reproducible**? Same scope → same hashes and manifests? | RG‑Core — reproducible exports |
| 6 | Can you reconstruct **group membership and identity attributes as‑of date X**, or do you rely on current directory state? | RG‑Plus — identity over time |
| 7 | Do you treat **audit logs as evidence** and correlate observed access to preserved versions — with explicit coverage bounds? | RG‑Plus — behavior evidence |
| 8 | How do you handle **interruption and resumption** for long‑running exports? | Operational robustness |
| 9 | How do you record **scope decisions** so proportionality arguments are supported by an immutable decision ledger? | RG‑Core — scope governance |
| 10 | What **conformance level** (RG‑Core / RG‑Plus / RG‑Max) do you claim, and can you demonstrate it with the [standard's test suite](../06-evaluation-framework.md#63-minimum-conformance-tests)? | Overall conformance |

---

## Red flags 🚩

Watch for these patterns — each indicates a system that may **not** meet Reconstruction‑Grade criteria:

- **"We export the latest version only."** — Fails as‑sent resolution (T‑01).
- **"Links are preserved as URLs."** — URL‑only linking breaks when objects move, rename, or permissions change.
- **"Failures are logged internally."** — If you can't see structured exception records with reason codes, failures are effectively silent.
- **"We use current directory for identity."** — No effective‑dated identity means you cannot answer "who was in that group on that date?"
- **"Audit data is supplementary, not evidence."** — If audit logs aren't ingested with provenance, behavior claims are unsubstantiated.
- **"Re‑running an export may produce different results."** — Non‑reproducible exports undermine defensibility.

---

## Next steps

- Use the [RFP Clause Pack](rfp-clauses.md) to formalize these questions in procurement documents.
- Score vendor responses with [Appendix H — Vendor Scoring Worksheet](../appendix-h-vendor-scoring.md).
- For the full question set, see [Appendix G — Questions to Ask Vendors](../appendix-g-vendor-questions.md).
