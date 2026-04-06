---
date: 2026-04-07
draft: false
description: "Craig Ball says collect linked attachments first, worry about versions later. We agree—and introduce RG-Aware, a pre-conformance tier for the preservation gap."
authors:
  - peterkozak
categories:
  - Standard Development
  - Industry Response
tags:
  - Craig Ball
  - Linked Attachments
  - Preservation Gap
  - Context Gap
  - RG-Aware
  - Conformance
  - Reconstruction-Grade
  - eDiscovery
chat_prompts:
  - "What is RG-Aware and how does it differ from RG-Core?"
  - "How did Craig Ball's assessment change the RGR Standard?"
  - "What are the conformance levels in the RGR Standard?"
  - "Can the RGR Standard be used as a shield against collecting linked attachments?"
---

# The Dog, the Tail, and the Staircase

![Staircase ascending into darkness — the first step lit in teal](../../images/blog/blog-dog-tail-staircase.webp)

**Craig Ball's engagement with the RGR Standard surfaced a real vulnerability in the conformance model. Here's the conversation — and what it led to.**

<!-- more -->

---

Craig Ball recently published [*A Dog and Its Tail: Don't Let Version Uncertainty Cloud Linked Attachment Production*](https://craigball.net/2026/04/02/a-dog-and-its-tail-dont-let-version-uncertainty-cloud-linked-attachment-production/), engaging directly with the Reconstruction-Grade eDiscovery Standard. Doug Austin picked it up on [eDiscovery Today](https://ediscoverytoday.com/2026/04/06/assessment-of-the-reconstruction-grade-ediscovery-standard-by-craig-ball-ediscovery-best-practices/).

Craig called the standard "ambitious and thoughtful" and said he wanted to engage constructively because "I think it gets several things right." Then he raised a concern we hadn't fully seen ourselves.

This post is a response to that. Not a rebuttal. A continuation of the conversation.

One point should be clear from the outset: **failure to achieve reconstruction-grade fidelity does not excuse failure to collect linked attachments.** That concern is at the heart of Craig's post, and it is now explicitly addressed in the standard.

## The Vulnerability Craig Found

Craig has been writing about linked attachments since his March and April 2024 posts — arguing that producing parties have been avoiding collection and search of hyperlinked content, and that the excuses don't hold up. Since then, his core proposition hasn't changed. If anything, *Carvana*, the Sedona Commentary, and the emergence of the RGR Standard itself have reinforced it.

But Craig spotted a new risk. The versioning question — *which version* of a linked document is the right one — is being elevated in ways that could become the next excuse for non-production. His concern: a standard with three conformance levels could be turned into a shield by a producing party arguing that because it can't achieve even baseline conformance, it shouldn't be required to attempt collection of linked attachments at all.

That's the tail wagging the dog. The difficulty of determining which version was communicated becomes a reason to avoid collecting *any* version — even though the threshold obligation to collect and search [linked attachments](../../concepts/modern-attachments.md) has nothing to do with version resolution.

Craig put it simply: "Producing the 'wrong' version of a responsive document is a problem. Producing *no* version of a responsive document is a bigger problem."

We couldn't agree more. And when we looked at the standard through that lens, we saw the gap he was pointing at.

## What the Standard Left Implicit

The standard's lowest conformance level — RG-Core — requires deterministic as-sent version resolution. That's the right technical bar for reconstruction-grade claims. But in practice, the standard left implicit something that needed to be explicit: the gap between "non-conformant" and "RG-Core" was wide enough that a producing party could read it as binary — either you reconstruct, or you're excused.

Craig identified the floor the standard was missing: "The floor is not reconstruction-grade fidelity. The floor is reasonable steps under Rule 37(e) and the obligation to search and produce relevant, responsive, non-privileged material."

That floor was implicit in everything we'd written — particularly in the [adversarial stress test](../posts/2026-04-02-i-tried-to-break-the-preservation-gap-argument.md#four-questions-any-practitioner-can-raise-today) of the Preservation Gap argument, where we arrived at structured transparency as the minimum defensible posture. But it wasn't in the standard itself. Craig's post made it clear that implicit wasn't good enough.

## RG-Aware: The Missing First Step

Version 0.54 of the standard introduces **RG-Aware** — a pre-conformance adoption tier beneath RG-Core, RG-Plus, and RG-Max.

RG-Aware doesn't lower the reconstruction-grade bar. It formalizes the floor — a standards floor for transparent practice, not a claim about the legal sufficiency of any particular matter response. An organization operating at RG-Aware:

- **Collects** hyperlinked and modern attachment content from same-tenant storage as part of reasonable steps to preserve and collect linked content, rather than treating the custodian container as the boundary of preservation.
- **Discloses** its limitations — whether the workflow identifies linked content outside the custodian scope, and whether collected versions reflect communication-time state — through Rule 26(f) conferences, ESI protocols, or equivalent mechanisms.
- **Generates structured exceptions** when linked content can't be collected, with reason codes and timestamps, rather than allowing silent loss.
- **Documents** known preservation and context gaps at the matter level.

No deterministic version resolution required. No specialized tooling required. Just collection, transparency, and documentation. The four actions map directly to the [practitioner questions](../posts/2026-04-02-i-tried-to-break-the-preservation-gap-argument.md#four-questions-any-practitioner-can-raise-today) we published earlier — and they're things any organization with a litigation hold process can do today.

RG-Aware directly addresses the shield argument Craig identified. The standard can no longer reasonably be read as "if you can't do RG-Core, you're excused." The standard now says: at minimum, collect and be transparent. Versioning complexity is not a reason to ignore linked content.

## A Point Craig Raised That Deserves More Attention

Beyond the versioning argument, Craig flagged a search logic problem that's easy to miss. Traditional email family workflows treat a family as responsive if either the message or the attachment generates a keyword hit. But when linked attachments enter the picture, some workflows only collect the linked document if the *parent email* hits first — effectively inverting the family logic and missing responsive content that lives in the linked file, not in the message.

This matters for RG-Aware. The collection obligation isn't conditioned on the parent message being responsive. If a preserved communication contains a hyperlink to same-tenant content, the linked content is within scope for collection and search on its own terms.

## Courts Are Already Doing This

One of the most striking parts of Craig's post was the *Uber* example. Judge Cisneros ordered two custom metadata fields in production — "Missing Google Drive Attachments" and "Non-Contemporaneous" — requiring the producing party to flag gaps and version discrepancies explicitly, on the record.

That's a court ordering a case-specific form of the same structured transparency RG-Aware formalizes. The difference is that *Uber* required it ad hoc, for a single case. The standard makes it a named, repeatable practice.

*Carvana* pushed further still — ordering a bounded capability test, then expanding it when results warranted it. The direction of travel is becoming clearer: courts are moving from accepting assertions of infeasibility to requiring demonstration of what tools can actually do.

## The Maturity Path

The standard now reads as a staircase, not a cliff:

| Tier / Level | What It Requires |
|---|---|
| **RG-Aware** | Collect linked content. Disclose limitations. Generate exceptions. Document gaps. |
| **RG-Core** | Deterministic as-sent version resolution, stable identifiers, relationship integrity, exception determinism, reproducible exports. |
| **RG-Plus** | RG-Core + effective-dated identity, audit correlation, access vs. permission distinction. |
| **RG-Max** | RG-Plus + accessed-version analysis, expanded artifact coverage, advanced validation. |

Craig's bridge — "do what you can now, document what you can't, and improve your capabilities over time" — is what the maturity path operationalizes. And his definition of proportionality captures the spirit of the entire framework: "Not perfection. Not paralysis. But reasonable, good-faith efforts commensurate with the stakes and the state of the art."

## On "Aspirational"

Craig framed reconstruction-grade fidelity as "aspirational architecture" — the place the industry should be heading. We think that's exactly right. And we think it's worth saying plainly: aspirational is not a limitation. It's how serious standards work.

The EDRM was aspirational when it launched — nobody was running full workflow governance. The Sedona Principles were aspirational before courts began citing them as authoritative. ISO 27001 was aspirational before it became a procurement checkbox. In each case, the trajectory was the same: a framework defined the target, adoption pressure followed, judicial and regulatory citation came next, and eventually what started as aspirational became the expected norm.

The RGR Standard is at the beginning of that arc. *Carvana* suggests that courts may increasingly require parties to demonstrate what reconstruction is technically possible, rather than resting on infeasibility claims. The question is whether the industry starts building toward it now, or waits for the next sanctions motion to force the conversation.

RG-Aware is how you start building today. It doesn't require aspirational capabilities — it requires transparency and collection, which are available now. The conformance levels above it define where the industry needs to go. The distance between those two points is the work ahead — for vendors, for service providers, and for the standard itself.

## The Empirical Question

Craig has been calling for data on linked attachment modification rates since his 2024 posts. In this piece, he repeated the call louder, and was characteristically honest about it: "I don't have solid metrics. I believe what I'm describing here, but belief is not evidence."

He also proposed a specific methodology: "Any organization with a reasonably mature M365 environment could sample and compare the version history of linked attachments against the timestamps of the messages that transmitted them." That's a practical, reproducible approach — and it's one the industry has had the ability to execute for years without doing so.

We think Craig is right that the empirical question matters, and right that it's overdue. Cloudficient is analyzing enterprise M365 datasets to better understand modification rates and version-divergence patterns. When that analysis is ready, we'll share it. But this shouldn't be a one-vendor effort. Craig's proposed methodology is straightforward enough that any organization with M365 production experience and version history access could contribute data points. The more the industry knows about actual modification rates, the less room there is for either side to argue from intuition alone.

Whether the number is five percent or thirty percent, the architectural principle is the same: if linked content can change after communication, the evidentiary record must account for it. At RG-Aware, that means disclosure. At RG-Core, that means resolution.

## Continuing the Conversation

Craig's post sharpened the standard. The shield vulnerability was real, and it needed to be closed. Craig's critique exposed a genuine ambiguity, and the standard was updated to address it — because a standard that can't respond to substantive critique isn't a standard worth having.

The [updated standard](../../front-matter.md) is available now. The [four practitioner questions](../posts/2026-04-02-i-tried-to-break-the-preservation-gap-argument.md#four-questions-any-practitioner-can-raise-today) remain the fastest way to assess where your organization stands. And the conversation is open — this is how standards get built.
