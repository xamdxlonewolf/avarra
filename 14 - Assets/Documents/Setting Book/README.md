# The Turning — World Book

A compiled setting book covering the world as it stands through Epics 0–7 (foundations through settlements). Written as settled setting, not as a build log.

About **108,000 words** / **~280 PDF pages**. The HTML is the easier reading copy; the PDF is for highlights and margin notes.

## Files

| File | What it is |
|---|---|
| **The-Turning-World-Book.html** | The book. Open in a browser. Searchable. Clickable contents. Prints cleanly. |
| **The-Turning-World-Book.pdf** | The same book, paginated, for annotation (Preview, Acrobat, GoodNotes, iPad). |
| `build_world_book.py` | Regenerates HTML (and PDF, if Chrome is available) from the chapter markdown. |
| Chapter `.md` files | Source chapters used by the builder. Not the reading copy. |

The vault notes remain canonical. This folder is a reading copy for audit.

## Why HTML and PDF

- **HTML** — best for sitting down with the whole world: jump the contents, search a name, read on a laptop or tablet.
- **PDF** — best for notes: highlights, sticky comments, print with a wide right margin.
- **Word** — open the HTML in Word or Google Docs if you want threaded comments. A native `.docx` is not the reading copy; the book is prose, not a spreadsheet.
- **Excel** — a bad fit for this.

## Parts

1. The World in Brief
2. Becomings (Kind / Condition, the Tithe, all ten Conditions with rules)
3. Peoples (hearths, four custom Kinds, naming, the Old Tongue)
4. The Tree and the Faiths
5. How People Live (law, economy, daily life, guilds, three corners)
6. The Lands (four continents, the calendar)
7. The Ages (Walking Years, First Cut, Years of Hands, folklore)
8. Powers and Places (fifteen powers, playable squares, three seats)
9. GM Appendix (keystone canon — spoilers)

## Rebuild

```bash
python3 "14 - Assets/Documents/Setting Book/build_world_book.py"
```
