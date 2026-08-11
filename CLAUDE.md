# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Avarra is a **worldbuilding repository** and serves as the **Obsidian vault** for the Avarra setting. There is no application code, build system, or tests — content is highly detailed Markdown notes organized in a structured folder system, each with detailed YAML front-matter that drives metadata-based search and discovery.

The tabletop system for Avarra is **Daggerheart**.

## What Avarra is (the setting)

> **Working names.** *Green Reach*, *the Kiln*, and *the Wardens* are placeholders pending a deliberate naming pass. Treat them as find-and-replaceable.

**The thematic spine:** *Every civilization thinks it is living in the real world. There is no "real" world — only people afraid of losing their home. Can two civilizations share a reality that was never built to hold both of them?*

**The campaign shape:** a chaptered saga (4–6 seasons, ~120–150 sessions of ≤3 hours) built as an **iceberg** — small, familiar troubles that slowly recontextualize into something older and vaster. The player-facing surface is deliberately *comfortable* high fantasy so the reveals land as awe, not exposition. The campaign's arc, in four beats:

> "We are exploring the ruins of the past." → "The past is happening somewhere else." → "The past is us." → "We have been trying to become whole by destroying ourselves." → "What if we choose to recognize ourselves instead?"

**The familiar surface (player-facing):** a lush, ancient, deeply lived-in high-fantasy world — old-growth forests, river-cities, worn stone, an agrarian-scholarly culture obsessed with its own antiquity, its lineages, and the "ancient civilizations" it excavates and reveres. Mature high civilization at its height (the heartland), dotted with frontier/ruin pockets, and rimmed by scarce, walled-out "wastes" in the far north, far south, and dead islands. Magic is a bounded, respected craft — not infrastructure. Default tone is early-Elder-Scrolls / Zelda **wonder**, hardening to uncanny **mystery** when it matters, with **grimdark spikes** at the pressure points (so there is always something to lose).

**Authoring rule (critical):** teach the world through *"something is weird,"* never through an encyclopedia dump. Questions first; answers much later. Every reveal should feel inevitable in retrospect, not arbitrary. The next major work is the campaign's **revelation architecture** (what players know at sessions 1–10, 20, 40, 60, 80, 100+, and the specific clues that earn each turn) — not more lore.

<!-- ============================================================ -->
<!-- GM SECRET — CORE CANON. Do NOT include in any player handout. -->
<!-- ============================================================ -->

## GM SECRET — the true cosmology

**Spoiler wall.** Everything below is the hidden truth of the setting. It is `visibility: gm` canon. Never surface it to players directly; it is revealed only through the campaign's iceberg structure.

There was one reality. It **fractured** — not from a fall from paradise, but because it could not reconcile **two incompatible ways of existing**. The two halves are not parallel universes and neither is the "original":

- **The Green Reach** (our familiar side): organic, growing, mutable, imperfect, warm, materially abundant.
- **The Kiln** (the "negative"): structured, geometric, crystalline, ordered, stable, thermally transformed — a world of glass, ash, and standing light. Street-for-street the *same* places, vitrified. Beautiful and alien, not hellish.

They are **two solutions to the same existential problem**. Same souls, alien clothes.

- **The soul-pool never divided.** Souls belong to the underlying reality, not to either world, so the same souls recur on both sides — not as identical copies but as **diverged possibilities** (lovers on one side, enemies on the other; a child here, an elder there; sometimes no counterpart at all). These are *possibilities of the same reality.*
- **The alignments are reality trying to remember it was one** — attempting to reunify. Because the halves have developed independently for millennia, reunification is catastrophic: matter can't decide which version to obey, geographies and bodies and histories try to occupy the same state, reality chooses neither, and **breaks**. The wreckage becomes an archaeological layer.
- **The strata are the scars of failed reunifications.** The party believes they excavate a sequence of ancient *civilizations*; they eventually find the impossible — two civilizations in the *exact same chronological layer*, then another, then another — and realize the layers aren't `civ → civ → civ` but `world → world → world`. **The "ancients" aren't predecessors. They're previous collisions.** The players aren't digging up the past; they're digging up previous attempts to become whole.
- **The Wardens** are not secret villains and get **no redemption arc** — they are the most morally uncomfortable people the party meets. They discovered that **recognition accelerates reunification**: if enough people recognize the other half is *alive*, reality starts trying to reconcile. So their doctrine is *forget* — and their great lie is a single verb tense: the Kiln must remain **"there was** another civilization," never **"there is."** They have made horrible choices for generations because they have never had another option, and every prior cycle proved them right. (Their fingerprint on the world: investigative magic — divination, speaking to the dead, scrying the deep past — is culturally taboo, because it's the fast path to recognition.)
- **Why this cycle is different (the new factor):** for the first time in recorded history, **both halves become aware of each other simultaneously** — someone on the Kiln side discovers the truth at the same time the party does. Every prior cycle ran *discover → collide → destroy → forget → diverge.* This one can run *discover → recognize → **communicate**.* Mutual awareness is the anomaly — it's why the cycle is accelerating and why the Wardens' calculations are failing. **Do not give the players a clean cycle number.** Let them believe it's predictable, then watch it collapse: "73 years" → "61" → "19" → "there isn't a cycle anymore."
- **The real final question is not "can we stop the alignment?"** (that is the Wardens' failed thousand-year project). It is **"can reality become one without one half of itself dying?"** Every previous cycle failed because all parties shared the same false premise — that becoming whole means *choosing which half is real* (replacement). The players discover the third possibility: reality doesn't have to choose; the Green Reach doesn't have to become the Kiln, nor the Kiln the Green Reach — they can become **something neither has ever been.** This can manifest in the finale at the level of a single soul meeting its counterpart: the old cycle whispers *"absorb them and be whole"*; the new solution is *"you don't have to become me, and I don't have to become you."*
- **The climax is relational, not martial.** Catastrophe rages — glass growing through forests, forests through glass, cities overlapping, both civilizations mobilizing — but the win condition is to **make the other side see that there is a person on the other side.** The Wardens preserved the world by making people *forget*; the party saves both worlds by making them *remember each other.* The solution is **created by the players, not excavated from a ruin.**

**Never explained (deliberate cosmic mystery):** *why* reality originally split, and *why* reality wants to be whole at all. The players get a complete answer to "what is happening?", a sufficient answer to "why has it been happening?", but never to "why does reality itself want to be one?" This is *origin* left unknowable — not the central conflict.

<!-- ============================================================ -->
<!-- END GM SECRET                                                -->
<!-- ============================================================ -->

## GM-secret / spoiler convention (vault-wide)

Avarra content is split by audience so a player-safe handout version can be generated by filtering:

- **Front-matter flag on every note:** `visibility: gm` or `visibility: player`. This is the source of truth for filtering/querying in Obsidian, regardless of folder.
- **Folder separation:** spoiler/secret notes also live under a dedicated GM-only folder tree (for humans browsing the vault), while player-facing notes live in the normal structure.
- Belt-and-suspenders: the folder is for people, the front-matter flag is for machine filtering. When creating any note, set `visibility` from birth. (A finer spoiler/`reveals` scheme may be added when the front-matter schema is finalized.)

## Working in the vault

Use the project-scoped **`/obsidian` (obsidian-vault) skill** for finding, creating, and organizing notes. It defines the conventions in detail. Key points:

- **Structured folders** by note kind (not a flat layout).
- Every note starts with **YAML front-matter** — keep metadata keys consistent across notes of the same kind so search/discovery works.
- **Title Case** filenames; connect notes with Obsidian `[[wikilinks]]`; use index / map-of-content notes to aggregate topics.

## Daggerheart SRD reference

Read the online SRD when rules or system details are needed:

- Classes: https://daggerheartsrd.com/classes/
- Heritage (ancestries & communities): https://daggerheartsrd.com/heritage/
- Abilities (by domain): https://daggerheartsrd.com/abilities/
- Equipment: https://daggerheartsrd.com/equipment/
- Rules (comprehensive, important): https://daggerheartsrd.com/rules/
- GM content (frames, environments, adversaries): https://daggerheartsrd.com/gm/
