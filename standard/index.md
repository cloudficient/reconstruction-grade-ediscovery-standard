---
title: Overview
description: Public overview of the Reconstruction-Grade eDiscovery Standard, its measurable scope, governance model, and evaluation tools.
hide:
  - navigation
  - toc
---

<div class="rgr-home" markdown="1">

<section class="rgr-hero" markdown="1">
<div markdown="1">
<p class="rgr-eyebrow">Versioned draft conformance standard</p>

# Reconstruction-Grade eDiscovery defines a measurable conformance target for modern collaborative evidence.

<p class="rgr-lead">It is a vendor-independent standard for preserving and reproducing collaborative evidence with point-in-time fidelity, relationship integrity, and bounded evidence handling. In cloud environments, messages often point to live files, shifting identities, changing permissions, and behavior evidence that can age out. RGR gives skeptical evaluators a versioned way to test whether enough fact was preserved to reproduce what existed at the relevant time.</p>

<div class="rgr-hero__actions" markdown="1">
[Read the Standard](front-matter.md){ .md-button .md-button--primary }
[Evaluate a Platform](toolkit/index.md){ .md-button }
[Join the Working Group](governance/index.md){ .md-button }
</div>
</div>

<aside class="rgr-status-card" markdown="1">
## Current draft

<p class="rgr-status-card__version">0.51-draft</p>
<p class="rgr-status-card__meta">Published March 3, 2026</p>

- [Front matter and executive summary](front-matter.md)
- [Version history](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/blob/main/CHANGELOG.md)
- [Latest PDF](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/releases/latest/download/rgr-standard-0.51-draft.pdf)
- [Canonical Markdown source](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/tree/main/standard)
</aside>
</section>

<section markdown="1">
<div class="rgr-card-grid" markdown="1">
<article class="rgr-card rgr-card--cta" markdown="1">
### Read the Standard

Start with the draft framing, canonical chapters, and requirement structure.

[Read the Standard](front-matter.md){ .md-button .md-button--primary }
</article>

<article class="rgr-card rgr-card--cta" markdown="1">
### Evaluate a Platform

Use the toolkit, vendor questions, scoring worksheet, and conformance tests.

[Evaluate a Platform](toolkit/index.md){ .md-button .md-button--primary }
</article>

<article class="rgr-card rgr-card--cta" markdown="1">
### Join the Working Group

Review governance and help pressure-test the draft against real practice.

[Join the Working Group](governance/index.md){ .md-button .md-button--primary }
</article>
</div>
</section>

<section markdown="1">
<p class="rgr-section__eyebrow">Why this matters now</p>
## Collaborative evidence no longer behaves like a stable attachment.

<p class="rgr-section__lede">In cloud collaboration environments, the evidentiary question is often no longer "which file was sent?" but "what did the communication point to, what existed at that moment, who could be tied to it, and what evidence remains to reproduce that state later?" That shift affects legal review, internal investigations, incident response, procurement, and platform evaluation.</p>

<div class="rgr-card-grid" markdown="1">
<article class="rgr-card" markdown="1">
### Hyperlinks replace attachments

Messages increasingly reference live objects in shared repositories rather than transmitting a fixed copy.
</article>

<article class="rgr-card" markdown="1">
### Version histories keep moving

The state relied upon at send time may differ from the state available later unless it was preserved with point-in-time discipline.
</article>

<article class="rgr-card" markdown="1">
### Permissions and identity change

Custody, ownership, and access posture are not static. Effective-dated identity and relationship evidence matter.
</article>
</div>

<p class="rgr-note">The consequence is practical: evidentiary fidelity, reproducibility, and defensibility can degrade when context is reconstructed after the fact instead of preserved while it exists.</p>
</section>

<section markdown="1">
<p class="rgr-section__eyebrow">What RGR is</p>
## Conformance standard first. Operating approach second.

<div class="rgr-card-grid rgr-card-grid--2" markdown="1">
<article class="rgr-card" markdown="1">
### Reconstruction-Grade eDiscovery (RGR)

A conformance standard that defines measurable preservation and reconstruction targets for collaborative evidence. It is versioned, testable, and intended to support platform evaluation against published criteria.
</article>

<article class="rgr-card" markdown="1">
### Context-Aware eDiscovery

The broader operating approach aligned to that standard. It treats context as evidence objects, bindings, and provenance rather than as post-hoc inference or marketing shorthand.
</article>
</div>
</section>

<section markdown="1">
<p class="rgr-section__eyebrow">What the standard measures</p>
## Measurable criteria, not abstract principles.

<p class="rgr-section__lede">Section 6 and Appendix B define requirement domains and conformance tests that can be examined, challenged, and compared against a specific version of the standard.</p>

<div class="rgr-card-grid" markdown="1">
<article class="rgr-card" markdown="1">
### Identity over time

Whether the system can preserve effective-dated identity state tied to a natural person rather than a single directory snapshot.
</article>

<article class="rgr-card" markdown="1">
### Behavior evidence

Whether relevant audit and activity signals are preserved and bounded clearly where platform availability or retention limits apply.
</article>

<article class="rgr-card" markdown="1">
### Document state

Whether referenced content can be resolved as of the relevant event time instead of being substituted with a later state.
</article>

<article class="rgr-card" markdown="1">
### Relationship integrity

Whether message, link, file, version, participant, and timeline relationships remain reproducible and traceable.
</article>

<article class="rgr-card" markdown="1">
### Export reproducibility

Whether outputs can be regenerated with manifest traceability, hashes, exception handling, and declared scope logic.
</article>

<article class="rgr-card" markdown="1">
### Operating model

Whether the preservation system of record and surrounding workflows support testable reconstruction rather than ad hoc matter-by-matter improvisation.
</article>
</div>

<p class="rgr-note">Conformance claims should reference a published version, stated scope, and the supporting artifacts or tests used to support that claim.</p>
</section>

<section markdown="1">
<p class="rgr-section__eyebrow">How to use it</p>
## Use the standard as a versioned evaluation framework.

<div class="rgr-card-grid" markdown="1">
<article class="rgr-card" markdown="1">
<p class="rgr-step__number">1</p>
### Read the standard

Start with the front matter, evaluation framework, and requirements to understand the preservation targets and definitions.
</article>

<article class="rgr-card" markdown="1">
<p class="rgr-step__number">2</p>
### Use the vendor questions

Apply [Appendix G](appendix-g-vendor-questions.md) to test how a platform explains versioning, audit coverage, relationship handling, and exceptions.
</article>

<article class="rgr-card" markdown="1">
<p class="rgr-step__number">3</p>
### Use the scoring worksheet

Apply [Appendix H](appendix-h-vendor-scoring.md) so platform comparisons are anchored to the same measurable criteria.
</article>

<article class="rgr-card" markdown="1">
<p class="rgr-step__number">4</p>
### Compare versioned declarations

Request a declaration against a specific standard version and compare the claim to the published conformance framework, not just sales language.
</article>
</div>
</section>

<section markdown="1">
<p class="rgr-section__eyebrow">Governance and participation</p>
## Visible origin, visible change control, visible participation.

<p class="rgr-section__lede">This draft was originated by Cloudficient and published openly so the requirements, terminology, and change history can be scrutinized. The stated objective is a vendor-independent conformance framework whose normative changes follow a documented governance process rather than private product positioning.</p>

<div class="rgr-card-grid rgr-card-grid--2" markdown="1">
<article class="rgr-card" markdown="1">
### Governance signals

- Normative changes follow a documented proposal and review path.
- Conformance claims must cite a specific version.
- The canonical text and change history are public.
- The governance chapter and working-group page are visible in the site itself.
</article>

<article class="rgr-card" markdown="1">
### Participation paths

- Enterprises and legal operations teams can pressure-test practical requirements.
- Law firms and service providers can review defensibility and workflow assumptions.
- Vendors can contribute under the same published criteria they are asked to meet.
- Individual practitioners can propose clarifications, examples, and non-normative improvements.
</article>
</div>

[Review governance](governance/index.md){ .md-button .md-button--primary }
[Participation options](participate/index.md){ .md-button }
</section>

<section markdown="1">
<p class="rgr-section__eyebrow">What this standard does not claim</p>
## RGR defines measurable preservation and reconstruction targets. It does not overclaim.

<div class="rgr-card" markdown="1">
- It does not itself create legal duties.
- It does not imply that every non-conforming workflow is per se deficient.
- It does not promise perfect determinism in every platform condition; it expects bounded evidence handling and explicit exception treatment where determinism is unavailable.
- It does not replace case-specific judgment about scope, proportionality, admissibility, or process.
</div>
</section>

<section markdown="1">
<p class="rgr-section__eyebrow">Current draft and transparency</p>
## Public, versioned, and reviewable.

<div class="rgr-card-grid" markdown="1">
<article class="rgr-card" markdown="1">
### Front matter and executive framing

Use the [front matter](front-matter.md) for draft status, scope framing, executive summary, and document conventions.
</article>

<article class="rgr-card" markdown="1">
### Change history and versioning

Use the [changelog](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/blob/main/CHANGELOG.md) and [governance pages](governance/index.md) to review how the draft evolves over time.
</article>

<article class="rgr-card" markdown="1">
### PDF and canonical source

Use the [latest PDF](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/releases/latest/download/rgr-standard-0.51-draft.pdf) for circulation and the [canonical Markdown source](https://github.com/cloudficient/reconstruction-grade-ediscovery-standard/tree/main/standard) for the authoritative text.
</article>
</div>
</section>

</div>
