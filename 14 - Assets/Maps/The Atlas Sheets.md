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
updated: 2026-10-03
---

# The Atlas Sheets

> **Label-free paintings, not surveys.** Generated from the pack in [[Map Generation Tooling]]. Names and travel: [[Named Ground]]. Placement: [[The Known Map]] (SVG). If a painting and a note disagree, the note wins.

> **Selected atlas (2026-09-01): Prototype 3.** The main world and continent filenames below are promoted copies of the matched Prototype 3 masters. The world sheet is composited from those exact landforms, so coastlines and physical features agree across scales.

> **Handouts.** These label-free sheets can go to the table. They are still paintings rather than surveys; [[The Known Map]] and [[Named Ground]] remain authoritative for names and placement. Prototypes 1 and 2 are archived under `99 - Archive/Atlas/`. [[Atlas Prototype Review]] keeps the comparison. They are rejected alternatives, not parallel canon. [[The Selected Handouts]] says the same, from the empty Handouts folder.

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

Labeled overlay (2026-09-16). Pillow on this master, not a new survey. Rebuild with `label_sacred_core_atlas.py`.

![[Sacred-Core-Atlas-Labeled.png]]

### R3 — the Rain-Wall

![[Rain-Wall-Atlas.png]]

Labeled overlay (2026-09-16). Pillow on this master, not a new survey. Rebuild with `label_rain_wall_atlas.py`.

![[Rain-Wall-Atlas-Labeled.png]]

### R4 — Rain-Shadow

![[Rain-Shadow-Atlas.png]]

Labeled overlay (2026-09-17). Pillow on this master, not a new survey. Rebuild with `label_rain_shadow_atlas.py`.

![[Rain-Shadow-Atlas-Labeled.png]]

### R5 — Chart-run / Salt Quay hinterland

![[Chart-Run-Atlas.png]]

Labeled overlay (2026-09-17). Pillow on this master, not a new survey. Rebuild with `label_chart_run_atlas.py`.

![[Chart-Run-Atlas-Labeled.png]]

### R6 — Night Shore / West Water

![[West-Water-Atlas.png]]

Labeled overlay (2026-09-17). Pillow on this master, not a new survey. Rebuild with `label_west_water_atlas.py`.

![[West-Water-Atlas-Labeled.png]]

### R7 — live front (Harrow's and the ford)

![[Live-Front-Atlas.png]]

Labeled overlay (2026-09-19). Pillow on this master, not a new survey. Rebuild with `label_live_front_atlas.py`.

![[Live-Front-Atlas-Labeled.png]]

### R8 — waiting vale

![[Waiting-Vale-Atlas.png]]

Labeled overlay (2026-09-19). Pillow on this master, not a new survey. Rebuild with `label_waiting_vale_atlas.py`.

![[Waiting-Vale-Atlas-Labeled.png]]

## City sheets

New paintings, not crops of Sacred Core, Chart-run, Old Crossing, or the continent masters. The unlabeled Prototype 3 sheets stay the regional handouts. [[Eolvaeth]] stays a town and has no city sheet.

### Maiethlir

![[Maiethlir-City-Atlas.png]]

Labeled overlay (2026-10-02). Pillow on this city master. The image model was not asked to write. Rebuild with `label_maiethlir_city.py`.

![[Maiethlir-City-Atlas-Labeled.png]]

### Orentel

![[Orentel-City-Atlas.png]]

Labeled overlay (2026-10-02). Pillow on this city master. The image model was not asked to write. Rebuild with `label_orentel_city.py`.

![[Orentel-City-Atlas-Labeled.png]]

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
| `99 - Archive/Atlas/label-trials/Heskoren-Atlas-labeled-gen.png` | Image model, reference-locked. Some spellings landed. It **redrew** the continent (snow, vertical title, stacked names). Not a copy of the master. Archived 2026-10-03. |
| `Heskoren-Atlas-Labeled.png` | Pillow overlay on the selected Prototype 3 master. Seats follow [[Named Ground]] and [[The Known Map]], not the largest painted cluster. **West (left):** last capes, marches, slate-shore, Ornled, toward the storm-wall. **East (right):** frontier coast, the West Water (to Strandoren), Eolvaeth / waiting vale, Harrow's and the Rise-water hamlets, the First Bowl. Vaelhesk is area-type over the south Yield. The south-east field-grid and extra roof-clusters stay unnamed. The north-east cloud bank is weather, not the storm-wall. |

The unlabeled C3 sheet stays the selected handout. The overlay is a table aid, not a second gazetteer. Do not promote generated fields or extra peaks into canon because a label sat near them. If a painted cluster and a note disagree, the note wins. Script: `14 - Assets/Maps/label_heskoren_atlas.py`.

The image-model attempt, archived for comparison:

![[99 - Archive/Atlas/label-trials/Heskoren-Atlas-labeled-gen.png]]

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

## Sacred Core overlay — 2026-09-16

Pillow overlay on the selected Prototype 3 R2 master. The four labels come from [[Named Ground]], [[The Known Map]], the R2 prompt, and their settlement notes. Thaeloren uses a canopy-ring mark at the sole exceptional Tree in the central old-growth grove; the First Seat receives no separate throne or capital mark. The Inner Close is the walled town one day's walk out, inside Orenbren lodging-country. The Third Hearth is a modest road-house mark three days outward on the same Near Mile, not a city or power. Maiethlir is the counted river-city where the Core-thaw slows, reached by a different river road. No incidental clearing, roof cluster, road branch, or forest track was named.

The unlabeled R2 sheet stays the selected handout. Script: `14 - Assets/Maps/label_sacred_core_atlas.py`.

## Rain-Wall overlay — 2026-09-16

Pillow overlay on the selected Prototype 3 R3 master. **The Rain-Wall** names Maiethorn's weathered north–south divide; Lirorn's local **Thaw-Wall** handle appears only as a secondary subtitle. The Noon Pass points to the older high northern road-notch and its water-line; Shelf-gate points to the lower road left after the Break. Small notch marks distinguish both from settlements and draw no border. The wet west face, dry east fall, snow-shelves, ridge towns, roads, and rivers remain painted terrain rather than additional named features. No label or fill claims Heskoren's separate spine, a Tengu nation, or a Fox nation.

The unlabeled R3 sheet stays the selected handout. Script: `14 - Assets/Maps/label_rain_wall_atlas.py`.

## Rain-Shadow overlay — 2026-09-17

Pillow overlay on the selected Prototype 3 R4 master. **The Rain-Shadow** names the dry east as climate-type, oriented east of the Rain-Wall; the left highlands are that range's back and are not given a second range label here. Ornsael receives a plain well-town dot at the west-road settlement with a Tree beside the well, not a capital star and not Thaeloren's canopy-ring. The Dry Stair is a small ascent mark on the stair-rise of a different hill; the well-town at its shoulder stays unnamed. The Well-wash follows the painted seasonal channel as hydrology, not a civic river or a border. Terraces, the far-east roof-cluster, and other incidental texture remain unnamed. Nothing draws Fox-nation colour.

The unlabeled R4 sheet stays the selected handout. Script: `14 - Assets/Maps/label_rain_shadow_atlas.py`.

## Chart-run overlay — 2026-09-17

Pillow overlay on the selected Prototype 3 R5 master. **The Chart-run** follows the interior river east into the Salt Quay estuary. The first quay is a landing mark at the old inner south waterfront below the rise, not a city or capital. **The White Note** is a desk-house on the third quay, north side — a building mark, not a crown. Leap-frog warehouses, the south-mouth yards, filed river-towns, and other incidental texture remain unnamed. Nothing draws a capital star or makes the desk the government.

The unlabeled R5 sheet stays the selected handout. Script: `14 - Assets/Maps/label_chart_run_atlas.py`.

## West Water overlay — 2026-09-17

Pillow overlay on the selected Prototype 3 R6 master. **The West Water** names the open ocean as the long sea-leg, not the crowded Crossing; the hydrology sits in the blue, not across the shore. **The Night Shore** is area-type on the west-and-south face because its seat remains unnamed. The unlit berth is left unmarked. Hulls, harbour hatches, lamp-ticks, the painted inland run, and the far-left weather remain unnamed. Nothing draws a capital star, a border, a Kind-nation, or a graft on the storm-isle.

The unlabeled R6 sheet stays the selected handout. Script: `14 - Assets/Maps/label_west_water_atlas.py`.

## Live Front overlay — 2026-09-19

Pillow overlay on the selected Prototype 3 R7 master. **Harrow's** is a plain grove-town on the rise canopy — not a capital star and not Thaeloren's canopy-ring. **The Rise-water** follows the low stream from that rise toward the ford. **Brenod**, **Vaelun**, and **Ornath** are small hearth marks on different ground past the crossing: the sending road-hearth, the wetter old plot, and the thinner rise. The ford, the cup-rock, distant canopy-pockets, and incidental roofs remain unnamed. Session one still sits here; that is not a map label.

The unlabeled R7 sheet stays the selected handout. Script: `14 - Assets/Maps/label_live_front_atlas.py`.

## Waiting Vale overlay — 2026-09-19

Pillow overlay on the selected Prototype 3 R8 master. **The Waiting Vale** names the fold behind the east-facing coast as area-type; *Eolvaeth country* is the seat's handle, not a capital title. The spring is a pool-mark at the painted water where the tracks meet — a site, not a mile-shrine stone and not a Tree. **Eolvaeth** receives a plain pilgrim-town dot at the gift-hall cluster, not a capital star and not Thaeloren's canopy-ring. Harrow's canopy is neither drawn nor named; inland luck stays out of sight. The coast sliver, garden-grid, extra tracks, and the western ridge remain unnamed. Nothing draws a border, a Kind-nation, or a throne.

The unlabeled R8 sheet stays the selected handout. Script: `14 - Assets/Maps/label_waiting_vale_atlas.py`.

## City sheets — 2026-10-02

Two new city paintings. Not crops, and not relabels, of Sacred Core, Chart-run, Old Crossing, or the continent masters. Names come from [[Maiethlir]] and [[Orentel]] only. If the painting and the note disagree, the note wins. The image model was not asked to write. Unlabeled Prototype 3 sheets stay the regional handouts. [[Eolvaeth]] has no city sheet. World book untouched.

Repainted again the same day so each city fills its sheet, and the zoom is the same place as the city plate. Maiethlir sits in Sacred Core forest, river running west, roofs on both banks. Orentel sits on the Chart-run estuary, filed plain to the west, sea to the east, the harbour the larger half. The Tree square is the smaller half of Orentel. No new names.

### Maiethlir heart

![[Maiethlir-Heart-Atlas.png]]

The same square as the city plate, drawn closer: the Tree on the left is a mature Hand, a broad dark hardwood filling its square, not the First Hand. The tablet-hall stays one street to the east. The Slow Water stays along the bottom. Rebuild with `label_maiethlir_heart.py`.

![[Maiethlir-Heart-Atlas-Labeled.png]]

### Orentel drop

![[Orentel-Drop-Atlas.png]]

The Rise inside the roofs. The Tree is a mature Hand, a broad dark hardwood filling its square, not the First Hand and not a glow. The Drop leaves the square through houses. The quays are not on this sheet. Rebuild with `label_orentel_drop.py`.

![[Orentel-Drop-Atlas-Labeled.png]]

**Maiethlir.** `Maiethlir-City-Atlas-Labeled.png` is a Pillow overlay on `Maiethlir-City-Atlas.png`. West is left. The river runs west. **Down Gate** is the downstream opening in the old flood-wall. **Wall Path** is the upstream road outside the wall, on the east bank. **Grove Bank** is the north road from the wood. The wood is not a seat. The First Seat is not marked. [[Maiethvael]]'s seat is not named. **The Tree** is the civic canopy on the **Slow Water**, inside the wall, with no capital star and not Thaeloren's ring. **Loft Row** is the one street from that Tree to the **Tablet-hall**, which stands east of the square. The heart sheet is that same square. Painted battlements are incidental; the wall is the flood-wall. South-bank streets stay unnamed. No second name on the Core-thaw. [[Nelath]] is not on this sheet. Script: `label_maiethlir_city.py`.

**Orentel.** `Orentel-City-Atlas-Labeled.png` is a Pillow overlay on `Orentel-City-Atlas.png`. West is left. The estuary opens east. **Chart mouth** is the western river entry. **Crossing-mouth** is the eastern sail-in. **The Tree** stands on **The Rise**, a small square inside the roofs. **The Drop** is the street from that free Hand down to the held berths. The drop sheet shows only its inland start, with the Tree surrounded by roofs, and does not draw the quays. **First Quay** is the old south landing at the end of that street, on the city plate. **The Third** is the north-side quay. **White Note** is a desk-house on that quay, not a crown and not on the Rise. **Hallowquay** is the lesser inner landing. **Inland yard** is the open pasture behind the Rise. No capital star. No city wall is named. [[Denlad]] is not a district here. Script: `label_orentel_city.py`.

## City details — 2026-10-03

Two new closer paintings. Not crops of Sacred Core, Chart-run, Old Crossing, the continent masters, or the four city paintings already in the atlas. Names come from [[Maiethlir]], [[Orentel]], and [[The White Note House]]. If a painting and a note disagree, the note wins. The image model was not asked to write. The city plates, the heart sheet, and the drop sheet were not redrawn. Unlabeled Prototype 3 sheets stay the regional handouts. World book untouched.

### Orentel piers

![[Orentel-Piers-Atlas.png]]

The tide, not the hill. The Rise stays off the inland edge, so the Tree stays inland. The Drop's quay end may enter from that edge. The Tree, the square, and the salt on the roots stay on the drop sheet. Rebuild with `label_orentel_piers.py`.

![[Orentel-Piers-Atlas-Labeled.png]]

### Maiethlir Grove Bank

![[Maiethlir-Grove-Bank-Atlas.png]]

The road, not the square. The gate is in the old flood-wall. The Motherwood is a dark behind that gate. The wood is not labeled. The First Seat is not marked. Rebuild with `label_maiethlir_grove_bank.py`.

![[Maiethlir-Grove-Bank-Atlas-Labeled.png]]

**Orentel piers.** `Orentel-Piers-Atlas-Labeled.png` is a Pillow overlay on `Orentel-Piers-Atlas.png`. West is left. The frame is the tide. **First Quay** is the south landing. Berths 1–4 are held. Berth 5 is earth. The berths are not lettered. **The Third** is the north-side quay. **White Note** is one desk-house on that north side, not the council, not the crown, and not a palace. Mataero's loft stays off this sheet with the Rise. Hallowquay, the inland yard, the Chart mouth, the Crossing-mouth, Denlad, the release-house, and the leaf-lots stay off the labels. No city wall. No capital star. Script: `label_orentel_piers.py`.

**Maiethlir Grove Bank.** `Maiethlir-Grove-Bank-Atlas-Labeled.png` is a Pillow overlay on `Maiethlir-Grove-Bank-Atlas.png`. West is left. The frame is the road. **Grove Bank** is the north road from the wood, one or two days, and it is not the Near Mile. The gate is in the old flood-wall. The wood is a dark behind that gate and is not labeled. The First Seat stays in that wood, unnamed: no college, no throne, no canopy-ring, and no mark. Thaeloren's canopy is not on this sheet. The civic Tree on the Slow Water stays on the heart sheet. Loft Row, the tablet-hall, the Down Gate, and the Wall Path are not redrawn here. [[Maiethvael]]'s seat is not named. The Down Gate is not that seat. Painted battlements are incidental; the wall is the flood-wall. Script: `label_maiethlir_grove_bank.py`.

**Queue.** [[Roadmap#Epic A — Atlas labels|Epic A]] is complete (A.1–A.14). Story M.1 is in. Story M.2 is in. Story M.3 is in. Unlabeled Prototype 3 sheets stay the regional handouts. Do not ask the image model to write. Do not start from these sheets by cropping a regional master, a city plate, or a town sheet. M.4 was not opened. Story M.4 puts pointers on the overlays that already exist. That pass has not been drawn.

## Town sheets — 2026-10-03

Six new paintings. Not crops of the regional masters, the continent masters, the city plates, the heart sheet, the drop sheet, the pier sheet, or the Grove Bank sheet. Names come from the settlement notes. If a painting and a note disagree, the note wins. The image model was not asked to write. Masters are 1152×864. West is left. No capital star. A civic Hand is a broad dark hardwood filling its square. Thaeloren is not on these sheets. Unlabeled Prototype 3 sheets stay the regional handouts. World book untouched.

[[Rothallo]] is the Inner Close. People still say that name. It is Orenbren's walled capital, one day from the wood, and it is the same place. No sheet in M.2. The plate is with the M.3 seats, below.

### Eolvaeth

![[Eolvaeth-Atlas.png]]

The fold. A maybe-Hand at the centre, the spring, the gift-hall, and camp-streets that learned to winter. No walls. Rebuild with `label_eolvaeth.py`.

![[Eolvaeth-Atlas-Labeled.png]]

### Harrow's Green

![[Harrows-Green-Atlas.png]]

The live-front square. A Hand at the centre, the stone in the square, the Rise-water at the foot of the rise. No walls. Rebuild with `label_harrows_green.py`.

![[Harrows-Green-Atlas-Labeled.png]]

### The Mill-hold

![[Mill-hold-Atlas.png]]

A mill-town. The Hand is sick this year: the canopy is visibly wrong, and it is still a hardwood. The mill-house and the race sit on the lower side. The culvert is under the square. No walls. Rebuild with `label_mill_hold.py`.

![[Mill-hold-Atlas-Labeled.png]]

### Ornsael

![[Ornsael-Atlas.png]]

A well-town in the dry country. The Tree stands beside the well. The west-road is the main street and leaves toward the pass. No walls. Rebuild with `label_ornsael.py`.

![[Ornsael-Atlas-Labeled.png]]

### Nelath

![[Nelath-Atlas.png]]

A smaller square than the Mill-hold. A sound Hand. The spur comes in and becomes the square. Beyond the boughs the road is a scar. The stone is in the square. No walls. Rebuild with `label_nelath.py`.

![[Nelath-Atlas-Labeled.png]]

### Ndenjoo

![[Ndenjoo-Atlas.png]]

A close piece of the slope, at village scale. The hill continues off the frame. A hall under the turf, a few dozen hearths, pasture, a standing-stone, and a path that leaves toward the sand. No Tree. Rebuild with `label_ndenjoo.py`.

![[Ndenjoo-Atlas-Labeled.png]]

**Eolvaeth.** `Eolvaeth-Atlas-Labeled.png` is a Pillow overlay on `Eolvaeth-Atlas.png`. West is left. The frame is the fold. **The Tree** is a maybe-Hand, a broad dark hardwood filling its square, not Harrow's luck and not Thaeloren. **The spring** is the pool. It is not a mile-shrine. **The gift-hall** is the long hall on the square. Vaethod is not labeled. No walls. No capital star. Script: `label_eolvaeth.py`.

**Harrow's Green.** `Harrows-Green-Atlas-Labeled.png` is a Pillow overlay on `Harrows-Green-Atlas.png`. West is left. **The Tree** is the sound Hand in the square. **The stone** is the standing stone in that square. The Rise-water runs at the foot of the rise and is not labeled. Brenod, Vaelun, and Ornath are not on this sheet. The square is not Nelath. No fortress. No capital star. Script: `label_harrows_green.py`.

**The Mill-hold.** `Mill-hold-Atlas-Labeled.png` is a Pillow overlay on `Mill-hold-Atlas.png`. West is left. **The Tree** is the sick Hand: leaves late and thin, the crown visibly wrong, still a hardwood and not a glow. **The mill-race** is the water on the lower side. **The culvert** is the drain in the square. Brenthael is not drawn. No capital star. Script: `label_mill_hold.py`.

**Ornsael.** `Ornsael-Atlas-Labeled.png` is a Pillow overlay on `Ornsael-Atlas.png`. West is left. **The Tree** stands beside **The well**. **The west-road** is the main street and leaves toward the pass. This is not Saelthael's capital and not Larbril. No capital star. Script: `label_ornsael.py`.

**Nelath.** `Nelath-Atlas-Labeled.png` is a Pillow overlay on `Nelath-Atlas.png`. West is left. **The Tree** is a sound Hand. **The stone** is in the square. **The scar** is the ditch and thorns beyond the boughs, with no cart-track. The cistern is the drink and is not labeled. The Third Hearth, the Mill-hold, and the First Seat are not drawn. No capital star. Script: `label_nelath.py`.

**Ndenjoo.** `Ndenjoo-Atlas-Labeled.png` is a Pillow overlay on `Ndenjoo-Atlas.png`. West is left. The frame is a piece of the slope. The hill continues off the edges. **The hall** is the lit turf door. The standing-stone, the path, and the sand stay unlabeled. Njunda is not labeled. No Tree, no dead trunk, no graft. The storm-wall stays weather. No capital star. Script: `label_ndenjoo.py`.

## Seats — 2026-10-03

Thirteen new paintings. Not crops of the regional masters, the continent masters, the city plates, the heart sheet, the drop sheet, the pier sheet, the Grove Bank sheet, or the M.2 town sheets. Names come from the settlement notes. If a painting and a note disagree, the note wins. The image model was not asked to write. Masters are 1152×864. West is left. No capital star. A civic Hand is a broad dark hardwood filling its square. Thaeloren is not on these sheets. [[Vaelhesk]] has no sheet. The six charter-towns were not painted. Unlabeled Prototype 3 sheets stay the regional handouts. World book untouched.

### Seinbrun

![[Seinbrun-Atlas.png]]

A large city off the water. The furnished hall, the green beside it, and a Hand beside the hall. No city wall. Rebuild with `label_seinbrun.py`.

![[Seinbrun-Atlas-Labeled.png]]

### Rothallo

![[Rothallo-Atlas.png]]

Orenbren's walled capital, one day from the wood. People still say the Inner Close. The gate, the beds outside the wall, and a Hand inside. Rebuild with `label_rothallo.py`.

![[Rothallo-Atlas-Labeled.png]]

### Rothallo gate

![[Rothallo-Gate-Atlas.png]]

The city plate could not hold the beds outside and the Book inside. This is that gate. Rebuild with `label_rothallo_gate.py`.

![[Rothallo-Gate-Atlas-Labeled.png]]

### Larbril

![[Larbril-Atlas.png]]

A medium city. No wall. The west road meets the Well-wash. The wash in this frame is a silt-line. A Hand at the meeting. Rebuild with `label_larbril.py`.

![[Larbril-Atlas-Labeled.png]]

### Votaer

![[Votaer-Atlas.png]]

One of the largest cities. The sea is west. The classification quay is the working waterfront. A Hand stands back from that quay. Rebuild with `label_votaer.py`.

![[Votaer-Atlas-Labeled.png]]

### Raitin

![[Raitin-Atlas.png]]

A river-city. The council hall stands at the head of the river stair. A Hand beside the hall. The river is not named. Rebuild with `label_raitin.py`.

![[Raitin-Atlas-Labeled.png]]

### Naenor

![[Naenor-Atlas.png]]

A large port on its own coast. The signing-watch is the book-table in the square. A Hand stands off that square. Rebuild with `label_naenor.py`.

![[Naenor-Atlas-Labeled.png]]

### Lunbra

![[Lunbra-Atlas.png]]

A large city on the Chart-run, inland of the salt. The river runs east. The roll-room stands on the square. A Hand in the square. Rebuild with `label_lunbra.py`.

![[Lunbra-Atlas-Labeled.png]]

### Braetu

![[Braetu-Atlas.png]]

A harbour city on the West Water. The sea is west. A Hand stands back from the working water. Rebuild with `label_braetu.py`.

![[Braetu-Atlas-Labeled.png]]

### Braetu quay

![[Braetu-Quay-Atlas.png]]

The city plate could not hold the quote-desk and the unlit berth together. The sea is west. Rebuild with `label_braetu_quay.py`.

![[Braetu-Quay-Atlas-Labeled.png]]

### Tasain

![[Tasain-Atlas.png]]

A walled town in the valley. The town gate is in the frame. The Shelf-gate stays off the sheet. Rebuild with `label_tasain.py`.

![[Tasain-Atlas-Labeled.png]]

### Sanbreo

![[Sanbreo-Atlas.png]]

A town on the brink of a small city. The shore gate, the slate on the wall inside it, and the beach. The sea is east. Rebuild with `label_sanbreo.py`.

![[Sanbreo-Atlas-Labeled.png]]

### Natai

![[Natai-Atlas.png]]

A march-town. The town gate is on the road. A young Hand. Rebuild with `label_natai.py`.

![[Natai-Atlas-Labeled.png]]

**Seinbrun.** `Seinbrun-Atlas-Labeled.png` is a Pillow overlay on `Seinbrun-Atlas.png`. West is left. The frame is the city. **The hall** is the furnished hall. **The green** is the ground beside it. **The Tree** is the Hand beside the hall. No city wall. The wood is not inside the city. The First Seat is not marked. Thaeloren is not on this sheet. No closer sheet. No capital star. Script: `label_seinbrun.py`.

**Rothallo.** `Rothallo-Atlas-Labeled.png` is a Pillow overlay on `Rothallo-Atlas.png`. West is left. This is the Inner Close. **The gate** is the argument. **The beds** are outside the wall. **The Tree** is the Hand inside the walls. The city does not Speak it. The Book is on the gate sheet. The First Seat stays in the wood, unnamed: no college, no throne, no canopy-ring, and no mark. Thaeloren is not on this sheet. No capital star. Script: `label_rothallo.py`.

**Rothallo gate.** `Rothallo-Gate-Atlas-Labeled.png` is a Pillow overlay on `Rothallo-Gate-Atlas.png`. West is left. **The gate** is the same gate. **The beds** are outside. **The Book** is the Book of Tithes, inside the wall. No capital star. Script: `label_rothallo_gate.py`.

**Larbril.** `Larbril-Atlas-Labeled.png` is a Pillow overlay on `Larbril-Atlas.png`. West is left. **The meeting** is where the west road meets the Well-wash. **The west road** leaves toward the pass. **Well-wash** is a silt-line in this frame. **The Tree** stands at the meeting. No wall. Not Ornsael. Not the Dry Stair. No capital star. Script: `label_larbril.py`.

**Votaer.** `Votaer-Atlas-Labeled.png` is a Pillow overlay on `Votaer-Atlas.png`. West is left. The sea is on the left. **Classification quay** is the working waterfront. **The Tree** stands back from that quay. The blessing and the docket are the same quay. No White Note. No Chart-run. No closer sheet. No capital star. Script: `label_votaer.py`.

**Raitin.** `Raitin-Atlas-Labeled.png` is a Pillow overlay on `Raitin-Atlas.png`. West is left. **The hall** is the council hall. **The river stair** is the stair under it. **The Tree** stands beside the hall. The river is not named. The six charter-towns stay off the sheet. No capital star. Script: `label_raitin.py`.

**Naenor.** `Naenor-Atlas-Labeled.png` is a Pillow overlay on `Naenor-Atlas.png`. West is left. **The signing-watch** is the book-table in the square. **The Tree** stands off that square. Working berths. Not the Chart-run. Not the West Water. The lost berth is not in this city. No capital star. Script: `label_naenor.py`.

**Lunbra.** `Lunbra-Atlas-Labeled.png` is a Pillow overlay on `Lunbra-Atlas.png`. West is left. The Chart-run runs east, toward the right. **The roll-room** stands on **the square**. **The Tree** is in the square. **Chart-run** is the river. The governing throat is not named. The square and the roll-room are both on this plate. No closer sheet. No capital star. Script: `label_lunbra.py`.

**Braetu.** `Braetu-Atlas-Labeled.png` is a Pillow overlay on `Braetu-Atlas.png`. West is left. The sea is on the left. **The Tree** stands back from the working water. **West Water** is that sea. The quote-desk and the unlit berth are on the quay sheet. The White Note is not here. No capital star. Script: `label_braetu.py`.

**Braetu quay.** `Braetu-Quay-Atlas-Labeled.png` is a Pillow overlay on `Braetu-Quay-Atlas.png`. West is left. **The quote-desk** is on the quay. **The unlit berth** has no house on it. **West Water** is the sea on the left. No capital star. Script: `label_braetu_quay.py`.

**Tasain.** `Tasain-Atlas-Labeled.png` is a Pillow overlay on `Tasain-Atlas.png`. West is left. The frame is the town, not the shelf. **The town gate** is the wall in the valley. **The Tree** is the Hand inside. The Shelf-gate stays off the sheet. Narol is not labeled. No capital star. Script: `label_tasain.py`.

**Sanbreo.** `Sanbreo-Atlas-Labeled.png` is a Pillow overlay on `Sanbreo-Atlas.png`. West is left. The sea is on the right. **The shore gate** meets the beach. **The slate** is on the wall inside the gate. The line is not written on it. No civic Hand is the subject. Not a harbour city. No capital star. Script: `label_sanbreo.py`.

**Natai.** `Natai-Atlas-Labeled.png` is a Pillow overlay on `Natai-Atlas.png`. West is left. The frame is the town. **The town gate** is on the road. **The Tree** is a young Hand. Harrow's Green, the ford, and the three hamlets are not drawn. Dumu is not labeled. No capital star. Script: `label_natai.py`.

## Epic M pointers — 2026-10-03

Capitals, large cities, and important towns get a plain pointer and a label on the overlays that already show their ground, and on [[The Known Map]]. Decided 2026-10-03. Story M.4 on [[Roadmap]]. The paintings stay. Pillow on these masters. No capital star. A mark only where the notes already place the place. [[Vaelhesk]] gets no settlement dot. Unlabeled Prototype 3 sheets stay the handouts. This pass has not been drawn.

## Label cleanup — 2026-09-23

Captions, epithets, and the survey footer are off the overlays. Each painted name is the thing itself: a place gets that name, and a point or leader only when the name would otherwise sit on the roofs. Rivers, oceans, and seas follow the water (`label_curves.py`). Land names stay straight. Sheet titles that repeated a name already on the water or the spine were dropped. Unlabeled sheets stay the handouts.

## Links
- [[Map Generation Tooling]] — prompts · [[The Known Map]] — labelled schematic
- [[Atlas Prototype Review]] — selected Prototype 3 and retained alternatives
- [[Named Ground]] · [[The World Frame]]
- [[14 - Assets]] · [[Roadmap]] (Story R.10 · Epic A · Story M.1 · Story M.2 · Story M.3 · Story M.4)
