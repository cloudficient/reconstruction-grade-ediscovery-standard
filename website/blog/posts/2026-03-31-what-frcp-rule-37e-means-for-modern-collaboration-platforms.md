---
date: 2026-03-31
draft: false
description: "How FRCP Rule 37(e) reasonable steps is evolving for collaboration platform evidence — case law from Epic v. Google to Carvana's capability testing."
authors:
  - brandondagostino
author_name: Brandon D'Agostino
categories:
  - Industry Analysis
tags:
  - eDiscovery
  - FRCP Rule 37(e)
  - Collaboration Platforms
  - Reconstruction-Grade
  - Preservation
  - Microsoft 365
chat_prompts:
  - "Could my preservation workflow fail a 37(e) challenge?"
  - "What did the Carvana court order for hyperlinked documents?"
  - "How does the Preservation Gap create 37(e) exposure?"
  - "What are reasonable steps for Teams and SharePoint evidence?"
---

# What FRCP Rule 37(e) Means for Modern Collaboration Platforms

![Balance scale — solid files vs networked cloud evidence](../../images/blog/blog-frcp-rule-37e-collaboration-platforms.webp)

**Rule 37(e) requires "reasonable steps" to preserve ESI. When evidence lives in Teams, Slack, and SharePoint, preservation steps designed for email may be structurally incomplete — even when they execute correctly.**

<!-- more -->

The same preservation steps that were reasonable for email-era evidence can be structurally incomplete for collaborative evidence. They execute correctly. They preserve real data. And they may silently miss the evidence that matters.

That is the emerging tension at the intersection of Federal Rule of Civil Procedure 37(e) and modern collaboration platforms. Rule 37(e) governs what happens when ESI is lost because a party failed to preserve it. It applies when the ESI should have been preserved in anticipation of litigation, the party failed to take reasonable steps, the information was lost, and it cannot be restored or replaced. Sanctions range from curative measures for prejudice under (e)(1) to adverse inference instructions, dismissal, or default judgment under (e)(2) where the court finds intent to deprive.

The threshold question is always whether the party took **reasonable steps**. The Advisory Committee Notes are explicit that perfection is impossible. Courts consider party resources, proportionality, the nature of the business, and the implementation of litigation holds.

In my view, that standard was designed for a world where evidence was primarily email and files. The question now is what it means when the evidence lives on collaboration platforms.

## What "Reasonable Steps" Meant for Email

For most of the past two decades, the preservation playbook was well understood. When litigation was reasonably anticipated, you issued a litigation hold. Custodian mailboxes were placed on hold. Relevant file shares were identified and preserved. The evidence — emails with embedded attachments, documents stored in known locations — was largely self-contained. A message carried its attachment. A file existed in one version at one location. Identity was a static directory entry.

Litigation holds and custodian-based preservation were reasonable steps for that evidence model. The evidence was bounded. The relationships were embedded. The system of record was the mailbox or file server.

That model worked because the evidence matched the assumptions.

## What Changed

Microsoft 365, Google Workspace, Slack, and every major collaboration platform introduced a fundamentally different evidence model. The changes are structural, not incremental:

**Hyperlinks replaced attachments.** When someone shares a document in an email or Teams message, the message carries a link to a live SharePoint or OneDrive object — not a frozen copy. The document continues to change after the message is sent. The version that existed at send time is typically not preserved by the message itself, and a standard collection workflow will often retrieve whatever version exists at the time of collection.

**Documents are versioned and shared.** A single document may accumulate dozens of versions across multiple authors. Which version matters depends on when the communication occurred — a question that requires correlating message timestamps with version history. Traditional preservation typically captures the current version, not the version the recipient saw.

**Identity is dynamic.** People change roles, departments, managers, and access rights over time. A current directory snapshot does not reflect who had access to what six months ago. When a litigation question turns on who could see a document at a specific point in time, the current state of the directory is not the answer.

**Relationships span systems.** A Teams message may reference a SharePoint document that was originally shared via OneDrive, authored by someone who has since left the organization, and edited by three people in a channel that no longer exists. The evidentiary relationships cross application boundaries in ways that custodian-based holds do not capture.

## The Case Law Is Catching Up

Courts have not yet established a uniform rule for collaborative evidence preservation. But the case law increasingly reflects that preservation failures on these platforms carry real consequences — and that courts are beginning to test what tools can actually do. (For detailed case-by-case analysis, see [Judicial Signals and Case Developments](../../judicial-signals.md).)

### Collaboration Platform Spoliation

In *Epic Games v. Google*, the court found in a March 2023 ruling that Google failed to take reasonable steps to preserve relevant chat evidence, that the deleted chats could not be restored or replaced, and that Google acted with intent to deprive. Google employees had routinely toggled "history off" on Google Chat, triggering automatic deletion of messages relevant to the litigation. In an October 2023 pretrial order, the court adopted a permissive adverse-inference instruction as the Rule 37(e)(2) remedy. When a platform allows evidence to disappear by default and the party fails to intervene, 37(e) applies.

Even without intent, the lower tier has teeth. In *Maziar v. City of Atlanta* (2024), the court found spoliation and prejudice sufficient for Rule 37(e)(1) curative measures — denying summary judgment and awarding fees — without finding the intent required for (e)(2). And the Ninth Circuit's decision in *Gregory v. State of Montana* (2024) strongly reinforced that sanctions for lost ESI must be analyzed through Rule 37(e), reversing a district court order that had relied on inherent authority instead of applying the rule.

### Hyperlinked Documents: From Definition Disputes to Capability Testing

As early as 2021, courts began resisting the idea that hyperlinks are automatically attachments — *Nichols v. Noom* declined to extend the traditional attachment analogy to linked content, pushing the analysis toward actual collection method and feasibility. (See [Judicial Signals](../../judicial-signals.md) for the full case analysis.) Since then, the pattern has developed through *In re StubHub*, where a court modified a stipulated ESI protocol after concluding that broad compliance with hyperlinked-file production was impossible; through *In re Insulin Pricing Litigation* (D.N.J., May 2024), where the court accepted that producing as-sent versions of hyperlinked documents was not feasible or practicable; and through *In re Uber Technologies* (N.D. Cal., 2024–2025), where a court-approved protocol treated modern attachments as within the attachments definition for purposes of that litigation while providing that contemporaneous production was not required where no existing technology made it feasible.

### Carvana: When Courts Start Testing Tools

The most significant recent development may be *In re Carvana Co. Securities Litigation*, No. CV-22-02126-PHX-MTL (D. Ariz., 2025–2026). Rather than accepting blanket infeasibility claims or requiring full production, the court ordered something new: a bounded forensic capability test — and then expanded it.

In August 2025, the court ordered a limited pilot: plaintiffs could select up to two custodians, and defendants were directed to run Forensic Email Collector (FEC) — a specific named tool — to test whether historical hyperlinked documents could be retrieved proportionally, producing versions "as closely contemporaneous to, but preceding" the email as feasible (Doc. 196, Aug. 21, 2025).

Following a compliance dispute, the court's January 2026 order expanded the exercise: plaintiffs may select 250 responsive emails from any of the 25 ESI custodians, defendants must run FEC and produce the most contemporaneous non-privileged hyperlinked documents within 10 days, and defendants must also produce responsive non-privileged Google Vault documents (Doc. 255, Jan. 12, 2026).

This is a different kind of order. The court did not resolve the definitional question of whether hyperlinks are attachments. It imposed a practical test: take a defined sample, run it through a forensic tool, and demonstrate what can and cannot be recovered. When the initial pilot supported further testing, the court escalated — moving from a bounded capability test to an expanded compliance requirement across all ESI custodians.

Practitioners should expect this approach to spread. Courts that have spent years hearing "it's not feasible" now have a template for testing that claim. Organizations and their eDiscovery providers should be prepared to demonstrate — not merely assert — what their tools can and cannot recover from hyperlinked content.

### Context in Production

In *Lubrizol Corp. v. IBM Corp.* (N.D. Ohio, 2023), the court required contextual production of Slack and Teams material, ordering whole conversations when the thread had 20 or fewer messages and 10 surrounding messages when it did not. Collaborative platform evidence should be produced with enough surrounding context to be meaningful — not as isolated fragments.

## The Sedona Conference Weighs In

The Sedona Conference released its "Commentary on Discovery of Collaboration Platforms Data" in 2025 — public comment opened in spring 2025, with the public comment version listed as July 2025 and the post-public-comment version in October 2025.

The Commentary catalogs the preservation, collection, and production challenges specific to collaboration platforms. It acknowledges that identifying relevant workspaces can be difficult, that data may be stored across multiple applications, and that format, unitization, and metadata of collaborative content require deliberate handling.

When The Sedona Conference — a highly influential source of eDiscovery guidance — publishes guidance acknowledging that collaboration platform data creates distinct preservation challenges, that acknowledgment becomes part of the landscape against which "reasonable steps" is evaluated. A party aware of these challenges may face increasing difficulty arguing that its traditional, email-era preservation workflow constitutes reasonable steps for evidence that behaves fundamentally differently.

This does not mean Sedona has prescribed a specific technical approach. It has identified the problem. How parties respond to that identification is what courts will evaluate.

## The Emerging Question

Rule 37(e) does not require perfection. It requires reasonableness. But reasonableness is not static. What was reasonable in 2015, when the rule was adopted, reflected the evidence landscape of that era. The evidence landscape has changed.

Consider what a party now knows — or should know — when it issues a litigation hold for a matter involving Microsoft 365 or similar platforms:

- Custodian-based holds do not automatically preserve documents linked from other custodians' locations
- The version of a document that exists at collection time may not be the version that existed when the communication was sent
- Identity, access, and organizational context change over time and are not captured by a point-of-collection directory snapshot
- Relationships between messages and documents span application boundaries that traditional holds do not traverse

Recent decisions suggest that the convergence of collaboration-platform case law, Sedona's 2025 guidance, and the known technical gaps in traditional preservation workflows raises a practical question that practitioners should expect opponents to raise in 37(e) disputes: if a party knows its evidence is collaborative, and the industry has identified specific structural gaps in traditional preservation, does continuing with final-state collection constitute "reasonable steps"?

No court has held that reconstruction-grade preservation is required by Rule 37(e). That is not the current state of the law. In my view, the stronger observation is that collaboration-platform case law, Sedona guidance, and known technical gaps are making final-state collection harder to defend as "reasonable" in certain matters involving collaborative, hyperlinked, versioned, and identity-dependent evidence.

## Two Failure Modes in Modern Preservation

The challenges described above are not a single problem. In modern collaboration environments, two distinct failure modes are emerging — and they have different legal implications.

**[The Preservation Gap](../../concepts/preservation-gap.md)** — the referenced content is never preserved. A custodian's email contains a hyperlink to a document in a non-custodian's OneDrive. The hold preserves the email. Nobody preserves the linked document. The retention clock runs out. The link is now dead. The evidence the communication referenced no longer exists anywhere. The Context Gap tells you what was damaged in transit. The Preservation Gap tells you what never made it onto the truck at all.

**[The Context Gap](../../concepts/context-gap-ediscovery.md)** — the content is preserved, but not in the state it existed at the time of the communication. The document is still there, but it has been edited since the message was sent. The preserved record reflects today's version, not the version the recipient saw. The evidence is complete but inaccurate.

The Preservation Gap aligns directly with Rule 37(e)'s focus on **loss** of ESI. Evidence that should have been preserved was not, and it cannot be restored or replaced. The legal framework fits.

The Context Gap presents a different challenge. The ESI was not lost — it was preserved. But the preserved record does not accurately reflect the state of the evidence at the relevant time. Rule 37(e) was designed for loss, not distortion. Courts do not yet have a clean doctrinal hook for "you preserved it, but what you preserved is not what was communicated."

Together, these gaps suggest that evaluating "reasonable steps" based solely on whether data was preserved may be insufficient in environments where evidence is relationship-dependent and state-dependent. Preservation completeness and preservation fidelity are separate questions — and the current legal framework addresses one more readily than the other.

## What Reconstruction-Grade Preservation Addresses

The [Reconstruction-Grade eDiscovery Standard](https://rgrstandard.org) is our proposed architectural response to the cases and commentary described above — a vendor-neutral, open-source conformance framework for evaluating preservation capabilities. It defines measurable criteria for the capabilities that, in my view, map directly to 37(e)'s requirements: deterministic version resolution (preserving the as-sent version, not just the current version), relationship preservation (maintaining bindings between messages and the specific document versions they reference), exception transparency (structured records of what could not be collected and why), reproducible exports (same scope produces same output with manifests), and graduated conformance levels (RG-Core, RG-Plus, RG-Max) that acknowledge proportionality applies to preservation capabilities, not just preservation scope. For the detailed problem-by-problem mapping of these capabilities to the challenges identified by The Sedona Conference, see [Sedona Identified the Problems. Here's the Architectural Answer.](https://rgrstandard.org/blog/sedona-identified-the-problems-heres-the-architectural-answer/)

Courts and Sedona have not endorsed this specific framework. It exists because the gap between what 37(e) requires and what traditional workflows deliver appears to be growing wider — and because the Carvana approach of testing forensic capabilities suggests that measurable, demonstrable preservation is becoming the expectation.

<hr class="rgr-divider">

## A Framework, Not a Mandate

This is not legal advice. Rule 37(e) analysis is fact-specific, and no single technical approach satisfies the rule in every matter. But the trajectory is clear: courts are expecting more technical competence in preservation, more validation of what was actually collected, and more transparency when preservation is incomplete. The Sedona Conference has acknowledged that collaboration platforms present distinct challenges. And the case law on hyperlinked documents, ephemeral messaging, and contextual production continues to develop.

The question for practitioners is not whether these issues will arise in their matters. For any organization operating on Microsoft 365, Google Workspace, Slack, or similar platforms, they already have. The question is whether the preservation workflow reflects what the industry now knows — or whether it is still calibrated for an evidence model that no longer exists.

---

*The [Reconstruction-Grade eDiscovery Standard](https://rgrstandard.org) is a vendor-neutral, open-source conformance framework for evaluating preservation and reconstruction of modern collaborative evidence. The public draft is available for review, critique, and participation.*

---

**Sources referenced in this post:**

- [FRCP Rule 37 — Cornell Legal Information Institute](https://www.law.cornell.edu/rules/frcp/rule_37)
- [Epic Games v. Google: Spoliation Lessons Learned — American Bar Association](https://www.americanbar.org/groups/antitrust_law/resources/newsletters/epic-games-v-google-lessons/)
- [Gregory v. State of Montana — Winston & Strawn](https://www.winston.com/en/insights-news/significant-sanctions-ruling-by-the-ninth-circuit-rejects-inherent-authority-and-reinforces-specific-intent-standard-for-case-ending-sanctions)
- [Selected eDiscovery and ESI Case Law from 2024 — Innovative Driven](https://www.innovativedriven.com/blog/selected-ediscovery-and-esi-case-law-from-2024/)
- [Lubrizol v. IBM — X1 Discovery](https://www.x1.com/blog/court-decision-in-lubrizol-vs-ibm-provides-important-guidance-on-ms-teams-discovery/)
- [The Preservation Nightmare of Hyperlinked Files — eDiscovery Today](https://ediscoverytoday.com/2024/08/20/the-preservation-nightmare-of-hyperlinked-files-ediscovery-trends/)
- [Commentary on Discovery of Collaboration Platforms Data — The Sedona Conference](https://www.thesedonaconference.org/node/11329)
- *In re Carvana Co. Sec. Litig.*, No. CV-22-02126-PHX-MTL, Doc. 196 (D. Ariz. Aug. 21, 2025); Doc. 255 (D. Ariz. Jan. 12, 2026)
- [eDiscovery Today — Carvana hyperlinks/FEC coverage](https://www.ediscoveryllc.com/recent-hyperlinked-documents-decision/)
- [Judicial Signals and Case Developments — RGR Standard](https://rgrstandard.org/judicial-signals/)
