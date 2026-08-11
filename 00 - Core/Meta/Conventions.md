---
title: Vault Conventions
type: reference
visibility: gm
note_status: draft
tags: [meta, conventions, schema]
aliases: [Schema, Front-matter Reference]
created: 2026-08-11
updated: 2026-08-11
---

# Vault Conventions

How the Avarra vault is organized and how every note is tagged. This is the contract all notes obey so metadata-driven search, discovery, and player-safe export work.

## The four-layer model

- **World = what exists.** The persistent setting (sections 01–10). The source of truth.
- **Campaign = what happened.** What the players did to the world (12 – Campaigns), kept separate so player actions never force a rewrite of the setting.
- **Secrets = what the GM knows.** The revelation architecture (11 – Secrets) + GM sections of otherwise-public notes.
- **Canon = what is actually true.** The settled truth (00 – Core/Canon, Cosmology), regardless of what any in-world source believes.

## Folder tree

Top-level folders use **numeric prefixes** to force reading order in the sidebar. Each has an index MOC named after it.

```
00 - Core         Canon · Cosmology · Themes · Meta
01 - World        Geography · Climate · Ecology · Astronomy · Planes · Phenomena
02 - History      Eras · Events · Timelines · Historical Figures · Archaeology
03 - Cultures     Peoples · Languages · Customs · Traditions · Social Structures · Naming
04 - Settlements  Continents · Regions · Cities · Towns · Villages · Sites
05 - Factions     Governments · Organizations · Guilds · Religious Orders · Military · Criminal
06 - Magic        Systems · Traditions · Schools · Practices · Artifacts · Phenomena
07 - Religion     Deities · Faiths · Mythology · Rituals · Religious History
08 - People       NPCs · Historical Figures · Leaders · Heroes · Villains
09 - Creatures    Beasts · Monsters · Spirits · Constructs · Unique
10 - Items        Weapons · Armor · Equipment · Artifacts · Materials
11 - Secrets      Mysteries · Revelations · Clues · Contradictions · GM Truth   (GM ONLY)
12 - Campaigns    <Campaign>/ Arcs · Chapters · Sessions · Player Characters · Campaign NPCs
13 - Game         Rules · Mechanics · Encounters · Tables · Daggerheart
14 - Assets       Maps · Images · Handouts · Documents · References
99 - Archive      retired / superseded notes
```

## One canonical home per entity

Every entity lives in **exactly one** folder. Overlapping sections **link**, they do not duplicate.

- A person → `08 - People` (campaign-spawned NPCs → `12 - Campaigns/<Campaign>/Campaign NPCs`).
- An item/artifact → `10 - Items` (Magic links to it).
- A historical figure → `08 - People/Historical Figures` (History links to them).
- MOCs and section indexes aggregate by linking only.

## Front-matter schema

### Base keys — on every note
```yaml
title:        # Title Case display name
type:         # note kind (see list below)
visibility:   # player | gm          — drives player-safe export
note_status:  # stub | draft | fleshed | canon   — how complete the NOTE is
tags: []
aliases: []
created:      # YYYY-MM-DD
updated:      # YYYY-MM-DD
```

### Common optional keys
```yaml
status:       # IN-WORLD state (alive | dead | ruined | active | forgotten | ...)
world:        # avarra | green-reach | kiln   — which half a thing belongs to
reveals: []   # secret reveal_tags this note exposes, e.g. [kiln-is-alive, avarra-meaning]
```

> **`note_status` vs `status`:** `note_status` = editorial completeness of the file. `status` = the thing's state inside the fiction. They never overlap.

> **`visibility`:** `gm` = never shown to players. `player` = safe to hand out. Mixed notes stay `player` but keep secrets in a `## GM Notes` section (stripped on export). Fully-secret notes live in `11 - Secrets` or under a `gm` MOC.

> **`reveals`:** the machine-filterable link between public notes and the secrets they'd spoil. Lets you later query "what is safe to hand out by session 20" by excluding notes that reveal not-yet-revealed `reveal_tag`s. Every secret note declares a `reveal_tag`; public notes list the tags they touch in `reveals: []`.

### `type` vocabulary
`moc`, `reference`, `lore`, `cosmology`, `theme`,
`region`, `settlement`, `city`, `town`, `village`, `site`,
`people`, `language`, `custom`, `tradition`,
`faction`,
`era`, `event`, `timeline`,
`npc`, `pc`, `character`,
`deity`, `faith`, `myth`, `ritual`,
`creature`, `adversary`,
`item`, `magic`,
`secret`, `mystery`, `clue`, `revelation`,
`campaign`, `arc`, `chapter`, `session`, `thread`,
`system`, `rule`, `encounter`, `table`,
`asset`, `map`, `handout`.

Templates for the common kinds live in `00 - Core/Meta/Templates/`.

## Linking & naming

- **Title Case** filenames.
- Connect notes with `[[wikilinks]]`; link inline and/or in a `## Links` section.
- Use MOC / index notes to aggregate topics; find backlinks by searching `[[Note Title]]`.

## Working names (pending naming pass)

*Green Reach*, *the Kiln*, and *the Wardens* are placeholders. The `world:` values `green-reach` / `kiln` are stable machine keys even after display names change.

## Related
- [[00 – Core]]
- [[Cosmology]] (see `00 - Core/Cosmology`)
- [[11 – Secrets]]
