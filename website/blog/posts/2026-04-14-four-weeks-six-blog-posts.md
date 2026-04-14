---
date: 2026-04-14
draft: false
slug: four-weeks-six-blog-posts
description: "How eDiscovery preservation quietly became an ethics question — four weeks, six blog posts, Rule 37(e), Comment 8, and the two gaps RGR was built to close."
authors:
  - peterkozak
categories:
  - Standard Development
tags:
  - Preservation Gap
  - Context Gap
  - FRCP Rule 37(e)
  - ABA Model Rule 1.1
  - Comment 8
  - Collaboration Platforms
  - Microsoft 365
  - Sedona Conference
  - Craig Ball
  - RG-Aware
chat_prompts:
  - "What are the Preservation Gap and the Context Gap?"
  - "How does the Reconstruction-Grade Standard close both gaps?"
  - "Where should I start reading about the RGR project?"
  - "What did Craig Ball say about reconstruction-grade preservation?"
  - "How does ABA Comment 8 connect to hyperlinked document preservation?"
---

# Four Weeks. Six Blog Posts. One Ethics Question I Didn't See Coming.

![A silhouette climbs a staircase while email, document, and link icons ascend the steps](../../images/blog/blog-four-weeks-six-blog-posts.webp)

*How a technical question about preservation architecture quietly became a question about professional ethics — in twenty-eight days and six blog posts.*

<!-- more -->

Somewhere this week, a lawyer will certify to a court that her client has taken "reasonable steps" under Rule 37(e) to preserve evidence. That evidence includes hyperlinked documents from Teams, SharePoint, and OneDrive.

Most of the tools on the market cannot actually preserve those documents.

The lawyer does not know this.

Over the last four weeks, Brandon D'Agostino and I published six posts that all led to the same conclusion: the two failure modes modern collaboration platforms introduce into eDiscovery — the **Preservation Gap** and the **Context Gap** — are no longer just an architecture problem. They are becoming a legal capability question and, increasingly, an ethics question.

Closing both gaps is the entire purpose of the Reconstruction-Grade Standard Brandon and I have been building.

---

## It began with Sedona.

In October 2025, The Sedona Conference published a Commentary on the discovery implications of collaboration platforms — Teams, Slack, SharePoint, the full modern stack. It named the structural cracks honestly. But Commentaries, by design, identify problems; they don't solve them.

I spent a long weekend with that document and wrote back — not a rebuttal, an architectural answer. That became the first post: [*Sedona Identified the Problems. Here's the Architectural Answer.*](../posts/2026-03-13-sedona-identified-the-problems.md)

I thought I was done. I wasn't.

---

## Then a test failed.

Two weeks later I ran the simplest experiment I could think of. A Microsoft 365 email contains a link to a SharePoint document. The document later changes. Can an eDiscovery tool produce the version that was *actually sent*?

Most tools cannot. Not because they are badly built — because the profession has been operating on preservation assumptions that no longer match how evidence actually moves through Microsoft 365. Attachments used to be blobs of bytes. They are now live pointers that drift, under litigation hold, away from the document the sender intended the recipient to see.

[*The Simplest E-Discovery Test Most Tools Would Fail.*](../posts/2026-03-26-the-simplest-ediscovery-test-most-tools-would-fail.md)

---

## Then the rule tightened.

This is where Brandon took the mic. Rule 37(e) requires "reasonable steps" to preserve evidence — but what counts as reasonable in 2026 when the evidence is a hyperlinked SharePoint document that may have changed seven times since the email was sent?

Brandon walked through the emerging case law, including the Carvana securities litigation — where Arizona Magistrate Judge John Z. Boyle ordered a bounded forensic test of the parties' ability to recover hyperlinked documents from Microsoft 365. Not a discussion. *A capability test.* On the record, before production.

Most preservation workflows in use today would not survive it.

[*What FRCP Rule 37(e) Means for Modern Collaboration Platforms.*](../posts/2026-03-31-what-frcp-rule-37e-means-for-modern-collaboration-platforms.md)

---

## Then I tried to break my own argument.

Anyone making a strong claim in public should steelman their own opponents. I spent two days in an adversarial dialogue with custom coded Claude and ChatGPT Pro agents, playing both sides — trying to find the strongest possible objection to the idea that the two gaps are a real legal problem at all.

What came out of that exercise sharpened the framework. The Preservation Gap and the Context Gap share a technical root, but they may need different doctrinal homes — loss-of-ESI doctrine under Rule 37(e) for the first, authenticity and completeness for the second. One limiting principle also emerged: not every hyperlink enlarges the preservation obligation; relevance and proportionality still apply.

And four specific questions came out of it — questions any practitioner can raise at a Rule 26(f) conference to test whether opposing counsel's tools actually preserve what they claim to preserve.

[*I Tried to Break the Preservation Gap Argument. Here's What's Left.*](../posts/2026-04-02-i-tried-to-break-the-preservation-gap-argument.md)

---

## Then Craig Ball answered.

Craig Ball — one of the most respected voices in eDiscovery — wrote a public response. His response was thoughtful, sharp, and in one important place corrective: he warned that a reconstruction-grade standard must not become a *shield* for parties to avoid collecting linked attachments in the first place. Duty to collect comes first; duty to reconstruct comes second. Dog, then tail.

He was right. I went back to the standard and added a new pre-conformance tier called **RG-Aware** — for organizations doing the honest, workmanlike collection work today while building toward reconstruction-grade fidelity tomorrow. A ramp, not a cliff. It sits alongside three other conformance tiers — RG-Core, RG-Plus, and RG-Max — each defined by measurable tests, not aspirational criteria.

[*The Dog, the Tail, and the Staircase.*](../posts/2026-04-07-the-dog-the-tail-and-the-staircase.md)

Four weeks in, and I still thought this was an architecture conversation. It wasn't.

---

## And then, last Wednesday, it became an ethics question.

Brandon published a post I did not see coming. Its premise is disarmingly simple: ABA Model Rule 1.1, Comment 8 — the duty of technological competence — does not require lawyers to build reconstruction-grade preservation systems. It requires something harder.

It requires that you *know* whether your workflow silently loses evidence. And if it does, it requires that you *disclose* that limitation.

Those are two different things from preserving evidence, and they are both now the floor of professional responsibility in matters involving collaboration platforms. "My tools are industry-standard, I didn't know they couldn't handle hyperlinked documents" is no longer an answer. Knowing, and disclosing, is the minimum.

[*The Ethics Question You Should Be Asking About Your Preservation Strategy.*](../posts/2026-04-08-the-ethics-question-you-should-be-asking-about-your-preservation-strategy.md)

That post is the one that made me write this summary. Because reading Brandon's draft, I realized I had been living through a category shift in public, one blog at a time — and the sequence belonged in front of the profession in one place.

---

## Six posts. One problem. Two gaps.

Depending on who you are:

- **Practicing lawyer** — start with the ethics post.
- **General Counsel** — start with the Rule 37(e) post.
- **Law firm litigator or defense team** — start with the steelman post and Craig Ball's response.
- **eDiscovery analyst or litigation-support lead** — start with the Sedona architectural answer and the simplest-test post.

Each post is a different door into the same room. The room contains two gaps — Preservation and Context — and it is larger than most of the profession realizes.

---

If any one of these six posts speaks to a colleague — a litigator, a GC, an outside counsel, an analyst — forward it.

The profession does not need consensus yet on how to close the preservation gap or the context gap. But it needs honesty about which current workflows close neither. That conversation cannot stay in hallways. It has to happen out loud.

---

**Explore the standard:**

- [The Preservation Gap](../../concepts/preservation-gap.md) — when hyperlinked evidence expires outside the litigation hold
- [The Context Gap](../../concepts/context-gap-ediscovery.md) — when collected evidence is preserved in the wrong state
- [The Reconstruction-Grade Standard](../../front-matter.md) — front matter, draft status, and entry point to the full specification
- [Measurable Evaluation Framework](../../06-evaluation-framework.md) — conformance tiers (RG-Aware, RG-Core, RG-Plus, RG-Max) and tests
