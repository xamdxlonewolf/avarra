---
name: obsidian-vault
description: Search, create, and manage notes in the Avarra Obsidian vault with structured folders, front-matter metadata, and wikilinks. Use when the user wants to find, create, or organize worldbuilding notes for Avarra.
---

# Avarra Obsidian Vault

This repository **is** the Obsidian vault for Avarra. All notes are highly detailed Markdown files organized in a structured folder system, each with detailed YAML front-matter that drives metadata-based search and discovery.

## Vault location

`/Users/mcobb/Documents/Personal/avarra` (this repository)

## Organization

**The schema is authoritative in `00 - Core/Meta/Conventions.md` — read it before creating notes.** Summary:

- **Numbered top-level folders** (`00 - Core` … `14 - Assets`, `99 - Archive`) on a four-layer model: **World** = what exists (01–10), **Campaign** = what happened (12), **Secrets** = what the GM knows (11), **Canon** = what is actually true (00). One canonical home folder per entity; other sections link, never duplicate.
- Every note begins with **YAML front-matter**. Base keys on *every* note: `title`, `type`, `visibility` (`player|gm`), `note_status` (`stub|draft|fleshed|canon`), `tags`, `aliases`, `created`, `updated`. Common optional: `status` (in-world state), `world` (`avarra|green-reach|kiln`), `reveals: []`. Plus kind-specific keys — copy the matching template from `00 - Core/Meta/Templates/`.
- `note_status` = how complete the note is; `status` = the thing's state in the fiction. Never conflate them.
- **`visibility` drives player-safe export** — set it on every note from birth; keep spoilers in `## GM Notes` sections or `11 - Secrets`.
- Use **Title Case** for note filenames.

## Linking

- Use Obsidian `[[wikilinks]]` to connect related notes: `[[Note Title]]`.
- Link related notes inline where relevant and/or at the bottom of a note.
- Use index/MOC (map-of-content) notes to aggregate related topics.

## Workflows

### Search for notes

Use the Grep/Glob tools directly on the vault path, or search front-matter fields to find notes by metadata (e.g. all notes with `type: character` or a given `tag`).

### Create a new note

1. Choose the correct folder for the note's kind.
2. Add complete YAML front-matter at the top.
3. Write detailed content.
4. Add `[[wikilinks]]` to related notes.

### Find backlinks

Search for `[[Note Title]]` across the vault to find notes that reference it.

## Daggerheart system reference (SRD)

Avarra uses **Daggerheart**. Read the online SRD when you need rules/system details:

- **Classes**: https://daggerheartsrd.com/classes/ (e.g. `/classes/bard/`, `/classes/wizard/`, …)
- **Heritage** (ancestries & communities): https://daggerheartsrd.com/heritage/ — `/ancestries/`, `/communities/`
- **Abilities** (by domain): https://daggerheartsrd.com/abilities/ — arcana, blade, bone, codex, grace, midnight, sage, splendor, valor
- **Equipment**: https://daggerheartsrd.com/equipment/ — weapons, armor, items, consumables
- **Rules** (important, comprehensive): https://daggerheartsrd.com/rules/
- **GM content** (frames, environments, adversaries): https://daggerheartsrd.com/gm/
