#!/usr/bin/env python3
"""Overlay canonical labels on the Maiethlir city sheet.

The painting is a new city chart, not a crop of Sacred Core. Placement
and names come from the Maiethlir note. The image model was not asked
to write. Rebuild:

    python3 "14 - Assets/Maps/label_maiethlir_city.py"

West is left. The Core-thaw runs west; inside the old flood-wall the
reach is the Slow Water, and the Tree stands on it. The Loft Row is the
one street from that Tree to the tablet-hall. Grove Bank, Down Gate, and
Wall Path are approaches. No capital star. The First Seat stays in the
wood and is not marked. Maiethvael's seat is not named.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Maiethlir-City-Atlas.png"
OUTPUT = ROOT / "Maiethlir-City-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_BOLD_ITALIC = FONT_DIR / "LiberationSerif-BoldItalic.ttf"

# Light city parchment: dark iron-gall with a pale halo, so type reads
# on roofs and on the river. Not the cream-on-dark used for the regional masters.
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


def hall_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """A long hall, deliberately unlike a capital star."""
    x, y = xy
    draw.rectangle((x - 14, y - 7, x + 14, y + 7), fill=HALO)
    draw.rectangle((x - 12, y - 5, x + 12, y + 5), fill=MARK)
    draw.rectangle((x - 4, y - 2, x + 4, y + 2), fill=HALO)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1152, 864):
        raise SystemExit(f"Expected 1152×864 Maiethlir city master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 28)
    place = font(SERIF_BOLD, 20)
    water = font(SERIF_BOLD_ITALIC, 20)

    halo_text(ink, (168, 748), "Maiethlir", title, TYPE)

    # Downstream, west, where the river leaves the flood-wall. Nothing
    # beyond this gate is Maiethvael's seat.
    leader(ink, (214, 418), (128, 362))
    halo_text(ink, (116, 362), "Down Gate", place, TYPE, anchor="rm")

    # Upstream path, east, toward the snow that feeds the thaw. Not the Noon Pass.
    leader(ink, (948, 248), (1048, 176))
    halo_text(ink, (1060, 176), "Wall Path", place, TYPE, anchor="lm")

    # The way from the wood. The road is outside the wall. The house on
    # that road stays unnamed; the First Seat is not in this city.
    leader(ink, (524, 118), (360, 78))
    halo_text(ink, (348, 78), "Grove Bank", place, TYPE, anchor="rm")

    # Civic Hand on the slow reach. The leader touches the painted canopy,
    # not the neighbouring roof. No ring that could be read as Thaeloren,
    # and no capital star.
    leader(ink, (498, 348), (330, 308))
    halo_text(ink, (318, 308), "The Tree", place, TYPE, anchor="rm")

    # The other end of the same street, on the hall side of the row, inside the wall.
    hall_mark(ink, (616, 222))
    leader(ink, (630, 214), (748, 148))
    halo_text(ink, (760, 148), "Tablet-hall", place, TYPE, anchor="lm")

    # The street between the Tree and the hall. The only district tension.
    leader(ink, (534, 268), (392, 228))
    halo_text(ink, (380, 228), "Loft Row", place, TYPE, anchor="rm")

    # The ford and mill-reach inside the wall, not a second name for the whole river.
    halo_text(ink, (560, 492), "Slow Water", water, TYPE_WATER)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
