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


def _blend(canvas: Image.Image, x: int, y: int, pix: tuple[int, int, int, int]) -> None:
    if not (0 <= x < canvas.width and 0 <= y < canvas.height) or pix[3] == 0:
        return
    dst = canvas.getpixel((x, y))
    a = pix[3] / 255.0
    canvas.putpixel(
        (x, y),
        (
            int(dst[0] * (1 - a) + pix[0] * a),
            int(dst[1] * (1 - a) + pix[1] * a),
            int(dst[2] * (1 - a) + pix[2] * a),
            255,
        ),
    )


def warp_along_arc(
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
) -> None:
    """Bend a whole word onto a circular arc so the type itself curves."""
    width, height = measure(typeface, text)
    pad_x, pad_y = stroke + 10, stroke + 12
    strip = Image.new("RGBA", (width + pad_x * 2, height + pad_y * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(strip)
    halo_text(
        draw,
        (strip.size[0] // 2, strip.size[1] // 2),
        text,
        typeface,
        fill,
        stroke=stroke,
    )
    # Slight horizontal stretch so the warp does not crush counters.
    strip = strip.resize(
        (int(strip.size[0] * 1.15), strip.size[1]),
        Image.Resampling.BICUBIC,
    )
    sw, sh = strip.size
    src = strip.load()
    half = sh / 2
    r_min = radius - half - 2
    r_max = radius + half + 2
    samples = [start_deg + (end_deg - start_deg) * i / 8 for i in range(9)]
    xs: list[float] = []
    ys: list[float] = []
    for deg in samples:
        th = math.radians(deg)
        for r in (r_min, r_max):
            xs.append(cx + r * math.cos(th))
            ys.append(cy - r * math.sin(th))
    x0, x1 = int(min(xs) - 2), int(max(xs) + 3)
    y0, y1 = int(min(ys) - 2), int(max(ys) + 3)
    span = end_deg - start_deg
    if abs(span) < 1e-6:
        return

    def arc_t(theta_rad: float) -> float | None:
        deg = math.degrees(theta_rad)
        for lift in (0.0, 360.0, -360.0):
            t = (deg + lift - start_deg) / span
            if -0.03 <= t <= 1.03:
                return t
        return None

    for py in range(y0, y1):
        for px in range(x0, x1):
            dx = px - cx
            dy = cy - py
            r = math.hypot(dx, dy)
            if r < r_min or r > r_max:
                continue
            t = arc_t(math.atan2(dy, dx))
            if t is None:
                continue
            sx = t * (sw - 1)
            sy = half - (r - radius)
            ix, iy = int(sx), int(sy)
            if not (0 <= ix < sw - 1 and 0 <= iy < sh - 1):
                continue
            fx, fy = sx - ix, sy - iy
            c00 = src[ix, iy]
            c10 = src[ix + 1, iy]
            c01 = src[ix, iy + 1]
            c11 = src[ix + 1, iy + 1]
            pix = tuple(
                int(
                    c00[c] * (1 - fx) * (1 - fy)
                    + c10[c] * fx * (1 - fy)
                    + c01[c] * (1 - fx) * fy
                    + c11[c] * fx * fy
                )
                for c in range(4)
            )
            _blend(canvas, px, py, pix)


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
    land = font(SERIF_BOLD, 46)
    land_small = font(SERIF_BOLD, 30)
    caption = font(SERIF_ITALIC, 17)
    water = font(SERIF_BOLD_ITALIC, 36)
    crossing = font(SERIF_BOLD_ITALIC, 26)
    feature = font(SERIF_ITALIC, 20)
    rain = font(SERIF_ITALIC, 20)
    note = font(SERIF_ITALIC, 13)

    ink = ImageDraw.Draw(canvas)

    # Quiet north water — sheet title, not a fifth land.
    halo_text(ink, (500, 50), "THE TURNING", title, TYPE, stroke=3)
    halo_text(ink, (500, 80), "the Known Lands", subtitle, TYPE_MUTED, stroke=2)

    # Kumbaan — name below the ring. Storm-wall is a shallow crown
    # over the foam, not a tight horseshoe.
    halo_text(ink, (152, 272), "Kumbaan", land_small, TYPE, stroke=3)
    halo_text(ink, (152, 300), "the Sundering Isle", caption, TYPE_MUTED, stroke=2)
    # Gentle tilt over the north foam — a full horseshoe read as too curved.
    paste_rotated(
        canvas,
        "the storm-wall",
        feature,
        TYPE_WATER,
        (158, 70),
        -8,
        stroke=2,
    )

    # Heskoren — south-west frontier, south of the Old World pair.
    halo_text(ink, (300, 898), "HESKOREN", land, TYPE, stroke=3)
    halo_text(ink, (300, 932), "the Sundered Reach", caption, TYPE_MUTED, stroke=2)

    # West Water — the wide ocean west of Strandoren and north of
    # Heskoren. Deep arc through the middle of that blue, not a
    # straight slug and not the north pocket under Kumbaan.
    warp_along_arc(
        canvas,
        "the West Water",
        water,
        TYPE_WATER,
        cx=575,
        cy=890,
        radius=290,
        start_deg=120,
        end_deg=60,
        stroke=3,
    )

    # Strandoren — maritime Old-World neighbour.
    halo_text(ink, (800, 152), "STRANDOREN", land, TYPE, stroke=3)
    halo_text(ink, (800, 184), "the Shore-lands", caption, TYPE_MUTED, stroke=2)

    # Old Crossing — one nearly-vertical word in the actual strait
    # between Strandoren and Maiethorn, not the north ocean above it.
    paste_rotated(
        canvas,
        "the Old Crossing",
        crossing,
        TYPE_WATER,
        (1054, 488),
        -88,
        stroke=3,
    )

    # Maiethorn — far east. Name north of the wet west.
    halo_text(ink, (1240, 222), "MAIETHORN", land, TYPE, stroke=3)
    halo_text(ink, (1240, 254), "the Motherland", caption, TYPE_MUTED, stroke=2)

    # Rain-Wall — bow with Maiethorn's crescent spine.
    paste_along_arc(
        canvas,
        "the Rain-Wall",
        rain,
        TYPE,
        cx=1280,
        cy=520,
        radius=118,
        start_deg=70,
        end_deg=-70,
        stroke=2,
        tracking=1.12,
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
