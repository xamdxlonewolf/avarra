---
title: Map Generation Tooling
type: asset
visibility: gm
note_status: draft
status: active
tags: [asset, map, tooling, azgaar, production]
aliases: [Azgaar Assets, Map Prompts, Heightmap Template, Atlas Prompts]
world: The Turning
created: 2026-08-22
updated: 2026-08-31
---

# Map Generation Tooling

> **Production aid, not canon.** Ways to *render* the world. The source of truth for what exists is [[The World Frame]], [[Named Ground]], and [[The Known Map]]. If a generator and a note disagree, the note wins. Extracted from player-facing geography in Story R.10 so a continent is not citing its own render pipeline.

> **How to use these.** **① Atlas prompts** (this section) → atmospheric base art; annotate yourself. **② Azgaar heightmap template** → a procedural labelled draft. **③ / ③b name bases** · **④ seed script** below. The SVG on [[The Known Map]] is a *schematic* for placement only — use these prompts when you want land that looks walked.

> **The label caveat (true of all AI image gens):** models garble text and will not keep a coastline identical between runs. Every prompt below ends **NO TEXT, NO LABELS**. You add names from [[Named Ground]] in Wonderdraft, Photoshop, or by hand. Do not treat a pretty generation as a survey.

## ① Atlas prompts — world, continents, regions

Paste **House style** + **Negative** + the **subject** block. Do not mix two subject blocks in one generate.

| Use | Aspect | Notes |
|---|---|---|
| World | 16:9 or 3:2 | all four landmasses; water must stay *readable as two different seas* |
| Continent | 4:3 or 3:2 | show a sliver of the neighbouring water so the set tiles in the head |
| Region | 4:3 or 1:1 | a week-to-a-month of ground, not another continent |

**Orientation (locked for this pack):** west = **left**, east = **right**, north = **up**. Matches [[The Known Map]] SVG. Flip later if a campaign wants it; keep a set internally consistent.

**What a Tree looks like in paint:** a slightly larger, darker canopy-dot or a small grove-circle — never a cartoon apple-tree, never a glowing world-tree on every square. One *exceptional* ancient canopy is allowed only at the Motherwood heart (world + Maiethorn + Sacred Core). **No Tree-mark on Kumbaan.**

**What settlement looks like:** nucleated — canopy, then roofs, then fields or lots. Quays are black hatch and crane-sticks, not modern docks. Roads are thin ochre threads with minute cairn-dots (mile-shrines). No painted national borders; powers are *textures of land*, not colour-fill.

### House style (paste first, every time)

```
Late-medieval illuminated portolan atlas page, not GIS, not a satellite, not a
generic high-fantasy poster. Strict top-down cartographic view (tiny bird's-eye
tilt only enough to read relief). Aged cream parchment, iron-gall brown ink,
moss-green forest wash, sea-green and slate water, warm ochre roads, muted umber
hills, cool grey rock. Fine hatching on cliffs, stipple on sand, tiny canopy-dots
for town Trees, one or two larger grove-masses where the wood is old. Thin ochre
road-threads; minute cairn-dots along pilgrimage roads; black hatch and tiny
crane-sticks on quays. Settlement is nucleated squares, not sprawl-megalopolis.
Ordinary lived land first — fields, coppice, salt, mud, snow — with a little
unease only in weather and distance. Silent decorative wind-rose with no letters.
Faint graticule or current-lines in the sea. Same atlas hand as the rest of the
set. Highly detailed terrain, readable at a glance and richer up close.
```

### Negative (paste last, every time)

```
NO TEXT, NO LABELS, NO LETTERS, NO NUMBERS, NO WORDS, NO BANNERS, NO CARTOUCHES
WITH WRITING, no compass letters, no modern typography, no photo-real satellite,
no neon, no chrome, no dragons, no flaming volcanoes, no lava, no giant castle
flags, no hard-painted national borders, no country colour-blocks, no race-coded
territory colours, no glowing magic runes, no spaceships, no twentieth-century
harbours, no motorways. Do not invent a fifth continent. Do not put a sacred
Tree or town-graft canopy on the far storm-walled isle.
```

*GPT Image / ChatGPT:* one subject per generate; add "square crop forbidden" on the world prompt if it wants to pad. *Midjourney:* `--ar 16:9` (world) or `--ar 4:3` (continent/region) `--style raw --v 6 --stylize 80`. *Flux / SD:* keep CFG moderate so the coast stays a coast.

**World-sheet failure mode.** Full-world gens reliably invent extra islands, sneak in fake script, and line the four lands up as a **necklace** (equal size, equal latitude, equal gaps — or the same trick on a diagonal). That is a diagram, not a world. Force an **Old World cluster** (Maiethorn + Strandoren almost touching across a thin strait) plus a **wide empty ocean** plus a **west-and-south frontier** plus a **tiny storm-isle** that is not the next bead. Prefer **C1–C4 + the two seas** as the working atlas, and treat **W** as a mood piece. If you need one sheet, composite the four continent paintings on parchment yourself. Do not let a pretty archipelago or a four-in-a-row become canon.

### Reference-locked workflow

When a world painting has been chosen, pass that same image into **every** world and continent generation. Start each continent prompt with:

```
Extract and enlarge the corresponding landmass from the supplied world
reference. Preserve its recognizable silhouette, capes, bays, orientation,
and north-up relationship. Do not rotate, mirror, or replace it with a generic
continent. Apply the canon terrain below inside that coastline.
```

The current reference is `references/World-Map-Reference.png`. Its upper-left storm-ringed isle is Kumbaan; lower-left is Heskoren; centre-right is Strandoren; far-right is Maiethorn. A detached storm-ringed speck southwest of Heskoren is source-art interpolation, **not** a fifth land, and must be omitted.

Three matched applications of this workflow are collected in [[Atlas Prototype Review]]:

1. **Reference-faithful dark portolan** — closest to the source palette.
2. **Pale engraved survey** — easiest to annotate.
3. **Weather-forward campaign atlas** — **selected 2026-09-01**; exact world-to-continent continuity plus strong climate and table mood.

Reference prompting keeps a family resemblance, but it does **not** guarantee identical geography. When exact continuity matters, make the continent sheets first and composite the world from scaled copies of those masters. Prototype 3 now follows that method; `build_prototype3_world.py` performs the reproducible composite. Do not independently regenerate its world sheet.

```bash
python3 -m pip install --upgrade pillow numpy
python3 "14 - Assets/Maps/build_prototype3_world.py"
```

### Prototype 3 regional rebuild workflow

Regional sheets should read as **the same atlas family**, inspired by the selected parent, not as duplicate continent crops. Supply the parent master plus a successful regional sheet (Old Crossing is the style match) and begin the subject with:

```
Paint this named region in the same dark weather-forward portolan hand as
the supplied regional sheet. Take coastline, watershed, wet/dry divide,
and settlement density from the supplied continent master. Keep north up
and west left. Do not copy the whole continent into the frame.
```

| Region | Required parent reference |
|---|---|
| R1 Old Crossing | `prototype3/Strandoren-Atlas.png` + `prototype3/Maiethorn-Atlas.png` |
| R2 Sacred Core | `prototype3/Maiethorn-Atlas.png` |
| R3 Rain-Wall | `prototype3/Maiethorn-Atlas.png` |
| R4 Rain-Shadow | `prototype3/Maiethorn-Atlas.png` |
| R5 Chart-run | `prototype3/Strandoren-Atlas.png` |
| R6 West Water | `prototype3/Strandoren-Atlas.png` + the selected world composite for open-water context |
| R7 Live Front | `prototype3/Heskoren-Atlas.png` |
| R8 Waiting Vale | `prototype3/Heskoren-Atlas.png` |

**Sacred Core and Rain-Wall** are generated regional paintings inspired by `prototype3/Maiethorn-Atlas.png` and styled to the other region sheets. They must remain **visibly different subjects**: forest heart with one exceptional Tree versus highland divide. Do not rebuild them as overlapping crops of the same continent sheet.

**Chart-run and West Water** remain Strandoren parent windows:

```bash
python3 "14 - Assets/Maps/build_prototype3_regions.py"
```

That script must not write Sacred Core or Rain-Wall.

**Visual review gate.** Reject a regional render if it is the same composition as another sheet, copies a whole continent into the frame, rotates/mirrors the parent, reverses a named river, adds text, introduces an exceptional Tree outside Sacred Core, or changes settlement scale. Reject Rain-Wall unless the divide is visibly made of irregular offset massifs, broad saddles, branching foothills, river-cut notches, and usable pass gaps. Match the selected set's dark weather-forward portolan hand, muted moss/umber land, iron-gall detail, and bronze frame.

**Interpolation remains non-canon.** Minor tributaries, unnamed roofs, exact paths, field divisions, forest edges, rocks, and weather decoration are rendering texture only. A generated detail enters canon only after it is reconciled and named in the vault.

**Sample renders** (this pass, label-free, not surveys) live beside this note and are browsable on [[The Atlas Sheets]]:

| File | Prompt |
|---|---|
| `The-Turning-World-Atlas.png` | Selected Prototype 3 continent-first composite |
| `Maiethorn-Atlas.png` | Selected Prototype 3 C1 master |
| `Strandoren-Atlas.png` | Selected Prototype 3 C2 master |
| `Heskoren-Atlas.png` | Selected Prototype 3 C3 master |
| `Kumbaan-Atlas.png` | Selected Prototype 3 C4 master |
| `Old-Crossing-Atlas.png` | R1 |
| `Sacred-Core-Atlas.png` | R2 |
| `Rain-Wall-Atlas.png` | R3 |
| `Rain-Shadow-Atlas.png` | R4 |
| `Chart-Run-Atlas.png` | R5 |
| `West-Water-Atlas.png` | R6 |
| `Live-Front-Atlas.png` | R7 |
| `Waiting-Vale-Atlas.png` | R8 |

---

### W. Known world

```
WORLD MAP of one ocean basin, west on the left, east on the right, north up.
Looks like a real hemisphere — two shores of a wide sea — NOT a diagram.

FORBIDDEN LAYOUTS: four continents in a straight horizontal row; the same four
on a diagonal necklace; equal size; equal latitude; equal gaps; beads on a
string; infographic lineup. Do not place the lands one-after-another along
any single line.

THE OLD WORLD CLUSTER fills the EASTERN HALF as neighbours:
Maiethorn (far east, largest) and Strandoren (immediately west of it) SHARE
latitudes and almost touch. Between them a NARROW crowded channel — a handful
of sailing-days, packed with tiny hull-ticks. They should read as one old
settled world that happens to have a busy strait through it.

MAIETHORN: bulky old continent. Western ports on the narrow sea. An IRREGULAR
north-south rain-divide through its middle (not a ring and not ruler-straight):
three offset weathered massifs joined by saddles, branching foothills, and
river-cut notches. West of the divide:
green cathedral-country, river valleys, one irregular old-growth heart with a
single enormous ancient tree-canopy. East of the spine: dry hills, sand-stipple,
a dashed seasonal wash.

STRANDOREN: a maritime land whose WHOLE identity is coastline — bays, sounds,
estuaries, peninsulas. Many tiny harbour-hatches. A fertile river-plain running
EAST to a large estuary on the narrow sea. Its WESTERN and SOUTHERN shores
face the WIDE darker ocean.

THE WEST WATER is the main emptiness: a dark open ocean TWO TO FOUR TIMES
wider than the eastern channel (weeks of sailing, not days). Few ships.
Lonely water also in the northwest.

HESKOREN sits on the WESTERN side of that wide ocean, distinctly SOUTH of the
Old World's midline — a frontier continent facing EAST toward home, not the
next tile in a path. Highland spines, dark forest pockets, moor, sparse
grove-settlements. Far western capes trail toward storm-cloud but do not
touch the isle.

KUMBAAN is SMALL and ALONE, west of Heskoren's last capes, not on anyone's
centerline. Compact green hills, pasture, standing-stones. Ringed by a killing
storm-girdle — dark swirling cloud, wrecking currents, pale reef. No city, no
great tree, no town-graft. Do not open a safe channel through the wall.

Exactly four landmasses. No extra islands. Three waters of different widths.
One parchment.
```

---

### C1. Maiethorn (Motherland)

```
CONTINENT MAP, one land filling most of the page, west on the left.

A large old rounded continent. WESTERN COAST (left): ancient rich ports on a
narrow crowded sea; old stone quays, not frantic modern docks; hinterland of
orchard and coppice. CENTRE-WEST: gentle rounded hills, dense town-canopies,
river valleys worn smooth — cathedral-country. HEART: a vast old-growth
woodland ring, clearings inside it, and at the very centre one enormous ancient
tree, darker and broader than any other canopy. A day's-walk ring of lodging
country and one small walled town-mark just outside the wood (not a capital
star). A thaw-river is born on the WEST FACE of the central highland and runs
west, slowing at a counted river-town where the water can hold a mill and a
grove. HIGHLAND CHAIN runs generally north–south through the middle as three
offset weathered massifs. It bends, widens, narrows, branches into foothills,
and briefly splits around upland basins before rejoining as one watershed.
Broad saddles connect the massifs; snow lies on broken high shelves. Show two
visible usable pass-notches (an older high notch with a pale water-stain line;
a lower shelf-road still in use). Do not paint a uniform white knife-edge or a
row of identical peaks. EAST of the divide:
abrupt climate change — dry hills, sand-stipple, well-towns, a dashed seasonal
watercourse, one west-road climbing back toward the passes. Ridge-perches and
pale high snow on the spine. Mix of nucleated Tree-towns everywhere west of the
divide; east, towns only at wells. Show a sliver of the narrow sea on the left
edge so this tiles against the trade continent.
```

---

### C2. Strandoren (Shore-lands)

```
CONTINENT MAP, one land filling most of the page, west on the left.

A large maritime continent that is almost all shoreline. Extraordinarily
indented coasts on EVERY side — fjordlets, tidal sounds, hooked peninsulas,
barrier islets, so the sea is the highway. EASTERN COAST (right) faces a NARROW
busy sea toward an unseen old land: the largest estuary on that face is a
salt-city — Tree-town on a rise, then leap-frog quays and warehouse-hatches
along the tide. A broad interior river-plain (the chart-run) feeds that estuary
from the west; a wealthy filed stretch of that river mid-continent. WESTERN and
SOUTHERN COASTS face a WIDER, darker ocean: fewer but bolder harbour-hatches,
one night-shore cluster of open-ocean berths, empty Eolthael-looking slips,
earth-dark holds. Interior lowlands fertile and wet-temperate; Trees mature
along wealthy coasts. Many tiny harbour ticks. No single throne-mark. Show the
narrow sea as a sliver on the right and the wide ocean as a sliver on the left.
```

---

### C3. Heskoren (Sundered Reach)

```
CONTINENT MAP, one land filling most of the page, west on the left.

A large rugged frontier continent, cooler and wilder than the Old World pair.
Highland spines (NOT the same range as the eastern rain-wall — different
weather, sharper, less settled), upland moors, deep dark forest pockets, long
rivers to a wild EASTERN COAST that faces a wide ocean (the way back toward
the trade continent). Civilization is a MAP OF SURVIVING GROVES: scattered
canopy-pockets with fields around them, long empty road between. One earlier
vale behind the east-facing coast — a pilgrim-fold at a spring, camp-streets,
a thin Tree that is not a certainty (not a capital star). Further inland, a
live-front rise with a healthier canopy; a small stream runs off that rise to
a ford where three tiny hamlet-greens sit, the far canopy visible from the
water. Wilder west and south: marches, slate-shore, host-right greens. Far
WESTERN CAPES trail toward storm-cloud and reef but the storm-isle is off this
page or only a hint on the far left. Harder winters in the wash: more rock,
more dark wood, fewer roofs. Show wide ocean on the right edge.
```

---

### C4. The Sundering Isle (Kumbaan)

```
ISLAND-CONTINENT MAP, the isle large on the page, utterly alone.

A small remote land of rolling green hills honeycombed with a sense of
under-hill life — pasture, terrace, standing-stones on the crests, NO cities,
NO great sacred tree, NO town-graft canopies. Moonlit-feeling even as a map:
pale hill-tops, silver water in folds, the surface quiet. The WHOLE isle is
girdled by a killing band: dense storm-cloud, wrecking current-whorls, jagged
pale reef, dark water. A few wreck-ticks in the reef, not a harbour. Mild wet
interior under the cloud-shadow. Walkable, known, the opposite of a trackless
frontier. Do not place a second island. Do not open a safe channel through the
wall — the wall is the climate.
```

---

### R1. The Old Crossing (both faces)

```
REGIONAL SEA-CHART of a NARROW crowded ancient sea, west on the left.

LEFT HALF: the eastern face of a deeply indented trade-coast. One large
estuary-city — nucleated Tree-town on a rise, first quay, second quay,
warehouse leap-frog along the tide, a lesser inner quay. Fertile river-plain
arriving from further left into the estuary.

THE WATER: close enough to feel like one argument. Wake-lines, many tiny
hull-ticks, a few tied berths, Hale-month storm-dark in the south of the
channel. Not an ocean. Not a river.

RIGHT HALF: the western face of an old rounded continent. Ancient rich ports,
less frantic; hinterland of coppice and orchard climbing toward green hills.
One hinge-shore cluster of old stone quays.

Both shores mild, wet-temperate, long-settled. This is the oldest trade route
in the world, painted as water that people have used for centuries. No capital
stars. No national colour.
```

---

### R2. Sacred Core and Motherwood

```
REGIONAL MAP of the old heart, west on the left. About a week of walking.

CENTRE: a vast old-growth woodland, the healthiest forest on the page, with
one enormous ancient tree-canopy in a deep grove. Small institutional
clearings in the wood — not a city, not a throne-mark.

A DAY'S WALK OUT from that grove (still close): lodging country — inns,
upper rooms, nucleated hearths along an ochre pilgrimage road marked with
cairn-dots. One small WALLED town inside that lodging country, not a flag
and not larger than the wood. Three days out along the same road: a
road-house hearth and a neighbour Hands-town.

A DIFFERENT ROAD, a thaw-river coming from the highland off the RIGHT of the
frame, slowing at a counted river-city (mill, wall-for-floods, tablet-halls
in old pilgrim-streets, Tree on the rise). The grove is a dark on that city's
horizon — close, not owned.

Rounded hills, four-season green, dense town-canopies. Ordinary cathedral-
country with pressure, not a golden paradise. No desert. No sea unless a
hint at the far left.
```

---

### R3. The Rain-Wall (Thaw-Land)

```
REGIONAL HIGHLAND MAP, west on the left.

A weathered north–south rain-divide filling the page: snow-shelves, rope-
and-wing ridge towns, not alpine postcard needles. WEST FACE (left): wet,
forested, rivers beginning as thaw; one substantial west-running river
leaving the snow. Two pass-notches: a HIGH old road-notch with a pale
horizontal water-stain across the ribbon-stone; a LOWER shelf-road still
carrying traffic, a toll-hatch at the lip. EAST FACE (right): the land
falls off into dry hill almost at once — rain-shadow starting in the same
frame. Sky-perches and pale high snow. A few nucleated valley-towns under
the west face. Mid-state: roads and water are levied; cliffs are not
furnished. Last year's snow as this year's civic year — snowfields still
lying while the west-running water is already fat. No Tengu-nation colour.
No Fox-nation colour.
```

---

### R4. Rain-Shadow (Saelthael)

```
REGIONAL DRY-COUNTRY MAP, west on the left.

Leeward land east of a highland that occupies only the LEFT edge of the
frame (the rain-wall's back). Dry hills, sand-stipple, pale grass, the one
true dry reach. A DASHED seasonal wash — river in a kind year, silt-line
in a cruel one. Towns ONLY at wells and at whatever grove has taken in thin
soil. One west-road well-town with a young-for-the-continent Tree beside
the well; a west-road climbing toward the unseen passes. A dry stair-rise
above a different well-town, climbing toward nothing that is a Tree. Sparse
canopy-dots. Heat-haze wash. This is still the same old land as the green
west — same town grammar, thinner wood. Not a desert-planet. Not a
Fox-kingdom colour-fill.
```

---

### R5. Chart-run and the Salt Quay hinterland

```
REGIONAL RIVER-AND-ESTUARY MAP, west on the left.

An interior fertile river-plain of a maritime continent, the river running
EAST into a large tidal estuary. Upstream: wealthy filed river-towns, mills,
ticket-hatches, grain. Mid-run: wet pasture, leaf-lots, carts. ESTUARY
(right): a salt-city — Tree on the rise, first quay as old landing, further
quays and warehouse leap-frog, a third quay on the north side with a
desk-house, ranging-yard inland, downwind infirmary-hatch, far shed. The
narrow sea beyond the estuary mouth, busy. Mild, wet, indented shores
north and south of the mouth. No throne-mark on the desk-house. Food is
this plain plus the catch.
```

---

### R6. Night Shore and the West Water

```
REGIONAL OPEN-OCEAN CHART, west on the left.

A west-and-south facing coast of the trade continent on the RIGHT of the
page; a WIDER, darker ocean filling the LEFT and CENTRE. Not the narrow
crowded crossing — this water is the long sea-leg. Bold harbour-hatches,
empty slips held for a far run, earth-dark holds, a night-shore cluster.
One UNLIT berth with no house-hatch attached (a gap in the lamps, not a
label). Tiny lamp-ticks along the quay. A few hull-ticks heading west.
Far LEFT: only a hint of a wilder coast or empty horizon — do not draw
the storm-isle unless as the faintest cloud. Weather is west-weather:
heavier swell, fewer wake-lines than the old crossing. This shore watches
for ships that do not arrive.
```

---

### R7. Live front (Harrow's rise and the ford)

```
REGIONAL FRONTIER MAP, west on the left. Hours-to-days of ground, not a
continent.

A low rise with a healthy grafted canopy and a small town around it —
fields, a square that used to be a road, the neighbour's green. A low
stream leaves that rise and runs to a FORD. Downstream of the ford: three
tiny hamlet-greens on slightly different ground (wetter shelf, old taken
plot, thinner rise), no stone on the waiting side, a cup-rock at the ford.
In clear weather the rise-canopy is a dark on the far slope from the
hamlets. Around this pocket: un-polity'd wild, long road, other distant
canopy-pockets. Cooler, wilder wash than the Old World. This is a Hand
that grew up, and a cluster that can see it and is still walking. Do not
draw a capital star on the rise. Do not make the hamlets a city.
```

---

### R8. Waiting vale (Eolvaeth country)

```
REGIONAL VALE MAP, west on the left.

A fold of upland BEHIND a wild east-facing frontier coast (show the coast
as a sliver on the right, not the subject). Two tracks meet at a spring.
A thin Tree — present, not a certainty, not Harrow's luck. Camp-streets
and pilgrim-fold around a gift-hall and gardens; almost no state. Ribbons
do not belong on a climb here: there is nothing to climb. Further inland
(left/up) the live-front luck is OUT OF SIGHT — do not draw Harrow's
canopy in this vale. Custom, gardens, ranging-slopes, alms-pot. Warm poor
faithful country, not a brutal frontier fort and not a pristine wilderness.
The wait is the town.
```

---

### How to annotate after generate

Add names from [[Named Ground]] and [[The Known Map]] only. Suggested first labels, not a new gazetteer:

| Art | Write on after |
|---|---|
| W | Kumbaan · storm-wall · Heskoren · West Water · Strandoren · Old Crossing · Maiethorn · Rain-Wall |
| C1 | Thaeloren · Inner Close · Orenbren · Maiethlir · Core-thaw · Noon Pass · Shelf-gate · Rain-Shadow · Hinge Shore |
| C2 | Orentel · Chart-run · Trenledd · Netstrand |
| C3 | Eolvaeth · Harrow's · the ford · Rise-water |
| C4 | nothing that implies a graft |
| R1 | Hinge Shore · Orentel · Hush-rate as a rate, not a border |
| R2 | Thaeloren · Inner Close · Third Hearth · Maiethlir |
| R3 | Thaw-Wall · Noon Pass · Shelf-gate |
| R4 | Ornsael · Well-wash · Dry Stair |
| R5 | Chart-run · first quay · White Note (building, not a crown) |
| R6 | West Water · Night Shore · the unlit berth unmarked or marked only in play |
| R7 | Harrow's · Rise-water · Brenod / Vaelun / Ornath |
| R8 | the spring · the vale — not "capital" |

---

## ② Azgaar heightmap template — the four continents

## ② Azgaar heightmap template — the four continents

Paste into Azgaar's Fantasy Map Generator: **Tools → Configure world / Template Editor → New template**, paste, and run. Encodes our layout — three large landmasses (east-old, west-trade, far-frontier) plus the small storm-walled isle far west. Coordinates are `X-range Y-range` on a 0–100 canvas (X: 0=west, 100=east; Y: 0=north, 100=south).

```
Hill 1 90-100 70-85 40-60
Hill 1 90-100 50-70 30-55
Multiply 0.8 30-100 0-100
Hill 1 85-100 35-50 55-75
Range 3-4 40-55 68-82 25-70
Hill 1 88-100 40-55 20-40
Hill 1 85-100 45-60 60-80
Hill 1 88-100 25-45 40-65
Range 2-3 30-45 20-40 45-70
Trough 3-4 25-35 30-45 20-80
Hill 1 80-95 20-40 65-90
Range 4-5 55-70 25-45 30-75
Trough 4-5 20-30 42-55 15-85
Hill 1 90-100 8-16 60-72
Pit 3-4 40-50 16-30 62-72
Range 1-2 30-45 8-16 60-72
Smooth 2
Add 5 20-100 0-100
```
*Reading it:* the first block builds **Maiethorn** (east, large, high, smoothed old land) with a central range; the middle block builds **Strandoren** (west-central) with a rough, trough-cut coast for all those harbours; then **Heskoren** (far west-south, large, mountainous frontier); then **The Sundering Isle** (far west, small, ringed by a `Pit`/`Trough` moat of deep water = the storm-wall). *Syntax drifts between Azgaar versions* — if a command errors, check the in-app template-editor legend and adjust the verb; the **shapes and positions** are the canon, the exact numbers are a starting point to nudge.

## ③ Azgaar Maiethren name base

So Azgaar auto-generates burgs/states that sound like our world. **Menu → Options → Configure → (Cultures / Names) → Add name base**, name it `Maiethren`, and paste this comma-separated list into the names field. Built from the [[The Old Tongue|Old Tongue]] phonology (liquids + nasals + soft *th*, long vowels, roots *oren / thael / maieth / vael / vaeth / hael / thren / ledd / orn*):

```
Maiethorn,Thaeloren,Vaethorn,Lestrand,Threnmaieth,Threnhael,Maieth,Thallow,Orenvael,Haelorn,Vaelthren,Strandor,Ledloren,Maiethren,Orenthael,Vaethael,Threnorn,Haelmaieth,Ledstrand,Vaeloren,Thaelvael,Orenmaieth,Vaethorn,Maiorn,Threnvael,Haelstrand,Ledoren,Vaelmaieth,Thaelorn,Orenhael,Maiethael,Strandoren,Vaethren,Ledmaieth,Thaelstrand,Orenvaeth,Haeloren,Threnstrand,Vaelthael,Maiethren,Ledhael,Orenstrand,Thaelmaieth,Vaethaloren,Haelvael,Threnloren,Maiethvael,Orenbren,Saelthael,Hinge Shore,Lirorn,Brenledd,Leddvael,Trenledd,Netstrand,Ornled,Vaelhesk,Saelvaeth,Eolvaeth,Orentel,Maiethlir
```
*Tuning:* set the name base's **"double-word" / min-max length** to taste; the roots above recombine into plausible Old-Tongue names.

Do not treat Azgaar's auto-names as new canon. Named ground lives in [[Named Ground]].

## ③b Azgaar Kumbaan name base

A **separate** base for [[The Sundering Isle]] — do not mix it with Maiethren. Open vowels, pre-nasal `mb` / `nd` / `nk` / `nj`, Wolof/Senegambian flavour, from the [[Yumboe]] register (seed `20260826` plus the locked own-names). **Menu → Options → Configure → (Cultures / Names) → Add name base**, name it `Kumbaan`:

```
Kumbaan,Bakhna,Rakhna,Ndeyaan,Ambaa,Njeela,Kumbo,Sambanka,Ndeya,Mbaraan,Njunda,Rakhilo,Sonkaa,Mbindaa,Yumbaka,Ndoolu,Sambiyo,Lunji,Yaaba,Saalo,Mbela,Soonke,Njili,Yendo,Waandi,Koriwaa,Mbaloolaa,Njunjo,Ndenjoo,Loowaa,Sindo,Nkusu,Bandoo,Lunkaa,Njaanjaa,Roondoo,Yaarose,Bundoke,Kanku,Lasoo,Nkiseke,Ndibi,Njuke,Nkoosa,Kumbili,Waandi,Yabuko
```

Person-names vs place-names: the short open words (Yaaba, Lunji, Saalo) work as people; the longer prenasal compounds (Mbaloolaa, Ndenjoo, Njaanjaa) read as hills and halls. Full rules in [[Naming People in the Turning]].

## ④ Azgaar seed script (bonus — version-fragile)

Optional. After generating a map in Azgaar, open the **browser console** (F12) and paste to *rename* three existing states + tag a religion toward our world. This binds to whatever states Azgaar already generated, so **run it once, post-generation**; it may break on Azgaar updates (the `pack` API drifts). Purely a convenience — not load-bearing.

```js
// Azgaar console seed — renames 3 states to our polities + 1 religion.
// Run AFTER the map generates. Fragile across Azgaar versions.
(() => {
  const S = pack.states.filter(s => s.i && !s.removed);
  const R = pack.religions.filter(r => r.i && !r.removed);
  const rename = (arr, i, name) => { if (arr[i]) arr[i].name = name; };
  rename(S, 0, "Threnmaieth");   // the Tallied Crown  — pious, surveilled core
  rename(S, 1, "Lestrand");      // the Ledger Coast   — secular merchant power
  rename(S, 2, "Vaethorn");      // the Waiting Lands   — devout frontier
  rename(R, 0, "The Motherfaith"); // the Leaf-Mother's gift-religion
  if (typeof drawStates === "function") drawStates();
  if (typeof drawReligions === "function") drawReligions();
  console.log("Seeded: Threnmaieth, Lestrand, Vaethorn + The Motherfaith.");
})();
```

## Links
- [[The Known Map]] — labelled schematic · [[The Atlas Sheets]] — generated paintings
- [[Named Ground]] — names and travel
- [[The World Frame]] · [[The Old Tongue]] · [[Yumboe]]
- [[14 - Assets]]
