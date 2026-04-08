---
date: 2026-04-10
draft: false
description: "ABA Comment 8 doesn't require forensic preservation — but it requires knowing whether your workflow silently loses evidence and disclosing that limitation."
authors:
  - brandondagostino
categories:
  - Industry Analysis
tags:
  - eDiscovery
  - ABA Model Rule 1.1
  - Comment 8
  - Technological Competence
  - Preservation Gap
  - Collaboration Platforms
  - Reconstruction-Grade
  - Microsoft 365
  - Litigation Hold
  - ESI Protocol
  - RG-Aware
chat_prompts:
  - "What does ABA Comment 8 mean for eDiscovery preservation?"
  - "Does Comment 8 require lawyers to build reconstruction-grade systems?"
  - "What questions should lawyers ask about their litigation hold workflow?"
  - "How does the duty of technological competence apply to linked attachments?"
---

# The Ethics Question You Should Be Asking About Your Preservation Strategy

![Closed book with teal light leaking from its pages](../../images/blog/blog-preservation-question-ethics-rules.webp)

**ABA Comment 8 doesn't require you to build a forensic preservation system. It does require you to know whether your workflow silently loses evidence — and to say so.**

<!-- more -->

---

If your litigation hold preserves an email but not the linked document it references — and you do not know it is happening — is that competent representation?

In Microsoft 365 and similar collaboration platforms, [hyperlinks have replaced traditional attachments](../../concepts/modern-attachments.md) as the default way to share documents. When a custodian sends an email with a link to a file in someone else's OneDrive, and the hold only covers the custodian's mailbox, the linked document sits in storage governed by a different retention policy. It can expire, be modified, or be deleted — silently, while the hold system reports full compliance.

That gap raises a question that isn't about technology architecture. It is about professional responsibility.

## Comment 8 in Thirty Seconds

In 2012, the ABA amended [Comment 8 to Model Rule 1.1](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_1_competence/comment_on_rule_1_1/) to add eight words: "...including the benefits and risks associated with relevant technology." The ABA and forty states have since amended their ethical rules to include a duty of technological competence. This is not aspirational guidance. It is the baseline professional obligation for practicing lawyers in most of the country.

The amendment doesn't require lawyers to become technologists. The duty is generally understood to require enough understanding of relevant tools and workflows to recognize material risks and limitations — not expert-level mastery. The ABA's ethics writing on newer technologies [reinforces this framing](https://www.redgravellp.com/publication/litigation-technology-and-ethics-the-importance-of-technological-competence-2025): lawyers need a reasonable understanding of the capabilities and limitations of the technology they use.

## What Competence Actually Requires

The clearest articulation of what Comment 8 means for eDiscovery practice comes from California Formal Opinion 2015-193, which holds that a lawyer's obligations include the duty to have "a reasonable understanding of the technologies and methodologies used to preserve, collect, and produce electronic documents."

The opinion identifies three pathways to meet the duty: acquire the knowledge yourself, associate with someone who has the competence, or decline the representation. But it is explicit that associating with someone competent does not mean handing off responsibility. The lawyer "maintains overall responsibility for the matter" — which means understanding enough to ask the right questions and evaluate the answers. ABA Formal Opinion 477R reinforces this: lawyers may rely on qualified professionals but cannot abdicate the obligation to understand what they are supervising.

The consistent principle across these authorities is that competence means understanding capabilities and limitations — not just what the technology does, but what it doesn't do, and where that gap creates risk.

## What Many Preservation Workflows Actually Do

Apply that principle to a modern preservation workflow. In many environments, preservation remains custodian-container scoped: place a hold on the custodian's mailbox, and the emails are preserved. That worked when emails carried their own attachments as embedded files.

It doesn't work the same way when the "attachment" is a hyperlink to a document in a shared repository. The hold preserves the email. It does not necessarily preserve the linked document, particularly when that document resides in storage belonging to a non-custodian. And it almost certainly does not preserve the version of the document that existed when the email was sent, because the document continues to be edited after transmission.

Many lawyers who are supervising preservation do not know this. Not because they are negligent, but because the gap is invisible. The hold system does not flag it, and the vendor does not report it. The linked document expires or changes, and no one generates an alert. The production goes out with the email intact and the link pointing to nothing — or to a version that post-dates the communication by months.

Comment 8 does not require that you build a system that prevents this. It requires the attorney to understand enough about the client's preservation technology to know the risk existed and whether you disclosed the limitation when it mattered.

## Four Questions for a Rule 26(f) Conference

Earlier this year, we published an [adversarial stress test](../posts/2026-04-02-i-tried-to-break-the-preservation-gap-argument.md) of this [preservation gap](../../concepts/preservation-gap.md) argument — pitting two AI systems against each other to pressure-test whether the concern survives proportionality scrutiny. The result was four questions that any practitioner can raise in a Rule 26(f) conference or ESI protocol negotiation:

1. Does your hold process identify linked content outside the custodian container?
2. Can you determine whether the collected version matches the version that existed at the time of the communication?
3. If not, what limitation disclosures have you made?
4. What targeted steps have you taken in matters where that difference could be material?

These are due diligence questions, not forensic engineering questions. They ask whether you understand how your preservation workflow handles a specific, increasingly common evidence pattern and whether you have been transparent about what it cannot do. Under Comment 8, a lawyer supervising preservation should be able to answer these or know to ask them of the professional who can. California's Formal Opinion 2015-193 is direct on this point: "An attorney's lack of technological knowledge or experience does not excuse the attorney from the duty of competence."

## Where RG-Aware Fits

The Reconstruction-Grade eDiscovery Standard recently [introduced RG-Aware](../posts/2026-04-07-the-dog-the-tail-and-the-staircase.md) — a pre-conformance adoption tier that formalizes the minimum transparent posture for organizations dealing with modern collaborative evidence. RG-Aware requires four things: collect linked content from same-tenant storage, disclose limitations through ESI protocols or equivalent mechanisms, generate structured exceptions when content cannot be collected, and document known gaps at the matter level.

RG-Aware is a transparency and awareness standard, not a technical capability standard. That maps directly to what Comment 8 asks of lawyers: that you understand enough about the technology to recognize when evidence is at risk and disclose that risk appropriately, not that you achieve reconstruction-grade fidelity.

The distance between "I didn't know the workflow had this limitation" and "I understood the limitation and disclosed it" is the distance Comment 8 exists to close. RG-Aware gives that obligation a practical shape.

## The Direction Courts Are Moving

In the *Uber* litigation, Judge Cisneros ordered custom metadata fields — "Missing Google Drive Attachments" and "Non-Contemporaneous" — requiring the producing party to flag gaps and version discrepancies explicitly. In [*Carvana*](../posts/2026-03-31-what-frcp-rule-37e-means-for-modern-collaboration-platforms.md), the court ordered capability testing rather than accepting blanket infeasibility claims. Courts are beginning to ask the same questions Comment 8 says lawyers should already be asking: what can your tools do, what they cannot do, and have you disclosed the difference?

The direction is toward transparency and demonstrated capability — not toward perfect preservation, but toward knowing and disclosing what you cannot preserve.

## What This Doesn't Mean

Comment 8 does not require lawyers to build reconstruction-grade preservation systems. It does not require RG-Core conformance. It does not create a per se ethics violation every time a linked document expires outside a hold scope.

What it does require is a reasonable understanding of how the technology works — including where it falls short. In the California opinion's framing: understand it, consult someone who does, or don't take on the work. And when you know about a limitation that could affect the evidentiary record, the obligation to disclose is already well established under existing discovery rules.

The preservation gap starts as a technology problem. The moment counsel does not know it exists, it becomes a competence problem.
