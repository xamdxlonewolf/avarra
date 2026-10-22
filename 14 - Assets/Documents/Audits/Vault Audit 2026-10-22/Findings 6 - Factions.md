---
title: "Vault Audit 2026-10-22 — Findings 6 - Factions"
type: reference
visibility: gm
note_status: draft
tags: [meta, audit, epic-v]
aliases: []
created: 2026-10-22
updated: 2026-10-22
---

# Findings: 05 - Factions

Notes read: 38 (all finished)

## Patterns
- "Mouth" (and "throat") used for a person, a voice, or a market is in about 15 notes. Examples: `Criminal/The Standing Trade.md` (about 12 uses), `Governments/The Reckoned Offices.md`, `Governments/The Walled Book.md`.
- Design-essay "On its face… Underneath…" paragraphs follow the in-world texts in about 16 notes. Three of them leak GM facts: `Religious Orders/The Watchers.md`, `Religious Orders/The Door-Keepers.md`, `Religious Orders/The Tree-Wardens.md`.
- Designer labels show up in player text. "~5% dial" appears 9 times in 7 notes, "Unlock:" in 7 notes, and `oblique-worldbuilding` in 9 notes. All 12 power stubs have an axis header, a "Leftover:" label, and a Roadmap/Story link. Examples: `Guilds/The Stillers.md`, `Religious Orders/The Book-Hands.md`, `Governments/Powers/Maiethvael.md`.
- Protector fire leaks into player text in 5 notes: `Organizations/The Protectors.md`, `Religious Orders/The Pourers.md`, `Governments/The Walled Book.md`, `05 - Factions.md`, `Religious Orders/The Tree-Wardens.md`.
- "Vaelun's guest-grove" contradicts the First Bowl and Three Hamlets notes, which say the guest-grove is the First Bowl. It appears in 4 notes: `Religious Orders/The Watchers.md`, `Religious Orders/The Door-Keepers.md`, `05 - Factions.md`.
- The riddle "A kind Tree would not…" is in 4 notes: `Guilds/The Stillers.md`, `Guilds/The Element-Guilds.md`, `Criminal/The Slide.md`.

## Strong — protect
- `Religious Orders/The Pourers.md` is plain prose. The founder is never named and never called a god, the in-world text is explained in ordinary words, and the GM section says "Keep these apart."
- The three new sections of `Governments/The Walled Book.md` ("What a visitor sees", "The lesson and the count", "Outside the walls") quote The Premise correctly and use ordinary speech.
- `Organizations/Movements.md` is close to the baseline and matches the Pourers.
- No note in the folder merges or confuses the Pourers, the Walled Book, and the Protectors. Habits written as "They will not say why." have a GM guard and should stay as they are (`Guilds/Craft Fellowships.md`, `Military/The Watch and the Cohort.md`).

## Findings
- [HIGH] [LEAK] `05 - Factions/Organizations/The Protectors.md`:30 — "the Care's store unbroken" — Lines 30, 32, 42, 46 and 62 together show that the Care keeps a store of fire and gets it from the dying, and this player note lacks the `when-the-fire-is-caught` tag — Move these lines under `## GM Notes` and keep only "a hospice; the one is in care" in the player body.
- [HIGH] [LEAK] `05 - Factions/Organizations/The Protectors.md`:49 — "filed as hush, while the Care still holds a name" — Lines 22, 49 and 70 show that the Protectors hush a second white-fire on purpose, and the player body should not show this — Move these lines under `## GM Notes`.
- [HIGH] [LEAK] `05 - Factions/05 - Factions.md`:79 — "The harvest stays behind the wall." — The player body of the folder index says the Protectors harvest fire, at lines 79 and 83, and at line 117 as "controlled deaths, harvested fire" — Move these lines and the "Three opposition engines" table under `## GM Notes`.
- [HIGH] [LEAK] `05 - Factions/Religious Orders/The Pourers.md`:80 — "They will not take Phoenix fire. Another house does that" — This tells players that some house takes Phoenix fire, and the note lacks the `when-the-fire-is-caught` tag — Cut the second sentence, or move both sentences under `## GM Notes`.
- [HIGH] [LEAK] `05 - Factions/Governments/The Walled Book.md`:99 — "Do not store fire in the Close. Different engine." — This table row tells players that some other house stores fire — Move the row under `## GM Notes`.
- [HIGH] [LEAK] `05 - Factions/Religious Orders/The Watchers.md`:185 — "the hand has a household it will not let them name" — The narrator confirms a hidden hand and household that the player note should not confirm — Cut the sentence, or move it under `## GM Notes`.
- [HIGH] [LEAK] `05 - Factions/Religious Orders/The Door-Keepers.md`:158 — "whether a hand was in the water too, at the end of its reach" — The narrator hints at the Leaf-Mother's limited reach as if it were fact — Cut the sentence, or move it under `## GM Notes`.
- [HIGH] [LEAK] `05 - Factions/Religious Orders/The Tree-Wardens.md`:162 — "are the same sentence said from two distances" — The narrator confirms that the Leaf-Mother's reach is limited, which player text must keep as belief — Cut the sentence, or move it under `## GM Notes`.
- [HIGH] [CONTRA] `05 - Factions/Governments/Powers/Maiethvael.md`:42 — "a land where almost no child is Kept" — This contradicts The Premise (about 40% are hugged at the ceremony) and Walled Book line 57; The Premise wins — Say that the Close teaches a hug is rare, not that it is rare.
- [MED] [CONTRA] `05 - Factions/Governments/The Walled Book.md`:114 — "Talnin, Closed, unmarked, heir" — Line 96 says that calling a Closed Heir "unmarked" is an insult, but Delamem's leaf uses the word; the line 96 rule (and How a Place Speaks) wins — Change the leaf's wording, or say plainly that only the desk writes "unmarked."
- [MED] [CONTRA] `05 - Factions/Guilds/Craft Fellowships.md`:39 — "The Walled Book may assign a body to a mill as labour" — The Walled Book gives turns of work (green, hall, wall, road, beds) and never ownership or mill labour; the Walled Book wins — Change the line to match the Walled Book's turns of work.
- [MED] [CONTRA] `05 - Factions/Organizations/Tithe-Infrastructure.md`:82 — "The founder is still alive. They still sit the chair." — Next to "No librarian-order" (line 47), this clashes with the Pourers, who keep the deathless library and have an unnamed living founder in GM notes; the Pourers note wins — Remove the founder line and the "no librarian-order" claim, or point to the Pourers.
- [MED] [CONTRA] `05 - Factions/Religious Orders/The Watchers.md`:36 — "Vaelun's guest-grove" — The First Bowl and Three Hamlets notes say the guest-grove is the First Bowl; those notes win (same at line 147) — Change it to "the First Bowl, where Vaelun walks."
- [MED] [CONTRA] `05 - Factions/Religious Orders/The Door-Keepers.md`:126 — "Vaelun's guest-grove" — This contradicts the note's own line 34 and the First Bowl note; the First Bowl note wins — Change it to "the First Bowl."
- [MED] [CONTRA] `05 - Factions/05 - Factions.md`:22 — "Vaelun's guest-grove" — The First Bowl note wins — Change it to "the First Bowl."
- [MED] [LEAK] `05 - Factions/Religious Orders/The Tree-Wardens.md`:33 — "white-fire letter that does not come back from the Care" — This player hook points at the Care hushing fire, and the note lacks the reveal tag — Move the hook under `## GM Notes`, or cut the Care from it.
- [MED] [LOCK] `05 - Factions/Organizations/Tithe-Infrastructure.md`:52 — "~29% of people" — This is a share stated without a link to The Premise — Link The Premise next to the number, or remove the number.
- [MED] [HOLE] `05 - Factions/Governments/The Walled Book.md`:59 — "Closed Heir" — The rules cover a Closed Heir who is Given, but not one who is Struck later (lines 59 and 70), and this will come up at the table — Add one plain sentence on what the Close does when an heir is Struck.
- [MED] [VOICE] `05 - Factions/Religious Orders/The Pourers.md`:96 — "Do not merge the cup with a Protector sanctuary." — Designer instructions sit in the player table at lines 94, 96 and 97 ("Let them try.", "Keep the two apart.") — Move them under `## GM Notes`.
- [MED] [VOICE] `05 - Factions/Governments/The Walled Book.md`:20 — "a roll that will not share ink" — The old picture voice in the header (also line 24, "a gate that grew a country" and "How the sitting broke") — Say plainly what the guest-compact was and how the meeting failed.
- [MED] [VOICE] `05 - Factions/Governments/The Walled Book.md`:40 — "Conservative mouth." — "Mouth" is used for people (2 times: lines 40 and 139) — Name the speakers or the language plainly.
- [MED] [VOICE] `05 - Factions/Governments/The Walled Book.md`:75 — "They share a country. They do not share a page." — This is a slogan in place of a fact (also line 79, "Motherfaith leaking in") — Say who refuses to record what.
- [MED] [VOICE] `05 - Factions/Governments/The Walled Book.md`:95 — "Unlock:" — Designer labels and instructions fill the table at lines 95, 97, 98 and 100 ("Rithim is not their clerk", "church of the cup", "whose bite is first") — Rewrite them as plain facts, or move them under `## GM Notes`.
- [MED] [VOICE] `05 - Factions/Governments/The Walled Book.md`:116 — "On its face… Underneath" — This is a design-essay explanation of the in-world text — Explain the text in ordinary words, as the Pourers note does.
- [MED] [VOICE] `05 - Factions/Organizations/The Protectors.md`:38 — "Conservative mouth, quiet sleeve." — Shorthand pictures (also line 55, "fishbowl") — Say plainly what language they speak and how they are watched.
- [MED] [VOICE] `05 - Factions/Organizations/Movements.md`:45 — "That rule is the class… the war made it a wall." — Picture language (also line 47, "sit the Close" and "Lodging is not their flag"; line 22, "sat that refusal") — Say who does what.
- [MED] [VOICE] `05 - Factions/05 - Factions.md`:60 — "Wear [[The Unspent]]." — Designer voice in the player body (also line 75, "archived menu… unused as Slide jobs"; line 89, "doors, not colleges"; line 109; "mouth" at lines 45, 55, 70 and 97) — Rewrite as plain facts, or move under `## GM Notes`.
- [MED] [VOICE] `05 - Factions/Organizations/The Greens-Keepers.md`:20 — "will not follow you home" — Riddle lines ("the cousin they will not name", "go to seed") — Say the fact plainly.
- [MED] [VOICE] `05 - Factions/Organizations/The Hall-Keepers.md`:20 — "One lintel" — Designer shorthand (also line 22, the paragraph about the retired Aeloren; "A throat is still full") — Say what the house is and does.
- [MED] [VOICE] `05 - Factions/Organizations/Tithe-Infrastructure.md`:40 — "under one lintel" — Designer voice (also line 33, "A wilt three streets off is already a week."; lines 46–50, "Do not invent a warmth-guild…"; line 89, "Unlock."; line 100, "Videm's leash"; line 110, "Underneath") — Rewrite as plain facts, and move the instructions under `## GM Notes`.
- [MED] [VOICE] `05 - Factions/Military/The Watch and the Cohort.md`:20 — "cohort is a summer with a name" — Picture voice ("Talen hears a date", "until a mouth comes", "mouths that buy bread") — Say plainly who is enlisted and who is fed.
- [MED] [VOICE] `05 - Factions/Guilds/The Stillers.md`:41 — "~5% dial" — Designer labels (line 25, "clock in the surgeon"; "surgeon's-college story"; "Do not convert the guild"; line 130, "A kind Tree would not…"; line 142, `oblique-worldbuilding`) — Rewrite as plain facts, or move under `## GM Notes`.
- [MED] [VOICE] `05 - Factions/Guilds/The Intake.md`:20 — "Shed notice. Not a liturgy." — Telegraphic shorthand throughout ("Mandate (keep it to four)", "Do not convert the guild", "throat", line 79 "sell a mouth", line 91 "The empty face is the point") — Rewrite in full sentences about who does what.
- [MED] [VOICE] `05 - Factions/Guilds/The Element-Guilds.md`:126 — "A kind Tree would not…" — Riddle and designer voice ("metaphysical teeth", "Exit grievance", "The Warm", line 140 `oblique-worldbuilding`, "Underneath") — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Guilds/Craft Fellowships.md`:32 — "the mouth the square turns on" — Picture voice (also "a tied hull is weather") — Say who speaks for the square and what a tied boat means.
- [MED] [VOICE] `05 - Factions/Religious Orders/The Tree-Wardens.md`:88 — "(Taste call — see GM Notes.)" — Designer labels (line 40, "~5% dial"; line 44, "given a lintel"; lines 68 and 136, underdog-unit formula; line 158, oblique) — Rewrite as plain facts, or move under `## GM Notes`.
- [MED] [VOICE] `05 - Factions/Religious Orders/The Remainder.md`:20 — "janitors with a liturgical lintel" — Designer voice ("A desk, not a thirteenth house"; line 27, Quiet Cut reference) — Say plainly what the desk does.
- [MED] [VOICE] `05 - Factions/Religious Orders/The Watchers.md`:26 — "That is not a metaphor we are willing to finish" — Designer voice and tone talk ("dial failing"; "seen seeing"; "~5% dial" at lines 44, 110 and 157; line 40, "archaeology is the theology"; line 147, "Unlock."; "mouth" at lines 34, 86 and 94) — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Religious Orders/The Shore-Sitters.md`:20 — "Built thin on purpose" — Designer voice ("flavor"; line 62, oblique; line 66, "Underneath… wanted was never a gift") — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Religious Orders/The Book-Hands.md`:42 — "~5% dial" — Designer labels (line 143, "Unlock"; "Grace is a closed book"; line 171, oblique; "Underneath"; "travelling underdog") — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Religious Orders/The Door-Keepers.md`:26 — "mouth" — Designer voice ("mouth" at lines 26 and 40; line 42, dial; line 126, "Unlock"; line 142, "spatial + inheritance parallax"; line 154, oblique) — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Religious Orders/The Table-Keepers.md`:88 — "(taste still open)" — Designer voice ("That is the whole lintel"; line 152, lecture; line 164, oblique; "Underneath") — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Criminal/The Slide.md`:41 — "~5% dial" — Designer voice (lines 82 and 135–137, "unused trades/Back Table"; line 115, "Unlock"; line 132, "A kind Tree"; line 149, oblique; line 160, "this was pick C; A and B unused") — Rewrite as plain facts, and move design history under `## GM Notes`.
- [MED] [VOICE] `05 - Factions/Criminal/The Holding Desk.md`:38 — "Eroded mouth." — "Mouth" used for people and trades ("That mouth is The Standing Trade", "needs a mouth"), plus "Do not merge the trades" in the table — Name the speakers and trades plainly, and move instructions under `## GM Notes`.
- [MED] [VOICE] `05 - Factions/Criminal/The Standing Trade.md`:20 — "mouth" — "Mouth" is used for the product and its people about 12 times (line 40, "Eroded mouth, conservative quay"), and lines 70 and 76 are designer instructions — Say plainly what is sold and by whom, and move instructions under `## GM Notes`.
- [MED] [VOICE] `05 - Factions/Governments/Powers of the Turning.md`:72 — "lodging-mouth" — "Mouth" and "throat" used for people (the heading "Two mouths, same fifteen"; line 90, "White Note is a mouth"; lines 74 and 102, "governing throat"; line 100, "remembers the sitting") — Name the speakers and governments plainly.
- [MED] [VOICE] `05 - Factions/Governments/The Reckoned Offices.md`:22 — "the roll's mouths" — "Mouth" used for people ("## The four mouths", "preferred mouth"; lines 86 and 89, "Unlock"; "Underneath") — Name the four speakers plainly.
- [MED] [VOICE] `05 - Factions/Governments/Powers/Maiethvael.md`:20 — "The un-built warm rich core" — Designer axis header, a "Leftover:" label, and a Roadmap/Story link in the player body — Rewrite as plain facts, and remove the labels and the Roadmap link.
- [MED] [VOICE] `05 - Factions/Governments/Powers/Orenbren.md`:22 — "The inns grew a country" — Picture voice (line 30, "share a page" slogan; line 34, "Adaptive reuse at polity scale"), plus axis header, "Leftover:", and Roadmap link — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Governments/Powers/The Hinge Shore.md`:38 — "The cool cousin starts there as weather" — Picture voice ("a hinge has two sides" twice; line 22, design paragraph about retiring Eolstrand), plus axis header, "Leftover:", and Roadmap link — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Governments/Powers/Saelvaeth.md`:26 — "live front of Clock 2" — Designer labels ("Paying-enough, soil-enough, chain-enough nexts"; "Folk-right temptation in a kitchen drawer"), plus axis header, "Leftover:", and Roadmap link — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Governments/Powers/Trenledd.md`:46 — "~5%-scary dial's bureaucratic edge" — Designer labels ("governing throat"), plus axis header, "Leftover:", and Roadmap link — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Governments/Powers/Leddvael.md`:18 — "honesty was a cough" — Picture voice (line 22, "that taste-lock stands"), plus axis header, "Leftover:", and Roadmap link — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Governments/Powers/Brenledd.md`:32 — "this note does not name them" — The narrator talks about the note itself ("single throat"), plus axis header, "Leftover:", and Roadmap link — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Governments/Powers/Netstrand.md`:20 — "how a night shore remembers it is a night shore" — Riddle voice, plus axis header, "Leftover:", and Roadmap link — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Governments/Powers/Lirorn.md`:32 — "No new mouth." — Shorthand, plus axis header, "Leftover:", and Roadmap link — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Governments/Powers/Vaelhesk.md`:30 — "Play with the Door-Keepers and with Nethiro" — Designer instruction in the player body, plus axis header, "Leftover:", and Roadmap link — Move it under `## GM Notes`.
- [MED] [VOICE] `05 - Factions/Governments/Powers/Ornled.md`:20 — "a luxury that died in a cart" — Picture voice, plus axis header, "Leftover:", and Roadmap link — Rewrite as plain facts.
- [MED] [VOICE] `05 - Factions/Governments/Powers/Saelthael.md`:1 — "Theology high · reach high · governance low" — Designer axis header, a "Leftover:" label, and a Roadmap/Story link in the player body — Remove the labels and the Roadmap link.
- [LOW] [LEAK] `05 - Factions/Religious Orders/The Remainder.md`:36 — "A house that wants the scrap as fire." — This hints that a house collects fire — Cut it, or move it under `## GM Notes`.
- [LOW] [CONTRA] `05 - Factions/Military/The Watch and the Cohort.md`:52 — "a town" — The Inner Close (Rothallo) is called a town, but the Rothallo note calls it the walled capital city; the Rothallo note wins — Change it to "the walled city."
- [LOW] [CONTRA] `05 - Factions/Religious Orders/The Tree-Wardens.md`:178 — "I ate at Vaelun first because the grove asked" — This is in-world speech that treats Vaelun as the grove; the First Bowl note wins — Change "Vaelun" to "the First Bowl."
- [LOW] [VOICE] `05 - Factions/Religious Orders/The Pourers.md`:105 — "read a winter" — Old voice in an in-world text; allowed there, but it is the only one in the note — Leave it, or change it to "read a year."
- [LOW] [VOICE] `05 - Factions/Governments/The Walled Book.md`:120 — "Engine two of three" — GM notes carry designer labels (line 121, "Placement 🔒 (Story R.10)") — Remove the tags and story numbers.
- [LOW] [VOICE] `05 - Factions/Governments/The Walled Book.md`:82 — "White-fire… not a relic" — A shorthand line — Say plainly what white-fire is to the Book.
- [LOW] [VOICE] `05 - Factions/Guilds/The Stillers.md`:1 — "🟡" — GM notes carry 🟡/🔒 canon-status tags — Remove the tags.
- [LOW] [VOICE] `05 - Factions/Organizations/Movements.md`:24 — "C.Y. 38" — "C.Y." is used in prose (also in The Watch and the Cohort ×4, Powers of the Turning, and the power stubs) — Write the year out as the house style asks.
- [LOW] [VOICE] `05 - Factions/Religious Orders/The Tree-Wardens.md`:62 — "Speaked" — A misspelling (also The Remainder line 24) — Change it to "Spoken."
- [LOW] [STALE] `05 - Factions/05 - Factions.md`:31 — "twelve stubs" — The Hinge Shore, Lirorn and Netstrand are still drafts — Say how many stubs are finished, or mark the drafts.
- [LOW] [STALE] `05 - Factions/Governments/Powers/Trenledd.md`:50 — "P2.1 tracker move… Story 7.3" — A tracker line sits under `## Links` and will survive export — Remove the line.
- [LOW] [HOLE] `05 - Factions/Governments/Powers/The Hinge Shore.md`:28 — "`[[Lestrand]]`" — More than one file uses this alias, so the link is ambiguous — Link the exact note.
- [LOW] [HOLE] `05 - Factions/Governments/Powers of the Turning.md`:1 — "`[[Naming Tools]]`" — This resolves only through an alias on `14 - Assets/Names/README.md` — Link the README by name.
- [LOW] [MECH] `05 - Factions/Organizations/The Protectors.md`:1 — "status: hidden" — A public hospice is marked hidden — Set the status that matches a known, public house.
- [LOW] [MECH] `05 - Factions/Organizations/The Greens-Keepers.md`:1 — "reveals:" — The reveal tag is not supported by anything in the player body (same in The Hall-Keepers and The Shore-Sitters) — Remove the tag, or add the text it guards.
- [LOW] [MECH] `05 - Factions/05 - Factions.md`:1 — "- - " — The GM section has doubled bullets — Remove the extra dash.
- [LOW] [MECH] `05 - Factions/Military/The Watch and the Cohort.md`:1 — "Sirtol" — This name collides with "Sirtal" elsewhere in the vault — Rename one of them.
- [LOW] [MECH] `05 - Factions/Governments/Powers/Netstrand.md`:1 — "[[Netstrand]]" — The note links to itself — Remove the self-link.

## Links
- [[Vault Audit 2026-10-22]] — the report
