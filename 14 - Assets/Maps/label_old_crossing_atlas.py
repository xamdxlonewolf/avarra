#!/usr/bin/env python3
"""Overlay canonical labels on the selected Old Crossing atlas painting.

The painting supplies texture only. Placement and names come from Named
Ground, the Known Map schematic, and the R1 prompt. Rebuild:

    python3 "14 - Assets/Maps/label_old_crossing_atlas.py"

West is left. Orentel sits at the large estuary on Strandoren's eastern
face. The Hinge Shore is the opposite Maiethorn coast and receives area
type rather than an invented seat. The Hush-rate is a crossing charge,
not a political border.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Old-Crossing-Atlas.png"
OUTPUT = ROOT / "Old-Crossing-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF = FONT_DIR / "LiberationSerif-Regular.ttf"
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "LiberationSerif-Italic.ttf"
SERIF_BOLD_ITALIC = FONT_DIR / "LiberationSerif-BoldItalic.ttf"

TYPE = (236, 226, 196)
TYPE_MUTED = (220, 208, 176)
TYPE_WATER = (214, 228, 230)
STROKE = (28, 22, 14)
MARK = (28, 24, 16)
MARK_RING = (236, 226, 200)
RATE_PLATE = (38, 45, 42, 210)


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


def settlement_dot(draw: ImageDraw.ImageDraw, xy: tuple[int, int], radius: int = 5) -> None:
    x, y = xy
    draw.ellipse(
        (x - radius - 2, y - radius - 2, x + radius + 2, y + radius + 2),
        fill=MARK_RING,
    )
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=MARK)


def leader(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int]) -> None:
    draw.line((start, end), fill=MARK_RING, width=3)
    draw.line((start, end), fill=STROKE, width=1)


def rate_cartouche(
    canvas: Image.Image,
    centre: tuple[int, int],
    heading_font: ImageFont.FreeTypeFont,
    caption_font: ImageFont.FreeTypeFont,
) -> None:
    """A docket-like plate: explicitly a charge, with no border line."""
    width, height = 194, 58
    x = centre[0] - width // 2
    y = centre[1] - height // 2
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle(
        (1, 1, width - 2, height - 2),
        radius=6,
        fill=RATE_PLATE,
        outline=MARK_RING,
        width=2,
    )
    halo_text(draw, (width // 2, 20), "HUSH-RATE", heading_font, TYPE, stroke=2)
    halo_text(
        draw,
        (width // 2, 42),
        "crossing charge",
        caption_font,
        TYPE_MUTED,
        stroke=2,
    )
    canvas.paste(layer, (x, y), layer)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Old Crossing master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 32)
    subtitle = font(SERIF_ITALIC, 15)
    region = font(SERIF_BOLD_ITALIC, 24)
    place_f = font(SERIF_BOLD, 20)
    rate_f = font(SERIF_BOLD, 17)
    caption_f = font(SERIF, 13)
    note = font(SERIF_ITALIC, 13)

    # The chart's name sits in open northern water between the two old shores.
    halo_text(ink, (768, 76), "THE OLD CROSSING", title, TYPE_WATER)
    halo_text(ink, (768, 106), "the oldest trade route", subtitle, TYPE_MUTED, stroke=2)

    # Orentel is the nucleated salt-city at the large western estuary. It gets
    # a plain settlement dot, never a capital star.
    settlement_dot(ink, (535, 620))
    leader(ink, (535, 620), (492, 579))
    halo_text(ink, (480, 571), "Orentel", place_f, TYPE, anchor="rm")

    # The opposite coast is a polity-region with an unnamed seat. Area type
    # follows the coast instead of promoting a painted quay cluster.
    paste_rotated(canvas, "THE HINGE SHORE", region, TYPE, (1218, 440), angle=69)

    # The peace survives as a docketed charge on traffic. A compact plate in
    # the channel communicates a rate without drawing anything border-like.
    rate_cartouche(canvas, (855, 728), rate_f, caption_f)

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
