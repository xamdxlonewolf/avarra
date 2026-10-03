#!/usr/bin/env python3
"""Overlay canonical labels on the Orentel city sheet.

The painting is a new harbour chart, not a crop of Chart-run or the Old
Crossing. Placement and names come from the Orentel note. The image model
was not asked to write. Rebuild:

    python3 "14 - Assets/Maps/label_orentel_city.py"

West is left. The estuary opens east. The Tree is on the Rise. The Drop
is the one street from that free Hand down to the held berths. The White
Note is a desk on the Third, north side, not a crown. No capital star.
Denlad is not in this city.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Orentel-City-Atlas.png"
OUTPUT = ROOT / "Orentel-City-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"

TYPE = (48, 32, 18)
TYPE_WATER = (28, 48, 62)
HALO = (244, 236, 214)
MARK = (42, 28, 16)


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def halo_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    typeface: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    *,
    anchor: str = "mm",
    stroke: int = 3,
) -> None:
    draw.text(
        xy,
        text,
        font=typeface,
        fill=fill,
        anchor=anchor,
        stroke_width=stroke,
        stroke_fill=HALO,
    )


def leader(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int]) -> None:
    draw.line((start, end), fill=HALO, width=3)
    draw.line((start, end), fill=MARK, width=1)


def quay_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """A small landing, deliberately unlike a settlement or a crown."""
    x, y = xy
    draw.rectangle((x - 9, y - 4, x + 9, y + 4), fill=HALO)
    draw.rectangle((x - 7, y - 2, x + 7, y + 2), fill=MARK)
    draw.line((x - 9, y - 7, x - 9, y + 7), fill=HALO, width=4)
    draw.line((x - 9, y - 6, x - 9, y + 6), fill=MARK, width=2)


def house_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """A desk-house, deliberately unlike a capital star."""
    x, y = xy
    roof = ((x, y - 8), (x + 7, y - 1), (x - 7, y - 1))
    draw.polygon(roof, fill=HALO)
    draw.polygon(((x, y - 6), (x + 5, y - 1), (x - 5, y - 1)), fill=MARK)
    draw.rectangle((x - 5, y - 1, x + 5, y + 7), fill=HALO)
    draw.rectangle((x - 3, y, x + 3, y + 5), fill=MARK)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1152, 864):
        raise SystemExit(f"Expected 1152×864 Orentel city master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 28)
    place = font(SERIF_BOLD, 20)

    halo_text(ink, (140, 48), "Orentel", title, TYPE)

    # Pasture north of the roofs. The inland edge.
    leader(ink, (540, 145), (400, 90))
    halo_text(ink, (388, 90), "Inland yard", place, TYPE, anchor="rm")

    # Open pavement of the square, south of the Hand, so the leader stays off the canopy.
    leader(ink, (430, 448), (300, 470))
    halo_text(ink, (288, 470), "The Rise", place, TYPE, anchor="rm")

    # The Hand in that square.
    leader(ink, (388, 378), (500, 330))
    halo_text(ink, (512, 330), "The Tree", place, TYPE, anchor="lm")

    # The one street from the square down to the berths. The far end sits mid-road.
    leader(ink, (640, 508), (520, 570))
    halo_text(ink, (508, 570), "The Drop", place, TYPE, anchor="rm")

    # Lesser inner pier, on its deck. West of the long landing.
    quay_mark(ink, (770, 450))
    leader(ink, (770, 450), (700, 390))
    halo_text(ink, (688, 390), "Hallowquay", place, TYPE, anchor="rm")

    # Long south landing. Open deck, clear of the boats.
    quay_mark(ink, (920, 590))
    leader(ink, (920, 590), (1000, 690))
    halo_text(ink, (1040, 710), "First Quay", place, TYPE, anchor="mm")

    # North-side quay, on the pier deck.
    quay_mark(ink, (910, 232))
    leader(ink, (926, 220), (1020, 168))
    halo_text(ink, (1032, 168), "The Third", place, TYPE, anchor="lm")

    # Desk-house on the pier. The name stays on the sheet.
    house_mark(ink, (966, 372))
    leader(ink, (978, 360), (1000, 300))
    halo_text(ink, (1012, 300), "White Note", place, TYPE, anchor="lm")

    halo_text(ink, (160, 200), "Chart mouth", place, TYPE_WATER)
    halo_text(ink, (980, 140), "Crossing-mouth", place, TYPE_WATER)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
