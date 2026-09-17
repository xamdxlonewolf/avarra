#!/usr/bin/env python3
"""Overlay canonical labels on the selected Rain-Shadow atlas painting.

The painting supplies texture only. Placement and names come from Named
Ground, the Known Map schematic, the R4 prompt, and the Ornsael / Dry
Stair notes. Rebuild:

    python3 "14 - Assets/Maps/label_rain_shadow_atlas.py"

West is left. The Rain-Wall's back occupies only the left edge. Ornsael
is a west-road well-town, not a capital. The Dry Stair climbs a different
rise toward nothing that is a Tree. The Well-wash is seasonal water, not
a civic river. These dry hills are not a Fox-nation.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Rain-Shadow-Atlas.png"
OUTPUT = ROOT / "Rain-Shadow-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF = FONT_DIR / "LiberationSerif-Regular.ttf"
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "LiberationSerif-Italic.ttf"

TYPE = (236, 226, 196)
TYPE_MUTED = (220, 208, 176)
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


def measure(typeface: ImageFont.FreeTypeFont, text: str) -> tuple[int, int]:
    bbox = typeface.getbbox(text)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def paste_rotated(
    canvas: Image.Image,
    text: str,
    typeface: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    centre: tuple[int, int],
    angle: float,
    stroke: int = 3,
) -> None:
    width, height = measure(typeface, text)
    pad = stroke * 2 + 10
    layer = Image.new("RGBA", (width + pad * 2, height + pad * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    halo_text(
        draw,
        (layer.width // 2, layer.height // 2),
        text,
        typeface,
        fill,
        stroke=stroke,
    )
    rotated = layer.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    canvas.paste(
        rotated,
        (centre[0] - rotated.width // 2, centre[1] - rotated.height // 2),
        rotated,
    )


def leader(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int]) -> None:
    draw.line((start, end), fill=MARK_RING, width=3)
    draw.line((start, end), fill=STROKE, width=1)


def settlement_dot(draw: ImageDraw.ImageDraw, xy: tuple[int, int], radius: int = 4) -> None:
    """A plain well-town mark. Never a capital star."""
    x, y = xy
    draw.ellipse(
        (x - radius - 2, y - radius - 2, x + radius + 2, y + radius + 2),
        fill=MARK_RING,
    )
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=MARK)


def stair_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """A small ascent mark, deliberately unlike a settlement or Tree."""
    x, y = xy
    steps = ((x - 9, y + 6, x + 9, y + 6), (x - 6, y, x + 6, y), (x - 3, y - 6, x + 3, y - 6))
    for x0, y0, x1, y1 in steps:
        draw.line((x0, y0, x1, y1), fill=MARK_RING, width=5)
        draw.line((x0, y0, x1, y1), fill=MARK, width=2)
    draw.line((x, y + 6, x, y - 6), fill=MARK_RING, width=4)
    draw.line((x, y + 6, x, y - 6), fill=MARK, width=2)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Rain-Shadow master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 32)
    subtitle = font(SERIF_ITALIC, 15)
    place_f = font(SERIF_BOLD, 19)
    caption_f = font(SERIF, 13)
    terrain = font(SERIF_ITALIC, 18)
    note = font(SERIF_ITALIC, 13)

    # Climate-type for the whole dry east. The left highlands are the
    # Rain-Wall's back, named only as orientation in the subtitle.
    halo_text(ink, (1248, 82), "THE RAIN-SHADOW", title, TYPE)
    halo_text(ink, (1248, 112), "east of the Rain-Wall", subtitle, TYPE_MUTED, stroke=2)

    # Ornsael is the west-road well-town with a young-for-the-continent Tree
    # beside the well. The dot sits on the well. Plain settlement mark:
    # not a capital, not Thaeloren's canopy-ring.
    settlement_dot(ink, (298, 678))
    leader(ink, (298, 678), (404, 598))
    halo_text(ink, (414, 588), "Ornsael", place_f, TYPE, anchor="lm")
    halo_text(ink, (414, 607), "well-town", caption_f, TYPE_MUTED, anchor="lm", stroke=2)

    # The Dry Stair is the climb on a different rise. The well-town at its
    # shoulder stays unnamed; the mark sits on the steps, not the houses.
    stair_mark(ink, (800, 728))
    leader(ink, (800, 728), (862, 742))
    halo_text(ink, (872, 734), "The Dry Stair", place_f, TYPE, anchor="lm")
    halo_text(ink, (872, 753), "not a Tree", caption_f, TYPE_MUTED, anchor="lm", stroke=2)

    # Seasonal hydrology, not a civic river and not a border. One name
    # along the painted wash; do not redraw the water as a dashed line.
    paste_rotated(canvas, "The Well-wash", terrain, TYPE, (1056, 552), angle=76, stroke=2)

    ink = ImageDraw.Draw(canvas)
    footer = "Names from Named Ground. Painting is not a survey."
    halo_text(ink, (1192, 991), footer, note, TYPE_MUTED, stroke=2)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
