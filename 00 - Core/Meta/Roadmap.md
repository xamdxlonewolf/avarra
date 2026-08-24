---
title: Roadmap
type: moc
visibility: gm
note_status: draft
status: active
tags: [meta, roadmap, build-plan, tracker, moc]
aliases: [The Roadmap, Epics, Build Tracker]
created: 2026-08-17
updated: 2026-08-24
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
| **1** | [[#Epic 1 — The Engine's Anchor (Turning Tree & Leaf-Mother)]] | Religion, geography, settlements, law, the schism all point back here | **High** | 🟢 core + 1.4 done |
| **2** | [[#Epic 2 — Society & Institutions]] | Every settlement & faction inherits these rules | **High** | ✅ done |
| **3** | [[#Epic 3 — The World Frame]] | The physical stage settlements/cultures stand on | Med | 🟢 core done |
| **4** | [[#Epic 4 — Cultures & Kinds]] | Peoples & customs; **4** custom ancestries ✅ · Story 4.2 ✅ | Low | 🟢 core done |
| **5** | [[#Epic 5 — Factions & Orders]] | The institutional actors (guilds, Tithe-infra orgs) | Med | ✅ done |
| **6** | [[#Epic 6 — History]] | When did the Trees appear? gives the world a past | Med | ✅ done |
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
- [x] 🟡 **Household elaboration (2026-08-23):** she is first of a pantheon; she Gives only; Other Hands Strike at restricted doors under her allowance. Yumboes: no Gifts, rare Struck. → [[The Other Hands]] (`reveal_tag: the-other-hands`). Names of the lesser Hands 🟡; structure 🔒. Player-facing unconfirmed.
- [x] 🔒 **Setting named (2026-08-20): _The Turning_** — named for its defining act (the tenth-year Turning at the [[Turning Tree]]); plainest register, sits flush with "Turning Tree" / "Turning-week." (Variant "The Turning Lands" available for regional phrasing.)

---

## Epic 1 — The Engine's Anchor (Turning Tree & Leaf-Mother)
**Skill:** `belief-systems` (+ `oblique-worldbuilding` for in-world texts, `paradox-fables` for the schism folklore) · **Status:** 🟢 **core done (2026-08-19); Story 1.4 done (2026-08-23); clergy → Stories 5.1–5.2 (2026-08-23)** — Tree + Motherfaith + the other four faiths written; working houses built. · **Blast radius: High.**

> The Leaf-Fall is *already* locked as the engine ([[The Premise]]). This epic makes the Tree and its religion **concrete** — the thing every later system references. **Core notes:** [[Turning Tree]] (object + rite) and [[The Leaf-Mother]] (the faith).

### Story 1.1 — The Turning Tree (the object) → [[Turning Tree]]
- [x] 🟡 Name the Tree — everyday **Turning Tree**; reverent **Hand of the Mother**; species-word **motherwood**; the origin is **the Awakening Tree** (liturg. *the First Hand*). *(Proposed — safe to change.)*
- [x] 🔒 **Topology decided (2026-08-19):** **one origin Tree (the Awakening Tree); town Trees are living grafts of it** — carried out to towns as they arise. Gives a Tree nearby *and* a pilgrimage. Drives geography (Epic 3) & settlement layout (Epic 7).
- [x] What a Tree physically *is* / where scions come from (graft-rite) / can one die or be moved (mortal wood; sickens & dies; replace by fresh graft; hard to transplant mature)
- [x] The Leaf-Fall ceremony: staging, who attends, the colour-fall, the "hug" (Kept) moment
- [x] How the colour→Condition mapping is read/known — folk-known commons + **tree-warden clergy** as authoritative readers
- [x] 🔒 **Colour→Condition palette** (2026-08-23, with Story 4.2; user-approved) — deep red Long-Lived · storm-grey Two-Bodied · lamp-amber Answered · sea-blue Far-Voiced · pale stone Stilled · copper-green Taken-In · white-fire Phoenix. Struck-only have no colour. → [[Turning Tree#Reading the colours (colour → Condition)]]

### Story 1.2 — The Leaf-Mother (the religion) → [[The Leaf-Mother]]
- [x] 🔒 (already) she's a *belief, not confirmed cosmology* — kept that way in-notes (player-facing; GM truth walled off in [[Is the Leaf-Mother Real]])
- [x] Believers' doctrine: the Conditioned are *chosen*; the Trees are her hands (gift-religion, "tend what you're given")
- [x] Skeptics' position: it's just what the Trees do — and the faith is **orthopraxic**, so skeptics belong through practice
- [x] The live schism — built as **three good-faith branches**: Kept (spared/slighted), Struck (still hers?), and does-a-mind-choose (believer/skeptic)
- [x] 🟡 Clergy / institutions of the faith — full orders built as [[The Tree-Wardens]] (Story 5.1, 2026-08-23). Names and the skeptic-warden call still **taste-open**.
- [x] 1–2 in-world texts (`oblique-worldbuilding`) that carry doctrine *and* seed a reveal — the Tender's blessing + the Kept-child's saying

### Story 1.3 — Reconcile with canon
- [x] Tree/Leaf-Mother notes declare `reveals: [leaf-mother-is-real]`
- [x] Cross-linked from [[The Premise]], the [[07 - Religion]] & [[11 - Secrets]] MOCs (Conditions cross-link pending a later pass)

> **Deferred out of Epic 1 (tracked):** Conditions cross-link (pending). Clergy orders ✅ Story 5.1 ([[The Tree-Wardens]], names 🟡). Other houses' orders ✅ Story 5.2. Colour palette ✅ Story 4.2 · Calendar ✅ Epic 3 · faith economy ✅ Epic 2 · wider pantheon ✅ Story 1.4.

### Story 1.4 — Wider pantheon / other religions ✅ **DONE (2026-08-23)** → [[Faiths of the Turning]]
- [x] 🟡 The Leaf-Mother is *one faith among several* — four lived rival faiths built against the Epic 3 continental seeds, plus how they coexist / syncretize / fight. **Not** a D&D god-list; no second cosmology locked. → [[The Watching]] (*Haelthael*, Maiethorn) · [[The Fair Hand]] (*Leddoren*, Strandoren) · [[The Old Ways]] (*Vaeloren*, Heskoren) · [[The Open Table]] (*Ndeyaan*, Kumbaan) · shared paradox-fable [[The Child at Four Doors]]

---

## Epic 2 — Society & Institutions
**Skill:** `governance-systems`, `economic-systems` · **Status:** ✅ **complete (2026-08-21)** · **Blast radius: High.**

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
### Story 2.3 — Daily life (`governance-systems` / `worldbuilding`) ✅ **DONE (2026-08-21)** → [[Daily Life]]
> **Frame:** everyday life is where the **~5%-scary** dial is set at eye level — warm and ordinary at the surface, a real ache in the specific cases. Family presented as a **spectrum** (mundane → aching); medicine as **wonder + uncanny** blended; city as **principles only** (concrete places deferred to Epic 7).
- [x] Marriage & family across Kinds + Conditions (stacking) — a **spectrum**: most households mundane-mixed (no "unmixed baseline" to marry away from); the middle = Tithe as shared family labor; the aching end = **loving someone you'll outlive** (the Long-Lived marriage — *the cost measured in funerals*, stop-or-begin-again). Threads: threshold courtesy in the home, the **Returned's "cold embrace"** as a family diagnostic, Two-Bodied bloodlines, raising a child before they Turn.
- [x] Medicine — **the Stilled are the surgeons** (gaze arrests bleeding/holds still, wonder + the feared-licensed edge); **the Returned do the lethal work** (plague wards, tending the dead); rest is ordinary 1400s care, **unequally distributed** (clusters in the rich core; Tithe-poor can't reach it)
- [x] City design — **principles, not places** (feeds [[#Epic 7 — Settlements]]): the **Tree at the centre**, Tithe-provision as civic utility (venting-halls, garden-commons, ranging-commons, endowed libraries), dangerous trades on the edges, homes that accommodate becomings, reach-edge writes the map
- [x] **Bonus:** 3 polity domestic faces on the same theology/reach/governance axes + "mind the combinations"; R2 guard applied in GM Notes (the injustice reaches the hearth and stays real)

### Story 2.4 — Polity archetypes (`governance-systems` / `worldbuilding`) ✅ **DONE (2026-08-21)** → [[Polity Archetypes]]
> **Frame:** prove the universal social physics flex by building **2–3 polities at *different corners* of the theology/reach/governance axis-space** (audit design note: NOT three-in-a-row on one axis). Each pair shares **exactly one** axis and differs on the other two, so the set *isolates* each axis and proves the three are independent. Extends the single-axis touchstones (Warm/Watchful/Frontier) into full three-knob corners.
- [x] **Three corners built** — **The Waiting Lands** (theology high · reach low · gov low — warm/poor/faithful pilgrim edge), **The Ledger Coast** (theology low · reach high · gov low — rich/cool secular merchant power), **The Tallied Crown** (all three high — sanctified surveillance, the darkest corner). Each walked through law · economy · daily life + its distinct injustice.
- [x] **R2 guard applied** — three *different* injustices (guilt-theology / market-fade / sacred census), none dissolvable by the keystone reveal because they share no mechanism, only that people built them. Reach-edge cause kept GM-side in all three.
- [x] 🟡 **Naming labels are provisional** (working names picked with user 2026-08-21: Waiting Lands / Ledger Coast / Tallied Crown) — settled in-world names come *in* the naming pass below.
- [x] ✅ **DONE (2026-08-21) — the in-world naming pass.** Built [[The Old Tongue]] (root liturgical tongue *Maiethren* — warm/weighty phonology, pronunciation key, sacred root lexicon; **one root → three daughter drifts** mirroring the one-Tree/grafts cosmology) and named the three polities from it: **Vaethorn** (the Waiting Lands), **Lestrand** (the Ledger Coast), **Threnmaieth** (the Tallied Crown) — *the most-eroded name is the most secular polity.* Then [[Naming in the Turning]] (institution dictionary: common-tongue name + three stance-variants each — e.g. venting-hall → gift-hall / release-house / counted hall; the census = Threnhael "the whole-keeping"). Design lever landed as built: *the name a polity gives a shared institution reveals its stance.* All four social-structure notes updated. **Epic 2 tail complete.** (Deep grammar + the other ~12 polities' tongues → [[#Epic 4 — Cultures & Kinds|Epic 4]].)

---

## Epic 3 — The World Frame
**Skill:** `systemic-worldbuilding` · **Status:** ✅ **core done (2026-08-22)** — the four-continent frame, all four continent notes, the calendar, and (pulled forward) the 4th ancestry are written. · Geography, climate, where the Trees grow, the physical stage.

> **Built as a reach-gradient.** The load-bearing call: the whole map is a **gradient of the [[Turning Tree|Trees']] reach** — sacred-dense origin → mercantile middle → thin frontier → storm-walled isle beyond. Physical map = cosmological map. → [[The World Frame]].

- [x] 🟡 **Geography & regions (`01 - World`)** → [[The World Frame]] (top-level) + four continents: **[[Maiethorn]]** (Motherland, full reach, holds [[Polity Archetypes|Threnmaieth]]), **[[Strandoren]]** (Shore-lands, high reach, trade, holds [[Polity Archetypes|Lestrand]]), **[[Heskoren]]** (Sundered Reach, thin reach, frontier, holds [[Polity Archetypes|Vaethorn]]), **[[The Sundering Isle]]** (Kumbaan — storm-walled, near-no reach, Yumboe homeland). The three archetype polities placed on three *different* continents; **rival faiths woven into the large continents** and now built ([[The Watching]] · [[The Fair Hand]] · [[The Old Ways]] · [[The Open Table]] — [[Faiths of the Turning]]).
- [x] 🟡 **Where Turning Trees grow** — the reach-gradient *is* this: densest/healthiest on Maiethorn, thinning outward, near-none across the storm-wall. Present-day thin reach = Tree-poor places (young/sick/few grafts), per [[The Ages of the Turning]] (the Grafting as a still-moving wave). Keystone edge kept GM-side in every continent note.
- [x] 🟡 **Astronomy/solstice — calendar locked** → [[The Reckoning of the Year]]: two solstices; the Leaf-Fall is **High Solstice / midsummer**, held **Turning-Week**; ~1400s-legible 12-month lunar-hinged calendar; [[The Sundering Isle|Kumbaan]] keeps the *moon, not the solstice* (a keystone tell).
- [x] 🟡 **(Pulled forward from Epic 4) — 4th custom ancestry built to full depth** → [[Yumboe]] (the good people / Bakhna Rakhna): three Daggerheart features (Hollow-Hill · Moon-Waked · The Unseen Hands), folklore-checked (Wolof/Senegambian *Yumboe* myth), small/pearly/silver, LOCKED. Its own non-Maiethren tongue seeded. The Isle *needed* its people, so the ancestry came here rather than waiting for Epic 4.
- **Map assets baked in (per user):** every geography note carries a **GPT Image prompt**; [[The World Frame]] additionally carries an **Azgaar heightmap template**, a **Maiethren name base**, and a bonus **Azgaar seed script**. (The Isle's own Wolof-flavoured name base is seeded in [[Yumboe]], to build alongside Epic 4.)
- **🟡 Deferred (tracked):** per-region *deep* climate/ecology; the ~12 other great powers as named-stubs (→ [[Roadmap|Epic 7]]). Month-names + the Isle's name base ✅ Story 4.2. Rival faiths ✅ Story 1.4.

---

## Epic 4 — Cultures & Kinds
**Skill:** `worldbuilding`, `character-naming`, optional `conlang`/`language-evolution` · **Status:** 🟢 custom ancestries DONE; Story 4.2 DONE (2026-08-23). · **Blast radius: Low.**

### Story 4.1 — Custom ancestries ✅ **DONE (3 merged 2026-08-17; 4th added 2026-08-22)**
- [x] 🔒 [[Kitsune]] — locked (3 features)
- [x] 🔒 [[Selkie]] — locked (3 features)
- [x] 🔒 [[Tengu]] — locked (3 features)
- [x] 🔒 [[Yumboe]] — locked (3 features: Hollow-Hill · Moon-Waked · The Unseen Hands). **Built in Epic 3** (the far isle [[The Sundering Isle]] needed its people); the good people / *Bakhna Rakhna*, small/pearly/silver hill-folk, folklore-checked, their own non-Maiethren tongue. Now **four** custom ancestries.
- [ ] 🟡 **Revisit flag:** give all four a light glance at the next review pass (may get small reworks) — noted, not blocking
### Story 4.2 — Peoples, customs, naming ✅ **DONE (2026-08-23)**
- [x] 🔒 How Kinds distribute across the world / cultures — **hearths, not nations.** Custom Kinds have terrain-origins (Kitsune three Fox-grounds · Selkie coasts · Tengu ridges · Yumboe = Kumbaan only). Stock ancestries lean, they do not own continents. → [[Kinds of the Turning]] *(user-approved 2026-08-23)*
- [x] 🔒 Naming conventions per culture (`character-naming` entropy approach + `conlang` naming-inventories) — a person is named by *place*; custom Kinds keep a hearth-register. Seeds recorded. → [[Naming People in the Turning]] *(user-approved 2026-08-23)*
- [x] 🔒 [[Kitsune]] / [[Selkie]] / [[Tengu]] naming registers — *Kusawe* · *Sakoa* · *Gonan*. [[Yumboe]] register expanded. *(user-approved 2026-08-23)*
- [x] 🔒 Month-names + Kumbaan's moons → [[The Reckoning of the Year]]; new Maiethren roots in [[The Old Tongue]] *(user-approved 2026-08-23)*
- [x] 🔒 Isle Azgaar name base → [[The World Frame#③b Azgaar Kumbaan name base]] *(user-approved 2026-08-23)*
- [x] 🟢 **Root language + naming system seeded (2026-08-21, from the Epic 2 tail):** [[The Old Tongue]] + [[Naming in the Turning]]. **Still deferred (on purpose):** deep grammar/morphology (only if spoken dialogue is ever needed); the other ~12 great powers' tongues (wait for Epic 7 named-stubs).

---

## Epic 5 — Factions & Orders
**Skill:** `governance-systems`, `underdog-unit`, `moral-parallax` · **Status:** ✅ **complete (2026-08-23)** — Stories 5.1–5.3 done. Depends on Epics 1, 2, and 4.2. The institutional actors — clergy, rival-faith orders, Tithe-infra, the guilds that train the Given and licence the hazardous. Recruits by **Condition / faith / office, not by Kind** ([[Kinds of the Turning]]).

> Do not invent Kind-only orders. Do not rebuild [[The Tree-Wardens]] or the other four houses. Liturgical / own-names stay 🟡 polishable.

### Story 5.1 — Motherfaith clergy (the tree-wardens) ✅ **DONE (2026-08-23)** → [[The Tree-Wardens]]
The sketched offices in [[Turning Tree]] / [[The Leaf-Mother]], built as **one order with offices**, not rival chapters.
- [x] 🟡 Everyday name stays **tree-wardens**; liturgical **Orenhael** *(or-EN-hayl)* proposed from existing roots
- [x] 🟡 Offices: warden-hearth (town) · the Speaking (colour-authority) · Road-hands / *Thaelvaeth* (graft + sickness) · the First Seat (college, not a throne)
- [x] 🔒 Graft rule kept from Epic 1: Seat *authorizes*; a healthy town Tree may supply the cut
- [x] 🟡 Who may serve: practice-first; **not by Kind**; Condition *leans* (Kept hearths, Long-Lived Speakers, Two-Bodied Road-hands); skeptics allowed at the town-hearth, Seat believer-heavy
- [x] 🟡 The **scion-queue** as the order's injustice (R2 / moral-parallax); Cutting-leave fee
- [x] 🟡 Road-hands built as the underdog office (time + thin soil + authority that expires)
- [x] Polity faces (Vaethorn Hands-folk · Lestrand tree-tenders · Threnmaieth Reckoned Hands) + one in-world Cutting-leave
- [x] 🟡 Names / skeptic-warden / college-not-pope parked as working canon (not locked). Do not rebuild. Polish later if wanted.

### Story 5.2 — The other four houses' orders ✅ **DONE (2026-08-23)**
Watchers, Book-hands, door-keepers / Old-Ways tenders, Open-Table hosts — **one lived order each**, not a god-list of paladins. Names from [[The Old Tongue]] / [[Naming in the Turning]]. Faiths were not rebuilt.
- [x] [[The Watching]] — [[The Watchers]] (no mother-church; second reading alongside the warden, not over; liturgical *Nethoren* 🟡)
- [x] [[The Fair Hand]] — [[The Book-Hands]] (no seat, many tables; liturgical *Leddhael* 🟡). **Taste: they do not rewrite Bound Terms.**
- [x] [[The Old Ways]] — [[The Door-Keepers]] (the land is the seat; liturgical *Vaelbren* 🟡)
- [x] [[The Open Table]] — [[The Table-Keepers]] kept (own-name *Njaalo* 🟡) · isle flavor add-on [[The Shore-Sitters]] (*Njawaal* 🟡)
- [x] Recruits by faith / office / Condition-lean, **not Kind**. Did not clone the Tree-Wardens' four-office shape onto houses that have no seat.
- [x] 🟡 Mainland shadow house — [[The Slide]] picked (own-name *Vaethledd* 🟡). Back Table retired. Bought Watch / Quiet Cut unused. Do not clone the Slide as Story 5.3's official guilds.

### Story 5.3 — Tithe-infrastructure & the safety-guilds ✅ **DONE (2026-08-23)**
The sector from [[Economy and the Tithe]]: who furnishes green / novelty / outlets; the ~3 hazardous-Condition licence-guilds from [[Law and Citizenship]]. At least one underdog-unit (impossible mandate, thin resources) for play. *(Road-hands already occupy the clergy underdog; 5.3 did not clone them. **Did not clone [[The Slide]] as the official guilds** — the Slide is the overflow those guilds pretend not to know. The four houses' exposed edges — recut lintel, novation, host-rights, the sentence that will not travel — were not travelling units either.)*
- [x] 🟡 Sector hub → [[Tithe-Infrastructure]] (official = *enough* and a gate; long-houses stay deathless patronage, not a new order; Bound stays a table; ranging / Unbound warmth / Returned Purpose stay un-guilded)
- [x] 🟡 Who furnishes green → [[The Greens-Keepers]] (the lot; they will not follow you home; liturg. *Saelhael* 🟡)
- [x] 🟡 Who furnishes outlets + the Voice-ticket (one lintel, seam Condition) → [[The Hall-Keepers]] (the scheduled hour; liturg. *Aeloren* 🟡)
- [x] 🟡 Novelty left on the long-house (no librarian-order)
- [x] 🟡 Model licence-guild → [[The Stillers]] (the Grey as labor; liturg. *Stelhael* 🟡)
- [x] 🟡 Answered crafts as one sector, four doors → [[The Element-Guilds]] (the shop you cannot leave; umbrella *the Crae* 🟡)
- [x] 🟡 Underdog office → [[The Intake]] (raw Struck; desk/shed, not a circuit; success is silence)
- [x] 🔒 Did not clone Road-hands, the Slide, or the four houses' edges. Recruits not by Kind. No Kumbaan export.

---

## Epic 6 — History
**Skill:** `world-fates`, `systemic-worldbuilding` · **Status:** ✅ **complete (2026-08-24).** When did the Trees appear? Eras, the shape of the past. Hub: [[The Ages of the Turning]]. Lived road: [[The Walking Years]]. Hinge and spread: [[The First Cut]]. Residues: [[The Years of Hands]] · [[Settlement Seeds]].

> **Load-bearing calls (Story 6.1):** two clocks, not four stacked ages — **how you Turned** (Walking vs Hands) and **where the wood has reached** (the Grafting as a *still-moving wave*). No universal year-zero; dating reveals stance. Do not date the Tree's appearing. Do not lock who cut. Do not lock the nature of her limit. Do not run the colonial "we brought Trees to the far" version.

### Story 6.1 — The era spine ✅ **DONE AND 🔒 (2026-08-24, user-approved)** → [[The Ages of the Turning]]
- [x] 🔒 Two clocks, not four stacked ages — Walking/Hands (personal) · the Grafting as a wave still unfinished at [[Heskoren]] (geographic)
- [x] 🔒 Unnamed preface → [[Before the Walk]] (Tree old beyond dating; [[The Watching]] keep *the Before*)
- [x] 🔒 Everyday + liturgical names — Walking Years / *Brenvaeth* · First Cut / *Eoloren* · Years of Hands / *Ornthael* (the *Thaelvaeth* / *Brenvaeth* inversion is load-bearing) *(user-approved 2026-08-24)*
- [x] 🔒 No universal year-zero; dating reveals stance (Seat Cut-years · house-years · "year the graft took" · Watching refuse the count · Kumbaan moons)
- [x] 🔒 Present **C.Y. 387**; First Cut = C.Y. 0; spread-table Maiethorn → Strandoren by sea → Heskoren live → Kumbaan never *(user-approved 2026-08-24)*
- [x] 🔒 Do not date the Tree's appearing; do not lock who cut; do not lock [[Is the Leaf-Mother Real|the nature of her limit]]
- [x] Spine consequences: local-witness citizenship is Hands-era; deathless houses from road-houses; Cutting-leave captures a heresy; language-drift after the road's conserving pull; Heskoren is the tail
- [x] One oblique document (White-Note clerk vs Eoloren-count) + era/event notes as spine, not lived chronicle

### Story 6.2 — The Walking Years (lived) ✅ **DONE (2026-08-24)** → [[The Walking Years]]
The road as a life, not a label. Depends on 6.1. Do not rebuild the spine.
- [x] 🟡 What the walk was — three walks (Near Mile · Salt Walk · Long Mile); Turning-Week as a one-week door; who could afford it; who died
- [x] 🔒 Far reaches Kept/Struck-heavy as the *rule*, not an edge-case (split household; Old Ways refusal is not a miss)
- [x] 🟡 Institutions of the road — mile-shrines (grave and waymark); road-houses in the act (*brenhael* 🟡); summer traffic; Tithe as a pot and a shed (did not clone Epic 5)
- [x] 🔒 Witness at the origin, or not at all — vouching-at-a-distance as road-tech; origin-orphans
- [x] 🔒 [[Long-Lived]] who still say *I walked* — four jobs, disagreed meaning
- [x] Folklore [[The Child Who Counted Stones]] + innkeeper's slate (Thilim; the Held bed)
- [x] 🔒 Do not write a golden age. Do not agree with Vaethorn's guilt-theology that distance was unworthiness.

### Story 6.3 — The First Cut and the spread ✅ **DONE (2026-08-24)** → [[The First Cut]]
Hinge event + how the wave moved. Depends on 6.1–6.2. Do not rebuild the spine. Do not pick a cutter unless play needs a face.
- [x] 🟡 The five attributions, lived — folk / clergy / devout / Watching / Old Ways, without collapsing them (nameless knife · generation of argument · Eoloren sermons · pear-grafts · first meal)
- [x] 🔒 Heresy → [[The Tree-Wardens|Cutting-leave]]; the queue is born as the Seat's capture of a copy-right (Rithnali's minute; fee as a fine that forgot)
- [x] 🟡 Continent-by-continent carrying inside the locked bands (Maiethorn C.Y. 0–80 · Strandoren by sea 40–160 · gap as dead wood + maturing chain + paying next · Heskoren 200–387 · Kumbaan never)
- [x] 🔒 Seat narration vs folk memory; R2 — spreading Trees did not make society kind
- [x] 🔒 Do not date the Tree. Do not lock [[Is the Leaf-Mother Real|the nature of her limit]]. Do not send a graft across the storm-wall.
- [x] Folklore [[The Branch That Came Away]] + Seat minute (Rithnali; the verso of dead pots)

### Story 6.4 — Residues (the present as history) ✅ **DONE (2026-08-24)** → [[The Years of Hands]]
What the Walking left on the ground. Depends on 6.1–6.3. Feeds Epic 7. Do not rebuild the spine, the lived road, or the Cut.
- [x] 🟡 Pilgrimage today — three jobs (devotion / *the extra mile* · prestige / *the First-Hand year* · necessity / *the neighbour's week*); Hands can un-Hands; wood-out / hearths-in
- [x] 🟡 Visible leftovers — mile-shrines as the stone in the square; upper rooms; roads that end at a Tree
- [x] 🟡 Deathless houses' road-past as present credit — two fates: [[The White Note House]] (desk) · [[The Third Hearth]] (Held bed)
- [x] 🟡 Heskoren as live Grafting — [[Harrow's Green]] · [[The Three Hamlets Past the Ford]]; fate-pressure on Seat / Road-hands / waiting towns (`world-fates`, **noted not rolled**)
- [x] 🟡 Settlement seeds for [[#Epic 7 — Settlements]] → [[Settlement Seeds]]
- [x] 🔒 Do not narrate Ornthael as "the modern age after history." Two clocks; the wave is live. Folklore [[The Child Who Climbed the Stone]] + Mataero's letting-slate

---

## Epic 7 — Settlements
**Skill:** `settlement-design` · **Status:** ⬜ **next.** Specific places, built on Epics 2–6. Residue types already on the ground → [[Settlement Seeds]]. Do not rebuild the era spine. Do not treat Ornthael as post-history.

> Progressive elaboration from Story 6.4. Task-depth only on the next story when it is picked up. Named stubs already implied (Harrow's · the three hamlets · Third Hearth · White Note) stay seeds until a story fleshes a square.

### Story 7.1 — Name the other powers (stubs)
The ~12 unnamed great powers across the four continents. Names from [[The Old Tongue]] + stance-drift; hearths not Kind-nations. Include the un-built **secular frontier** corner on [[Heskoren]] ([[Polity Archetypes]]). Kumbaan is not a thirteenth mainland power.

### Story 7.2 — Playable squares from the leftover types
Flesh a few settlements from [[Settlement Seeds]] (not all nine types). Tree-at-the-centre grammar from [[Daily Life]]; two clocks visible; one leftover job per street. Do not clone Road-hands, the Slide, or Kind-quarters.

### Story 7.3 — The three archetype seats
Vaethorn / Lestrand / Threnmaieth as *places* (not only corners). Capitals wait on 7.1's naming pass if they need neighbours. Do not let Threnmaieth capture the First Seat in the first sentence.

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

- **Epic 0 — Foundations:** 7 / 7 tasks (100%) ✅ — setting named *The Turning* (2026-08-20); household elaboration 2026-08-23 → [[The Other Hands]]
- **Epic 1 — Anchor:** 15 / 15 tasks checked (100% of listed) — clergy orders → [[The Tree-Wardens]] (Story 5.1, names 🟡). Remaining leftover: Conditions cross-link (pending, not a checkbox)
- **Epic 3 — The World Frame:** 🟢 **core done (2026-08-22)** — 4/4 marked: [[The World Frame]] + four continents ([[Maiethorn]] · [[Strandoren]] · [[Heskoren]] · [[The Sundering Isle]]); calendar locked ([[The Reckoning of the Year]] — month-names filled Story 4.2); 4th ancestry ([[Yumboe]]) pulled forward. Map assets baked in (Kumbaan name base ✅ 4.2). Deferred: deep per-region climate/ecology, ~12 named-stub powers (→E7). Rival faiths ✅ Story 1.4.
- **Epic 4 — Cultures & Kinds:** custom ancestries **4/4 ✅**. **Story 4.2 ✅ and 🔒 (2026-08-23, user-approved)** → [[Kinds of the Turning]] · [[Naming People in the Turning]] · months · Kumbaan name base · leaf-colours. Revisit flag on the four ancestries still open (not blocking). Deep grammar + ~12 powers' tongues still deferred.
- **Epic 5 — Factions:** ✅ **COMPLETE (2026-08-23).** Stories 5.1–5.3 done → [[The Tree-Wardens]] · [[The Watchers]] · [[The Book-Hands]] · [[The Door-Keepers]] · [[The Table-Keepers]] · [[The Shore-Sitters]] · [[The Slide]] · [[Tithe-Infrastructure]] · [[The Greens-Keepers]] · [[The Hall-Keepers]] · [[The Stillers]] · [[The Element-Guilds]] · [[The Intake]] (names 🟡, do not rebuild).
- **Epic 6 — History:** ✅ **COMPLETE (2026-08-24).** 8 / 8 of 6.1 🔒; 7 / 7 of 6.2; 6 / 6 of 6.3; 6 / 6 of 6.4. Hub [[The Ages of the Turning]] · lived road [[The Walking Years]] · hinge [[The First Cut]] · residues [[The Years of Hands]] · seeds [[Settlement Seeds]] · fables [[The Child Who Counted Stones]] · [[The Branch That Came Away]] · [[The Child Who Climbed the Stone]]. Names *Brenvaeth / Eoloren / Ornthael* 🔒. Walks, *brenhael*, Cut texture, residue jobs 🟡. Present C.Y. 387 🔒. **Cutter still unpicked.** Nature of her limit still open. Fate-pressure noted, not rolled. **⭐ Next: Epic 7 (settlements) — Story 7.1, name the other powers.**
- **Epic 2 — Society:** ✅ **COMPLETE (2026-08-21).** Frame locked (world scale + register + R2 guard); **all four stories + the naming pass done, core audited.** **2.1 (Law & Citizenship) ✅** → [[Law and Citizenship]]; **2.2 (Economy & the Tithe) ✅** → [[Economy and the Tithe]]; **2.3 (Daily Life) ✅** → [[Daily Life]]; **2.4 (Polity Archetypes) ✅** → [[Polity Archetypes]] (three corners, now named **Vaethorn / Lestrand / Threnmaieth**). **Naming pass ✅** → [[The Old Tongue]] + [[Naming in the Turning]]. Core audit complete → [[Epic 2 Audit Guide]]. **→ Story 4.2 done. Epic 5 complete (5.1–5.3). Epic 6 complete (6.1–6.4). Next: Epic 7 Story 7.1.**
- **Locked decisions:** **setting name (_The Turning_)**, two-layer model, engine, roster, all 10 Condition mechanics, **4 custom ancestries** (Kitsune · Selkie · Tengu · Yumboe), keystone secret (Leaf-Mother real+benevolent **but bounded & costly**), Tree topology (one Awakening Tree + living grafts), **world scale (~15 polities / 3+1 continents)**, **register (late-medieval + Condition-labor advances)**, **world frame (four continents on a reach-gradient: [[Maiethorn]] · [[Strandoren]] · [[Heskoren]] · [[The Sundering Isle]])**, **calendar (High-Solstice Turning-Week + twelve Maiethren months + three new-year's days)**, **five lived faiths** (Motherfaith + Watching / Fair Hand / Old Ways / Open Table — names 🔒), **household cosmology** (she Gives; Other Hands Strike — structure 🔒, Hand-names 🟡), **Kind-hearths not Kind-nations**, hearth-registers ***Kusawe / Sakoa / Gonan***, **leaf-colour table**, **era spine** (two clocks · Grafting as live wave · no universal year-zero · dating reveals stance · *Brenvaeth / Eoloren / Ornthael* 🔒 · C.Y. 387 🔒 · Tree undated · cutter unpicked · limit's nature still open), **First Cut lived** (five attributions uncollapsed · Cutting-leave as captured copy-right · spread inside locked bands · Kumbaan never), **residues lived** (walk's three jobs · Hands can un-Hands · road-past as credit · Heskoren live front · fate-pressure noted not rolled). Epic 5 complete (clergy/guild names 🟡). **Next: Epic 7 Story 7.1 (name the other powers).**

## Links
- [[Build Plan]] — handoff brief (points here) · [[The Premise]] — design hub
- [[The Ages of the Turning]] — Epic 6 hub · [[The Walking Years]] · [[The Child Who Counted Stones]] · [[The First Cut]] · [[The Branch That Came Away]] · [[The Years of Hands]] · [[The Child Who Climbed the Stone]] · [[Settlement Seeds]]
- [[Conditions]] · [[00 - Core]] · [[Conventions]]
