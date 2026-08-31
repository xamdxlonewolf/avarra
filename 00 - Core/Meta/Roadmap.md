---
title: Roadmap
type: moc
visibility: gm
note_status: draft
status: active
tags: [meta, roadmap, build-plan, tracker, moc]
aliases: [The Roadmap, Epics, Build Tracker]
created: 2026-08-17
updated: 2026-08-31
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
| **1** | [[#Epic 1 — The Engine's Anchor (Turning Tree & Leaf-Mother)]] | Religion, geography, settlements, law, the schism all point back here | **High** | 🟢 core + 1.4 done |
| **2** | [[#Epic 2 — Society & Institutions]] | Every settlement & faction inherits these rules | **High** | ✅ done |
| **3** | [[#Epic 3 — The World Frame]] | The physical stage settlements/cultures stand on | Med | 🟢 core done |
| **4** | [[#Epic 4 — Cultures & Kinds]] | Peoples & customs; **4** custom ancestries ✅ · Story 4.2 ✅ · R.3 glance ✅ | Low | 🟢 core done |
| **5** | [[#Epic 5 — Factions & Orders]] | The institutional actors (guilds, Tithe-infra orgs) | Med | ✅ done |
| **6** | [[#Epic 6 — History]] | When did the Trees appear? gives the world a past | Med | ✅ done |
| **7** | [[#Epic 7 — Settlements]] | Concrete stages for play | Med | ✅ done |
| **8** | [[#Epic 8 — People]] | The cast | Low | 🟢 8.1 landed in R.8 |
| **9** | [[#Epic 9 — Secrets & Canon]] | Revelation architecture — runs *alongside* from Epic 0 | — | 🟡 ongoing |
| **P2** | [[#Pass two — verification]] | Whole-world consistency, contradictions, gaps, quality — after pass one | **High** | P2.1 done; later undecomposed |
| **10** | [[#Epic 10 — Campaign]] | Actual play material; needs the world to exist first | — | 🟢 opening done |

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
**Skill:** `story-sense` (router) · `worldbuilding` · **Status:** **P2.1 complete 2026-08-31; later stories undecomposed** · **Blast radius:** High. Pass one is complete. Do not resume the old Epic 8 plan.

> A review sweep of the whole world for consistency, contradictions, gaps, and quality. Log and resolve under [[Contradictions]]. The bible stays this vault. Do not invent a parallel `world-bible/` tree. Do not update the world book unless asked. Hub collisions found while writing the opening are logged and fixed on that log (C-05).

> A review sweep of the whole world for consistency, contradictions, gaps, and quality. Log and resolve under [[Contradictions]]. The bible stays this vault. Do not invent a parallel `world-bible/` tree. Do not update the world book unless asked.

### Story P2.1: Residual export polish ✅ **DONE (2026-08-31)**
- [x] Move remaining Story numbers, "Canon status" blockquotes, and "Do not clone / Do not rebuild" out of player bodies of history, faction, settlement, and MOC notes (under `## GM Notes`)
- [x] Decide whether 🟡 on liturgical names stays in player text (taste-open) or moves with the rest — **option 2:** names stay visible; markers and taste-open status move under `## GM Notes`; no name locked or changed
- [x] Leave the compiled world book untouched unless the user asks for a rebuild

> **P2.1 recorded decisions.** C-01 is resolved. C-04 stays taste-open without player-facing status marks. C-03's skill links are plain code text; atlas embeds remain GM production aids because their PNG files are not tracked. C-02 was decided as no rebuild without an explicit request; **the user asked (2026-08-31)** and the compiled book was rebuilt. Stop here; later pass-two stories remain undecomposed.

### Later (do not decompose until asked)
- Contradiction sweep from the log (C-02 compile-stale resolved by the 2026-08-31 rebuild; C-05 resolved in passing with the opening)
- Quality / thin-spot pass if `story-sense` still flags voice after the strip
- Further campaign stories after [[#Epic 10 — Campaign|Story 10.1]] — not a return to the old Epic 8 roster plan

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
**Skill:** `systemic-worldbuilding` · **Status:** ✅ **core done (2026-08-22)** — the four-continent frame, all four continent notes, the calendar, and (pulled forward) the 4th ancestry are written. · Geography, climate, where the Trees grow, the physical stage.

> **Built as a reach-gradient.** The load-bearing call: the whole map is a **gradient of the [[Turning Tree|Trees']] reach** — sacred-dense origin → mercantile middle → thin frontier → storm-walled isle beyond. Physical map = cosmological map. → [[The World Frame]].

- [x] 🟡 **Geography & regions (`01 - World`)** → [[The World Frame]] (top-level) + four continents: **[[Maiethorn]]** (Motherland, full reach, holds [[Polity Archetypes|Threnmaieth]]), **[[Strandoren]]** (Shore-lands, high reach, trade, holds [[Polity Archetypes|Lestrand]]), **[[Heskoren]]** (Sundered Reach, thin reach, frontier, holds [[Polity Archetypes|Vaethorn]]), **[[The Sundering Isle]]** (Kumbaan — storm-walled, near-no reach, Yumboe homeland). The three archetype polities placed on three *different* continents; **rival faiths woven into the large continents** and now built ([[The Watching]] · [[The Fair Hand]] · [[The Old Ways]] · [[The Open Table]] — [[Faiths of the Turning]]).
- [x] 🟡 **Where Turning Trees grow** — the reach-gradient *is* this: densest/healthiest on Maiethorn, thinning outward, near-none across the storm-wall. Present-day thin reach = Tree-poor places (young/sick/few grafts), per [[The Ages of the Turning]] (the Grafting as a still-moving wave). Keystone edge kept GM-side in every continent note.
- [x] 🟡 **Astronomy/solstice — calendar locked** → [[The Reckoning of the Year]]: two solstices; the Leaf-Fall is **High Solstice / midsummer**, held **Turning-Week**; ~1400s-legible 12-month lunar-hinged calendar; [[The Sundering Isle|Kumbaan]] keeps the *moon, not the solstice* (a keystone tell).
- [x] 🟡 **(Pulled forward from Epic 4) — 4th custom ancestry built to full depth** → [[Yumboe]] (the good people / Bakhna Rakhna): three Daggerheart features (Hollow-Hill · Moon-Waked · The Unseen Hands), folklore-checked (Wolof/Senegambian *Yumboe* myth), small/pearly/silver, LOCKED. Its own non-Maiethren tongue seeded. The Isle *needed* its people, so the ancestry came here rather than waiting for Epic 4.
- **Map production aid (extracted Story R.10):** GPT Image prompts, Azgaar heightmap template, Maiethren + Kumbaan name bases, and the seed script live in `14 - Assets/Maps/Map Generation Tooling.md` — **not** inside player geography. Named waters, range, rivers, travel: [[Named Ground]]. Labelled picture: [[The Known Map]].
- **🟡 Deferred (tracked):** per-region *deep* climate/ecology. ~12 other great powers ✅ Story 7.1 → [[Powers of the Turning]]. Month-names + the Isle's name base ✅ Story 4.2. Rival faiths ✅ Story 1.4.

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
**Skill:** `settlement-design` · **Status:** ✅ **complete (2026-08-24).** Specific places, built on Epics 2–6. Residue types → [[Settlement Seeds]]. Named powers → [[Powers of the Turning]]. Playable squares → [[Harrow's Green]] · [[The Three Hamlets Past the Ford]] · [[The Third Hearth]] · [[Ornsael]]. Archetype seats → [[Eolvaeth]] · [[Orentel]] · [[Maiethlir]]. Do not rebuild the era spine. Do not treat Ornthael as post-history. Do not rebuild 7.1. Do not rebuild 7.2. Do not rebuild 7.3.

> Progressive elaboration. Unused leftover types (sick-Tree, guest-grove, lead road-end) stay types. Do not capture the First Seat. Do not make Harrow's or Ornsael a capital.

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
**Skill:** `oblique-worldbuilding`, `paradox-fables` · **Status:** 🟡 ongoing — runs *alongside* everything from Epic 0. · The revelation architecture (`11 - Secrets`). Seed the keystone secret in Epic 0; flesh reveals as notes that expose them get authored (`reveals:` front-matter).

---

## Epic 10 — Campaign
**Skill:** `key-moments`, `table-tone`, `dialogue` (`endings` later) · **Status:** 🟢 **Story 10.1 done (2026-08-31).** Actual play material (`12 - Campaigns`). Hub: [[The Isolated Fall]]. Kit: [[The Opening]]. Do not resume the old Epic 8 roster. Do not name the cutter, date the Tree, coin liturgy, or add a sixteenth power.

> **Locked opening (2026-08-31).** Session one sits at [[Harrow's Green]] — one existing square, live front, not a new town, not a capital, not a Protector fortress. On-screen: escaped remnant-walker + [[Rosire]] + the new Gift ([[Taeren]] as the hidden seat, *or* a PC in that seat). [[Reimaethe]] and [[Hithaen]] offstage. Five key moments, mystery first; one 5% wrongness beat; wonder at the isolated fall. No Leaf-Mother reveal. Agency stays on [[A Hidden Phoenix]]. Engine: [[When the Fire Is Caught]] — apparent two is leftover fire next to a Gift.

### Story 10.1 — The opening ✅ **DONE (2026-08-31)**
- [x] Sit session one in one existing square — [[Harrow's Green]], Hale-month, C.Y. 387. Not a new town. Not a Protector fortress.
- [x] Put the escaped Phoenix, the inside helper, and the new Gift on-screen; leave the Pourer and the Walled-Book heir offstage — walker (remnant NPC) · [[Rosire]] · [[Taeren]] XOR a PC in that seat. [[Reimaethe]] · [[Hithaen]] stay put.
- [x] Write four or five key moments, not a plot — mystery first (two tenses; Hope scars that do not match remembered deaths); wonder at the isolated fall (last Eolthael, unspoken); one 5% wrongness beat (harvested fire answering the new Gift); helper as choice, not confession. Do not reveal the Leaf-Mother. Do not fire the remnant-to-ash confirm.
- [x] GM kit, not a novel — opening situation, what the table can see, what stays player choice. Skills: `key-moments`, `table-tone`, `dialogue`. → [[The Opening]]

> **10.1 recorded decisions.** Unseen-leaf + remnant walker. A walker-PC who can still Rise is a different opening; do not stack it on Taeren as a second Gift. Taeren is of Brenod; the fall was the neighbour's week at Harrow's Tree (C-05). Rosire left Tesara's shed. The walker stays unnamed this session. No sixteenth power. World book untouched. Later sessions, fragments-as-campaign, and endings stay undecomposed.

### Later (do not decompose until asked)
- Memory-fragment continuation and later sessions
- `endings` when the campaign needs a close
- Do not resume the old Epic 8 roster to fill a court

---

## Progress

> Manual tally — update when checking boxes. (Story/Task counts, not epics.)

- **Pass two — verification:** 3 / 3 tasks of P2.1 (100%) ✅ **Story P2.1 complete 2026-08-31.** Later pass-two stories undecomposed. C-01 resolved; C-05 resolved in passing with the opening. **C-02 resolved 2026-08-31** by user-requested world-book rebuild.
- **Epic 10 — Campaign:** 4 / 4 tasks of Story 10.1 (100%) ✅ **opening done 2026-08-31.** Hub [[The Isolated Fall]] · kit [[The Opening]]. Later campaign stories undecomposed. Do not resume the old Epic 8 roster.
- **Epic R: Editorial repair and table readiness:** 97 / 97 tasks (100%) ✅ **closed 2026-08-31.** Gate: [[Epic R Completion Gate 2026-08-31]]. Stories **R.1–R.13** ✅. Residual export polish is **P2.1**, not a reopened R.13. Source: [[Editorial Audit 2026-08-29]]. **Story R.1 ✅** (population arithmetic; Unbound inside Bound; Premise is the sole census). **Story R.2 ✅** (Condition mechanics; one-Gift rule in [[When the Fire Is Caught]]; no level scaling). **Story R.3 ✅** (Hearth-Mark, not a trim; Mixed Ancestry as SRD; Yumboe GM-leave and full Kind; one surprise keyword; other kitchen). **Story R.4 ✅** — warden questions and Leaf-Fall failure on [[Turning Tree]]; dread → [[The Wrong Green]]; Other Hands wants / Orledd receive / allowance strain → [[The Other Hands]]; Open Table lintel → [[The Open Table]]. **Story R.5 ✅** — leaks walled; tag split (`keystone-adjacent` / `the-other-hands`); firing pin [[The Spent Leaf]] + [[The Remainder]]; rungs 1–5 deniable, rung 6 can fire; [[The Unspent]] outside the Five Hands. **Story R.6 ✅** — licence pool ≠ census; Tithe-provision as wells not grain; hearth-stand; road-word; crime ladder; urban Taken-In; prestige-walk chained (Netstrand berths → White Note terms → Orentel holds). **Story R.7 ✅** — lived faces [[The Holding Desk]] · [[The Standing Trade]]; Threnmaieth instruments [[The Reckoned Offices]]; three unlocked fights; header blocks; voice break; greens/halls folded; opposition can act; three engines [[The Pourers]] · [[The Walled Book]] · [[The Protectors]], kept distinct. **Story R.8 ✅** — six pivots + named wants in the three seats + four campaign seeds; hub [[People of the Turning]]. **Story R.9 ✅** — [[The Other Count]]; Closed Seat / [[The Closing]]; five dated years; three leftovers; Ledan query C.Y. 280; fifteen inherited claims. **Story R.10 ✅** — [[Named Ground]] (Old Crossing · Rain-Wall · four rivers · travel table) · [[The Known Map]] · tooling extracted to `14 - Assets/Maps/` · Kumbaan never aligned · Inner Close 🔒 in [[Orenbren]] · the Hinge Shore / Lirorn / Netstrand sharpened. **Story R.11 ✅** — Ornsael de-cloned (well-share); formula varied across seven; White Note walkable; Kumbaan committed ([[Ndenjoo]] · [[Njunda]] · crossing); leftovers given entrances/pressures; retrieval headers; scene-entering dangers. **Story R.12 ✅** — phonology and drift repaired; common handles promoted; *Aeloren* / *Eolstrand* retired; root families closed; fables and note voices differentiated; editorial mantras capped; deterministic naming tool stored. **Story R.13 ✅** — [[Build Plan]] rewritten; `locked` → `canon`; Conditions `player`; [[09 - Creatures]] filled; [[Rogue House Options]] archived; strip rule on [[Conventions]]; scaffolding moved; [[At the Table]] · [[Dangers of the Turning]] · [[A Hidden Phoenix]]. Engine untouched. World book rebuilt 2026-08-31 on explicit request (C-02).
- **Epic 0 — Foundations:** 7 / 7 tasks (100%) ✅ — setting named *The Turning* (2026-08-20); household elaboration 2026-08-23 → [[The Other Hands]]
- **Epic 1 — Anchor:** 15 / 15 tasks checked (100% of listed) — clergy orders → [[The Tree-Wardens]] (Story 5.1, names 🟡). Remaining leftover: Conditions cross-link (pending, not a checkbox)
- **Epic 3 — The World Frame:** 🟢 **core done (2026-08-22)** — 4/4 marked: [[The World Frame]] + four continents ([[Maiethorn]] · [[Strandoren]] · [[Heskoren]] · [[The Sundering Isle]]); calendar locked ([[The Reckoning of the Year]] — month-names filled Story 4.2); 4th ancestry ([[Yumboe]]) pulled forward. **Story R.10 ✅** named the waters and the range → [[Named Ground]] · [[The Known Map]]; tooling extracted to `14 - Assets/Maps/Map Generation Tooling.md`. Deferred: deep per-region climate/ecology. ~12 named-stub powers ✅ Story 7.1. Rival faiths ✅ Story 1.4.
- **Epic 4 — Cultures & Kinds:** custom ancestries **4/4 ✅**. **Story 4.2 ✅ and 🔒 (2026-08-23, user-approved)** → [[Kinds of the Turning]] · [[Naming People in the Turning]] · months · Kumbaan name base · leaf-colours. **Story R.3 ✅ (2026-08-30)** → [[Kind Heritage]] (Hearth-Mark, not a trim; Mixed Ancestry as SRD; Yumboe GM-leave and full Kind; one surprise keyword) · other kitchen. Revisit flag closed. Deep grammar still deferred. ~12 powers' stance-drifts ✅ Story 7.1 (no new grammars).
- **Epic 5 — Factions:** ✅ **COMPLETE (2026-08-23).** Stories 5.1–5.3 done → [[The Tree-Wardens]] · [[The Watchers]] · [[The Book-Hands]] · [[The Door-Keepers]] · [[The Table-Keepers]] · [[The Shore-Sitters]] · [[The Slide]] · [[Tithe-Infrastructure]] · [[The Greens-Keepers]] · [[The Hall-Keepers]] · [[The Stillers]] · [[The Element-Guilds]] · [[The Intake]] (names 🟡, do not rebuild). **Story R.7 ✅ (2026-08-30)** added lived faces and engines → [[The Holding Desk]] · [[The Standing Trade]] · [[The Pourers]] · [[The Walled Book]] · [[The Protectors]] · [[The Reckoned Offices]]; greens/halls folded as jurisdictions.
- **Epic 6 — History:** ✅ **COMPLETE (2026-08-24).** 8 / 8 of 6.1 🔒; 7 / 7 of 6.2; 6 / 6 of 6.3; 6 / 6 of 6.4. **Story R.9 ✅ (2026-08-30)** added the Other Count beside the clocks. Hub [[The Ages of the Turning]] · lived road [[The Walking Years]] · hinge [[The First Cut]] · war [[The Closing]] · residues [[The Years of Hands]] · chronicle [[The Other Count]] · leftovers [[The Low Wall]] · [[The Seeing-Ring]] · [[The Dry Stair]]. Names *Brenvaeth / Eoloren / Ornthael* 🔒. Present C.Y. 387 🔒. **Cutter still unpicked.** Nature of her limit still open. Closed Seat / crown-count / Hush-rate 🟡.
- **Epic 7 — Settlements:** ✅ **COMPLETE (2026-08-24).** 6 / 6 of 7.1 🔒. 5 / 5 of 7.2. 5 / 5 of 7.3. Hub [[Powers of the Turning]] · twelve stubs · four playable squares ([[Harrow's Green]] · [[The Three Hamlets Past the Ford]] · [[The Third Hearth]] · [[Ornsael]]) · three archetype seats ([[Eolvaeth]] · [[Orentel]] · [[Maiethlir]]). Names *Eolvaeth / Orentel / Maiethlir* 🟡. White Note placed on Orentel, not crowned. Cast on the seats → Story R.8 / [[People of the Turning]]. **Story R.11 ✅** — retrieval, de-clone, Kumbaan hall, leftover depth.
- **Epic 8 — People:** 🟢 **8.1 landed in Story R.8 (2026-08-30).** 5 / 5 of 8.1. Hub [[People of the Turning]] · six pivots · seat wants · four seeds. Do not rebuild. R.11 added [[Njunda]] and [[Ledan]] as mouths, not pivots. Hidden-Phoenix agency ✅ [[A Hidden Phoenix]]. Stories R.12–R.13 ✅. Epic R closed. Next: Pass two · P2.1.
- **Epic 2 — Society:** ✅ **COMPLETE (2026-08-21).** Frame locked (world scale + register + social guard); **all four stories + the naming pass done, core audited.** **2.1 (Law & Citizenship) ✅** → [[Law and Citizenship]]; **2.2 (Economy & the Tithe) ✅** → [[Economy and the Tithe]]; **2.3 (Daily Life) ✅** → [[Daily Life]]; **2.4 (Polity Archetypes) ✅** → [[Polity Archetypes]] (three corners, now named **Vaethorn / Lestrand / Threnmaieth**, seats **Eolvaeth / Orentel / Maiethlir**). **Naming pass ✅** → [[The Old Tongue]] + [[Naming in the Turning]]. Core audit complete → [[Epic 2 Audit Guide]]. **→ Story 4.2 done. Epic 5 complete (5.1–5.3). Epic 6 complete (6.1–6.4). Epic 7 complete (7.1–7.3). Story 8.1 landed in R.8. Stories R.9–R.13 ✅. Epic R closed. Next: Pass two · P2.1.**
- **Locked decisions:** **setting name (_The Turning_)**, two-layer model, engine, roster, all 10 Condition mechanics, **4 custom ancestries** (Kitsune · Selkie · Tengu · Yumboe), keystone secret (Leaf-Mother real+benevolent **but bounded & costly**), Tree topology (one Awakening Tree + living grafts), **world scale (~15 polities / 3+1 continents)**, **register (late-medieval + Condition-labor advances)**, **world frame (four continents on a reach-gradient: [[Maiethorn]] · [[Strandoren]] · [[Heskoren]] · [[The Sundering Isle]])**, **calendar (High-Solstice Turning-Week + twelve Maiethren months + three new-year's days)**, **five lived faiths** (Motherfaith + Watching / Fair Hand / Old Ways / Open Table — names 🔒), **household cosmology** (she Gives; Other Hands Strike — structure 🔒, Hand-names 🟡), **Kind-hearths not Kind-nations**, hearth-registers ***Kusawe / Sakoa / Gonan***, **Kind heritage (Hearth-Mark · Mixed Ancestry as SRD · Yumboe GM-leave and full Kind · surprise keyword once on Tengu)**, **leaf-colour table**, **era spine** (two clocks · Grafting as live wave · no universal year-zero · dating reveals stance · *Brenvaeth / Eoloren / Ornthael* 🔒 · C.Y. 387 🔒 · Tree undated · cutter unpicked · limit's nature still open), **First Cut lived** (five attributions uncollapsed · Cutting-leave as captured copy-right · spread inside locked bands · Kumbaan never), **residues lived** (walk's three jobs · Hands can un-Hands · road-past as credit · Heskoren live front · fate-pressure noted not rolled). Epic 5 complete (clergy/guild names 🟡). **~15 powers named and 🔒 (Story 7.1, user-approved 2026-08-24):** three corners + twelve stubs → [[Powers of the Turning]]; *Eolstrand* retired in R.12 and the slot remains [[The Hinge Shore]]. **Playable squares (Story 7.2, 2026-08-24):** [[Harrow's Green]] · [[The Three Hamlets Past the Ford]] · [[The Third Hearth]] · [[Ornsael]]. **Archetype seats (Story 7.3, 2026-08-24):** [[Eolvaeth]] · [[Orentel]] · [[Maiethlir]]. **Cast (Story R.8 / 8.1, 2026-08-30):** [[People of the Turning]]. **Other Count (Story R.9, 2026-08-30):** [[The Other Count]] · Closed Seat / [[The Closing]] · cutter still unpicked. **Named ground (Story R.10, 2026-08-30):** [[Named Ground]] · [[The Known Map]] · Inner Close 🔒 in Orenbren · Kumbaan never. **Settlements / Kumbaan (Story R.11, 2026-08-31):** Ornsael de-cloned; White Note walkable; Kumbaan committed ([[Ndenjoo]]); leftovers runnable. **Language / naming / voice (Story R.12, 2026-08-31):** common handles promoted; *Aeloren* / *Eolstrand* retired; fables and note voices differentiated; naming tooling stored. **Table readiness (Story R.13, 2026-08-31):** [[At the Table]] · [[Dangers of the Turning]] · [[A Hidden Phoenix]] · export strip on [[Conventions]]. **Epic R closed. P2.1 done. Opening ✅ [[The Opening]].**

## Links
- [[Build Plan]] — handoff brief (points here) · [[The Premise]] — design hub
- [[Epic R Completion Gate 2026-08-31]] — Epic R close · [[Contradictions]] — pass-two log
- [[Named Ground]] · [[The Known Map]] — Story R.10 geography
- [[Powers of the Turning]] — Epic 7 Story 7.1 hub · [[Maiethvael]] · [[Orenbren]] · [[Saelthael]] · [[The Hinge Shore]] · [[Lirorn]] · [[Brenledd]] · [[Leddvael]] · [[Trenledd]] · [[Netstrand]] · [[Ornled]] · [[Vaelhesk]] · [[Saelvaeth]]
- [[Harrow's Green]] · [[The Three Hamlets Past the Ford]] · [[The Third Hearth]] · [[Ornsael]] — Story 7.2 squares · [[Settlement Seeds]]
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
- [[The Isolated Fall]] · [[The Opening]] — Epic 10 Story 10.1
