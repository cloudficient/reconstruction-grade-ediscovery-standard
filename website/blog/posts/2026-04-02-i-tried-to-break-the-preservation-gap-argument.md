---
date: 2026-04-02
draft: false
description: "We used Claude and ChatGPT Pro in an adversarial AI dialogue to stress-test the Preservation Gap under Rule 37(e). Two failure modes, a limiting principle, and four questions any eDiscovery practitioner can raise in their next ESI protocol."
authors:
  - peterkozak
categories:
  - Industry Analysis
tags:
  - eDiscovery
  - FRCP Rule 37(e)
  - Preservation Gap
  - Context Gap
  - Collaboration Platforms
  - Reconstruction-Grade
  - Microsoft 365
  - Litigation Hold
  - ESI Protocol
  - AI in Legal
chat_prompts:
  - "What objections would a 37(e) scholar raise against the Preservation Gap argument?"
  - "Is the Preservation Gap an edge case or a default behavior in M365?"
  - "How should parties disclose preservation workflow limitations at a Rule 26(f) conference?"
  - "What questions should opposing counsel ask about hyperlinked document preservation?"
---

# I Tried to Break the Preservation Gap Argument. Here's What's Left.

Before I brought this argument to the profession, I tried to break it.

Our team has spent the last several months documenting a structural problem in how modern eDiscovery workflows handle collaborative evidence — [hyperlinked documents](../../concepts/modern-attachments.md) that live outside the custodian container, versions that shift after communication, evidence relationships that cross boundaries litigation holds weren't designed to traverse.

Brandon D'Agostino, our VP and an attorney, wrote the [legal analysis mapping FRCP Rule 37(e) to collaboration platform evidence](../posts/2026-03-31-what-frcp-rule-37e-means-for-modern-collaboration-platforms.md). That piece grounds the argument in case law — from *Epic Games v. Google* through [Carvana's capability testing orders](../../judicial-signals.md). We published [the Sedona commentary analysis](../posts/2026-03-13-sedona-identified-the-problems.md) showing where the industry's own authority acknowledges the gap. And we built [a practical test](../posts/2026-03-26-the-simplest-ediscovery-test-most-tools-would-fail.md) anyone can run in five minutes.

But the legal framing had been written by our team, about our thesis. That's not adversarial. I needed to hear the objections a skeptical scholar would raise — the proportionality challenges, the doctrinal fit questions, the "you're just a vendor ratcheting up the burden" pushback — before taking this to the academic community.

So I did something unusual: I had two AI systems argue it out. Claude, with full access to the RGR standard, the case law analysis, and the Sedona mapping, argued the RGR position. ChatGPT Pro, prompted to adopt the perspective of a skeptical Rule 37(e) scholar, tried to dismantle it. I used the objections that survived that adversarial exchange to tighten the argument before publishing.

Several challenges forced significant revisions. Here's a condensed version of that dialogue.

<!-- more -->

---

## The Dialogue

**Scholar:** You're identifying a real technical issue. But Rule 37(e) doesn't ask whether a party used the best available method. It asks whether they took *reasonable steps*. When does the availability of a better preservation approach make failure to use it unreasonable?

**RGR:** If I were arguing that the existence of an API creates a legal obligation to build a new preservation architecture around it, I'd deserve to lose that argument. The existence of a better method doesn't make the standard method unreasonable.

Here's the fact pattern where I think it crosses from optional to unreasonable: a matter where the substantive dispute turns on what was communicated and when. Custodians on a collaboration platform where the primary sharing mechanism is [hyperlinks, not embedded attachments](../../concepts/modern-attachments.md). The party knows this — it's their platform, their workflows. The Sedona Conference has published [guidance identifying exactly this evidence behavior](../posts/2026-03-13-sedona-identified-the-problems.md) as a distinct preservation challenge. And the party's hold system, by design, does not traverse links or preserve linked content outside the custodian container.

If that linked content expires and opposing counsel can demonstrate the lost documents were relevant to the disputed communications, the [37(e) analysis](../posts/2026-03-31-what-frcp-rule-37e-means-for-modern-collaboration-platforms.md) gets very uncomfortable. Not because the party didn't try — but because they knew the tool couldn't reach the evidence that mattered, and they had a feasible alternative.

**Scholar:** But are you saying the existence of the hyperlink itself should enlarge the preservation obligation? Because if that's the move, that has very significant implications for scope, burden, and proportionality.

**RGR:** No. I'm not arguing that the hyperlink enlarges the hold. I'm arguing that the hyperlink *identifies* a specific piece of evidence that the communication depends on — and that the architecturally correct response is to collect that specific object, not to expand the hold to the person who owns the storage.

The traditional response is to expand the custodian scope — put the content owner on hold. That cascades immediately. Holding User B to preserve one linked document means holding all of B's content. B's messages link to content in C, D, and E's storage. Within two hops, a significant fraction of the organization is on litigation hold. That's not preservation. That's paralysis.

The alternative is to collect the specific linked document — at the version contemporaneous to the message — without touching the content owner's hold status. The unit of preservation becomes the evidence relationship, not the custodian container. It's targeted, bounded, and the technology exists today. The linked content is in the same tenant, under the same administrative control. The APIs are there. The gap is in the workflow, not in the platform's capability.

**Scholar:** I hear what you're describing, but I think many judges would hear this as a vendor or technologist trying to ratchet up the preservation burden by reference to technical possibility rather than legal reasonableness. What you're really proposing is not a new preservation rule — it's an enhanced collection strategy for certain matters.

**RGR:** I'm actually comfortable with that framing. I think "enhanced collection strategy for certain matters" is probably where this lives for most litigation today. The question is when it crosses from optional best practice to something a party needs to be able to explain not doing.

**Scholar:** Fair enough. But you seem to be describing two different problems. Linked content that expires entirely, and linked content that exists but has been materially revised since the communication. Those aren't the same thing doctrinally.

**RGR:** You're right, and separating them is important.

The first is cross-boundary loss — what we call the [Preservation Gap](../../concepts/preservation-gap.md). A custodian's email links to a document in a non-custodian's OneDrive. The custodian is on hold; the content owner isn't. The document hits retention and is purged. The email is preserved, the link is preserved, the evidence the link pointed to is gone. That maps more naturally to 37(e) — ESI that should have been preserved wasn't.

The second is fidelity failure — the [Context Gap](../../concepts/context-gap-ediscovery.md). The document exists, but it's been edited since the message was sent. Collection captured today's version, not Tuesday's. If someone sent a message saying "I've reviewed the analysis and approve the recommendation," and the linked document has been revised seventeen times since — the collected version isn't the document that was approved. The bytes are there. The evidence isn't.

Whether that second pattern constitutes "loss" under 37(e), or whether it's better addressed through authenticity, completeness, or evidentiary weight — I genuinely don't know. That's a question for legal scholarship, not engineering.

**Scholar:** Then let me push that point. Are you prepared to argue that, in some matters, a later-collected version of the linked document is functionally no different from loss — because it fails to preserve the state that made the communication meaningful?

**RGR:** Sometimes yes, and the conditions under which it's yes are identifiable. If someone sends a message saying "I've reviewed the attached analysis and I approve the recommendation" — and the linked document has been edited seventeen times since — the version at collection time is not the document that was approved. It's a different document. The approval, the reliance, the decision — those all attached to a state that no longer exists in the preserved record.

But is that every version mismatch? No. If someone links to a corporate policy document that had a typo corrected two days later, the later version is probably a perfectly adequate substitute. The limiting condition is whether the version change is material to the question the evidence is being used to answer. Courts make materiality judgments all the time. The unfamiliar part is that most parties don't even know the version discrepancy exists, because their collection workflow doesn't compare the collected version against the version that existed at communication time. The discrepancy is invisible unless you look for it.

**Scholar:** How often do these two problems actually arise in matters of real consequence — as opposed to existing mostly as a technically possible but relatively uncommon edge case?

**RGR:** It's not an edge case. In enterprise M365 environments, it's often the default behavior.

Every modern collaboration platform — Microsoft 365, Google Workspace, Slack — has shifted from embedded attachments to [hyperlinks as the primary sharing mechanism](../../concepts/modern-attachments.md). When someone shares a document in Teams or Outlook, the platform generates a link to a live SharePoint or OneDrive object. The user often doesn't even choose this — it's the default. Microsoft has been actively steering users toward sharing links rather than attaching copies for years.

So in any matter involving M365 custodians, the question isn't whether hyperlinked evidence exists. It's what percentage of document sharing happened that way. In many enterprise environments we work in, it's the majority.

And here's what makes it structural rather than incidental: the documents most likely to be shared as hyperlinks are the ones people are actively working on. That's why they're sharing them. Stable, final documents are more likely to be attached as PDFs. The living, evolving, collaboratively-edited documents — the ones most likely to have material version changes — are exactly the ones shared as links.

The problem is particularly acute in regulatory investigations, securities matters, employment disputes involving collaborative performance documents, board decision-making, merger diligence, and life sciences contexts where shared analyses evolve over time and the sequence of revisions matters. In those settings, the difference between the contemporaneous version and the later-collected version isn't merely interesting — it's central.

**Scholar:** So what's the narrowest incremental response a court could adopt now — without requiring anyone to embrace the full architecture you have in mind?

**RGR:** Transparency. Not a new preservation mandate. A structured obligation to disclose known limitations in the preservation workflow as it relates to collaborative, hyperlinked evidence.

In a Rule 26(f) conference or ESI protocol, parties would address: does your preservation workflow identify and preserve linked content outside the custodian container? Does your collection process capture the version contemporaneous to the communication, or the version extant at collection time?

If the answer is no — and for most organizations today, it will be — that's not sanctionable. It's disclosed. The parties and the court have a shared understanding of what the preserved record reflects and what it doesn't. And from there, they can make informed decisions about proportionality — whether targeted preservation of specific linked content is warranted given the nature of the dispute, the importance of the evidence, and the burden.

That uses the existing procedural framework — the meet-and-confer, the ESI protocol, the Rule 26(g) certification — and adds one question: does your workflow have this known limitation, and if so, what are you doing about it in this matter?

---

## What's Left

The objections were hard. Not everything I started with survived.

**Two distinct failure modes.** Evidence that expires outside hold scope — the [Preservation Gap](../../concepts/preservation-gap.md) — and evidence preserved in the wrong state — the [Context Gap](../../concepts/context-gap-ediscovery.md). They share a technical root but may need different doctrinal homes.

**A limiting principle.** Not every hyperlink enlarges the preservation obligation. The same relevance and proportionality judgments apply. The difference is having a mechanism that acts at the evidence level rather than the custodian level.

**A comfortable framing for skeptics.** This is an enhanced collection strategy for certain matters — not a new preservation rule. The question is when a party needs to be able to explain not using it.

**It's not an edge case.** In enterprise M365 environments, [hyperlinks are often the default sharing mechanism](../../concepts/modern-attachments.md). The documents shared as links are the ones most likely to have material version changes. The categories of matters where this can be outcome-determinative — regulatory, securities, employment, board decisions, M&A, life sciences — are not niche.

**An incremental path.** Transparency about workflow limitations — through existing procedural tools — before anyone needs to adopt a new preservation theory.

## Four Questions Any Practitioner Can Raise Today

1. Does your hold process identify linked content outside the custodian container?
2. Can you determine whether the collected version matches the version that existed at the time of the communication?
3. If not, what limitation disclosures have you made?
4. What targeted steps have you taken in matters where that difference could be material?

Those questions don't require a rule change. They don't require new technology. They require knowing to ask.

Disclosure surfaces the gap. Closing it requires evidence-level preservation — collecting the specific linked object at the version contemporaneous to the communication, without cascading custodian holds. That's what the [Reconstruction-Grade eDiscovery Standard](../../front-matter.md) was built to define.

---

*For the full framework behind these failure modes, see [The Preservation Gap](../../concepts/preservation-gap.md) and [The Context Gap](../../concepts/context-gap-ediscovery.md). For the case law analysis, see Brandon D'Agostino's [What FRCP Rule 37(e) Means for Modern Collaboration Platforms](../posts/2026-03-31-what-frcp-rule-37e-means-for-modern-collaboration-platforms.md). For the developing judicial landscape, see [Judicial Signals and Case Developments](../../judicial-signals.md). For the five-minute test that makes the gap visible, see [The Simplest eDiscovery Test Most Tools Would Fail](../posts/2026-03-26-the-simplest-ediscovery-test-most-tools-would-fail.md).*
