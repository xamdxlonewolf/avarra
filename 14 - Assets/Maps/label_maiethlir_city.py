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

    halo_text(ink, (150, 36), "Maiethlir", title, TYPE)

    # Downstream opening, where the road leaves the wall onto the bridge.
    leader(ink, (150, 560), (60, 470))
    halo_text(ink, (60, 470), "Down Gate", place, TYPE)

    # Upstream road on the east bank, where the reach leaves the wall.
    leader(ink, (1050, 450), (960, 320))
    halo_text(ink, (960, 320), "Wall Path", place, TYPE)

    # The road in the north gate, where it leaves toward the wood.
    leader(ink, (540, 130), (720, 50))
    halo_text(ink, (720, 50), "Grove Bank", place, TYPE)

    # Civic Hand on the north bank. No capital star.
    leader(ink, (340, 300), (160, 180))
    halo_text(ink, (160, 180), "The Tree", place, TYPE)

    # Long hall one street east of the Tree.
    hall_mark(ink, (650, 320))
    leader(ink, (650, 320), (880, 220))
    halo_text(ink, (880, 220), "Tablet-hall", place, TYPE)

    # The street between the Tree and the hall. Not the canopy.
    halo_text(ink, (500, 420), "Loft Row", place, TYPE)

    # The wide reach inside the wall.
    halo_text(ink, (780, 500), "Slow Water", water, TYPE_WATER)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
