---
title: Atlas Prototype Review
type: asset
visibility: gm
note_status: draft
status: active
tags: [asset, map, atlas, prototype, production]
aliases: [Atlas Prototypes, Prototype Maps]
world: The Turning
reveals: []
created: 2026-08-31
updated: 2026-08-31
---

# Atlas Prototype Review

> **Production comparison, not canon.** These three sets use the supplied world map as their coastline and layout reference, then apply the established geography from [[The World Frame]], [[Named Ground]], and the four continent notes. If an image disagrees with a vault note, the note wins.

## Reference contract

![[references/World-Map-Reference.png]]

- North is up. The principal layout remains **Kumbaan upper-left · Heskoren lower-left · Strandoren centre-right · Maiethorn far-right**.
- Each continent sheet enlarges the corresponding silhouette from this reference without rotating or mirroring it.
- The detached storm-ringed speck southwest of Heskoren in the supplied painting is **not carried forward**. The setting has four landmasses, and Kumbaan is the upper-left storm-walled isle. Treat that speck as source-art interpolation, not a fifth land.
- Atlas sheets remain label-free. Add only names already established on [[Named Ground]] and [[The Known Map]].

## Prototype 1 — reference-faithful dark portolan

Closest to the supplied painting's palette, border, sea treatment, and terrain density.

![[prototype1/The-Turning-World-Atlas.png]]

| Kumbaan | Heskoren |
|---|---|
| ![[prototype1/Kumbaan-Atlas.png]] | ![[prototype1/Heskoren-Atlas.png]] |

| Strandoren | Maiethorn |
|---|---|
| ![[prototype1/Strandoren-Atlas.png]] | ![[prototype1/Maiethorn-Atlas.png]] |

## Prototype 2 — pale engraved survey

The cleanest option for later annotation: pale vellum, fine hachures, restrained washes, and clearer hydrology.

![[prototype2/The-Turning-World-Atlas.png]]

| Kumbaan | Heskoren |
|---|---|
| ![[prototype2/Kumbaan-Atlas.png]] | ![[prototype2/Heskoren-Atlas.png]] |

| Strandoren | Maiethorn |
|---|---|
| ![[prototype2/Strandoren-Atlas.png]] | ![[prototype2/Maiethorn-Atlas.png]] |

## Prototype 3 — weather-forward campaign atlas

The most atmospheric option: stronger sea states, rain, forest mass, and the wet/dry divide across Maiethorn.

**Consistency rule:** the four continent sheets are the masters. The world sheet is a deterministic composite of those exact painted landforms, not a separate generation. Coastlines, mountain chains, forests, rivers, and other visible features therefore match at both scales. `Painted-Ocean-Background.png` supplies one continuous portolan sea, current texture, frame, and compass beneath the masters; it is a build plate, not a separate handout. Rebuild with `build_prototype3_world.py` after replacing any continent master.

![[prototype3/The-Turning-World-Atlas.png]]

| Kumbaan | Heskoren |
|---|---|
| ![[prototype3/Kumbaan-Atlas.png]] | ![[prototype3/Heskoren-Atlas.png]] |

| Strandoren | Maiethorn |
|---|---|
| ![[prototype3/Strandoren-Atlas.png]] | ![[prototype3/Maiethorn-Atlas.png]] |

## Canon checks applied

- **Kumbaan:** one small island; complete storm/current/reef wall; rolling wet hill-country; no city, no quay, no graft, no hidden Tree, and no permanent safe channel.
- **Heskoren:** rugged highlands distinct from Maiethorn's Rain-Wall; cooler moor and forest; sparse settlement pockets around surviving grafts; no capital star.
- **Strandoren:** coast-dominant and deeply indented; wet lowlands; the Chart-run crosses toward the large eastern estuary; the eastern sea is busier than the western water.
- **Maiethorn:** Rain-Wall north–south; wet, old, densely settled west; one exceptional canopy in the Motherwood; Core-thaw running west; dry Rain-Shadow and seasonal water east.
- No political borders, Kind-nations, new powers, dated Tree, or First Seat capital were added.

## Visual interpolation register

The generator necessarily supplied small-scale details that the setting has not named:

- minor river branches and tiny coastal rocks;
- exact road curves, field boundaries, coves, reef breaks, and mountain notches;
- unnamed roof clusters, harbour marks, standing stones, and grove dots;
- the precise shape and location of forest patches outside established regions.

These are **non-canon visual texture**, not proposals and not a queue of places that now require lore. Do not write them into the setting merely because they appear in a prototype. If a later map choice promotes one of them into play, first name and reconcile it in the vault, then annotate the selected sheet.

## Selection notes

- Choose **Prototype 1** if continuity with the supplied world painting matters most.
- Choose **Prototype 2** if the next step is hand-labeling or overpainting.
- Choose **Prototype 3** if exact world-to-continent continuity, table mood, and climate readability matter most.
- Mixing a world sheet from one prototype with continent sheets from another weakens the visual set, but does not change canon.

## Links

- [[The Atlas Sheets]] — existing atlas set
- [[Map Generation Tooling]] — prompt and annotation guidance
- [[The Known Map]] — labelled schematic
- [[Maiethorn]] · [[Strandoren]] · [[Heskoren]] · [[The Sundering Isle]]
- [[Climate of Maiethorn]] · [[Climate of Strandoren]] · [[Climate of Heskoren]] · [[Climate of Kumbaan]]
