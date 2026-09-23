#!/usr/bin/env python3
"""Overlay the two canonical labels on the selected Kumbaan atlas painting.

The painting supplies texture only. Names come from Named Ground, the Known
Map schematic, and the C4 prompt. Rebuild:

    python3 "14 - Assets/Maps/label_kumbaan_atlas.py"

Kumbaan is the isle. The storm-wall is the complete girdle of cloud, current,
and reef around it. Nothing marks a graft, city, settlement, harbour, or Tree.
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Kumbaan-Atlas.png"
OUTPUT = ROOT / "Kumbaan-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "LiberationSerif-Italic.ttf"
SERIF_BOLD_ITALIC = FONT_DIR / "LiberationSerif-BoldItalic.ttf"

TYPE = (236, 226, 196)
TYPE_MUTED = (220, 208, 176)
TYPE_WATER = (214, 228, 230)
STROKE = (28, 22, 14)


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


def glyph_width(typeface: ImageFont.FreeTypeFont, char: str) -> int:
    if char == " ":
        return max(6, measure(typeface, "n")[0] // 2)
    return max(1, measure(typeface, char)[0])


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


def paste_along_arc(
    canvas: Image.Image,
    text: str,
    typeface: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    centre: tuple[float, float],
    radius: float,
    start_deg: float,
    end_deg: float,
    *,
    stroke: int = 3,
    tracking: float = 1.1,
) -> None:
    """Place upright glyphs along a circular arc."""
    widths = [glyph_width(typeface, char) * tracking for char in text]
    total = sum(widths)
    start = math.radians(start_deg)
    end = math.radians(end_deg)
    walked = 0.0

    for char, width in zip(text, widths, strict=True):
        mid = (walked + width / 2) / total
        theta = start + (end - start) * mid
        x = centre[0] + radius * math.cos(theta)
        y = centre[1] - radius * math.sin(theta)
        rotation = 90.0 - math.degrees(theta)
        if char != " ":
            paste_rotated(
                canvas,
                char,
                typeface,
                fill,
                (int(round(x)), int(round(y))),
                rotation,
                stroke,
            )
        walked += width


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Kumbaan master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    isle = font(SERIF_BOLD, 48)
    wall = font(SERIF_BOLD_ITALIC, 25)

    # The island gets land-type only: no settlement marker and no inferred
    # interior name.
    halo_text(ink, (768, 520), "KUMBAAN", isle, TYPE, stroke=4)

    # Follow the northern cloud-ring. This labels the complete girdle rather
    # than suggesting a border, passage, harbour, or break in the wall.
    paste_along_arc(
        canvas,
        "the storm-wall",
        wall,
        TYPE_WATER,
        centre=(768, 610),
        radius=506,
        start_deg=112,
        end_deg=68,
        stroke=3,
    )

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
