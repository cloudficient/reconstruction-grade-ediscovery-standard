---
date: 2026-04-28
draft: false
description: "AI review now costs $0.11–$0.50 per document. But if collection fed wrong versions and broken threads, cheaper review just gets to the wrong answer faster."
authors:
  - peterkozak
categories:
  - Legal Analysis
  - Research & Dialogue
tags:
  - AI Review
  - Collection Fidelity
  - eDiscovery Costs
  - Microsoft 365
  - Collaboration Platforms
  - TAR
  - Craig Ball
chat_prompts:
  - "What percentage of eDiscovery spend goes to document review, and why hasn't AI fixed it?"
  - "How does collection fidelity affect TAR and AI review accuracy?"
  - "What does 'all versions' collection actually mean in a collaborative SharePoint environment?"
  - "What questions should I ask my eDiscovery vendor about collection methodology?"
---

# AI Review Got Cheaper. Bad Collection Got More Expensive.

![Fragmented evidence — broken chains, shattered conversations, torn document fragments — funneled through a sleek portal into neat stacks of color-coded documents](../../images/blog/blog-ai-review-cheaper-collection.webp)

**AI review is getting cheaper, fast.**

**Relativity bundled aiR for Review and aiR for Privilege into standard RelativityOne packaging. Everlaw made single-document AI actions free. GenAI-assisted review pricing is now clustering in the $0.11–$0.50 range — challenging the $0.50–$1.00 band where human review still lives.**

**The industry is celebrating the new unit economics.**

**But nobody is asking what those AI models are actually reviewing — or how much of it should never have entered the pipeline.**

<!-- more -->

The headlines write themselves: *review costs are finally moving in the right direction.* The [Winter 2026 eDiscovery Pricing Survey](https://complexdiscovery.com/the-pricing-pulse-document-review-insights-from-the-winter-2026-ediscovery-pricing-survey/) confirms the trajectory — GenAI-assisted review clustering well below traditional human rates, with the major platforms folding AI capabilities into base offerings. Per-document review cost is heading toward a fraction of what it was two years ago.

But review cost per document was never the whole problem. The real question is: **how many documents are in your review set that shouldn't be there, and how many of the ones that should be there are missing the context your reviewers — human or AI — need to get the answer right?**

That question leads upstream — past the review platform, past the culling filters, past the processing pipeline — all the way back to collection. And the economics of that pipeline tell a story the industry hasn't fully reckoned with.

---

## The $18,000-Per-Gigabyte Question

In 2012, the RAND Institute for Civil Justice published what remains the gold-standard study on eDiscovery expenditures. Nicholas Pace and Laura Zakaras examined 57 large-volume productions and found that **document review consumed 73% of total eDiscovery production costs** — approximately $14,000 of every $18,000 spent per gigabyte.[^1]

That ratio has shifted modestly. By 2024, ComplexDiscovery's market analysis placed review at **64% of total eDiscovery spend** — roughly $10.8 billion of a $16.9 billion global market.[^2] Collection's share has risen from 8% to 16%, and is projected to **double** to $6.03 billion by 2029 — the fastest-growing segment in the industry.[^2]

Review's share is declining for two reasons at once: review is getting cheaper, and collection and processing are getting more expensive. Data sources are more complex, collaboration platforms generate more volume, and the gap between what tools collect and what actually matters is widening.

Here's the math that should concern every litigation budget holder: **every unnecessary gigabyte that enters the pipeline incurs costs at every downstream stage — hosting, processing, culling, and review.** Historically, downstream costs have amplified over-collection many times over — when collection represented 8% of spend and review consumed 73%, problems originating in collection cascaded disproportionately through the most expensive phases of the pipeline.[^1]

The question isn't just what review costs per document. It's what you're *paying to review* — and whether it needed to be there at all.

---

## The Fidelity Trap

For organizations collecting from Microsoft 365, the native eDiscovery collection tool is Microsoft Purview. Purview's cloud attachment collection capabilities have evolved — it now supports collecting the live version, the version at the time of sharing (with appropriate retention label configuration), or multiple versions.[^3] That's progress.

But the capability ceiling and the operational default are not the same thing.

Capturing the version at the time of sharing requires **E5 retention labels configured prospectively** — meaning the label must be in place *before* the sharing event occurs. That requires an E5 license, which carries significant per-user cost, and proactive configuration. Without that configuration, the default behavior documented by Microsoft is to collect the current live version of the hyperlinked file.[^3]

Microsoft's own documentation acknowledges the gap: "the version you collect and add to a review set or export might be different from the version that was originally shared in the cloud attachment."[^3]

Purview's review-set workflow does now expose version-collection modes — Latest, Recent 10, Recent 100, or All versions — giving operators more granularity than a simple binary choice.[^3] That's a meaningful improvement. But the options still frame the question in terms of *how many versions to collect*, not *which version corresponds to a specific custodian interaction.*

In a collaborative environment — where teams co-author documents, iterate on proposals, revise contracts, and update analyses — even "Recent 10" can mean ten versions of a document that was edited daily, none of which may correspond to the version a custodian shared or relied upon at a specific point in time. And "All versions" can mean **every retained save/version event across the lifecycle of every hyperlinked document.** A single SharePoint document with an active collaboration history might have 20, 50, or 100+ versions. Multiply that across a custodian population sharing documents from shared libraries, and "all versions" isn't a preservation strategy — it's a data explosion.

Craig Ball identified this problem precisely in his [four-version taxonomy](https://craigball.net/2024/04/08/cloud-attachments-versions-and-purview/). When a custodian shares a hyperlinked document, four distinct versions may matter:

1. **The version existing when sent** — what the sender intended to share
2. **The version first viewed by recipients** — what recipients actually saw
3. **The version last viewed by recipients** — the final state recipients engaged with
4. **The most current version** — what exists now

Microsoft's documented options address the current version by default and can address the shared version when the required prospective retention-label configuration is in place. They do not appear to target #2 and #3 — the version first viewed and the version last viewed by recipients — as custodian-interaction-specific collection targets.[^4]

The result: without the E5 investment and proactive configuration, you get one version that may bear no relationship to the communication it was shared in. With full configuration and "all versions," you get dozens of versions, most of which are irrelevant — but still may not reliably include the specific version that was viewed or relied upon at a given point in time.

The underlying challenge isn't the tool's capability ceiling — it's that the tool asks *how many versions* rather than *which version mattered for this custodian's interaction.* That's the question the collection workflow needs to answer.

---

## The Waterfall of Waste

When collection scope is broader than it needs to be — or when the collected data includes versions that don't correspond to any custodian interaction — the cost doesn't land once. It cascades through every stage of the eDiscovery pipeline.

**Stage 1: Hosting.** Cloud hosting and review platform ingestion are priced per gigabyte. Every unnecessary version of every SharePoint document occupies storage that appears on your invoice.

**Stage 2: Processing.** Raw collected data must be processed — extracted, indexed, de-NISTed, and prepared for culling. Processing fees are typically per-gigabyte. The pipeline doesn't know which versions matter. It processes all of them.

**Stage 3: Culling.** This is where the industry assumes the problem gets fixed. Date-range filters, keyword searches, deduplication, email threading — all designed to reduce the review population to what's relevant.

But culling has limits. **Deduplication catches exact copies. It does not catch 50 near-duplicate versions of the same SharePoint document** that differ by a paragraph, a tracked change, or a single cell in a spreadsheet. Each version has a different hash. Each survives dedup. Each enters the review population.

Keyword culling is similarly blind to the version problem. If the relevant keyword appears in version 12 and version 47 of the same document, both versions hit. Neither is necessarily the version the custodian saw.

Email threading depends on threading metadata surviving collection. Microsoft Teams compliance records handle threading differently depending on the conversation type: standard and private channel posts include the responsive message and all replies, but [1:1 and group chat transcripts can include messages within a 12-hour window](https://learn.microsoft.com/en-us/purview/ediscovery-teams-workflow) around responsive items — potentially splitting extended conversations across multiple transcript files. When collection fragments threads, downstream threading tools cannot reconstruct what was separated at the source.

**Stage 4: Review.** Whatever survives culling lands on a reviewer's screen — human or AI. And this is where the cost compounds most severely. A reviewer encountering 30 near-duplicate versions of the same document doesn't just review 30 documents. They **context-switch** between versions, trying to determine which one matters, whether the differences are material, and how each version relates to the communication it was shared in. APA research on task switching shows toggling between contexts can [reduce productivity by up to 40%](https://www.apa.org/topics/research/multitasking) — a penalty that applies directly when reviewers must reconstruct version context the collection workflow didn't preserve.[^5]

**You've paid four times** — hosting, processing, culling, review — for data that should never have entered the pipeline. And the most expensive stage is the one where the damage is worst.

Culling does important work. Deduplication can cut volumes by [30–40%, and in some cases up to 90%](https://edrm.net/2022/08/how-denisting-and-deduplication-instantly-reduce-ediscovery-costs/).[^6] In one Perkins Coie case study, [email threading reduced review costs by up to 65%](https://ccbjournal.com/articles/getting-smart-email-e-discovery---how-email-threading-can-lower-costs-and-increase-sp).[^7] But these tools assume the collection population is structurally sound — that threads are intact, that document families are complete, that the version in the collection is the version that matters. When collection produces version sprawl, culling reduces volume but not version noise.

EDRM has been advocating for [moving eDiscovery upstream](https://edrm.net/2024/02/moving-ediscovery-upstream/) — investing earlier in the pipeline to reduce downstream costs. That's the right instinct. But "upstream" has been interpreted as "filter earlier" or "collect less." The missing dimension is **fidelity**: not just collecting less data, but collecting the *right* data — the version that corresponds to the custodian's interaction, with the context that makes it meaningful.

---

## AI Won't Save You Either

AI review models — whether TAR, predictive coding, or large language models — share a fundamental constraint with human reviewers: **they can only evaluate what they're given.**

The EDRM's [TAR Guidelines](https://edrm.net/wp-content/uploads/2019/02/TAR-Guidelines-Final.pdf) establish rigorous protocols for seed set selection, training, recall measurement, and quality control. But these protocols are built for measuring and improving review quality *within* a document population — they do not address how upstream collection fidelity affects the composition of that population in the first place.[^8] Recall is measured against a universe of documents that is implicitly assumed to represent the full scope of relevant evidence. When that universe is incomplete or structurally degraded, the recall metric itself becomes unreliable.

Consider what happens when AI review encounters documents from a low-fidelity collection:

- **A Teams message references a shared document, but the hyperlinked file was collected at its current version — not the version that existed when the message was sent.** The AI classifies the document based on content that may have changed materially since the communication. It doesn't flag the version discrepancy because it has no way to detect it.

- **A conversation thread spanning multiple days was collected across separate compliance record transcripts.** The AI reviews each fragment independently. Context that spans transcripts — the question in one record and the answer in another — may be invisible to the model.

- **A modern attachment link resolved to a dead URL at collection time.** The parent message is in the review set. The document it referenced is not. The AI classifies the message without the document that gave it meaning.

In each case, the AI doesn't produce an error. It produces **a confident classification based on incomplete evidence.** The gap doesn't surface as a warning or a flag. It surfaces as a relevance determination that looks correct but is based on a document the custodian never saw, a thread the custodian never had, or an attachment the custodian could no longer access.

Grossman and Cormack's foundational research — including their widely cited 2011 *Richmond Journal of Law & Technology* article — demonstrated that TAR can be "more effective and more efficient than exhaustive manual review."[^9] That advantage is meaningful, and it is well-established for review *within a defined corpus.* But it is measured against a document population that is assumed to be complete. When the population itself is incomplete or degraded, recall percentages become misleading. You can achieve 95% recall against a universe that's missing 30% of the relevant evidence and still produce a fundamentally deficient review.

AI makes review cheaper per document. It does not make collection fidelity less important. If anything, it makes it *more* important — because AI processes documents at a speed and scale where human spot-checking can't catch what the algorithm missed. At 50 documents per hour, a human reviewer might notice a version discrepancy. At thousands of documents per hour, AI will classify through it without hesitation.

**The cost of review per document is falling. The cost of reviewing the *wrong* documents hasn't changed.**

This is not just an eDiscovery problem. Broader legal AI commentary has begun calling out the same pattern — unit-cost savings celebrated before net productivity, verification cost, and input quality are measured.[^16] "$0.50 per document" is not a productivity claim unless the review population is structurally sound. If the input set contains wrong versions, fragmented conversations, and orphaned links, the lower unit cost simply accelerates review of a degraded evidence universe.

None of this is a criticism of TAR validation inside a defined corpus. TAR's recall and precision measurements are rigorous and meaningful for the population they are measured against. The warning here is different: it is about pretending the corpus boundary is self-validating. Recall against an undefined evidence universe is not a metric; it is a number.

This is the gap the [Reconstruction-Grade eDiscovery Standard](https://rgrstandard.org/) is designed to name: not whether review technology can classify documents efficiently, but whether the evidence universe being classified was reconstructed with enough fidelity for those classifications to mean anything.

---

## The Non-Custodial Flood

The version problem is compounded by a scope problem that affects virtually every matter involving shared data sources.

Consider a common fact pattern: a litigation matter involves 12 custodians who collaborate through shared infrastructure — a departmental SharePoint library, a shared Teams channel, a common OneDrive folder. The shared library contains thousands of documents, each with multiple versions.

Under traditional collection methodology, the options are:

1. **Collect the entire shared source.** Every document, every version — regardless of whether any custodian in scope ever interacted with it. The rationale: we can't risk missing something.
2. **Don't collect the shared source.** Treat it as non-custodial and out of scope. The rationale: proportionality.

Neither is satisfactory. Option 1 floods the pipeline with irrelevant data. Option 2 risks missing evidence that is directly relevant to custodian communications — the documents they shared, discussed, relied upon, or approved.

There is a third approach, grounded in what RGR calls context-aware collection: **collect only the documents the custodians actually interacted with, at the versions corresponding to their interactions.**

If 12 custodians interacted with 12 files in a library of 5,000 documents — each with an average of 20 versions — the traditional "collect everything" approach produces 100,000 document-versions. The context-aware approach targets 12 documents at the specific versions matching custodian interaction. The difference is orders of magnitude.

And when the specific version corresponding to a custodian's interaction is no longer available — because retention policies have purged it, or because the version history has been truncated — the context-aware approach doesn't silently substitute the current version and call it done. It collects the closest available version **and produces a documented exception**: this is what we collected, this is when the custodian interacted with it, and this is the gap between the two.

That exception report is not a failure. **It is defensibility.** It demonstrates that the collecting party understood what evidence mattered, attempted to collect the right version, and transparently documented where the evidence record is incomplete. Compare that to the alternative: collecting the current version, presenting it as the document the custodian relied on, and never disclosing that the version has changed — because the collection workflow had no mechanism to detect the discrepancy.

---

## The Exception Trail

Courts evaluating preservation efforts under FRCP Rule 37(e) ask whether a party took "reasonable steps" to preserve relevant ESI. The reasonableness inquiry is practical: did the party understand what evidence existed, take affirmative steps to preserve it, and document their methodology?[^10]

Most matters do not produce the kind of intentional-spoliation sanctions that have hit cases like *DR Distributors v. 21 Century Smoking* — where counsel was held personally liable for failing to verify cloud-based ESI sources.[^11] But the doctrinal trajectory is instructive: courts are increasingly receptive to asking whether parties understood their evidence landscape, used available technology proportionate to what they knew, and documented their methodology — not just their preservation intent.

The Sedona Conference's [Commentary on Discovery of Collaboration Platforms Data](https://www.thesedonaconference.org/node/11329) (public comment version July 2025; post-comment revision October 2025) explicitly identifies the challenge: "finding and collecting hyperlinked documents, and associating the correct version with a contemporaneous communication, can be particularly complex."[^14] Sedona's [Principle 6](https://www.thesedonaconference.org/sites/default/files/3-2_Sedona_Principles_3d_Ed.pdf) establishes that responding parties are best situated to choose the methods and technologies for preserving and producing their own ESI; Comment 6.d supports documenting and validating the discovery process.[^15]

A collection methodology that transparently documents what it collected, what version it targeted, and where gaps exist is in a fundamentally stronger defensibility position than one that silently collected whatever version happened to exist at the time and presented it without qualification.

The exception trail isn't overhead. It's the documentation that demonstrates reasonable steps were taken — and that the party understood what reasonable steps looked like in the context of modern collaboration evidence.

---

## The Right Version

The eDiscovery industry has spent two decades debating *how much* to collect. Broadest reasonable scope versus proportional scope. Collect everything versus targeted collection. Cast a wide net versus surgical precision.

That debate has mostly been about **volume**: documents, custodians, sources, gigabytes. The 2015 amendments to Rule 26(b)(1), TAR, AI review, culling, deduplication, and threading all gave practitioners better tools to manage volume. But volume was never the only dimension that mattered.

The dimension the industry has not systematically addressed is **fidelity**: whether the evidence that enters the pipeline accurately represents what custodians created, shared, viewed, and relied upon. Whether the version collected is the version that mattered. Whether the thread preserved is the thread the participants experienced. Whether the relationship between a message and its linked document survived collection intact.

RGR addresses this dimension directly. It defines tiers of collection fidelity — from baseline compliance through full reconstruction-grade — and provides a framework for measuring whether a collection methodology preserves the evidence relationships that make documents meaningful in their original context.

The principle is simple: **collect the right version, at the right moment, for the right custodian.** Not the current version. Not all versions. The version that corresponds to the custodian's interaction — with a documented exception when that version is no longer available.

When collection gets the version right:

- **Hosting costs drop** — you're storing what matters, not every version that ever existed
- **Processing costs drop** — the pipeline handles a fraction of the data
- **Culling becomes surgical** — there's no version noise to filter through
- **Review becomes accurate** — reviewers and AI models see what the custodian saw
- **Defensibility improves** — you can articulate exactly what you collected and why

The AI review revolution is real, and per-document costs will continue to fall. But cheaper review doesn't fix expensive collection. **The most impactful cost reduction in eDiscovery isn't faster review — it's never sending the wrong data to review in the first place.**

---

## What Should You Be Asking?

If you're responsible for eDiscovery costs — whether as general counsel, litigation support, or outside counsel managing a matter — here are the questions this analysis raises:

1. **What version of hyperlinked documents does your collection tool capture?** The current version? All versions? Or the version that existed when the custodian shared or accessed it?

2. **How does your workflow handle non-custodial shared sources?** Do you collect entire SharePoint libraries, or can you scope collection to the files custodians actually interacted with?

3. **What happens when the right version isn't available?** Does your collection silently substitute the current version, or does it document the gap?

4. **How much of your review population consists of near-duplicate versions of the same document?** If you don't know the answer, you're paying to review all of them.

5. **What is your AI review model actually classifying?** If the input includes wrong versions, broken thread fragments, and orphaned modern attachment links, the output reflects those gaps — regardless of the model's accuracy on well-formed inputs.

6. **What percentage of your collected data is relevant to custodian interactions versus collected as a byproduct of scope decisions?** The delta between those numbers is the tax you're paying at every stage of the pipeline.

The tools to answer these questions exist today. The [Reconstruction-Grade eDiscovery Standard](https://rgrstandard.org/) provides a framework for evaluating whether your collection methodology addresses them. The economics are clear: the most expensive data in your pipeline is the data that shouldn't be there.

**AI review is getting cheaper. Make sure it has something worth reviewing.**

---

[^1]: Nicholas M. Pace & Laura Zakaras, *Where the Money Goes: Understanding Litigant Expenditures for Producing Electronic Discovery*, [RAND Monograph MG-1208-ICJ (2012)](https://www.rand.org/pubs/monographs/MG1208.html). Review = 73% of total production costs; approximately $18,000 per gigabyte total production cost. RAND notes results cannot be generalized to all litigants or all large corporations.

[^2]: ComplexDiscovery, [*2024-2029 eDiscovery Market Size Mashup*](https://complexdiscovery.com/complete-look-complexdiscoverys-2024-2029-ediscovery-market-size-mashup/) (January 2025). Review = 64% of 2024 spend; collection projected to double from $2.70B to $6.03B by 2029.

[^3]: Microsoft Learn, [*Collect cloud attachments in eDiscovery (Premium)*](https://learn.microsoft.com/en-us/purview/ediscovery-cloud-attachments). Documents version discrepancy between collected and originally shared versions, and the Latest / Recent 10 / Recent 100 / All versions options in the review-set workflow.

[^4]: Craig Ball, [*Cloud Attachments: Versions and Purview*](https://craigball.net/2024/04/08/cloud-attachments-versions-and-purview/) (April 2024). Four-version taxonomy. Inference that Purview's documented options do not target #2 and #3 as custodian-interaction-specific collection targets is drawn from Ball's taxonomy combined with Microsoft's documentation in [^3].

[^5]: American Psychological Association, [*Multitasking: Switching Costs*](https://www.apa.org/topics/research/multitasking). Task switching can reduce productivity by up to 40%.

[^6]: EDRM, [*How De-NISTing and Deduplication Instantly Reduce eDiscovery Costs*](https://edrm.net/2022/08/how-denisting-and-deduplication-instantly-reduce-ediscovery-costs/) (2022). Deduplication savings of 30–40%, up to 90% in some cases.

[^7]: Perkins Coie case study reported in [*Getting Smart about Email in E-Discovery*](https://ccbjournal.com/articles/getting-smart-email-e-discovery---how-email-threading-can-lower-costs-and-increase-sp). Single-firm case study; not a generalized industry benchmark.

[^8]: EDRM, [*Technology Assisted Review (TAR) Guidelines*](https://edrm.net/wp-content/uploads/2019/02/TAR-Guidelines-Final.pdf) (January 2019). Guidelines address workflow, training, validation, and recall measurement within a document population; they do not address how upstream collection fidelity affects the composition of that population.

[^9]: Maura R. Grossman & Gordon V. Cormack, *Technology-Assisted Review in E-Discovery Can Be More Effective and More Efficient Than Exhaustive Manual Review*, 17 Rich. J.L. & Tech. 11 (2011). Foundational authority on TAR effectiveness, drawing on TREC Legal Track evaluation data.

[^10]: FRCP Rule 37(e) requires showing that ESI "should have been preserved in the anticipation or conduct of litigation," was "lost because a party failed to take reasonable steps to preserve it," and "cannot be restored or replaced through additional discovery."

[^11]: *DR Distributors, LLC v. 21 Century Smoking, Inc.*, No. 12-cv-50324 (N.D. Ill. Oct. 5, 2022). Sanctions of $2,526,744.76 for failure to preserve cloud-based ESI; counsel held personally liable for approximately $1.25 million. Reported by [eDiscovery Today](https://ediscoverytoday.com/2022/10/10/plaintiffs-awarded-2-5-million-in-fees-in-dr-distributors-case-ediscovery-case-law/).

[^14]: The Sedona Conference, [*Commentary on Discovery of Collaboration Platforms Data*](https://www.thesedonaconference.org/node/11329) (public comment version July 2025; post-comment revision October 2025). Addressing hyperlinked document collection and versioning challenges in collaboration platforms.

[^15]: The Sedona Conference, [*The Sedona Principles, Third Edition*](https://www.thesedonaconference.org/sites/default/files/3-2_Sedona_Principles_3d_Ed.pdf) (2018). Principle 6 establishes that responding parties are best situated to choose preservation and production methods and technologies; Comment 6.d addresses documentation and validation of the discovery process.

[^16]: ComplexDiscovery, [*We Wanted Smarter Legal Tech, but Instead Got an Expensive Dependency*](https://complexdiscovery.com/we-wanted-smarter-legal-tech-but-instead-got-an-expensive-dependency/) (April 10, 2026). Source for the broader legal-AI productivity-measurement critique referenced as a parallel pattern.
