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
| **0** | [[#Epic 0 — Foundations]] | The load-bearing concept & mechanics | — | ✅ done |
| **1** | [[#Epic 1 — The Engine's Anchor (Turning Tree & Leaf-Mother)]] | Religion, geography, settlements, law, the schism all point back here | **High** | 🟢 core done |
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
**Skill:** `systemic-worldbuilding` · **Status:** ✅ **complete (2026-08-20).**

- [x] 🔒 Two-layer model (Kind + Condition) — see [[The Premise]]
- [x] 🔒 Acquisition engine (Given at the Tree / Struck later) + population math
- [x] 🔒 Full 10-Condition roster (monsters, standing, path, %)
- [x] 🔒 All 10 Condition **mechanics** designed (Transformation cards in `09 - Creatures/Conditions/`)
- [x] 🔒 **Keystone GM secret locked (2026-08-19):** *the Leaf-Mother is real and benevolent* — the Trees genuinely are her hands, the gifts are real, skeptics are sincere and wrong. One-line answer decided, not fleshed. → [[Is the Leaf-Mother Real]] (`reveal_tag: leaf-mother-is-real`), seeds [[#Epic 9 — Secrets & Canon]]
- [x] 🔒 **Setting named (2026-08-20): _The Turning_** — named for its defining act (the tenth-year Turning at the [[Turning Tree]]); plainest register, sits flush with "Turning Tree" / "Turning-week." (Variant "The Turning Lands" available for regional phrasing.)

---

## Epic 1 — The Engine's Anchor (Turning Tree & Leaf-Mother)
**Skill:** `belief-systems` (+ `oblique-worldbuilding` for in-world texts, `paradox-fables` for the schism folklore) · **Status:** 🟢 **core done (2026-08-19)** — Tree + faith notes written; deferred sub-items remain. · **Blast radius: High.**

> The Leaf-Fall is *already* locked as the engine ([[The Premise]]). This epic makes the Tree and its religion **concrete** — the thing every later system references. **Core notes:** [[Turning Tree]] (object + rite) and [[The Leaf-Mother]] (the faith).

### Story 1.1 — The Turning Tree (the object) → [[Turning Tree]]
- [x] 🟡 Name the Tree — everyday **Turning Tree**; reverent **Hand of the Mother**; species-word **motherwood**; the origin is **the Awakening Tree** (liturg. *the First Hand*). *(Proposed — safe to change.)*
- [x] 🔒 **Topology decided (2026-08-19):** **one origin Tree (the Awakening Tree); town Trees are living grafts of it** — carried out to towns as they arise. Gives a Tree nearby *and* a pilgrimage. Drives geography (Epic 3) & settlement layout (Epic 7).
- [x] What a Tree physically *is* / where scions come from (graft-rite) / can one die or be moved (mortal wood; sickens & dies; replace by fresh graft; hard to transplant mature)
- [x] The Leaf-Fall ceremony: staging, who attends, the colour-fall, the "hug" (Kept) moment
- [x] How the colour→Condition mapping is read/known — folk-known commons + **tree-warden clergy** as authoritative readers (full colour palette deferred to Epic 2/4)

### Story 1.2 — The Leaf-Mother (the religion) → [[The Leaf-Mother]]
- [x] 🔒 (already) she's a *belief, not confirmed cosmology* — kept that way in-notes (player-facing; GM truth walled off in [[Is the Leaf-Mother Real]])
- [x] Believers' doctrine: the Conditioned are *chosen*; the Trees are her hands (gift-religion, "tend what you're given")
- [x] Skeptics' position: it's just what the Trees do — and the faith is **orthopraxic**, so skeptics belong through practice
- [x] The live schism — built as **three good-faith branches**: Kept (spared/slighted), Struck (still hers?), and does-a-mind-choose (believer/skeptic)
- [ ] Clergy / institutions of the faith — sketched (tree-wardens, the Awakening-Tree seat); full orders **deferred to [[#Epic 5 — Factions & Orders]]**
- [x] 1–2 in-world texts (`oblique-worldbuilding`) that carry doctrine *and* seed a reveal — the Tender's blessing + the Kept-child's saying

### Story 1.3 — Reconcile with canon
- [x] Tree/Leaf-Mother notes declare `reveals: [leaf-mother-is-real]`
- [x] Cross-linked from [[The Premise]], the [[07 - Religion]] & [[11 - Secrets]] MOCs (Conditions cross-link pending a later pass)

> **Deferred out of Epic 1 (tracked):** full clergy orders + pilgrimage-seat politics → Epic 5 · colour→Condition palette → Epic 2/4 · sacred calendar/solstice reckoning → Epic 3 · faith economy → Epic 2 · **the wider pantheon / other religions** (Motherfaith is one faith among several — user directive 2026-08-19) → **new religion-as-a-whole pass** (see Story 1.4).

### Story 1.4 — Wider pantheon / other religions (🟡 NEW — deferred)
- [ ] 🟡 The Leaf-Mother is *one faith among several* — design the other gods/religions and how they coexist, compete, or syncretize with the Motherfaith. Keeps the world alive & diverse. *(Per user, do this in the religion-as-a-whole pass, not now.)*

---

## Epic 2 — Society & Institutions
**Skill:** `governance-systems`, `economic-systems` · **Status:** 🟢 in progress (started 2026-08-20) · **Blast radius: High.**

> The payoff epic: *how does a civilization work when 3 of 4 people carry a Tithe?* Every settlement & faction inherits these answers, so it comes before the specific places.

> **Frame locked before starting (2026-08-20 — see [[The Premise]]):**
> - **Scale:** ~15 large polities across 3 large + 1 small continent. Epic 2 builds the **universal social physics** + **2–3 polity archetypes**; the rest are named-stubs deferred to Epic 3/7.
> - **Register:** late-medieval burgher surface (no print, no gunpowder); the *only* advancement beyond comes from **Condition-labor** — legible, concentrated, paid-for by Tithes.
> - **R2 social guard (from the keystone):** the Leaf-Mother's benevolence is *cosmological, not social* — do **not** let it launder injustice. Struck stigma, Tithe-infrastructure-as-leverage, guild conscription are **real frictions to keep**, not misreadings to dissolve.

### Story 2.1 — Law & citizenship (`governance-systems`) ✅ **DONE (2026-08-20)** → [[Law and Citizenship]]
> **Core design call (user, 2026-08-20): citizenship is _witnessed, not recorded_.** No universal register (that was too invasive for a ~5%-scary world). You belong because your town *watched you Turn*; proof-at-a-distance runs through **vouching people** (Long-Lived memory / Bound binding word / Far-Voiced unfakeable feeling), not papers. The only per-person paper is a **guild safety-licence for the ~3 hazardous Conditions.** A universal register survives *only* as **one aberrant kingdom's paranoia** (the Watchful) — the creepy version is rare and villainous, not the baseline.
- [x] Legal status of each Condition; who regulates the feared ones (The Stilled, Bound) — the **guild safety-licence** (danger-to-others only, held by the person, not a census); the **Inviolate Will** doctrine (no Condition compels a will) sorts the criminal code
- [x] How the Struck are handled legally ("a little suspect") — they **changed *unwitnessed*** (later & alone), so must be **vouched anew**; the vulnerable are the *unvouched*, not the "undocumented"
- [x] Rights of the Kept — witnessed at ten, untithed, unlicensed; the *default legal person*; wrinkles: still-Struck-later, and pitied where reverence runs hot
- [x] **Bonus locks:** the **three pillars** (Long-Lived / Bound / Far-Voiced *are* the evidence/contract apparatus — and are *why* no register is needed); **3 polity stances** (Warm / Watchful-register-keeper / Frontier) — no planet-of-hats; R2 guard applied in GM Notes
- **🟡 Deferred:** in-world naming + regional/language variants for every institution (names here are provisional descriptive placeholders) → after polity archetypes + language sketches exist (Epic 2 tail / Epic 4).
### Story 2.2 — Economy & the Tithe-infrastructure (`economic-systems`) ✅ **DONE (2026-08-20)** → [[Economy and the Tithe]]
> **Thesis:** the **Tithe is the economy's engine** — 75% of people carry a permanent upkeep, so *Tithe-provision is a whole sector* (the answer to "why society organizes around the Conditioned"). **Structural key:** **self-paying Tithes** (the work *is* the payment — Answered craft, Two-Bodied ranging, Stilled exertion, Returned purpose) vs **provided-for Tithes** (pure cost — Taken-In green, Long-Lived novelty, Far-Voiced outlets, Unbound warmth, Bound terms). The provided-for are *economically exposed* → whoever furnishes the Tithe holds power (the R2 lever).
- [x] Institutions that help people pay their Tithes — the **Tithe-infrastructure sector**; **Tithe-poverty** ("too poor to stay whole" → slides to the scary edge); public-good / private-burden / leverage answers
- [x] Labor by Condition (systematized) — the Tithe and the vocation are usually the *same shape*; **the Kept = free generalist labor** (untithed, unguilded — an economic freedom under the social slight)
- [x] Banking / longevity / inheritance under the Long-Lived — **deathless houses** (the trusted note ≈ this world's gold standard; century instruments; concentration risk); the deathless **outlive all heirs → endow** (pay their own novelty-Tithe by funding libraries/universities); Given-Over = a self absorbed by a creditor
- [x] **Bonus:** center/periphery (reach-edge shapes the trade map); shadow economy (illicit Tithe-supply, off-book contracts, sold vouching); 3 polity economic faces (Warm public-good / Watchful leverage / Frontier improvise)
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

- **Epic 0 — Foundations:** 6 / 6 tasks (100%) ✅ — setting named *The Turning* (2026-08-20)
- **Epic 1 — Anchor:** 12 / 15 (80%) — core done; deferred: full clergy orders (→E5), wider pantheon Story 1.4 (→religion pass), Conditions cross-link
- **Epic 4 — Cultures & Kinds:** custom ancestries 3/3 ✅; peoples/customs 0/3
- **Epics 2, 3, 5–10:** not yet decomposed (progressive elaboration)
- **Epic 2 — Society:** 🟢 in progress (started 2026-08-20); frame locked (world scale + register + R2 guard). **Story 2.1 (Law & Citizenship) ✅** → [[Law and Citizenship]]; **Story 2.2 (Economy & the Tithe) ✅** → [[Economy and the Tithe]]. Story 2.3 (Daily life) pending, then 2–3 polity archetypes.
- **Locked decisions:** **setting name (_The Turning_)**, two-layer model, engine, roster, all 10 Condition mechanics, 3 custom ancestries, keystone secret (Leaf-Mother real+benevolent **but bounded & costly**), Tree topology (one Awakening Tree + living grafts), **world scale (~15 polities / 3+1 continents)**, **register (late-medieval + Condition-labor advances)**.

## Links
- [[Build Plan]] — handoff brief (points here) · [[The Premise]] — design hub
- [[Conditions]] · [[00 - Core]] · [[Conventions]]
