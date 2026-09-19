#!/usr/bin/env python3
"""Overlay canonical labels on the selected Waiting Vale atlas painting.

The painting supplies texture only. Placement and names come from Named
Ground, the Known Map schematic, the R8 prompt, and the Eolvaeth note.
Rebuild:

    python3 "14 - Assets/Maps/label_waiting_vale_atlas.py"

West is left. The fold sits behind a sliver of east-facing coast. Two
tracks meet at a spring; that water is a site, not a mile-shrine. The
vale is area-type. Eolvaeth is a pilgrim-edge, not a capital. Harrow's
canopy is out of sight and is neither drawn nor named.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Waiting-Vale-Atlas.png"
OUTPUT = ROOT / "Waiting-Vale-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF = FONT_DIR / "LiberationSerif-Regular.ttf"
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "LiberationSerif-Italic.ttf"

TYPE = (236, 226, 196)
TYPE_MUTED = (220, 208, 176)
TYPE_WATER = (214, 228, 230)
STROKE = (28, 22, 14)
MARK = (28, 24, 16)
MARK_RING = (236, 226, 200)


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
        stroke_fill=STROKE,
    )


def leader(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int]) -> None:
    draw.line((start, end), fill=MARK_RING, width=3)
    draw.line((start, end), fill=STROKE, width=1)


def settlement_dot(draw: ImageDraw.ImageDraw, xy: tuple[int, int], radius: int = 4) -> None:
    """A plain pilgrim-town mark. Never a capital star."""
    x, y = xy
    draw.ellipse(
        (x - radius - 2, y - radius - 2, x + radius + 2, y + radius + 2),
        fill=MARK_RING,
    )
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=MARK)


def spring_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """A small pool, deliberately unlike a settlement or Tree-ring."""
    x, y = xy
    draw.ellipse((x - 9, y - 6, x + 9, y + 6), fill=MARK_RING)
    draw.ellipse((x - 7, y - 4, x + 7, y + 4), fill=MARK)
    draw.ellipse((x - 4, y - 2, x + 4, y + 2), fill=TYPE_WATER)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Waiting Vale master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 32)
    subtitle = font(SERIF_ITALIC, 15)
    place_f = font(SERIF_BOLD, 19)
    caption_f = font(SERIF, 13)
    note = font(SERIF_ITALIC, 13)

    # Area-type for the fold itself. The wait is the town; this is not a
    # capital title sitting on a starred seat.
    halo_text(ink, (720, 148), "THE WAITING VALE", title, TYPE)
    halo_text(ink, (720, 178), "Eolvaeth country", subtitle, TYPE_MUTED, stroke=2)

    # The spring is the vale's reason: two tracks meet at the water.
    # Site-mark on the painted pool, not a shrine-stone and not a Tree.
    spring_mark(ink, (752, 506))
    leader(ink, (752, 506), (612, 456))
    halo_text(ink, (600, 448), "The Spring", place_f, TYPE, anchor="rm")
    halo_text(ink, (600, 467), "not a stone", caption_f, TYPE_MUTED, anchor="rm", stroke=2)

    # Eolvaeth is the pilgrim-edge square around the gift-hall. A plain
    # town mark only: no capital star, no Thaeloren canopy-ring. Sit the
    # name just south of the camp-streets so the coast sliver stays
    # unnamed. The live-front luck stays out of sight further inland.
    settlement_dot(ink, (786, 556))
    leader(ink, (786, 556), (800, 668))
    halo_text(ink, (800, 686), "Eolvaeth", place_f, TYPE, anchor="mm")
    halo_text(ink, (800, 705), "pilgrim-edge", caption_f, TYPE_MUTED, anchor="mm", stroke=2)

    footer = "Names from Named Ground. Painting is not a survey."
    halo_text(ink, (1192, 991), footer, note, TYPE_MUTED, stroke=2)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
