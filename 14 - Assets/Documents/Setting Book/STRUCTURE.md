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
| 16-climate-and-ecology.md | V · The Lands | Climate, Ecology, and Travel | reserved |
| 17-maps.md | V · The Lands | Maps | reserved |
| 18-the-ages.md | VI · The Ages | The Ages | filled |
| 19-the-fifteen-powers.md | VII · Powers and Places | The Fifteen Powers | filled |
| 20-gazetteer.md | VII · Powers and Places | Gazetteer | filled |
| 21-other-places.md | VII · Powers and Places | Other Places | reserved |
| 22-faces-of-the-turning.md | VIII · Faces | Faces of the Turning | reserved |
| 23-at-the-table.md | IX · At the Table | Playing in the Turning | reserved |
| 24-gm-canon.md | X · For the GM | GM Canon | filled |

## Reserved holes inside filled chapters

These stay where they are. Do not promote them to new chapters unless the spine is deliberately revised.

- **The Twelve** (ch. 19) — named stubs; seats unnamed on purpose. Fill texture in place.
- **Gazetteer types** (ch. 20) — leftover types listed; unused ones wait in ch. 21.
- **Open questions** (ch. 24) — who made the First Cut; the nature of her limit; what she is; whether the storm-wall can be crossed.

## How to update

1. Find the chapter in the table (or in `chapters/`).
2. Replace a **Not yet written.** block, or add under the heading that already exists.
3. Run `python3 build_world_book.py`.
4. Do not rename files or reorder the spine to make a new idea fit. If something truly has no home, add a reserved heading *inside* the nearest chapter and note it here.
