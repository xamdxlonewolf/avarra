#!/usr/bin/env python3
"""Overlay canonical labels on the selected Rain-Wall atlas painting.

The painting supplies texture only. Placement and names come from Named
Ground, the Known Map schematic, and the R3 prompt. Rebuild:

    python3 "14 - Assets/Maps/label_rain_wall_atlas.py"

West is left. Rain-Wall is the common name; Lirorn calls it the Thaw-Wall.
Noon Pass is the old high road; Shelf-gate is the lower road left after
the Break. These highlands are not Heskoren's spine and carry no
Kind-territory fill.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Rain-Wall-Atlas.png"
OUTPUT = ROOT / "Rain-Wall-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF = FONT_DIR / "LiberationSerif-Regular.ttf"
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "LiberationSerif-Italic.ttf"
SERIF_BOLD_ITALIC = FONT_DIR / "LiberationSerif-BoldItalic.ttf"

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


def pass_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """A small road-notch mark, deliberately unlike a settlement or border."""
    x, y = xy
    draw.line((x - 7, y - 4, x, y + 4, x + 7, y - 4), fill=MARK_RING, width=5)
    draw.line((x - 7, y - 4, x, y + 4, x + 7, y - 4), fill=MARK, width=2)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Rain-Wall master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 32)
    subtitle = font(SERIF_ITALIC, 15)
    region = font(SERIF_BOLD_ITALIC, 24)
    place_f = font(SERIF_BOLD, 19)
    caption_f = font(SERIF, 13)
    note = font(SERIF_ITALIC, 13)

    # Rain-Wall is the common atlas name. Lirorn's Thaw-Wall remains a local
    # secondary handle rather than replacing the mapped feature's name.
    halo_text(ink, (252, 74), "THE RAIN-WALL", title, TYPE)
    halo_text(ink, (252, 104), "Lirorn: the Thaw-Wall", subtitle, TYPE_MUTED, stroke=2)
    paste_rotated(canvas, "THE RAIN-WALL", region, TYPE, (941, 506), angle=72)

    # Noon Pass is the older, higher northern notch. Its pale water-line and
    # the road ribbon remain physical texture; the overlay adds no boundary.
    ink = ImageDraw.Draw(canvas)
    pass_mark(ink, (811, 361))
    leader(ink, (811, 361), (721, 292))
    halo_text(ink, (709, 282), "Noon Pass", place_f, TYPE, anchor="rm")
    halo_text(ink, (709, 301), "old high road", caption_f, TYPE_MUTED, anchor="rm", stroke=2)

    # Shelf-gate is the lower surviving traffic road, below the old notch.
    pass_mark(ink, (724, 716))
    leader(ink, (724, 716), (631, 673))
    halo_text(ink, (619, 665), "Shelf-gate", place_f, TYPE, anchor="rm")
    halo_text(ink, (619, 684), "lower shelf-road", caption_f, TYPE_MUTED, anchor="rm", stroke=2)

    footer = "Names from Named Ground. Painting is not a survey."
    halo_text(ink, (1192, 991), footer, note, TYPE_MUTED, stroke=2)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
