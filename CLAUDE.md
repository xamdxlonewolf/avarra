# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **worldbuilding repository** and serves as an **Obsidian vault** for a tabletop RPG setting. There is no application code, build system, or tests — content is detailed Markdown notes organized in a structured folder system, each with YAML front-matter that drives metadata-based search and discovery.

The tabletop system is **Daggerheart**.

## What the setting is

> **"The Empire That Wasn't Evil."** An enormous, centuries-old empire that is *genuinely good at governing* — safe roads, fair courts, low crime, protected trade, preserved cultures, no slavery, a citizenry that genuinely likes it. And yet there is a rebellion whose members are *not obviously wrong.* The campaign is the slow discovery of **why anyone would destroy a government that works** — and the players cannot resolve it by picking the good guys, because there are none. They decide what kind of world they actually want.

**The design contract (load-bearing — do not violate):** *both the Empire's defenders and the rebels must stay right for the entire campaign.* The test for any secret/faction/reveal: *could a thoughtful, decent person, knowing the full truth, still choose to keep it running?* If the answer becomes "no," the story has collapsed into Evil Empire / Plucky Rebels — the cliché this premise exists to transcend. This is a **`moral-parallax`** build.

**The players** are a **mixed commission of inquiry / circuit court** in imperial service — a *job*, not an imposed identity: who each character is and whether they love or despise the Empire is player-authored. They personally dispense the Empire's justice (complicity built in), which makes each province a self-contained, table-ready case that also seeds the iceberg.

**Authoring rule:** teach through *"something is weird,"* never an encyclopedia dump. Comfort/competence first (a world worth loving) → uncanny when the seam shows → grimdark spikes at the pressure points. The peace is real; the cost is real; everyone is grateful.

The canonical write-ups live in the vault — start there, they are the source of truth:
- **`00 - Core/Concept/The Premise.md`** — full overview, vantage, design contract, build roadmap *(GM)*
- **`00 - Core/Themes/Themes.md`** — the moral-parallax spine *(GM)*
- **`11 - Secrets/GM Truth/The Cost.md`** — the core secret: why the Empire works *(GM · spoiler)*

> **GM-secret spoiler wall:** the truth of *why the Empire works* is a fused secret — a small ongoing sacrifice of people that *also* holds a returning catastrophe at bay, where no one alive can confirm the threat is still real. Never surface it as exposition; it is revealed only through the iceberg. Details in `The Cost` (`visibility: gm`).

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
