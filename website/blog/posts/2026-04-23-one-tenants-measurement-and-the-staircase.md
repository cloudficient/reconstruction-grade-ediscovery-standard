---
date: 2026-04-23
draft: false
description: "A first empirical measurement of linked-document drift after email send in one enterprise tenant, and what it suggests for the RGR conformance staircase."
authors:
  - peterkozak
categories:
  - Research & Dialogue
  - Standard Development
tags:
  - Linked Attachments
  - Microsoft 365
  - Preservation Gap
  - RG-Aware
  - Craig Ball
  - Benchmarking
chat_prompts:
  - "How often do linked documents change after they're sent?"
  - "What did a first tenant measurement show about Office document version drift?"
  - "How should the RGR standard respond to empirical evidence about version drift?"
  - "Is linked-document version change purely platform noise, or is it real?"
---

# What One Tenant's Measurement Suggests for the RGR Staircase

![A tape measure extended across a document on a dark desk, teal layout blocks beneath the tape — measurement applied to content that had previously been intuition](../../images/blog/blog-first-measurement-staircase.webp)

**A first tenant-bounded measurement of linked-document version drift, on a platform-versioning measure — and what it suggests for the standard's conformance staircase.**

<!-- more -->

---

A recurring question in modern preservation is how often a [linked document](../../concepts/modern-attachments.md) in an email — a Word file, a PowerPoint deck, an Excel workbook shared by link rather than attachment — still matches its send-time state by the time anyone goes looking for it. It is the question that sits behind every "did we produce the right version?" dispute, every [Rule 37(e)](2026-03-31-what-frcp-rule-37e-means-for-modern-collaboration-platforms.md) argument about whether preservation was reasonable, and every vendor claim that a modern collection workflow is sufficient.

Craig Ball posed that question publicly in his April 2, 2026 essay *A Dog and Its Tail: Don't Let Version Uncertainty Cloud Linked Attachment Production*. The essay made two arguments. First — the "dog" — that collecting and searching linked attachments is a threshold discovery obligation, "full stop." Second — the "tail" — that getting the precise as-sent version of a linked file is aspirational, important, and solvable over time. In between, Craig asked the empirical question at the center of this post, and was candid that his own answer was a guess: his stated intuition was that fewer than 10 to 20 percent of linked attachments are meaningfully modified after being shared, while emphasizing that this was belief rather than evidence and calling for the industry to measure it.

A companion Cloudficient post now reports a first tenant-bounded measurement prompted by that public question: [How Often Do Linked Documents Change After Send?](https://www.cloudficient.com/blog/how-often-do-linked-documents-change-after-send). The measurement is one large Microsoft 365 environment, ~9 million captured send events, 10,000 randomly sampled links, and a clean denominator of 6,098 non-`.aspx` file-link rows where both the Graph lookup succeeded and the preservation system had captured a send-time version identifier. The definition of "changed" is specific and worth naming up front:

> **In this first run, a file is classified as changed when the Microsoft version identifier returned at query time differs from the version identifier preserved at send time. This is a platform-versioning measure. It is not a hash-level or semantic comparison of file contents, and it may therefore include version increments associated with autosave, co-authoring, or other platform activity that would not necessarily amount to a reader-visible substantive edit. A hash-level follow-up on the subset where the as-sent content was preserved is the appropriate next refinement, and is planned as a separate measurement.**

Within that boundary, on the clean denominator of 6,098 non-`.aspx` linked-document rows: **75.3 percent no longer carried the same Microsoft version identifier at query time that they carried at send time.** Across the Microsoft Office document types that dominate modern discovery — Word, PowerPoint, and Excel — the figure rises to **81.9 percent**. Of the 4,592 rows that changed, 30.5 percent had reached their current latest-version timestamp within one week of send; more than half had done so within thirty days.

The first measurement came in materially above the provisional 10–20 percent intuition Craig offered in the essay, but it does so on a platform-versioning measure rather than a content-level comparison, and should be read within that boundary. This post does not treat the result as a final answer. It considers what the result, taken on its own terms, suggests for the Reconstruction-Grade eDiscovery Standard's transparency and collection floor.

## The Dog Is Still the Dog

Craig's central argument is not the 10–20 percent estimate — it is that versioning uncertainty has been "weaponized" as a reason to produce nothing rather than produce imperfectly. The dog — collection of linked attachments as a threshold discovery obligation — is undisturbed by anything in the measurement.

If anything, the measurement *reinforces* the dog. When 81.9 percent of linked Office documents no longer match their send-time version identifier — even allowing that some portion of that figure is autosave, co-authoring, or other platform-layer activity a hash-level comparison would filter out — a party that waits until versioning is perfect is a party whose evidence continues to move in the meantime. Collection cannot wait for perfect tooling. The obligation runs now, with whatever level of capability a party can defend, and with transparent disclosure of what it could not capture. That is the point the essay made. This first measurement is consistent with it.

## What the Measurement Adds at the Platform-Versioning Layer

One feature of the dataset is worth naming because it addresses the natural skepticism the headline number provokes. If the measurement were catching autosave-generated version increments or routine platform touches uniformly across all file types, PDFs in the same sample would drift comparably. They do not: PDFs moved in only 8.4 percent of cases, and saved-email files and videos moved close to zero. The contrast between file types that should be stable and file types that should churn makes a purely uniform platform-noise explanation less persuasive — a pure-noise story would have to explain why that noise is absent from PDFs, MSGs, and MP4s in the same tenant. It does not, however, settle the separate question of substantive materiality at the content layer. A hash-level follow-up on the subset where the archive preserved the as-sent content is the next refinement, though a substantive-content comparison layer on top of it is what would most directly answer the substantive-modification question. Both are scoped as companion studies.

Two additional cuts of the data are worth naming, within the same versioning boundary. First, velocity, measured as elapsed time between the preserved input-version timestamp and the current latest-version timestamp: 30.5 percent of the rows that changed had reached their current latest-version timestamp within one week of send, and more than half within thirty days. Whatever the mix of substantive editing, autosave, and co-authoring activity beneath that signal, the version state of linked Office documents does not stabilize after send. Second, multiplicity, measured as the arithmetic difference between preserved and current numeric version identifiers: across the 4,583 rows with a positive numeric version difference, the median was **17**, with a long right tail (p90 = 146, max = 1,704). Among Office-document rows, the median positive version difference was 18; among PDFs that changed, the median positive version difference was **1**. The numeric difference is not a literal count of distinct substantive edits — SharePoint minor versions produce fractional increments, and autosave generates new identifiers without substantive edit — but the file-type contrast at the intensity layer parallels the contrast at the prevalence layer.

The data also confirms, in numbers, the distinction Craig drew between two failure modes: *"Producing the 'wrong' version of a responsive document is a problem. Producing no version of a responsive document is a bigger problem."* In the measured tenant, there is often a version-drift candidate to worry about at the platform layer — 75.3 percent across the clean headline denominator, and 81.9 percent for linked Office-document rows. There is also a "no version" outcome — the 2.1 percent of links that failed to resolve at all because of deletion, file-not-found outcomes, access or sharing-link failures, blocked sites, or other [preservation-gap](../../concepts/preservation-gap.md) conditions. Both categories matter. Both are measurable. Neither is hypothetical.

## The Staircase — Where Measurement Meets Practice

Accepting the dog and the tail as Craig framed them still leaves the practitioner question: *what do I actually do tomorrow?*

That is what the Reconstruction-Grade eDiscovery Standard's tiered conformance levels are for. The standard treats full reconstruction-grade preservation (RG-Core and above) as a ceiling the industry is building toward, not a ticket for admission. Below that ceiling, it names the intermediate steps that are operationally achievable today and the specific capabilities that separate each step from the next — a staircase.

Version 0.54 of the standard, published April 6, 2026 — in direct response to Craig's "shield" concern that conformance levels could be cited as a reason to do nothing — introduced a new step at the bottom of the staircase: **RG-Aware**.

RG-Aware does not require content reconstruction. It requires four things:

1. Collection of hyperlinked content from same-tenant storage when identified during preservation workflows — rather than limiting collection to whatever happened to sit inside the custodian's mailbox.
2. Disclosure, through Rule 26(f) conferences, ESI protocols, or equivalent mechanisms, of whether the preservation workflow can identify linked content outside the custodian container and whether collected versions reflect communication-time state.
3. Structured exception records when linked content cannot be collected — permission denied, content expired, out-of-scope storage — rather than silent loss.
4. Matter-level documentation of known [preservation](../../concepts/preservation-gap.md) and [context gaps](../../concepts/context-gap-ediscovery.md), so the record of what the workflow could and could not capture travels with the production rather than being reconstructed retrospectively.

An organization at RG-Aware has committed to a specific posture: it collects rather than excludes, it discloses the capabilities and limits of its workflow to the tribunal and to opposing counsel, and it generates auditable exception records when collection fails. That is materially different from producing whatever version happens to exist at collection time and declining to discuss the gap. RG-Aware does *not* require deterministic per-link version resolution — the capability to answer, for a specific file, "is this the as-sent version?" — which is a higher step on the staircase. What it requires is that the producing party *know, and state*, what its preservation workflow can and cannot do, and produce structured records when it cannot.

This first measurement strengthens the case for a transparency-and-collection floor such as RG-Aware, because it shows that link state is often not stable at later query time in at least one large enterprise tenant. The precise rate, and the share corresponding to substantive content change rather than other version-generating platform activity, remain questions for follow-on measurement. Even allowing for that, version drift at the magnitude observed here — on the most inclusive definition available — makes it difficult to treat a transparency-and-collection floor as an overengineered response to a rare problem. The measurement is relevant to the staircase because it helps test whether a transparency-and-collection floor is addressing a marginal problem or a common one. This first run suggests the latter, at least within the tenant and measurement layer studied here.

A companion post on this blog will apply the staircase across custodians — mirroring the established practice of reserving higher-fidelity collection (forensic imaging, key-custodian treatment) for matters and custodians where the stakes warrant, and RG-Aware posture elsewhere. Proportional allocation of fidelity is a familiar move in eDiscovery; the staircase simply names it at the collaboration-platform layer, and reframes the "shield" concern as a question of *where* effort goes rather than *whether* effort happens.

## What the Measurement Does Not Yet Say

This is one tenant. One run. One channel — email. Several important boundaries are worth holding in view:

- **The definition of change is platform-versioning, not content-level.** A file was classified as changed when the current Microsoft version identifier differs from the one preserved at send time. This is a platform-versioning measure, not a hash-level or semantic-delta measure. Autosave and co-authoring sessions do generate new version identifiers without substantive edit, so the count necessarily includes some modifications that a content-level comparison would not flag. The PDF contrast described above is evidence against the interpretation that the 81.9 percent is purely platform-layer noise. A hash-level follow-up on the subset where as-sent content was preserved is the next refinement, and a substantive-content comparison layer on top of it is what would most directly answer the substantive-modification question. The standard will watch both — and whatever other companion studies the field produces — as evidence on this question accumulates.
- **Lifecycle events are bucketed separately.** Links that were deleted, moved, renamed, or rendered inaccessible between send and query are *not* folded into the 81.9-percent version-drift rate. They are the 2.1 percent of links that failed to resolve, and they are reported as a distinct preservation-gap statistic.
- **Retention aging.** The next measurement will ask not only *is the as-sent version still current?* but also *is the as-sent version still retrievable from the platform's version history at all?* The second statistic speaks directly to whether the as-sent file is recoverable today by any practitioner, not just by one whose preservation system captured the version identifier at the right moment.
- **Cross-tenant comparison — and boundary of the headline.** A large enterprise tenant operating a knowledge-work-heavy document population will likely show higher version-drift rates than tenants with more static document bases. Readers should treat the 81.9 percent as a tenant-bounded figure on a platform-versioning measure, not a cross-sector default and not a content-level rate. Additional tenants in other industry segments are next; when results accumulate, the sector-correlation question becomes answerable rather than assumable.
- **Non-email channels.** Teams messages, channel posts, and other in-platform sharing events were out of scope for this run. A Teams-channel study is a separate workstream.
- **Materiality.** The measurement does not judge whether any specific modification was legally consequential. That is matter-specific human review. What the measurement establishes is that the *presumption* of a stable linked file is not supported by how the platform actually behaves.

## What the Standard Does Next

The 81.9 percent figure sharpens the case for what constitutes a reasonable preservation floor, and the standard will track that as subsequent measurements — including the hash-level refinement — refine it. Concretely:

- **This first measurement strengthens the empirical case for retaining RG-Aware on the staircase.** Early adopters of RG-Aware now have an initial data point they can point to when explaining why the floor exists.
- **Retention-aging is a likely addition to the conformance requirements.** When the second measurement lands — specifically the statistic on how often the as-sent version has been purged from the platform entirely — the standard will evaluate whether the relevant conformance tier should acquire an explicit capability test around it.
- **Reproducibility is the evidence bar the standard applies.** Measurements that inform conformance requirements should be independently reproducible on public methodology — so the evidence base, as it accumulates, does not depend on any one implementer. The standard aggregates evidence produced by implementers, practitioners, and independent researchers; it does not produce or publish measurements itself.

## Where This Leaves the Standard

A public empirical question about linked-document drift has now received one tenant-bounded answer at the platform-versioning layer. That answer is materially above the informal intuitions that have circulated in the field, but it is not a settled content-level rate, and it is not a cross-sector default. Further measurement — a hash-level refinement on the subset where as-sent content was preserved, additional tenants, retention aging, Teams-native sharing — will refine the picture in specific, scoped ways, each reported on its own footing when complete.

The role of the Reconstruction-Grade eDiscovery Standard in that sequence is not to adjudicate the content-level question one measurement at a time. It is to translate accumulating evidence into transparent capability language — so that producing parties, requesting parties, and tribunals can talk about preservation posture in terms that do not depend on any single vendor's claims or any one tenant's numbers.

On the evidence available today: the dog is undisturbed — collection of linked attachments is a threshold discovery obligation, with or without perfect versioning. The tail is, at a minimum, not the edge case that the oldest industry assumptions treated it as. And the staircase — the calibrated set of capability steps from RG-Aware upward — is the standards language for *"do what you can now, document what you can't, and improve over time"* when translated into conformance requirements.
