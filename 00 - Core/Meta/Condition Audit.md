---
title: Condition Audit
type: reference
visibility: gm
note_status: draft
status: active
tags: [meta, audit, condition, balance, review]
aliases: [Conditions Audit, Condition Balance Pass]
created: 2026-08-19
updated: 2026-08-19
---

# Condition Audit

> **What this is.** A design/balance review of all ten Conditions (see [[Conditions]]), run 2026-08-19 before building society on top of them. Findings are triaged **Tier 1** (fix before building forward), **Tier 2** (cheap consistency cleanup), **Tier 3** (taste-forks). Tiers 1, 2, and 3 are **resolved** (2026-08-19) — with a single item, **#12 (flight density), deliberately left open** for a later rework pass. Track resolution here as a running list (the pass-two convention from [[Roadmap]]).

## Verdict in one line

The Conditions are strong — the anti-fun traps are genuinely avoided and no Tithe seizes PC control. The problems are mostly **relative** (cards not power-normalized against each other) and a few **internal inconsistencies** that get expensive once law/guilds/settlements encode assumptions about them.

---

## Tier 1 — Real issues ✅ RESOLVED (2026-08-19)

- [x] **#4 — 9-vs-10 count contradiction.** [[The Premise]] said "9 total", [[Conditions]] said "roster (10)". **Resolved:** canon is **9 selectable Conditions + [[The Unbound]] as the downstream 10th** (reachable only through [[Bound]]). Both notes reworded to the "9 selectable + 1 downstream" framing.
- [x] **Rename — The Hollow → [[The Unbound]].** Title now names the *release* (contract over → unbound); **"the Hollow" kept as the in-world colloquial nickname** (alias + prose). File renamed; all links in [[Bound]] and [[Conditions]] updated.
- [x] **#3 — [[Returned]] had the strongest anti-death kit in the game.** Free negation of a failed death move **plus** a guaranteed 1/arc auto-success. **Resolved:** cut *Refuse the Rest* entirely; reworked *Unfinished Business* into **Refuse to Fall** — a 4th death-move option that costs a **scar (a Hope slot) every time**, with the **last slot = true death**. Now finite, costly, and death-move tension is intact. (Also trimmed the card from 3 features to a clean boon + Tithe.)
- [x] **#2 — [[Two-Bodied]] (18%, commonest) was thinnest & weakest, esp. in combat; animal choice unbounded.** **Resolved:** shift is now **free/at-will** (Stress was discouraging the core fantasy; the Tithe already supplies the downside); boon gains a **natural weapon** (combat legibility) + a **signature capability** alongside the Experience; added an explicit **size/capability band** (housecat-to-bear; no true flight/water-breathing/giant-reach) with lane-lines vs. [[Tengu]], Ribbet, [[The Answered]].

---

## Tier 2 — Consistency & polish ✅ RESOLVED (2026-08-19)

- [x] **[[Phoenix]] — *Rise From Ash* and *The Dwindling* overlap.** **Resolved:** kept both features (every Condition must carry a labeled Tithe), but split their jobs cleanly — **Rise From Ash** now owns the rebirth + memory-loss (no longer restates the Hope-slot cost), and **The Dwindling** *(Tithe)* owns the cost-accounting (the crossed slot, the finite count, true death). Cross-referenced, no duplicated mechanic.
- [x] **Normalize feature *count* across the roster.** **Resolved as a deliberate non-change:** the count varies by design — spotlight/complex Conditions (Phoenix, Answered, Bound) legitimately carry more than the workhorse cards. What matters is that *each* card has a clean boon + labeled Tithe and no card is over/underpowered for its rarity; Tier-1 already leveled the outliers. The [[Conditions]] MOC line updated from "normalizing is tracked" to "count varies by design."
- [x] **Standardize the damage idiom.** **Resolved:** the one offender, [[The Taken-In]]'s entangle, changed from flat **1d8** to **Proficiency d6s** to match Ember/Kindle. A roster grep confirms no other flat-dice attacks remain.
- [x] **Attack-roll-first, per our own rule.** **Resolved:** [[The Taken-In]]'s entangle now leads with an **attack roll (Instinct or Strength)**; the Spellcast-first phrasing is gone. Grep confirms no "Spellcast" idiom remains on any card.
- [x] **The "3-token clock" Tithe rhythm.** The identical rest-drain chassis was really on 4 cards (Long-Lived, Answered, Taken-In, Stilled — Far-Voiced's Undertow is already scene-triggered). **Resolved by re-rhythming [[The Stilled]]:** *The Grey* is now a **filling** clock (0→3) that rises when you *use the Gaze* and settles into a seizure at full, rather than a passive drain — motivated directly by its fiction ("the stillness has to come from somewhere"). One distinct rhythm added; the remaining drain-clocks kept for teachability.
- [x] **Finish the Given-Over name.** **Resolved:** placeholder flag dropped in [[Bound]]. Settled as **the Given-Over** (plain name) with **the Forfeit** as the contract-guild term of art.
- [x] **`note_status`.** **Resolved:** flipped 9 Condition cards to `locked`; **[[Long-Lived]] left `draft`** pending its Tier-3 monster-legibility question (#11). ([[Conditions]] MOC stays `draft` as an index.)
- [x] **Hope-economy pressure.** **Resolved (targeted):** [[The Stilled]]'s Gaze moved **off Hope** — using it now feeds the Grey clock instead of spending Hope, which the re-rhythm made natural. Left the rest on Hope-cost as a deliberate throttle; revisit only with playtest data on which specific boons bite.

## Tier 3 — Taste-forks (RESOLVED 2026-08-19, except #12 flagged for rework)

- [x] **#11 — Is [[Long-Lived]] still recognizably a *vampire*?** **Resolved — re-attached two subtle tells** (user chose recognizable-but-fresh over the clean break): (1) **Blood-Read**, a usable card mechanic — a single drop of blood yields a *glimpse of memory* (blood-drinking reframed as memory-reading, non-predatory, no damage); (2) **the old courtesy**, passive story flavor — a Long-Lived never crosses a private threshold uninvited, held as deep manners, "the last shadow" of the cannot-enter-unbidden vampire. GM Notes guard both against being weaponized into "the vampire rules." Long-Lived flipped to **locked**.
- [x] **#10 — Phoenix fire immunity.** **Resolved — kept full immunity** (user's call): a Phoenix *is* fire; total immunity is on-myth, and as a trace spotlight-only Condition (<0.1%) it won't warp normal play. No card change; the long-open "resistance dial" is closed as decided.
- [x] **#8 — The demon complex is top-heavy.** **Resolved — confirmed intended.** One monster (demon) spanning three notes ([[Bound]], [[The Unbound]], the Given-Over) is a deliberate richness: the contract → release → forfeit arc is the setting's one fully-mapped moral spiral, and it earns the extra surface. Documented as a conscious choice, closed.
- [ ] **#12 — Flight appears 3× among Conditions** (avian [[Two-Bodied]], [[Bound]]'s granted power, [[Phoenix]]) + [[Tengu]] — **FLAGGED FOR REWORK (user's call).** Revisit whether flight is over-dense across the roster and whether some of these powers should be spread to other movement/senses. Left **open** on purpose; not blocking — resolve in a later pass (likely alongside the Bound granted-power list).

---

## Per-Condition quick reference (post-Tier-2)

| Condition | State after Tier 2 |
|---|---|
| [[Long-Lived]] | **Locked.** Added two vampiric tells — Blood-Read (memory-from-blood mechanic) + the threshold courtesy (flavor). |
| [[Two-Bodied]] | Locked. Tier-1 rework + post-audit refine: growth = Experiences (2nd capability is a once-ever milestone), real flight freed (lane vs. Tengu = no hands/mind), other self has a voice. |
| [[Returned]] | Locked. Refuse to Fall costs a scar, finite; Refuse the Rest cut. |
| [[Bound]] | Locked. Given-Over name settled (Forfeit = guild term); top-heavy demon complex (#8) is Tier-3. |
| [[The Unbound]] | Locked. Renamed from The Hollow; good temptation engine. |
| [[Far-Voiced]] | Locked. One of the best; its Undertow is already a distinct (scene-triggered) rhythm. |
| [[The Stilled]] | Locked. **Re-rhythmed:** Grey is now a *filling* clock fed by using the Gaze (also moved the Gaze off Hope). |
| [[The Answered]] | Locked. Most complex card; well-built; Ember is the combat default (mild). |
| [[The Taken-In]] | Locked. Fixed — entangle now attack-roll-first + Proficiency-d6s scaling. |
| [[Phoenix]] | Locked. Rise From Ash / Dwindling de-duplicated (Rise = rebirth+memory, Dwindling = the count). Fire-immunity→resistance still an open Tier-3 dial. |

## Links
- [[Conditions]] · [[The Premise]] · [[Build Plan]] · [[Roadmap]]
