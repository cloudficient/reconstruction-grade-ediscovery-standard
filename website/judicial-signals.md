---
title: Judicial Signals and Case Developments
description: Selected discovery decisions and disputes involving hyperlinked files, linked cloud content, feasibility limits, and collaborative evidence handling.
---

# Judicial Signals and Case Developments

Courts are increasingly confronting disputes involving linked and cloud-hosted evidence, but the decisions remain highly dependent on protocol language, factual context, relevance, and technical feasibility. This page highlights selected developments as signals of an emerging problem space, not as a substitute for legal analysis or case-specific advice.

!!! tip "Related Analysis"
    For analysis of what these developments mean for Rule 37(e) "reasonable steps" obligations, see [What FRCP Rule 37(e) Means for Modern Collaboration Platforms](blog/what-frcp-rule-37e-means-for-modern-collaboration-platforms/).

## What the cases seem to show

Across the cases below, a few recurring themes appear:

- **No blanket rule that hyperlinks are always attachments.** Courts have repeatedly resisted treating a hyperlink relationship alone as equivalent to a traditional attachment.
- **Protocol language matters.** Where parties expressly define linked documents as family members or attachments, courts may enforce that agreement.
- **Feasibility and proportionality matter just as much.** Courts have backed away from broad requirements when the producing party shows that the relationship cannot be reconstructed with existing technology at scale.
- **Targeted production often replaces automatic family production.** When linked material is important to understanding the parent communication, courts may require targeted requests or case-specific handling rather than universal production.
- **Courts may impose bounded forensic testing rather than accepting blanket infeasibility.** At least one court has ordered a targeted sample-based approach using a specific forensic tool — creating a practical middle ground between full production and no production of linked content.
- **Courts expect contextual production of collaborative messaging.** When Slack or Teams evidence is at issue, courts may require production of surrounding conversational context rather than isolated messages.
- **Collaboration platform spoliation carries the same Rule 37(e) consequences as any other ESI loss.** Courts have applied the full sanctions framework — including adverse-inference instructions under 37(e)(2) — to failures involving ephemeral messaging defaults on collaboration platforms.
- **Rule 37(e) is the exclusive framework for ESI spoliation sanctions.** An appellate court has reversed a district court for relying on inherent authority instead of applying Rule 37(e), reinforcing that the rule's specific requirements — including the intent-to-deprive standard for severe sanctions — cannot be bypassed.

## Collaboration Platform Spoliation and Contextual Production

### Gregory v. State of Montana
**9th Cir. (2024)**

The Ninth Circuit reversed a district court order that had imposed case-ending sanctions for ESI spoliation under the court's inherent authority rather than applying Rule 37(e). The appellate court held that Rule 37(e) provides the exclusive framework for sanctions when electronically stored information is lost because a party failed to preserve it, and that the district court erred by bypassing the rule's specific requirements — including the intent-to-deprive standard required for the most severe sanctions.

**Why it matters**

- The decision establishes at the circuit level that Rule 37(e) is not optional — courts must apply its framework rather than resorting to inherent authority for ESI spoliation.
- The specific-intent standard under 37(e)(2) for severe sanctions (adverse inference, dismissal, default) cannot be circumvented by invoking inherent power.
- The ruling strengthens the predictability of 37(e) analysis by confirming that it displaces broader judicial discretion for ESI-specific spoliation.

**Why it matters for system design**

- The decision reinforces that preservation failures will be evaluated through 37(e)'s structured framework — making "reasonable steps" documentation more important, not less.
- Systems that can demonstrate the specific steps taken (and exceptions encountered) during preservation are better positioned under the rule's framework than those relying on general assertions.

**References**

- [Winston & Strawn — Ninth Circuit rejects inherent authority for ESI sanctions](https://www.winston.com/en/insights-news/significant-sanctions-ruling-by-the-ninth-circuit-rejects-inherent-authority-and-reinforces-specific-intent-standard-for-case-ending-sanctions)

---

### Maziar v. City of Atlanta
**(2024)**

The court found that the City of Atlanta's failure to preserve text messages caused prejudice sufficient for Rule 37(e)(1) curative measures, without finding the intent to deprive required for Rule 37(e)(2). The court denied the City's summary-judgment motion as a curative sanction and awarded fees.

**Why it matters**

- The case demonstrates that the lower tier of Rule 37(e) has practical teeth even without intent to deprive.
- Negligent preservation failures — failing to meet the "reasonable steps" standard — can result in meaningful curative measures.
- The denial of summary judgment as a sanction shows that preservation failures can affect case outcomes even under (e)(1).

**Why it matters for system design**

- Organizations cannot assume that only intentional destruction creates litigation risk — negligent failures to preserve collaborative evidence are sanctionable.
- Systems should document preservation steps taken and exceptions encountered to demonstrate reasonableness even when preservation is imperfect.

**References**

- [Innovative Driven — Selected eDiscovery and ESI Case Law from 2024](https://www.innovativedriven.com/blog/selected-ediscovery-and-esi-case-law-from-2024/)

---

### Epic Games v. Google
**N.D. Cal. (2023)**

In this antitrust litigation, the court found in a March 2023 ruling that Google failed to take reasonable steps to preserve relevant Google Chat messages. Google employees had routinely toggled "history off" — a feature that triggered automatic deletion of chat messages — including on topics directly relevant to the litigation. The court found the lost chats could not be restored or replaced and that Google acted with intent to deprive. In an October 2023 pretrial order, the court adopted a permissive adverse-inference instruction as the Rule 37(e)(2) remedy.

**Why it matters**

- The case is the highest-profile example of collaboration platform spoliation to date.
- The "history off" default — where a platform allows evidence to disappear unless affirmatively preserved — became the central preservation failure mechanism.
- The court applied the full Rule 37(e) framework, including the intent-to-deprive finding under subsection (e)(2), resulting in an adverse-inference instruction.

**Why it matters for system design**

- Systems must ensure that platform defaults do not allow evidence destruction after a duty to preserve is triggered.
- Preservation workflows must account for ephemeral and auto-deleting message features, not just files and email.
- Organizations must be able to demonstrate that litigation holds override platform-level deletion defaults.

**References**

- [ABA — Epic Games v. Google: Spoliation Lessons Learned](https://www.americanbar.org/groups/antitrust_law/resources/newsletters/epic-games-v-google-lessons/)
- [CNBC — Google not preserving chats merits sanctions](https://www.cnbc.com/2023/03/28/google-not-preserving-chats-in-epic-case-merits-sanctions-judge-says-.html)
- [Legal Dive — Deleted messages bedeviled Google](https://www.legaldive.com/news/deleted-messages-google-antitrust-case-epic-games-deliberate-spoliation-donato/702306/)

---

### Lubrizol Corp. v. IBM Corp.
**N.D. Ohio (2023)**

In this breach of contract action, the court addressed whether individual Slack messages should be treated as discrete documents or whether a Slack channel is a continuous conversation requiring contextual production. The court required contextual production of both Slack and Teams material: entire conversations when the thread had 20 or fewer messages, and 10 messages before and after responsive messages in larger channels.

**Why it matters**

- The court recognized that collaborative messaging evidence requires surrounding context to be meaningful.
- Rather than treating individual messages as standalone documents, the ruling treats conversational threads as contextual units.
- The same production approach was applied to both Slack and Microsoft Teams, establishing a cross-platform expectation.

**Why it matters for system design**

- Preservation and export tools must capture thread context, not isolated messages.
- Export formats should support configurable context windows around responsive content.
- Systems must maintain the conversational structure of collaborative messaging data through preservation and production.

**References**

- [X1 Discovery — Lubrizol guidance on Teams discovery](https://www.x1.com/blog/court-decision-in-lubrizol-vs-ibm-provides-important-guidance-on-ms-teams-discovery/)
- [Minerva26 — Lubrizol case analysis](https://minerva26.com/episode-108-is-an-individual-slack-message-considered-a-document-under-frcp-34/)

---

## Selected developments

### Yotta Technologies Inc. v. Evolve Bancorp, Inc.
*Often cited as Yotta Technologies Inc. v. Evolve Bank & Trust in eDiscovery commentary*
**N.D. Cal. (2026)**

Yotta is a useful recent signal because it restates the foundational cautionary line clearly while also acknowledging that context can still require production of linked material. The decision confirms that the default rule against automatic attachment treatment remains intact even as courts become more familiar with the technology.

**Why it matters**

- The court agreed that a hyperlink relationship alone does not mean the linked document should be treated as an attachment and produced.
- At the same time, the court recognized that production of linked material may still be appropriate depending on the nature of the produced document.
- Its reliance on the broader line of authority shows that the foundational rule has stabilized, even as its application remains fact-specific.

**Why it matters for system design**

- Systems should preserve enough relationship and provenance evidence to support targeted, context-sensitive handling — not just the existence of the link.
- The decision reinforces the need for capability models that distinguish between link existence, relationship preservation, and reproducible historical state.

**References**

- [Recent Yotta discussion](https://www.ediscoveryllc.com/recent-hyperlinked-documents-decision/)
- [Later coverage quoting the ruling](https://ediscoverytoday.com/2026/02/27/four-categories-of-documents-requested-by-plaintiffs-denied-by-court-ediscovery-case-law/amp/)
- [Case page](https://cand.uscourts.gov/cases-e-filing/cases/324-cv-06456-tlt/yotta-technologies-inc-v-evolve-bancorp-inc-et-al)

---

### In re Carvana Co Securities Litigation
*Often cited in eDiscovery commentary as United Association National Pension Fund v. Carvana Company, following plaintiffs' counsel press materials rather than the official caption*
**D. Ariz. (January 12, 2026)**

Arizona Magistrate Judge John Z. Boyle issued a January 2026 discovery order in this securities MDL addressing document retrieval. Based on eDiscovery Today reporting — the underlying order is not publicly available — the ruling addressed hyperlinked attachments, allowing plaintiffs to select batches of up to 250 emails for defendants to process using Forensic Email Collector (FEC), with defendants required to provide the most contemporaneous version of non-privileged linked attachments within 10 days.

> **Source confidence: secondary reporting only.** The characterization of this order rests on eDiscovery Today reporting. The underlying order is not publicly available as of this writing. The Courthouse News report of the same hearing characterizes the ruling more broadly as a document retrieval methodology dispute.

**Why it matters**

- Rather than accepting infeasibility wholesale or requiring full production, the court appears to have ordered a targeted, bounded approach: a defined sample processed through a specific named forensic tool.
- This would represent a practical middle ground between the StubHub and Uber outcomes — testing available forensic capability before accepting production limits.
- The hyperlinks framing comes from a single secondary source; a Courthouse News report of the same hearing characterizes the ruling more broadly as a document retrieval methodology dispute.

**Why it matters for system design**

- Systems and providers should be prepared to demonstrate — not merely assert — what forensic tools can and cannot recover from linked content.
- Capability models should account for the possibility that courts will order bounded forensic testing as a condition before accepting production limits.

**References**

- [eDiscovery Today coverage (hyperlinks/FEC framing)](https://www.ediscoveryllc.com/recent-hyperlinked-documents-decision/)

---

### In re Uber Technologies, Inc., Passenger Sexual Assault Litigation
**N.D. Cal. (2024–2025)**

The Uber disputes are among the clearest examples of courts confronting collaborative evidence directly: modern attachments, linkage metadata, contemporaneous versions, and feasibility limits all appear in the same line of orders. The litigation produced a court-approved protocol that expressly included hyperlinks within the attachments definition, while simultaneously acknowledging that contemporaneous production was not always technically achievable.

**Why it matters**

- The court-approved protocol treated hyperlinks and "modern attachments" as within the attachments definition, showing that protocol language can expand obligations beyond the default rule.
- The court recognized feasibility limits, stating that contemporaneous linked-file production was not required where no existing technology makes it feasible — but drew a practical line between ordinary Google Drive links and harder categories such as material in Google Vault.
- The court also moved toward a targeted-request process for certain categories of linked material rather than automatic production of every linked item.

**Why it matters for system design**

- Systems should preserve linkage metadata, repository identifiers, and enough supporting evidence to reproduce or bound the historical state later.
- Where full determinism is not available, capability limits should be declared explicitly rather than obscured behind generic "attachment" language in protocol agreements.

**References**

- [Official March 3, 2025 order (PDF)](https://www.govinfo.gov/content/pkg/USCOURTS-cand-3_23-md-03084/pdf/USCOURTS-cand-3_23-md-03084-97.pdf)
- [Case page](https://www.cand.uscourts.gov/cases-e-filing/cases/323-md-03084-crb/re-uber-technologies-inc-passenger-sexual-assault-litigation)
- [Discussion of the March 2025 order](https://www.jdsupra.com/legalnews/uber-technologies-another-hyperlink-2148686/)
- [Discussion of the 2024 ESI protocol dispute](https://app.ediscoveryassistant.com/case_law/57047-in-re-uber-techs-inc-passenger-sexual-assault-litig)

---

### In re Insulin Pricing Litigation
**D.N.J. (May 28, 2024)**

In this MDL, New Jersey Magistrate Judge Rukhsanah L. Singh ruled on contested ESI protocol issues, agreeing with defendants that hyperlinks are not the same as traditional attachments. The court found it was not feasible, practicable, or proportionate to produce hyperlinked documents in family groups — particularly when attempting to produce the as-sent version of any linked document.

**Why it matters**

- The court applied the same feasibility-focused reasoning seen in StubHub and other N.D. Cal. decisions, but in a New Jersey federal court, extending the trend beyond a single district.
- Like StubHub, the court evaluated the actual technical burden rather than applying a categorical rule about how hyperlinks must be treated.
- The as-sent version problem — capturing what a linked document looked like at the moment of transmission — was specifically identified as a feasibility barrier.

**Why it matters for system design**

- Systems must be able to articulate the specific feasibility constraints of producing hyperlinked content as family groups, not just assert that it is difficult.
- Capability declarations should describe what reconstruction is achievable and what is not, with enough specificity to support the burden analysis courts are performing across jurisdictions.

**References**

- [Insulin Pricing Litigation coverage](https://ediscoverytoday.com/2024/06/03/court-rules-hyperlinks-are-not-the-same-as-traditional-attachments-ediscovery-case-law/)

---

### In re StubHub Refund Litigation
**N.D. Cal. (2023–2024)**

StubHub is important because it shows both sides of the issue: first, a court enforcing protocol language that expressly treated hyperlinked files as attached documents; later, the same court modifying that requirement after a stronger technical record was developed.

**Why it matters**

- Earlier protocol language expressly said hyperlinked files had to be produced as separate attached documents, and the court initially enforced what the parties had agreed to.
- Later, after extensive effort and a fuller evidentiary record, the court modified the ESI order after finding that broad compliance was not technologically possible and that no commercially available or custom program existed to perform the requested collection comprehensively.
- The court instead accepted a narrower targeted approach for additional linked documents.

**Why it matters for system design**

- Discovery obligations can turn on promises made in protocols before the true technical limits are understood.
- Systems and providers should distinguish clearly between demonstrable capability and aspirational workflow language.
- Bounded evidence handling is not an excuse; it is a requirement to state what can and cannot be reconstructed with specificity.

**References**

- [Official May 20, 2024 order (PDF)](https://www.govinfo.gov/content/pkg/USCOURTS-cand-4_20-md-02951/pdf/USCOURTS-cand-4_20-md-02951-42.pdf)
- [StubHub order discussion](https://www.jdsupra.com/legalnews/stubhub-modification-of-esi-protocol-3301137/)
- [ACEDS discussion of StubHub](https://aceds.org/navigating-hyperlinks-in-ediscovery-lessons-from-the-stubhub-refund-litigation-aceds-b/)

---

### In re Meta Pixel Healthcare Litigation
**N.D. Cal. (2023 / later cited in 2026)**

This case reinforced the cautionary position established in Noom and continued to be cited in later hyperlink disputes through 2026. It reflects a consistent reluctance to treat a hyperlink relationship as automatically requiring attachment-style treatment.

**Why it matters**

- The case is cited for the proposition that a hyperlink relationship does not, by itself, require treatment of the linked document as an attachment.
- It reflects a context-sensitive approach that evaluates the relationship rather than assuming it carries the same obligations as a traditional attachment.
- Its continued citation into 2026 shows that the foundational principle has held even as courts encounter more technically complex scenarios.

**Why it matters for system design**

- Relationship evidence should be preserved explicitly where possible, rather than assumed to follow from the presence of a link.
- Systems should distinguish between the existence of a link and the existence of a preserved, reproducible evidentiary relationship.

**References**

- [Meta Pixel order discussion](https://www.fredlaw.com/alert-hyperlinks-to-documents-are-not-the-same-as-traditional-attachments)
- [Later citation in Yotta coverage](https://www.ediscoveryllc.com/recent-hyperlinked-documents-decision/)

---

### Nichols v. Noom, Inc.
**S.D.N.Y. (2021)**

This early decision became a reference point for the proposition that hyperlinks should not automatically be treated as traditional attachments for discovery purposes. Rather than extending the traditional attachment analogy, the court focused on the underlying technology and actual collection method.

**Why it matters**

- The court did not accept the view that a hyperlink relationship alone makes the linked content an attachment.
- The decision pushed the discussion toward the actual collection method rather than forcing a simplistic analogy to legacy email attachments.
- It helped frame hyperlinked files as a distinct discovery problem requiring their own analysis.

**Why it matters for system design**

- Systems should not assume that a hyperlink can be treated as a self-contained evidence object equivalent to an embedded attachment.
- Preservation and reconstruction need to account for the referenced object, its state over time, and the limits of what the available evidence can support.

**References**

- [Nichols v. Noom, Inc. discussion](https://app.ediscoveryassistant.com/case_law/32615-nichols-v-noom-inc)
- [Commentary on Nichols](https://www.jdsupra.com/legalnews/what-hath-noom-wrought-7577098/)

---

## What this means for system design

These decisions do not establish a single technical rule for linked and collaborative evidence. They do, however, repeatedly surface the same operational questions:

- Can the relationship between a communication and the referenced artifact be preserved?
- Can the relevant state be reproduced as of the event time rather than substituted with a later version?
- Does identity, access, and audit evidence survive long enough to support reconstruction?
- Are platform limits and retention gaps declared clearly when full determinism is not available?

Reconstruction-Grade eDiscovery (RGR) is intended to make those questions measurable. It does not claim that courts have adopted a single uniform rule. It provides a conformance framework for evaluating whether platforms and workflows preserve enough evidence to support defensible reconstruction, and whether declared limits are stated clearly when they do not.

## Boundary note

This page tracks selected developments relevant to collaborative evidence and hyperlinked or cloud-linked content. It is not legal advice, not a complete survey of all authority, and not a substitute for matter-specific analysis of scope, proportionality, protocol language, or applicable law.