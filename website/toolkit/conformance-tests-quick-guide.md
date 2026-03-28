---
description: "Quick reference guide for the seven RGR conformance tests (T-01 to T-07) covering version resolution, link canonicalization, and export reproducibility."
---

# Conformance Tests Quick Guide

!!! warning "Non‑Normative"
    This page is **non‑normative** and is **not legal advice**.
    It summarizes the minimum conformance tests defined in
    [Section 6.3](../06-evaluation-framework.md#63-minimum-conformance-tests).
    The standard text is authoritative; this guide is a convenience summary.

---

## Overview

The standard defines seven minimum conformance tests (T‑01 through T‑07). These are controlled scenarios designed to demonstrate that a system's Reconstruction‑Grade claims are verifiable.

| Test | Category | Required for |
|---|---|---|
| T‑01 | As‑sent resolution | RG‑Core |
| T‑02 | Link canonicalization | RG‑Core |
| T‑03 | Relationship integrity | RG‑Core |
| T‑04 | Identity as‑of | RG‑Plus |
| T‑05 | Access evidence (bounded) | RG‑Plus |
| T‑06 | Exception determinism | RG‑Core |
| T‑07 | Export reproducibility | RG‑Core |

---

## T‑01: As‑sent resolution

**Setup:** Create a document with multiple versions. Send a message containing a link or modern attachment at time t₀. Modify the document at time t₁ (where t₁ > t₀).

**Expected outcome:** The export produces the version of the document whose `lastModifiedDateTime` ≤ t₀ — the version that existed when the message was sent.

**Common failure modes:**

- System exports the latest (current) version instead of the as‑sent version
- System exports a version but does not record which version was resolved or why
- Version resolution is non‑deterministic across repeated exports

---

## T‑02: Link canonicalization

**Setup:** Create sharing links, redirect patterns (e.g., shortened URLs), and then rename or move the target objects.

**Expected outcome:** The export resolves all links to the correct objects using stable identifiers (siteId, driveId, itemId), not URLs. Moved/renamed objects are still correctly linked.

**Common failure modes:**

- Links break when objects are moved or renamed
- System stores URL strings without resolving to stable identifiers
- Redirect links are not followed or canonicalized

---

## T‑03: Relationship integrity

**Setup:** Create a single message that references multiple objects (e.g., two modern attachments and a shared link). Verify parent–child mappings.

**Expected outcome:** The export preserves explicit parent↔child relationship mappings with relationship types (e.g., message → attachment, message → linked document).

**Common failure modes:**

- Relationships are flattened (all items appear as siblings with no linkage)
- Relationship type is missing (you can see items are related but not *how*)
- One-to-many references collapse into a single record

---

## T‑04: Identity as‑of

**Setup:** Change a user's department, manager, and group membership between date X and date Y.

**Expected outcome:** As‑of queries for date X and date Y produce different, correct results reflecting the user's historical state at each point in time.

**Common failure modes:**

- System returns current directory state regardless of query date
- Group membership is not historically preserved
- Identity changes are recorded but not queryable as‑of a specific date

---

## T‑05: Access evidence (bounded)

**Setup:** Generate view and edit events in the audit log for specific objects and versions.

**Expected outcome:** The system correlates audit events to the correct objects and versions, and explicitly reports coverage bounds (e.g., "audit available from date X; no data before date X").

**Common failure modes:**

- Audit events are ingested but not correlated to specific object versions
- System does not differentiate potential access (permissions) from observed access (audit)
- Coverage bounds are not reported — user assumes complete coverage when it is partial

---

## T‑06: Exception determinism

**Setup:** Force a preservation or export failure (e.g., permission denial on a specific item).

**Expected outcome:** The system produces a structured exception record containing:

- Item identifier
- Reason code (e.g., `permission-denied`)
- Retry history (attempts, timestamps, outcomes)
- Deterministic end‑state (`failed-permanent`, `failed-transient`, etc.)

**Common failure modes:**

- Item is silently dropped — no record of failure
- Exception record exists but lacks a reason code or retry history
- End‑state is ambiguous (you cannot tell if the system will retry or has given up)

---

## T‑07: Export reproducibility

**Setup:** Run the same export scope twice (without intervening preservation events).

**Expected outcome:** Both exports produce the same items with matching cryptographic hashes. Manifests are consistent and exceptions are stable and explainable.

**Common failure modes:**

- Hash mismatches between runs (non‑deterministic serialization)
- Item counts differ between runs without explanation
- Manifest structure changes between runs

---

## See also

- [Section 6.3 — Minimum Conformance Tests](../06-evaluation-framework.md#63-minimum-conformance-tests) — authoritative test definitions
- [Conformance Declaration Template](conformance-declaration-template.md) — document your test results
- [Appendix B — Requirements](../appendix-b-requirements.md) — normative requirements mapped to conformance levels
