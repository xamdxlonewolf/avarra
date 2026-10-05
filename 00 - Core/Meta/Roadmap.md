---
title: Roadmap
type: moc
visibility: gm
note_status: draft
status: active
tags: [meta, roadmap, build-plan, tracker, moc]
aliases: [The Roadmap, Epics, Build Tracker]
created: 2026-08-17
updated: 2026-10-04
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
| **R** | [[#Epic R: Editorial repair and table readiness]] | Clears every actionable finding in the full editorial audit before new canon is built | **High** | ✅ done (2026-08-31) |
| **0** | [[#Epic 0 — Foundations]] | The load-bearing concept & mechanics | — | ✅ done |
| **1** | [[#Epic 1 — The Engine's Anchor (Turning Tree & Leaf-Mother)]] | Religion, geography, settlements, law, the schism all point back here | **High** | 🟢 core + 1.4 + Conditions cross-link |
| **2** | [[#Epic 2 — Society & Institutions]] | Every settlement & faction inherits these rules | **High** | ✅ done |
| **3** | [[#Epic 3 — The World Frame]] | The physical stage settlements/cultures stand on | Med | 🟢 core + climate/ecology |
| **4** | [[#Epic 4 — Cultures & Kinds]] | Peoples & customs; **4** custom ancestries ✅ · Story 4.2 ✅ · R.3 glance ✅ | Low | 🟢 core done |
| **5** | [[#Epic 5 — Factions & Orders]] | The institutional actors (guilds, Tithe-infra orgs) | Med | ✅ done |
| **6** | [[#Epic 6 — History]] | When did the Trees appear? gives the world a past | Med | ✅ done |
| **7** | [[#Epic 7 — Settlements]] | Concrete stages for play | Med | ✅ done + leftover squares |
| **8** | [[#Epic 8 — People]] | The cast | Low | 🟢 8.1 landed in R.8 |
| **9** | [[#Epic 9 — Secrets & Canon]] | Revelation architecture — runs *alongside* from Epic 0 | — | 🟢 architecture done; still alongside |
| **P2** | [[#Pass two — verification]] | Whole-world consistency, contradictions, gaps, quality — after pass one | **High** | P2.1–P2.4 done 2026-10-05. Endings stay undecomposed |
| **10** | [[#Epic 10 — Campaign]] | Actual play material; needs the world to exist first | — | 🟢 10.1–10.2 done. Endings undecomposed |
| **A** | [[#Epic A — Atlas labels]] | Overlay names on the selected paintings, one sheet per story | Low | ✅ A.1–A.14 done |
| **L** | [[#Epic L — The lived world]] | Soul pass after the build: voices, then faces, then what people do. Empty folders are not a checklist | Med | ✅ L.1–L.9 done 2026-10-03 |
| **S** | [[#Epic S — The other seats]] | The twelve powers whose seats were left unnamed. A city, a town, or a recorded refusal. Maps of those places wait on Epic M | Med | ✅ S.0–S.3 done 2026-10-03. Epic S complete |
| **M** | [[#Epic M — Town sheets and the new seats]] | Sheets for squares that already have streets, then sheets for whatever S seats. Pointers for capitals, large cities, and important towns go on the maps that already show that ground. The ordinary house is Story M.5. Does not reopen A.1–A.14 | Low | ✅ M.1–M.5 done. M.4 pointers 2026-10-05 |

> **Two deliberate departures from the old [[Build Plan]] order:** (1) the **Turning Tree / Leaf-Mother** is promoted *above* the custom ancestries — it's the single highest-leverage anchor, so society/religion/geography get a fixed point to build against. (2) An explicit **"lock the keystone secret"** task sits in Epic 0 — we don't flesh it, just *decide the answer*, because the theme and every reveal need to point somewhere.

---

## Epic R: Editorial repair and table readiness
**Source:** [[Editorial Audit 2026-08-29]] · **Status:** ✅ **complete (2026-08-31)** · **Blast radius:** High. Gate report: [[Epic R Completion Gate 2026-08-31]].

> Work this epic before Epic 8. Each story owns one audited domain. Fix every red, yellow, blue, and white finding. A task may close with a documented decision instead of a change when the audit identifies a real choice, but nothing may close through silence. Preserve the protected strengths in section 3 of the audit. Do not update the world book until the user explicitly asks for a rebuild.

### Story R.1: Core premise and engine ✅ **DONE (2026-08-30)**
- [x] Reconcile the population model in [[The Premise]] so Given, Struck, Both-path sub-splits, and Kept total cleanly; decide whether The Unbound is included within Bound's share *(2026-08-30: Unbound is inside Bound's ~5%; Returned ~7%; Both-path Struck ~1% of all people each. Engine 60/15/25 unchanged.)*
- [x] Make [[The Premise]] the single canonical source for population figures; replace duplicated figures elsewhere with links or clearly derived summaries
- [x] Propagate the settled arithmetic to [[Conditions]], [[Law and Citizenship]], [[Economy and the Tithe]], and [[Build Plan]] without weakening the locked Given / Struck / Kept engine

### Story R.2: Condition mechanics ✅ **DONE (2026-08-30)**
- [x] Replace The Stilled's incorrect `Restrained` usage with a distinct effect, then add an appropriate roll or resource gate to Gaze — **Stilled** is a special condition (no actions/reactions); unwilling Gaze is an attack roll (Instinct or Presence)
- [x] State explicitly whether [[Returned]] loses the core Avoid Death move and make Refuse to Fall's relationship to the remaining death moves unambiguous — **Avoid Death is off the list**; options are Blaze of Glory, Risk It All, Refuse to Fall
- [x] Standardize all Tithe clock drains to `long rest` unless a card deliberately needs different timing — Long-Lived / Answered / Taken-In / Stilled tick on long rest; Far-Voiced, Two-Bodied, Bound, Phoenix keep their own triggers
- [x] Add the missing damage die, trait, and other required weapon fields to the [[Two-Bodied]] natural weapon — Primary · Instinct or Strength · Melee · d8 phy (d6 / d10 by size) · One-Handed · Natural
- [x] Rebalance [[Phoenix]] or add firm spotlight and party-consent guidance for its immunity, flight, Evasion, attack, and extra death move package — **both:** other-four-players consent; Evasion once per rest; Rise clears HP not Stress; fire immunity kept (user lock, Condition Audit #10)
- [x] Preserve the one-true-Phoenix rule while resolving the apparent second Phoenix: determine when the captive's original self ends, how harvested fire sustains what remains, and why a new white-fire Gift can fall unseen by the wider world — 🔒 [[When the Fire Is Caught]]: Gift ends at the death they cannot Rise from; harvested fire keeps a remnant, not a second Phoenix; new leaf may fall unseen. Harvesters stay R.7
- [x] Narrow [[The Unbound]] mind-lane immunity and distinguish Quiet tokens from both that immunity and Returned's unshaken clause — Absence = Stress-marking (or Fear) through the hole only; Quiet spends to act through it; unshaken stays corpses/gore/deathly places
- [x] Rebalance [[Long-Lived]] so its boon and severe low-token penalties occupy the same power band — always-on recall advantage; Hope for complete recall; fade is targeted; starve is Stress then HP, not an unclearable spiral
- [x] Give [[The Answered]] a mechanic that expresses being spoken to rather than commanded — **Spoken, not commanded** (one ask per long rest; element refuses another master)
- [x] Reduce mixed-party token bookkeeping and replace fuzzy refill tests where a cleaner trigger can carry the same fiction — yes/no rest checklist on [[Conditions]]
- [x] Decide whether and how Condition cards advance from levels 1–10; record a deliberate no-scaling rule if that is the answer — 🔒 **no level scaling**; Two-Bodied Experiences / once-ever second signature stay flavor; Proficiency dice still rise

### Story R.3: Custom Kinds ✅ **DONE (2026-08-30)**
- [x] Resolve the three-feature power gap against stock two-feature ancestries by trimming custom Kinds or granting a bounded compensating hearth benefit to stock-ancestry characters — **kept the locked three-feature packages**; stock (and stock-and-stock mixes) take a [[Kind Heritage|Hearth-Mark]] (once/session +2, no Hope, place-phrase)
- [x] Write the mixed-ancestry ruling, including how custom three-feature packages combine with SRD heritage rules — **SRD mix allowed** (Top + Bottom; hearth feature not mixed; no Hearth-Mark if any custom feature is taken). [[Yumboe]] excluded: GM leave, full Kind only. → [[Kind Heritage]]
- [x] Consolidate the repeated "cannot be caught off guard" immunity so the four Kinds retain distinct mechanical lanes — keyword **once**, on [[Tengu|The Mountain's Mood]] (environment/terrain only); [[Selkie|Seal-Kin]] names the approach; [[Yumboe|Hollow-Hill]] is tremor-sense
- [x] Fix stale claims in [[Selkie]] and [[Tengu]], and reconcile Fox of the Sands' "many-tailed" epithet with [[Kitsune]] canon — four customs, three features each; Sands is the huge-eared fox; nine-tails stay honorific
- [x] Explain how dispersed Kind hearths transmit culture without becoming Kind-nations — **the other kitchen** (fox-summer / another strand / other perch / hill-feast). → [[Kinds of the Turning]]
- [x] Address mixed-Kind children in the setting's layered identity model — mainland mixes **allowed** as the SRD; register from a Kind you wear; byname follows place; [[Yumboe]] GM-leave and unmixed

### Story R.4: Religion and the Turning Tree ✅ **DONE (2026-08-30)**
- [x] Add a scannable "Questions a warden gets asked" section to [[Turning Tree]] covering missed solstices, refusal, orphans, adults who never Turned, whether the rite can repeat, and other likely backstory cases
- [x] Settle Leaf-Fall failure and edge-case procedure without confirming the Leaf-Mother in player-facing text
- [x] Add one restrained point of religious dread, using the Phoenix fall or a historical mis-Speaking without moving the setting above its 5% scary dial → [[The Wrong Green]]
- [x] Give each Other Hand a positive want; state what Orledd receives in a Bound bargain and what strains or breaks the Leaf-Mother's allowance → [[The Other Hands]] · [[Bound]]
- [x] Turn the Open Table's sentence-that-will-not-travel into a visible table conflict instead of leaving it buried in an order note → [[The Open Table#The sentence at the mainland lintel]]

> **R.4 recorded decisions (did not change the locked engine).** The Given-door stays one week in the tenth year ([[The Walking Years]]). A completed standing (colour or hug under sound wood) is once. A miss, refusal, or unsound Tree that spends the week makes a child **unTurned**, not Kept, and does not unlock next year. Struck remains the later mercy. Some Kept are past her reach *this turning*; she does not tell them apart, and a later week is not offered to sort them. Player-facing text does not confirm her. The dread is a human mis-Speaking, not an eerie Tree. Other Hands wants and allowance failure stay GM-only. No Kumbaan mission; the Open Table fight is a mainland lintel.

### Story R.5: Secrets and revelation ✅ **DONE (2026-08-30)**
- [x] Move the keystone truth leaks in [[Turning Tree]], [[The Leaf-Mother]], and the affected faction notes beneath proper `## GM Notes` walls — Tree blockquote + hug-as-locked-kindness; Mother design-note; ten injustice "Confirming she is real" paragraphs; Yumboe household sentence; Faiths pantheon dump; Law "keystone pattern"
- [x] Reduce `leaf-mother-is-real` to notes that truly expose confirmation, introduce a lighter adjacent tag if useful, and key `the-other-hands` to every player note that exposes it — `leaf-mother-is-real` is the keystone's `reveal_tag` only; clue notes take `keystone-adjacent`; household GM walls take `the-other-hands`. Vocab on [[Conventions]] and [[11 - Secrets]]
- [x] Populate `foreshadowed_by` on [[Is the Leaf-Mother Real]] and repair the Secrets MOC so clue-bearing notes can be found
- [x] Build a usable firing pin for the keystone: one confirmable artifact, a faction that wants proof found or suppressed, and concrete consequences if confirmation lands → [[The Spent Leaf]] · [[The Remainder]] (desk split: bury / walk) · [[Is the Leaf-Mother Real#If confirmation lands]]
- [x] Review all six clue rungs so the reveal can fire in play while preserving deniable early clues — rungs 1–5 stay deniable; rung 6 is the Spent Leaf during a Giving, not "reserve this"
- [x] Add a lesser household deity that accepts the Long-Lived sect's worship and invented mask while letting the sect believe it created the god; keep it outside the Five Hands and unable to Give or Strike → [[The Unspent]] (everyday *the Poured God*). Sect stays R.7

> **R.5 recorded decisions (did not change the locked engine).** She is still real, benevolent, bounded, and costly. The Given-door is still one week; a completed standing is still once; unTurned is still not Kept. The Five Hands table is unchanged. The Unspent is furniture, not a sixth door. Confirmation can fire and still does not sort the Kept, name the Other Hands, explain the limit, or launder injustice (R2). World book untouched. Strip rule: [[Conventions#Player-safe export]].

### Story R.6: Society, law, and economy ✅ **DONE (2026-08-30)**
- [x] Correct the licence-rate claim and decide how a 28–33% licensed or supervised population still avoids becoming a general surveillance system — ticketable pool (Stilled + Far-Voiced + Answered) ≈ 29% of people; a ticket names a hazardous *use*, not a Condition; Bound is a table, not a fourth body-licence; three guilds, no shared roll; state watches the charter. → [[Law and Citizenship]]
- [x] Soften the claim that Tithe-provision rivals food or fuel, or demonstrate the transaction volume that makes the claim true — **softened:** civic utility like wells, not grain. Self-paying vocation ~35%; purchased/civic customers ~a seventh, concentrated in stone towns. → [[Economy and the Tithe]]
- [x] Define big-city Turning and witnessing procedure for settlements where communal memory cannot know every child — **hearth-stand:** nested witness (street / quay-gang / courtyard); week-slate is hours, not gifts. → [[Law and Citizenship]] · [[Turning Tree#Turning-Week in a city]]
- [x] Define legitimate travel and vouching customs so rootless adventurers can cross jurisdictions without routine arbitrary harassment — road-word, company-vouch, guild-mark, guest-right, walk-custom; watch asks name / last hearth / who stands (two will do). → [[Law and Citizenship#How a traveler stays vouched]]
- [x] Add a crime, watch, hearing, and punishment ladder that fits witnessed citizenship and the Inviolate Will doctrine — neighbour-word → watch (hold till morning) → guild-hearing → open hearing; exile from the hearth is the civic death; no Condition-crime. → [[Law and Citizenship#Harm, the watch, and the hearing]]
- [x] Resolve why enough Taken-In live in stone cities to sustain urban green-poverty and the Slide's customer base — Given here, harvest-hands, lot labor, rare city-doors, lot-hour trap. Arm's length is manners, not absence. → [[Economy and the Tithe#Why Taken-In live in stone cities]]
- [x] Chain or separate Netstrand berths, White Note terms, and Orentel holds so the prestige-walk product is not triple-booked — **chained:** [[Netstrand]] hulls → [[The White Note House]] terms → [[Orentel]] holds; [[Orenbren]] houses the origin-winter, does not sell the berth.

> **R.6 recorded decisions (did not change the locked engine).** Citizenship is still witnessed, not recorded. No universal register. The Given-door is still one week; a completed standing is still once; unTurned is still not Kept. Tickets are still guild-issued for the three hazardous uses (Stilled, Far-Voiced, Answered). Bound is still a table. The Watchful census is still the aberration. Tithe-provision is a real sector and is not food. World book untouched. Sold vouching and the Given-Over pipeline later received lived faces in R.7. Table procedures: [[At the Table]].

### Story R.7: Factions, institutions, and conflict ✅ **DONE (2026-08-30)**
- [x] Give the Given-Over pipeline and sold-vouching trade named lived faces with motives, methods, limits, and ways they reach the party → [[The Holding Desk]] (Mutelo) · [[The Standing Trade]] (Nomele)
- [x] Give Threnmaieth three or four named instruments, including a registrar, Reckoned Speaker, and channel-clerk, with distinct good-faith agendas → [[The Reckoned Offices]] (Menirein · Tarvae · Videm · Sirtal)
- [x] Unlock two or three inter-faction disputes and let at least one escalate on-screen; remove instructions that prevent useful contact or disagreement — Watchers/Door-Keepers (Vaelun grove can leave the meal); Book-Hands/Holding Desk (same Bound, same week); Tithe-Infrastructure/Slide (official door closes on purpose). Tarvae vs Rithim also live
- [x] Add a compact want / have / fear / live conflict / hooks block to each faction that needs table-facing retrieval
- [x] Break the shared faction-note voice and structure so at least one order is sprawling, one is terse, one is bureaucratic, and one is paranoid — Tree-Wardens appendix · Intake shed-memo · Tithe-Infrastructure forms · Watchers second-guess
- [x] Decide whether [[The Greens-Keepers]] and [[The Hall-Keepers]] remain factions; if not, fold their jurisdictions into [[Tithe-Infrastructure]] — **folded**; stubs kept so aliases survive
- [x] Keep each faction's injustice real while removing prohibitions that make opposition unable to act — Slide / Holding Desk / Standing Trade prefer not to ruin an asset; preference is not a lock
- [x] Build a fringe Long-Lived religious sect around volunteered five-year sacrifice, shared blood-memory, and knowledge passed to a god the sect falsely believes it created; make withdrawal possible but socially costly → [[The Pourers]] wearing [[The Unspent]]
- [x] Build the former Kept empire and its surviving walled regime as political class rule, not another church: the Book of Tithes assigns taxes, restrictions, and labour while Kept heirs can lose status if Given → [[The Walled Book]] (Inner Close inside [[Orenbren]], not a sixteenth flag)
- [x] Build the Protectors as secret Phoenix worshippers who remove each Phoenix from public life, cause controlled deaths, harvest Phoenix Fire, erase the deaths from the Phoenix's returning memory, and turn accumulated fire into institutional power → [[The Protectors]]; engine stays [[When the Fire Is Caught]]
- [x] Keep the three opposition engines distinct: religious self-consumption, political classification, and worship used to hide coercive extraction — Pourers / Walled Book / Protectors; do not share a cellar

> **R.7 recorded decisions (did not change the locked engine).** No sixteenth great power. **Inner Close placement 🔒 Story R.10** — stays inside [[Orenbren]]; do not replace [[The Hinge Shore]] as a power. The First Cut war stays unwritten; folk memory that the old untithed sat on the grove is a light seed only. Protectors use the locked Phoenix engine and never force a PC Rise. Greens and halls are doors, not colleges. Three opposition engines stay distinct from Threnmaieth's instruments and from the Remainder. R.8 seeds are named, not plotted: [[Reimaethe]] · [[Hithaen]] · [[Taeren]] · [[Rosire]]. A Standing Trade recanter stays unnamed. World book untouched.

### Story R.8: People and capital casts ✅ **DONE (2026-08-30)**
- [x] Build the planned 4–6 positional pivots from existing offices, each with a non-Tree want, leverage created by their job, and a distinct character arc — **six:** [[Vaethod]] · [[Rithim]] · [[Mataero]] · [[Thilim]] · [[Laevila]] (Grown-Over) · [[Tesara]] (Intake). Hub [[People of the Turning]]
- [x] Give each of [[Eolvaeth]], [[Orentel]], and [[Maiethlir]] three to five named wants carried by people rather than institutions — Eolvaeth 4 · Orentel 5 · Maiethlir 4
- [x] Connect the cast across capitals, factions, and disputes without turning them into a preassembled adventuring party or another row of document-holding clerks — paper / beds / pots / one Eolthael; not a crew
- [x] Seed four later campaign-facing roles without fully plotting them here: a sacrifice volunteer who wants out, a disinherited Given heir of the Kept regime, a hidden second Phoenix, and a Protector who helped that Phoenix escape — [[Reimaethe]] · [[Hithaen]] · [[Taeren]] · [[Rosire]]. Houses exist ([[The Pourers]] · [[The Walled Book]] · [[The Protectors]]); do not plot the openings. Hidden-Phoenix PC: [[A Hidden Phoenix]]; campaign opening stays Epic 10

> **R.8 recorded decisions.** Offices became people; seats were not rebuilt. Two clocks: Thilim and Laevila walked (different jobs of *I walked*); Mataero thinks the wave is over; Vaethod still sends; live front pointed at Haelin, not cloned. Seeds are mouths, not factions. Given-Over broker and Threnmaieth instrument-set landed in R.7. World book untouched. Stories R.9–R.13 ✅. Epic R closed. Next: Pass two · P2.1.

### Story R.9: History ✅ **DONE (2026-08-30)**
- [x] Add three to five dated non-Tree events within C.Y. 0–387, including inter-power conflict and a mix of political, epidemic, and natural events — **five:** [[The Closing]] (C.Y. 19–38, war) · [[The Two Papers]] (C.Y. 67, political) · [[The Grey Summer]] (C.Y. 171, epidemic) · [[The Thaw-Break]] (C.Y. 233, natural) · [[The Hinge Hush]] (C.Y. 304, treaty after inter-power war). Hub [[The Other Count]]
- [x] Add two or three pre-Walk physical survivals that support archaeology and play without dating the Tree — [[The Low Wall]] · [[The Seeing-Ring]] · [[The Dry Stair]] (uncounted; adventure-depth stays R.11)
- [x] Give the fifteen powers enough shared history for current borders, treaties, dynastic claims, and grudges to have causes — table on [[Powers of the Turning#What they remember (the Other Count)]]; each stub and the three corners carry a remember-line
- [x] Re-date Ledan's White Note query to C.Y. 280 and repair every dependent "200th summer" reference — query archival; Ledan [[Long-Lived]]; present house-year **307**; Threnmaieth crown-count from C.Y. 67 (present Crown-year **320**)
- [x] Keep the two-clock model intact while proving that 387 years contained more than the spread of grafts — clocks stay; Other Count sits beside
- [x] Make the First Cut the break in the old empire's monopoly on access to the Awakening Tree, then place the resulting war, imperial collapse, and retreat behind the surviving walls without identifying the cutter — Closed Seat / Grove-Sitters; war [[The Closing]]; remnant [[The Walled Book]]; cutter unpicked

> **R.9 recorded decisions (did not change the locked engine).** Two clocks stand. Tree undated. Cutter unpicked. No sixteenth power. Closed Seat was an *origin-gate*, not a world-empire. Four monopolies from one fall (wood / beds / later list / rank). Crown-count starts at the Two Papers. Ledan is Long-Lived; 200th summer = C.Y. 280. Common-tongue names only (Closed Seat, Other Count, five years, three leftovers). Terrain names ✅ Story R.10 → [[Named Ground]]. Adventure-site depth stays R.11. World book untouched.

### Story R.10: Geography and powers ✅ **DONE (2026-08-30)**
- [x] Name the inner sea, central range, and three or four rivers used by existing settlement and history notes — **the Old Crossing** · **the Rain-Wall** (Lirorn: *the Thaw-Wall*) · **the Core-thaw** · **the Well-wash** · **the Rise-water** · **the Chart-run** (+ **the West Water**, Noon Pass, Shelf-gate). Hub [[Named Ground]]. Seed `20260831`, mid-list. No new liturgy
- [x] Add a compact travel-time table derived from established walk durations and place the current settlements relative to it — day's walk = mile-shrine; Near Mile 3–12 days · Salt Walk 3–5 days' sail + inland · Long Mile 6–12 weeks. Table on [[Named Ground#Travel times]]
- [x] Remove map-generator tooling as an authority inside player-facing geography; extract the tooling to `14 - Assets` and link to it as a production aid — `14 - Assets/Maps/Map Generation Tooling.md`. Continents no longer cite Azgaar as terrain
- [x] Align [[The World Frame]] with [[The First Cut]] on the strict ruling that no Kumbaan graft ever took — wobble removed; wrecked pots allowed; a taking is not
- [x] Sharpen or consolidate the weakest power stubs, especially the Hinge Shore, Lirorn, and Netstrand, without adding more powers — Hinge Shore *classifies* (not Lestrand-lite) · Thaw-Land is last-year's-snow-as-civic-year · Night Shore watches for hulls that do not arrive. No sixteenth
- [x] Decide whether the surviving Kept regime replaces a weak existing power such as the Hinge Shore or survives inside the successor of its fallen empire; do not add a sixteenth great power — **🔒 inside [[Orenbren]]**. Closed Seat sat the grove; Retreat is a day's walk from the Motherwood. The Hinge Shore stays the hinge of a different war
- [x] Produce a finished canonical visual map after physical names, borders, climate regions, and travel relationships are settled — [[The Known Map]] (labelled SVG) + [[The Atlas Sheets]] (paintings) + prompts in [[Map Generation Tooling]] (W · C1–C4 · R1–R8)

> **R.10 recorded decisions.** Common-tongue first. No new liturgy (phonology repaired in R.12). Kumbaan never. Inner Close stays in Orenbren. Fifteen still fifteen. SVG = placement; paintings = terrain feel; world-sheet extra isles are not canon. World book untouched. **Stories R.11–R.13 ✅.** Epic R closed. Next: Pass two · P2.1.

### Story R.11: Settlements and Kumbaan ✅ **DONE (2026-08-31)**
- [x] Break the Eolvaeth / Ornsael near-clone by changing one settlement's physical problem, institutional response, cast shape, and mystery — **Ornsael:** well dropping (not maybe-Tree); well-share (not warden-won't-invent-colour); Theisva / Lesna / Bovaer; wet knot below the water. [[Eolvaeth]] keeps spring, maybe-Tree, wet leaf, Vaethod
- [x] Vary the one-NPC / one-document / one-blindness formula across all seven developed settlements — Harrow's = a day + two mouths (Haelin / Tora) · Hamlets = three named kitchens · Third Hearth = a made bed + Meirim · Ornsael = well-gang · Eolvaeth = conflict walks in · Orentel = slate and crane · Maiethlir = two hands on one slip + a river
- [x] Turn [[The White Note House]] from a cross-reference ledger into a usable place or institution — rooms, a day's work, how you get a term, [[Ledan]] in the room
- [x] Make an explicit Kumbaan commit-or-gate decision in the Roadmap — **committed for play**
- [x] If Kumbaan is opened for play, add one settlement, one Table-Keeper, crossing rules, and session-facing wants unrelated to guarding a reveal — [[Ndenjoo]] · [[Njunda]] · [[The Sundering Isle#How a crossing works]] · wants: Nolas / Soonke / Saalo (not a keystone vault)
- [x] Add two or three adventure sites, including pre-Walk ruins, with entrances, pressures, discoveries, and links to current actors — [[The Low Wall]] · [[The Seeing-Ring]] · [[The Dry Stair]]
- [x] Preserve the best ground-level texture while making each settlement retrieve its conflicts quickly at the table — cup, Seine's bed, wet leaf kept; **At the table** headers on all seven + White Note + Ndenjoo + three leftovers
- [x] Give capitals and wild settlements dangers that can enter a scene, not only social conditions that remain in exposition — cohort / stone-day / cup / well-mouth / crane / thaw-flood / wreck; wilderness rolls → [[Dangers of the Turning]]

> **R.11 recorded decisions (did not change the locked engine).** Two clocks stand. Tree undated. Cutter unpicked. No sixteenth power. No Kumbaan graft (strict never). Given-door still one week; a dry well is not a second-chance year. **Kumbaan committed:** one hall, table-at-the-centre, crossing as a dial not a ferry. Session wants are hospitality and the wall, not a reveal. Ornsael is the clone-break; Eolvaeth's leftover stays devotion. White Note stays terms, not holds or hulls. Adventure leftovers still do not date the Tree. Named terrain ✅ R.10. Wilderness rolls: [[Dangers of the Turning]]. World book untouched. **Stories R.12–R.13 ✅.** Epic R closed. Next: Pass two · P2.1.

### Story R.12: Language, naming, and voice ✅ **DONE (2026-08-31)**
- [x] Repair [[The Old Tongue]] to license its real consonant clusters and `ai`, state compound stress accurately, correct Worn-drift, and fix the Maethaem / Reimaethe samples
- [x] Promote common-tongue epithets as primary spoken handles and adopt the rule "speak the common name; write the liturgical name"
- [x] Retire or respell the worst collisions, beginning with Aeloren and Eolstrand; add roots before any future liturgical coinage
- [x] Freeze new liturgical names until the phonology and collision list are repaired
- [x] De-clone at least two fables; demote, replace, or substantially rewrite [[The Child Who Climbed the Stone]]
- [x] Break one faith, one guild, one fable, and one settlement out of the shared aphoristic template
- [x] Cap recurring editorial mantras such as R2 and "both are telling the truth" to one authoritative home
- [x] Store a reproducible name generator and algorithm, or delete seed and "re-run" language from canon notes

> **R.12 recorded decisions (2026-08-31).** Speak the common name; write the liturgical name. New liturgical coinage is frozen; crowded root families are closed. *Aeloren* and *Eolstrand* are retired; [[The Hinge Shore]] remains one of the fifteen. [[The Child Who Climbed the Stone]] is now the square-game *Here and Far*; [[The Child Who Counted Stones]] is a road-song. [[The Fair Hand]], [[The Element-Guilds]], and [[The Three Hamlets Past the Ford]] no longer share one essay template. The social guard has one canonical home in [[Is the Leaf-Mother Real]]. Reproducible naming tooling lives under `14 - Assets/Names/`. World book untouched. Story R.13 ✅.

### Story R.13: Vault hygiene and table readiness ✅ **DONE (2026-08-31)**
- [x] Rewrite [[Build Plan]] as a true fast brief; correct the Condition and ancestry counts, include The Unbound, remove stale contradictions, and drop the `Roadmap` alias — alias is now `Handoff Brief` only; 9 selectable + Unbound; 4 ancestries
- [x] Resolve all 19 `note_status: locked` values into the documented vocabulary and record the chosen finished-state convention — vault held **15** (`locked` notes); all → `canon`. Convention recorded on [[Conventions]]. Roadmap 🔒/🟡 stays a tracker tag
- [x] Decide player-safe visibility for the Condition hub and cards so usable player mechanics are not stripped from exports — hub + 10 cards `visibility: player`; secrets stay in GM Notes / `11 - Secrets`; `reveals` empty unless the player body confirms
- [x] Fill the `09 - Creatures` MOC, archive [[Rogue House Options]], and fix or remove the opaque "fourteen-cell catalogue" claim — MOC filled; Options → `99 - Archive`; fourteen-cell cut
- [x] Write the exact player-export strip rule into [[Conventions]], including how nested GM material and blockquotes are handled — [[Conventions#Player-safe export]]
- [x] Move seeds, story numbers, canon emoji, "do not clone," and similar production scaffolding out of player-facing bodies — power stubs, seats, leftovers, gazetteer, Kind Heritage, People hub; R.12's phonology and spoken-handle work kept
- [x] Create an "At the Table" note covering character-creation timing, the Kept benefit or deliberate tradeoff, Struck-in-play acquisition, Kind + Condition stacking, advancement, travel papers, city witnessing, crime procedure, and Leaf-Fall edge cases — [[At the Table]] (Kept = empty clock, deliberate tradeoff)
- [x] Build a small Daggerheart dangers layer with wilderness adversaries and hazards for the Long Mile, Heskoren, and other named travel routes — [[Dangers of the Turning]] + five adversaries
- [x] Define player-agency rules for a hidden Phoenix PC: starting Hope scars, missing murder memories, fragment recovery, what the Protectors' stored fire can reveal, and which truths remain player choices — [[A Hidden Phoenix]]

> **R.13 recorded decisions (did not change the locked engine).** `note_status` is stub / draft / fleshed / canon only; `locked` is retired. Condition cards are player-visible mechanics. Kept get no consolation Condition. Struck-in-play is opt-in. One Gift still one Gift. Hidden Phoenix is a seat on the existing card, not a second card. Dangers are beasts, leftover hospitality, unfinished weeks, and dead wood — not a second monster taxonomy. World book untouched. Stories R.1–R.13 ✅. **Epic R closed 2026-08-31.** Next: Pass two · P2.1.

### Epic R completion gate ✅ **DONE (2026-08-31)**
- [x] Every non-green finding in [[Editorial Audit 2026-08-29]] maps to a completed task or a recorded decision with rationale — map on [[Epic R Completion Gate 2026-08-31]]
- [x] Protected strengths from audit section 3 remain intact except for necessary arithmetic corrections — checklist on the gate note
- [x] Player-facing export contains no keystone confirmation or production scaffolding — **keystone pass.** Remaining Story-number / 🟡 / "Do not clone" in working-note bodies is **recorded residual C-01**, owned by [[#Pass two — verification|P2.1]], not a silent close
- [x] Core arithmetic, links, front-matter vocabulary, and Daggerheart rules terms pass a fresh mechanical audit — §4 of the gate note
- [x] Table test can create a Kept or Conditioned PC, travel to a city, meet an active conflict, and face a runnable danger without inventing missing procedure — Infernis + Bound stacking written this gate
- [x] Update [[Build Plan]] and this Progress section, then begin pass-two verification before resuming the old Epic 8 plan — log: [[Contradictions]]

> **Gate recorded decisions (2026-08-31).** Remaining scaffolding is P2.1, not Epic R unfinished. Infernis + Bound stack. Thuda stays an on-page mouth. Haelin is an alias of [[Harrow's Green]]. World book stays stale until an explicit rebuild. Locked engines stand. Do not start Epic 10.

---

## Pass two — verification
**Skill:** `story-sense` (router) · `worldbuilding` · **Status:** **P2.4 complete 2026-10-05.** P2.3 contradiction sweep the same day. P2.2 complete 2026-10-02. P2.1 complete 2026-08-31. **Blast radius:** High. Pass one is complete. Do not resume the old Epic 8 plan. Do not reopen P2.1 or P2.2.

> A review sweep of the whole world for consistency, contradictions, gaps, and quality. Log and resolve under [[Contradictions]]. The bible stays this vault. Do not invent a parallel `world-bible/` tree. Do not update the world book unless asked. Hub collisions found while writing the opening are logged and fixed on that log (C-05).

> A review sweep of the whole world for consistency, contradictions, gaps, and quality. Log and resolve under [[Contradictions]]. The bible stays this vault. Do not invent a parallel `world-bible/` tree. Do not update the world book unless asked.

### Story P2.1: Residual export polish ✅ **DONE (2026-08-31)**
- [x] Move remaining Story numbers, "Canon status" blockquotes, and "Do not clone / Do not rebuild" out of player bodies of history, faction, settlement, and MOC notes (under `## GM Notes`)
- [x] Decide whether 🟡 on liturgical names stays in player text (taste-open) or moves with the rest — **option 2:** names stay visible; markers and taste-open status move under `## GM Notes`; no name locked or changed
- [x] Leave the compiled world book untouched unless the user asks for a rebuild

> **P2.1 recorded decisions.** C-01 is resolved. C-04 stays taste-open without player-facing status marks. C-03's skill links are plain code text; atlas embeds remain GM production aids because their PNG files are not tracked. C-02 was decided as no rebuild without an explicit request; **the user asked (2026-08-31)** and the compiled book was rebuilt. Stop here; later pass-two stories remain undecomposed.

### Story P2.2 — Plain prose ✅ **DONE (2026-10-02)**
The notes had picked up a writing habit: facts hidden in riddles, and the labels "Inscrutable," "leave it," and "20%." The user asked for an audit so the notes sound like normal sentences. The facts stay. A habit people will not explain stays unexplained. The sentence that says so has to be ordinary. Rule: [[Conventions#Plain prose]].

- [x] Write the rule in [[Conventions#Plain prose]]. Point `memetic-depth` in `CLAUDE.md` at that rule, so a later pass does not put the labels back.
- [x] In vault notes, replace those labels with the same fact in an ordinary sentence. Do not explain the heel, the salt, the wet leaf, the loud thaw, the fourth-fox word, or the Fungril spoonful. Do not turn any of them into a power, a relic, or a rite.
- [x] Rewrite the stock kitchens on [[Kinds of the Turning]] in ordinary sentences. The nine groups, where they are common, and what they do not own stay as written in L.6.
- [x] Do not update the world book. Do not open L.7, Epic S, or Epic M.

> **P2.2 recorded decisions (2026-10-02).** Plain prose is the note voice. Unexplained habits stay unexplained, and they are written as what people do. The compiled world book still has the old sentences. It was not rebuilt. L.7 was not opened.

### Story P2.3 — Contradiction sweep after L, S, and M ✅ **DONE (2026-10-05)**
Read the world again now that Epics L, S, and M are in. The new seats, their people and habits, the close plates, and the pointers on [[The Known Map]] and the overlays. If a painting and a note disagree, the note wins. Do not redraw a map. Log on [[Contradictions]]. Resolve in the home note when the locked spine already decides it. If two locked decisions conflict, log that and stop. Do not silently pick.

- [x] Read [[Contradictions]] first. Leave C-01 through C-06 and R-01 through R-04 resolved. Do not reopen P2.1 or P2.2.
- [x] Read the Epic S seats, their people and habits, the close plates, and the pointers.
- [x] Where a painting and a note disagree, the note wins. Do not redraw a map. Log the finding. Resolve it in the home note when the locked spine already decides it.
- [x] If two locked decisions conflict, log that and stop on that item. Do not silently pick.
- [x] Do not invent a parallel world-bible. Do not generate a new power, faith, tongue, or liturgical name. Do not update the world book. Do not reopen M.4 or M.5.

> **P2.3 recorded decisions (2026-10-05).** C-07, C-08, and C-09 are on [[Contradictions]]. Rothallo's painted square stays town-scale; the note says capital. Natai's placement is the schematic, west of Harrow's; the overlays that put the name east were not redrawn. Larbril is the meeting of the west road and the Well-wash, not a west bank; the dot was not moved. Living notes that still said "unnamed seat" or "not a capital" were corrected. Habit counts and people matched the grill. The world book was not rebuilt. No map was redrawn.

### Story P2.4 — Thin-spot pass on what the sweep touched ✅ **DONE (2026-10-05)**
`story-sense` on the notes P2.3 touched. Fix a note only when that diagnosis says the note is thin. If nothing is thin, write that down. Do not reopen P2.2.

- [x] Run `story-sense` on the seats, people, close-plate labels, and pointer notes the sweep touched.
- [x] Fix a note only if the diagnosis says it is thin. If nothing is thin, write that down.
- [x] Do not reopen P2.2. Do not put "inscrutable," "leave it," or "20%" back into a note. Do not explain the heel, the salt, the wet leaf, the loud thaw, the fourth-fox word, or the Fungril spoonful. Do not turn any of those into a power, a relic, or a rite. Do not fill an empty folder. Plain prose, per [[Conventions#Plain prose]].

> **P2.4 recorded decisions (2026-10-05).** The seats already have a way in, a job, a tension, and the mouths the grill allowed. `story-sense` reads the sweep's trouble as stale sentences, not a world without a street. No note was thickened. The unexplained habits stay unexplained. Written on [[Contradictions]] beside the sweep.

### Later (do not decompose until asked)
- The campaign's close — [[#Epic 10 — Campaign]]. Endings stay here until asked. Not a return to the old Epic 8 roster plan.

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
**Skill:** `belief-systems` (+ `oblique-worldbuilding` for in-world texts, `paradox-fables` for the schism folklore) · **Status:** 🟢 **core done (2026-08-19); Story 1.4 done (2026-08-23); Conditions cross-link leftover done (2026-08-31); clergy → Stories 5.1–5.2 (2026-08-23)** — Tree + Motherfaith + the other four faiths written; working houses built. · **Blast radius: High.**

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
- [x] Tree/Leaf-Mother notes declare `reveals:` (R.5: player bodies that only clue take `keystone-adjacent`; `leaf-mother-is-real` is the keystone's own tag)
- [x] Cross-linked from [[The Premise]], the [[07 - Religion]] & [[11 - Secrets]] MOCs
- [x] Conditions hub and cards cross-link to Tree colours, faith readings, and civic next-steps *(2026-08-31 leftover)* — derived palette on [[Conditions]]; each card has At the Tree / Away from the Tree. Palette still lives on [[Turning Tree]]

> **Deferred out of Epic 1 (tracked):** Clergy orders ✅ Story 5.1 ([[The Tree-Wardens]], names 🟡). Other houses' orders ✅ Story 5.2. Colour palette ✅ Story 4.2 · Calendar ✅ Epic 3 · faith economy ✅ Epic 2 · wider pantheon ✅ Story 1.4. Conditions cross-link ✅ 2026-08-31.

### Story 1.4 — Wider pantheon / other religions ✅ **DONE (2026-08-23)** → [[Faiths of the Turning]]
- [x] 🟡 The Leaf-Mother is *one faith among several* — four lived rival faiths built against the Epic 3 continental seeds, plus how they coexist / syncretize / fight. **Not** a D&D god-list; no second cosmology locked. → [[The Watching]] (*Haelthael*, Maiethorn) · [[The Fair Hand]] (*Leddoren*, Strandoren) · [[The Old Ways]] (*Vaeloren*, Heskoren) · [[The Open Table]] (*Ndeyaan*, Kumbaan) · shared paradox-fable [[The Child at Four Doors]]

---

## Epic 2 — Society & Institutions
**Skill:** `governance-systems`, `economic-systems` · **Status:** ✅ **complete (2026-08-21)** · **Blast radius: High.**

> The payoff epic: *how does a civilization work when 3 of 4 people carry a Tithe?* Every settlement & faction inherits these answers, so it comes before the specific places.

> **Frame locked before starting (2026-08-20 — see [[The Premise]]):**
> - **Scale:** ~15 large polities across 3 large + 1 small continent. Epic 2 builds the **universal social physics** + **2–3 polity archetypes**; the rest are named-stubs deferred to Epic 3/7.
> - **Register:** late-medieval burgher surface (no print, no gunpowder); the *only* advancement beyond comes from **Condition-labor** — legible, concentrated, paid-for by Tithes.
> - **Social guard (from the keystone):** the Leaf-Mother's benevolence is *cosmological, not social* — do **not** let it launder injustice. Struck stigma, Tithe-infrastructure-as-leverage, guild conscription are **real frictions to keep**, not misreadings to dissolve.

### Story 2.1 — Law & citizenship (`governance-systems`) ✅ **DONE (2026-08-20)** → [[Law and Citizenship]]
> **Core design call (user, 2026-08-20): citizenship is _witnessed, not recorded_.** No universal register (that was too invasive for a ~5%-scary world). You belong because your town *watched you Turn*; proof-at-a-distance runs through **vouching people** (Long-Lived memory / Bound binding word / Far-Voiced unfakeable feeling), not papers. The only per-person paper is a **guild safety-licence for the ~3 hazardous Conditions.** A universal register survives *only* as **one aberrant kingdom's paranoia** (the Watchful) — the creepy version is rare and villainous, not the baseline.
- [x] Legal status of each Condition; who regulates the feared ones (The Stilled, Bound) — the **guild safety-licence** (danger-to-others only, held by the person, not a census); the **Inviolate Will** doctrine (no Condition compels a will) sorts the criminal code
- [x] How the Struck are handled legally ("a little suspect") — they **changed *unwitnessed*** (later & alone), so must be **vouched anew**; the vulnerable are the *unvouched*, not the "undocumented"
- [x] Rights of the Kept — witnessed at ten, untithed, unlicensed; the *default legal person*; wrinkles: still-Struck-later, and pitied where reverence runs hot
- [x] **Bonus locks:** the **three pillars** (Long-Lived / Bound / Far-Voiced *are* the evidence/contract apparatus — and are *why* no register is needed); **3 polity stances** (Warm / Watchful-register-keeper / Frontier) — no planet-of-hats; social guard applied in GM Notes
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
- [x] **Bonus:** 3 polity domestic faces on the same theology/reach/governance axes + "mind the combinations"; the injustice reaches the hearth and stays real

### Story 2.4 — Polity archetypes (`governance-systems` / `worldbuilding`) ✅ **DONE (2026-08-21)** → [[Polity Archetypes]]
> **Frame:** prove the universal social physics flex by building **2–3 polities at *different corners* of the theology/reach/governance axis-space** (audit design note: NOT three-in-a-row on one axis). Each pair shares **exactly one** axis and differs on the other two, so the set *isolates* each axis and proves the three are independent. Extends the single-axis touchstones (Warm/Watchful/Frontier) into full three-knob corners.
- [x] **Three corners built** — **The Waiting Lands** (theology high · reach low · gov low — warm/poor/faithful pilgrim edge), **The Ledger Coast** (theology low · reach high · gov low — rich/cool secular merchant power), **The Tallied Crown** (all three high — sanctified surveillance, the darkest corner). Each walked through law · economy · daily life + its distinct injustice.
- [x] **Social guard applied** — three *different* injustices (guilt-theology / market-fade / sacred census), none dissolvable by the keystone reveal because they share no mechanism, only that people built them. Reach-edge cause kept GM-side in all three.
- [x] 🟡 **Naming labels are provisional** (working names picked with user 2026-08-21: Waiting Lands / Ledger Coast / Tallied Crown) — settled in-world names come *in* the naming pass below.
- [x] ✅ **DONE (2026-08-21) — the in-world naming pass.** Built [[The Old Tongue]] (root liturgical tongue *Maiethren* — warm/weighty phonology, pronunciation key, sacred root lexicon; **one root → three daughter drifts** mirroring the one-Tree/grafts cosmology) and named the three polities from it: **Vaethorn** (the Waiting Lands), **Lestrand** (the Ledger Coast), **Threnmaieth** (the Tallied Crown) — *the most-eroded name is the most secular polity.* Then [[Naming in the Turning]] (institution dictionary: common-tongue name + three stance-variants each — e.g. venting-hall → gift-hall / release-house / counted hall; the census = Threnhael "the whole-keeping"). Design lever landed as built: *the name a polity gives a shared institution reveals its stance.* All four social-structure notes updated. **Epic 2 tail complete.** (Deep grammar still deferred. The other ~12 polities' names + stance-drifts ✅ [[#Epic 7 — Settlements|Story 7.1]].)

---

## Epic 3 — The World Frame
**Skill:** `systemic-worldbuilding` · **Status:** ✅ **core done (2026-08-22); climate/ecology leftover done (2026-08-31)** — the four-continent frame, all four continent notes, the calendar, the 4th ancestry, named ground, and playable week-weather / living-ground notes. · Geography, climate, where the Trees grow, the physical stage.

> **Built as a reach-gradient.** The load-bearing call: the whole map is a **gradient of the [[Turning Tree|Trees']] reach** — sacred-dense origin → mercantile middle → thin frontier → storm-walled isle beyond. Physical map = cosmological map. → [[The World Frame]].

- [x] 🟡 **Geography & regions (`01 - World`)** → [[The World Frame]] (top-level) + four continents: **[[Maiethorn]]** (Motherland, full reach, holds [[Polity Archetypes|Threnmaieth]]), **[[Strandoren]]** (Shore-lands, high reach, trade, holds [[Polity Archetypes|Lestrand]]), **[[Heskoren]]** (Sundered Reach, thin reach, frontier, holds [[Polity Archetypes|Vaethorn]]), **[[The Sundering Isle]]** (Kumbaan — storm-walled, near-no reach, Yumboe homeland). The three archetype polities placed on three *different* continents; **rival faiths woven into the large continents** and now built ([[The Watching]] · [[The Fair Hand]] · [[The Old Ways]] · [[The Open Table]] — [[Faiths of the Turning]]).
- [x] 🟡 **Where Turning Trees grow** — the reach-gradient *is* this: densest/healthiest on Maiethorn, thinning outward, near-none across the storm-wall. Present-day thin reach = Tree-poor places (young/sick/few grafts), per [[The Ages of the Turning]] (the Grafting as a still-moving wave). Keystone edge kept GM-side in every continent note.
- [x] 🟡 **Astronomy/solstice — calendar locked** → [[The Reckoning of the Year]]: two solstices; the Leaf-Fall is **High Solstice / midsummer**, held **Turning-Week**; ~1400s-legible 12-month lunar-hinged calendar; [[The Sundering Isle|Kumbaan]] keeps the *moon, not the solstice* (a keystone tell).
- [x] 🟡 **(Pulled forward from Epic 4) — 4th custom ancestry built to full depth** → [[Yumboe]] (the good people / Bakhna Rakhna): three Daggerheart features (Hollow-Hill · Moon-Waked · The Unseen Hands), folklore-checked (Wolof/Senegambian *Yumboe* myth), small/pearly/silver, LOCKED. Its own non-Maiethren tongue seeded. The Isle *needed* its people, so the ancestry came here rather than waiting for Epic 4.
- **Map production aid (extracted Story R.10):** GPT Image prompts, Azgaar heightmap template, Maiethren + Kumbaan name bases, and the seed script live in `14 - Assets/Maps/Map Generation Tooling.md` — **not** inside player geography. Named waters, range, rivers, travel: [[Named Ground]]. Labelled picture: [[The Known Map]].
- [x] Per-region *deep* climate/ecology *(2026-08-31 leftover)* — hubs [[Climate of the Turning]] · [[Ecology of the Turning]]; continent notes [[Climate of Maiethorn]] · [[Climate of Strandoren]] · [[Climate of Heskoren]] · [[Climate of Kumbaan]]. Eight bands unchanged. No new liturgy. Kumbaan has no Tree-ecology. Travel table stays on Named Ground. ~12 other great powers ✅ Story 7.1 → [[Powers of the Turning]]. Month-names + the Isle's name base ✅ Story 4.2. Rival faiths ✅ Story 1.4.

---

## Epic 4 — Cultures & Kinds
**Skill:** `worldbuilding`, `character-naming`, optional `conlang`/`language-evolution` · **Status:** 🟢 custom ancestries DONE; Story 4.2 DONE (2026-08-23); Story R.3 glance DONE (2026-08-30). · **Blast radius: Low.**

### Story 4.1 — Custom ancestries ✅ **DONE (3 merged 2026-08-17; 4th added 2026-08-22)**
- [x] 🔒 [[Kitsune]] — locked (3 features)
- [x] 🔒 [[Selkie]] — locked (3 features)
- [x] 🔒 [[Tengu]] — locked (3 features)
- [x] 🔒 [[Yumboe]] — locked (3 features: Hollow-Hill · Moon-Waked · The Unseen Hands). **Built in Epic 3** (the far isle [[The Sundering Isle]] needed its people); the good people / *Bakhna Rakhna*, small/pearly/silver hill-folk, folklore-checked, their own non-Maiethren tongue. Now **four** custom ancestries.
- [x] 🟡 **Revisit flag:** Story R.3 glance done (2026-08-30) — power band, mix rule, surprise-keyword lanes, stale lines. Features not rebuilt.
### Story 4.2 — Peoples, customs, naming ✅ **DONE (2026-08-23)**
- [x] 🔒 How Kinds distribute across the world / cultures — **hearths, not nations.** Custom Kinds have terrain-origins (Kitsune three Fox-grounds · Selkie coasts · Tengu ridges · Yumboe = Kumbaan only). Stock ancestries lean, they do not own continents. → [[Kinds of the Turning]] *(user-approved 2026-08-23)*
- [x] 🔒 Naming conventions per culture (`character-naming` entropy approach + `conlang` naming-inventories) — a person is named by *place*; custom Kinds keep a hearth-register. Seeds recorded. → [[Naming People in the Turning]] *(user-approved 2026-08-23)*
- [x] 🔒 [[Kitsune]] / [[Selkie]] / [[Tengu]] naming registers — *Kusawe* · *Sakoa* · *Gonan*. [[Yumboe]] register expanded. *(user-approved 2026-08-23)*
- [x] 🔒 Month-names + Kumbaan's moons → [[The Reckoning of the Year]]; new Maiethren roots in [[The Old Tongue]] *(user-approved 2026-08-23)*
- [x] 🔒 Isle Azgaar name base → `14 - Assets/Maps/Map Generation Tooling.md` §③b *(user-approved 2026-08-23; extracted from player notes Story R.10)*
- [x] 🟢 **Root language + naming system seeded (2026-08-21, from the Epic 2 tail):** [[The Old Tongue]] + [[Naming in the Turning]]. **Still deferred (on purpose):** deep grammar/morphology (only if spoken dialogue is ever needed). The other ~12 great powers' *stance-drifts* ✅ Story 7.1 → [[Powers of the Turning]] (no new grammars; same three daughters).

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
- [x] 🟡 Who furnishes outlets + the Voice-ticket (one lintel, seam Condition) → [[The Hall-Keepers]] (the scheduled hour; *Aeloren* retired in R.12)
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
**Skill:** `settlement-design` · **Status:** ✅ **complete (2026-08-24); sick-Tree / guest-grove leftover done (2026-08-31).** Specific places, built on Epics 2–6. Residue types → [[Settlement Seeds]]. Named powers → [[Powers of the Turning]]. Playable squares → [[Harrow's Green]] · [[The Three Hamlets Past the Ford]] · [[The Third Hearth]] · [[Ornsael]] · [[The Mill-hold]] · [[The First Bowl]]. Archetype seats → [[Eolvaeth]] · [[Orentel]] · [[Maiethlir]]. Do not rebuild the era spine. Do not treat Ornthael as post-history. Do not rebuild 7.1. Do not rebuild 7.2. Do not rebuild 7.3.

> Progressive elaboration. The lead road-end is seated at [[Nelath]] (Story L.5, 2026-10-02). Do not capture the First Seat. Do not make Harrow's, Ornsael, the Mill-hold, the First Bowl, or Nelath a capital.

### Story 7.1 — Name the other powers (stubs) ✅ **DONE (2026-08-24)** → [[Powers of the Turning]]
The other twelve great powers, named. Names from [[The Old Tongue]] + stance-drift; hearths not Kind-nations. Includes the **secular frontier** corner on [[Heskoren]] ([[Ornled]]). Kumbaan is not a thirteenth mainland power.
- [x] 🔒 Count and place — **15** = 3 worked corners + 12 stubs; [[Maiethorn]] 6 · [[Strandoren]] 5 · [[Heskoren]] 4; [[The Sundering Isle|Kumbaan]] not a thirteenth mainland power *(user-approved 2026-08-24)*
- [x] 🔒 Names from [[The Old Tongue]] + stance-drift (seed `20260827`). Conservative Motherland · worn Heskoren · eroded Strandoren. How a power sounds reveals stance *(user-approved 2026-08-24)*
- [x] 🔒 Un-built corners now stubbed — **[[Maiethvael]]** (devout rich light-state) · **[[Trenledd]]** (surveillance, no hymn) · **[[Ornled]]** (secular frontier, required on Heskoren) *(user-approved 2026-08-24)*
- [x] 🔒 Hearths not Kind-nations ([[Kinds of the Turning]]). No Fox / Tengu / Selkie / Taken-In flags. [[The Watching]] stays a heresy inside districts, not a sixth Motherland power
- [x] 🟡 Hub + twelve stub notes in `05 - Factions/Governments/`. Capitals of the three corners named Story 7.3 ([[Eolvaeth]] · [[Orentel]] · [[Maiethlir]]). The twelve stubs' seats stay unnamed. Do not capture the [[The Tree-Wardens|First Seat]]. Do not make [[Harrow's Green]] a capital. Stub *texture* stays polishable; the **names and placement are 🔒**.
- [x] 🔒 Do not rebuild Epic 6. Do not narrate Ornthael as post-history. Do not put a mile-shrine on Kumbaan

### Story 7.2 — Playable squares from the leftover types ✅ **DONE (2026-08-24)**
Flesh a few settlements from [[Settlement Seeds]] (not all nine types). Tree-at-the-centre grammar from [[Daily Life]]; two clocks visible; one leftover job per street. Polity-face from [[Powers of the Turning]]. Do not clone Road-hands, the Slide, or Kind-quarters. Do not rebuild 7.1. Did not name the three archetype capitals (that was 7.3).

- [x] 🟡 Pick **3–4 types**, not nine. Include **at least one already-named stub** to flesh ([[Harrow's Green]] / [[The Three Hamlets Past the Ford]] / [[The Third Hearth]] / [[The White Note House]]) **and at least one new square** from an unused type. **Mix:** Harrow's + the hamlets + Third Hearth + new [[Ornsael]] (Rain-Shadow walk-hold). White Note unpicked here (desk fate; placed Story 7.3 on [[Orentel]]).
- [x] 🔒 Tree at the centre ([[Daily Life]]); **two clocks visible** (stone / west-road / wait / upper room); **one leftover job per street** (Harrow's · hamlets · Ornsael = necessity; Third Hearth/Brenthael = devotion)
- [x] 🟡 Polity-face from [[Powers of the Turning]], not only the three corners. [[Harrow's Green]] in [[Saelvaeth]] orbit, not a capital. [[Ornsael]] on [[Saelthael]], not a capital. [[The Third Hearth]] in [[Orenbren]] lodging-country. First Seat not captured.
- [x] 🔒 Hearths not Kind-quarters ([[Kinds of the Turning]]). Ornsael has a fox-market neighbourhood, not a Fox gate. Do not clone Road-hands or [[The Slide]] as a district
- [x] 🟡 `settlement-design` at square scale (site, leftover, one tension) — not a full district grid. Names from [[The Old Tongue]] + the power's drift (seed `20260828`, middle of the list): *Ornsael · Brenthael · Brenod / Vaelun / Ornath*; warden *Haelin* 🟡

### Story 7.3 — The three archetype seats ✅ **DONE (2026-08-24)**
Vaethorn / Lestrand / Threnmaieth as *places* (not only corners). Neighbours now named ([[Maiethvael]] · [[Orenbren]] · [[Brenledd]] · [[Saelvaeth]], etc.). Playable leftover-squares already on the ground (7.2) — do not clone them as the capitals. Do not let Threnmaieth capture the First Seat in the first sentence. Do not rebuild 7.1. Do not rebuild 7.2.

- [x] 🟡 Seat each corner as a leftover type + a square: [[Eolvaeth]] (waiting / pilgrim edge — **not** Harrow's, **not** the three hamlets) · [[Orentel]] (salt quay — [[The White Note House]] placed, desk not the crown) · [[Maiethlir]] (origin pilgrimage-town *under* a roll — **not** Brenthael, **not** the grove)
- [x] 🔒 Tree at the centre; two clocks visible; one leftover job per street. Threnmaieth's job is not "the census" as a postcard — the roll *layers* a leftover
- [x] 🔒 Do not capture the [[The Tree-Wardens|First Seat]]. Orenbren lodges; the college sits in the Motherwood beside. Do not make [[Harrow's Green]] or [[Ornsael]] a capital to tidy a map
- [x] 🔒 Hearths not Kind-quarters. Do not clone Road-hands or [[The Slide]] as a district. Do not clone 7.2's stones/cups/sand as the seats' only texture
- [x] 🟡 `settlement-design` at seat scale (site, leftover, one tension, enough street to play a capital without a full ward-grid). Names from [[The Old Tongue]] + the corner's drift (seed `20260829`, middle of the list): *Eolvaeth · Orentel · Maiethlir*; warden/factor/Speaker *Vaethod / Sorim / Rithim* 🟡

*Lean that landed:* three seats, not a continent-tour. Lestrand picked up the White Note's quay. Vaethorn feels the wait *without* being Saelvaeth's march. Threnmaieth feels the roll *without* owning Thaeloren.

### Leftover — sick-Tree and guest-grove ✅ **DONE (2026-08-31)**
User-asked seating of two unused leftover types. Do not rebuild 7.1–7.3. Do not resume the old Epic 8 roster. Do not write later campaign sessions. World book untouched.

- [x] Seat **sick-Tree** as a named square: Hands un-Hands, necessity-walk returns, civic crisis wearing a child's summer — not Ornsael's well, not Brenthael, not a cursed Tree → [[The Mill-hold]] (Orenbren Near Mile, past Brenthael; neighbour-slate and a shovel; Talen · Milsun · Thurrei)
- [x] Seat **guest-grove** as a named square: first meal vs Cutting-leave, host-rights, play with Door-Keepers and Vaelun — not a second Harrow, not Vaelun itself, not a sick guest → [[The First Bowl]] (Vaelhesk; folk *Lonasir*; two settings of one bowl; Delvor · Vilraet · Brudu)
- [x] Wire both into the existing network without cloning formulas — Brenthael hosts the Mill-hold's week; Harrow's later planting is the First Bowl; Nethiro walks there; same queue as the hamlets, opposite ends
- [x] Update [[Settlement Seeds]], [[04 - Settlements]], travel on [[Named Ground]], [[People of the Turning]] mouths, [[Build Plan]], this Progress section. Lead road-end stays a type. No new liturgy (seed `20260901`, middle of the worn/conservative lists)

> **Leftover recorded decisions.** Two clocks stand. Tree undated. Cutter unpicked. No sixteenth power. No Kumbaan graft. Given-door still one week; unsound wood spends it. The Mill-hold's physical problem is mill-race vs roots, not thirst. The First Bowl's guest is healthy; the fight is who sat down. Names common-tongue first. Seats of the twelve stubs stay unnamed.

---

## Epic 8 — People
**Skill:** `character-arc`, `character-naming`, `positional-revelation`, `perspectival-constellation` · **Status:** 🟢 **8.1 landed in Story R.8 (2026-08-30).** Hub [[People of the Turning]]. Offices named as furniture are people now. Do not rebuild the seats. Do not rebuild the squares. Stories R.12–R.13 ✅. Epic R closed. Next: Pass two · P2.1.

### Story 8.1 — Positional pivots from the seats ✅ **landed in Story R.8 (2026-08-30)**
Ordinary-job characters who become structural pivots. Draw from offices 7.2–7.3 already forced to exist; do not invent a chosen-one roster. Names from [[Naming People in the Turning]] (seed `20260830`; pick from the middle). Recruits not by Kind.

- [x] 🟡 Pick **4–6** pivots, not a court. Mix: at least one already-named office (Haelin / Thilim / Ledan / Vaethod / Rithim / Sorim) **and** at least one new mouth from an unused leftover (sick-Tree, guest-grove, Intake desk, Grown-Over room) — named: Vaethod · Rithim · Mataero · Thilim · Sorim (want, not sixth pivot). New leftovers: [[Laevila]] (Grown-Over) · [[Tesara]] (Intake)
- [x] 🔒 Positional, not destined — the job is why they matter (warden who sends, clerk who copies, factor who holds a berth, Speaker who will not say the line)
- [x] 🔒 Two clocks visible in the cast (someone who walked / someone who did not; someone on the live front / someone who thinks the wave is over)
- [x] 🔒 Hearths not Kind-champions. Do not clone an Epic-5 order as a person. Do not capture the First Seat as a pope-NPC
- [x] 🟡 `character-arc` false-belief for each; `perspectival-constellation` so their squares intersect without a party-of-protagonists

*Lean that landed:* Rithim's incomplete refusal; Vaethod's sent cohort; Mataero's occupancy; Laevila under Maiethlir's recut chapel; Tesara at the Intake desk; Thilim as the walker. Hub [[People of the Turning]]. Do not rebuild.

---

## Epic 9 — Secrets & Canon
**Skill:** `oblique-worldbuilding`, `paradox-fables` · **Status:** 🟢 **architecture done (2026-08-31)** — still *alongside* new notes (`reveals:` as they are authored). Hub: [[11 - Secrets]]. Procedure: [[Revelation Architecture]]. Index: [[Reveal Index]]. Do not lock the nature of her limit. Do not add a sixth Hand.

### Story 9.1 — Revelation architecture ✅ **DONE (2026-08-31)**
- [x] Write a GM procedure hub so a table can fire secrets without inventing cosmology — [[Revelation Architecture]] (fire plot vs cosmology; opening does not need the Spent Leaf)
- [x] Index every `reveal_tag` and patch missing tags on walls that already spoil — [[Reveal Index]]
- [x] Fill `foreshadowed_by` on [[The Other Hands]] and [[When the Fire Is Caught]]; keep keystone rungs 1–5 intact
- [x] Add at most two deniable clue objects — [[The Uncoloured Intake]] (household, unnamed Hands) · [[The Closed Lamp]] (fire plot, not a leaf). No fifth teaching-fable

> **9.1 recorded decisions.** Fire-plot can run without the keystone. Household confirmation is late and never first, never with the Spent Leaf pin. Unspent is furniture. Limit's nature stays open. Bound / Returned take `the-other-hands`; Phoenix card stays untagged. World book untouched.

---

## Epic 10 — Campaign
**Skill:** `key-moments`, `table-tone`, `dialogue` (`endings` later) · **Status:** 🟢 **Story 10.2 done (2026-10-05).** Story 10.1 done (2026-08-31). Actual play material (`12 - Campaigns`). Hub: [[The Isolated Fall]]. Kits: [[The Opening]] · [[The Walk Home]] · [[The Offered Fragment]] · [[The Week Still Open]]. Endings stay undecomposed. Do not resume the old Epic 8 roster. Do not name the cutter, date the Tree, coin liturgy, or add a sixteenth power.

> **Locked opening (2026-08-31).** Session one sits at [[Harrow's Green]] — one existing square, live front, not a new town, not a capital, not a Protector fortress. On-screen: escaped remnant-walker + [[Rosire]] + the new Gift ([[Taeren]] as the hidden seat, *or* a PC in that seat). [[Reimaethe]] and [[Hithaen]] offstage. Five key moments, mystery first; one 5% wrongness beat; wonder at the isolated fall. No Leaf-Mother reveal. Agency stays on [[A Hidden Phoenix]]. Engine: [[When the Fire Is Caught]] — apparent two is leftover fire next to a Gift.

### Story 10.1 — The opening ✅ **DONE (2026-08-31)**
- [x] Sit session one in one existing square — [[Harrow's Green]], Hale-month, C.Y. 387. Not a new town. Not a Protector fortress.
- [x] Put the escaped Phoenix, the inside helper, and the new Gift on-screen; leave the Pourer and the Walled-Book heir offstage — walker (remnant NPC) · [[Rosire]] · [[Taeren]] XOR a PC in that seat. [[Reimaethe]] · [[Hithaen]] stay put.
- [x] Write four or five key moments, not a plot — mystery first (two tenses; Hope scars that do not match remembered deaths); wonder at the isolated fall (last Eolthael, unspoken); one 5% wrongness beat (harvested fire answering the new Gift); helper as choice, not confession. Do not reveal the Leaf-Mother. Do not fire the remnant-to-ash confirm.
- [x] GM kit, not a novel — opening situation, what the table can see, what stays player choice. Skills: `key-moments`, `table-tone`, `dialogue`. → [[The Opening]]

> **10.1 recorded decisions.** Unseen-leaf + remnant walker. A walker-PC who can still Rise is a different opening; do not stack it on Taeren as a second Gift. Taeren is of Brenod; the fall was the neighbour's week at Harrow's Tree (C-05). Rosire left Tesara's shed. The walker stays unnamed this session. No sixteenth power. World book untouched. Later sessions, fragments-as-campaign, and endings stay undecomposed.

### Story 10.2 — The next sessions ✅ **DONE (2026-10-05)**
Memory-fragment continuation after [[The Opening]]. GM kits, in the same voice: key moments, not a plot. What the table can see. What stays a player choice. Session one stays done.

- [x] Read [[The Opening]] and [[The Isolated Fall]] before writing.
- [x] Write the kits. [[The Walk Home]] · [[The Offered Fragment]] · [[The Week Still Open]]. Key moments, not a plot.
- [x] Session one stays at [[Harrow's Green]], Hale-month, C.Y. 387. One Gift. [[Taeren]] or a PC in that seat, not both. The walker stays unnamed. [[Reimaethe]] and [[Hithaen]] stay offstage.
- [x] No Leaf-Mother reveal. Do not fire the remnant-to-ash confirm. No Protector fortress. No second bird. Do not write the campaign's close.
- [x] Point the hub at the kits. Do not resume the old Epic 8 roster. Do not update the world book.

> **10.2 recorded decisions (2026-10-05).** Three kits after session one. The walk is a choice, still Hale-month. The fragment is one offer, and zero is legal. Early Eolthael leaves the threads open. Leaf-Fall is not played. The walker is still unnamed. Clue 5 stays unfired. Endings stay undecomposed. World book untouched.

### Later (do not decompose until asked)
- `endings` when the campaign needs a close
- Do not resume the old Epic 8 roster to fill a court

---

## Epic A — Atlas labels
**Skill:** vault geography ([[Named Ground]] · [[The Known Map]]) · **Status:** 🟢 **A.1–A.14 done (2026-10-02).** City sheets for [[Maiethlir]] and [[Orentel]] are in. Does not reopen A.1–A.13. **Blast radius:** Low. Table aids only. Does not reopen R.10, invent a gazetteer, or touch the world book.

> **What this is.** The selected Prototype 3 paintings stay label-free as the handouts. Each story adds a Pillow overlay on *one* master. Names come from [[Named Ground]] and [[The Known Map]] only. If a painting and a note disagree, the note wins. Incidental roofs, field-grids, extra isles, and decorative weather stay unnamed.

> **Method (🔒 from A.1).** Do **not** ask the image model to write on the painting — that redrew Heskoren. Copy the overlay pattern in `14 - Assets/Maps/label_heskoren_atlas.py`. One script + one `*-Atlas-Labeled.png` per story. West = left. No borders, no capital stars, no new place-names. Unlabeled sheet stays the selected handout. Work **one story / one PR / one session**.

> **Do not.** Rebuild the paintings. Date the Tree. Add a sixteenth power. Put a graft on Kumbaan. Fold this into the world book unless asked.

First labels (not a new gazetteer) live on [[Map Generation Tooling#How to annotate after generate]].

### Story A.1 — Heskoren (C3) ✅ **DONE (2026-09-01)**
- [x] Learn that in-image text fails — trial archived in L.9 to `99 - Archive/Atlas/label-trials/Heskoren-Atlas-labeled-gen.png`
- [x] Overlay Named Ground on the selected C3 master — `label_heskoren_atlas.py` → `Heskoren-Atlas-Labeled.png`
- [x] Seat west-face names on the storm-side — last capes · marches · slate-shore · Ornled · toward the storm-wall
- [x] Seat east-face names on the Strandoren-facing side — frontier coast · the West Water (to Strandoren) · Eolvaeth / waiting vale · Harrow's · Rise-water · the ford · Brenod / Vaelun / Ornath · the First Bowl
- [x] Leave the south-east field-grid and extra roof-clusters unnamed; treat the north-east cloud bank as weather, not the storm-wall

> **A.1 recorded decisions.** The West Water is the *east* sea of Heskoren. The storm-wall is west, past the last capes. Eolvaeth is the vale behind the east coast, not the field-grid. Ornled is the west-coast pocket. Vaelhesk is area-type over the Far Yield. Unlabeled C3 stays the handout. World book untouched.

### Story A.2 — World sheet (W) ✅ **DONE (2026-09-03)**
One session. Master: `The-Turning-World-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], and the W prompt on [[Map Generation Tooling]]; list only those names
- [x] Write a Pillow overlay on the selected world master; do not ask the image model to write
- [x] Seat the four lands and the two waters west → east: Kumbaan · storm-wall · Heskoren · West Water · Strandoren · Old Crossing · Maiethorn · Rain-Wall. No fifth land. Extra painted isles stay unnamed
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled world sheet stays the handout

> **A.2 recorded decisions.** One Pillow overlay, not three label prototypes — A.1 already locked the method; placement iterates on the same script. Sheet title is *The Turning / the Known Lands* (from this schematic), not a fifth land. Continent epithets are the [[The World Frame]] handles. The storm-wall is the Kumbaan girdle; "no graft" is not a second type-line. The Rain-Wall sits Maiethorn's spine. Decorative stars and extra painted texture stay unnamed. Unlabeled W stays the handout. World book untouched.

### Story A.3 — Maiethorn (C1) ✅ **DONE (2026-09-16)**
One session. Master: `Maiethorn-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], and the C1 prompt on [[Map Generation Tooling]]; list only those names
- [x] Write a Pillow overlay on the selected C1 master; do not ask the image model to write
- [x] Seat Thaeloren · Inner Close · Orenbren · Maiethlir · Core-thaw · Noon Pass · Shelf-gate · Rain-Wall · Rain-Shadow · Hinge Shore · Ornsael · Well-wash. One exceptional Tree. No capital star on the First Seat
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled C1 sheet stays the handout

> **A.3 recorded decisions (2026-09-16).** `Maiethorn-Atlas-Labeled.png` is one Pillow overlay on the selected C1 master. Thaeloren uses a canopy-ring mark in the old-growth heart, not a capital star. The Inner Close is a small walled-town mark inside Orenbren, one day's walk from the Tree; it is neither a capital nor a sixteenth power. Maiethlir sits on the west-running Core-thaw. Noon Pass is the older high northern notch; Shelf-gate is the lower road left after the Break. The Rain-Wall names the full mountain divide. The Hinge Shore is coast-type on the Old Crossing face; Rain-Shadow is climate-type east of the watershed, not a border. Ornsael and the Well-wash keep the dry east legible at continent scale; the Dry Stair remains for R4. Incidental painted detail remains unnamed. Formal map labels capitalize their leading articles. Unlabeled C1 stays the handout. World book untouched.

### Story A.4 — Strandoren (C2) ✅ **DONE (2026-09-16)**
One session. Master: `Strandoren-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], and the C2 prompt on [[Map Generation Tooling]]; list only those names
- [x] Write a Pillow overlay on the selected C2 master; do not ask the image model to write
- [x] Seat Orentel at the large eastern estuary · Chart-run from the west · Trenledd over the wealthy filed interior · Netstrand on the open-ocean west and south face. No borders and no capital star
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled C2 sheet stays the handout

> **A.4 recorded decisions (2026-09-16).** `Strandoren-Atlas-Labeled.png` is one Pillow overlay on the selected C2 master. Orentel receives a plain settlement dot at the large eastern estuary, not a capital star. The Chart-run follows the broad interior river toward it from the west. Trenledd and Netstrand are area-type because both seats remain unnamed: Trenledd over the wealthy filed interior; Netstrand on the open-ocean west and south face. No political borders were inferred from the painting. Incidental harbours, river branches, roofs, and field divisions remain unnamed. Unlabeled C2 stays the handout. World book untouched.

### Story A.5 — Kumbaan (C4) ✅ **DONE (2026-09-16)**
One session. Master: `Kumbaan-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], and the C4 prompt on [[Map Generation Tooling]]; list only the isle and the storm-wall
- [x] Write a Pillow overlay on the selected C4 master; do not ask the image model to write
- [x] Seat Kumbaan on the central hill-country and the storm-wall along the complete outer cloud-ring. Nothing that implies a graft, city, harbour, settlement, or Tree
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled C4 sheet stays the handout

> **A.5 recorded decisions (2026-09-16).** `Kumbaan-Atlas-Labeled.png` is one Pillow overlay on the selected C4 master. Kumbaan receives land-type and its common-tongue epithet, without a point marker. The storm-wall follows the northern outer cloud-ring as a label for the complete girdle of cloud, current, and reef; the arc is not a border or an opening. No painted standing stone, wreck, hill, path, or interior texture is named. Nothing marks a graft, city, harbour, settlement, safe channel, or Tree. Unlabeled C4 stays the handout. World book untouched.

### Story A.6 — Old Crossing (R1) ✅ **DONE (2026-09-16)**
One session. Master: `Old-Crossing-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], the R1 prompt on [[Map Generation Tooling]], and [[The Hinge Hush]]; use only the crossing, Hinge Shore, Orentel, and Hush-rate
- [x] Write a Pillow overlay on the selected R1 master; do not ask the image model to write
- [x] Seat Orentel at the large Strandoren estuary and the Hinge Shore as area-type on the opposite Maiethorn coast; use no capital star and invent no Hinge seat
- [x] Show the Hush-rate as a compact crossing-charge cartouche in the channel, with no border line
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled R1 sheet stays the handout

> **A.6 recorded decisions (2026-09-16).** `Old-Crossing-Atlas-Labeled.png` is one Pillow overlay on the selected R1 master. Orentel receives a plain settlement dot at the large western estuary, not a capital star. The Hinge Shore follows the opposite coast as area-type because its seat remains unnamed. The Hush-rate is a small docket-like plate in the channel captioned as a crossing charge; no line, territorial fill, or political border is drawn. The chart names the Old Crossing itself but promotes no incidental quay, hull, tributary, roof cluster, or field division. Unlabeled R1 stays the handout. World book untouched.

### Story A.7 — Sacred Core (R2) ✅ **DONE (2026-09-16)**
One session. Master: `Sacred-Core-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], the R2 prompt on [[Map Generation Tooling]], and the four place notes; list only Thaeloren · Inner Close · Third Hearth · Maiethlir
- [x] Write a Pillow overlay on the selected R2 master; do not ask the image model to write
- [x] Seat Thaeloren at the sole exceptional canopy · Inner Close at the walled town one day out · Third Hearth three days outward on the Near Mile · Maiethlir at the Core-thaw city. No capital star
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled R2 sheet stays the handout

> **A.7 recorded decisions (2026-09-16).** `Sacred-Core-Atlas-Labeled.png` is one Pillow overlay on the selected R2 master. Thaeloren uses the canopy-ring marker in the central old-growth grove as the sole exceptional Tree; the First Seat receives no separate throne or capital mark. The Inner Close is the visibly walled town inside Orenbren lodging-country, one day's walk out. The Third Hearth receives a modest road-house diamond three days outward on the same Near Mile, not a city or power mark. Maiethlir receives a plain settlement dot at the eastern Core-thaw city, reached by its separate river road. Incidental clearings, roof clusters, road branches, and forest tracks remain unnamed. Unlabeled R2 stays the handout. World book untouched.

### Story A.8 — Rain-Wall (R3) ✅ **DONE (2026-09-16)**
One session. Master: `Rain-Wall-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], and the R3 prompt on [[Map Generation Tooling]]; use only Rain-Wall (with Thaw-Wall as Lirorn's local handle), Noon Pass, and Shelf-gate
- [x] Write a Pillow overlay on the selected R3 master; do not ask the image model to write
- [x] Seat Noon Pass at the older high northern road-notch and Shelf-gate at the lower surviving road; use notch marks, not settlement marks or borders
- [x] Name the Rain-Wall, with Lirorn's Thaw-Wall handle secondary, without claiming Heskoren's separate spine or drawing Tengu- or Fox-nation colour
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled R3 sheet stays the handout

> **A.8 recorded decisions (2026-09-16).** `Rain-Wall-Atlas-Labeled.png` is one Pillow overlay on the selected R3 master. Rain-Wall is the primary atlas label; Thaw-Wall is Lirorn's local secondary handle, not a second range. Noon Pass points to the older high northern road-notch and its water-line; Shelf-gate points to the lower road left after the Break. Small notch marks distinguish both from settlements and draw no border. Wet west, dry east, snow-shelves, ridge towns, roads, and rivers remain unnamed painted texture. Nothing claims Heskoren's separate spine or turns Tengu or Fox-of-the-Snows hearth density into a nation. Unlabeled R3 stays the handout. World book untouched.

### Story A.9 — Rain-Shadow (R4) ✅ **DONE (2026-09-17)**
One session. Master: `Rain-Shadow-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], the R4 prompt on [[Map Generation Tooling]], and the two place notes; use only Ornsael · Well-wash · Dry Stair
- [x] Write a Pillow overlay on the selected R4 master; do not ask the image model to write
- [x] Seat Ornsael as a plain well-town on the west-road and the Dry Stair as a site-mark on a different rise; leave the Stair's well-town unnamed and use no capital star
- [x] Name the Well-wash as seasonal hydrology without drawing a border or Fox-nation fill
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled R4 sheet stays the handout

> **A.9 recorded decisions (2026-09-17).** `Rain-Shadow-Atlas-Labeled.png` is one Pillow overlay on the selected R4 master. Rain-Shadow is climate-type for the dry east, oriented as east of the Rain-Wall; the left highlands are that range's back and receive no separate range label here. Ornsael receives a plain well-town dot at the west-road settlement with a Tree beside the well, not a capital star and not Thaeloren's canopy-ring. The Dry Stair is a site-mark on the stair-rise of a different hill; the well-town at its shoulder stays unnamed. The Well-wash follows the painted seasonal channel as hydrology, not a civic river or a border. Terraces, the far-east roof-cluster, and other incidental texture remain unnamed. Nothing draws Fox-nation colour. Unlabeled R4 stays the handout. World book untouched.

### Story A.10 — Chart-run (R5) ✅ **DONE (2026-09-17)**
One session. Master: `Chart-Run-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], the R5 prompt on [[Map Generation Tooling]], and the two place notes; use only Chart-run · first quay · White Note
- [x] Write a Pillow overlay on the selected R5 master; do not ask the image model to write
- [x] Seat the Chart-run along the interior river and the first quay as the old landing; use no capital star
- [x] Mark the White Note as a desk-house on the third quay, north side, with no crown on the desk
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled R5 sheet stays the handout

> **A.10 recorded decisions (2026-09-17).** `Chart-Run-Atlas-Labeled.png` is one Pillow overlay on the selected R5 master. The Chart-run follows the interior river east into the Salt Quay estuary. The first quay is a landing mark at the old inner south waterfront below the rise, not a city or capital. The White Note is a desk-house on the third quay, north side — a building, not a crown. Leap-frog warehouses, the south-mouth yards, and filed river-towns remain unnamed. Unlabeled R5 stays the handout. World book untouched.

### Story A.11 — Night Shore / West Water (R6) ✅ **DONE (2026-09-17)**
One session. Master: `West-Water-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], the R6 prompt on [[Map Generation Tooling]], and [[Netstrand]]; use only West Water · Night Shore
- [x] Write a Pillow overlay on the selected R6 master; do not ask the image model to write
- [x] Seat the West Water in the open ocean and the Night Shore as area-type on the west-and-south face; use no capital star and invent no Night Shore seat
- [x] Leave the unlit berth unmarked; name no incidental quay, hull, or harbour-hatch
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled R6 sheet stays the handout

> **A.11 recorded decisions (2026-09-17).** `West-Water-Atlas-Labeled.png` is one Pillow overlay on the selected R6 master. The West Water names the open ocean as the long sea-leg, not the crowded Crossing; the hydrology sits in the blue, not across the shore. The Night Shore is area-type on the west-and-south face because its seat remains unnamed; *Netstrand* stays the continent-sheet liturgy. The unlit berth is left unmarked. Hulls, harbour hatches, lamp-ticks, the painted inland run, and the far-left weather remain unnamed. Nothing draws a capital star, a border, a Kind-nation, or a graft on the storm-isle. Unlabeled R6 stays the handout. World book untouched.

### Story A.12 — Live Front (R7) ✅ **DONE (2026-09-19)**
One session. Master: `Live-Front-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], the R7 prompt on [[Map Generation Tooling]], and the two place notes; use only Harrow's · Rise-water · Brenod / Vaelun / Ornath
- [x] Write a Pillow overlay on the selected R7 master; do not ask the image model to write
- [x] Seat Harrow's as a plain grove-town on the rise with no capital star, and the Rise-water along the stream to the ford
- [x] Seat Brenod, Vaelun, and Ornath as three small downstream hearths on different ground; leave the ford unmarked and invent no extra names
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled R7 sheet stays the handout

> **A.12 recorded decisions (2026-09-19).** `Live-Front-Atlas-Labeled.png` is one Pillow overlay on the selected R7 master. Harrow's receives a plain settlement dot on the rise canopy, not a capital star and not Thaeloren's canopy-ring. The Rise-water follows the low stream from that rise toward the ford. Brenod, Vaelun, and Ornath are small hearth marks on different ground past the crossing: the sending road-hearth, the wetter old plot, and the thinner rise. The ford, the cup-rock, distant canopy-pockets, and incidental roofs remain unnamed. Session one still sits here; that is not a map label. Unlabeled R7 stays the handout. World book untouched.

### Story A.13 — Waiting Vale (R8) ✅ **DONE (2026-09-19)**
One session. Master: `Waiting-Vale-Atlas.png`.
- [x] Read [[Named Ground]], [[The Known Map]], the R8 prompt on [[Map Generation Tooling]], and [[Eolvaeth]]; use only the spring · the vale / Eolvaeth
- [x] Write a Pillow overlay on the selected R8 master; do not ask the image model to write
- [x] Seat the spring as a site-mark at the track-junction pool and the vale as area-type; mark Eolvaeth as a pilgrim-edge, not a capital
- [x] Leave Harrow's canopy undrawn and unnamed; name no incidental garden, extra track, coast-sliver, or inland ridge
- [x] Record the labeled file on [[The Atlas Sheets]]; unlabeled R8 sheet stays the handout

> **A.13 recorded decisions (2026-09-19).** `Waiting-Vale-Atlas-Labeled.png` is one Pillow overlay on the selected R8 master. **The Waiting Vale** is area-type for the fold behind the east-facing coast. The spring is a pool-mark at the painted water where the tracks meet, not a mile-shrine stone and not a Tree. Eolvaeth receives a plain pilgrim-town dot at the gift-hall cluster, not a capital star and not Thaeloren's canopy-ring. Harrow's canopy is neither drawn nor named; inland luck stays out of sight. The coast sliver, garden-grid, extra tracks, and the western ridge remain unnamed. Unlabeled R8 stays the handout. World book untouched.

### Story A.14 — City sheets (Maiethlir and Orentel) ✅ **DONE (2026-10-02)**
Two city sheets, from the layout already written in L.5. It does not reopen A.1–A.13. [[Eolvaeth]] stays a town and gets no city sheet. Lived-world next stays **L.6**. L.6 was not opened in this pass.

- [x] Read the layout on [[Maiethlir]] and [[Orentel]]. Use only names those notes already carry. If a painting and a note disagree, the note wins.
- [x] One **Maiethlir** city sheet. Approaches: the Grove Bank, the Down Gate, the Wall Path. The Tree stands on the Slow Water, inside the old flood-wall. The one tension is the Loft Row, between the Tree and the tablet-hall. No capital star. The First Seat stays in the wood. [[Maiethvael]]'s seat stays unnamed.
- [x] One **Orentel** city sheet. Approaches: the Crossing-mouth and the Chart mouth. The Tree is on the Rise. The one tension is the Drop, from that free Hand down to the held berths. Also carry: the First Quay, the Third on the north side ([[The White Note House]], a desk), Hallowquay, the inland yard. No capital star. The White Note is not the crown.
- [x] These are new sheets. Do not crop or relabel Sacred Core, Chart-run, Old Crossing, or the continent masters. Do not put [[Nelath]], [[Raillath]], [[Denlad]], [[Tunral]], or a second name on the Core-thaw onto the regional sheets. Denlad is a day's sail short of the estuary and is not a district of Orentel. Nelath is a different road and is not a district of Maiethlir.
- [x] If a painting is generated, do not ask the image model to write. Label from the notes. Record both sheets on [[The Atlas Sheets]]. Unlabeled Prototype 3 sheets stay the regional handouts. Do not update the world book.

> **A.14 recorded decisions (2026-10-02).** `Maiethlir-City-Atlas-Labeled.png` and `Orentel-City-Atlas-Labeled.png` are Pillow overlays on new city paintings, not crops of Sacred Core, Chart-run, Old Crossing, or the continent masters. The image model was not asked to write. The first paintings read as villages and were replaced the same day. A later pass the same day set Maiethlir in Sacred Core forest and Orentel on the Chart-run estuary, and added heart and drop zooms because a full-city plate stays about 1152 pixels on the long side. Maiethlir is the compact counted city. Orentel is the larger salt-city, and the Tree square is the smaller half. Maiethlir: Grove Bank (north road from the wood; the wood is not a seat), Down Gate (downstream, west), Wall Path (upstream road outside the wall, east), the Tree on the Slow Water inside the old flood-wall, Loft Row as the one street to the Tablet-hall. No capital star. The First Seat is not marked. Maiethvael's seat is not named. Orentel: Crossing-mouth, Chart mouth, the Tree on the Rise, the Drop from that free Hand down to the held berths, First Quay, the Third on the north side, White Note as a desk on that quay, Hallowquay, the inland yard. No capital star. The White Note is not the crown. Painted battlements and precinct lines are incidental. [[Nelath]], [[Raillath]], [[Denlad]], and [[Tunral]] were not added to any sheet. [[Eolvaeth]] has no city sheet. Unlabeled Prototype 3 sheets stay the regional handouts. World book untouched. L.6 was not opened.

---

## Epic L — The lived world
**Skill:** `story-sense` → `memetic-depth`, `dialogue`, `language-evolution`, `character-arc`, `belief-systems` · **Status:** ✅ **L.9 done 2026-10-03.** Epic L complete. Epic S and Epic M were not opened. **Blast radius:** Med.

> **Diagnosis (2026-09-28).** Pass one is built, the contradiction log is empty, and the world still feels designed. `story-sense` reads this as a world without life: history is a list of events with nobody in them, and culture is law and economy with one mouth. `worldbuilding` reads the same gap as institutions without faces and culture without depth. The fix is voices, then the dead, then what the living still do. It is not a second gazetteer.

> **Empty folders are a mixed signal.** Some headings have no notes because the work was never done. Many others are empty because the note already lives in the parent folder or in another section. One canonical home per entity ([[Conventions]]). Link. Do not duplicate. Do not move a note just so a sidebar looks full.

> **Do not.** Invent a fourth mainland language, unfreeze liturgical coinage, or write a grammar nobody speaks. Give witness-lands or Kumbaan a surname. Turn stock ancestries into nations. Add a fourth body-licence. Invent planes. Name the cutter. Date the Tree. Lock the nature of her limit. Add a sixteenth power. Put a graft on Kumbaan. Write a reliable pre-Cut year-chronicle, or treat C.Y. 0 as the birthday of Conditions. Set a power in the storm-wall to block the household. Name the twelve stub seats during L; that pass is [[#Epic S — The other seats]]. Fill every village. Write the campaign. Rebuild the Epic 8 roster. Move [[Conditions]] out of `09 - Creatures/Conditions`. Update the world book unless asked.

### Where the ask lands

| The gap | Story | Already written — link, do not rewrite |
|---|---|---|
| How a place speaks; what they call the Tree and the Mother | **L.1** ✅ | [[How a Place Speaks]] · [[The Old Tongue]] (three drifts + Kumbaan outside the box) · [[Naming People in the Turning]] |
| Historical figures; past heroes and the condemned | **L.2** ✅ | [[The Other Count]] and its five years · [[The Closing]] · [[The First Cut]] · the walk |
| Customs, traditions, rituals, mythology folders, religious history | **L.3** ✅ | [[What the Year Feels Like]] · [[How the Week Is Kept]] · [[When the Town Buries]] · [[The Guest-Meal]] · [[When Someone Is Struck]] · [[Maieth]] · [[The Houses and the Years]] · [[Daily Life]] |
| Second names on the cast; leaders; living arguments | **L.4** ✅ | [[People of the Turning]] · the NPC notes · [[Leaders]] · [[Heroes and Villains]] · byname or house-name by raising-place, locked 2026-09-28 |
| Continents, regions, city layouts, the road-end town, a few villages and sites, sky, phenomena, archaeology | **L.5** ✅ | Continents in `01 - World/Geography` · [[Named Ground]] · [[Maiethlir]] · [[Orentel]] · [[Settlement Seeds]] · [[The Reckoning of the Year]] · [[The Low Wall]] · [[The Seeing-Ring]] · [[The Dry Stair]] |
| The other Daggerheart ancestries | **L.6** ✅ | [[Kinds of the Turning]] (hearths, not nations) · [[Kind Heritage]] |
| Criminal houses, more fellowships, the watch, movements | **L.7** ✅ | [[The Slide]] · [[The Holding Desk]] · [[The Standing Trade]] · [[Craft Fellowships]] · [[The Watch and the Cohort]] · [[Movements]] |
| Magic, beasts, constructs, artifacts, secrets folders | **L.8** ✅ | [[How the Work Is Done]] · [[A Made Thing]] · [[The Cart-Ox]] · [[The Terrace Goat]] · [[The Path Dog]] · [[Kin at the Door]] · [[What a Place Needed]] · [[Mysteries]] |
| Sidebar honesty and old atlas leftovers | **L.9** ✅ | Pointers for decisions already written. Prototypes 1 and 2 and the label trial archived. Prototype 3 stays |

### Story L.1 — How a place speaks ✅ **DONE (2026-09-29)**
Player-facing voice. Skills: `language-evolution`, `dialogue`, `memetic-depth`. One note, not a language family. Deep grammar stays deferred except a paradigm a spoken line actually needs.

- [x] Write **How a Place Speaks** (`03 - Cultures/Languages/`): conservative, worn, and eroded Maiethren, plus Kumbaan's own mouth. For each, the spoken handles for the Tree, the Mother, a hug, a colour, a warden, and a graft. Common speech only. No new liturgical compounds.
- [x] Four tones a player can actually use — devout core, dock, waiting or live front, hill-hall. Sentence length, what they repeat, what they will not say in company.
- [x] Say why a witness-town asks *of where?* and a list-land asks *what house?* Point at [[Naming People in the Turning]]. House-names (the surname slot) are already locked for Threnmaieth, Trenledd, the Inner Close, and filing houses. Do not rename the cast in this story.
- [x] Leave one phrase per drift in use and untranslated. Recognizable speech, inferrable drift, a little that will not gloss.
- [x] Do not unfreeze coinage. Do not add a fourth mainland tongue. Kumbaan stays outside the Old Tongue box.

> **L.1 recorded decisions (2026-09-29).** [[How a Place Speaks]] is the player voice note. Handles are common speech: conservative, worn, and eroded Maiethren, plus Kumbaan's own mouth. Four tones: devout core, dock, waiting or live front, hill-hall. One untranslated phrase per drift, and one hill phrase that is not Maiethren. Second-name rule unchanged; cast not renamed. No new liturgical compounds. No fourth mainland tongue. No grammar. World book untouched.

### Story L.2 — Faces on the years ✅ **DONE (2026-09-29)**
The dated years get people. Skills: `character-arc`, `positional-revelation`, `character-naming`. Files live in `08 - People/Historical Figures`. Event notes link. Names from the existing drifts and the naming tool; record the draw.

- [x] One remembered person for [[The Closing]], [[The Two Papers]], [[The Grey Summer]], [[The Thaw-Break]], and [[The Hinge Hush]]. What they wanted. What people still argue they did. Where the name is still said.
- [x] Two or three people around the Walk and the Cut who are not the cutter — a sermon, a minute, a folk blame. The cutter stays unpicked.
- [x] Mark each as praised, condemned, or still argued. That is the past hero and villain layer. No present campaign antagonist.
- [x] Do not date the Tree. Do not lock her limit. Do not add a sixteenth power. Do not coin liturgy.

> **L.2 recorded decisions (2026-09-29).** Remembered persons, all **still argued:** [[Hildal]] (clerk of the Retreat), [[Limrae]] (Manril stays the argument), [[Dirrol]] (desk; Nidtol stays the later overlay), [[Narol of the Pass]], [[Taerso]] (Sirtol stays the other shore). Around the Walk and the Cut, not the cutter: [[Monseoth]] of the Near Mile (**praised**, the sermon), [[Rithnali]] (**still argued**, the minute), [[Sedrad]] of the Salt Walk (**condemned**, the folk blame). Five attributions uncollapsed. No house-names on the witness-roads. Draws, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20260930 --register conservative --count 40` — Monseoth, position 11. `python3 "14 - Assets/Names/generate_names.py" --seed 20260930 --register eroded --count 40` — Sedrad, position 22. Heroes / Villains index not built (L.4). World book untouched.

### Story L.3 — What the year feels like ✅ **DONE (2026-10-01)**
Customs, traditions, and rituals by **stance and faith**, not by Kind. Skills: `story-sense`, `memetic-depth`, `belief-systems`. The felt year is practice. Doctrine stays on the faith essays.

- [x] Write the ordinary year by stance and faith, not by Kind, in [[What the Year Feels Like]]. Link [[Daily Life]]. Do not copy it. Leave one local habit per stance unexplained: the thaw, the salt, the wet leaf, and the heel.
- [x] Write Turning-Week as kept in a devout square, on a dock, and in a waiting town, and what the hill-hall does instead of a Leaf-Fall → [[How the Week Is Kept]].
- [x] Write a funeral, a guest-meal, and the hour someone is Struck. Ritual notes are practice, not a second copy of doctrine. Do not coin liturgy. → [[When the Town Buries]] · [[The Guest-Meal]] · [[When Someone Is Struck]]
- [x] One home each. Faith essays into `07 - Religion/Faiths`. Four fables into `07 - Religion/Mythology`. [[The Unspent]] under `07 - Religion/Deities`, no second cup-note. [[Maieth]] is belief beside [[The Leaf-Mother]]. The keystone stays behind the wall.
- [x] [[The Houses and the Years]] links [[The Ages of the Turning]], [[The First Cut]], [[The Wrong Green]], and the household notes. It does not rewrite Epic 6. [[The Other Hands]] stay GM.
- [x] Do not date the Tree. Do not lock her limit. Do not add a sixteenth power. Do not put a graft on Kumbaan. Do not write a reliable pre-Cut year-chronicle, or treat C.Y. 0 as the birthday of Conditions. Do not set a power in the storm-wall. Do not name the cutter. Do not coin liturgy. Do not update the world book.

> **L.3 recorded decisions (2026-10-01).** Felt year → [[What the Year Feels Like]] · [[How the Week Is Kept]] ([[Maiethlir]] square, [[Orentel]] dock, [[Eolvaeth]] waiting; [[Ndenjoo]] keeps supper instead). Hours → [[When the Town Buries]] · [[The Guest-Meal]] · [[When Someone Is Struck]]. Unexplained habits left where they were: thaw, salt, wet leaf; the heel is new on [[Ndenjoo]] and unglossed. [[Maieth]] is the player-facing presence, belief only. [[The Unspent]] moved, not rewritten. [[The Houses and the Years]] is a door. World book untouched.

### Story L.4 — Names in the room ✅ **DONE (2026-10-01)**
Every existing NPC note gets the **second name their raising-place uses**: a byname, or a house-name if they were raised where a list finds people (Threnmaieth, including Maiethlir, Trenledd, the Inner Close, a filing house while the paper is open). No English surnames. No Kind-name in the civic slot. Kumbaan and the witness-lands stay without house-names. A Leaders index links the people who already hold an office; it does not clone their notes. New present leaders only where a road the table will walk has no mouth. Do not staff the twelve unnamed seats. A Heroes / Villains index is mostly L.2's dead, plus at most two living people the street argues about. No campaign villain. On-page mouths without notes stay on-page unless a story needs them.

- [x] Write the second name on every note in `08 - People/NPCs/`. House-name only for a raising-place that lists people. Bynamed where people are witnessed. Neighbour gets the given name; a list-land clerk gets the house first; a witness-town gets the given name and *of the place* for a stranger; Kumbaan gets the given name. Draws from `generate_names.py`; record seed and position. No English surnames. No Kind-name in the civic slot. If [[Naming People in the Turning]] already has a worked row, use it. Textbook rows stay textbook. Thilim stays of the Held bed. Njunda stays the given name. The Orentel [[Valen]] is not Valen of Hallowquay; an N. still gives no family name. The White Note is a desk only while the paper is open.
- [x] Write [[Leaders]]: link offices that already have a mouth. Do not clone their notes. No new present leader — the roads the table walks already have mouths. Do not staff the twelve unnamed seats. Do not capture the First Seat.
- [x] Write [[Heroes and Villains]]: L.2's dead, plus at most two living people the street argues about. No campaign villain. Do not add house-lines to Hildal, Limrae, or Dirrol.
- [x] On-page mouths without notes stay on-page. Tora stays on [[08 - People]]. Do not give Maiethvael, the Waiting Lands, or Kumbaan a person-list.
- [x] Do not unfreeze liturgical coinage. Do not add a fourth mainland tongue. Do not date the Tree. Do not name the cutter. Do not lock the nature of her limit. Do not add a sixteenth power. Do not put a graft on Kumbaan. Do not update the world book.

> **L.4 recorded decisions (2026-10-01).** Second names are on the NPC notes. House-names, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261001 --register conservative --count 40` — **Thalonve** position 27 ([[Laevila]] · [[Senithi]]), **Rairtei** position 26 ([[Baerith]]), **Nirsei** position 32 ([[Rithim]]; [[Valein]] unwritten), **Brethlumal** position 15 ([[Hithaen]], unsaid). English-adjacent and Maieth-adjacent draws in that field were thrown back (Tervi, Mermil, Theolvo, Leobrai, Maithvoro, Meirleth, Brathru, Runnaeth, Muleonmen, Simulsai). Natul was distance 2 of Narol. Lertae sat too near Limrae. Witness-lands and Orentel stay bynames. Thilim of the Held bed. Njunda the given name. Textbook rows unseated, including Valen of Hallowquay. White Note is a desk only while the paper is open. [[Leaders]] links existing mouths; no new leader; twelve seats unstaffed. [[Heroes and Villains]] links the L.2 dead plus [[Vaethod]] and [[Sorim]], still argued, not villains. World book untouched.

### Story L.5 — Places with a street ✅ **DONE (2026-10-02)**
Selective. [[Settlement Seeds]] is the catalog of leftover *types*. The lead that was waiting is now one town. No new type besides that seating. Skills: `story-sense`, `settlement-design`, `memetic-depth`.

- [x] Continents stay in `01 - World/Geography`. `04 - Settlements/Continents` is a pointer index. Essays were not copied. Canonical notes were not moved. → [[Continents]]
- [x] Regions: an index from [[Named Ground]] and the fifteen powers. New region texture only for the blank between [[Maiethlir]] and [[The Hinge Shore]]. Stub seats stay unnamed. The spur at [[Nelath]] had no mouth; it is a town, not a seat. → [[Regions]] · [[The Down-Bank]]
- [x] [[Maiethlir]] and [[Orentel]] have enough layout for a later city atlas: approaches, the Tree, one district tension, names a map could carry. The atlas was not drawn in L.5. City sheets are [[#Story A.14 — City sheets (Maiethlir and Orentel)|Story A.14]], drawn 2026-10-02. [[Eolvaeth]] stays a town.
- [x] Seat the lead road-end as one town: the walk stopped, the square is the last mile, a stone in the square, the road ends at the boughs, an upper room. Not [[Harrow's Green]], not Brenthael, not [[The Mill-hold]]. Not a capital. Not the First Seat. → [[Nelath]]
- [x] Three villages on roads that already exist. Not a gazetteer. → [[Raillath]] (Near Mile) · [[Denlad]] (Salt Walk) · [[Tunral]] (live front)
- [x] The argued sites stay [[The Low Wall]], [[The Seeing-Ring]], and [[The Dry Stair]]. The Low Wall records who dug and what they fought over. No archaeology discipline.
- [x] One sky-from-the-ground note beside [[The Reckoning of the Year]]. Solstice and Kumbaan's moons as a person sees them. Not a star catalog. → [[The Sky from the Ground]]
- [x] Three phenomena that climate and reach already imply. → [[The Green Across the Gap]] · [[The Day-Wash]] · [[Brine and Rain]]
- [x] Planes: one decision note. This world does not have them. → [[Planes]]

> **L.5 recorded decisions (2026-10-02).** `story-sense`: Harrow's already says the square is the last mile while a cart-track continues to the ford; the Mill-hold says the road ended at the boughs while the Mile continues grove-ward. Seating either again would be a second copy. [[Nelath]] is a spur off the Near Mile, a day short of the Third Hearth, that stops. The scar is thorns and a ditch, not a green lane. Orenbren's seat stays unnamed. The First Seat stays in the wood. Eolvaeth was not given wards. Maiethlir's tension is the Loft Row. Orentel's is the Drop. The Down-Bank is the days after Maiethlir's Down Gate and before a hull is classified; Maiethvael's seat stays unnamed and unlistable. Draws, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261002 --register conservative --count 40` — **Nelath** position 34, **Raetoth** position 9, **Lithsur** position 30, **Raillath** position 25, **Lonteith** position 22, **Nurreith** position 14. `python3 "14 - Assets/Names/generate_names.py" --seed 20261002 --register eroded --count 40` — **Denlad** position 4, **Relmun** position 10. `python3 "14 - Assets/Names/generate_names.py" --seed 20261002 --register worn --count 40` — **Tunral** position 7, **Huval** position 2. Thrown back from those fields: distance-2 collisions (Nulol, Tairol, Maiseoth, Mimae, Taemeon, Lirrei, Dirto, Sonral, Bonti, Daded, Motel, Sati, Benrad, Niren, Sirse, Nolol, Vuren, Lirvei, Taeril, Loltir, Narat) and ear-collisions or English stems (Thaeval, Neilsur, Seonmith, Sainral, Rairin, Voseil, Virmeil, Rulrat, Tailreth, Breintae) plus the th-stacks that will not be said at a table. Given names only. No house-names. No person-list for Maiethvael, the Waiting Lands, or Kumbaan. World book untouched.

### Story L.6 — The other hearths ✅ **DONE (2026-10-02)**
The stock Daggerheart ancestries get a **hearth-glance**: where they are dense, one kitchen habit, what they do not own. Group them. No new features. No Kind-nations. The four custom Kinds stay as written. Mechanics stay on [[Kind Heritage]]. Skills: `memetic-depth`.

- [x] Keep the leans already on [[Kinds of the Turning]] and write them as glances. Water-born (Ribbet, Galapa) on the Selkie coasts, and not Selkies. Height-and-wild (Giant, beside some Ridgeborne / Wildborne communities) on Heskoren's uplands, beside Tengu ridges. Old-wood (Elf, Faerie, Fungril, Firbolg) in the Motherwood, beside Wilds-fox hearths.
- [x] Group the rest, still as hearths: hedgerow and herd (Faun, Halfling); loft, mast, and canopy (Katari, Simiah); the warm bench (Clank, Dwarf, Goblin, Drakona); the carrying yard (Orc); Human; Infernis. All eighteen named. No eighteen nations. No country each.
- [x] For each group: where they are dense, one kitchen from the ordinary larder, and what they do not own. Humans common, not a baseline. Infernis born demon-blooded, not [[Bound]], no homeland. Halfling and Faerie not [[Yumboe]]. A thicker pocket is a town fact. A Ribbet inland and a Giant on a Lestrand dock stay ordinary.
- [x] Link [[Kind Heritage]]. Do not add features. Do not move Hearth-Mark, Mixed Ancestry, or the surprise keyword. The four custom Kinds stay as written.
- [x] Do not create a Kind-nation note, a fox-summer office, or a guild that recruits by ears. Do not rename the cast. Do not seat the twelve unnamed powers. Do not update the world book. Do not open L.7, Epic S, or Epic M.

> **L.6 recorded decisions (2026-10-02).** Glances live in [[Kinds of the Turning]], not in a new note. Nine groups: water-born (Ribbet, Galapa); beside the ridges (Giant); old wood (Elf, Faerie, Fungril, Firbolg); hedgerow and herd (Faun, Halfling); loft, mast, and canopy (Katari, Simiah); the warm bench (Clank, Dwarf, Goblin, Drakona); the carrying yard (Orc); Human; born to the blood (Infernis). Kitchens are the place's larder ([[Ecology of the Turning]]). A Fungril household sets one spoonful aside and will not say who it is for. Ember stays a lean, not a Drakona chapter. Hearth-Mark, Mixed Ancestry, and the surprise keyword stay on [[Kind Heritage]]. World book untouched. L.7 not opened.

### Story L.7 — Fellowships, the watch, and movements ✅ **DONE (2026-10-02)**
[[The Slide]], [[The Holding Desk]], and [[The Standing Trade]] are the criminal layer already. Rehome or index them under `05 - Factions/Criminal`. Do not invent a fourth syndicate. [[The Protectors]] stay a public care with the harvest behind the wall, not a street gang.

The three licence guilds stay the only body-licences ([[The Stillers]], [[The Element-Guilds]], [[The Intake]]). The Voice-ticket already belongs to [[The Hall-Keepers]]. Add a few **craft fellowships** — mill, hull, road — that are not tickets.

One military note: the town watch, a cohort, and what [[The Closing]] and [[The Hinge Hush]] left behind. No fifteen standing armies. No new war.

Two or three movements, each marked **past** or **present**, grown from schisms that already exist (Watching, the Walled Book, the Pourers). No new ideology.

Skills: `memetic-depth`, `cliche-transcendence`. Ordinary sentences. A habit people will not explain is written as what they do.

- [x] Rehome [[The Slide]], [[The Holding Desk]], and [[The Standing Trade]] into `05 - Factions/Criminal`. Index them from [[05 - Factions]]. Do not invent a fourth syndicate. Leave [[The Protectors]] under Organizations: a public care, harvest behind the wall.
- [x] Write [[Craft Fellowships]]: the mill-share, the hull-wrights, and the road-mend. They are not body-licences. [[The Stillers]], [[The Element-Guilds]], and [[The Intake]] stay the licences already named in this story. [[The Hall-Keepers]] keep the Voice-ticket they already stamp. Do not turn Gale, Tide, or Root into these fellowships. Do not turn Road-hands into the road-mend.
- [x] Write one military note, [[The Watch and the Cohort]]. The town watch is the civic hold in [[Law and Citizenship]]. A cohort is a send when a Hand cannot Turn the week, the one [[Vaethod]] already sends and the one [[The Mill-hold]] already walks. [[The Closing]] left a wall. [[The Hinge Hush]] left a rate. No fifteen standing armies. No new war.
- [x] Write [[Movements]]. The pear-graft is past (Watching, during the Closing). The withdrawers are present (Pourers: stop). The disinherited are present (a Given heir the Book already strikes). No new ideology.
- [x] Do not update the world book. Do not open L.8, Epic S, or Epic M.

> **L.7 recorded decisions (2026-10-02).** Criminal home is `05 - Factions/Criminal` for the three houses already written. No fourth syndicate. [[The Protectors]] stay a public care. Fellowships are the mill-share, the hull-wrights, and the road-mend; each has one habit they will not explain (grain on the lip, a silent empty walk, a shovel left in the bank). Body-licences unchanged, including the Hall-Keepers' Voice-ticket. One military note: watch, cohort, Retreat's wall, Hush-rate. The cohort eats at the thorn outside Eolvaeth and will not say why. Movements: pear-graft **past**; withdrawers **present**; disinherited **present**. Withdrawers stand in the passage and will not say why. The disinherited do not trade the old house-name and will not say why. World book untouched. L.8 not opened.

### Story L.8 — The weird, the made, and the found ✅ **DONE (2026-10-02)**
One magic hub. Daggerheart domains are crafts with jobs. A Spoken colour is not a spell. [[Conditions]] are not a second magic system and stay where they are. When a ruling needs a procedure, add a short pointer under `13 - Game`. Do not rewrite the SRD.

Constructs: a ruling. Condition labor and Answered craft already do most of that work. A construct, if one exists, has a maker and a problem. It is not a people.

Beasts: promote two or three working animals out of [[Ecology of the Turning]] into creature notes, each with a use and a fear. Not a bestiary. Do not restock the five adversaries. A Two-Bodied other self stays a person. Spirits only where a faith already has them (a door, a return), and not in a way that confirms the Other Hands. No unique-creature quota.

Artifacts: [[The Spent Leaf]] and [[The Closed Lamp]] stay. Add a few argued objects — some true, some embellished, one never found. Meaning first. Daggerheart stats only if a PC could hold the thing. A short list of weapons, coats, and materials that exist because a place needed them. No loot ladder. Do not fire the keystone.

Secrets: point [[Revelation Architecture]] and [[Reveal Index]] from Mysteries, Revelations, and Clues. Move a note only when the folder is its real home. Add at most two playable mysteries that are not the keystone and not a campaign plot. Do not confirm the Leaf-Mother or the Other Hands.

Skills: `memetic-depth`, `systemic-worldbuilding`. Ordinary sentences. A habit people will not explain is written as what they do.

- [x] Write one hub, [[How the Work Is Done]]. The nine domains are crafts with jobs. A Spoken colour is the warden's sentence. [[Conditions]] stay in `09 - Creatures/Conditions`. Do not reprint the SRD. Where the ruling needs a procedure, add a short pointer on [[At the Table]].
- [x] Write the construct ruling, [[A Made Thing]]. Condition labor and Answered craft already do the work. If a made thing is in a scene, it has a maker and a problem. It is not a people. Clank stay a Kind. Do not stock constructs.
- [x] Promote three working animals from the livelihood table: [[The Cart-Ox]], [[The Terrace Goat]], [[The Path Dog]]. Each has a use and a fear. Spirits only at a door and a return: [[Kin at the Door]]. Do not restock the five adversaries. A Two-Bodied other self stays a person. No unique-creature quota.
- [x] Leave [[The Spent Leaf]] and [[The Closed Lamp]] where they are. Add argued objects: [[The Other Chip]] and [[The Dry Slip]] (true), [[The Ribboned Knife]] and [[The Socket Ribbon]] (embellished), [[The One Knife]] (never found). Meaning first. A stat line only on the ribboned knife, and only as the SRD's smallest one-handed blade. Write [[What a Place Needed]]. No loot ladder. Do not fire the keystone. Do not name the cutter.
- [x] Point [[Revelation Architecture]] and [[Reveal Index]] from [[Mysteries]], [[Revelations]], and [[Clues]]. Move a note only when the folder is its real home. No note moved. Add [[The Name-Stone Bed]] and [[A Buyer for the Knife]]. Not the keystone. Not the opening. Do not confirm the Leaf-Mother or the Other Hands.
- [x] Do not update the world book. Do not open L.9, Epic S, or Epic M.

> **L.8 recorded decisions (2026-10-02).** One hub: [[How the Work Is Done]]. Domains are jobs. A Spoken colour is not a spell. Conditions stay in `09 - Creatures/Conditions`. Procedure pointer on [[At the Table]]. [[A Made Thing]]: maker and problem; not a people; Clank stay a Kind. Beasts: ox (ford over the axle; drivers still lead on a shallow ford and will not say why), goat (the house fears the wall and the well-share), dog (floodwater). [[Kin at the Door]] is the Old Ways meal and a Returned person. Five adversaries unrestocked. No unique quota. Objects: Other Chip true; Dry Slip true; Ribboned Knife embellished; Socket Ribbon embellished (they will not say why the cloth is a colour); One Knife never found. [[What a Place Needed]] has no ladder. The ribboned knife, if fought with, uses the SRD's smallest one-handed physical weapon and gains nothing from the ribbon. Secrets: Mysteries, Revelations, and Clues point at the architecture and the index. No note moved. Two mysteries: the name-stone bed, a buyer for the knife. Keystone unfired. Cutter unpicked. Leaf-Mother and Other Hands unconfirmed. World book untouched. L.9 not opened.

### Story L.9 — Sidebar honesty ✅ **DONE (2026-10-03)**
After L.1–L.8, empty folders that were decisions get a stub that says so, and leftovers get linked from the section MOCs. Archive atlas prototypes 1 and 2 and the label-trial image. Keep the Prototype 3 masters, the labeled overlays, the label scripts, and the reference painting. World book untouched.

- [x] Stub each empty folder whose emptiness is already a decision. The stub says the decision and points at the note that holds it. [[Schools]] · [[Traditions]] · [[Systems]] · [[Artifacts]] · [[Monsters]] · [[Unique]] · [[Weapons]] · [[Armor]] · [[Equipment]] · [[Materials]] · [[Historical Figures]] · [[Archaeology]] · [[Heroes]] · [[Villains]] · [[Movements Home]] · [[Rules]] · [[Mechanics]] · [[Encounters]] · [[Tables]] · [[Daggerheart]] · [[The Selected Handouts]]. Do not invent a school, a bestiary, a loot ladder, a fourth site, or a second copy.
- [x] Link those pointers from the section indexes: [[02 - History]] · [[05 - Factions]] · [[06 - Magic]] · [[08 - People]] · [[09 - Creatures]] · [[10 - Items]] · [[13 - Game]] · [[14 - Assets]]. A leftover that already had a home stays there. [[Movements]] stays under Organizations. Historical figures stay under `08 - People`. Magic artifacts stay in `10 - Items`. [[Conditions]] stay in `09 - Creatures/Conditions`. Procedure stays on [[At the Table]], [[Kind Heritage]], [[Dangers of the Turning]], and [[A Hidden Phoenix]].
- [x] Unused shelf, nothing decided: one line on [[00 - Core]] for Canon, Cosmology, and Themes. No essays. One line on [[06 - Magic]] for `Practices` and `Phenomena`. One line on [[14 - Assets]] for Images and References. Leave those folders empty.
- [x] Archive Prototype 1, Prototype 2, and the Heskoren label-trial image under `99 - Archive/Atlas/`. Point [[Atlas Prototype Review]] at the archive. Update [[The Atlas Sheets]] and [[Map Generation Tooling]] so no embed points at a missing file. Keep the Prototype 3 masters, the labeled overlays, the label scripts, the unlabeled handouts, and `references/World-Map-Reference.png`. Do not draw a new sheet.
- [x] Do not update the world book. Do not open Epic S or Epic M. Do not add a fourth mainland tongue, a Kind-nation, a plane, a sixteenth power, a graft on Kumbaan, a name for the cutter, or a date for the Tree.

> **L.9 recorded decisions (2026-10-03).** Decision folders point. They do not hold a second copy. One hub stays [[How the Work Is Done]]: [[Schools]], [[Traditions]], [[Systems]]. Magic [[Artifacts]] point at `10 - Items`. [[Monsters]] is not a bestiary. [[Unique]] has no quota. [[Weapons]], [[Armor]], [[Equipment]], and [[Materials]] point at [[What a Place Needed]]. [[Historical Figures]] stay under `08 - People`. [[Archaeology]] is [[The Low Wall]], [[The Seeing-Ring]], and [[The Dry Stair]]. [[Heroes]] and [[Villains]] point at [[Heroes and Villains]]. [[Movements]] stays under Organizations; [[Movements Home]] only points. [[Rules]], [[Mechanics]], [[Encounters]], [[Tables]], and [[Daggerheart]] point at the four procedure notes. [[The Selected Handouts]] keeps the unlabeled Prototype 3 sheets in Maps. Canon, Cosmology, and Themes stay empty. `Practices`, `Phenomena`, Images, and References stay empty. Prototype 1, Prototype 2, and the label-trial image are under `99 - Archive/Atlas/`. The reference painting stays. World book untouched. Epic S and Epic M were not opened.

> **L.5 done (2026-10-02).** The spur stops at [[Nelath]]. Next session may open L.6. This pass did not. L.6–L.9 stay coarse.

> **L.6 done (2026-10-02).** Stock hearth-glances are in [[Kinds of the Turning]]. Next session may open L.7. This pass did not. L.7–L.9 stay coarse. Epic S and Epic M were not opened.

> **L.7 done (2026-10-02).** The three criminal houses are under `05 - Factions/Criminal`. Fellowships, the watch, and three movements are in. Next session may open L.8. This pass did not. L.8–L.9 stay coarse. Epic S and Epic M were not opened.

> **L.8 done (2026-10-02).** The work, the made thing, three animals, the argued objects, and two afternoons are in. Next session may open L.9. This pass did not. L.9 stays coarse. Epic S and Epic M were not opened.

> **L.9 done (2026-10-03).** Empty shelves that were decisions now point at the notes that hold them. Prototype 1, Prototype 2, and the label-trial image are archived. Next session may open Epic S or Epic M. This pass did not.

---

## Epic S — The other seats
**Skill:** `story-sense` → `settlement-design`, `governance-systems`, `memetic-depth` · **Status:** ✅ **S.3 done (2026-10-03). Epic S complete.** The grill is recorded. Maiethorn's five seats, Strandoren's four seats, and Heskoren's three seats are written or refused. **Blast radius:** Med.

> The fifteen already exist on [[Powers of the Turning]]. Three seats are named: [[Maiethlir]] (city), [[Orentel]] (city), [[Eolvaeth]] (town). The other twelve were left unnamed on purpose, so a paragraph would not invent a capital. This epic is the pass that names a place or records the refusal. Beneath them the world still swarms. This epic does not census that swarm.

> **Do not.** Add a sixteenth power. Put a graft on Kumbaan. Capture the First Seat. Move [[Rothallo]] out of [[Orenbren]]. It is Orenbren's capital. Inner Close stays an alias. [[Brenledd]] gets a throne-city (S.0, 2026-10-03), and that note is S.2, not this pass. Make [[Harrow's Green]], [[Ornsael]], [[The Mill-hold]], [[Nelath]], or [[The First Bowl]] into a capital to tidy a stub. Date the Tree. Name the cutter. Staff every new seat with a cast. Update the world book unless asked. Draw the sheets here; that is Epic M. S.0 is recorded. S.1, S.2, and S.3 are written. Do not open Epic M from this epic. Write ordinary sentences. Do not use "compact" for a league or a group of towns. Do not use "a stranger means."

### Story S.0 — Grill before seating ✅ **DONE (2026-10-03)**
`grill-me` on this epic, before any seat is written. One question at a time. Each question carries a recommended answer. A question the vault already answers is not asked again. Record the answers on this story. S.1 stays closed until the grill is finished.

- [x] Walk the open calls one at a time: what "do not name a capital" means now; how many of the twelve may be cities; Brenledd's charter-town count; how much street a named place gets; whether any new mouth is allowed; whether a name-draw is shown before it is written; whether a new place gets one habit people will not explain.
- [x] Record the answers here. Do not write them onto the power notes during the grill.
- [x] Do not open S.1, S.2, or S.3 until those answers are on this story. Do not update the world book. Do not draw a sheet.

> **Answered (2026-10-03).** A capital is allowed when the power needs one and the place can say why. When there is a capital, prefer a large or huge city. Towns, villages, and hamlets are allowed as well. No seat has been written.
>
> **Answered (2026-10-03), next.** True medieval structure. Capitals and seats of power where they are needed. Large cities where they are expected. The rest scattered as towns, villages, and hamlets. A walled city that is all there is counts as a capital of sorts. No seat has been written.
>
> **Answered (2026-10-03), Orenbren.** The [[The Walled Book|Inner Close]] is Orenbren's capital. Smaller towns and villages around it as needed. It stays inside Orenbren. No settlement note has been written yet.
>
> **Answered (2026-10-03), First Seat.** The First Seat stays in the wood. The Inner Close is the civic capital. One power, not a sixteenth. The wood is not crowned. The Close is not the college.
>
> **Answered (2026-10-03), Brenledd.** Brenledd gets a throne-city. The name is not chosen yet.
>
> **Answered (2026-10-03), the throne-city.** It is a river-city on the upper end of large, one of the largest, where the council sits and the shared notes clear. The charter-towns stay around it. It is not a second [[Orentel]]. The name is not chosen yet. No note has been created yet.
>
> **Answered (2026-10-03), seven hearths.** The shared list is seven. The throne-city is one. Six charter-towns sit with it. Villages and hamlets are not on the list. The six towns are not named in this pass. Nidtol stays the hearth-name people recite, and is not the throne-city. Field, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261008 --register conservative --count 80`. Shown: Meonsai 6, Bruthei 9, Raitin 16, Breolta 28, Momeil 33, Meilre 58. Thrown back: Braelsu beside Braesu, Larnaena beside Larbril, Brulrei (brul), Lireolbrath beside Lirorn, Murtol beside Nidtol, Neonnun (neo, nun), Breolleor (leo), Breinenlei and Raineon and Laithrein (rein, rain), Railvolthun (rail), Molli, Lairro (lair), Runtun (run), Muntheon (theo), Mulbrairthen (mul), Seillarthur (arthur), Bravur and Braveil (brave), Mailror (mail), and the th-stacks a table will not say.
>
> **Answered (2026-10-03), Raitin.** The user picked Raitin, position 16. Brenledd's throne-city. No note has been created yet.
>
> **Answered (2026-10-03), Leddvael's port.** [[Leddvael]] gets a large port city on its own stretch of coast, where the signing-watch sits. It is slightly smaller than [[Orentel]]. It competes with the Ledger Coast, and it wins in some ways and loses in others. Towns and villages along the rest of that coast. The [[The Book-Hands|Book-Hands]] still have no seat of their own. Field, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261009 --register conservative --count 80`. Shown: Naenor 5, Mairsa 8, Reilnai 20, Tilbreo 21, Maenreil 63, Veornei 69. Thrown back: Millil (mil), Taermen beside Taeren, Silo, Nuroth beside Rothallo, Reitein beside Raitin, Tulvaevon beside Tulvaeril, Leinbru beside Seinbrun, Noltul beside Nidtol, Neilvo, Monthin (month), Bresil, Lamin beside Tasain and Raitin, and the th-stacks a table will not say.
>
> **Answered (2026-10-03), Naenor.** The user picked Naenor, position 5. Leddvael's port city. No note has been created yet.
>
> **Answered (2026-10-03), Trenledd's city.** [[Trenledd]] gets a large city on the Chart-run, days inland of [[Orentel]], where the roll is kept. It is wealthy and opulent, and it shows the money. People go there to make big money, because the family already has it, or because they want it. Towns and villages through the filed country. The governing throat stays unnamed. Field, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261010 --register conservative --count 80`. Shown: Teonreil 6, Rinvor 11, Volnae 13, Lunbra 40, Tanteon 57, Veoton 62. Thrown back: Neolbreoth (neo), Leithron (Leith), Sunel (sun), Mainmae (main), Railan beside Raitin, Nasan beside Tasain, Rainlun (rain), Rothalve beside Rothallo, Thulleo and Leolir and Leonri (leo), Theorel and Sultheor (theo), and the th-stacks a table will not say.
>
> **Answered (2026-10-03), Lunbra.** The user picked Lunbra, position 40. Trenledd's opulent city on the Chart-run. No note has been created yet.
>
> **Answered (2026-10-03), the Night Shore.** [[Netstrand]] gets a large harbour city on the west and south face, where a far crossing is quoted and a lamp can be kept on a name. Smaller than [[Orentel]], because the far run is thinner than the Old Crossing. Towns and villages along the rest of the shore. The unlit berth stays one berth in that city, with no house attached. Field, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261011 --register conservative --count 80`. Shown: Laelsain 1, Ruren 5, Braetu 11, Rulmar 20, Seolun 68, Vemae 78. Thrown back: Railtholvaer (rail), Romul (mul), Veintheoth (theo), Munrunein (run), Loneo and Neorle (neo), Sabraini (rain), Veotho beside Veoton, Terbrail (rail), Milsilae (mil), Neosaibrol (neo), Rusailrae (sail), Sirnen (sir), Brothvain (vain), Naerlu beside Naenor, Lulveo beside Lunbra, Tannail (nail), and the th-stacks a table will not say.
>
> **Answered (2026-10-03), Braetu.** The user picked Braetu, position 11. The Night Shore's harbour city. No note has been created yet. Strandoren's four seats are named in S.0. No settlement note has been written.
>
> **Answered (2026-10-03), Ornled's seat.** [[Ornled]] gets a town on the brink of a small city, where the slate is kept and a beach-fee can be paid when a hull arrives. Villages and hamlets in the pockets around it. That town is the seat. Field, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261012 --register conservative --count 80`. Shown: Sanbreo 6, Vairtain 8, Tolsel 18, Broran 34, Letair 63, Ranto 75. Thrown back: Brothreo (broth), Tailritei (tail), Mainen (main), Rairneoth and Neorith (neo), Rainvailme (rain), Braivainseo (vain), Lubrail (rail), Sethmabri (seth), Sirsuth (sir), Semul (mul), Vele beside Vemae, Nonnae beside Volnae, Seothlun beside Seolun, Rothmaenlith beside Rothallo, Rithme (rhythm), Loten beside Lonteith, Lumunon beside Lunbra, and the th-stacks a table will not say.
>
> **Answered (2026-10-03), Sanbreo.** The user picked Sanbreo, position 6. Ornled's town on the brink of a small city. No note has been created yet.
>
> **Answered (2026-10-03), Vaelhesk.** No new city, and no new name. The land stays the seat. Villages and hamlets stay on the old greens. [[The First Bowl]] stays the guest-grove it already is. A traveler is pointed at a door.
>
> **Answered (2026-10-03), Saelvaeth's town.** [[Saelvaeth]] gets one town, where the march-voice stands. Other towns where a graft has taken. Hamlets and waiting clusters between them. [[Harrow's Green]] stays as it is. The three hamlets past the ford stay the three hamlets. The name is not chosen yet. No note has been created yet.
>
> **Answered (2026-10-03), the epithets.** Keep them for now. The user was asking, not opening a rewrite. "The Sown Waiting" stays the spoken line. The same kind of line stays on the other powers. No sweep.
>
> **Answered (2026-10-03), the march-town's name is open.** Field, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261013 --register conservative --count 80`. Shown: Rulvai 8, Natai 13, Tilbrai 14, Laevo 17, Teomar 31, Brelvol 44. Thrown back: Rimeitheo (theo), Monmail (mail), Raintol beside Ranto, Leinuthsail (sail), Rainneon (rain, neo), Runbrae beside Lunbra, Norbrain (rain), Vonna beside Volnae, Nannar beside Naenor, Thaerleithneth (leith), Veota beside Votaer, Brulbrir (brul), and the th-stacks a table will not say.
>
> **Answered (2026-10-03), Natai.** The user picked Natai, position 13. Saelvaeth's march-town. No note has been created yet. The twelve seats are named or refused in S.0. No settlement note has been written.
>
> **Answered (2026-10-03), the draw.** A name is shown before it is written. The user picks. That is how Rothallo through Natai were chosen.
>
> **Answered (2026-10-03), the street.** When the notes are written, a city gets the ways in, the place the work happens, and one tension. A town gets the gate, the work, and one tension. No ward-grid. Vaelhesk gets no new street. The detail comes from notes already in the vault. It is not grilled place by place. The sheets wait for Epic M.
>
> **Answered (2026-10-03), mouths.** A new seat may have new people, on a scale. A capital has more than one. One of the largest cities has more than one. A large city has one. Towns and villages are skipped unless a person belongs there. No person has been written.
>
> **Answered (2026-10-03), 3, 2, 1.** Capitals get three new people. One of the largest cities gets two. A large city gets one. Rothallo, Seinbrun, and Raitin get three. Votaer gets two. Naenor, Lunbra, and Braetu get one. Larbril gets one, because it is the only city of that power. Natai gets one, because the town exists so someone can be blamed. The person at Lunbra is not the crown. That throat stays unnamed. Tasain, Sanbreo, Vaelhesk, the six charter-towns, and the villages get no new person. Narol and Vathne stay the people already written. No person has been written yet.
>
> **Answered (2026-10-03), habits.** More where there is more to do. A habit is an ordinary sentence: what people do, and that they will not say why. Habits already on a note count toward the number. Add only the shortfall. Capitals sit between 5 and 10. Below a capital the number steps down. **Capitals:** Orentel 9, Raitin 8, Seinbrun 7, Rothallo 6. **Largest city:** Votaer 4. **Large cities:** Naenor, Lunbra, Braetu, and Maiethlir, 3 each. **Medium:** Larbril 2. **Towns and played squares:** Tasain, Sanbreo, Natai, Eolvaeth, Harrow's Green, Ornsael, the Third Hearth, the Mill-hold, the First Bowl, and Nelath, 1 each. The three hamlets keep one among them if the note does not already have it. Villages with no walked note get none. Vaelhesk gets no new place. The six charter-towns get none in this pass. When S.1–S.3 are written, the places already done on that ground are topped up to these numbers. No habit has been written in this story.
>
> **Answered (2026-10-03), words.** Ordinary sentences. "Compact" is not the word for a league or a group of towns. "A stranger means" is not a test. The plain-prose pass removed riddles and the labels Inscrutable, leave it, and 20%. It did not give the Inner Close a place-name. "The Close" and "Inner Close" stay as the old description until a real name is chosen.
>
> **Answered (2026-10-03), the name.** Draw a spoken name from the conservative list and show it before any note changes. The user picks. "Inner Close" stays an alias. New liturgical compounds stay frozen. Field, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261003 --register conservative --count 40`. Shown: Breolma 4, Reolnain 5, Tairthen 16, Brortaer 22, Leinren 23, Rothallo 28. Thrown back from that field: English stems (Mortin, Tensen, Neosuth, Thuleith, Breitein, Vurleon, and the theo/neo draws), th-stacks a table will not say, Laethmaeth beside Maieth, Railnal and Venlaith beside Raillath.
>
> **Answered (2026-10-03), Rothallo.** The user picked Rothallo, position 28. Orenbren's capital. Inner Close remains an alias. No note has been renamed yet.
>
> **Answered (2026-10-03), Maiethvael.** Maiethvael gets a capital. It is a large city, with smaller towns and villages around it. Not [[Maiethlir]]. Not [[The Down-Bank]]. The name is drawn and shown before it is written. Field, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261004 --register conservative --count 40`. Shown: Seinbrun 1, Laerthaer 6, Vireoth 7, Seithna 9, Vilmol 22, Braeveir 34. Thrown back: Romanrun, Rulbrain, Sailsailthi, Mollei, Theonnai, Mateth beside Maieth, Leinneor beside Oren, Bronthul beside Bren, and the th-stacks a table will not say.
>
> **Answered (2026-10-03), Seinbrun.** The user picked Seinbrun, position 1. Maiethvael's capital. No note has been renamed or created yet.
>
> **Answered (2026-10-03), Saelthael.** One medium city, close to something people already want to be near. Not a huge capital. [[Ornsael]] is not renamed into it. Where it sits is still open. No note has been created yet.
>
> **Answered (2026-10-03), the Well-wash.** The city sits where the west road meets the Well-wash, short of the pass. People are close to water and to the walk west. [[Ornsael]] stays the smaller well-town, farther into the dry. The [[The Dry Stair|Dry Stair]] is not the reason for the city. Field, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261005 --register conservative --count 40`. Shown: Larbril 4, Tethraith 9, Brulvol 18, Tubreo 28, Leithrae 32, Seollin 40. Thrown back: Tunsir (sir), Reinvan (rain), Neothson (son), Nimaeth beside Maieth, Lirto and Lirebrul beside Lirorn, Maelve, Nethair beside the Neth- clergy names, and the th-stacks a table will not say.
>
> **Answered (2026-10-03), Larbril.** The user picked Larbril, position 4. Saelthael's medium city on the Well-wash. No note has been created yet.
>
> **Answered (2026-10-03), the Hinge port.** [[The Hinge Shore]] gets a port city, and it is one of the largest. The crossing is why that many people are there. Hulls are classified on those quays, and the Hush-rate is charged there. It faces [[Orentel]] across the Old Crossing and is not a second Orentel. Towns and villages along the rest of the shore. Field, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261006 --register conservative --count 40`, with later positions from the same seed at count 80. Shown: Tulvaeril 6, Lomainbro 19, Tirril 27, Votaer 35, Lanmeor 58, Braesu 74. Thrown back: Thinleo (leo), Theorvaer and Theonur (theo), Brethreinsir (sir), Roneilsail (sail), Rormonrein (rein), Nunvove (nun), Nevain and Vainteon (vain), Lineir (line), Rothmir beside Rothallo, Brinbrul beside Larbril, Mulsor, and the th-stacks a table will not say.
>
> **Answered (2026-10-03), Votaer.** The user picked Votaer, position 35. The Hinge Shore's great port city. No note has been created yet.
>
> **Answered (2026-10-03), Lirorn's town.** [[Lirorn]] gets a walled town in a sheltered valley below the Shelf-gate, where the west road comes down and the levy is taken, and where people can stay the winter. That town is the seat. Villages and hamlets stay on the shelves and at the passes. The Noon Pass stays a pass. Not a great city. Not a second [[Maiethlir]]. Field, algorithm 1: `python3 "14 - Assets/Names/generate_names.py" --seed 20261007 --register conservative --count 80`. Shown: Nennae 18, Volthei 26, Tormer 37, Tasain 66, Meolsor 76, Reiva 79. Thrown back: Maeleoth and Leonna (leo), Sonlur (son), Sunva (sun), Railsin (rail), Lubrain and Meobrain (rain), Theotolon and Breortheon (theo), Braerbril and Thaebril beside Larbril, Rothuruth beside Rothallo, Nathlir beside Lirorn, Neornil (neo), Vathsemen, Runthei (run), Maenlair (lair), Rasin (raisin), and the th-stacks a table will not say.
>
> **Answered (2026-10-03), Tasain.** The user picked Tasain, position 66. Lirorn's walled town below the Shelf-gate. No note has been created yet. Maiethorn's five seats are named in S.0. No settlement note has been written.

### Story S.1 — Maiethorn's unnamed seats ✅ **DONE (2026-10-03)**
[[Maiethvael]] (capital [[Seinbrun]]), [[Orenbren]] (capital [[Rothallo]], still called the Inner Close), [[Saelthael]] (medium city [[Larbril]], on the Well-wash), [[The Hinge Shore]] (port [[Votaer]]), [[Lirorn]] (walled town [[Tasain]], below the Shelf-gate). The S.0 answers are the decisions. A city gets the ways in, the work, and one tension. A town gets the gate, the work, and one tension. No ward-grid. The First Seat stays in the wood.

- [x] Write [[Seinbrun]]. Maiethvael's capital. A large city, with smaller towns and villages around it, unnamed. Not [[Maiethlir]]. Not [[The Down-Bank]]. Seven habits. Three new people: [[Vuthbraen]], [[Breillai]], [[Raermu]]. Point [[Maiethvael]] at the seat.
- [x] Write [[Rothallo]]. Orenbren's capital. The place still called the Inner Close. Inner Close stays an alias. It stays inside Orenbren. The First Seat stays in the wood. The wood is not crowned. Rothallo is not the college. Six habits. Three new people: [[Brimaen]], [[Breolnir]], [[Methei]]. Point [[Orenbren]] and [[The Walled Book]] at the seat. Do not replace Delamem or Talnin.
- [x] Write [[Larbril]]. Saelthael's medium city, where the west road meets the Well-wash, short of the pass. [[Ornsael]] stays the smaller well-town, farther into the dry. The Dry Stair is not the reason. Two habits. One new person: [[Brormei]]. Point [[Saelthael]] at the seat.
- [x] Write [[Votaer]]. The Hinge Shore's port, one of the largest, because the crossing is why the people are there. Hulls are classified there. The Hush-rate is charged there. It faces [[Orentel]] and is not a second Orentel. Towns and villages along the rest of the shore stay unnamed. Four habits. Two new people: [[Tumair]], [[Lertho]]. Not a Selkie nation. Point [[The Hinge Shore]] at the seat.
- [x] Write [[Tasain]]. Lirorn's walled town in a sheltered valley below the Shelf-gate, where the west road comes down and the levy is taken. Villages and hamlets stay on the shelves. The Noon Pass stays a pass. One habit. No new person. [[Narol of the Pass]] stays. Not a Tengu empire and not a Fox kingdom. Point [[Lirorn]] at the seat.
- [x] On Maiethorn ground already written, add only the missing habits. [[Maiethlir]] to three (the loud thaw already counted). [[The Third Hearth]] to one. [[Ornsael]], [[The Mill-hold]], and [[Nelath]] already had one. Do not rename them. Do not give them a new person. Leave Heskoren and Strandoren places, including [[Orentel]], [[Eolvaeth]], [[Harrow's Green]], [[The First Bowl]], and the three hamlets.
- [x] Do not update the world book. Do not draw a sheet. Do not open S.2, S.3, or Epic M. Do not add a sixteenth power. Do not put a graft on Kumbaan. Do not capture the First Seat, date the Tree, or name the cutter.

> **S.1 recorded decisions (2026-10-03).** One home each under `04 - Settlements`. Visibility set at birth. Street taken from notes already in the vault. Epithets left on the power notes. Ordinary sentences. No "compact" for the lodging-country in the new lines. No "a stranger means."
>
> **Seinbrun.** Large city, off the Core-thaw, a day's argument from Maiethlir. The work is the furnished hall. The tension is the hymn and the net. Seven habits. Witness-land: given names only. Algorithm 1. `python3 "14 - Assets/Names/generate_names.py" --seed 20261014 --register conservative --count 80` — Vuthbraen 31, Breillai 43, Raermu 56. Thrown back: th-stacks; theo; sir; mail; nail; beside Maieth; sun; beside Rothallo; neo; vain; Seine; beside Nelath; beside Nirsei; saith; tilt; laith; thane.
>
> **Rothallo.** Walled capital, one day from the wood. Alias Inner Close moved onto the city note. The Walled Book keeps the class and links the place. Beds outside, Book inside. Six habits. List-land: neighbour says the given name; clerk says the house first. Algorithm 1. `python3 "14 - Assets/Names/generate_names.py" --seed 20261015 --register conservative --count 80` — Breolnir 30 / Tethnae 63; Brimaen 39 / Lanbru 36; Methei 70 / Sithlaen 76. Delamem and Talnin stay. Hithaen is not Methei. Thrown back: rein; leo; theo; laith; mol; run; rail; beside Seinbrun; silver; beside Maethaem; beside Rothallo; beside Raitin; sun; brave; nail; th-stacks; brul; month.
>
> **Larbril.** Medium city at the road and the wash, short of the Shelf-gate. Ornsael stays farther into the dry. Two habits. Algorithm 1. `python3 "14 - Assets/Names/generate_names.py" --seed 20261016 --register conservative --count 80` — Brormei 69. Thrown back: brul; lair; nun; beside Natai; theo; sun; mul; beside Nirsei; mil; roman; sir; run; rain; main; broth; th-stack; tail.
>
> **Votaer.** Classification quay and the Hush-rate. Faces Orentel. Four habits. Algorithm 1. `python3 "14 - Assets/Names/generate_names.py" --seed 20261017 --register conservative --count 80` — Tumair 33, Lertho 50. Thrown back: th-stacks; thane; vain; neo; beside Rothallo; beside Seinbrun; run; lair; beside Maieth; beside Volnae; sin; rail; their; rain. Taerso stays the historical mouth.
>
> **Tasain.** Gate, levy, one habit (shelf-snow left on the gate-stone until it is water). Narol stays. Noon Pass stays a pass.
>
> **Already written.** Maiethlir: used cups, and a thread on the stylus, added to the loud thaw. Third Hearth: the broom across the lintel. Ornsael, the Mill-hold, and Nelath were left at the habit they already had. A later note must not explain these habits, and must not turn them into a power, a relic, or a rite. World book untouched. S.2 not opened. Epic M not opened.

### Story S.2 — Strandoren's unnamed seats ✅ **DONE (2026-10-03)**
[[Brenledd]] (throne-city [[Raitin]], upper end of large, a river-city, seven hearths, S.0), [[Leddvael]] (port city [[Naenor]], slightly smaller than Orentel, S.0), [[Trenledd]] (opulent city [[Lunbra]], on the Chart-run, S.0), [[Netstrand]] (harbour city [[Braetu]], smaller than Orentel, S.0). The S.0 answers are the decisions. A city gets the ways in, the work, and one tension. No ward-grid. [[Orentel]] is not redrawn. A new harbour is not a second Orentel.

- [x] Write [[Raitin]]. Brenledd's throne-city. A river-city on the upper end of large, one of the largest, where the council sits and the shared notes clear. Six charter-towns stay around it, unnamed. Seven hearths. Raitin is one. Nidtol stays the recited hearth-name, and is not the throne-city. The league stays a league of hearths. It does not become one house. Not a second [[Orentel]]. Eight habits. Three new people: [[Turvo]], [[Nubo]], [[Sulnu]]. Point [[Brenledd]] at the seat. Replace the line that said Brenledd has no capital.
- [x] Write [[Naenor]]. Leddvael's port, on its own stretch of coast, where the signing-watch sits. Slightly smaller than Orentel. It competes with the Ledger Coast, and it wins the term and loses the berth. Towns and villages along the rest of that coast stay unnamed. The Book-Hands still have no seat, and they still do not rewrite Terms. Three habits. One new person: [[Derdil]]. Point [[Leddvael]] at the seat.
- [x] Write [[Lunbra]]. Trenledd's large city on the Chart-run, four to eight days upriver of Orentel, where the roll is kept. Wealthy, and it shows the money. Towns and villages through the filed country stay unnamed. The governing throat stays unnamed. Three habits. One new person: [[Vamar]], house Melro. That person is not the crown. Point [[Trenledd]] at the seat.
- [x] Write [[Braetu]]. The Night Shore's harbour on the west and south face, where a far crossing is quoted and a lamp can be kept on a name. Smaller than Orentel, because the far run is thinner than the Old Crossing. Towns and villages along the rest of the shore stay unnamed. The unlit berth stays one berth, with no house attached. The dark book stays a dark book. Selkie stay common, and stay off the flag. Three habits. One new person: [[Mursur]]. Not a second Orentel. Point [[Netstrand]] at the seat.
- [x] On Strandoren ground already written, add only the missing habits. [[Orentel]] to nine. The salt on the Tree's roots already counted. Do not rename Orentel. Do not give it a new person. Do not move the White Note. Leave [[Denlad]] and the White Note at what they already are. Leave Heskoren places for S.3, including [[Eolvaeth]], [[Harrow's Green]], [[The First Bowl]], and the three hamlets.
- [x] Do not update the world book. Do not draw a sheet. Do not open S.3 or Epic M. Do not add a sixteenth power. Do not put a graft on Kumbaan. Do not capture the First Seat, date the Tree, or name the cutter. Do not name the six charter-towns. Do not give them a habit or a person.

> **S.2 recorded decisions (2026-10-03).** One home each under `04 - Settlements`. Visibility set at birth. Street taken from notes already in the vault. Epithets left on the power notes: the Hearth-League, the Reckoned Gift, the Worn Count, the Night Shore. Ordinary sentences. No "compact" for the league in the new lines. No "a stranger means."
>
> **Raitin.** River-city behind and between the premier coast. The work is the council hall. The tension is a note that clears here and can still die in the next hearth. Eight habits. Not a person-list. Algorithm 1. `python3 "14 - Assets/Names/generate_names.py" --seed 20261018 --register eroded --count 80` — Nubo 27, Turvo 42, Sulnu 60. Thrown back: son, run, sun, sir, nun, sin, mort, roman, beside Volnae, beside Nidtol, beside Vonti, and stacks a table will not say.
>
> **Naenor.** Signing-watch on its own coast. Wins the term. Loses the berth. Three habits. Algorithm 1. `python3 "14 - Assets/Names/generate_names.py" --seed 20261019 --register eroded --count 80` — Derdil 60. Thrown back: silo, vain, nun, mul, mol, norse, valid, night, beside Valen, beside Natai, beside Nirsei.
>
> **Lunbra.** Roll-room on the square that shows the money. Four to eight days up the Chart-run. Three habits. List-land: neighbour says Vamar; clerk says Melro first. Vamar is not the throat. Algorithm 1. `python3 "14 - Assets/Names/generate_names.py" --seed 20261020 --register eroded --count 80` — Vamar 33, house Melro 76. Thrown back: sun, mol, mil, sir, run, tense, valid, beside Naenor, beside Lunbra, beside Votaer, beside Tasain, beside Valen. Dirrol stays the historical column.
>
> **Braetu.** Quote-desk and the dark book. Eight to fourteen days coasting from Orentel. Two to four weeks on the West Water. Three habits. The unlit berth stays one berth. Algorithm 1. `python3 "14 - Assets/Names/generate_names.py" --seed 20261021 --register eroded --count 80` — Mursur 35. Thrown back: sir, nun, mol, sin, son, beside Larbril.
>
> **Already written.** Orentel: eight habits added to the salt on the roots. Denlad and the White Note were not changed. Heskoren places were not changed. A later note must not explain these habits, and must not turn them into a power, a relic, or a rite. World book untouched. S.3 not opened. Epic M not opened.

### Story S.3 — Heskoren's unnamed seats ✅ **DONE (2026-10-03)**
[[Ornled]] (town [[Sanbreo]], on the brink of a small city, S.0), [[Vaelhesk]] (no city; the land stays the seat, S.0), [[Saelvaeth]] (march-town [[Natai]], S.0). Harrow's Green stays as it is. The twelve seats are named or refused. Thin country. A town is the likely answer, and a refusal is allowed. Vaelhesk's land can remain the seat; [[The First Bowl]] stays a guest-grove. Saelvaeth does not absorb [[Harrow's Green]]. [[Eolvaeth]] stays Vaethorn's town and is not given wards here. The S.0 answers are the decisions. A town gets the gate, the work, and one tension. No ward-grid. Vaelhesk gets no new street.

- [x] Write [[Sanbreo]]. Ornled's town, on the brink of a small city, where the slate is kept and a beach-fee can be paid when a hull arrives. Villages and hamlets in the pockets stay unnamed. The town is the seat. It is still a town. One habit. No new person. Vathne stays the slate. Point [[Ornled]] at the seat. Replace the line that said the seat is unnamed.
- [x] Record [[Vaelhesk]]'s refusal. No new city and no new name. The land stays the seat. Villages and hamlets stay on the old greens. [[The First Bowl]] stays the guest-grove. A traveler is pointed at a door. No new street. No new place-note. No new person. The line stays a refusal.
- [x] Write [[Natai]]. Saelvaeth's town, where the march-voice stands. Other towns where a graft has taken stay unnamed. Hamlets and waiting clusters between them stay unnamed. [[Harrow's Green]] stays as it is, and stays out of the seat. The three hamlets stay the three hamlets. One habit. One new person: [[Dumu]]. That person is not Haelin, not Tora, and not a warden of Harrow's Green. Point [[Saelvaeth]] at the seat. Replace the line that said the seat is unnamed.
- [x] On Heskoren ground already written, add only the missing habits. [[Eolvaeth]] already had one (the wet leaf on the spring). Do not rename it. Do not give it a new person. [[Harrow's Green]] to one. No new person. [[The First Bowl]] to one. The sour bread does not count. No new person. Delvor, Vilraet, and Brudu stay. The three hamlets already had one (the cup on the ford-rock). Do not explain the cup. No new person. Leave Maiethorn and Strandoren places at what they already are.
- [x] Do not update the world book. Do not draw a sheet. Do not open Epic M. Do not add a sixteenth power. Do not put a graft on Kumbaan. Do not capture the First Seat, date the Tree, or name the cutter. Do not name the other towns where a graft has taken. Do not give them a habit or a person.

> **S.3 recorded decisions (2026-10-03).** One home each under `04 - Settlements`, except Vaelhesk, which stays a refusal on the power note. Visibility set at birth. Street taken from notes already in the vault. Epithets left on the power notes: the Outer Ledger, the Far Yield, the Sown Waiting. Ordinary sentences. No "compact" for the pockets, the old greens, or the towns between grafts. No "a stranger means."
>
> **Sanbreo.** Shore gate, slate on the wall, one tension (a hull can pay, and a person can still slide). One habit (the coin stays on the sill until the hull is gone). No new person. Vathne stays the line on the slate.
>
> **Vaelhesk.** No place-note. The land is the seat. A traveler is pointed at a door. The First Bowl stays the guest-grove.
>
> **Natai.** Town gate on the road between grafts. The work is the march-voice. One habit (the latch on the post). One person. Witnessed speech, worn register. Algorithm 1. `python3 "14 - Assets/Names/generate_names.py" --seed 20261022 --register worn --count 80` — Dumu 46. Thrown back: English stems and th-stacks, and names beside Volnae, Haelin, Brudu, Delvor, Vathne, Sorel, Meirim, Derdil, Nelath. Full list on the seat note. Harrow's stays out of the seat.
>
> **Already written.** Eolvaeth was left at the wet leaf. Harrow's Green: the cistern-dipper hung toward the stream. The First Bowl: a rye-straw on the door-path's first stone. The sour bread stays explained, and does not count. The three hamlets were left at the cup. The cup was not explained. A later note must not explain these habits, and must not turn them into a power, a relic, or a rite. World book untouched. Epic M not opened.

---

## Epic M — Town sheets and the new seats
**Skill:** `settlement-design` · **Status:** ✅ **complete (2026-10-05).** M.1–M.3 done 2026-10-03. M.5 done 2026-10-04. M.4 done 2026-10-05. **Blast radius:** Low.

> Paintings follow notes. If a painting and a note disagree, the note wins. New city and town sheets are new paintings, not crops of the regional masters. The image model does not write. Pillow labels from the notes. Record each sheet on [[The Atlas Sheets]]. Unlabeled Prototype 3 sheets stay the handouts. A civic Hand is a broad dark hardwood filling its square, not the First Hand, and not a glow. Thaeloren remains the only exceptional canopy. No capital star. No world book unless asked.

> **Pointers (2026-10-03).** Capitals, large cities, and important towns get a plain pointer and a label on the maps that already show that ground: [[The Known Map]], the world overlay, and the continent and region overlays. A reader has to be able to find the place. The painting stays the painting. Pillow on the existing master. No capital star. A mark only where the notes already place the place. Do not drop a name on an incidental roof cluster. [[Vaelhesk]] gets no settlement dot. The land stays area-type. Unlabeled handouts stay unlabeled.

> **Order.** M.1 and M.2 use squares that already have streets. They may open before Epic S. M.3 waits until S has named or refused the place. A refusal gets no city plate. M.4 can be drawn before those plates. A reader finds the place on the map that already shows that ground.

### Story M.1 — Details the two cities still lack ✅ **DONE (2026-10-03)**
[[Orentel]]: a pier sheet of the First Quay, the Third, and the White Note, with the Rise left off it so the Tree stays inland. [[Maiethlir]]: the Grove Bank as a road view, the wood a dark behind the gate, the First Seat unnamed. Do not redraw the city plates or the heart and drop sheets unless a note has changed.

- [x] Read [[Orentel]], [[Maiethlir]], and [[The White Note House]]. Use only the names those notes already place on these frames. If a painting and a note disagree, the note wins.
- [x] One **Orentel** pier sheet, `Orentel-Piers-Atlas.png`, labeled with `label_orentel_piers.py`. The frame is the tide. The Rise stays off the inland edge, so the Tree, the square, and the salt on the roots stay on the drop sheet. The Drop's quay end may enter from that edge. Label only First Quay, The Third, and White Note. The First Quay is the Salt Walk's old landing: berths 1–4 held, berth 5 earth, unlettered. The Third is the north-side quay. The White Note is one desk-house on that north side, not the council, not the crown, and not a palace. Mataero's loft stays off this sheet with the Rise. Hallowquay, the inland yard, the Chart mouth, the Crossing-mouth, Denlad, the release-house, and the leaf-lots stay off the labels. No city wall. No capital star.
- [x] One **Maiethlir** Grove Bank sheet, `Maiethlir-Grove-Bank-Atlas.png`, labeled with `label_maiethlir_grove_bank.py`. The frame is the road, not the square. Grove Bank is the north road from the wood, one or two days, and it is not the Near Mile. The gate is in the old flood-wall, and the Motherwood is a dark behind that gate. Label Grove Bank. Do not label the wood. The First Seat stays unnamed in that wood: no college, no throne, no canopy-ring, no mark. Do not draw Thaeloren's exceptional canopy. The civic Tree on the Slow Water stays on the heart sheet. Do not redraw Loft Row, the tablet-hall, the Down Gate, or the Wall Path. Do not name Maiethvael's seat. The Down Gate is not that seat.
- [x] These are new paintings, not crops of Sacred Core, Chart-run, Old Crossing, the continent masters, or the four city paintings already in the atlas. Masters are 1152×864. West is left. Match the dark weather of the city paintings, and fill the frame at city scale. If a painting reads as a village, replace it. Do not ask the image model to write. Pillow labels in the same hand as `label_orentel_drop.py`: Liberation Serif, a halo, a leader only when the name would sit on the roofs. Do not redraw or relabel Maiethlir-City, Orentel-City, Maiethlir-Heart, or Orentel-Drop. Do not put Nelath, Raillath, Denlad, or Tunral on any sheet. Do not name Seinbrun, the six charter-towns, or any seat this story did not already place. Unlabeled Prototype 3 sheets stay the regional handouts.
- [x] Record both sheets on [[The Atlas Sheets]]. Add the two scripts beside `label_orentel_drop.py` and `label_maiethlir_heart.py` in [[Map Generation Tooling]]. Do not update the world book. Do not open M.2, M.3, or M.4. Do not add a sixteenth power. Do not put a graft on Kumbaan. Do not capture the First Seat, date the Tree, or name the cutter. Do not add a person. Do not add a habit. Do not explain a habit that is already written.

> **M.1 recorded decisions (2026-10-03).** `Orentel-Piers-Atlas.png` and `Maiethlir-Grove-Bank-Atlas.png` are new paintings, not crops of Sacred Core, Chart-run, Old Crossing, the continent masters, or the four city paintings already in the atlas. The image model was not asked to write. Pillow on those masters: `label_orentel_piers.py` and `label_maiethlir_grove_bank.py`. The pier sheet is the tide. The Rise stays off the inland edge. The labels are First Quay, The Third, and White Note. The White Note is one desk-house on the north quay. The Grove Bank sheet is the north road, the gate in the old flood-wall, and the wood a dark behind that gate. The wood is not labeled. The First Seat is not marked. No capital star. The city plates, the heart sheet, and the drop sheet were not redrawn. World book untouched. M.2, M.3, and M.4 were not opened.

### Story M.2 — Towns and squares already seated ✅ **DONE (2026-10-03)**
One sheet each, at the size the note already claims. [[Rothallo]] is [[The Walled Book|the Inner Close]]: Orenbren's walled capital, one day from the wood. People still say the Inner Close. It is the same place, not a second town. The plate stays for M.3. [[Eolvaeth]]: a town in the waiting vale, not a city. [[Harrow's Green]]: the live-front square. [[The Mill-hold]]: a sick Hand, the canopy visibly wrong. [[Ornsael]]: a Tree beside the well. [[Nelath]]: the road ends at the boughs. [[Ndenjoo]]: the Feeding Hill, and no Tree.

- [x] Read [[Rothallo]] and [[The Walled Book]] before deciding the Inner Close. Rothallo is Orenbren's walled capital, one day from the wood. People still say the Inner Close. It is the same place, not a second town. Do not paint it in M.2. Leave the plate for M.3. Do not open M.3.
- [x] Read [[Eolvaeth]]. One town sheet, `Eolvaeth-Atlas.png`, labeled with `label_eolvaeth.py`. The frame is the fold: a maybe-Hand at the centre, the spring, the gift-hall, and camp-streets that learned to winter. No walls. The spring is not a mile-shrine. There is nothing to climb. Do not draw Harrow's canopy, and do not show that luck. Label only the Tree, the spring, and the gift-hall. Do not label Vaethod. Do not explain the wet leaf.
- [x] Read [[Harrow's Green]]. One town sheet, `Harrows-Green-Atlas.png`, labeled with `label_harrows_green.py`. The live-front square. No walls. A Hand at the centre, the stone in the square, the Rise-water at the foot of the rise. The oldest lintels face the Tree. The hamlets can be a sightline. Do not name them, and do not put Brenod, Vaelun, or Ornath on this sheet. Do not relabel this square into Nelath. Do not build a fortress on the rise. Label only the Tree and the stone. Do not explain the cistern-dipper.
- [x] Read [[The Mill-hold]]. One town sheet, `Mill-hold-Atlas.png`, labeled with `label_mill_hold.py`. A mill-town. No walls. The Hand is sick this year: leaves late and colourless at the edges, the canopy visibly wrong, still a hardwood and not a glow. The mill-house and the race sit on the lower side. The culvert is under the square. Do not draw Brenthael. Do not narrate a curse. Label only the Tree, the mill-race, and the culvert.
- [x] Read [[Ornsael]]. One town sheet, `Ornsael-Atlas.png`, labeled with `label_ornsael.py`. A well-town in the dry country east of the Rain-Wall. No walls. The Tree stands beside the well. The west-road is the main street and leaves toward the pass. This is not Saelthael's capital and not Larbril. Label only the Tree, the well, and the west-road.
- [x] Read [[Nelath]]. One town sheet, `Nelath-Atlas.png`, labeled with `label_nelath.py`. A smaller square than the Mill-hold. No walls. A sound Hand. The spur comes in and becomes the square. Beyond the boughs the road is a scar: ditch, thorns, and no cart-track. The stone is in the square. The cistern is the drink, and it is not the stone. Do not draw the Third Hearth, the Mill-hold, or the First Seat. Label only the Tree, the stone, and the scar.
- [x] Read [[Ndenjoo]]. One village sheet, `Ndenjoo-Atlas.png`, labeled with `label_ndenjoo.py`. One hill and a hall under the turf. A few dozen hearths, not a town grid. Pasture and a standing-stone on the turf. A path down to the sand. No quay. No Tree, no dead trunk standing in for one, no graft. The storm-wall stays weather. Label only the hall. Do not label Njunda.
- [x] These are new paintings, not crops of the regional masters, the continent masters, the city plates, the heart sheet, the drop sheet, the pier sheet, or the Grove Bank sheet. Masters are 1152×864. West is left. Match the dark weather of the city plates. Fill the frame at the size the note already claims. A town fills the frame as a town. If it reads as a city, or as a region with a village in it, replace it. Do not ask the image model to write. Pillow labels in the same hand as `label_orentel_drop.py`: Liberation Serif, a pale halo, a leader only when the name would sit on the roofs. No capital star. A civic Hand is a broad dark hardwood filling its square, not the First Hand and not a glow. Thaeloren remains the only exceptional canopy, and it is not on these sheets. Do not redraw or relabel any sheet already in the atlas. Unlabeled Prototype 3 sheets stay the regional handouts.
- [x] Record the six sheets on [[The Atlas Sheets]]. Add the six scripts beside the M.1 scripts in [[Map Generation Tooling]]. Do not update the world book. Do not open M.3 or M.4. Do not add a sixteenth power. Do not put a graft on Kumbaan. Do not capture the First Seat, date the Tree, or name the cutter. Do not add a person. Do not add a habit. Do not explain a habit that is already written.

> **M.2 recorded decisions (2026-10-03).** Six new paintings, not crops of the regional masters, the continent masters, the city plates, the heart sheet, the drop sheet, the pier sheet, or the Grove Bank sheet. The image model was not asked to write. Pillow on those masters. Masters are 1152×864. West is left. No capital star. A civic Hand is a broad dark hardwood filling its square. Thaeloren is not on these sheets. Unlabeled Prototype 3 sheets stay the regional handouts. World book untouched. M.3 and M.4 were not opened.
>
> **Rothallo.** Read with [[The Walled Book]]. Rothallo is Orenbren's walled capital, one day from the wood. People still say the Inner Close. It is the same place, not a second town. No sheet in M.2. The plate stays for M.3.
>
> **Eolvaeth.** `Eolvaeth-Atlas.png`, `label_eolvaeth.py`. The frame is the fold. Labels: the Tree, the spring, the gift-hall. Vaethod is not labeled. The wet leaf was not explained.
>
> **Harrow's Green.** `Harrows-Green-Atlas.png`, `label_harrows_green.py`. Labels: the Tree, the stone. Brenod, Vaelun, and Ornath are not on the sheet. The square was not relabeled into Nelath. The cistern-dipper was not explained.
>
> **The Mill-hold.** `Mill-hold-Atlas.png`, `label_mill_hold.py`. The canopy is visibly wrong and still a hardwood. Labels: the Tree, the mill-race, the culvert. Brenthael is not drawn.
>
> **Ornsael.** `Ornsael-Atlas.png`, `label_ornsael.py`. Labels: the Tree, the well, the west-road. Not Saelthael's capital. Not Larbril.
>
> **Nelath.** `Nelath-Atlas.png`, `label_nelath.py`. Labels: the Tree, the stone, the scar. The cistern is the drink and is not labeled. The Third Hearth, the Mill-hold, and the First Seat are not drawn.
>
> **Ndenjoo.** `Ndenjoo-Atlas.png`, `label_ndenjoo.py`. A close piece of the slope, at village scale. The hill continues off the frame. Label: the hall. Njunda is not labeled. No Tree, no dead trunk, no graft. The storm-wall stays weather. Harrow's Green and Nelath names sit on the features they name.

### Story M.3 — Sheets for whatever S seats ✅ **DONE (2026-10-03)**
After S.1–S.3. A city gets a city plate. If that plate cannot hold the tension the note already names, one closer sheet of the same place. A town gets a town sheet. A refusal gets nothing. [[Vaelhesk]] gets no sheet and no dot. The six charter-towns were not named. They are not painted. A league does not get a capital plate in place of a town S never named. These plates do not replace the pointers on the maps that already exist.

- [x] Read the S.1–S.3 seat notes. Paint only [[Seinbrun]], [[Rothallo]], [[Larbril]], [[Votaer]], [[Raitin]], [[Naenor]], [[Lunbra]], [[Braetu]], [[Tasain]], [[Sanbreo]], and [[Natai]]. Vaelhesk gets nothing. Do not invent a charter-town. Do not paint one.
- [x] **Seinbrun.** One city plate, `Seinbrun-Atlas.png`, labeled with `label_seinbrun.py`. A large city off the water, in the warm core. The furnished hall, the green beside it, and a Hand beside the hall. No city wall. The wood is not inside the city. The First Seat is not marked. Do not draw Thaeloren. Label the hall, the green, and the Tree. Do not label a person. Do not explain a habit. One plate holds the hall and the green. Do not add a closer sheet to be thorough.
- [x] **Rothallo.** One city plate, `Rothallo-Atlas.png`, labeled with `label_rothallo.py`. This is the plate M.2 left. Orenbren's walled capital, one day from the wood. People still say the Inner Close. It is the same place. The gate is the argument: the beds outside the wall, the Book of Tithes inside. A Hand inside the walls. The city does not Speak it. The First Seat stays in the wood, unnamed: no college, no throne, no canopy-ring, no mark. Do not draw Thaeloren. Label the gate, the beds, the Book, and the Tree. Do not label a person. Do not explain a habit. Add one closer sheet of the gate only if this plate cannot hold the beds outside and the Book inside.
- [x] **Larbril.** One city plate, `Larbril-Atlas.png`, labeled with `label_larbril.py`. A medium city. No wall. The west road meets the Well-wash, short of the pass. The wash in this frame is a silt-line, because the water is not a certainty. A Hand at the meeting. Not [[Ornsael]]. Not the Dry Stair. Label the meeting, the west road, the Well-wash, and the Tree. Do not label a person. Do not explain a habit.
- [x] **Votaer.** One city plate, `Votaer-Atlas.png`, labeled with `label_votaer.py`. One of the largest cities. The sea is west, on the left. The classification quay is the working waterfront. A Hand stands back from that quay. It faces [[Orentel]] and is not a second Orentel. No White Note. No Chart-run. Label the classification quay and the Tree. The blessing and the docket are the same quay. Do not add a closer sheet unless that quay cannot be read.
- [x] **Raitin.** One city plate, `Raitin-Atlas.png`, labeled with `label_raitin.py`. A river-city, one of the largest. The council hall stands at the head of the river stair. A Hand beside the hall. This river is not the Chart-run, and it is not named. The six charter-towns stay off the sheet. Label the hall, the river stair, and the Tree. Do not label a person. Do not explain a habit. Do not give the league a second capital.
- [x] **Naenor.** One city plate, `Naenor-Atlas.png`, labeled with `label_naenor.py`. A large port on its own coast, slightly smaller than Orentel. The signing-watch is the book-table in the square. A Hand stands off that square. Working berths. Not the Chart-run. Not the West Water. It does not face the Hinge Shore. Label the signing-watch and the Tree. The lost berth is not in this city. Do not label a person. Do not explain a habit.
- [x] **Lunbra.** One city plate, `Lunbra-Atlas.png`, labeled with `label_lunbra.py`. A large wealthy city on the Chart-run, inland of the salt. The river runs east, toward the right. The roll-room stands on the square where the money is shown. A Hand in the square. Label the roll-room, the square, the Tree, and the Chart-run. Do not name the governing throat. Do not label a person. Do not explain a habit. Do not add a closer sheet unless the square and the roll-room cannot both be read.
- [x] **Braetu.** One city plate, `Braetu-Atlas.png`, labeled with `label_braetu.py`. A harbour city, smaller than Orentel, on the West Water. The sea is west, on the left. The quote-desk is on the quay. One berth stays unlit, with no house on it. A Hand stands back from the working water. Label the quote-desk, the unlit berth, the Tree, and the West Water. Do not move the White Note here. Do not label a person. Do not explain a habit. Add one closer sheet of the harbour only if the plate cannot hold the desk and the dark berth together.
- [x] **Tasain.** One town sheet, `Tasain-Atlas.png`, labeled with `label_tasain.py`. A walled town in the valley, where the levy is taken. Not a city. Not the whole shelf. The town gate is in the frame. The Shelf-gate stays off the sheet. A Hand in the valley. Label the town gate and the Tree. Do not label Narol. Do not explain the bowl of snow.
- [x] **Sanbreo.** One town sheet, `Sanbreo-Atlas.png`, labeled with `label_sanbreo.py`. Still a town, on the brink of a small city. The shore gate, the slate on the wall inside it, and the beach. The sea is east, on the right. Not a harbour city. The note does not seat a civic Hand here. Do not paint one as the subject. Label the shore gate and the slate. Do not write the line on the slate. Do not explain the coin.
- [x] **Natai.** One town sheet, `Natai-Atlas.png`, labeled with `label_natai.py`. A march-town. The town gate is on the road between grafts. A young Hand, not the luck at [[Harrow's Green]]. Do not draw Harrow's, the ford, or the three hamlets. Label the town gate and the Tree. Do not label Dumu. Do not explain the latch.
- [x] These are new paintings, not crops of the regional masters, the continent masters, the city plates, the heart sheet, the drop sheet, the pier sheet, the Grove Bank sheet, or the M.2 town sheets. Masters are 1152×864. West is left. Match the dark weather of the city plates. A city fills the frame as a city. If it reads as a village, replace it. A town fills the frame as a town. If it reads as a city, or as a region with a settlement in it, or as a whole hill or island, replace it. The ground continues off the edges. Do not ask the image model to write. Pillow labels in the same hand as `label_orentel_drop.py`: Liberation Serif, a pale halo, a leader only when the name would sit on the roofs. The name sits on the feature it names. No capital star. A civic Hand is a broad dark hardwood filling its square, not the First Hand and not a glow. Thaeloren remains the only exceptional canopy, and it is not on these sheets. Do not redraw or relabel any sheet already in the atlas. Unlabeled Prototype 3 sheets stay the regional handouts.
- [x] Record the sheets on [[The Atlas Sheets]]. Add the scripts beside the M.2 scripts in [[Map Generation Tooling]]. Do not update the world book. Do not open M.4. Do not add a sixteenth power. Do not put a graft on Kumbaan. Do not capture the First Seat, date the Tree, or name the cutter. Do not add a person. Do not add a habit. Do not explain a habit that is already written.

> **M.3 recorded decisions (2026-10-03).** Thirteen new paintings, not crops of the regional masters, the continent masters, the city plates, the heart sheet, the drop sheet, the pier sheet, the Grove Bank sheet, or the M.2 town sheets. The image model was not asked to write. Pillow on those masters. Masters are 1152×864. West is left. No capital star. A civic Hand is a broad dark hardwood filling its square. Thaeloren is not on these sheets. Vaelhesk has no sheet and no dot. The six charter-towns were not painted. Unlabeled Prototype 3 sheets stay the regional handouts. World book untouched. M.4 was not opened.

> **Follow-up the same day.** The Rothallo gate sheet was redrawn so the gatehouse is the square gate on the city plate. The beds stay outside. The Book stays inside. Larbril's Well-wash is the thin silt-line. It is not a road. The west road is the only street. Overhead plans were added for the cities and towns already seated: Seinbrun, Rothallo, Larbril, Votaer, Raitin, Naenor, Lunbra, Braetu, Maiethlir, Orentel, Tasain, Sanbreo, Natai, Eolvaeth, Harrow's Green, the Mill-hold, Ornsael, Nelath. Script: `label_seat_plans.py`. Vaelhesk has no plan. Ndenjoo has no plan. The oblique plates stay. M.4 was not opened. World book untouched.

> **Seinbrun.** `Seinbrun-Atlas.png`, `label_seinbrun.py`. A large city off the water. No wall. Labels: the hall, the green, the Tree. One plate holds the hall and the green. No closer sheet.

> **Rothallo.** `Rothallo-Atlas.png`, `label_rothallo.py`. Orenbren's walled capital, one day from the wood. People still say the Inner Close. It is the same place. Labels: the gate, the beds, the Tree. The Book is on the gate sheet. The First Seat stays in the wood, unnamed.

> **Rothallo gate.** `Rothallo-Gate-Atlas.png`, `label_rothallo_gate.py`. The city plate could not hold the beds outside and the Book inside. Labels: the gate, the beds, the Book.

> **Larbril.** `Larbril-Atlas.png`, `label_larbril.py`. No wall. The west road meets the Well-wash. The wash in this frame is a silt-line. Labels: the meeting, the west road, the Well-wash, the Tree. Not Ornsael. Not the Dry Stair.

> **Votaer.** `Votaer-Atlas.png`, `label_votaer.py`. The sea is west. Labels: the classification quay, the Tree. The blessing and the docket are the same quay. No White Note. No Chart-run. No closer sheet.

> **Raitin.** `Raitin-Atlas.png`, `label_raitin.py`. Labels: the hall, the river stair, the Tree. The river is not named. The six charter-towns stay off the sheet.

> **Naenor.** `Naenor-Atlas.png`, `label_naenor.py`. Labels: the signing-watch, the Tree. The signing-watch is the book-table in the square. Not the Chart-run. Not the West Water. The lost berth is not in this city.

> **Lunbra.** `Lunbra-Atlas.png`, `label_lunbra.py`. The Chart-run runs east, toward the right. Labels: the roll-room, the square, the Tree, the Chart-run. The square and the roll-room are both on this plate. No closer sheet. The governing throat is not named.

> **Braetu.** `Braetu-Atlas.png`, `label_braetu.py`. The sea is west. Labels: the Tree, the West Water. The quote-desk and the unlit berth are on the quay sheet.

> **Braetu quay.** `Braetu-Quay-Atlas.png`, `label_braetu_quay.py`. The city plate could not hold the quote-desk and the unlit berth together. Labels: the quote-desk, the unlit berth, the West Water. No house on the unlit berth. The White Note is not here.

> **Tasain.** `Tasain-Atlas.png`, `label_tasain.py`. A walled town. Labels: the town gate, the Tree. The Shelf-gate stays off the sheet. Narol is not labeled.

> **Sanbreo.** `Sanbreo-Atlas.png`, `label_sanbreo.py`. A town. The sea is east. Labels: the shore gate, the slate. The line is not written on the slate. No civic Hand is the subject.

> **Natai.** `Natai-Atlas.png`, `label_natai.py`. A march-town. A young Hand. Labels: the town gate, the Tree. Harrow's, the ford, and the three hamlets are not drawn. Dumu is not labeled.

### Story M.4 — Pointers on the maps that already exist ✅ **DONE (2026-10-05)**
Capitals, large cities, and important towns. A plain pointer and a label, so a reader can find them. [[The Known Map]] schematic, the world overlay, and the continent and region overlays whose ground the note already names. Pillow on the existing master. The image model does not write. No new survey. No capital star. Unlabeled Prototype 3 sheets stay the handouts. M.4 can be drawn before the close-up plates.

- [x] Capitals and large cities: [[Maiethlir]] and [[Orentel]] already marked. Add [[Seinbrun]], [[Rothallo]], [[Raitin]], [[Votaer]], [[Naenor]], [[Lunbra]], [[Braetu]]. [[Rothallo]] is the name. Inner Close stays an alias on the same mark.
- [x] [[Larbril]] is the only city of [[Saelthael]]. It gets a pointer where the west road meets the Well-wash, short of the pass.
- [x] Important towns: [[Tasain]] below the Shelf-gate. [[Sanbreo]] on the slate-shore. [[Eolvaeth]] and [[Harrow's Green]] stay the marks they already are, and Harrow's is not a capital. [[Natai]] only where the notes already put the march, and not on Harrow's square and not on the ford. If a note does not place a town on that painting, do not borrow a roof cluster for it.
- [x] [[Naenor]] is its own coast. Not the Chart-run sheet. Not the West Water sheet. [[Lunbra]] is the Chart-run, four to eight days upriver of Orentel. [[Braetu]] is the West Water. [[Raitin]] is the river behind the premier coast, and that river is not the Chart-run.
- [x] No dot for [[Vaelhesk]]. No names for the six charter-towns, the pockets, the shelves, or the villages between grafts.

> **M.4 done (2026-10-05).** Pointers on the maps that already existed. No new painting. Pillow, Liberation Serif, cream type with a dark stroke, a leader when the name would sit on the feature. West is left. No capital star. The note won where a painting disagreed. [[The Known Map]] schematic, the world overlay, Maiethorn, Sacred Core, Strandoren, Heskoren, the Old Crossing, the Chart-run, the West Water, the Rain-Wall, and the Rain-Shadow. The Inner Close square on Maiethorn and on Sacred Core is labeled Rothallo. Maiethlir and Orentel were left where a sheet already had them, and marked once on the world overlay, which had not. Seinbrun is off the Core-thaw. Votaer is the Hinge Shore port. Tasain is in the valley below the Shelf-gate. Larbril is where the west road meets the Well-wash, short of the pass, west of Ornsael's well. Lunbra is upriver on the Chart-run. Raitin is the river behind the premier coast. Naenor is the south coast of Strandoren. Braetu is the Night Shore. Sanbreo is the slate-shore mark that had said Ornled. Natai is the march, not Harrow's square and not the ford. Eolvaeth and Harrow's stay. Vaelhesk has no dot. The six charter-towns, the pockets, the shelves, and the villages between grafts stay unnamed. Live Front, Waiting Vale, Kumbaan, the close plates, and the plans were not redrawn. Unlabeled Prototype 3 sheets stay the handouts. The world book was not rebuilt. M.5 stays checked.

### Story M.5 — The ordinary house ✅ **DONE (2026-10-04)**
Close plates and overhead plans use the house of their band. The cards are in [[Map Generation Tooling#The ordinary house]] and on [[The Atlas Sheets]]. The ink stays one atlas. The ordinary house is distinct from band to band. Towns inside a band vary by the landmark the note already names. `Orentel-City-Atlas.png` is the shore-lands house, and the reference for that band. Regional masters stay. Epic A stays closed. M.4 does not redraw a painting. This story does not open a new epic. The world book stays untouched.

- [x] Write the six mainland cards, and the Kumbaan card, into [[Map Generation Tooling]] and [[The Atlas Sheets]]. A later close painting pastes Close-plate hand and one band. The image model does not write.
- [x] Redraw the mother-core close plates and plans: Seinbrun, Rothallo, the Rothallo gate, Maiethlir (city, heart, Grove Bank), the Mill-hold, Nelath. Same landmarks. The mother-core house.
- [x] Redraw Tasain, plate and plan, as the Thaw-Wall house.
- [x] Redraw Larbril and Ornsael, plates and plans, as the Rain-Shadow house. Larbril's wash stays the water. The west road stays the street.
- [x] Keep Orentel as the shore-lands model. Redraw Raitin, Naenor, Lunbra, Braetu, and the Braetu quay, plates and plans, where they still wear another band's house.
- [x] Redraw Votaer, plate and plan, as the Old Crossing house.
- [x] Redraw Eolvaeth, Harrow's Green, and Natai, plates and plans, as the Sundered Reach house. Sanbreo is the slate-shore version of that house.
- [x] Read Ndenjoo again. If the village wears a mainland house, replace it with the Kumbaan card. No Tree.
- [x] Cover the labels on one plate from mother-core, rain-shadow, shore-lands, and the reach. If they do not sort, replace the plate before the rest of that band. Do not update the world book. Do not reopen A.1–A.14. Do not redraw a regional master. Do not open a new epic.

> **M.5 done (2026-10-04).** Close plates and overhead plans wear the house of their band. Maiethlir, Larbril, Braetu, and Harrow's Green sort with the labels covered. Orentel stays the shore-lands model. The Rothallo gate keeps the beds outside the wall and the Book inside it. Ndenjoo already wore turf and stone, a hall under the hill, and no Tree, so that sheet was left. Pillow labels, Liberation Serif, cream halo, a leader when the name would sit on the feature. Masters stay 1152×864. West is left. Regional masters stay. The world book was not rebuilt. M.4 was not opened. A.1–A.14 stay closed.

> **L.4 done (2026-10-01).** The room can say a second name. Next session may open L.5. This pass did not. L.5–L.9 stay coarse.

> **L.3 done (2026-10-01).** The year has a street. Next session may open L.4. This pass did not. L.4–L.9 stay coarse.

> **L.2 done (2026-09-29).** Faces are in. L.3 opened the following session.

> **Shelf and storm (2026-10-01).** Dated years are since the First Cut, a graft. Conditions, the Giving, and the doors are older and undated. Kumbaan's storm-wall stays weather, current, and reef. No blocker in the water. Her limit's nature stays open. Recorded on [[Before the Walk]], [[The Ages of the Turning]], [[The Other Hands]], [[The Sundering Isle]]. World book untouched.

---

## Progress

> Manual tally — update when checking boxes. (Story/Task counts, not epics.)

- **Epic L — The lived world:** 34 / 34 tasks of L.1–L.6 (100%). 5 / 5 tasks of L.7 (100%). 6 / 6 tasks of L.8 (100%). 5 / 5 tasks of L.9 (100%) ✅ **L.9 done 2026-10-03. Epic L complete.** Diagnosis: voices, then faces, then customs, then the names in the room, then a street, then the other hearths, then fellowships and the watch, then the weird, the made, and the found, then sidebar honesty. Empty folders are not a fill-list. World book untouched. Epic S and Epic M were not opened.
- **Epic S — The other seats:** 3 / 3 tasks of S.0 ✅ **(2026-10-03).** 7 / 7 tasks of S.1 ✅ **(2026-10-03).** 6 / 6 tasks of S.2 ✅ **(2026-10-03).** 5 / 5 tasks of S.3 ✅ **(2026-10-03). Epic S complete.** Maiethorn's five seats, Strandoren's four seats, and Heskoren's three seats are written or refused. [[Orentel]] has nine habits. [[Sanbreo]], [[Natai]], [[Harrow's Green]], and [[The First Bowl]] have one. [[Eolvaeth]] and the three hamlets already had one. [[Vaelhesk]] has no new place. World book untouched. Epic M not opened.
- **Epic M — Town sheets and the new seats:** 5 / 5 tasks of M.1 ✅ **(2026-10-03).** 9 / 9 tasks of M.2 ✅ **(2026-10-03).** 14 / 14 tasks of M.3 ✅ **(2026-10-03).** 5 / 5 tasks of M.4 ✅ **(2026-10-05).** 9 / 9 tasks of M.5 ✅ **(2026-10-04).** Epic M complete. Rothallo is the Inner Close, and the plate is in. Vaelhesk has no sheet and no dot. Does not reopen A.1–A.14. World book untouched.
- **Epic A — Atlas labels:** 5 / 5 of A.1 (100%) ✅ **2026-09-01.** 4 / 4 of A.2 (100%) ✅ **2026-09-03.** 4 / 4 of A.3 (100%) ✅ **2026-09-16.** 4 / 4 of A.4 (100%) ✅ **2026-09-16.** 4 / 4 of A.5 (100%) ✅ **2026-09-16.** 5 / 5 of A.6 (100%) ✅ **2026-09-16.** 4 / 4 of A.7 (100%) ✅ **2026-09-16.** 5 / 5 of A.8 (100%) ✅ **2026-09-16.** 5 / 5 of A.9 (100%) ✅ **2026-09-17.** 5 / 5 of A.10 (100%) ✅ **2026-09-17.** 5 / 5 of A.11 (100%) ✅ **2026-09-17.** 5 / 5 of A.12 (100%) ✅ **2026-09-19.** 5 / 5 of A.13 (100%) ✅ **2026-09-19.** 5 / 5 of A.14 (100%) ✅ **2026-10-02.** Overlay queue closed. City sheets for [[Maiethlir]] and [[Orentel]] are in. Does not reopen A.1–A.13. [[Eolvaeth]] has no city sheet. L.6 was not opened. World book untouched.
- **Heskoren label trial:** folded into [[#Epic A — Atlas labels|Story A.1]]. Image-model labels redrew C3. Overlay `Heskoren-Atlas-Labeled.png` keeps the Prototype 3 master; names from [[Named Ground]] only. Unlabeled sheets stay the selected handouts.
- **Atlas follow-up:** 8 / 8 regional sheets rebuilt and visually reviewed ✅ **2026-09-01.** Sibling region sheets are distinct generated paintings, not parent crops: Sacred Core versus Rain-Wall; Chart-run versus West Water. Crop builder retired. Non-canon interpolation boundary recorded on [[The Atlas Sheets]] and [[Map Generation Tooling]]. Thaeloren remains the only exceptional Tree. World book untouched.
- **Epic 7 leftover — sick-Tree / guest-grove:** 4 / 4 tasks (100%) ✅ **2026-08-31.** [[The Mill-hold]] (Hands un-Hands; mill-race vs roots) · [[The First Bowl]] (guest-grove; two settings of one bowl). Lead road-end seated at [[Nelath]] in Story L.5 (2026-10-02). World book untouched.
- **Pass two — verification:** 3 / 3 tasks of P2.1 (100%) ✅ **Story P2.1 complete 2026-08-31.** 4 / 4 tasks of P2.2 (100%) ✅ **Story P2.2 complete 2026-10-02** — plain prose. 5 / 5 tasks of P2.3 (100%) ✅ **Story P2.3 complete 2026-10-05** — contradiction sweep after L, S, and M. C-07, C-08, C-09 on [[Contradictions]]. No map redrawn. 3 / 3 tasks of P2.4 (100%) ✅ **Story P2.4 complete 2026-10-05** — nothing the sweep touched was thin. C-01 through C-06 and R-01 through R-04 stay resolved. **C-02** stays the 2026-08-31 rebuild. World book not rebuilt. Endings stay undecomposed.
- **Epic 9 — Secrets & Canon:** 4 / 4 tasks of Story 9.1 (100%) ✅ **architecture done 2026-08-31.** Hub [[Revelation Architecture]] · [[Reveal Index]]. Clues [[The Uncoloured Intake]] · [[The Closed Lamp]]. Still alongside for new `reveals:`.
- **Epic 10 — Campaign:** 4 / 4 tasks of Story 10.1 (100%) ✅ **opening done 2026-08-31.** 5 / 5 tasks of Story 10.2 (100%) ✅ **next sessions done 2026-10-05.** Hub [[The Isolated Fall]] · kits [[The Opening]] · [[The Walk Home]] · [[The Offered Fragment]] · [[The Week Still Open]]. Endings stay undecomposed. Do not resume the old Epic 8 roster.
- **Epic R: Editorial repair and table readiness:** 97 / 97 tasks (100%) ✅ **closed 2026-08-31.** Gate: [[Epic R Completion Gate 2026-08-31]]. Stories **R.1–R.13** ✅. Residual export polish is **P2.1**, not a reopened R.13. Source: [[Editorial Audit 2026-08-29]]. **Story R.1 ✅** (population arithmetic; Unbound inside Bound; Premise is the sole census). **Story R.2 ✅** (Condition mechanics; one-Gift rule in [[When the Fire Is Caught]]; no level scaling). **Story R.3 ✅** (Hearth-Mark, not a trim; Mixed Ancestry as SRD; Yumboe GM-leave and full Kind; one surprise keyword; other kitchen). **Story R.4 ✅** — warden questions and Leaf-Fall failure on [[Turning Tree]]; dread → [[The Wrong Green]]; Other Hands wants / Orledd receive / allowance strain → [[The Other Hands]]; Open Table lintel → [[The Open Table]]. **Story R.5 ✅** — leaks walled; tag split (`keystone-adjacent` / `the-other-hands`); firing pin [[The Spent Leaf]] + [[The Remainder]]; rungs 1–5 deniable, rung 6 can fire; [[The Unspent]] outside the Five Hands. **Story R.6 ✅** — licence pool ≠ census; Tithe-provision as wells not grain; hearth-stand; road-word; crime ladder; urban Taken-In; prestige-walk chained (Netstrand berths → White Note terms → Orentel holds). **Story R.7 ✅** — lived faces [[The Holding Desk]] · [[The Standing Trade]]; Threnmaieth instruments [[The Reckoned Offices]]; three unlocked fights; header blocks; voice break; greens/halls folded; opposition can act; three engines [[The Pourers]] · [[The Walled Book]] · [[The Protectors]], kept distinct. **Story R.8 ✅** — six pivots + named wants in the three seats + four campaign seeds; hub [[People of the Turning]]. **Story R.9 ✅** — [[The Other Count]]; Closed Seat / [[The Closing]]; five dated years; three leftovers; Ledan query C.Y. 280; fifteen inherited claims. **Story R.10 ✅** — [[Named Ground]] (Old Crossing · Rain-Wall · four rivers · travel table) · [[The Known Map]] · tooling extracted to `14 - Assets/Maps/` · Kumbaan never aligned · Inner Close 🔒 in [[Orenbren]] · the Hinge Shore / Lirorn / Netstrand sharpened. **Story R.11 ✅** — Ornsael de-cloned (well-share); formula varied across seven; White Note walkable; Kumbaan committed ([[Ndenjoo]] · [[Njunda]] · crossing); leftovers given entrances/pressures; retrieval headers; scene-entering dangers. **Story R.12 ✅** — phonology and drift repaired; common handles promoted; *Aeloren* / *Eolstrand* retired; root families closed; fables and note voices differentiated; editorial mantras capped; deterministic naming tool stored. **Story R.13 ✅** — [[Build Plan]] rewritten; `locked` → `canon`; Conditions `player`; [[09 - Creatures]] filled; [[Rogue House Options]] archived; strip rule on [[Conventions]]; scaffolding moved; [[At the Table]] · [[Dangers of the Turning]] · [[A Hidden Phoenix]]. Engine untouched. World book rebuilt 2026-08-31 on explicit request (C-02).
- **Epic 0 — Foundations:** 7 / 7 tasks (100%) ✅ — setting named *The Turning* (2026-08-20); household elaboration 2026-08-23 → [[The Other Hands]]
- **Epic 1 — Anchor:** 16 / 16 tasks checked (100% of listed) — clergy orders → [[The Tree-Wardens]] (Story 5.1, names 🟡). **Conditions cross-link leftover ✅ 2026-08-31** → [[Conditions]] derived palette; At the Tree / Away from the Tree on all ten cards.
- **Epic 3 — The World Frame:** 🟢 **core done (2026-08-22); climate/ecology leftover ✅ 2026-08-31** — 5/5 marked: [[The World Frame]] + four continents; calendar locked ([[The Reckoning of the Year]]); 4th ancestry ([[Yumboe]]) pulled forward; **climate/ecology** → [[Climate of the Turning]] · [[Ecology of the Turning]] · [[Climate of Maiethorn]] · [[Climate of Strandoren]] · [[Climate of Heskoren]] · [[Climate of Kumbaan]]. **Story R.10 ✅** named the waters and the range → [[Named Ground]] · [[The Known Map]]; tooling extracted to `14 - Assets/Maps/Map Generation Tooling.md`. ~12 named-stub powers ✅ Story 7.1. Rival faiths ✅ Story 1.4.
- **Epic 4 — Cultures & Kinds:** custom ancestries **4/4 ✅**. **Story 4.2 ✅ and 🔒 (2026-08-23, user-approved)** → [[Kinds of the Turning]] · [[Naming People in the Turning]] · months · Kumbaan name base · leaf-colours. **Story R.3 ✅ (2026-08-30)** → [[Kind Heritage]] (Hearth-Mark, not a trim; Mixed Ancestry as SRD; Yumboe GM-leave and full Kind; one surprise keyword) · other kitchen. Revisit flag closed. Deep grammar still deferred. ~12 powers' stance-drifts ✅ Story 7.1 (no new grammars).
- **Epic 5 — Factions:** ✅ **COMPLETE (2026-08-23).** Stories 5.1–5.3 done → [[The Tree-Wardens]] · [[The Watchers]] · [[The Book-Hands]] · [[The Door-Keepers]] · [[The Table-Keepers]] · [[The Shore-Sitters]] · [[The Slide]] · [[Tithe-Infrastructure]] · [[The Greens-Keepers]] · [[The Hall-Keepers]] · [[The Stillers]] · [[The Element-Guilds]] · [[The Intake]] (names 🟡, do not rebuild). **Story R.7 ✅ (2026-08-30)** added lived faces and engines → [[The Holding Desk]] · [[The Standing Trade]] · [[The Pourers]] · [[The Walled Book]] · [[The Protectors]] · [[The Reckoned Offices]]; greens/halls folded as jurisdictions.
- **Epic 6 — History:** ✅ **COMPLETE (2026-08-24).** 8 / 8 of 6.1 🔒; 7 / 7 of 6.2; 6 / 6 of 6.3; 6 / 6 of 6.4. **Story R.9 ✅ (2026-08-30)** added the Other Count beside the clocks. Hub [[The Ages of the Turning]] · lived road [[The Walking Years]] · hinge [[The First Cut]] · war [[The Closing]] · residues [[The Years of Hands]] · chronicle [[The Other Count]] · leftovers [[The Low Wall]] · [[The Seeing-Ring]] · [[The Dry Stair]]. Names *Brenvaeth / Eoloren / Ornthael* 🔒. Present C.Y. 387 🔒. **Cutter still unpicked.** Nature of her limit still open. Closed Seat / crown-count / Hush-rate 🟡.
- **Epic 7 — Settlements:** ✅ **COMPLETE (2026-08-24); leftover squares ✅ 2026-08-31.** 6 / 6 of 7.1 🔒. 5 / 5 of 7.2. 5 / 5 of 7.3. **4 / 4 of sick-Tree / guest-grove leftover.** Hub [[Powers of the Turning]] · twelve stubs · playable squares ([[Harrow's Green]] · [[The Three Hamlets Past the Ford]] · [[The Third Hearth]] · [[Ornsael]] · [[The Mill-hold]] · [[The First Bowl]]) · three archetype seats ([[Eolvaeth]] · [[Orentel]] · [[Maiethlir]]). Names *Eolvaeth / Orentel / Maiethlir* 🟡. White Note placed on Orentel, not crowned. Cast on the seats → Story R.8 / [[People of the Turning]]. **Story R.11 ✅** — retrieval, de-clone, Kumbaan hall, leftover depth. The lead road-end was seated later, at [[Nelath]] (Story L.5, 2026-10-02).
- **Epic 8 — People:** 🟢 **8.1 landed in Story R.8 (2026-08-30).** 5 / 5 of 8.1. Hub [[People of the Turning]] · six pivots · seat wants · four seeds. Do not rebuild. R.11 added [[Njunda]] and [[Ledan]] as mouths, not pivots. Hidden-Phoenix agency ✅ [[A Hidden Phoenix]]. Stories R.12–R.13 ✅. Epic R closed. Next: Pass two · P2.1.
- **Epic 2 — Society:** ✅ **COMPLETE (2026-08-21).** Frame locked (world scale + register + social guard); **all four stories + the naming pass done, core audited.** **2.1 (Law & Citizenship) ✅** → [[Law and Citizenship]]; **2.2 (Economy & the Tithe) ✅** → [[Economy and the Tithe]]; **2.3 (Daily Life) ✅** → [[Daily Life]]; **2.4 (Polity Archetypes) ✅** → [[Polity Archetypes]] (three corners, now named **Vaethorn / Lestrand / Threnmaieth**, seats **Eolvaeth / Orentel / Maiethlir**). **Naming pass ✅** → [[The Old Tongue]] + [[Naming in the Turning]]. Core audit complete → [[Epic 2 Audit Guide]]. **→ Story 4.2 done. Epic 5 complete (5.1–5.3). Epic 6 complete (6.1–6.4). Epic 7 complete (7.1–7.3). Story 8.1 landed in R.8. Stories R.9–R.13 ✅. Epic R closed. Next: Pass two · P2.1.**
- **Locked decisions:** **setting name (_The Turning_)**, two-layer model, engine, roster, all 10 Condition mechanics, **4 custom ancestries** (Kitsune · Selkie · Tengu · Yumboe), keystone secret (Leaf-Mother real+benevolent **but bounded & costly**), Tree topology (one Awakening Tree + living grafts), **world scale (~15 polities / 3+1 continents)**, **register (late-medieval + Condition-labor advances)**, **world frame (four continents on a reach-gradient: [[Maiethorn]] · [[Strandoren]] · [[Heskoren]] · [[The Sundering Isle]])**, **calendar (High-Solstice Turning-Week + twelve Maiethren months + three new-year's days)**, **five lived faiths** (Motherfaith + Watching / Fair Hand / Old Ways / Open Table — names 🔒), **household cosmology** (she Gives; Other Hands Strike — structure 🔒, Hand-names 🟡), **Kind-hearths not Kind-nations**, hearth-registers ***Kusawe / Sakoa / Gonan***, **Kind heritage (Hearth-Mark · Mixed Ancestry as SRD · Yumboe GM-leave and full Kind · surprise keyword once on Tengu)**, **leaf-colour table**, **era spine** (two clocks · Grafting as live wave · no universal year-zero · dating reveals stance · *Brenvaeth / Eoloren / Ornthael* 🔒 · C.Y. 387 🔒 · Tree undated · cutter unpicked · limit's nature still open), **First Cut lived** (five attributions uncollapsed · Cutting-leave as captured copy-right · spread inside locked bands · Kumbaan never), **residues lived** (walk's three jobs · Hands can un-Hands · road-past as credit · Heskoren live front · fate-pressure noted not rolled). Epic 5 complete (clergy/guild names 🟡). **~15 powers named and 🔒 (Story 7.1, user-approved 2026-08-24):** three corners + twelve stubs → [[Powers of the Turning]]; *Eolstrand* retired in R.12 and the slot remains [[The Hinge Shore]]. **Playable squares (Story 7.2, 2026-08-24):** [[Harrow's Green]] · [[The Three Hamlets Past the Ford]] · [[The Third Hearth]] · [[Ornsael]]. **Sick-Tree / guest-grove leftover (2026-08-31):** [[The Mill-hold]] · [[The First Bowl]]. **Archetype seats (Story 7.3, 2026-08-24):** [[Eolvaeth]] · [[Orentel]] · [[Maiethlir]]. **Cast (Story R.8 / 8.1, 2026-08-30):** [[People of the Turning]]. **Other Count (Story R.9, 2026-08-30):** [[The Other Count]] · Closed Seat / [[The Closing]] · cutter still unpicked. **Named ground (Story R.10, 2026-08-30):** [[Named Ground]] · [[The Known Map]] · Inner Close 🔒 in Orenbren · Kumbaan never. **Settlements / Kumbaan (Story R.11, 2026-08-31):** Ornsael de-cloned; White Note walkable; Kumbaan committed ([[Ndenjoo]]); leftovers runnable. **Language / naming / voice (Story R.12, 2026-08-31):** common handles promoted; *Aeloren* / *Eolstrand* retired; fables and note voices differentiated; naming tooling stored. **Table readiness (Story R.13, 2026-08-31):** [[At the Table]] · [[Dangers of the Turning]] · [[A Hidden Phoenix]] · export strip on [[Conventions]]. **Climate/ecology leftover (2026-08-31):** [[Climate of the Turning]] · [[Ecology of the Turning]]. **Revelation architecture (Story 9.1, 2026-08-31):** [[Revelation Architecture]] · [[Reveal Index]] · [[The Uncoloured Intake]] · [[The Closed Lamp]]. **Epic R closed. P2.1 done. Opening ✅ [[The Opening]]. Leftovers 1 / 3 / 7 / 9 done.**

## Links
- [[Build Plan]] — handoff brief (points here) · [[The Premise]] — design hub
- [[Epic R Completion Gate 2026-08-31]] — Epic R close · [[Contradictions]] — pass-two log
- [[Named Ground]] · [[The Known Map]] · [[Climate of the Turning]] · [[Ecology of the Turning]] — geography and living ground
- [[Powers of the Turning]] — Epic 7 Story 7.1 hub · [[Maiethvael]] · [[Orenbren]] · [[Saelthael]] · [[The Hinge Shore]] · [[Lirorn]] · [[Brenledd]] · [[Leddvael]] · [[Trenledd]] · [[Netstrand]] · [[Ornled]] · [[Vaelhesk]] · [[Saelvaeth]]
- [[Harrow's Green]] · [[The Three Hamlets Past the Ford]] · [[The Third Hearth]] · [[Ornsael]] — Story 7.2 squares · [[Settlement Seeds]]
- [[The Mill-hold]] · [[The First Bowl]] — sick-Tree / guest-grove leftover
- [[Eolvaeth]] · [[Orentel]] · [[Maiethlir]] — Story 7.3 seats · [[The White Note House]]
- [[Ndenjoo]] — R.11 Kumbaan hall · [[Njunda]] · [[Ledan]]
- [[The Ages of the Turning]] — Epic 6 hub · [[The Walking Years]] · [[The Child Who Counted Stones]] · [[The First Cut]] · [[The Branch That Came Away]] · [[The Years of Hands]] · [[The Child Who Climbed the Stone]] · [[Settlement Seeds]]
- [[The Wrong Green]] — Story R.4 cited mis-Speaking · [[Turning Tree]] · [[The Open Table]] · [[The Other Hands]]
- [[The Spent Leaf]] · [[The Remainder]] · [[The Unspent]] — Story R.5 firing pin and lesser presence
- [[Law and Citizenship]] · [[Economy and the Tithe]] — Story R.6 procedure (hearth-stand, road-word, watch, urban green)
- [[The Holding Desk]] · [[The Standing Trade]] · [[The Pourers]] · [[The Walled Book]] · [[The Protectors]] · [[The Reckoned Offices]] — Story R.7 houses
- [[People of the Turning]] — Story R.8 hub · [[Vaethod]] · [[Rithim]] · [[Mataero]] · [[Thilim]] · [[Laevila]] · [[Tesara]] · [[Reimaethe]] · [[Hithaen]] · [[Taeren]] · [[Rosire]]
- [[The Other Count]] — Story R.9 hub · [[The Closing]] · [[The Two Papers]] · [[The Grey Summer]] · [[The Thaw-Break]] · [[The Hinge Hush]] · [[The Low Wall]] · [[The Seeing-Ring]] · [[The Dry Stair]]
- [[Conditions]] · [[Kind Heritage]] · [[At the Table]] · [[Dangers of the Turning]] · [[A Hidden Phoenix]] · [[Kinds of the Turning]] · [[00 - Core]] · [[Conventions]] · [[99 - Archive]]
- [[The Isolated Fall]] · [[The Opening]] · [[The Walk Home]] · [[The Offered Fragment]] · [[The Week Still Open]] — Epic 10 Stories 10.1 and 10.2. Endings undecomposed.
- [[The Atlas Sheets]] · [[Map Generation Tooling]] · [[The Known Map]] — Epic A closed (A.1–A.14, 2026-10-02). City sheets: [[Maiethlir]] · [[Orentel]]. Story M.1 (2026-10-03): Orentel piers · Maiethlir Grove Bank. Unlabeled Prototype 3 sheets stay the regional handouts. L.6 was not opened with the sheets. Next lived-world story is L.7; it was not opened in the L.6 pass.
- Epic S — the other seats. S.0 done 2026-10-03. S.1 done 2026-10-03 → [[Seinbrun]] · [[Rothallo]] · [[Larbril]] · [[Votaer]] · [[Tasain]]. S.2 done 2026-10-03 → [[Raitin]] · [[Naenor]] · [[Lunbra]] · [[Braetu]]. S.3 done 2026-10-03 → [[Sanbreo]] · [[Vaelhesk]] (the land is the seat) · [[Natai]].
- Epic M — town sheets and the new seats. M.1 done 2026-10-03 → Orentel piers · Maiethlir Grove Bank. M.2 done 2026-10-03 → Eolvaeth · Harrow's Green · the Mill-hold · Ornsael · Nelath · Ndenjoo. M.3 done 2026-10-03 → Seinbrun · Rothallo (and the gate) · Larbril · Votaer · Raitin · Naenor · Lunbra · Braetu (and the quay) · Tasain · Sanbreo · Natai. Rothallo is the Inner Close. Vaelhesk has no sheet and no dot. M.4 done 2026-10-05 → pointers on [[The Known Map]] and the overlays that already show that ground. M.5 done 2026-10-04 → close plates and plans wear the ordinary house in [[Map Generation Tooling]]. Orentel stays the shore-lands model. Ndenjoo was already the Kumbaan house.
- Epic L — the lived world. **L.1 done 2026-09-29** → [[How a Place Speaks]]. **L.2 done 2026-09-29** → [[Hildal]] · [[Limrae]] · [[Dirrol]] · [[Narol of the Pass]] · [[Taerso]] · [[Monseoth]] · [[Rithnali]] · [[Sedrad]]. **L.3 done 2026-10-01** → [[What the Year Feels Like]] · [[How the Week Is Kept]] · [[When the Town Buries]] · [[The Guest-Meal]] · [[When Someone Is Struck]] · [[Maieth]] · [[The Houses and the Years]]. **L.4 done 2026-10-01** → second names on the NPC notes · [[Leaders]] · [[Heroes and Villains]]. **L.5 done 2026-10-02** → [[Nelath]] · [[Raillath]] · [[Denlad]] · [[Tunral]] · [[The Down-Bank]] · [[The Sky from the Ground]] · [[Planes]]. **L.6 done 2026-10-02** → stock hearth-glances on [[Kinds of the Turning]]. **L.7 done 2026-10-02** → [[The Slide]] · [[The Holding Desk]] · [[The Standing Trade]] under Criminal · [[Craft Fellowships]] · [[The Watch and the Cohort]] · [[Movements]]. **L.8 done 2026-10-02** → [[How the Work Is Done]] · [[A Made Thing]] · [[The Cart-Ox]] · [[The Terrace Goat]] · [[The Path Dog]] · [[Kin at the Door]] · [[What a Place Needed]] · [[The Other Chip]] · [[The Dry Slip]] · [[The Ribboned Knife]] · [[The Socket Ribbon]] · [[The One Knife]] · [[The Name-Stone Bed]] · [[A Buyer for the Knife]]. **L.9 done 2026-10-03** → decision folders point at the notes that already hold them. Prototype 1, Prototype 2, and the label-trial image are under `99 - Archive/Atlas/`. Epic S and Epic M were not opened.
- [[Revelation Architecture]] · [[Reveal Index]] · [[The Uncoloured Intake]] · [[The Closed Lamp]] — Story 9.1
