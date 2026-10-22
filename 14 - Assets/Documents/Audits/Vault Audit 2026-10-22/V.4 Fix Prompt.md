---
title: V.4 Fix Prompt
type: reference
visibility: gm
note_status: draft
tags: [meta, audit, epic-v, prompt]
created: 2026-10-22
updated: 2026-10-22
---

# V.4 Fix Prompt

> **What this is.** The prompt for the agent that runs Story V.4 on the [[Roadmap#Epic V — Read the whole vault|Roadmap]]. Paste everything under "The prompt" into a new agent session. The orchestrator plans, hands out the work, checks it, and commits. Claude Sonnet 5.5 subagents make the edits. The fixes were already worked out in the audit, so no subagent needs a larger model.

## The prompt

You are the orchestrator for Story V.4 of Epic V in this Obsidian worldbuilding vault, the Daggerheart setting *The Turning*. An audit has already found what is wrong and how to fix it. Your job is to have subagents carry out those fixes in a safe order, check their work, and keep the trackers honest. You edit only the trackers and the contradictions log. The subagents edit the notes.

### Before anything else

1. Read `CLAUDE.md` in the repo root.
2. Read these, in this order:
   - `00 - Core/Meta/Roadmap.md`: the whole Epic V section, especially the **V.3 recorded decisions**. Those decisions are canon for this work.
   - `14 - Assets/Documents/Audits/Vault Audit 2026-10-22.md`: the report.
   - `11 - Secrets/Contradictions/Contradictions.md`: the Open table, C-10 to C-24.
   - `00 - Core/Meta/Conventions.md`: Plain prose and Player-safe export.
3. Make sure your checkout has the latest `master` (`git fetch origin master` and `git checkout master && git pull`). Then create a feature branch off `master`, named by your branch rules. Do not work on `master`. Do not merge unless the user asks.
4. Run `python3 "14 - Assets/Documents/Audits/Vault Audit 2026-10-22/mechanical_scan.py"`. It prints counts and writes the full hit list to `/tmp/vault-audit/mechanical.md`. Keep that first output; wave 3 compares against it.

### Subagents

- **Model.** Every subagent is **Claude Sonnet 5.5**. In Cursor's Task tool, set `model: claude-sonnet-5-5-high`. In Claude Code, use `model: sonnet`. Do not use Opus for subagents.
- **Ownership.** Every subagent in a wave owns a fixed set of folders and edits files only there. It may read any file to check a fact. No two subagents in a wave edit the same file. You own these files, and no subagent may edit them: `00 - Core/Meta/Roadmap.md`, `11 - Secrets/Contradictions/Contradictions.md`, `11 - Secrets/Reveal Index.md` (until wave 2), and everything in `14 - Assets/Documents/Audits/Vault Audit 2026-10-22/`.
- **Never.** No subagent touches `14 - Assets/Documents/Setting Book/` (the world book), runs git, or creates a new setting note, unless its task names one.
- **Parallel.** Launch each wave's subagents in parallel. Wait for every one to finish before you check the wave and commit.
- **Commit.** Commit once per wave with a clear message, and push the branch after wave 3.

### Wave 1: fix by folder (8 subagents in parallel)

| # | Owns (edits only here) | Findings note | Also does |
|---|---|---|---|
| 1 | `00 - Core`, except the Roadmap | `Findings 1 - Core.md` | Trims the Build Plan's "Active next" to one short paragraph per epic, saying what it built and what is next, with the history left to the Roadmap. Fixes the folder tree in Conventions. Fixes the stale lines in `Condition Audit.md` and `Epic 2 Audit Guide.md` |
| 2 | `01 - World`, `06 - Magic`, `10 - Items`, `13 - Game` | `Findings 2 - World, Magic, Items, Game.md` | Adds rows to Named Ground for Seinbrun, Naenor, Raitin, Natai, Tasain, Larbril, and the Seeing-Ring, with direction and travel time, taken from the seat notes, [[The Known Map]], and the atlas sheets in `14 - Assets/Maps/` (read the PNGs). It writes no distance the seat notes do not support; where they give none, it gives the direction and says the time is not recorded |
| 3 | `02 - History`, `11 - Secrets`, except Contradictions and the Reveal Index | `Findings 3 - History and Secrets.md` | Brings `A History of the Turning.md` and `The Library Pages.md` into line with the one-year-at-a-time decision |
| 4 | `03 - Cultures` | `Findings 4 - Cultures.md` | |
| 5 | `04 - Settlements` | `Findings 5 - Settlements.md` | Sanbreo is already fixed. Does not change the bread heel, the empty bowl, or the turned chair |
| 6 | `05 - Factions` | `Findings 6 - Factions.md` | Rewrites the gift on `The Pourers.md` to one year at a time |
| 7 | `07 - Religion`, `09 - Creatures` | `Findings 7 - Religion and Creatures.md` | Brings `The Unspent.md` and `Long-Lived.md` into line with one year at a time. Points the ten cards, the hub, and Turning Tree at [[Conditions]] for shares instead of the GM-only Premise, and checks that the hub's share table matches The Premise |
| 8 | `08 - People`, `12 - Campaigns`, `14 - Assets` except the world book and the Vault Audit 2026-10-22 folder; `99 - Archive` is read only | `Findings 8 - People, Campaigns, Assets.md` | Rewrites `14 - Assets/Documents/Library/Minutes of a Gift.md` as the minutes of one year, K.'s fifth, per the V.3 decision. Fixes `Reimaethe.md` and `Methei.md`. Fixes the stale status lines in `Editorial Audit 2026-08-29.md` and `Epic R Completion Gate 2026-08-31.md` |

Give each wave 1 subagent the **Shared brief** below, plus its row: the folders it owns, its Findings note, and its "Also does" column.

**Check the wave.** When all eight finish, read each subagent's report. Spot-check at least two high findings per group by opening the file. Run the scan again. Then commit: "Epic V V.4 wave 1: fix findings by folder". Check the eight wave 1 boxes on the Roadmap and update its Progress tally.

### Wave 2: across the vault (1 subagent)

One Sonnet subagent owns `11 - Secrets/Reveal Index.md` and may edit any note for a broken link only. Its tasks:

1. Rebuild the Reveal Index from every note's `reveals:` key and every secret's `reveal_tag`, as they stand now. Keep the index's existing layout.
2. Fix every broken link the scan lists. Repair the link to the right note. Where no note exists, make it plain text. Do not create notes.
3. Check that the C-01 (scaffolding in player bodies), C-04 (house-name markers), and C-07 (Rothallo called a town) leftovers are gone from the notes those entries name, and list any that remain.

Fix whatever item 3 lists, or hand it to a subagent. Commit: "Epic V V.4 wave 2: Reveal Index, links, old leftovers". Check the boxes and update the tally.

### Wave 3: check (8 readers, then you)

1. Run the scan and compare it with the first run and with `mechanical-scan.txt`. Every remaining hit of "mouth", "C.Y.", 🔒, 🟡, a story number, "Clock 1/2", "Leftover", or a percentage in a player body must be either allowed or fixed. Allowed: an Old Ways door, a Condition card's own share, the retired-form examples in Conventions, and anything under GM Notes on a tracker note.
2. Launch eight Sonnet readers, one per wave 1 group. They are **read-only**. Each rereads its folders against its Findings note and the V.3 decisions, and returns a short list of what is still wrong, with file, line, quote, and fix. Fix the lists yourself, or hand them to a subagent with the same ownership rules.
3. On Contradictions, move C-10 to C-24 into a new "Resolved in Epic V (2026-10-22)" table, each with a one-line resolution. Set the note's `updated` date.
4. Update the trackers. On the Roadmap: check the wave 3 boxes, update the Epic V Progress line and the spine row, and fix the stale "Next: Pass two · P2.1" lines in the Epic 2 and Epic 8 Progress entries. On the Build Plan: update the Epic V paragraph. Leave the V.4h world book box open; it is the user's.
5. Commit: "Epic V V.4 wave 3: check and trackers". Push the branch and open a draft pull request against `master`.
6. Tell the user what was fixed, what was left and why, and that the world book is waiting on their word.

### Shared brief (give this to every wave 1 subagent)

You are fixing one group of folders in an Obsidian worldbuilding vault for the Daggerheart setting *The Turning*. An audit already found the problems and wrote a fix for each one. Your job is to make those fixes in the files you own, without changing canon beyond what the decisions below say.

**Read first.**
1. `CLAUDE.md`.
2. `00 - Core/Meta/Conventions.md`: Plain prose and Player-safe export.
3. The **V.3 recorded decisions** in the Epic V section of `00 - Core/Meta/Roadmap.md`.
4. Your Findings note in `14 - Assets/Documents/Audits/Vault Audit 2026-10-22/`.
5. The Open table on `11 - Secrets/Contradictions/Contradictions.md`, for any C-item that touches your files.
6. The hits for your folders in `/tmp/vault-audit/mechanical.md`.
7. The skills `revision`, `prose-style`, and `voice-analysis` in `.claude/skills/`. Apply their methods directly and do not run their scripts.
8. The baseline voice: `02 - History/A History of the Turning.md` and `How a Place Speaks.md`. Ordinary sentences that say who does what, in words a person would say out loud.

**Work in this order, one note at a time.** Facts first, so a sentence pass does not polish a line that a fact fix then deletes.
1. **Facts and locks.** The C-items and V.3 decisions that touch the note.
2. **Leaks.** A GM truth in a player body goes under `## GM Notes`, or is cut. If `## Links` comes after `## GM Notes` at the same level, move Links above GM Notes, because export only strips from the GM heading down. Set `reveals:` to list the `reveal_tag` of any secret the player body still points at.
3. **Scaffolding.** 🔒 and 🟡, story and epic numbers, skill names, "Canon status" blocks, "Do not…" orders to the GM, "Built with…", "The fresh angle", "Leftover job on this street", "Clock 1 / Clock 2", the "~5% dial", "Unlock:", and the "X cannot afford to see…" and "On its face… Underneath…" paragraphs. Move each under `## GM Notes`, or delete it if the GM Notes already say the same thing. Where a label hides a fact ("Leftover job on this street: the blame"), keep the fact as a plain sentence in the body.
4. **The old voice.** A person is never a "mouth" or a "throat", in the player body or in GM Notes; say person, speaker, or who speaks for whom. "C.Y." becomes "Cut-year". Replace "lintel", "the sitting", "seen seeing", "a send", and the riddle "A kind Tree would not…" with the plain fact they stand for.
5. **The rest.** Every remaining medium and low finding for your files.

**Canon you must keep.**
- Kind is what you are born; a Condition is what you become; they stack. Population shares live only on The Premise. Condition cards may quote their own share.
- A child who misses the Tree is UnTurned, not Kept. Kept means the leaves hugged the child at the Tree.
- The Leaf-Mother is a belief in player text. Never confirm her, her reach, her limit, or her household there.
- The Pourers, the Walled Book, and the Protectors are three separate groups. The founder is never named and never called a god in player text. The Protectors catching Phoenix fire is GM only.
- Rothallo is inside Orenbren. There is no sixteenth power. Kumbaan has no Tree and never took a graft. Kinds are not nations.
- The present year is Cut-year 387. The Tree is undated. The cutter is unnamed. The Leaf-Mother's limit stays open.
- A habit the notes leave unexplained ("They will not say why.") stays unexplained.
- About 5% frightening.

**Do not.** Create new canon beyond the V.3 decisions. Add a power, a person, a place, or a rite. Name the cutter or the founder. Date the Tree. Touch the world book or any file outside your folders. Run git. Rewrite a note that the audit lists under "Strong — protect"; fix only its listed findings. If a finding is wrong, or its fix would break canon, skip it and say why.

**When you are done,** set `updated: 2026-10-22` (or today's date) on every note you changed. Reply with: the number of notes changed; for each high finding in your Findings note, fixed or skipped with the reason; the count of medium and low findings fixed and skipped; anything you found that the audit missed. Nothing else.

## Links
- [[Vault Audit 2026-10-22]] — the report
- [[Roadmap]] · [[Contradictions]] · [[Conventions]]
