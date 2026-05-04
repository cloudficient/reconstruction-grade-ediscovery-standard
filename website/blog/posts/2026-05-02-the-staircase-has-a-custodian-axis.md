---
date: 2026-05-02
draft: false
description: "When the meet-and-confer turns to custodians, what framework determines who needs full-fidelity collection? A three-condition test for ESI protocol use."
authors:
  - brandondagostino
categories:
  - Legal Analysis
  - Standard Development
tags:
  - Custodians
  - Legal Hold
  - ESI Protocol
  - Proportionality
  - Rule 26(f)
  - Collaboration Platforms
  - RG-Aware
  - RG-Core
  - Preservation Gap
chat_prompts:
  - "How do I decide which custodians need higher-fidelity collection?"
  - "What goes into an ESI protocol clause for per-custodian collection scope?"
  - "How do I document the basis for not elevating a custodian to higher-fidelity collection?"
  - "Can a tiered preservation framework become a shield for under-collection?"
---

# The Staircase Has a Custodian Axis

![Four ascending platforms in a dark blue void, each topped by a glowing humanoid figure connected by light trails to floating document and link icons — the RGR staircase, custodian by custodian](../../images/blog/blog-staircase-custodian-axis.webp)

**The harder question on the RGR staircase isn't which step a matter belongs on — it's which step each custodian belongs on. A three-condition framework for allocating fidelity custodian by custodian, on the record at the Rule 26(f) conference.**

<!-- more -->

---

A [recent measurement post](2026-04-23-one-tenants-measurement-and-the-staircase.md) asked which step on the [Reconstruction-Grade eDiscovery Standard](../../) staircase a matter belongs on, and reported the first tenant-bounded measurement of how often linked Office documents drift after send: **81.9 percent** in one large M365 environment, on a platform-versioning measure.

The harder question is on which step of the staircase each custodian belongs.

The staircase has a custodian axis, and this post discusses how to use it.

## Tiering Custodians Is Not a Novel Move

Nothing about per-custodian fidelity allocation is novel in eDiscovery. Defensible practice already reserves forensic imaging for key custodians and uses logical collection elsewhere. Defensible practice already varies search-term aggressiveness, custodian interview depth, and review tier by role and exposure. It is settled that different custodians may warrant different treatment. The current question is whether there is *vocabulary* for that allocation at the collaboration-platform layer.

Until recently there was not. A producing party either "collected Teams" or it did not. A producing party either "collected linked attachments" or it did not. There was no third axis, fidelity per custodian, because there was no settled language for the gradient between "collected the link" and "preserved the as-sent version with audit trail and content hash."

The RGR staircase introduces that gradient: [RG-Aware](2026-04-07-the-dog-the-tail-and-the-staircase.md) at the bottom, [RG-Core](../../concepts/reconstruction-grade-ediscovery.md#rg-core-baseline-reconstruction-grade) in the middle, and the advanced tiers ([RG-Plus](../../concepts/reconstruction-grade-ediscovery.md#rg-plus-identity-and-behavior-conformance), [RG-Max](../../concepts/reconstruction-grade-ediscovery.md#rg-max-expanded-reconstruction-depth)) at the top. Once the gradient exists, custodian-by-custodian allocation becomes possible. And once allocation is possible, it becomes, for the first time, *negotiable* at the Rule 26(f) conference and *auditable* on the record.

## The Three Conformance Tiers, in Custodian-Allocation Language

Before we get into the decision framework, here is a brief restatement of the staircase from the perspective of how a custodian gets handled, rather than what a vendor product can do.

**RG-Aware custodian.** Same-tenant linked content is collected during preservation rather than excluded. Workflow capabilities and limits are disclosed in the ESI protocol. Failures to collect generate structured exception records. Matter-level documentation captures known [preservation gaps](../../concepts/preservation-gap.md) and [context gaps](../../concepts/context-gap-ediscovery.md). What RG-Aware does *not* require is per-link version resolution. At this tier, the producing party cannot answer, for any given link, whether the collected version is the as-sent version.

**RG-Core custodian.** Everything above, plus deterministic per-link version resolution. For an outbound shared link, the producing party can identify and produce the version that was actually transmitted at communication time, not whatever version happens to be current at collection time.

**RG-Plus / RG-Max custodian.** Advanced reconstruction-grade preservation: send-time content hash where available, version timeline, audit-evidence correlation, and documented ability to reconstruct the document state as closely as the platform evidence permits.

These are tier descriptions for *how this custodian is handled in this matter*, not labels on a vendor SKU. The same vendor stack could produce RG-Aware output for thirty custodians and RG-Core output for four of them in the same collection.

## A Proposed Decision Framework

This post proposes a framework in which custodian elevation up the staircase is driven by the intersection of three distinct conditions. No single condition is sufficient on its own; any two together support raising a custodian to RG-Core, and any one above a documented threshold does the same. The framework is offered for practitioner pressure-testing, not as a finalized rule.

**Condition 1: Role-based prior.** Static, custodian-specific, independent of the matter. Examples that may warrant default elevation:

- General Counsel, Chief Legal Officer, and direct reports.
- C-suite officers (CEO, CFO, COO) and named board members where their communications are within scope.
- Named parties to the matter.
- The custodian-of-record for any document set the matter turns on.
- Deal leads on transactional matters; principal investigators on regulatory matters.

These are roles whose outbound communications are foreseeably probative to facts at issue in the dispute, not merely incidental to it. For these custodians, per-link authenticity is not a technical refinement. It is often central to the preservation decision.

**Condition 2: Matter-type prior.** Matter-type prior creates a default elevation presumption for custodians whose role or communications intersect the factual narrative of that matter type. Matter classes where linked-content authenticity is foreseeably contested:

- Trade secret and IP misappropriation, where what the custodian saw, when, and which version was shared is often the case itself.
- M&A disputes where representations and warranties turn on document state at a specific date.
- Securities matters where disclosure adequacy is litigated.
- Employment matters with retaliation, discrimination, or whistleblower claims, where document timestamps and shared versions are probative.
- Regulatory investigations where the regulator's record-retention demands extend to linked content.

The default elevation extends to in-scope custodians whose role or communications intersect the factual narrative, not to every custodian within nominal scope. Custodians on the periphery of the matter (administrative support, finance back-office, unrelated functions) remain at RG-Aware unless context dictates otherwise.

**Condition 3: Communication-pattern signal.** Dynamic, measurable, custodian-specific within the matter. This is where matter-level measurement begins to inform custodian-level allocation.

A custodian whose outbound communication contains a high density of linked content, particularly to opposing-party-adjacent or external recipients, is a custodian whose linked-document send events are themselves likely to be evidentiary. The relevant measurement happens at preservation, not at guess: how many outbound shared links did this custodian send within the relevant period, to which recipients, on which platforms.

A documented threshold (for example, more than N outbound external links per week within the matter window) elevates a custodian even when role and matter signals are weak.

**The framework, stated as a sentence:** *A custodian receives RG-Core treatment when at least two of the three conditions above are true, or when any single condition exceeds the matter's documented threshold for that condition.*

### Documenting Non-Elevation in the Collection Memo

This is a framework that can be audited. The *basis for non-elevation is recorded*. Every custodian assigned to RG-Aware was assigned there by an affirmative determination against three named criteria, not by silent default. Practically, that means a one-line entry in the collection memo for each custodian held at RG-Aware: which conditions were considered, which did not fire, and why.

## A Worked Example

Consider a hypothetical: a mid-size enterprise faces a trade secret misappropriation matter brought by a former engineering director. The complaint identifies a window of approximately fourteen months and references documents shared via Teams and SharePoint. Forty custodians are identified after initial scoping.

Applied to the framework:

- **Six custodians** elevate on Role alone above threshold: the former director (named party), the CTO and VP of Engineering (direct supervisors during the window), the General Counsel and Deputy GC (involved in the post-departure investigation), and the Director of Information Security (custodian-of-record for the access logs the matter relies on).
- **Matter type is "trade secret,"** a matter class where elevation is the default for custodians whose role or communications intersect the factual narrative. The narrative bounds to the engineering organization (twenty-two custodians) and the directly adjacent legal and security functions (eight custodians), each of whom touch the at-issue documents, communications, or investigation. The remaining ten custodians (HR, finance support, executive assistants outside the principal chain) sit on the periphery; their role and communications do not intersect the factual narrative, so the elevation presumption does not extend to them. The basis for that boundary is captured in writing in the collection memo before collection begins.
- **Condition 3** then re-elevates two custodians from the peripheral set back to RG-Core: an HR business partner whose communication-pattern data shows substantial outbound linked content to external counsel during the window, and an executive assistant whose calendar-related linked sends connect the deal lead to outside parties.

**Final allocation:** thirty-two RG-Core custodians and eight RG-Aware custodians. Every RG-Aware assignment has a one-line basis statement in the collection memo identifying which signals were considered and why elevation was not warranted. Every RG-Core assignment is similarly documented.

The exact numbers are illustrative; the structure is the artifact. A practitioner reading this post should be able to produce the same kind of memo for a real matter the same week.

## What Goes in the ESI Protocol

The decision framework lives outside the ESI protocol, in the producing party's collection memo. What enters the ESI protocol is the *posture*: that the producing party is allocating custodians to staircase tiers under a documented framework, that custodian-tier assignments are available on request and subject to the customary meet-and-confer process, and that exception records will be produced when collection encounters preservation-gap conditions.

Concretely, an ESI protocol clause might read:

> "Producing party will allocate custodians to RGR treatment tiers (RG-Aware or RG-Core) under a documented framework that considers custodian role, matter type, and communication-pattern signals. Custodian-tier assignments will be available to requesting party on reasonable request. For custodians assigned to RG-Aware, producing party will disclose known workflow limits and generate structured exception records for linked content that could not be collected, resolved, or otherwise preserved within the declared workflow. Producing party preserves the right to elevate any custodian's tier mid-collection upon discovery of new information; demotion below an initial tier assignment will be undertaken only on documented basis."

This is sample text, not a model clause. The point is that the language exists for the negotiation to happen at all, and the language tracks the staircase, the custodian axis, and the documented basis.

## The "Shield" Concern

A reasonable concern with tiered conformance is that it could become a shield, giving producing parties vocabulary to do less rather than more. The custodian axis is the most plausible vector for that critique. If a producing party can place every custodian at RG-Aware, then the staircase has been weaponized: the lowest tier becomes the universal default, and the higher tiers exist as theoretical aspirations.

The decision framework above tests that critique structurally.

A producing party that places every custodian at RG-Aware has now made an *affirmative claim*, in writing, that no custodian on the matter satisfies any of the three signals at any threshold. That claim is testable against the record. For any named custodian, the question becomes whether role, matter-type, and communication-pattern signals warranted elevation, and what basis supported the determination that they did not. A motion to compel, if one arises, becomes a custodian-by-custodian inquiry rather than an undifferentiated complaint about under-collection.

The shield only works in the absence of vocabulary. Once the staircase exists with its custodian axis, every allocation is on the record. *Proportionality with a paper trail is not a shield. Proportionality without one is.*

## Where This Leaves the Standard

The measurement post asked what the staircase should look like at the matter level. This post asks what it should look like at the custodian level. Both are necessary.

The next questions on the bench are operational: what does the exception-record format look like in practice; how should a meet-and-confer transcript that successfully negotiates custodian-tier assignments read; what does a matter that *demoted* a custodian from RG-Core to RG-Aware mid-collection look like, and what record did the producing party keep of that demotion. Companion posts will address each in turn.

The Reconstruction-Grade eDiscovery Standard does not adjudicate these questions one matter at a time. What it does is provide the vocabulary, the staircase, the tiers, and now the custodian axis, so that producing parties, requesting parties, and tribunals have language to negotiate proportional fidelity rather than re-litigate it from first principles every time a Teams collection comes up.

That is the work this post is meant to advance.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I decide which custodians need higher-fidelity collection?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Under the proposed three-condition framework, a custodian receives RG-Core treatment when at least two of three conditions are true: a role-based prior (e.g., named parties, General Counsel, C-suite officers, custodian-of-record), a matter-type prior (e.g., trade secret, M&A, securities, employment retaliation, regulatory), or a communication-pattern signal (high density of outbound shared links to external recipients within the matter window). A single condition above a documented threshold also elevates the custodian."
      }
    },
    {
      "@type": "Question",
      "name": "What goes into an ESI protocol clause for per-custodian collection scope?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The ESI protocol states that the producing party allocates custodians to RGR treatment tiers (RG-Aware or RG-Core) under a documented framework considering custodian role, matter type, and communication-pattern signals. Custodian-tier assignments are available to the requesting party on reasonable request. For RG-Aware custodians, workflow limits are disclosed and structured exception records are produced for linked content that could not be collected, resolved, or otherwise preserved within the declared workflow. The producing party preserves the right to elevate any custodian's tier mid-collection upon discovery of new information; demotion below an initial tier assignment is undertaken only on documented basis."
      }
    },
    {
      "@type": "Question",
      "name": "How do I document the basis for not elevating a custodian to higher-fidelity collection?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every custodian assigned to RG-Aware should have a one-line basis statement in the collection memo identifying which of the three conditions were considered (role, matter type, communication pattern) and why elevation was not warranted. The artifact is the affirmative determination against named criteria — assignment by silent default does not satisfy auditability. The same memo also records the boundary of the matter's factual narrative that defined which custodians the matter-type elevation presumption did or did not extend to."
      }
    },
    {
      "@type": "Question",
      "name": "Can a tiered preservation framework become a shield for under-collection?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only in the absence of documented basis. A producing party that places every custodian at RG-Aware has made an affirmative claim, in writing, that no custodian on the matter satisfies any of the three conditions at any threshold. That claim is testable against the record, and a motion to compel becomes a custodian-by-custodian inquiry rather than an undifferentiated complaint about under-collection. Proportionality with a paper trail is not a shield. Proportionality without one is."
      }
    }
  ]
}
</script>
