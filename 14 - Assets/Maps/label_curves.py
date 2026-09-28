"""Glyphs along a curve for atlas water labels.

Rivers, oceans, and seas use this. Land names stay straight. Each
overlay script keeps its own placement; this module only bends type.
"""

from __future__ import annotations

import math

from PIL import Image, ImageDraw, ImageFont

STROKE = (28, 22, 14)


def measure(typeface: ImageFont.FreeTypeFont, text: str) -> tuple[int, int]:
    bbox = typeface.getbbox(text)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def glyph_width(typeface: ImageFont.FreeTypeFont, char: str) -> int:
    if char == " ":
        return max(6, measure(typeface, "n")[0] // 2)
    return max(1, measure(typeface, char)[0])


def _halo(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    typeface: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    stroke: int,
) -> None:
    draw.text(
        xy,
        text,
        font=typeface,
        fill=fill,
        anchor="mm",
        stroke_width=stroke,
        stroke_fill=STROKE,
    )


def _paste_rotated(
    canvas: Image.Image,
    text: str,
    typeface: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    centre: tuple[int, int],
    angle: float,
    stroke: int,
) -> None:
    width, height = measure(typeface, text)
    pad = stroke * 2 + 8
    layer = Image.new("RGBA", (width + pad * 2, height + pad * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    _halo(draw, (layer.width // 2, layer.height // 2), text, typeface, fill, stroke)
    rotated = layer.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    canvas.paste(
        rotated,
        (centre[0] - rotated.width // 2, centre[1] - rotated.height // 2),
        rotated,
    )


def cubic(
    start: tuple[float, float],
    control_1: tuple[float, float],
    control_2: tuple[float, float],
    end: tuple[float, float],
    steps: int = 28,
) -> list[tuple[float, float]]:
    """Sample a smooth path. Reading follows start → end."""
    points: list[tuple[float, float]] = []
    for index in range(steps + 1):
        t = index / steps
        u = 1.0 - t
        x = (
            u**3 * start[0]
            + 3 * u**2 * t * control_1[0]
            + 3 * u * t**2 * control_2[0]
            + t**3 * end[0]
        )
        y = (
            u**3 * start[1]
            + 3 * u**2 * t * control_1[1]
            + 3 * u * t**2 * control_2[1]
            + t**3 * end[1]
        )
        points.append((x, y))
    return points


def paste_along_path(
    canvas: Image.Image,
    text: str,
    typeface: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    points: list[tuple[float, float]],
    stroke: int = 2,
    tracking: float = 1.04,
    fit: str = "span",
) -> None:
    """Place glyphs along a polyline. Letters stand on the path.

    ``fit="span"`` opens the name across the whole path, which suits a
    sea or a long coast. ``fit="type"`` keeps the face's own letter
    spacing and centres that run on the path, so a river name follows
    the water without scattering into caption-like letters.
    """
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

    widths = [glyph_width(typeface, char) * tracking for char in text]
    text_w = sum(widths)
    if fit == "span":
        origin = 0.0
        scale = total / text_w
    elif fit == "type":
        origin = max(0.0, (total - text_w) / 2.0)
        scale = 1.0
    else:
        raise ValueError(f"Unknown fit {fit!r}")

    walked = 0.0
    for char, width in zip(text, widths, strict=True):
        target = origin + (walked + width / 2.0) * scale
        x, y, angle = _point_on_path(segs, total, target)
        if char != " ":
            _paste_rotated(
                canvas,
                char,
                typeface,
                fill,
                (int(round(x)), int(round(y))),
                angle,
                stroke,
            )
        walked += width


def _point_on_path(
    segs: list[tuple[float, float, float, float, float, float]],
    total: float,
    target: float,
) -> tuple[float, float, float]:
    """Return x, y, and the reading angle in degrees. Past the end, follow the last heading."""
    x0, y0, x1, y1, length, base = segs[-1]
    if target > total and length > 0:
        extra = (target - total) / length
        x = x1 + (x1 - x0) * extra
        y = y1 + (y1 - y0) * extra
        angle = math.degrees(math.atan2(y0 - y1, x1 - x0))
        return x, y, angle
    for x0, y0, x1, y1, length, base in segs:
        if target <= base + length or (x0, y0, x1, y1, length, base) == segs[-1]:
            break
    t = 0.0 if length == 0 else min(1.0, max(0.0, (target - base) / length))
    x = x0 + (x1 - x0) * t
    y = y0 + (y1 - y0) * t
    angle = math.degrees(math.atan2(y0 - y1, x1 - x0))
    return x, y, angle
