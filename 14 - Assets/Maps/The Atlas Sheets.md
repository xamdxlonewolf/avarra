---
title: The Atlas Sheets
type: map
visibility: gm
note_status: draft
status: active
tags: [asset, map, atlas, epic-r, story-r10]
aliases: [Atlas Gallery, Generated Maps, Continent Paintings]
world: The Turning
created: 2026-08-30
updated: 2026-09-01
---

# The Atlas Sheets

> **Label-free paintings, not surveys.** Generated from the pack in [[Map Generation Tooling]]. Names and travel: [[Named Ground]]. Placement: [[The Known Map]] (SVG). If a painting and a note disagree, the note wins.

> **Selected atlas (2026-09-01): Prototype 3.** The main world and continent filenames below are promoted copies of the matched Prototype 3 masters. The world sheet is composited from those exact landforms, so coastlines and physical features agree across scales.

> **Handouts.** These label-free sheets can go to the table. They are still paintings rather than surveys; [[The Known Map]] and [[Named Ground]] remain authoritative for names and placement. Prototypes 1 and 2 remain available in [[Atlas Prototype Review]] as rejected alternatives, not parallel canon.

> **Canon boundary.** Coastline, watershed, named hydrology, settlement relationships, scale, and orientation follow the notes and selected masters. Minor tributaries, exact road bends, roof clusters, field edges, forest texture, coastal rocks, and decorative weather supplied by generation are **non-canon incidental texture**.

| Regions | Prototype 3 parent |
|---|---|
| Old Crossing | Strandoren + Maiethorn |
| Sacred Core · Rain-Wall · Rain-Shadow | Maiethorn |
| Chart-run · West Water | Strandoren |
| Live Front · Waiting Vale | Heskoren |

## Selected continents

### Maiethorn (C1)

![[Maiethorn-Atlas.png]]

### Strandoren (C2)

![[Strandoren-Atlas.png]]

### Heskoren (C3)

![[Heskoren-Atlas.png]]

Labeled trial (2026-09-01). Overlay on this master, not a new survey. Rebuild with `label_heskoren_atlas.py`.

![[Heskoren-Atlas-Labeled.png]]

### Kumbaan (C4)

No graft. No city. The wall is the climate.

![[Kumbaan-Atlas.png]]

## Regions

### R1 — the Old Crossing

![[Old-Crossing-Atlas.png]]

### R2 — Sacred Core / Motherwood

![[Sacred-Core-Atlas.png]]

### R3 — the Rain-Wall

![[Rain-Wall-Atlas.png]]

### R4 — Rain-Shadow

![[Rain-Shadow-Atlas.png]]

### R5 — Chart-run / Salt Quay hinterland

![[Chart-Run-Atlas.png]]

### R6 — Night Shore / West Water

![[West-Water-Atlas.png]]

### R7 — live front (Harrow's and the ford)

![[Live-Front-Atlas.png]]

### R8 — waiting vale

![[Waiting-Vale-Atlas.png]]

## Selected world atlas

![[The-Turning-World-Atlas.png]]

## Regional rebuild review — 2026-09-01

- All eight sheets use the dark, weather-forward Prototype 3 portolan hand and bronze frame.
- **Sacred Core and Rain-Wall** are distinct generated region paintings inspired by Maiethorn. Sacred Core is the inland Motherwood with Thaeloren as the sole exceptional Tree. Rain-Wall is the highland divide: offset massifs, saddles, foothills, river notches, pass gaps, wet west and dry east, and no exceptional Tree.
- **Chart-run and West Water** are distinct generated region paintings inspired by Strandoren, not two crops of the same continent sheet. Chart-run is the interior river-plain running east into the Salt Quay estuary. West Water is the sparse open-ocean Night Shore face.
- Old Crossing retains the two facing Old World shores. `build_prototype3_regions.py` is retired.
- Rain-Shadow remains the dry leeward country. Live Front keeps Harrow's rise, the ford, and three small downstream hearths. Waiting Vale stays behind the east-facing coast and does not show Harrow's canopy.
- No labels, political borders, new named places, new powers, or canon claims were added.

## Label trial — Heskoren (2026-09-01)

Tried putting names on the painting even though the generate prompts say **NO TEXT**.

| File | What happened |
|---|---|
| `label-trials/Heskoren-Atlas-labeled-gen.png` | Image model, reference-locked. Some spellings landed. It **redrew** the continent (snow, vertical title, stacked names). Not a copy of the master. |
| `Heskoren-Atlas-Labeled.png` | Pillow overlay on the selected Prototype 3 master. Seats follow [[Named Ground]] and [[The Known Map]], not the largest painted cluster. **West (left):** last capes, marches, slate-shore, Ornled, toward the storm-wall. **East (right):** frontier coast, the West Water (to Strandoren), Eolvaeth / waiting vale, Harrow's and the Rise-water hamlets, the First Bowl. Vaelhesk is area-type over the south Yield. The south-east field-grid and extra roof-clusters stay unnamed. The north-east cloud bank is weather, not the storm-wall. |

The unlabeled C3 sheet stays the selected handout. The overlay is a table aid, not a second gazetteer. Do not promote generated fields or extra peaks into canon because a label sat near them. If a painted cluster and a note disagree, the note wins. Script: `14 - Assets/Maps/label_heskoren_atlas.py`.

The image-model attempt, for comparison:

![[label-trials/Heskoren-Atlas-labeled-gen.png]]

## Links
- [[Map Generation Tooling]] — prompts · [[The Known Map]] — labelled schematic
- [[Atlas Prototype Review]] — selected Prototype 3 and retained alternatives
- [[Named Ground]] · [[The World Frame]]
- [[14 - Assets]] · [[Roadmap]] (Story R.10)
