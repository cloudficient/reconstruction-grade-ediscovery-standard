---
date: 2026-03-26
draft: false
description: "Why most eDiscovery tools fail a basic modern attachment test: resolving the correct as-sent document version from a SharePoint link in Microsoft 365 email."
authors:
  - peterkozak
categories:
  - Industry Analysis
tags:
  - eDiscovery
  - Reconstruction-Grade
  - Modern Attachments
  - Microsoft 365
  - Benchmarking
---

# The Simplest E-Discovery Test Most Tools Would Fail

*When a SharePoint link resolves successfully but the produced document is not the version that existed at send time, the evidentiary record is silently wrong.*

Consider a scenario that should be unremarkable. A company discovers a potential data breach. Incident response begins.

At 7:15 p.m. on a Wednesday, the CISO emails the customer support lead, the communications director, and the product VP:

> *"Attached is the draft customer FAQ for tomorrow morning in case we need it. Please review before end of day."*

<!-- more -->

The attachment is a SharePoint link to a live document: *Incident FAQ - External Use.docx*.

At the time the email is sent, the FAQ states that the company is investigating suspicious activity, has found no evidence of data exfiltration, and believes the incident window was limited to a few hours on a single system.

At 1:30 a.m., the forensic firm delivers an updated timeline. The scope of the incident has changed materially. The CISO reopens the same document and revises it. The updated version states that exfiltration is now suspected, two customer datasets may be affected, and the intrusion may have begun more than a week earlier.

The document is the same. The SharePoint link is the same. The content is not.

The FAQ is ultimately never sent to customers. The company issues a different public statement several days later, once the facts are confirmed. But the SharePoint document — the one linked in the 7:15 p.m. email — now reflects the 1:30 a.m. revision. The original version is still in SharePoint's version history, but nothing in a standard collection workflow will associate it with the 7:15 p.m. email. The link resolves to the current version.

<hr class="rgr-divider">

## The Discovery Problem

A year later, the company faces consumer litigation and regulatory scrutiny. A central question in both proceedings: **when did the company first understand the breach was broader than initially reported?**

The CISO's 7:15 p.m. email is collected as part of the discovery process. The SharePoint link is resolved. The document is produced into the review set.

A reviewer opens the email. It says: *attached is the draft customer FAQ, please review.* The reviewer opens the linked document. It describes suspected exfiltration, two affected datasets, and an intrusion window exceeding one week.

The email is there. The document is there. The link resolved. Nothing in the review workflow signals a discrepancy.

But the document the reviewer is reading is not the document the CISO was referring to at 7:15 p.m. At that time, the FAQ described a limited incident with no evidence of exfiltration. The version describing a broader breach did not exist until 1:30 a.m. — after the forensic firm's update.

The produced record now places the more serious version of the FAQ next to an email sent six hours earlier, creating the impression that the company was already preparing external messaging around a broader breach before the forensic findings were delivered. That misalignment — between what was communicated and what was later collected — may not be apparent to anyone in the review workflow.

## Why This Happens

In legacy email, attachments were embedded in the message body. A file sent with an email was frozen at send time. Open the message years later, and the attachment is unchanged.

Microsoft 365 introduced a different model. In many enterprise workflows, an email no longer carries the file itself. It carries a reference — a link — to a document that continues to exist and evolve in SharePoint or OneDrive. The link may remain stable while the underlying document accumulates new versions.

A collection workflow can therefore resolve a link, retrieve a document, and produce a file that is authentic as a file object — yet is not the version that existed when the communication was sent.

This is what the Reconstruction-Grade eDiscovery Standard refers to as the **[modern attachment](../../concepts/modern-attachments.md) problem**: the document is present, but the point-in-time relationship between the communication and the correct version has not been preserved.

## What This Implies for Defensibility

The scenario above is not exotic. It requires only the conditions that exist in most Microsoft 365 environments today:

- An email containing a SharePoint link
- A document that was edited after the email was sent
- A collection that occurred after the edit

No data was deleted. No evidence was tampered with. The workflow operated as designed. And the resulting record does not reflect what was communicated at the time the email was sent.

A diligent team can work around this. They can collect all SharePoint versions, examine timestamps, and manually correlate the correct version to each email. In a focused investigation with a handful of key documents, that is feasible — and teams do it today.

But that workaround depends on knowing the problem exists in the first place. This is the kind of failure that does not announce itself. A reviewer examining the email and the linked document has no inherent reason to question whether they represent the same point in time. If the workflow does not flag the discrepancy, the team may never realize there is a version to investigate.

And the manual approach does not scale. A matter with thousands of custodian emails containing SharePoint links to hundreds of documents — each with multiple versions — cannot be reconstructed by hand at reasonable cost. The version correlation has to be an automated capability of the workflow, not an ad hoc exercise applied selectively to documents that happen to attract scrutiny.

That is the practical case for treating version determinism as a baseline requirement rather than a manual workaround: not because the workaround is impossible, but because it is silent, expensive, and unreliable at scale.

## When the Link Dies

The version problem assumes the document still exists. Sometimes it doesn't.

User A sends User B an email with a hyperlink to a document in B's OneDrive. A gets placed on legal hold. B doesn't. The document hits its retention limit and expires.

A's email is preserved — but the link is now dead. The hold on A didn't cascade to B's storage. You can prove the email existed, but you can't reconstruct what was actually shared.

Under Rule 37(e), was that "reasonable steps"? The party preserved the custodian's mailbox. The hold executed correctly. But the evidence relationship — the binding between the communication and the content it referenced — was never within scope. The hold preserved the pointer. The thing it pointed to was in a different custodian's storage, governed by a different retention policy, with no hold in place.

Courts are [increasingly testing](../../judicial-signals.md) what "reasonable" means for exactly this kind of failure — where the workflow operated as designed but the evidence model it was designed for no longer matches how people actually share information.

<hr class="rgr-divider">

## The Baseline Requirement

The [Reconstruction-Grade eDiscovery Standard](https://rgrstandard.org) addresses this problem directly. Before evaluating more complex challenges — [identity drift](../../concepts/identity-drift.md), observed-access correlation, cross-platform evidence chains — the standard asks a more fundamental question:

<div class="rgr-callout" markdown>

**If an email contains a link to a SharePoint document, can the workflow determine which version of that document existed when the email was sent?**

</div>

That is not an advanced requirement. It is a baseline. If a workflow cannot answer it in a simple, two-party scenario, broader claims about faithful reconstruction of collaborative evidence are premature.

At minimum, a compliant workflow must preserve:

- The message containing the link
- The identity of the referenced SharePoint item
- The version chain of that item
- The rule for resolving which version existed at send time
- The binding between that specific communication and that specific version
- Reproducible export evidence demonstrating that the same scope yields the same result

The standard captures these through **version determinism**, **[modern attachment](../../concepts/modern-attachments.md) binding**, and **export reproducibility** — baseline conformance requirements, not aspirational targets.

## A Practical Question

How many matters currently in your portfolio include custodian emails with links to SharePoint or OneDrive documents? How many of those documents were modified after the email was sent? And how many review teams are in a position to confirm that the version in the review set is the version that existed at the time of the communication?

These are not theoretical concerns. They are practical questions about whether the evidentiary record reflects the chronology it appears to reflect — and whether the workflow that produced it can demonstrate that it does.

<div class="rgr-highlight" markdown>

**The question worth asking**

The next time a review set includes an email with a SharePoint or OneDrive link:

*Is this the version that was sent, or the version that was collected?*

If the workflow cannot answer that in a defensible, reproducible way, it is not yet reconstructing collaborative evidence with point-in-time fidelity.

It may still be collecting documents. It may still be populating a review set. But it is not preserving the evidentiary record as it existed at the time of the communication.

That is the simplest e-discovery test most tools would fail — and the reason the [Reconstruction-Grade eDiscovery Standard](https://rgrstandard.org) begins there.

</div>

---

**Explore the standard:**

- [Modern Attachments](../../concepts/modern-attachments.md) — the concept behind the hyperlinked-file problem described above
- [The Context Gap in eDiscovery](../../concepts/context-gap-ediscovery.md) — how collaborative platforms broke traditional collection assumptions
- [What Is Reconstruction-Grade eDiscovery?](../../concepts/reconstruction-grade-ediscovery.md) — conformance levels and the evidence model
- [Defining Reconstruction-Grade eDiscovery](../../03-defining-reconstruction-grade.md) — the full standard chapter on version determinism and as-sent resolution
- [Reconstruction Scenarios](../../appendix-d-reconstruction-scenarios.md) — concrete scenarios including hyperlinked attachment after-the-fact edits
- [Vendor Scoring Worksheet](../../appendix-h-vendor-scoring.md) — evaluate whether your tools handle this test
- [ESI Protocol Addendum](../../toolkit/esi-protocol-addendum.md) — starter language for addressing collaborative evidence in ESI protocols
