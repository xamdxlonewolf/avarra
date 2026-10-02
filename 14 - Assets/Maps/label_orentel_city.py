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

    halo_text(ink, (168, 760), "Orentel", title, TYPE)

    # Open pasture behind the Rise, where the beasts are. Not the roofs.
    leader(ink, (158, 248), (130, 172))
    halo_text(ink, (130, 148), "Inland yard", place, TYPE)

    # The hill the Tree stands on. Short leader into the canopy's ground,
    # so the line does not stop on the neighbouring roof.
    leader(ink, (500, 158), (392, 88))
    halo_text(ink, (380, 88), "The Rise", place, TYPE, anchor="rm")

    # Ordinary civic canopy. Not Thaeloren's ring, and not a capital star.
    leader(ink, (530, 118), (620, 64))
    halo_text(ink, (632, 64), "The Tree", place, TYPE, anchor="lm")

    # The walked street from that free Hand down toward the held berths.
    leader(ink, (655, 355), (500, 318))
    halo_text(ink, (488, 318), "The Drop", place, TYPE, anchor="rm")

    # Lesser inner landing, upstream of the outer berths. Not a second city.
    quay_mark(ink, (508, 488))
    leader(ink, (496, 488), (360, 548))
    halo_text(ink, (348, 548), "Hallowquay", place, TYPE, anchor="rm")

    # The Salt Walk's old landing, below the Rise.
    quay_mark(ink, (748, 508))
    leader(ink, (760, 516), (900, 590))
    halo_text(ink, (912, 590), "First Quay", place, TYPE, anchor="lm")

    # North-side quay. The long shed is not the government.
    quay_mark(ink, (868, 312))
    leader(ink, (880, 304), (1004, 248))
    halo_text(ink, (1016, 248), "The Third", place, TYPE, anchor="lm")

    # A desk on that quay's town end. Not a crown, and not on the Rise.
    house_mark(ink, (748, 276))
    leader(ink, (736, 270), (640, 214))
    halo_text(ink, (628, 214), "White Note", place, TYPE, anchor="rm")

    # Inland boats. Trenledd's seat stays off this sheet.
    halo_text(ink, (118, 430), "Chart mouth", place, TYPE_WATER)

    # The sail in from the Hinge Shore. No far-shore city is named.
    halo_text(ink, (1010, 430), "Crossing-mouth", place, TYPE_WATER)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
