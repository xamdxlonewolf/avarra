---
title: The Atlas Sheets
type: map
visibility: gm
note_status: draft
status: active
tags: [asset, map, atlas, epic-r, story-r10, epic-a]
aliases: [Atlas Gallery, Generated Maps, Continent Paintings]
world: The Turning
created: 2026-08-30
updated: 2026-09-16
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

Labeled overlay (2026-09-16). Pillow on this master, not a new survey. Rebuild with `label_maiethorn_atlas.py`.

![[Maiethorn-Atlas-Labeled.png]]

### Strandoren (C2)

![[Strandoren-Atlas.png]]

Labeled overlay (2026-09-16). Pillow on this master, not a new survey. Rebuild with `label_strandoren_atlas.py`.

![[Strandoren-Atlas-Labeled.png]]

### Heskoren (C3)

![[Heskoren-Atlas.png]]

Labeled trial (2026-09-01). Overlay on this master, not a new survey. Rebuild with `label_heskoren_atlas.py`.

![[Heskoren-Atlas-Labeled.png]]

### Kumbaan (C4)

No graft. No city. The wall is the climate.

![[Kumbaan-Atlas.png]]

Labeled overlay (2026-09-16). Pillow on this master, not a new survey. Rebuild with `label_kumbaan_atlas.py`.

![[Kumbaan-Atlas-Labeled.png]]

## Regions

### R1 — the Old Crossing

![[Old-Crossing-Atlas.png]]

Labeled overlay (2026-09-16). Pillow on this master, not a new survey. Rebuild with `label_old_crossing_atlas.py`.

![[Old-Crossing-Atlas-Labeled.png]]

### R2 — Sacred Core / Motherwood

![[Sacred-Core-Atlas.png]]

### R3 — the Rain-Wall

![[Rain-Wall-Atlas.png]]

Labeled overlay (2026-09-16). Pillow on this master, not a new survey. Rebuild with `label_rain_wall_atlas.py`.

![[Rain-Wall-Atlas-Labeled.png]]

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

Labeled overlay (2026-09-03). Pillow on this master, not a new survey. Rebuild with `label_world_atlas.py`.

![[The-Turning-World-Atlas-Labeled.png]]

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

## Label trial — World sheet (2026-09-03)

Pillow overlay on the selected Prototype 3 world master. Seats follow [[Named Ground]] and [[The Known Map]], west → east: Kumbaan · the storm-wall · Heskoren · the West Water · Strandoren · the Old Crossing · Maiethorn · the Rain-Wall. Continent names are large land-type. Seas sit in the middle of their water: the West Water in the southern basin between Heskoren and Strandoren (in the blue, not across either shore); the Old Crossing in the strait, following the channel. The storm-wall is a shallow crown on Kumbaan's foam ring. No fifth land. Decorative stars and extra painted texture stay unnamed. The Rain-Wall sits Maiethorn's spine, not Heskoren's highlands. No graft, city, or Tree named on Kumbaan. Continent epithets are the World Frame handles, not new places. Script: `14 - Assets/Maps/label_world_atlas.py`.

The unlabeled world sheet stays the selected handout.

## Maiethorn overlay — 2026-09-16

Pillow overlay on the selected Prototype 3 C1 master. The continent-scale labels come from [[Named Ground]], [[The Known Map]], and the locked C1 prompt: Thaeloren · Inner Close · Orenbren · Maiethlir · Core-thaw · Noon Pass · Shelf-gate · Rain-Wall · Rain-Shadow · Hinge Shore · Ornsael · Well-wash. Thaeloren sits in the circular old-growth heart and uses a canopy-ring marker as the sole exceptional Tree. The Inner Close is a small walled-town mark inside Orenbren, one day's walk from Thaeloren, and not a capital or sixteenth power. Maiethlir sits where the west-running Core-thaw slows. Noon Pass is the older high northern notch; Shelf-gate is the lower road. The Hinge Shore marks the western Old Crossing face. The Rain-Wall names the full divide; Rain-Shadow is broad climate type east of it, balanced by the well-town Ornsael and the seasonal Well-wash.

The unlabeled C1 sheet stays the selected handout. Incidental rivers, roofs, paths, and wells remain unnamed. Script: `14 - Assets/Maps/label_maiethorn_atlas.py`.

## Strandoren overlay — 2026-09-16

Pillow overlay on the selected Prototype 3 C2 master. The four map labels come from [[Named Ground]], [[The Known Map]], and the locked C2 prompt. Orentel sits at the large eastern estuary on the Old Crossing face; its plain settlement dot is not a capital star. The Chart-run crosses the fertile interior from the west to that estuary. Trenledd is area-type over the wealthy filed interior, with its still-unnamed seat unmarked. Netstrand is area-type on the open-ocean west and south face, also without a seat marker. No borders were drawn, and no incidental harbour, river branch, roof cluster, or field division was named.

The unlabeled C2 sheet stays the selected handout. Script: `14 - Assets/Maps/label_strandoren_atlas.py`.

## Kumbaan overlay — 2026-09-16

Pillow overlay on the selected Prototype 3 C4 master. Kumbaan is the only land label, seated over the central hill-country without a point marker; *the Sundering Isle* is its subordinate common-tongue epithet. The storm-wall follows the northern outer cloud-ring and names the complete girdle of cloud, current, and reef, not a political border or a break in the weather. No painted standing stone, wreck, hill, path, or interior texture is named. Nothing marks a graft, city, harbour, settlement, safe channel, or Tree.

The unlabeled C4 sheet stays the selected handout. Script: `14 - Assets/Maps/label_kumbaan_atlas.py`.

## Old Crossing overlay — 2026-09-16

Pillow overlay on the selected Prototype 3 R1 master. The chart names the Old Crossing in the channel. Orentel receives a plain settlement dot at the large Strandoren estuary on the western face, not a capital star. The Hinge Shore follows the opposite Maiethorn coast as area-type because its seat remains unnamed. The Hush-rate appears as a compact docket-like cartouche captioned *crossing charge*: no line crosses the water, and no territorial fill or political border is implied. Incidental quays, hulls, tributaries, roof clusters, and field divisions remain unnamed.

The unlabeled R1 sheet stays the selected handout. Script: `14 - Assets/Maps/label_old_crossing_atlas.py`.

## Rain-Wall overlay — 2026-09-16

Pillow overlay on the selected Prototype 3 R3 master. **The Rain-Wall** names Maiethorn's weathered north–south divide; Lirorn's local **Thaw-Wall** handle appears only as a secondary subtitle. The Noon Pass points to the older high northern road-notch and its water-line; Shelf-gate points to the lower road left after the Break. Small notch marks distinguish both from settlements and draw no border. The wet west face, dry east fall, snow-shelves, ridge towns, roads, and rivers remain painted terrain rather than additional named features. No label or fill claims Heskoren's separate spine, a Tengu nation, or a Fox nation.

The unlabeled R3 sheet stays the selected handout. Script: `14 - Assets/Maps/label_rain_wall_atlas.py`.

**Queue.** Remaining sheets are [[Roadmap#Epic A — Atlas labels|Epic A]] stories A.7 and A.9–A.13 — one sheet, one session. Copy the overlay scripts; do not ask the image model to write.

## Links
- [[Map Generation Tooling]] — prompts · [[The Known Map]] — labelled schematic
- [[Atlas Prototype Review]] — selected Prototype 3 and retained alternatives
- [[Named Ground]] · [[The World Frame]]
- [[14 - Assets]] · [[Roadmap]] (Story R.10 · Epic A)
