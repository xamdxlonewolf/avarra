---
title: "Vault Audit 2026-10-22 — Findings 8 - People, Campaigns, Assets"
type: reference
visibility: gm
note_status: draft
tags: [meta, audit, epic-v]
aliases: []
created: 2026-10-22
updated: 2026-10-22
---

# Findings: 08 - People, 12 - Campaigns, 14 - Assets (excluding Setting Book), 99 - Archive

Notes read: 77 (all finished)

## Patterns
- "Mouth" used for a person in player text, about 28 notes and more than 80 uses — for example `08 - People/People of the Turning.md`, `08 - People/Historical Figures/Taerso.md`, `08 - People/Leaders.md`.
- Older seed NPC notes that predate the H-stories and now contradict the Pourers and the Walled Book, 2 notes — `08 - People/NPCs/Reimaethe.md`, `08 - People/NPCs/Methei.md`.
- Seed notes that still carry "what this note does not do" lists and story numbers that later stories settled, 2 notes — `08 - People/NPCs/Hithaen.md`, `08 - People/NPCs/Reimaethe.md`.
- Names that sound too alike in one place, 5 places — Orentel (Sorim and Sorel), the Maiethorn seats (Brimaen, Breolnir, Breillai, Brormei), the six-pivot table (Valen and Valein).
- Hints at the Protectors' Phoenix fire in player bodies, 2 notes — `08 - People/People of the Turning.md`, `08 - People/NPCs/Rosire.md`.
- Status lines in the audit notes that later work has closed, 2 notes — `14 - Assets/Audits/Editorial Audit 2026-08-29.md`, `14 - Assets/Audits/Epic R Completion Gate 2026-08-31.md`.

## Strong — protect
- The campaign kits keep every lock: no session reveals the Leaf-Mother, one Gift holder only (Taeren or a player character), the Pourers stay offstage, and each kit has clear stop lines and a "What the table can see" list.
- The six Library pages and `02 - History/The Library Pages.md` index: no page names the founder, calls the founder a god, ages the Unspent, or ties the three groups together, and the index records each page's deliberate error without fixing it.
- The S-epic seat NPCs (Brimaen, Breolnir, Derdil, Mursur and others) each carry one unexplained habit with a GM guard against explaining it.
- The historical-figure notes leave the cutter of the First Cut unpicked and give no one a house-name.

## Findings
- [HIGH] [CONTRA] `08 - People/NPCs/Reimaethe.md`:22 — "poured four years into a cup and wants to stop before the fifth" — `The Pourers.md` says "A member gives five years into the cup" as one gift, but Reimaethe gives them one at a time; line 26 repeats this ("The fifth is the one the circle treats as the real gift") — The Pourers should win because H.1 and H.6 locked it later; rewrite Reimaethe around one five-year gift that is coming due.
- [HIGH] [CONTRA] `08 - People/NPCs/Methei.md`:21 — "they stop at dark if they are allowed to stop" — `The Walled Book.md` (lines 53 and 127) says a person with a Condition can walk out and the turns of work are owed by people living inside the walls, but Methei reads as held to the beds; line 37 and the fear at line 45 ("makes the bed into the rest of a life") repeat it — The Walled Book should win because H.2 locked it; rewrite Methei as a resident owing turns who can leave.
- [HIGH] [LEAK] `08 - People/People of the Turning.md`:142 — "Hidden second fire | [[Taeren]]" — a player table tells players there is a hidden second Phoenix fire, and `reveals: []` does not list it — Move the row under GM Notes or reword it to Taeren's public hook, and add `when-the-fire-is-caught` to reveals if anything stays.
- [HIGH] [LEAK] `08 - People/NPCs/Rosire.md`:26 — "a house that keeps a fire safe and does not show it" — with "The house is [[The Protectors]]" and the closed lamp at line 39, the player body points straight at the Protectors holding Phoenix fire — Move the fire and lamp lines under GM Notes and keep only Rosire's public work in the body.
- [MED] [STALE] `08 - People/NPCs/Hithaen.md`:44 — "Does not name the surviving power... later geography story" — The Walled Book and Rothallo have since settled this — Delete the stale line or replace it with links to those notes.
- [MED] [STALE] `08 - People/NPCs/Hithaen.md`:48 — "R.10 may still move the Inner Close" — R.10 is finished and the Inner Close is placed — Delete the caveat.
- [MED] [VOICE] `08 - People/NPCs/Hithaen.md`:60 — "(Story R.8 seed; placement still R.10)" — a designer story label sits in a player Links section that survives export — Remove the parenthesis.
- [MED] [STALE] `08 - People/NPCs/Reimaethe.md`:46 — "Does not name a sect. Does not write the withdrawal-price as law." — `The Pourers.md` now names the group and sets the price (the papers come back as the thinner copy) — Delete the list and link The Pourers.
- [MED] [VOICE] `08 - People/NPCs/Reimaethe.md`:26 — "cupboard" — the banned picture of the Unspent appears in the player body — Say the Unspent stores what it is given.
- [MED] [VOICE] `08 - People/NPCs/Reimaethe.md`:60 — "(Story R.8 seed)" — a designer story label in a player Links section — Remove it.
- [MED] [VOICE] `08 - People/People of the Turning.md`:40 — "mouth" — "mouth" stands for a person or speaker about 10 times (lines 40, 66, 70, 74, 76, 96, 112, 114, 127) — Say "speaker", "clerk", or the actual office.
- [MED] [VOICE] `08 - People/08 - People.md`:21 — "Dead mouths" — headings "Dead mouths", "Seat mouths" and "House-mouths" use "mouth" for people, 4 times (lines 21, 25, 40, 70) — Rename them "Historical figures", "Seat leaders", "House speakers".
- [MED] [VOICE] `08 - People/Leaders.md`:17 — "Mouth" — the column header and two headings ("Offices that already have a mouth", "Where the other mouths already are") use "mouth" for office-holders, 4 times — Use "Holder" and "office-holders".
- [MED] [VOICE] `08 - People/Heroes and Villains.md`:36 — "mouth" — "mouth" for a person, 2 times (lines 36, 40) — Name the role.
- [MED] [VOICE] `08 - People/Historical Figures/Taerso.md`:7 — "berth-mouth" — the front-matter role and about 8 body uses call Taerso a mouth — Say what the job was, for example "berth clerk" or "berth speaker".
- [MED] [VOICE] `08 - People/Historical Figures/Hildal.md`:21 — "the last mouth" — "mouth" for a person, 3 times (lines 7, 21, 49) — Name the office Hildal held.
- [MED] [VOICE] `08 - People/Historical Figures/Hildal.md`:37 — "the sitting" — banned phrase for a meeting, 2 times in the player body (lines 37, 40) and 2 in GM Notes — Say "the meeting" or name the council.
- [MED] [VOICE] `08 - People/Historical Figures/Ledan.md`:21 — "the writing-mouth" — alias and body call Ledan a mouth, 4 times (lines 21, 23, 33 and the alias), plus "Tide in the door." and "the house is one mouth" — Say "the clerk who wrote it down" and state what the house did.
- [MED] [VOICE] `08 - People/Historical Figures/Sedrad.md`:37 — "mouth" — "mouth" for a person, 3 times (lines 37, 40, 52) — Name the role.
- [MED] [VOICE] `08 - People/Historical Figures/Dirrol.md`:37 — "mouth" — "mouth" for a person, 2 times (lines 37, 54) — Name the role.
- [MED] [VOICE] `08 - People/Historical Figures/Vaethod.md`:33 — "mouth" — "mouth" for a person, 4 times (lines 33, 41, 55, 59) — Name the role.
- [MED] [VOICE] `08 - People/Historical Figures/Monseoth.md`:40 — "mouth" — "mouth" for a person, once; Narol line 50 and Rithnali line 44 have the same, once each — Name the role in all three.
- [MED] [VOICE] `08 - People/NPCs/Dumu.md`:33 — "The mouth is here. The canopy is not." — "mouth" for a person 4 times (lines 33, 37, 44, 54), and line 31 "A week that still has no door except a child's walk" is a picture standing in for a fact — Say who is here and what the only way out is.
- [MED] [VOICE] `08 - People/NPCs/Lertho.md`:41 — "mouth" — "mouth" for a person, 3 times (lines 41, 49, 51) — Name the role.
- [MED] [VOICE] `08 - People/NPCs/Thilim.md`:33 — "mouth" — "mouth" for a person, 3 times (lines 33, 38, 61) — Name the role.
- [MED] [VOICE] `08 - People/NPCs/Rithim.md`:36 — "mouth" — "mouth" for a person, 2 times (lines 36, 56) — Name the role.
- [MED] [VOICE] `08 - People/NPCs/Hithaen.md`:29 — "mouth" — "mouth" for a person, 2 times (lines 29, 39) — Name the role.
- [MED] [VOICE] `08 - People/NPCs/Taeren.md`:39 — "mouth" — "mouth" for a person, 2 times (lines 39, 40) — Name the role.
- [MED] [VOICE] `08 - People/NPCs/Brormei.md`:7 — "mouth at the meeting of road and wash" — the front-matter role and one body use call Brormei a mouth — Say what Brormei does at the crossing.
- [MED] [VOICE] `08 - People/NPCs/Mataero.md`:55 — "mouth" — "mouth" for a person once; Derdil line 44, Saelid line 22, Turvo, Vuthbraen, Nubo, Sulnu and Sorim have the same once each — Name the role in each note.
- [MED] [VOICE] `08 - People/NPCs/Tesara.md`:38 — "The ~5% stays at the rope" — the design tone label sits in the player body, beside "Catch. Steady. Hand to the year." and "Success is silence" at lines 37–38 — Say plainly what Tesara does at the rope and what goes wrong if it fails.
- [MED] [VOICE] `08 - People/NPCs/Taeren.md`:43 — "Isolation is the leftover square" — "leftover" is a banned design label — Say what isolation costs Taeren.
- [MED] [VOICE] `08 - People/NPCs/Sorim.md`:38 — "Prestige is the leftover on this street." — "leftover" is a banned design label — Say who on the street wants prestige and why.
- [MED] [VOICE] `08 - People/NPCs/Vamar.md`:21 — "A throat this note does not name" — "throat" is a nickname for the governing body, 2 times with "the governing throat" — Name the council or say "the people who govern".
- [MED] [VOICE] `08 - People/NPCs/Turvo.md`:30 — "one throat" — "throat" stands for a group speaking together — Say who speaks.
- [MED] [VOICE] `08 - People/NPCs/Laevila.md`:21 — "Filed as the second column. Has a day job." — insider shorthand and "make the amber stay in the air" replace plain facts — Say what role Laevila plays and what the amber does.
- [MED] [HOLE] `08 - People/NPCs/Sorim.md`:1 — "Sorim" — Sorim and Sorel live in the same city, Orentel, and sit in the same want table, so a table will mix them up — Rename one of them using the naming method.
- [MED] [HOLE] `08 - People/NPCs/Valein.md`:1 — "Valein" — Valein (Maiethlir) and Valen (Orentel) both sit in the six-pivot table — Rename one of them.
- [MED] [HOLE] `08 - People/NPCs/Breolnir.md`:1 — "Breolnir" — the Maiethorn seats cluster on "Br-": Brimaen and Breolnir in Rothallo, Breillai in Seinbrun, Brormei in Larbril, plus Brudu, Brenod, Brenthael, Braetu, Brenledd — Rename the newest two in Rothallo and Seinbrun to break the cluster.
- [MED] [HOLE] `08 - People/Historical Figures/Taerso.md`:1 — "Taerso" — Taerso (historical) sounds like Taeren (the opening's Gift holder), and the Taerso note's Sirtol sounds like the Reckoned Offices' Sirtal — Rename Taerso or Sirtol; Taeren should keep its name because the campaign uses it.
- [MED] [HOLE] `08 - People/Historical Figures/Ledan.md`:1 — "Ledan" — Ledan and Lertho are both quay clerks with near names — Rename one of them.
- [LOW] [HOLE] `08 - People/NPCs/Thilim.md`:21 — "Seine" — Thilim's Held-bed name Seine sounds like the city Seinbrun — Rename the bed.
- [LOW] [HOLE] `08 - People/NPCs/Rithim.md`:1 — "Rithim" — Rithim sounds like Rithnali, and the cast has six V- names (Vaethod, Valen, Valein, Vamar, Vehaela, Vuthbraen) — Spread future names away from these starts.
- [LOW] [HOLE] `08 - People/NPCs/Brimaen.md`:21 — "a Conditioned person" — the note relies on Brimaen having a Condition but never names it; Breolnir has the same gap and Methei is only "Given" — Name each Condition from the ten.
- [LOW] [CONTRA] `08 - People/NPCs/Mataero.md`:21 — "Twelve beds. Eight let. Four open for Eolthael. North bed not to let." — the counts add to thirteen unless the north bed is one of the four; `The White Note House.md` line 61 has the same line — Say which group the north bed belongs to in both notes.
- [LOW] [CONTRA] `08 - People/NPCs/Saelid.md`:26 — "They have not asked him" — Saelid calls Vaethod "him", but `Vaethod.md` uses "they" — Vaethod's own note should win; change "him" to "them".
- [LOW] [VOICE] `08 - People/Historical Figures/Hildal.md`:37 — "C.Y." — "C.Y." is used in player prose across the historical figures (Dirrol 21; Limrae 37, 50; Narol 21, 37; Taerso 21, 37, 39; Hildal 37; Ledan 21; Vaethod 60) — Write "Cut-year" in prose.
- [LOW] [VOICE] `08 - People/NPCs/Hithaen.md`:25 — "Kept blood is still a class" — this implies being Kept is inherited, but Kept is a Leaf-Fall outcome — Say that families with many Kept still form a class.
- [LOW] [MECH] `08 - People/People of the Turning.md`:5 — "epic-r, story-r-8" — story tags in the front-matter of a player note; `14 - Assets/Maps/The Atlas Sheets.md` has the same — Drop the story tags.
- [LOW] [MECH] `14 - Assets/14 - Assets.md`:39 — "- - **Maps (Story R.10):**" — an orphan double bullet with a story number, and the front-matter says `note_status: stub` on a filled MOC — Fix the bullet, drop the story number, and set the status to draft.
- [LOW] [HOLE] `14 - Assets/14 - Assets.md`:41 — "Maps" — the MOC does not list `Documents/Library/` or `Audits/` — Add both sections.
- [LOW] [MECH] `14 - Assets/Map Generation Tooling.md`:598 — "## ② Azgaar heightmap template" — the heading appears twice (lines 598 and 600) — Delete the duplicate.
- [LOW] [MECH] `14 - Assets/Map Generation Tooling.md`:1 — "Waandi" — the Kumbaan name base lists Waandi twice, and the Maiethren base still feeds retired coinages (Vaeloren, Orenvael) to the generator — Remove the duplicate and the retired names.
- [LOW] [STALE] `14 - Assets/Maps/The Atlas Sheets.md`:566 — "selected Prototype 3 and retained alternatives" — the alternatives were archived on 2026-10-03 — Say they are archived and link the archive.
- [LOW] [HOLE] `12 - Campaigns/The Isolated Fall/The Walk Home.md`:23 — "Explain the cup" — this cup is the hamlets' cup but the line does not link it, so a GM may read it as the Pourers' cup; line 98 "Do not put the cup on the rock" has the same gap — Link The Three Hamlets Past the Ford at both lines.
- [LOW] [CONTRA] `12 - Campaigns/The Isolated Fall/The Opening.md`:21 — "Next week is Eolthael" — line 58 says "Leaf-Fall is next month", and The Walk Home repeats both — Use one timing in both kits; "next week" should win because the opening scene is built on it.
- [LOW] [VOICE] `12 - Campaigns/The Isolated Fall/The Isolated Fall.md`:22 — "The lamp they kept still knows more than one mouth." — GM-only picture standing in for a fact; The Opening ("The lamp that knows two mouths", "extra mouths"), The Walk Home and The Week Still Open use "mouth" the same way many times — Say who has carried or spoken over the lamp.
- [LOW] [STALE] `14 - Assets/Audits/Editorial Audit 2026-08-29.md`:3 — "status: active" — it "Covers Epics 0–7 complete + Epic 8 pending", and the Epic R Gate closed all its findings — Mark it superseded.
- [LOW] [STALE] `14 - Assets/Audits/Epic R Completion Gate 2026-08-31.md`:165 — "Pass-two residual P2.1" — the Build Plan says P2.1 was resolved on 2026-08-31, but the gate still lists it as open here and in §3, and `status: active` remains — Mark P2.1 resolved and set the status to closed.
- [LOW] [STALE] `14 - Assets/Audits/Epic R Completion Gate 2026-08-31.md`:1 — "World book. Still carries *Eolstrand*, *Aeloren*" — the book was rebuilt on 2026-08-31 and 2026-10-05, so §3 and §6.5 ("World book stays stale until an explicit rebuild") are out of date — Note that the rebuilds cleared these.

## Links
- [[Vault Audit 2026-10-22]] — the report
