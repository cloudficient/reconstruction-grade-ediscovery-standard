---
date: 2026-04-16
draft: true
description: "The RGR conformance question is entering client conversations. A short playbook for advisory teams who want to answer it without overpromising."
authors:
  - peterkozak
categories:
  - Practice Guides
tags:
  - RGR Conformance
  - Advisory Teams
  - ESI Protocol
  - RG-Aware
  - RG-Core
  - Client Engagement
  - Technological Competence
  - Legal Practice
chat_prompts:
  - "How should an advisor answer when a client asks about RGR conformance?"
  - "What's the difference between RG-Aware and RG-Core for a client-facing conversation?"
  - "Do law firms and service providers need to claim RGR conformance?"
  - "What language should advisors use to describe their workflow's RGR posture?"
---

# When Your Client Asks About RGR Conformance

![Dark conference room with a leather portfolio open on the table, teal light and networked data patterns flowing from its pages](../../images/blog/blog-two-second-silence.webp)

**A short playbook for advisory teams who want to answer the conformance question without overpromising, without dismissing it, and without breaking the two seconds of silence that follow.**

<!-- more -->

---

A general counsel leans forward in a conference room. She looks at the partner across the table and says, "Our eDiscovery vendor mentioned something called RGR conformance — should I be asking our outside counsel about it?"

The partner feels the silence stretch. It is not a long silence. Perhaps two seconds. But in those two seconds, a calculation every advisor makes sooner or later: *do I know enough about this to answer confidently, or do I hedge?*

This post is for the advisor in that two-second pause.

It is written for law firm counsel who advise trial teams, for project managers at service providers who sit between counsel and the platform, and for independent consultants who get pulled in when things get hard. The conformance question lands on all of you differently, but it lands on all of you. The goal of this piece is not to teach you [the standard](../../concepts/reconstruction-grade-ediscovery.md) — the standard is on the website, linked throughout. The goal is to give you a way to *think* about conformance questions inside a client engagement, so that the two seconds stop being a calculation and start being a rehearsal.

## Why This Question Is Arriving Now

A year ago, almost no one outside a small circle of eDiscovery specialists was asking about conformance to a reconstruction-grade standard. That is changing, and it is changing for reasons that have nothing to do with marketing.

In October 2025, [the Sedona Conference Commentary on Information Governance](../posts/2026-03-13-sedona-identified-the-problems.md) named — in authoritative, working-group-reviewed language — the same cluster of problems the RGR standard was written to address: modern attachments, hyperlinked content, version drift, identity drift, the failure of custodian-scoped preservation against collaborative evidence. When a Sedona working group publishes on a problem, the vocabulary enters the mainstream within months. It is entering now.

On the case law side, [Carvana](../posts/2026-03-31-what-frcp-rule-37e-means-for-modern-collaboration-platforms.md) and *Uber* are already doing the work. Courts are ordering capability testing rather than accepting blanket claims that certain content cannot be preserved. Judges are ordering custom metadata fields to flag gaps and version discrepancies. [FRCP Rule 37(e) analysis](../posts/2026-03-31-what-frcp-rule-37e-means-for-modern-collaboration-platforms.md) is moving from theoretical to operational. The questions courts are beginning to ask look very similar to the questions [RGR was designed to answer](../../concepts/evidence-reconstruction.md).

And on the ethics side, [ABA Model Rule 1.1 Comment 8](../posts/2026-04-08-the-ethics-question-you-should-be-asking-about-your-preservation-strategy.md) — the duty of technological competence, now adopted in forty states — has started to be read through the specific lens of collaborative evidence. The distance between "I didn't know the workflow had that limitation" and "I understood the limitation and disclosed it" is the distance that rule exists to close. Corporate general counsel know this. Some of them are starting to ask.

None of that is RGR-driven. RGR is simply a place the vocabulary converges. The question is coming whether we publish another blog post or not.

## Three Shapes the Question Takes

In practice, the conformance question almost never arrives as "Are you RGR-conformant?" It arrives in disguise, and the disguise depends on who is sitting across the table.

**Shape one: the boardroom question.** A partner is in a privileged conversation with a general counsel. The GC has been hearing murmurs — from a peer, from a conference, from a vendor — about reconstruction-grade standards. She asks whether her outside counsel has a position. She is not looking for a technical briefing. She is looking for confidence that her firm has thought about the question before she did. The underlying ask is: *tell me you're ahead of this.*

**Shape two: the kickoff call question.** A service provider project manager is running a kickoff for a new matter. Inside counsel on the client side asks, almost in passing, whether the provider's collection workflow is "RGR-aware or RGR-conformant." The PM has to decide, in real time, whether to claim something, defer the answer, or pivot. The underlying ask is: *is your workflow going to create a problem I have to defend in motion practice?*

**Shape three: the protocol review question.** An independent consultant is reviewing an ESI protocol on behalf of a client. She notices that the other side's protocol references "reconstruction-grade conformance" as a baseline expectation. She has to advise whether to accept, negotiate, or push back. The underlying ask is: *does this language mean what I think it means, and is my client on the hook for it?*

Three different rooms. Three different phrasings. One underlying question: *has your workflow been built with this class of problem in mind, and can you say so honestly?*

## The Playbook: Answer Without Overpromising

What follows is not a script. Scripts fail the moment the conversation turns. This is a sequence of moves that works across all three shapes of the question — boardroom, kickoff, protocol — because it is built around the advisor's real posture, not around the standard's technical vocabulary.

### Move one: Separate awareness from capability

The single most important thing to understand about RGR, for a client-facing conversation, is that the standard distinguishes between *awareness* and *capability*. These are two different postures, and they demand different answers.

- **[RG-Aware](../posts/2026-04-07-the-dog-the-tail-and-the-staircase.md)** is a transparency and disclosure posture. It says: *we know how our workflow handles modern collaborative evidence, we know where its limits are, and we disclose those limits through our ESI protocols or equivalent mechanisms.* It is not a capability claim. It is a knowledge claim. Most competent advisory teams can reach RG-Aware with deliberate work — cataloguing how their workflow actually handles collaborative evidence, documenting the limits, and building disclosure language into their matter practice. That work is primarily an internal exercise, not a tooling upgrade, and many teams can begin it immediately. What the standard asks is that you have actually done it — not that you intend to, and not that you have heard of the problem.

- **RG-Core (and the higher tiers — RG-Plus and RG-Max)** are capability postures. They make specific, testable claims about what the workflow can reconstruct and how faithfully. These tiers are evaluated against the [conformance declaration template](../../toolkit/conformance-declaration-template.md) and backed by structured test results.

For most client-facing conversations happening in 2026, the honest answer is somewhere inside RG-Aware territory — *we understand the problem, we disclose the limits, we do not overclaim.* That is almost always enough, and — for teams that have done the cataloguing work — it is almost always true.

### Move two: Acknowledge the question directly, then reframe it

When the question lands, do not reach for jargon. Reach for acknowledgment.

Language that works:

> "That's a fair question, and it's one we're seeing more often. The short answer is that 'conformance' to a standard like RGR breaks into two postures — awareness and capability. Awareness means we know how our workflow handles modern collaborative evidence and we disclose what it can't do. Capability means we've built toward a specific testable standard. Most organizations right now are focused on awareness first, because awareness and disclosure are the posture most organizations can support honestly today in protocol negotiations and in court-facing conversations, including the kind of matters at issue in *Carvana* and *Uber*. Want me to walk you through how we're thinking about it on this matter?"

That answer does three things at once. It acknowledges the question without flinching. It reframes "conformance" from a binary into a two-tier model the client can reason about. And it pivots to the advisor's own engagement, which is the terrain where the advisor is strongest.

### Move three: Match your claim to your posture — exactly

Do not claim RG-Core if you are working inside RG-Aware. Do not claim RG-Aware if you have not actually catalogued your workflow's limits. The standard is public, the conformance declaration template is public, and opposing counsel can — and increasingly will — read both. An overclaim today is a cross-examination in twelve months.

A safe and honest posture for most advisory teams today sounds something like:

> "On this matter, our workflow is RG-Aware in the sense the standard describes: we have documented how we handle linked content, how we identify version drift, and where our collection scope has known limits. We are not claiming RG-Core conformance today. If the matter requires a specific capability-level claim, we'll raise it and scope it explicitly."

That sentence is defensible. It commits to the knowledge claim the standard actually asks advisors to make. It refuses the capability claim unless earned. It signals technological competence without overpromising.

To make it concrete: imagine the client asks whether linked SharePoint documents are preserved at send-time version. The bad answer is reflexive and lossy — *"yes, we handle that"* — because it papers over a limit that the other side may later prove. The good answer is specific and survivable:

> *"Our current workflow is RG-Aware, not RG-Core. We preserve the message and the linked content within a defined scope, but version-at-time-of-communication is disclosed as a known limit unless we scope and test for it separately on a given matter."*

The second answer takes nine seconds longer to deliver. It is also the difference between a statement that holds up and a statement that does not.

### Move four: Make the disclosure move

The final move is the one most advisors skip, because it feels counterintuitive. **Disclose the limit.** If your workflow cannot collect linked content from non-custodian storage, say so. If your preservation system does not capture the version-at-time-of-communication, say so. Document it in the [ESI protocol addendum](../../toolkit/esi-protocol-addendum.md) — which is written to be used from either side of a matter, producing or receiving — or in whatever mechanism the matter uses.

Disclosure is the move that turns a vulnerability into a record of competence. Every ethics authority on the duty of technological competence — the California opinion, the ABA's Formal Opinion 477R, the emerging 37(e) case law — converges on the same principle: *disclosure materially improves defensibility, preserves credibility, and narrows the ground on which a later challenge can stand.* It is not absolution. It is the difference between a defendable record and an exposed one. The advisors who will be in the strongest position twelve months from now are the ones who put the limitation on the record today.

## What To Do This Quarter

The piece you are reading is not theoretical. It is describing a market that is moving, and the advisors who rehearse will answer better than the advisors who do not. Four concrete moves for this quarter:

1. **Map your workflow's limits.** Sit down with whoever runs your preservation and collection workflow, and catalogue what the workflow can and cannot do with linked content, version drift, non-custodian storage, and short-retention channels. Write it down.
2. **Prepare one approved explanation.** Draft a single paragraph — the sample language earlier in this post is a starting point — that describes your workflow's posture honestly and defensibly. Get it reviewed. Use it.
3. **Add protocol language.** Incorporate the disclosure into your ESI protocol templates or kickoff documentation, so the posture travels with every matter rather than being reinvented in every conference.
4. **Stop hand-waving.** Retire vague claims like *"we handle modern attachments"* or *"our tooling covers collaborative evidence"* from marketing materials, capability decks, and client conversations. Every vague claim is a cross-examination exposure. Replace it with the approved explanation.

Over the next twelve months, the environment is going to keep moving: [Sedona working groups](../posts/2026-03-13-sedona-identified-the-problems.md) will publish more, [37(e) case law](../posts/2026-03-31-what-frcp-rule-37e-means-for-modern-collaboration-platforms.md) will harden further, and *"RGR conformance"* language will start to appear in opposing counsel's protocols and in corporate RFPs. The advisors who did the quarterly work above will find those moments ordinary. The advisors who did not will find them uncomfortable.

## The Two Seconds Don't Go Away

The general counsel will keep asking the question. The partner will keep feeling the silence. The service provider PM will keep hitting mute. The consultant will keep making notes on the protocol.

What changes, with practice, is what happens inside the two seconds. For the advisor who has rehearsed — who has thought about the difference between awareness and capability, who has catalogued their workflow's limits, who has decided in advance what they will and will not claim — the silence becomes shorter, and what comes after it becomes more confident.

The goal of this post is not to sell conformance. It is to give advisory teams the vocabulary to have the conversation honestly. Most of the work is awareness, most of the awareness is already possible, and most of the risk comes from either overclaiming or pretending the question isn't being asked.

The question is being asked. It will be asked more. The two seconds will keep arriving.

Rehearse the moves. Then the silence is yours.

---

*For advisory teams ready to work through their own posture: the [RG-Aware](../posts/2026-04-07-the-dog-the-tail-and-the-staircase.md) discussion, the [ESI Protocol Addendum toolkit](../../toolkit/esi-protocol-addendum.md), and the [conformance declaration template](../../toolkit/conformance-declaration-template.md) are all public on rgrstandard.org. This post is a starting point for an internal conversation — not a substitute for one.*
