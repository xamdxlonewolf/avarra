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
    if base.size != (1280, 720):
        raise SystemExit(f"Expected 1280×720 Orentel city master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 28)
    place = font(SERIF_BOLD, 20)

    halo_text(ink, (180, 660), "Orentel", title, TYPE)

    # Open pasture behind the Rise. Small beside the roof-mass.
    leader(ink, (175, 180), (175, 118))
    halo_text(ink, (210, 100), "Inland yard", place, TYPE, anchor="lm")

    # The small square the Tree stands on. The city around it is the larger half.
    leader(ink, (500, 235), (400, 165))
    halo_text(ink, (388, 165), "The Rise", place, TYPE, anchor="rm")

    # Ordinary civic canopy in that square. Not a capital star.
    leader(ink, (575, 210), (680, 150))
    halo_text(ink, (692, 150), "The Tree", place, TYPE, anchor="lm")

    # The street from the free Hand down toward the held berths.
    leader(ink, (545, 340), (410, 300))
    halo_text(ink, (398, 300), "The Drop", place, TYPE, anchor="rm")

    # Lesser inner landing, on the upstream wharf, not in the channel.
    quay_mark(ink, (430, 512))
    leader(ink, (415, 518), (230, 575))
    halo_text(ink, (218, 575), "Hallowquay", place, TYPE, anchor="rm")

    # The old landing on the long south waterfront, below the Rise.
    quay_mark(ink, (620, 530))
    leader(ink, (635, 545), (790, 610))
    halo_text(ink, (802, 610), "First Quay", place, TYPE, anchor="lm")

    # North-side waterfront. On the shore, not out among the hulls.
    quay_mark(ink, (868, 238))
    leader(ink, (882, 232), (1048, 175))
    halo_text(ink, (1060, 175), "The Third", place, TYPE, anchor="lm")

    # A desk just inland of that north quay. Not a crown, and not on the Rise.
    house_mark(ink, (830, 230))
    leader(ink, (815, 225), (720, 200))
    halo_text(ink, (708, 200), "White Note", place, TYPE, anchor="rm")

    # Inland boats. Trenledd's seat stays off this sheet.
    halo_text(ink, (155, 400), "Chart mouth", place, TYPE_WATER)

    # The sail in from the Hinge Shore. No far-shore city is named.
    halo_text(ink, (1080, 360), "Crossing-mouth", place, TYPE_WATER)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
