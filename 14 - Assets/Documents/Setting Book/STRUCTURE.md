# World Book Structure

This is the **locked spine** of *The Turning* world book. Chapter numbers and titles do not move. New work fills a reserved chapter or a reserved heading inside one. It does not invent a parallel outline.

**Status**
- **filled** — prose is in; polish later, don't restructure
- **partial** — the chapter exists; named holes inside it are marked *Not yet written*
- **reserved** — the chapter is a stub. Write into it when that part of the world is built

**Convention in the text.** A reserved hole is a block beginning **Not yet written.** The builder styles those blocks so they are obvious in HTML and PDF. When you fill a hole, delete that block and put the real prose in its place.

The compiled book is `The-Turning-World-Book.html` / `.pdf`. Source chapters live in `chapters/`. Rebuild with `build_world_book.py`. Vault notes remain canonical; this book is the reading copy. **Do not update this book as vault work lands — only when the user asks for an updated version.**

## Spine

| File | Book | Chapter | Status |
|---|---|---|---|
| 00-using-this-book.md | Front | Using This Book | filled |
| 01-the-world-in-brief.md | I · What This World Is | The World in Brief | filled |
| 02-kind-and-condition.md | I · What This World Is | Kind and Condition | filled |
| 03-the-conditions.md | II · Peoples | The Conditions | filled |
| 04-the-kinds.md | II · Peoples | The Kinds | filled |
| 05-language-and-naming.md | II · Peoples | Language and Naming | filled |
| 06-the-turning-tree.md | III · The Tree and the Faiths | The Turning Tree | filled |
| 07-the-leaf-mother.md | III · The Tree and the Faiths | The Leaf-Mother | filled |
| 08-the-five-faiths.md | III · The Tree and the Faiths | The Five Faiths | filled |
| 09-orders-and-houses.md | III · The Tree and the Faiths | Orders and Houses | filled |
| 10-law-and-citizenship.md | IV · How People Live | Law and Citizenship | filled |
| 11-economy-and-the-tithe.md | IV · How People Live | Economy and the Tithe | filled |
| 12-daily-life.md | IV · How People Live | Daily Life | filled |
| 13-tithe-guilds.md | IV · How People Live | Tithe-Infrastructure and Guilds | filled |
| 14-the-lands.md | V · The Lands | The Four Continents | filled |
| 15-the-reckoning.md | V · The Lands | The Reckoning of the Year | filled |
| 16-climate-and-ecology.md | V · The Lands | Climate, Ecology, and Travel | filled |
| 17-maps.md | V · The Lands | Maps | filled |
| 18-the-ages.md | VI · The Ages | The Ages | filled |
| 19-the-fifteen-powers.md | VII · Powers and Places | The Fifteen Powers | filled |
| 20-gazetteer.md | VII · Powers and Places | Gazetteer | filled |
| 21-other-places.md | VII · Powers and Places | Other Places | partial |
| 22-faces-of-the-turning.md | VIII · Faces | Faces of the Turning | filled |
| 23-at-the-table.md | IX · At the Table | Playing in the Turning | filled |
| 24-gm-canon.md | X · For the GM | GM Canon | filled |

## Reserved holes inside filled chapters

These stay where they are. Do not promote them to new chapters unless the spine is deliberately revised.

- **Two claimants on one green** (ch. 21) — a type only. Vaelun leans this way. No seated square.
- **Open questions** (ch. 24) — who made the First Cut; the nature of her limit; what she is; whether the storm-wall can be crossed.

## Headings added inside filled chapters

- **GM only: Language** (ch. 24) — glossary, sound-inventories, and regular sound-change. The player how-to (pick, make, glue) stays in ch. 05. Continent-name gloss is in ch. 14.
- **What the names mean** (ch. 14) — first-read gloss of the continents, the Awakening Tree, the Isle, and the three corners.
- **Hearth-Mark / Mixed Ancestry** (ch. 04) — stock compensation and SRD mix; Yumboe GM-leave, full Kind.
- **Turning-Week in a city / Questions a warden gets asked** (ch. 06) — nested hearths; unTurned is not Kept.
- **The sentence at the mainland lintel** (ch. 08) — Open Table vs witnessed citizenship.
- **Houses after the Slide** (ch. 09) — Holding Desk, Standing Trade, Reckoned Offices, Pourers, Walled Book / Inner Close; Protectors as public rumour.
- **Named water and travel** (ch. 16) — Old Crossing, West Water, Rain-Wall, four rivers, travel table. Deep forage ecology stays thin.
- **The Other Count** (ch. 18) — Closing, Two Papers, Grey Summer, Thaw-Break, Hinge Hush; Closed Seat as origin-gate.
- **Secrets and reveals** (ch. 24) — when the fire is caught; hidden Phoenix agency; Isolated Fall opening at Harrow's Green.
- **How a place speaks / the second name** (ch. 05) — four tones; byname or house-name.
- **Stock kitchens** (ch. 04) — glances. Not Kind-nations.
- **The hour someone is Struck / the watch and the cohort** (ch. 10) — care before the argument; a bench until morning; a send, not an army.
- **Fellowships, and the work** (ch. 13) — mill, hull, road. Not a fourth ticket. A domain is a job.
- **Burial, the guest-meal, what a house keeps** (ch. 12).
- **What the year feels like / the sky from the ground** (ch. 15) — one ground. This world has no planes.
- **The twelve seats** (ch. 19 and ch. 20) — named, or refused. Rothallo is the Inner Close.
- **The Mill-hold, the First Bowl, Nelath** (ch. 21) — sick-Tree, guest-grove, road-end.
- **Known Map and overlays** (ch. 17) — notes place the marks. Vaelhesk has no settlement dot.

## How to update

1. Find the chapter in the table (or in `chapters/`).
2. Replace a **Not yet written.** block, or add under the heading that already exists.
3. Run `python3 build_world_book.py`.
4. Do not rename files or reorder the spine to make a new idea fit. If something truly has no home, add a reserved heading *inside* the nearest chapter and note it here.
