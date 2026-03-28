---
description: Deterministic resolution algorithms and processing profiles for reproducible evidence handling, including as-sent version resolution for eDiscovery systems.
---

# Appendix I: Deterministic Resolution and Processing Profiles

This appendix provides non-normative algorithm sketches that illustrate deterministic processing. Implementations will vary, but outcomes must be reproducible.

## I.1 As-Sent Version Resolution (Conceptual)

Inputs: messageTimestamp, linkReference

1) Resolve linkReference to underlying object using canonicalization + platform APIs

2) Enumerate object versions with (versionId, lastModifiedDateTime)

3) CandidateVersions = { v | v.lastModifiedDateTime <= messageTimestamp }

4) If CandidateVersions is empty:

Record fallback rule; emit exception or select earliest available per policy

Else:

Select v* = argmax(CandidateVersions.lastModifiedDateTime)

If ties on timestamp: select highest versionId per deterministic ordering

5) Preserve bytes(v*), metadata(v*), versionId(v*)

6) Persist binding: (messageId -> link -> objectId -> versionId) with provenance

## I.2 Exception and Retry Handling (Conceptual)

When a linked object cannot be collected:

- Create ExceptionRecord { originalReference, resolvedIds, reasonCode, attempts[] }

- attempts[] includes { attemptTime, outcome, errorDetail, backoffApplied }

- Retry bounded times for transient conditions (e.g., throttling)

- Mark deterministic end state when retries exhausted

- Allow reprocessing after remediation while preserving attempt history
