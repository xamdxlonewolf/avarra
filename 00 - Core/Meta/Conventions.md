---
title: Vault Conventions
type: reference
visibility: gm
note_status: draft
tags: [meta, conventions, schema]
aliases: [Schema, Front-matter Reference]
created: 2026-08-11
updated: 2026-08-31
---

# Vault Conventions

How this vault is organized and how every note is tagged. This is the contract all notes obey so metadata-driven search, discovery, and player-safe export work.

## The four-layer model

- **World = what exists.** The persistent setting (sections 01–10). The source of truth.
- **Campaign = what happened.** What the players did to the world (12 - Campaigns), kept separate so player actions never force a rewrite of the setting.
- **Secrets = what the GM knows.** The revelation architecture (11 - Secrets) + GM sections of otherwise-public notes.
- **Canon = what is actually true.** The settled truth (00 - Core/Canon, Cosmology), regardless of what any in-world source believes.

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
09 - Creatures    Beasts · Monsters · Spirits · Constructs · Unique · Conditions
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
world:        # optional — which world/realm a thing belongs to, if the setting has more than one
reveals: []   # secret reveal_tags this note exposes, e.g. [the-big-secret]
```

> **`note_status` vs `status`:** `note_status` = editorial completeness of the file. `status` = the thing's state inside the fiction. They never overlap.

> **`note_status` vocabulary (finished-state convention, Story R.13).** Only these four values are legal:
> - **`stub`** — placeholder or empty index.
> - **`draft`** — in progress; do not treat the body as settled.
> - **`fleshed`** — complete enough to play or cite; still polishable.
> - **`canon`** — finished and load-bearing. The note is the settled reference. Later edits are corrections, not redesign.
>
> **`locked` is retired.** It was never in this list. An earlier pass used it on fifteen finished design notes (ten Condition cards, four custom Kinds, the keystone). Those notes are now `canon`. The Editorial Audit counted nineteen; the vault held fifteen when this story ran. Roadmap 🔒 / 🟡 / ⚠️ remains a *decision-settlement* tag on the tracker, not a front-matter value.

> **`visibility`:** `gm` = never shown to players. `player` = safe to hand out. Mixed notes stay `player` but keep secrets in a `## GM Notes` section (stripped on export — see [Player-safe export](#Player-safe%20export)). Fully-secret notes live in `11 - Secrets` or under a `gm` MOC.
>
> **Condition cards and the Conditions hub are `player`.** Usable mechanics must survive export. Design history, household names, the one-Gift harvest, and Protector methods stay in `## GM Notes` or in `11 - Secrets`. A card's `reveals` is empty unless the *player body* would confirm a secret.

> **`reveals`:** the machine-filterable link between public notes and the secrets they'd spoil. Lets you later query "what is safe to hand out by session 20" by excluding notes that reveal not-yet-revealed `reveal_tag`s. Every secret note declares a `reveal_tag`; public notes list the tags they touch in `reveals: []`.

> **Reveal-tag vocabulary (Story R.5).** `leaf-mother-is-real` = this note's player *body* would confirm the Leaf-Mother, or it is the keystone's own `reveal_tag`. `keystone-adjacent` = clue, doctrine, Tree, or reach-pattern without confirmation — use this so clue-bearing notes can be found without treating the vault as one spoiler. `the-other-hands` = the note exposes the household (usually in `## GM Notes`). `the-unspent` = the lesser household presence the Long-Lived fringe named. `when-the-fire-is-caught` = the Phoenix slot. Index and examples: [[11 - Secrets]].

### `type` vocabulary
`moc`, `reference`, `lore`, `cosmology`, `theme`,
`region`, `settlement`, `city`, `town`, `village`, `site`,
`people`, `language`, `custom`, `tradition`,
`faction`,
`era`, `event`, `timeline`,
`npc`, `pc`, `character`,
`deity`, `faith`, `myth`, `ritual`,
`creature`, `adversary`, `condition`,
`item`, `magic`,
`secret`, `mystery`, `clue`, `revelation`,
`campaign`, `arc`, `chapter`, `session`, `thread`,
`system`, `rule`, `encounter`, `table`,
`asset`, `map`, `handout`.

Templates for the common kinds live in `00 - Core/Meta/Templates/`.

## Player-safe export

This is the strip rule. A heading-based filter that does not follow it will leak. Implement it in this order; do not invent a parallel rule.

### 1. Omit whole notes

Drop every note whose front-matter `visibility` is `gm`. `visibility` is the source of truth — do not add folder-level exceptions. `11 - Secrets` is already `gm`. Mixed notes stay `player` and are handled in step 2.

### 2. Strip GM sections from remaining notes

On each `visibility: player` note, remove every ATX heading (`#` through `######`) whose heading text is exactly `GM Notes` or begins with `GM Notes` (so `GM Notes (the reality)` counts).

The stripped span runs from that heading through **the next heading of equal or higher rank**, or through end of file if none follows. Nested headings of lower rank go with the section. A blockquote, list, or table that sits inside that span is already gone.

Usual vault shape is `## GM Notes` near the end. If `## Links` follows it, Links survive (same rank). If Links sit *inside* the GM section, they go with it. Prefer Links before or after the wall, not under it.

### 3. Strip unmarked GM blockquotes

After the heading pass, remove any remaining blockquote whose first significant line (after `>` and optional space) begins with `GM —`, `GM:`, or `GM Notes`. This is the leak class a heading-strip cannot catch — a "GM — why this matters" callout sitting in the player body.

Do **not** strip ordinary player-body blockquotes, in-world documents, or epigraphs.

### 4. Strip HTML comments

Remove `<!-- ... -->` (including multiline). They are production notes, not player text.

### 5. Optional campaign filter (after the strip)

If a campaign is tracking unrevealed `reveal_tag`s, you may then omit notes whose `reveals` list contains a tag not yet revealed **and** whose remaining body would spoil that tag. Do **not** use this filter to hide [[Conditions]] or [[Kind Heritage]]: those player bodies are mechanics. Confirmation that would spoil lives behind the wall (already stripped) or in a `visibility: gm` note (already omitted).

### 6. Front-matter on a handout

Keep `title`, `type`, and `aliases`. Drop `visibility`, `reveals`, `note_status`, and other production keys.

### What this rule does not do

It does not rewrite voice. It does not remove `🔒` / `🟡` from the Roadmap. It does not treat a player-body "Not *Saelorn* (a month)" disambiguation as a GM note. Production scaffolding (seeds, story numbers, "do not clone") belongs under `## GM Notes` so this rule removes it.

## Linking & naming

- **Title Case** filenames.
- Connect notes with `[[wikilinks]]`; link inline and/or in a `## Links` section.
- Use MOC / index notes to aggregate topics; find backlinks by searching `[[Note Title]]`.

## Related
- [[00 - Core]] — section index
- [[At the Table]] — session procedures
- [[Dangers of the Turning]] — wilderness adversaries
- [[A Hidden Phoenix]] — Phoenix PC agency
- [[11 - Secrets]] — reveal-tag index
