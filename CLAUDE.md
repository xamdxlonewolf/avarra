# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **worldbuilding repository** and serves as an **Obsidian vault** for a tabletop RPG setting. There is no application code, build system, or tests — content is detailed Markdown notes organized in a structured folder system, each with YAML front-matter that drives metadata-based search and discovery.

The tabletop system is **Daggerheart**.

## What the setting is

> **Active setting (started 2026-08-14): an integrated-"monsters" world.** Vampires, werewolves, and their kin exist and are **accepted, employed, and needed** members of society — not hidden, not a persecuted underclass, each a *fresh* reinvention rather than the horror-movie cliché. Tone dial: **~5% scary** (mostly mundane neighbours/colleagues; a real, dangerous obstacle underneath).

**The design spine (LOCKED — do not re-litigate):**
- **Two-layer model:** every person has a **Kind** (what you're *born* — a Daggerheart ancestry, mundane) and, for ~75% of people, a **Condition** (what you *become* — an *acquired* transformation). They **stack**. Sorting test: *becoming = Condition; born-that-way = Kind.*
- **Acquisition engine:** two paths. **Given** at the **Leaf-Fall** (a child's 10th-year solstice at a town **Turning Tree**; a leaf-colour = a Condition Given, a hug/no-colour = one of **the Kept**), or **Struck** by a later threshold (dying, an oath, a drowning). Pop. math ~60% Given · ~15% Struck · ~25% Kept.
- **Every Condition carries a Tithe** — an upkeep that must never seize control of the PC; the scary edge is opt-in.
- **The Leaf-Mother** is a *belief, not confirmed cosmology* (deliberate live schism).

**Key notes (the vault is the source of truth):**
- **[[Build Plan]]** (`00 - Core/Concept/`) — fast status brief + next task.
- **[[Roadmap]]** (`00 - Core/Meta/Roadmap.md`) — **the detailed build tracker** (Epics → Stories → Tasks, dependency-ordered, canon-status tags, progress tally). **Consult it to know what we're working on and in what order.**
- **[[The Premise]]** (`00 - Core/Concept/`) — the design hub (full locked detail).
- The 10 Conditions live in `09 - Creatures/Conditions/`; the 4 custom ancestries (Kitsune, Selkie, Tengu, Yumboe) in `03 - Cultures/Peoples/`.
- **World book** (`14 - Assets/Documents/Setting Book/`) — compiled reading copy (HTML + PDF). Vault notes are canonical. **Do not update the world book as we go** — see below.

## How we build this world (workflow)

We build **incrementally, in dependency order**, tracked in **[[Roadmap]]**. Follow this loop:

1. **Know the current work.** At the start of a session, read [[Build Plan]] then [[Roadmap]] to see the active epic and the next unchecked task. Work top-down through the epics unless the user redirects.
2. **Pass one — build.** Do the design work for a task/story using the right craft skill; write the canonical note(s) in the vault; then **check the box** in [[Roadmap]] and update its **Progress** tally. Advance canon-status tags as decisions firm up (🟡 Proposed → 🔒 Locked). When an epic finishes, note it and move to the next. **Do not** fold the new work into the world book as part of finishing a task.
3. **When the Roadmap hits 100% (pass one complete),** do **pass two — verify:** a review sweep over the whole world for consistency, contradictions (log/resolve under `11 - Secrets/Contradictions`), gaps, and quality — using `story-sense` to route what feels off. Only after pass two is the world considered settled.
4. **Keep the tracker honest.** Update [[Roadmap]] and [[Build Plan]] *as part of finishing a task*, not later. Progressive elaboration: only decompose the next 1–2 epics to task depth; leave later epics coarse until reached.

## The world book (compiled reading copy)

Location: `14 - Assets/Documents/Setting Book/`

| File | What it is |
|---|---|
| `STRUCTURE.md` | Locked spine (chapter numbers/titles do not move) |
| `chapters/` | One markdown file per chapter — this is what you edit |
| `The-Turning-World-Book.html` / `.pdf` | Compiled reading copies |
| `build_world_book.py` | Rebuilds HTML + PDF from the spine + chapters |
| `README.md` | Short how-to |

**Never update the world book as we go.** The vault is the source of truth and is what you write when finishing a story/epic. The world book is a *compiled reading copy* for audit. Update it **only when the user explicitly asks** (e.g. "update the world book", "rebuild the PDF", "fold the new work into the setting book"). Do not treat finishing an epic, checking a Roadmap box, or "keep the tracker honest" as a trigger to touch the book.

**When asked to update it:**
1. Read `STRUCTURE.md`. Find the existing chapter. Do **not** invent a parallel outline or new chapter numbers.
2. Edit `chapters/<file>`. Replace a **Not yet written.** block, or add under a heading that already exists. If something has no home, add a reserved heading *inside* the nearest chapter and note it in `STRUCTURE.md`.
3. Write as settled setting: no design notes, no LOCKED tags, no epic/story numbers, no "why we chose this."
4. Rebuild: `python3 "14 - Assets/Documents/Setting Book/build_world_book.py"`
5. Do not rename chapter files or reorder the spine to make a new idea fit.

## Vault structure & conventions

The vault uses numbered top-level folders (`00 - Core` … `14 - Assets`, `99 - Archive`) on a four-layer model — **World** (what exists), **Campaign** (what happened), **Secrets** (what the GM knows), **Canon** (what is actually true). The full folder tree, front-matter schema, and `type` vocabulary live in **`00 - Core/Meta/Conventions.md`** — that file is the source of truth; consult it before creating notes. Per-kind templates are in `00 - Core/Meta/Templates/`.

**GM-secret / spoiler convention:** every note carries `visibility: gm | player` (the machine-filterable source of truth for player-safe export), and fully-secret material also lives under GM-only sections/folders (`11 - Secrets`, most of `00 - Core`, `12 - Campaigns`). Mixed notes stay `player` with a walled-off `## GM Notes` section. Public notes list the secrets they'd expose via `reveals: []`, keyed to each secret's `reveal_tag`. Set `visibility` on every note from birth.

## Working in the vault

Use the project-scoped **`/obsidian` (obsidian-vault) skill** for finding, creating, and organizing notes. It defines the conventions in detail. Key points:

- **Structured folders** by note kind (not a flat layout).
- Every note starts with **YAML front-matter** — keep metadata keys consistent across notes of the same kind so search/discovery works.
- **Title Case** filenames; connect notes with Obsidian `[[wikilinks]]`; use index / map-of-content (MOC) notes to aggregate topics.

## Creative craft skills (worldbuilding & fiction)

A suite of fiction/worldbuilding skills is installed (from `jwynia/agent-skills`). **Use them** — don't hand-wave a design task you have a purpose-built skill for. They form a linked system: **`story-sense` is the router** — when something feels broken, thin, or stuck, invoke it first to diagnose *which* problem this is, then it points to the specific skill. Don't guess; diagnose, then reach for the named tool.

**Adaptations to note:**
- **`shared-world`** — adopt its *philosophy* (canon-status tracking: Established / Proposed / Contradicted; a running conflicts log; "the bible grows with the story, stay lean"), but **ignore its file scaffolding and Deno scripts** — this vault (`00–14` folders, `visibility`/`note_status`/`reveals` front-matter, templates, MOCs in `00 - Core/Meta/`) is already a stronger, spoiler-aware world bible. Track canon status and contradictions *inside* the existing notes (e.g. `11 - Secrets/Contradictions`, `note_status`), not in a parallel `world-bible/` tree.
- **`metabolic-cultures`** — built for closed-loop *space habitats*. Only reach for it if the setting has sealed/closed-system cultures; otherwise skip.
- **`memetic-depth`** — a few habits stay unexplained. Write what people do, and that they will not say why. The heel of the loaf at Ndenjoo is the named example, and the same refusal covers every other habit the notes already leave unexplained. Do not invent a cause. Do not turn the habit into a power, relic, or rite. Do not put "inscrutable," "leave it," or "20%" in a setting note, and do not write riddles. The rule is **Plain prose** in `00 - Core/Meta/Conventions.md`. `oblique-worldbuilding` is for an in-world page (a library handout, a poem, a minute-book, a play) in that speaker's voice. The note around the page still says what the page is. It is not the voice of a reference note.
- **Setting notes use connected paragraphs.** A setting note reads like a person explaining a place in a Daggerheart or D&D setting book. One sentence arrives at the next. Read it aloud. If it comes out as a list with periods, rewrite it. The same standard covers an answer to a question about the world. If a sentence already sounds like a person, keep it and fold any missing explanation into it. Do not chop prose that already breathes. Keep the Tengu overview, "lean, sharp-featured people with dark feathers through their hair and down their arms." "Tengu are a people, born that way" and "One Phoenix is alive in the world at a time. The wings are living fire. The moment they fly, anyone watching knows what they are." are too short and assembled. Explain a term the first time a new reader needs it, in the sentence that uses it, using a fact the note is allowed to say. Do not add canon to make the gloss. A picture, a nickname, or a metaphor may not hide a fact. "The circle drinks that winter back" and "the Unspent stays a cupboard" are failures of hiding, not a demand to write the shortest possible sentence. A Long-Lived gives one year of memory into a cup at a time, and later the others can read those memories from it. The Unspent stores the memories it is given, lets the circle describe it however they like, and does not make plans. Unexplained habits stay unexplained, as in the `memetic-depth` note above. In-world pages stay in the speaker's voice. GM truth stays in GM Notes and in `11 - Secrets`. Player-facing text does not pick up what is under GM Notes. Facts, numbers, secrets, and front-matter stay. Do not invent canon. The Turning Tree chapter is no longer the baseline for short sentences. Do not put that short voice back. Roadmap tasks and checklists stay short because they are a tracker, not setting notes. Do not rewrite the Roadmap into chapters, and do not use the Roadmap's shortness as a reason to chop a setting note. The full rule is **Plain prose** in `00 - Core/Meta/Conventions.md`.

**By job:**
- *Diagnosis & routing:* `story-sense` (invoke first when something feels off).
- *World generators:* `systemic-worldbuilding` (trace consequences of any new element), `belief-systems`, `economic-systems`, `governance-systems`, `settlement-design` (cities/regions), `conlang` + `language-evolution` (keep tongues phonologically consistent and historically layered).
- *Depth & texture:* `memetic-depth` (unexplained habits stay unexplained; do not invent a cause — see Conventions, Plain prose), `oblique-worldbuilding` (in-world pages only, in the speaker's voice; the note around the page still says what the page is), `cliche-transcendence` (fresh angles on stock tropes — familiar surface, uncanny underneath), `paradox-fables` (unresolved-wisdom folklore), `world-fates` (impermanent powers + accumulating consequences across a long campaign).
- *Character & story:* `character-arc`, `character-naming` (use its entropy approach — don't let names cluster), `positional-revelation` (ordinary-job characters who become structural pivots), `perspectival-constellation` (interlocking POVs), `underdog-unit` (David-vs-Goliath / institutional-outcast), `moral-parallax` (harm-exporting systems, complicity without clean villains), `key-moments` (build around emotional beats — wonder, mystery, etc.), `endings` (stick the finale).
- *Table voice:* `joke-engineering` (sparingly, with `dialogue`), `dialogue` (session/gameplay writing), `table-tone` (GM narration calibration).
- *Sentences:* `prose-style` (when the facts are in and the sentences still do not sound like a person explaining a place). Diagnose first. Write connected setting-book paragraphs. Explain a term the first time a new reader needs it, in the sentence that uses it, using a fact the note is allowed to say. Do not add canon to make the gloss. Do not chop prose that already breathes, and do not replace a fact with a picture. The Turning Tree chapter is no longer the baseline for short sentences. **Plain prose** in Conventions is the rule.
- *Audit:* `voice-analysis` (find where a setting note no longer sounds like a person explaining a place, per Plain prose in Conventions), `blind-spot-detective` (find what is missing; built for non-fiction, which a reference note is), `revision` (order a large edit pass so fixes do not cascade). Use them with `story-sense` for a whole-vault review. Added 2026-10-22 for Epic V.

**Scripts caveat:** several skills ship Deno `.ts` helpers. They're optional — the frameworks work without running them, and Deno may not be installed. Prefer applying the method directly.

## Daggerheart SRD reference

Read the online SRD when rules or system details are needed:

- Classes: https://daggerheartsrd.com/classes/
- Heritage (ancestries & communities): https://daggerheartsrd.com/heritage/
- Abilities (by domain): https://daggerheartsrd.com/abilities/
- Equipment: https://daggerheartsrd.com/equipment/
- Rules (comprehensive, important): https://daggerheartsrd.com/rules/
- GM content (frames, environments, adversaries): https://daggerheartsrd.com/gm/
