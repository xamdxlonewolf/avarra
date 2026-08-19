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

> **What this is.** A design/balance review of all ten Conditions (see [[Conditions]]), run 2026-08-19 before building society on top of them. Findings are triaged **Tier 1** (fix before building forward), **Tier 2** (cheap consistency cleanup), **Tier 3** (taste-forks). Tier 1 is **done**; Tier 2/3 are open. Track resolution here as a running list (the pass-two convention from [[Roadmap]]).

## Verdict in one line

The Conditions are strong — the anti-fun traps are genuinely avoided and no Tithe seizes PC control. The problems are mostly **relative** (cards not power-normalized against each other) and a few **internal inconsistencies** that get expensive once law/guilds/settlements encode assumptions about them.

---

## Tier 1 — Real issues ✅ RESOLVED (2026-08-19)

- [x] **#4 — 9-vs-10 count contradiction.** [[The Premise]] said "9 total", [[Conditions]] said "roster (10)". **Resolved:** canon is **9 selectable Conditions + [[The Unbound]] as the downstream 10th** (reachable only through [[Bound]]). Both notes reworded to the "9 selectable + 1 downstream" framing.
- [x] **Rename — The Hollow → [[The Unbound]].** Title now names the *release* (contract over → unbound); **"the Hollow" kept as the in-world colloquial nickname** (alias + prose). File renamed; all links in [[Bound]] and [[Conditions]] updated.
- [x] **#3 — [[Returned]] had the strongest anti-death kit in the game.** Free negation of a failed death move **plus** a guaranteed 1/arc auto-success. **Resolved:** cut *Refuse the Rest* entirely; reworked *Unfinished Business* into **Refuse to Fall** — a 4th death-move option that costs a **scar (a Hope slot) every time**, with the **last slot = true death**. Now finite, costly, and death-move tension is intact. (Also trimmed the card from 3 features to a clean boon + Tithe.)
- [x] **#2 — [[Two-Bodied]] (18%, commonest) was thinnest & weakest, esp. in combat; animal choice unbounded.** **Resolved:** shift is now **free/at-will** (Stress was discouraging the core fantasy; the Tithe already supplies the downside); boon gains a **natural weapon** (combat legibility) + a **signature capability** alongside the Experience; added an explicit **size/capability band** (housecat-to-bear; no true flight/water-breathing/giant-reach) with lane-lines vs. [[Tengu]], Ribbet, [[The Answered]].

---

## Tier 2 — Consistency & polish (OPEN)

- [ ] **[[Phoenix]] — *Rise From Ash* and *The Dwindling* overlap.** *(Flagged by the user; my first pass mistakenly touched the boons instead — reverted, boons are fine as written.)* The two rebirth features restate the same mechanic: **Rise From Ash** already says "cross out a Hope slot (as a scar)," and **The Dwindling** just repeats "each Rise From Ash permanently crosses out a Hope slot," then adds the "last slot = true death" clause (which is already the base SRD scar rule). **The Dwindling is redundant as a standalone feature** — fold its finite-lives/true-death framing into Rise From Ash and drop the separate bullet, OR give The Dwindling a distinct mechanic if it should carry its own weight. Decide in the Tier-2 pass.
- [ ] **Normalize feature *count* across the roster.** Cards range from 2 clean features (Long-Lived, Far-Voiced, Stilled, now Two-Bodied/Returned) to loaded (Bound = 3, Phoenix = 4+, Answered = boon + per-element sub-table). Decide a target shape and trim/pad to it (the ancestries got this pass; the Conditions never did). *The [[Conditions]] "two features" line was softened to "features vary — normalizing is tracked here."*
- [ ] **Standardize the damage idiom.** Mixed: "Proficiency d6s" (Ember, Phoenix Kindle) vs. flat "1d8" (Taken-In entangle — doesn't scale, weak mid-game). Pick one.
- [ ] **Attack-roll-first, per our own rule.** [[The Taken-In]]'s entangle leads with a **Spellcast Roll** ("or attack roll if none"); flip to attack-roll-first to match Stilled/Ember/Phoenix and the captured design rule (Spellcast keys off a subclass trait a Condition can't assume).
- [ ] **The "3-token clock" Tithe is on 5 of 10** (Long-Lived, Far-Voiced, Stilled, Answered, Taken-In) — identical chassis. Fine for teachability, but consider giving 1–2 a different rhythm so Tithes feel distinct.
- [ ] **Finish the Given-Over name.** [[Bound]] still flags it "(Placeholder name.)" while also offering "the Forfeit" — pick one term.
- [ ] **`note_status`.** All ten Condition notes are still `draft` though Build Plan/MOC call the mechanics "locked." Flip to `locked` (or agreed status) once this audit's changes settle.
- [ ] **Hope-economy pressure.** 6+ boons cost "spend a Hope" — competes with Experiences/Tag Team. Consider moving a couple to Stress or passive.

## Tier 3 — Taste-forks (OPEN — need the user)

- [ ] **#11 — Is [[Long-Lived]] still recognizably a *vampire*?** Reframed so hard (ageless + perfect memory + "feed on knowledge or fade") it may not *read* as vampire. The "feed or fade" + immortality skeleton is there, but it's the least legible-to-its-monster of the set. Keep the clean break, or re-attach a small vampiric tell (blood-as-memory, a threshold custom, a sensory thing)?
- [ ] **#12 — Flight appears 3× among Conditions** (avian Two-Bodied [now capped to glide], Bound's granted power, Phoenix) + Tengu. Probably fine at this world's density — but make it a conscious worldbuilding note, not an accident.
- [ ] **#8 — The demon complex is top-heavy.** One monster (demon) spans three notes — [[Bound]], [[The Unbound]], the Given-Over — while every other monster gets one. Rich and good, but confirm it's intended.

---

## Per-Condition quick reference (post-Tier-1)

| Condition | State after Tier 1 |
|---|---|
| [[Long-Lived]] | Clean. Only open Q is monster-legibility (#11, Tier 3). |
| [[Two-Bodied]] | **Reworked** — free shift, natural weapon + signature capability, size band. |
| [[Returned]] | **Reworked** — Refuse to Fall costs a scar, finite; Refuse the Rest cut. |
| [[Bound]] | Strong; top-heavy demon complex (#8); finish Given-Over name (Tier 2). |
| [[The Unbound]] | **Renamed** from The Hollow; good temptation engine. |
| [[Far-Voiced]] | One of the best. Shares the token-clock chassis. |
| [[The Stilled]] | Solid; leans on "stop bleeding/poison" mechanics DH lacks (minor). |
| [[The Answered]] | Most complex card; well-built; Ember is the combat default (mild). |
| [[The Taken-In]] | Fix Spellcast-first + 1d8 scaling (Tier 2). |
| [[Phoenix]] | Boons unchanged (they're fine). **Open (Tier 2):** Rise From Ash / The Dwindling overlap — fold or differentiate. Fire-immunity→resistance still an open dial. |

## Links
- [[Conditions]] · [[The Premise]] · [[Build Plan]] · [[Roadmap]]
