# 2. The Context Collapse Problem

Context collapse occurs when collaborative evidence is flattened into files and messages that cannot carry the full burden of explanation. The result is not merely inefficiency. It is [reconstruction](concepts/evidence-reconstruction.md) failure: the inability to reproduce what the actors experienced at the time. Context collapse is the primary mechanism through which the [Context Gap](concepts/context-gap-ediscovery.md) manifests in practice.

## 2.1 Failure Mode: Final-State Collection

Final-state collection captures what exists today. It does not capture what existed at the relevant time, what was shared, what was relied upon, or what version was accessible when a communication occurred.

In collaborative systems, "latest" is not a substitute for "as-of." When the evidence model treats it as such, the record becomes time-shifted.

## 2.2 Failure Mode: Archive-Everything-First

Archive-everything-first strategies assume that comprehensive capture is the path to defensibility. At enterprise scale, this approach often delays legal outcomes.

Two realities dominate: (1) preserved footprint grows non-linearly once version history and indexing are included, and (2) Microsoft 365 service limits (API throttling), permissions, retries, and network egress govern time-to-ingest.

## 2.3 Failure Mode: Static Identity and Custodian-Centric Scoping

Custodian-centric scoping assumes that ownership maps to relevance and that repository boundaries align with work boundaries. Modern work is cross-functional, link-based, and shared. Relevant artifacts frequently reside outside the custodian's owned spaces.

## 2.4 Failure Mode: Permission-Based Inference

Inferring access from permissions is convenient but methodologically weak. It produces statements like "it appears that..." rather than "the preserved record shows that...". Under scrutiny, inferred narratives are fragile.

## 2.5 Practical Symptoms of Context Collapse

- Escalating over-collection due to uncertainty about where relevant content lived.
- Version explosion in review datasets without a defensible rule for which versions matter.
- Inability to explain which document state informed a decision at a given time.
- Difficulty defending proportionality decisions because scope was not evidence-based.
- Gaps in "who saw what, when" because audit signals were not preserved or correlated.
