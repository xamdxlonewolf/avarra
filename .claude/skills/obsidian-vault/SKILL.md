---
name: obsidian-vault
description: Search, create, and manage notes in the Avarra Obsidian vault with structured folders, front-matter metadata, and wikilinks. Use when the user wants to find, create, or organize worldbuilding notes for Avarra.
---

# Avarra Obsidian Vault

This repository **is** the Obsidian vault for Avarra. All notes are highly detailed Markdown files organized in a structured folder system, each with detailed YAML front-matter that drives metadata-based search and discovery.

## Vault location

`/Users/mcobb/Documents/Personal/avarra` (this repository)

## Organization

- **Structured folders**, not a flat layout — group notes by kind (e.g. lore, locations, characters, factions, sessions, and Daggerheart system reference).
- Every note begins with **YAML front-matter** for metadata-driven search and discovery. Prefer consistent keys across notes of the same kind (e.g. `title`, `type`, `tags`, `status`, `aliases`, plus kind-specific fields like `region`, `faction`, `class`, `domain`).
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
