---
title: Editorial Audit 2026-08-29
type: reference
visibility: gm
note_status: draft
status: active
tags: [meta, audit, editorial, review]
aliases: [The Full Audit, Editorial Audit]
created: 2026-08-29
updated: 2026-08-29
---

# The Turning — Full Editorial Audit

> An honest, end-to-end reading of everything built so far, what to refine, what doesn't hold up, and where to go next.
>
> **Prepared 2026-08-29** · Covers Epics 0–7 complete + Epic 8 pending · 94 canonical notes, ~130 files read · Audit basis: full-vault read, six domain deep-reviews, mechanical link/front-matter scans, Daggerheart SRD cross-checks. **This report is advisory; no canon was altered in its preparation.**

## Contents

1. [The editor's letter (my true feelings)](#1--the-editors-letter)
2. [Scorecard by domain](#2--scorecard-by-domain)
3. [What is genuinely excellent — protect it](#3--what-is-genuinely-excellent--protect-it)
4. [The five systemic problems](#4--the-five-systemic-problems)
5. [Concrete canon bugs (checkable, fix-now)](#5--concrete-canon-bugs--checkable-fix-now)
6. [What just does not make sense](#6--what-just-does-not-make-sense)
7. [Domain-by-domain findings](#7--domain-by-domain-findings)
8. [Direction: where this is going, where it should go](#8--direction--where-this-is-going-and-where-it-should-go)
9. [The prioritized work plan](#9--the-prioritized-work-plan)

---

## 1 · The editor's letter

**The short version: this is top-percentile worldbuilding that is in danger of becoming a beautifully written essay about a world instead of a world people play in.**

I want to be precise about both halves of that sentence, because you asked for my true feelings.

**The half you should feel great about.** The design spine is genuinely excellent — not "good for homebrew," excellent by the standard of published settings. The two-layer Kind/Condition model, the Given/Struck/Kept engine, the Tithe as both a personal cost and the economy's engine, the reach-gradient map, the two-clock history, and the bounded-benevolence keystone are each individually strong ideas, and — rarer — they all point at each other. The internal discipline is extraordinary: the Roadmap is honest (117 checkboxes verified against reality, all true), there are effectively *zero* broken wikilinks across 4,290 of them, the world book is current, and the "a Tithe never seizes the PC" rule is actually enforced on every card. The freshness mandate is delivered: the Long-Lived's blood-drop memory-reading and threshold courtesy, the Stilled's Grey clock, the split household of the Walking Years, the cup on the ford-rock — this is the real thing.

**The half that needs saying plainly.** The vault has been optimizing for design coherence for seven epics, and the costs of that are now visible everywhere at once. Every faith, guild, fable, and settlement is written in the same aphoristic voice, on the same template, to the point where the world's supposed plurality reads as one author's grid. The naming system has out-coined its own phoneme budget — `Eolvaeth / Eolstrand / Eoloren / Eolthael` all coexist and nearly every note now needs a "Not X, not Y" disclaimer paragraph, which is the system confessing failure. There are almost no people: across ~20 society and faction notes I can find *two* named characters, and every named NPC in the settlement layer is the same figure (a warden/clerk with one document and one blindness). There are no antagonists, no dangers, no adversary a GM can roll, and inter-faction conflict has been explicitly legislated away ("Do not let them"). And the process scaffolding — story numbers, seeds, canon emoji, "do not clone" imperatives — has leaked so thoroughly into player-facing canon that the setting text reads like its own change log in places.

**The one-sentence prescription.** Stop building grammar; start building people, procedure, and permission to fight — Epic 8 is exactly the right next epic, but it should be widened from "a cast" into "a cast, an opposition, a dangers layer, and a table-procedures note," and a naming deconfliction pass should happen before any more coinages are locked.

---

## 2 · Scorecard by domain

| Domain | Grade | One-line verdict |
|---|:---:|---|
| Core premise & engine (Premise, Tree, Given/Struck/Kept) | **A** | Locked, load-bearing, fresh. The best thing here. Two arithmetic bugs to fix. |
| Condition mechanics (the 10 cards) | **A−** | Well above typical homebrew; fiction-to-mechanics translation often superb. Two rules-keyword misuses, one overtuned card, and the connective tissue (creation, Kept, Struck-in-play) is missing. |
| Custom Kinds (4 ancestries) | **B** | Distinct fictional lanes, real culture — but 3-feature kits are acknowledged power creep over the SRD's 2, rationalized rather than resolved. |
| Religion & the five faiths | **A−** | Doctrinally genuinely plural, schism playable — but one narrator voice, zero dread inside religion, and the Tree's ceremony has no edge-case procedure. |
| Secrets architecture | **B−** | The bounded keystone is great design; the reveal is built never to fire, the `reveals:` tag has decayed into noise, and the truth leaks into player text in ~13 places. |
| Society & economy (Epic 2) | **A−** | The strongest structural thinking in the vault; two load-bearing numeric claims are false as written; procedure (crime, travelers, big cities) missing. |
| Factions & guilds (Epic 5) | **B** | Conceptually well-separated, presentationally identical; too harmonious to drive a campaign; two notes are jurisdiction sketches wearing faction clothes. |
| History (Epic 6) | **A−** | Two-clock model is the best history design here; but 387 years contain zero non-Tree events, so the world doesn't feel like it pre-exists the premise. |
| Geography & the 15 powers (Epics 3, 7.1) | **B−** | Brilliant diagram, not yet a place: no named rivers/seas, no distances, canon citing its own map-tooling; the 12 stubs are real designs trapped in a name-blur. |
| Settlements (Epics 7.2–7.3) | **A−** | The strongest ground-level layer; genuinely runnable — but one-NPC-one-conflict formula is exposed by the seventh note. |
| Language & naming | **B−** | Best-idea architecture (drift reveals stance), sloppy execution: the phonology contradicts its own rules and the namespace is exhausted. |
| Vault hygiene & trackers | **A−** | Near-perfect links and front-matter; Build Plan is stale and self-contradictory; a handful of schema drift items. |
| **Playability at the table, today** | **C+** | The honest grade. Superb physics, no cast, no opposition, no adversaries, no procedures, actionable material buried at the bottom of stylized notes. |

---

## 3 · What is genuinely excellent — protect it

Before the criticism: these are the load-bearing successes. In the refinement work ahead, **none of these should be touched except to fix arithmetic**.

- **The engine itself.** Given at the Tree / Struck at a threshold / Kept and wanted — with the sorting rule (innate fates are Given-only; things a ten-year-old can't have done are Struck-only; survivable doors are Both). This is clean, teachable in one minute, and generative.
- **The bounded keystone.** "She is real and benevolent" alone would deflate the schism; "she is real, benevolent, *bounded, and giving costs her*" keeps every faith half-right. The single best sentence of GM truth in the vault: *"some Kept are chosen for wholeness, and some are simply past her reach… She does not tell them apart for us, and neither can they."*
- **Fiction-to-mechanics translation on the Condition cards.** The Stilled's filling Grey clock ("the stillness has to come from somewhere"), the Two-Bodied's Fear-triggered involuntary shift (zero bookkeeping, rides the duality dice), the Long-Lived's blood-drop memory read, the Unbound's Absence-as-immunity. This is the craft the whole premise promised.
- **The self-paying vs. provided-for Tithe spectrum** ([[Economy and the Tithe]]) — a character-generation engine and a politics in one idea, and the reason "whoever furnishes the Tithe holds power" works.
- **The axis-isolation of the three polities** ([[Polity Archetypes]]): each pair shares exactly one axis, so the design *proves* the axes independent rather than asserting it. The three injustices are mechanized, not asserted.
- **The two-clock history** — "how you Turned" vs. "where the wood has reached" — avoids the stacked-ages cliché, keeps Heskoren present-tense, and "dating reveals stance" is a lovely lever. The spread-band math (a generation per hop) is genuinely well-engineered.
- **The Walking Years as lived history**: the one-week door, the split household ("The one who walked might come home Given. The ones who stayed were Kept… and grew up in the same kitchen"), Thilim's slate, mile-shrines as grave-and-waymark.
- **The colour→Condition palette table** in [[Turning Tree]] — the single best GM-facing artifact in the vault; the Phoenix row ("A warden who names it at a ceremony has just made history (and a problem)") is a whole adventure in one cell.
- **The best small texture:** the cup on the ford-rock at the Three Hamlets; Seine's held bed at the Third Hearth; the withheld blessing of the Watching ("What falls, was seen. What is kept, was seen."); the Bound contract-preamble ("If a mother had wanted me she would have sent a leaf, not a clause. I prefer the clause. I can read it."); the skeptic's ending of the Four Doors fable ("There were not four doors. There was a child, and a year, and a town that needed a story.").
- **Vault mechanics.** 94/94 content notes carry correct front-matter; 3 broken links out of 4,290 (all illustrative); Roadmap tallies verified true; the world book is current through Epic 7. This discipline is rare and worth preserving.

---

## 4 · The five systemic problems

Every domain review, run independently, converged on the same five walls. These are not note-level bugs; they are properties of how the last seven epics were built, and they need deliberate, cross-cutting passes rather than spot fixes.

### 4.1 · One author, one voice 🔴 SYSTEMIC

The world's plurality is doctrinally real and stylistically fake. Every faith note has the identical skeleton and exactly one two-branch schism; every guild "thinks they are in an X story," has "no pope," and ends its slate with a variation of "we do not know a pot"; all four fables share identical narrative furniture *verbatim* ("the tellings do not agree, and it does not change the ___"; the Long-Lived who "will tell you the child's name… not which summer"; "Kumbaan does not keep this story"). Four supposedly independent folk stories from different eras do not share machinery unless one author wrote them — which is exactly the impression a folk corpus must never give. The settlements repeat "cannot afford to see" and "both are telling the truth they have" in nearly every note; Eolvaeth and Ornsael are structural near-clones (spring/well, maybe-Tree, far shed downwind, warden who won't call a false fall, one inscrutable token).

**Refinement:** a deliberate asymmetry pass. Make one faith sprawling and contradictory and one barely articulate; give one guild a boring note and another a paranoid one; de-clone two of the four fables (demote [[The Child Who Climbed the Stone]] — its paradox is thin and it's unintelligible without the history behind it); break the settlement template in Eolvaeth *or* Ornsael. Cap each recurring mantra ("R2," "both are telling the truth they have") to one authoritative location.

### 4.2 · The name-collision crisis 🔴 SYSTEMIC

"How a name sounds reveals its stance" is the best idea in the culture layer, and it has been driven past the phoneme budget that could support it. The two-root compound space is exhausted. Confusion clusters, spanning *different categories of thing* (a player must distinguish a polity from a month from an era from a guild by one syllable):

| Cluster | Members (category) |
|---|---|
| `eol-` | Eolstrand (power) · Eolvaeth (capital) · Eolthael (month) · Eoloren (the First Cut era) |
| `sael-` | Saelthael (power) · Saelvaeth (power) · Saelhael (guild liturgy) · Saelorn (month) · Ornsael (town) |
| `vael / vaeth` | Vaethorn · Vaelhesk · Vaeloren (faith) · Vaelbren (clergy) · Vaelun (hamlet) · Vaethledd (shadow house) · Maiethvael · Leddvael · Thaelvaeth · Brenvaeth — "vayl" vs "vayth" differ by one final fricative when spoken |
| `-oren` | Thaeloren (the Tree!) · Vaeloren (faith) · Leddoren (faith) · Eoloren (era) · Aeloren (guild) · Nethoren (clergy) · Orenhael · Orenbren (power) · Orentel (capital) · Heskoren & Strandoren (continents) |
| `bren-` | Brenvaeth (era) · Brenorn (month) · brenhael (inn) · Brenthael (town) · Brenledd (power) · Brenod (hamlet) |
| `maieth- / thren-` | Maiethren (language) · Maiethorn (continent) · Maiethvael · Maiethlir · Threnmaieth · Trenledd · Threnhael (census) |

The tell that the system knows it has failed: nearly every coinage already ships with a defensive disambiguation paragraph — [[Maiethlir]] needs **seven** "Not X" lines; [[Saelthael]] opens by explaining it is "Not *Saelorn* (a month). Not *Saelhael* (greens-keepers' liturgy)."

**Refinement:** (1) Promote the epithets — "the Worn Count," "the Night Shore," "the Far Yield" are instantly memorable and already exist; make them the primary handles in body text and tables, with Old-Tongue forms kept as the liturgy they are. (2) Adopt one table rule: *speak the common-tongue name; write the liturgical one.* (3) Retire or respell the worst offenders — `Aeloren` beside Vaeloren/Leddoren/Eoloren is indefensible; `Eolstrand` is the top rename candidate among powers. (4) Freeze new liturgical coinage until the phonology is repaired (see §5) or new roots are added.

### 4.3 · A world of systems, not people 🔴 SYSTEMIC

Across roughly twenty society and faction notes there are **two named characters**, both inside in-world documents. The polities have injustices but no ministers; the guilds have jurisdictions but no masters; Orentel is a city of tens of thousands with one named living resident. Every named NPC in the settlement layer is the same figure — a warden or clerk with one document and one blindness. Nobody in the entire canon wants money, love, revenge, or power for a non-Tree reason. The three polity injustices are *weather, not actors*: none of them can knock on the party's door until someone incarnates them.

Worse, opposition has been engineered out on purpose. The Slide — the closest thing to a criminal organization — is *locked* as "will not push someone over the scary edge on purpose." The setting's two nastiest practices — the Given-Over pipeline (personhood absorbed by a creditor) and sold vouching — are explicitly denied a lived face in [[Economy and the Tithe]] ("No lived face — do not give this trade to the Slide"). Inter-faction tables repeatedly rule "Almost no contact," "None that matters," and — the anti-model — "They would not agree if a campaign sat them down. *Do not let them.*" Peace has been legislated. A Daggerheart campaign has nothing to push against.

**Refinement:** this is Epic 8, correctly sequenced and needing widening. (1) The planned 4–6 positional pivots, yes. (2) Give the Given-Over pipeline a lived face — it is the setting's sharpest wound and currently faceless by decree. (3) Give Threnmaieth 3–4 named instruments (a registrar, a Reckoned Speaker, a channel-clerk) — antagonists can stay good-faith and still have names and agendas. (4) Unlock two or three inter-faction disputes and let them escalate (the contested grove is the model). (5) Give each capital 3–5 named wants beyond the Tree-question.

### 4.4 · The world before and beyond the premise doesn't exist 🟡 SYSTEMIC

Every event in 387 counted years is about the Trees. No war, no dynasty, no plague, no named battle, no ruler anywhere in `02 - History`; fifteen great powers with zero inter-power history — no treaty, no border dispute, no succession crisis. The History MOC promises "the archaeology the culture is obsessed with"; nothing delivers any. Physically, three continents contain *no named river* (in a setting that runs on thaw-rivers and fords), no named sea, no stated distance between any two places — and two continent notes literally cite the Azgaar map template as the source of their own terrain, which is canon deferring to its render pipeline. There are zero creatures, adversaries, or environmental dangers: Heskoren's "un-polity'd wild" is filled with nothing; the Two-Bodied "range" against nothing; the only adventure verbs currently supported are witness, vouch, walk, wait, and audit.

**Refinement:** (1) Three to five dated non-Tree events inside C.Y. 0–387 (one war between named powers, a dynasty's end, a plague, a disaster) plus two or three pre-Walk physical survivals — a ruin, a wall against a forgotten enemy, an over-built Watching site (which would serve the keystone *and* give parties somewhere to go). (2) Name the inner sea, the central range, three or four rivers; add a small travel-time table built from the walk-durations that already exist in [[The Walking Years]]. (3) A dangers layer keyed to Daggerheart adversaries — what lives on the Long Mile and in Heskoren's wild. The ~5% scary dial is currently entirely sociological; it needs teeth an adversary roll can express.

### 4.5 · Scaffolding leaking into canon 🟡 SYSTEMIC

Player-facing notes are carrying the build process on their surface: canon-status emoji, RNG seeds ("Seed `20260829`, middle of the list"), Roadmap story numbers, and dozens of "Do not clone / Do not rebuild" imperatives sit in the public bodies of nearly every Epic 5–7 note. Beyond style, there are **real spoiler leaks**: the keystone truth appears in the body text (outside the strippable `## GM Notes` wall) of [[Turning Tree]] (twice — including a "GM — why this matters" blockquote that a heading-based strip cannot catch) and [[The Leaf-Mother]] (a design-note blockquote stating "she is real, present, and kind" in plain text); eleven faction notes carry a keystone-presupposing "Confirming she is real does not…" paragraph in their public injustice sections. Meanwhile the revelation architecture has decayed: `reveals: [leaf-mother-is-real]` now sits on 60+ notes (a filter matching everything filters nothing), the `the-other-hands` tag is keyed to *zero* of the eight player notes that reference it, and [[Is the Leaf-Mother Real]] still says `foreshadowed_by: []` despite six texts written specifically as foreshadowing.

**Refinement:** (1) Move the ~13 leaking passages under `## GM Notes` and write the exact strip rule into Conventions. (2) Split the over-applied tag (keep `leaf-mother-is-real` only where confirmation would actually leak; a lighter `keystone-adjacent` elsewhere); key `the-other-hands` to the eight notes that expose it; populate `foreshadowed_by`. (3) A style pass moving seeds, story numbers, emoji, and "do not clone" apparatus into GM Notes — the world book already proves the clean register is achievable.

---

## 5 · Concrete canon bugs — checkable, fix-now

These are not matters of taste. Each is verifiable against the vault's own text.

| Severity | Bug | Where / detail |
|:---:|---|---|
| 🔴 HIGH | **The population math cannot reconcile.** | The locked split is ~60% Given · ~15% Struck · ~25% Kept. But the Struck-only Conditions alone (Returned 9 + Bound 5 + Unbound 1.5) total 15.5% *before counting a single Struck member* of the three Both-path Conditions (jointly ~30%). The roster also sums to ~76% + 25% Kept ≈ 101%. Fix: shave Returned to ~7%, publish Given/Struck sub-splits for the Both-path three, and rule whether the Unbound 1.5% is inside or additional to Bound's 5% (The Premise implies subset; the tables imply parallel). |
| 🔴 HIGH | **The licence-math rhetoric is false.** | [[Law and Citizenship]] claims "the great majority of the Conditioned carry nothing at all" (audit guide: "~90% carry nothing"), but licensed Conditions (Stilled 7 + Far-Voiced 11 + Answered 10, + Bound oversight 5) are ~28–33% of the population ≈ 40–44% of the Conditioned. Either the percentages or the rhetoric must move — and it's load-bearing for the "not a surveillance state" tone claim. |
| 🔴 HIGH | **Restrained is misused on The Stilled.** | [[The Stilled]] uses the SRD keyword to mean full action denial ("they cannot act until they mark a Stress"); SRD Restrained = can't move, *can* act. Combined with no roll and no Hope cost, the Gaze is the strongest and cheapest combat effect in the roster. Rename the effect (you already coined "Stilled") and gate it behind a roll or cost. |
| 🔴 HIGH | **The Returned silently drops Avoid Death.** | [[Returned]] lists Blaze of Glory and Risk It All as the remaining options; the SRD has three death moves. If the Returned keeps Avoid Death, its signature Refuse-to-Fall is dominated by a core rule. Removing the *safest* option is the right design — say it out loud. |
| 🟡 MED | **Ledan's query is mis-dated by a century.** | [[The Ages of the Turning]] headers it "Cut-year 387," but its internal arithmetic ("our founding-summer, the 200th of the White Note… your college will write it as the 280th Cut-year") places it at C.Y. 280 — confirmed by [[The White Note House]] (founding ≈ C.Y. 80). At C.Y. 387 the house is in its ~307th summer, which also breaks the "200th summer" idiom quoted as current in [[The Reckoning of the Year]]. Cleanest fix: re-date the query to C.Y. 280 as an archival document. |
| 🟡 MED | **The Kumbaan graft contradiction.** | [[The World Frame]] allows "the grafts never reached across the storm-wall, *or never took when they did*"; [[The First Cut]] is absolute ("never. Dead wood is not a Tree"). Pick the strict version and align the frame. |
| 🟡 MED | **Build Plan contradicts itself and the vault.** | [[Build Plan]] line 19 says "full 9-Condition roster" and "all 3 custom ancestries LOCKED" in the same paragraph that later says "four ancestries, not three"; line 29's roster table omits The Unbound; the "STATUS (2026-08-19)" header caps a paragraph running to 08-24 that has grown to ~1,300 words — the "fast brief" now defeats its purpose. Also: `aliases: [Roadmap]` on Build Plan makes every `[[Roadmap]]` link in the vault ambiguous. Remove the alias. |
| 🟡 MED | **Stale cross-references in the Kinds.** | [[Selkie]] says "Tengu stays lean at two [features]" while [[Tengu]] locks three; [[Tengu]] says "a world of three custom Kinds" (it's four); Fox of the Sands is epitheted "the many-tailed fox" while [[Kitsune]] insists nine-tails is reputation, not biology. |
| 🟡 MED | **The phonology contradicts its own rules.** | [[The Old Tongue]]: "no harsh consonant clusters" vs. its own roots `thren, stel, crae, hesk, strand` (and `strand` isn't even in the root table despite Lestrand being glossed from it); the vowel inventory (a e i o u + ae ei eo) doesn't license `ai` — i.e. the setting's most important word, *maieth*; the second-syllable stress rule is broken by half the coinages; the Worn-drift example ("Vaethorn → Wethorn") illustrates *th*-softening with a form that keeps the th. Two sample names violate the pronunciation key (`Maethaem` glossed "MY-eth-aym" though ae="ay"; `Reimaethe` "ray-" though ei="eye"). License the real clusters, add the digraph, restate stress as compound-initial, fix the samples. |
| ⚪ LOW | **Rest ambiguity on four Tithe clocks.** | Long-Lived, Answered, Taken-In, Stilled drain "each rest" — short or long? [[Returned]] correctly says "long rest." Standardize; a double-short-rest day currently drains clocks at double speed. |
| ⚪ LOW | **Schema drift.** | 19 notes use `note_status: locked`, which isn't in Conventions' vocabulary (stub\|draft\|fleshed\|canon) — a query for finished notes misses the most-finished notes. All 10 Condition cards + hub are `visibility: gm`, so a player-safe export strips the player-facing mechanics. The `09 - Creatures` MOC is an empty shell above 12 notes. [[Rogue House Options]] is `status: superseded` but not archived. "Fourteen-cell catalogue" in [[Polity Archetypes]] is opaque (3 axes = 8 corners; 15 powers); fix or cut. |
| ⚪ LOW | **Unreproducible seeds.** | Multiple notes instruct "re-run from the seed" (`20260823/27/28/29`) but no generator script or algorithm is stored anywhere — the seeds are decoration. Store the generator or delete the language. |

---

## 6 · What just does not make sense

You asked specifically for the things that don't hold together. Beyond the bugs above, these are claims and structures that fail on their own terms:

1. **"Tithe-provision is as large and load-bearing as food or fuel."** By the note's own roster, the purchased-provision sector serves maybe 15% of people, mostly with dirt, books, and company; ~35% of the population self-pays by vocation. It's a real sector; it is not food. Soften the claim or show the volume that earns it.
2. **Cities cannot witness.** Witnessed-not-recorded citizenship works for a village of 300. A Lestrand port of 20,000 with hundreds of ten-year-olds per solstice at one Tree has no described mechanism — and "living communal memory" does not scale past Dunbar's number. This is the biggest hole in the legal grammar, and it's structural, not cosmetic.
3. **Adventurers are the unvouched.** The law layer establishes that the rootless are the truly vulnerable, then never says what a legitimate traveler does — no vouching-letter custom, no road-law, nothing. PCs are travelers by definition; as written, a rules-literal GM hassles the party in every town or ignores the system.
4. **The keystone reveal is designed never to fire.** All six clue rungs are explicitly deniable and rung 6 is "reserve this." There is no confirmable artifact, no faction that would kill to prove or suppress it, no consequence specified if it landed. A secret with no path to mattering is a theme, not a secret.
5. **The Other Hands have no wants.** Each is defined negatively ("Not Hades." "Not a devil.") and "allowance" has no failure mode. Most practically: when a Bound PC's petition is answered, nothing anywhere says *what Orledd gets from the deal* — without a motive, the Counterparty defaults at the table to exactly the devil the note forbids.
6. **The urban Taken-In circularity.** Tithe-poverty's flagship case is green as an expense in stone cities — but the same note says cities keep the Taken-In at arm's length and they thrive on the frontier. Why are they in the city? The Slide's customer base quietly depends on a population the economy note explains away.
7. **The Kept have no deal, mechanically.** ~25% of people — and any player who wants one — get nothing where others get a free transformation card, in a setting whose theology insists the Kept are "wanted in their own right." Either compensate Kept PCs (an Experience, a Hope slot, something) or state that it's a deliberate hard-mode pick. Related: nothing anywhere says when a PC takes a Condition card, what happens if a Kept PC walks through a Struck door mid-campaign, or how three-feature custom Kinds interact with the SRD's mixed-ancestry rules. These are the first three questions a real table asks.
8. **Canon citing its own tooling.** "The Azgaar template builds Heskoren as the large, mountainous far-continent" — a canonical geography note sourcing its terrain from the map-generator config is backwards; over half of [[The World Frame]] is version-fragile build tooling sitting inside a `visibility: player` note. It belongs in `14 - Assets` with a link back.
9. **Three of four custom Kinds have "cannot be caught off guard."** A rare hard immunity, issued three times, has become the house's accidental signature move — and it erodes exactly the distinctness the Kinds claim.
10. **Prestige-walk triple-booking.** The First-Hand-year-as-product is assigned to Netstrand, to Orentel, and to the White Note House in three different notes. Chain them (Netstrand berths → White Note terms → Orentel holds) or thin one.

---

## 7 · Domain-by-domain findings

### 7.1 · The Conditions (mechanics)

**Verdict: well above typical homebrew, with a short, specific errata list.** The design rule against control-seizure is genuinely enforced on all ten cards. The tuning spread:

- **Overtuned:** The Stilled (no-roll, no-Hope action denial with a pre-payable Tithe — see §5); Phoenix (fire immunity + true flight + a Faerie-grade Evasion feature + a Proficiency attack + a full-reset extra death move; honestly fenced as a table-consent spotlight pick, but with no guidance for the other four players); The Unbound (blanket mind-lane immunity *plus* three Quiet tokens that no-sell the same lane — cap the immunity to Stress-marking effects and differentiate it from the Returned's unshaken clause, which it currently duplicates).
- **Undertuned:** Long-Lived — the weakest boon paired with the harshest Tithe (global disadvantage at 1 token, an unclearable HP death-spiral at 0). Soften the fade to targeted disadvantage or strengthen the boon.
- **Well-tuned:** Far-Voiced, Bound, The Answered, Two-Bodied, Returned — though the Answered is the most generic card (four-element genasi territory; nothing mechanizes "spoken to, not commanded"), and Two-Bodied's natural weapon never states a damage die or trait.
- **Bookkeeping load:** six of ten cards run token pools; in a mixed party, rests become a checklist of fuzzy refill adjudications ("learn something genuinely new," "in earnest," "true contact with living land"). The best Tithes here are the ones with zero bookkeeping (Two-Bodied's Fear-triggered shift) — a model for future trims.
- **Missing entirely:** the procedural page — character-creation timing, the Kept deal, Struck-in-play acquisition, Kind+Condition stacking edge cases (Infernis + Bound is named in [[Bound]] and never resolved), and advancement (only Two-Bodied scales; every other card is identical at level 1 and 10).

### 7.2 · The Kinds and the language

**Verdict: clean fictional lanes, acknowledged power creep, exhausted namespace.** All four Kinds run three features against the SRD's two, several features are bundles (Kitsune is effectively four-to-five abilities; [[Kitsune]] itself admits Slip the Frame is "a notch above the SRD band… kept at full strength by choice"), and the notes record the drift: both Selkie and Tengu say "earlier lean was 'stay at two'; reversed on refinement." Refinement went one direction, four times, and the customs are balanced *against each other* rather than against the roster players actually choose from — which makes stock ancestries trap options. Either trim to two features per Kind or give stock-ancestry PCs a compensating hearth boon; and rule the mixed-ancestry interaction explicitly. Culturally the Kinds are real (the Selkie skin-intimacy reframe and the lost fourth Fox are the best paragraphs in the set), but pan-Kind culture has no transmission mechanism in a "hearths, not nations" world, and mixed-Kind children are unaddressed in a setting about layered identity. The language findings are consolidated in §4.2 and §5.

### 7.3 · Religion, the Tree, the secrets

**Verdict: the doctrines are genuinely plural; the procedure and the danger are missing.** The five faiths answer the same fact with five different verbs, and the schism is performable in one sentence — this layer works. But the Leaf-Fall has no edge-case procedure (the missed solstice, refusal, orphans, adults never Turned, whether the rite is once-only — the single most likely PC-backstory questions, all unanswered, and the GM truth about "past her reach *this turning*" makes the once-only question urgent). Religion itself contains zero dread — the notes enforce it — so the folder's own subject is the safest thing in the setting; the Phoenix fall and a historical mis-Speaking are the natural, floor-safe places to put one shadow. The Other Hands are integrated (the division-of-labour maps one-to-one onto the locked engine) but inert — defined negatively, no wants, no failure mode for "allowance." The Open Table is lovely and unplayable ("Almost no contact"); its one campaign-usable edge — the sentence that will not travel, colliding with citizenship-by-witness — is buried at the bottom of an order note. And the highest-value fix per word in the vault: a "Questions a warden gets asked" section in [[Turning Tree]] — ten edge cases, two sentences of in-world custom each.

### 7.4 · Society, economy, factions

**Verdict: the physics is finished and good; the people and the procedures are not.** The self-paying/provided-for spectrum, the deathless-banking reconciliation, and the seam-dweller precarity are the strongest structural thinking here. The gaps: the two numeric claims in §5; no crime-and-punishment ladder anywhere ("the watch" appears repeatedly and is never defined); the traveler problem; the big-city witnessing problem. The thirteen orders and guilds are conceptually well-separated — each owns one job and one injustice (the scion-queue is the layer's best institutional wound; the Slide's "they rent you not falling" is a complete villain-adjacent engine; the Intake's "success is silence" is a perfect underdog) — but presentationally identical, running 60–70 proper nouns for 13 organizations on one shared skeleton and one shared wry slate-voice. Greens-Keepers and Hall-Keepers are jurisdiction sketches, not factions — fold both into [[Tithe-Infrastructure]] and spend the recovered effort on named NPCs. Add a ten-line scannable header block (want / have / fear / live conflict / three hooks) atop every faction note; the stylized prose can stay below it.

### 7.5 · World, history, powers, settlements

**Verdict: a brilliant diagram over an unnamed planet; ground-level texture the vault's best.** The reach-gradient and two-clock designs are excellent and internally consistent to a degree most published settings never reach (spread bands, dates, and placements verified consistent everywhere but the two bugs in §5). What's missing is everything that isn't the system: named terrain, distances, non-Tree history, physical danger (§4.4). Among the twelve power stubs: Trenledd ("a census with the halo worn off… they agree, and list you anyway"), Ornled ("The loneliest unvouched in the world are… next door, where no one is waiting with them"), Leddvael, Vaelhesk, and Maiethvael earn their slots; Eolstrand is Lestrand-lite, Lirorn is a watershed with a toll, Netstrand's one mystery is a placeholder wearing an inscrutability badge. The settlements are the strongest layer — the Three Hamlets ("the cluster is a complaint with three kitchens," and the cup on the ford-rock is the best small mystery in the vault) and the Third Hearth lead; the White Note House is still a draft ledger of cross-references; Eolvaeth/Ornsael expose the shared template. Kumbaan justifies itself structurally as the keystone's control group and is otherwise a well-designed appendix — everything about it is a reveal being guarded, nothing is a session being offered. Commit (one settlement, one Table-Keeper, crossing rules) or explicitly gate it in the Roadmap so the appendix status is a decision.

### 7.6 · Vault hygiene, trackers, world book

**Verdict: unusually healthy; the fixes are small and enumerable.** 94/94 content notes carry correct front-matter; 3 broken links in 4,290 (all illustrative examples); the Roadmap's 117 checked boxes all verify; the world book is current through Epic 7 (rebuilt in the two most recent commits), with its only gaps mirroring genuine vault gaps. The fix list: rewrite Build Plan's stale status paragraph (§5); remove the Roadmap alias; resolve `locked` vs `canon` in the note_status vocabulary (19 notes); decide the Conditions-folder `visibility: gm` question deliberately; fill the empty `09 - Creatures` MOC; archive [[Rogue House Options]]; and make [[The Premise]] the single canonical statement of the population math, which is currently duplicated in 8+ places (all copies agree today; they will not forever).

---

## 8 · Direction — where this is going, and where it should go

**Where it's going.** The trajectory of Epics 0–7 has been: lock a mechanism, derive its social physics, name it, then armor it with negative guidance so later work can't break it. That method produced the coherence that makes this setting special — and it has diminishing returns from here, because the remaining absences (people, opposition, danger, procedure) are precisely the things that method doesn't produce. The vault's own next step (Epic 8, positional pivots) is correctly aimed; the risk is doing Epic 8 *in the established mode* — six more beautifully-voiced office-holders, each with one document and one blindness, each armored with "do not clone" — and arriving at pass-two with a world that still has no one to fight, nowhere dangerous to go, and no procedure for the first hour of play.

**Where it should go — my recommendation as your editor, in order:**

1. **Errata pass first (small, sharp):** the §5 bug list. Population math, licence math, Restrained/Avoid Death, the Ledan date, the Kumbaan wobble, Build Plan, phonology-vs-practice, stale Kind cross-references. None of this is creative work; all of it is credibility work. Do it before pass-two so the audit trail stays clean.
2. **The playability quartet (this is the real Epic 8, widened):**
   - *People* — the planned pivots, plus 3–5 named wants per capital, plus faces for the Given-Over pipeline and Threnmaieth's instruments;
   - *Procedure* — one "At the Table" note: character-creation timing, the Kept deal, Struck-in-play, travelers' vouching custom, the crime ladder, big-city witnessing, and the Leaf-Fall edge cases;
   - *Danger* — a small adversaries/hazards layer keyed to Daggerheart's adversary system, plus 2–3 adventure sites (pre-Walk ruins serve the keystone twice over);
   - *Permission to fight* — unlock two or three inter-faction disputes and let one escalate on-screen.
3. **The deconfliction-and-voice pass:** promote epithets to primary handles, retire the worst homophones, freeze new coinage, break the templates (one faith, one guild, one fable, one settlement each rebuilt asymmetrically), move scaffolding into GM Notes, and repair the reveals architecture. This is the pass that makes the world read as plural.
4. **Then pass-two verification** as planned — it will be auditing a world that can actually be played, rather than certifying a beautiful diagram.

**And what I would *not* do:** don't rebuild anything locked (the locks are good locks); don't add more powers, faiths, guilds, or liturgical names — the namespace and the reader are both full; don't write more universal grammar — every grammar the setting needs now exists; and don't soften the injustices in response to this audit — the R2 discipline (her benevolence is cosmological, not social) is one of the best decisions in the vault and the darkest material here is its best material.

---

## 9 · The prioritized work plan

| Priority | Work item | Scope / touches |
|:---:|---|---|
| 🔴 P0 | Errata: population & licence math; Unbound-inside-Bound ruling; Given/Struck sub-splits for the Both three | [[The Premise]], [[Conditions]], [[Law and Citizenship]], [[Economy and the Tithe]], Build Plan, book chs. 01–03 (on next explicit rebuild) |
| 🔴 P0 | Errata: The Stilled's Gaze (rename off Restrained + add roll/cost); Returned's Avoid Death ruling; standardize "long rest"; Two-Bodied weapon statline | 4 files in `09 - Creatures/Conditions/` |
| 🔴 P0 | Spoiler-leak repair: move ~13 keystone passages under GM Notes; write the strip rule into Conventions; fix `reveals:` for the-other-hands (8 notes); split the over-applied keystone tag | [[Turning Tree]], [[The Leaf-Mother]], 11 faction notes, [[Conventions]], Secrets MOC |
| 🔴 P0 | Tracker & schema: rewrite Build Plan status; drop its Roadmap alias; `locked`→schema decision; Conditions visibility decision; fill 09-MOC; archive Rogue House Options; fix Ledan date + Kumbaan wobble + Selkie/Tengu stale lines | [[Build Plan]], [[Conventions]], ~25 front-matter touches, 5 content fixes |
| 🟡 P1 | "At the Table" procedural note: creation timing, the Kept deal, Struck-in-play, stacking, travelers' vouching, crime ladder, city witnessing, Leaf-Fall edge cases ("Questions a warden gets asked") | 1–2 new notes (`13 - Game` + a Turning Tree section); the highest table-value item in this plan |
| 🟡 P1 | Epic 8 widened: pivots + capital casts (3–5 wants each) + faces for the Given-Over pipeline and Threnmaieth's instruments + 2–3 unlocked inter-faction disputes | `08 - People` (new), touches to 3 capitals + 3 faction notes |
| 🟡 P1 | Dangers layer: wilderness adversaries keyed to Daggerheart, 2–3 adventure sites / pre-Walk ruins; 3–5 dated non-Tree historical events | `09 - Creatures` (new section), `02 - History` additions, continent touches |
| 🟡 P1 | Kind power-band resolution: trim to two features or add a stock-ancestry hearth boon; mixed-ancestry ruling; consolidate "cannot be caught off guard" to one keyword issued once | 4 Kind notes + a short design ruling |
| 🔵 P2 | Naming deconfliction: epithets as primary handles; retire/respell worst homophones (Aeloren, Eolstrand first); phonology repair; "speak common, write liturgical" table rule; coinage freeze | [[The Old Tongue]], [[Powers of the Turning]] + stub touches |
| 🔵 P2 | Voice & asymmetry pass: de-clone two fables; break one faith / one guild / one settlement template; scannable header blocks on faction notes; mantras capped to one home; scaffolding into GM Notes | Broad but mechanical; no canon changes |
| 🔵 P2 | Geography grounding: name the inner sea, the range, 3–4 rivers; travel-time table; extract map tooling to `14 - Assets`; keystone firing-pin (one confirmable artifact + consequences paragraph); animate the Other Hands (wants, one strain on "allowance") | [[The World Frame]] + continents, [[Is the Leaf-Mother Real]], [[The Other Hands]] |
| ⚪ P3 | Polish: fold Greens/Hall-Keepers into Tithe-Infrastructure; Kumbaan commit-or-gate decision; dedupe the prestige-walk product; store the name-generator or delete seed language; one point of dread inside religion (the Phoenix fall) | Assorted, low-risk |

When this plan is done, run pass-two as the Roadmap already intends. My honest expectation: after the P0–P1 work, this stops being an exceptionally well-designed document and becomes an exceptionally well-designed *game* — and it is much closer to that than most projects ever get.

---

*Sources: full read of the design hub and trackers; six independent domain deep-reviews (Conditions · Kinds/Language · Religion/Secrets · Society/Factions · World/History/Settlements · Hygiene/Book); mechanical scans of 4,290 wikilinks and 94 front-matter blocks; Daggerheart SRD cross-checks.*
