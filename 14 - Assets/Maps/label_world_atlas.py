#!/usr/bin/env python3
"""Overlay Named Ground labels on the selected world atlas painting.

The painting stays the geographic texture. Names come from Named Ground
and the Known Map schematic only — four lands and the two waters, west
to east. Extra painted isles, decorative stars, and weather stay unnamed.
Rebuild:

    python3 "14 - Assets/Maps/label_world_atlas.py"

West is left. East is right. No fifth land. No graft on Kumbaan.
The Rain-Wall is Maiethorn's spine, not Heskoren's highlands.
Seas sit in the middle of their water. The storm-wall follows
Kumbaan's foam ring.
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "The-Turning-World-Atlas.png"
OUTPUT = ROOT / "The-Turning-World-Atlas-Labeled.png"

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
    w, h = measure(typeface, text)
    pad = stroke * 2 + 10
    layer = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    halo_text(
        draw,
        (layer.size[0] // 2, layer.size[1] // 2),
        text,
        typeface,
        fill,
        stroke=stroke,
    )
    rotated = layer.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    canvas.paste(
        rotated,
        (centre[0] - rotated.size[0] // 2, centre[1] - rotated.size[1] // 2),
        rotated,
    )


def paste_along_arc(
    canvas: Image.Image,
    text: str,
    typeface: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    cx: float,
    cy: float,
    radius: float,
    start_deg: float,
    end_deg: float,
    stroke: int = 3,
    tracking: float = 1.12,
) -> None:
    """Place glyphs on a circular arc.

    Angles are mathematical degrees (0 = east, counterclockwise).
    Screen y is inverted so 90° is north. Letters stand outside the
    arc with the baseline toward the centre (rainbow / ring type).
    """
    widths = [glyph_width(typeface, ch) * tracking for ch in text]
    total = sum(widths)
    if total <= 0:
        return
    start = math.radians(start_deg)
    end = math.radians(end_deg)
    walked = 0.0
    for char, width in zip(text, widths, strict=True):
        mid = (walked + width / 2) / total
        theta = start + (end - start) * mid
        x = cx + radius * math.cos(theta)
        y = cy - radius * math.sin(theta)
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


def paste_along_path(
    canvas: Image.Image,
    text: str,
    typeface: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    points: list[tuple[float, float]],
    stroke: int = 3,
    tracking: float = 1.08,
) -> None:
    """Place glyphs along a polyline. Reading follows the point order."""
    if len(points) < 2:
        return
    segs: list[tuple[float, float, float, float, float, float]] = []
    total = 0.0
    for (x0, y0), (x1, y1) in zip(points, points[1:], strict=False):
        length = math.hypot(x1 - x0, y1 - y0)
        segs.append((x0, y0, x1, y1, length, total))
        total += length
    if total <= 0:
        return

    widths = [glyph_width(typeface, ch) * tracking for ch in text]
    text_w = sum(widths)
    walked = 0.0
    for char, width in zip(text, widths, strict=True):
        target = ((walked + width / 2) / text_w) * total
        x0 = y0 = x1 = y1 = 0.0
        length = 1.0
        base = 0.0
        for x0, y0, x1, y1, length, base in segs:
            if target <= base + length or (x0, y0, x1, y1) == segs[-1][:4]:
                break
        t = 0.0 if length == 0 else min(1.0, max(0.0, (target - base) / length))
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        angle = math.degrees(math.atan2(y0 - y1, x1 - x0))
        if char != " ":
            paste_rotated(
                canvas,
                char,
                typeface,
                fill,
                (int(round(x)), int(round(y))),
                angle,
                stroke,
            )
        walked += width


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 world master, got {base.size}")

    canvas = base.copy()

    title = font(SERIF_BOLD, 34)
    subtitle = font(SERIF_ITALIC, 16)
    land = font(SERIF_BOLD, 42)
    land_small = font(SERIF_BOLD, 28)
    caption = font(SERIF_ITALIC, 17)
    water = font(SERIF_BOLD_ITALIC, 32)
    crossing = font(SERIF_BOLD_ITALIC, 22)
    feature = font(SERIF_ITALIC, 19)
    rain = font(SERIF_ITALIC, 18)
    note = font(SERIF_ITALIC, 13)

    ink = ImageDraw.Draw(canvas)

    # Quiet north water — sheet title, not a fifth land.
    halo_text(ink, (520, 52), "THE TURNING", title, TYPE, stroke=3)
    halo_text(ink, (520, 82), "the Known Lands", subtitle, TYPE_MUTED, stroke=2)

    # Kumbaan — small storm-walled isle, upper left. Name sits below the
    # ring. The storm-wall follows the circular foam, not a straight slug.
    halo_text(ink, (152, 268), "Kumbaan", land_small, TYPE, stroke=3)
    halo_text(ink, (152, 294), "the Sundering Isle", caption, TYPE_MUTED, stroke=2)
    # Crown the foam ring. A short top arc keeps the letters leaning
    # with the wall instead of stacking down the west coast.
    paste_along_arc(
        canvas,
        "the storm-wall",
        feature,
        TYPE_WATER,
        cx=152,
        cy=132,
        radius=88,
        start_deg=160,
        end_deg=20,
        stroke=2,
        tracking=1.16,
    )

    # Heskoren — south-west frontier, distinctly south of the Old World pair.
    halo_text(ink, (300, 900), "HESKOREN", land, TYPE, stroke=3)
    halo_text(ink, (300, 932), "the Sundered Reach", caption, TYPE_MUTED, stroke=2)

    # West Water — the wide emptiness between Heskoren and Strandoren.
    # Stay in the open southern basin; do not start on Heskoren's land.
    paste_along_path(
        canvas,
        "the West Water",
        water,
        TYPE_WATER,
        [
            (538, 778),
            (590, 760),
            (650, 752),
            (715, 762),
            (768, 782),
        ],
        stroke=3,
        tracking=1.03,
    )

    # Strandoren — maritime Old-World neighbour, centre of the sheet.
    halo_text(ink, (800, 158), "STRANDOREN", land, TYPE, stroke=3)
    halo_text(ink, (800, 188), "the Shore-lands", caption, TYPE_MUTED, stroke=2)

    # Old Crossing — the crowded strait between Strandoren and Maiethorn.
    # Follow the water down the channel; do not float in the north ocean.
    paste_along_path(
        canvas,
        "the Old Crossing",
        crossing,
        TYPE_WATER,
        [
            (1096, 238),
            (1100, 278),
            (1102, 318),
            (1094, 358),
            (1082, 398),
            (1068, 438),
        ],
        stroke=2,
        tracking=1.02,
    )

    # Maiethorn — far east, largest old land. Name north of the wet west.
    halo_text(ink, (1236, 228), "MAIETHORN", land, TYPE, stroke=3)
    halo_text(ink, (1236, 258), "the Motherland", caption, TYPE_MUTED, stroke=2)

    # Rain-Wall — Maiethorn's north–south divide, on the ridge.
    paste_along_path(
        canvas,
        "the Rain-Wall",
        rain,
        TYPE,
        [
            (1364, 360),
            (1370, 430),
            (1376, 510),
            (1386, 590),
            (1394, 660),
        ],
        stroke=2,
        tracking=1.10,
    )

    # Compass sits bottom-centre; keep the disclaimer off it and off Heskoren.
    footer = "Names from Named Ground. Painting is not a survey."
    halo_text(ink, (1188, 996), footer, note, TYPE_MUTED, stroke=2)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
