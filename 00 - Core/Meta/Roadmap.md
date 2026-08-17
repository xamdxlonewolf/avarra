---
title: Roadmap
type: moc
visibility: gm
note_status: draft
status: active
tags: [meta, roadmap, build-plan, tracker, moc]
aliases: [The Roadmap, Epics, Build Tracker]
created: 2026-08-17
updated: 2026-08-17
---

# Roadmap

> **What this is.** The dependency-ordered build plan for the setting, as **Epics → Stories → Tasks**. It answers *what to work on, in what order,* so each piece has a fixed reference point before the pieces that lean on it get built. [[Build Plan]] stays the fast handoff brief; **this** is the detailed tracker. Design premise & locked decisions live in [[The Premise]].

## How to use this note

- **Order = dependency, not folder number.** Do the things *most other things point at* first (the Turning Tree before the society that forms around it), so later work builds against a fixed anchor instead of being retrofitted.
- **Two status signals, not one:**
  - **Checkboxes** (`- [ ]` / `- [x]`) = *is the work done?* Gives a live % (Obsidian can total them; a manual tally sits under [[#Progress]]).
  - **Canon-status tag** = *how settled is the decision?* — 🔒 **Locked** (load-bearing, don't re-litigate) · 🟡 **Proposed** (provisional, safe to change) · ⚠️ **Contradicted** (conflicts something else, needs reconciling). Borrowed from the `shared-world` philosophy. A one-line 🔒 decision is worth more than a fleshed 🟡 note.
- **Progressive elaboration.** Only the **next 1–2 epics** are broken down to Task depth. Later epics stay at Epic/Story level until we reach them — planning subtasks for things not yet conceived is waste (`shared-world`: *the bible grows with the story; stay lean*).
- **Check the skill.** Each epic names the craft skill to run. When something feels off, route through `story-sense` first.
- **Blast radius.** Low = self-contained, safe to do anytime. High = many notes will point at it; get it right early.

---

## The Epic Spine (dependency order)

| # | Epic | Unblocks / why here | Blast radius | Status |
|---|------|--------------------|:---:|:---:|
| **0** | [[#Epic 0 — Foundations]] | The load-bearing concept & mechanics | — | 🟢 ~90% |
| **1** | [[#Epic 1 — The Engine's Anchor (Turning Tree & Leaf-Mother)]] | Religion, geography, settlements, law, the schism all point back here | **High** | ⬜ next |
| **2** | [[#Epic 2 — Society & Institutions]] | Every settlement & faction inherits these rules | **High** | ⬜ |
| **3** | [[#Epic 3 — The World Frame]] | The physical stage settlements/cultures stand on | Med | ⬜ |
| **4** | [[#Epic 4 — Cultures & Kinds]] | Peoples & customs; custom ancestries ✅ done | Low | 🟢 partial |
| **5** | [[#Epic 5 — Factions & Orders]] | The institutional actors (guilds, Tithe-infra orgs) | Med | ⬜ |
| **6** | [[#Epic 6 — History]] | When did the Trees appear? gives the world a past | Med | ⬜ |
| **7** | [[#Epic 7 — Settlements]] | Concrete stages for play | Med | ⬜ |
| **8** | [[#Epic 8 — People]] | The cast | Low | ⬜ |
| **9** | [[#Epic 9 — Secrets & Canon]] | Revelation architecture — runs *alongside* from Epic 0 | — | 🟡 ongoing |
| **10** | [[#Epic 10 — Campaign]] | Actual play material; needs the world to exist first | — | ⬜ |

> **Two deliberate departures from the old [[Build Plan]] order:** (1) the **Turning Tree / Leaf-Mother** is promoted *above* the custom ancestries — it's the single highest-leverage anchor, so society/religion/geography get a fixed point to build against. (2) An explicit **"lock the keystone secret"** task sits in Epic 0 — we don't flesh it, just *decide the answer*, because the theme and every reveal need to point somewhere.

---

## Epic 0 — Foundations
**Skill:** `systemic-worldbuilding` · **Status:** 🟢 nearly done — only the keystone secret remains.

- [x] 🔒 Two-layer model (Kind + Condition) — see [[The Premise]]
- [x] 🔒 Acquisition engine (Given at the Tree / Struck later) + population math
- [x] 🔒 Full 10-Condition roster (monsters, standing, path, %)
- [x] 🔒 All 10 Condition **mechanics** designed (Transformation cards in `09 - Creatures/Conditions/`)
- [ ] 🟡 **Lock the keystone GM secret** — *is the Leaf-Mother real?* Decide the one-line answer (don't flesh it). Everything in Epic 1 & the theme aim at this. → seeds [[#Epic 9 — Secrets & Canon]]
- [ ] 🟡 **Name the setting** (currently unnamed) — low urgency, but stops being "the setting" once it has a name

---

## Epic 1 — The Engine's Anchor (Turning Tree & Leaf-Mother)
**Skill:** `belief-systems` (+ `oblique-worldbuilding` for in-world texts, `paradox-fables` for the schism folklore) · **Status:** ⬜ **← NEXT** · **Blast radius: High.**

> The Leaf-Fall is *already* locked as the engine ([[The Premise]]). This epic makes the Tree and its religion **concrete** — the thing every later system references.

### Story 1.1 — The Turning Tree (the object)
- [ ] 🟡 Name the Tree (species-name + common name)
- [ ] 🟡 **One great Tree vs. scion-per-town** (Build Plan leans scion-per-town) — decide; it drives geography & settlement layout
- [ ] What a Tree physically *is* / where scions come from / can one die or be moved
- [ ] The Leaf-Fall ceremony: staging, who attends, what the colours look like, the "hug" (Kept) moment
- [ ] How the colour→Condition mapping is read/known (a priesthood? common knowledge? a guild?)

### Story 1.2 — The Leaf-Mother (the religion)
- [ ] 🔒 (already) she's a *belief, not confirmed cosmology* — keep it that way in-notes
- [ ] Believers' doctrine: the Conditioned are *chosen*; the Trees are her hands
- [ ] Skeptics' position: it's just what the Trees do — biology, not benediction
- [ ] The live schism (from [[The Premise]]): *if she blesses everyone, why are ~25% Given nothing? Are the Kept unblessed or spared? What does it mean the Struck receive a Condition she never handed out?*
- [ ] Clergy / institutions of the faith (feeds [[#Epic 5 — Factions & Orders]])
- [ ] 1–2 in-world texts or sayings (`oblique-worldbuilding`) that carry the doctrine *and* seed a reveal

### Story 1.3 — Reconcile with canon
- [ ] Ensure Tree/Leaf-Mother notes declare `reveals:` for the keystone secret (Epic 0)
- [ ] Cross-link from [[The Premise]], [[Conditions]], and the relevant section MOCs

---

## Epic 2 — Society & Institutions
**Skill:** `governance-systems`, `economic-systems` · **Status:** ⬜ · **Blast radius: High.**

> The payoff epic: *how does a civilization work when 3 of 4 people carry a Tithe?* Every settlement & faction inherits these answers, so it comes before the specific places.

### Story 2.1 — Law & citizenship (`governance-systems`)
- [ ] Legal status of each Condition; who regulates the feared ones (The Stilled, Bound)
- [ ] How the Struck are handled legally (no ceremony, sometimes "a little suspect")
- [ ] Rights of the Kept
### Story 2.2 — Economy & the Tithe-infrastructure (`economic-systems`)
- [ ] The institutions that help people *pay their Tithes* (the "why society organizes around the Conditioned")
- [ ] Labor: which Conditions do which needed jobs (already sketched per-Condition — systematize)
- [ ] Banking / longevity / inheritance under the Long-Lived (they outlive heirs)
### Story 2.3 — Daily life
- [ ] Marriage & family across Kinds + Conditions (stacking); the Long-Lived emotional Tithe socially
- [ ] Medicine (The Stilled in medicine; the Returned tending the dead)
- [ ] City design when a quarter of adults have a becoming — *feeds [[#Epic 7 — Settlements]]*

---

## Epic 3 — The World Frame
**Skill:** `systemic-worldbuilding` · **Status:** ⬜ · Geography, climate, where the Trees grow, the physical stage. Depends only on Epic 0; can run in parallel with Epic 1–2 once the one-vs-many-Trees call is made.

- [ ] Geography & regions (`01 - World`)
- [ ] Where Turning Trees grow (ties to Epic 1.1) — climate/ecology consequences
- [ ] Astronomy/solstice (the Leaf-Fall is solstice-timed — lock the calendar)

---

## Epic 4 — Cultures & Kinds
**Skill:** `worldbuilding`, `character-naming`, optional `conlang`/`language-evolution` · **Status:** 🟢 custom ancestries DONE; peoples/customs pending. · **Blast radius: Low.**

### Story 4.1 — Custom ancestries ✅ **DONE (merged 2026-08-17)**
- [x] 🔒 [[Kitsune]] — locked (3 features)
- [x] 🔒 [[Selkie]] — locked (3 features)
- [x] 🔒 [[Tengu]] — locked (3 features)
- [ ] 🟡 **Revisit flag:** give all three a light glance at the next review pass (may get small reworks) — noted, not blocking
### Story 4.2 — Peoples, customs, naming (pending)
- [ ] How Kinds distribute across the world / cultures
- [ ] Naming conventions per culture (`character-naming` entropy approach)
- [ ] (optional) any conlang seeds

---

## Epic 5 — Factions & Orders
**Skill:** `governance-systems`, `underdog-unit`, `moral-parallax` · **Status:** ⬜ · Depends on Epics 1 & 2. The guilds that train the Given & regulate the Struck; the faith's clergy; the Tithe-infrastructure orgs. *Stub only until the anchor & society are set.*

---

## Epic 6 — History
**Skill:** `world-fates`, `systemic-worldbuilding` · **Status:** ⬜ · When did the Trees appear? Eras, the shape of the past. Seed the *theme* early; flesh once there's a world to have a history *of*.

---

## Epic 7 — Settlements
**Skill:** `settlement-design` · **Status:** ⬜ · Specific places, built on Epics 2–4. *Stub only for now.*

---

## Epic 8 — People
**Skill:** `character-arc`, `character-naming`, `positional-revelation`, `perspectival-constellation` · **Status:** ⬜ · The specific cast. *Stub only for now.*

---

## Epic 9 — Secrets & Canon
**Skill:** `oblique-worldbuilding`, `paradox-fables` · **Status:** 🟡 ongoing — runs *alongside* everything from Epic 0. · The revelation architecture (`11 - Secrets`). Seed the keystone secret in Epic 0; flesh reveals as notes that expose them get authored (`reveals:` front-matter).

---

## Epic 10 — Campaign
**Skill:** `key-moments`, `endings`, `table-tone`, `dialogue` · **Status:** ⬜ · Actual play material (`12 - Campaigns`). Depends on the world existing. *Not before the world frame + a settlement + a cast exist.*

---

## Progress

> Manual tally — update when checking boxes. (Story/Task counts, not epics.)

- **Epic 0 — Foundations:** 4 / 6 tasks (67%) — keystone secret + name remain
- **Epic 1 — Anchor:** 0 / ~14 — **next**
- **Epic 4 — Cultures & Kinds:** custom ancestries 3/3 ✅; peoples/customs 0/3
- **Epics 2, 3, 5–10:** not yet decomposed (progressive elaboration)
- **Locked decisions:** two-layer model, engine, roster, all 10 Condition mechanics, 3 custom ancestries.

## Links
- [[Build Plan]] — handoff brief (points here) · [[The Premise]] — design hub
- [[Conditions]] · [[00 - Core]] · [[Conventions]]
