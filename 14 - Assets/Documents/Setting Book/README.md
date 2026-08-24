# The Turning — World Book

A living setting book. The **spine is locked** in `STRUCTURE.md`. New work fills a reserved chapter or a *Not yet written* box; it does not invent a parallel outline.

HTML is the reading copy. PDF is the notes copy.

## Files

| File | What it is |
|---|---|
| **STRUCTURE.md** | Locked table of contents. Status: filled / partial / reserved. |
| **chapters/** | One markdown file per chapter. This is what you edit. |
| **The-Turning-World-Book.html** | The book. Searchable. Clickable contents. Reserved chapters marked *to write*. |
| **The-Turning-World-Book.pdf** | Same book, paginated, for annotation. |
| `build_world_book.py` | Rebuilds HTML and PDF from `STRUCTURE.md` + `chapters/`. |

The vault notes remain canonical. This folder is the reading copy.

## How to update

**Only when the user asks for an updated world book.** Do not fold vault work into this book as epics finish.

1. Open `STRUCTURE.md` and find the chapter.
2. Edit `chapters/<file>`. Replace a **Not yet written.** block, or add under a heading that already exists.
3. Run:

```bash
python3 "14 - Assets/Documents/Setting Book/build_world_book.py"
```

4. Do not rename files or reorder the spine to make a new idea fit. If something has no home, add a reserved heading *inside* the nearest chapter and note it in STRUCTURE.

## Books

| Book | What's in it |
|---|---|
| I · What This World Is | Using this book, the world in brief, Kind and Condition |
| II · Peoples | Conditions, Kinds, language and naming |
| III · The Tree and the Faiths | Tree, Motherfaith, five faiths, orders and houses |
| IV · How People Live | Law, economy, daily life, Tithe-guilds |
| V · The Lands | Continents, calendar, **climate (to write)**, **maps (to write)** |
| VI · The Ages | Two clocks, Walking Years, First Cut, Years of Hands |
| VII · Powers and Places | Fifteen powers, gazetteer, **other places (to write)** |
| VIII · Faces | **People (to write)** |
| IX · At the Table | **Play material (to write)** |
| X · For the GM | Keystone canon |
