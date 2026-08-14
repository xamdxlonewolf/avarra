# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **worldbuilding repository** and serves as an **Obsidian vault** for a tabletop RPG setting. There is no application code, build system, or tests — content is detailed Markdown notes organized in a structured folder system, each with YAML front-matter that drives metadata-based search and discovery.

The tabletop system is **Daggerheart**.

## What the setting is

> **No setting is currently defined.** The vault was reset to its bare framework on 2026-08-14 — the previous setting ("The Empire That Wasn't Evil," and its after-world pivot) was scrapped and lives only in git history. The folder structure, conventions, templates, and craft-skill suite are intact and ready for a fresh setting.

When a new setting is established, record its canonical write-ups in the vault (the source of truth) and summarize the essentials here — the premise, the design spine/contract, the players' vantage, the authoring rule, and pointers to the key notes (typically under `00 - Core/Concept`, `00 - Core/Themes`, and any GM secret under `11 - Secrets`).

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

**Two adaptations to note:**
- **`shared-world`** — adopt its *philosophy* (canon-status tracking: Established / Proposed / Contradicted; a running conflicts log; "the bible grows with the story, stay lean"), but **ignore its file scaffolding and Deno scripts** — this vault (`00–14` folders, `visibility`/`note_status`/`reveals` front-matter, templates, MOCs in `00 - Core/Meta/`) is already a stronger, spoiler-aware world bible. Track canon status and contradictions *inside* the existing notes (e.g. `11 - Secrets/Contradictions`, `note_status`), not in a parallel `world-bible/` tree.
- **`metabolic-cultures`** — built for closed-loop *space habitats*. Only reach for it if the setting has sealed/closed-system cultures; otherwise skip.

**By job:**
- *Diagnosis & routing:* `story-sense` (invoke first when something feels off).
- *World generators:* `systemic-worldbuilding` (trace consequences of any new element), `belief-systems`, `economic-systems`, `governance-systems`, `settlement-design` (cities/regions), `conlang` + `language-evolution` (keep tongues phonologically consistent and historically layered).
- *Depth & texture:* `memetic-depth` (implied depth via the 40/40/20 recognizable/inferrable/inscrutable ratio — teach through "something is weird," not exposition), `oblique-worldbuilding` (in-world epigraphs/documents whose blindness seeds reveals), `cliche-transcendence` (fresh angles on stock tropes — familiar surface, uncanny underneath), `paradox-fables` (unresolved-wisdom folklore), `world-fates` (impermanent powers + accumulating consequences across a long campaign).
- *Character & story:* `character-arc`, `character-naming` (use its entropy approach — don't let names cluster), `positional-revelation` (ordinary-job characters who become structural pivots), `perspectival-constellation` (interlocking POVs), `underdog-unit` (David-vs-Goliath / institutional-outcast), `moral-parallax` (harm-exporting systems, complicity without clean villains), `key-moments` (build around emotional beats — wonder, mystery, etc.), `endings` (stick the finale).
- *Table voice:* `joke-engineering` (sparingly, with `dialogue`), `dialogue` (session/gameplay writing), `table-tone` (GM narration calibration).

**Scripts caveat:** several skills ship Deno `.ts` helpers. They're optional — the frameworks work without running them, and Deno may not be installed. Prefer applying the method directly.

## Daggerheart SRD reference

Read the online SRD when rules or system details are needed:

- Classes: https://daggerheartsrd.com/classes/
- Heritage (ancestries & communities): https://daggerheartsrd.com/heritage/
- Abilities (by domain): https://daggerheartsrd.com/abilities/
- Equipment: https://daggerheartsrd.com/equipment/
- Rules (comprehensive, important): https://daggerheartsrd.com/rules/
- GM content (frames, environments, adversaries): https://daggerheartsrd.com/gm/
