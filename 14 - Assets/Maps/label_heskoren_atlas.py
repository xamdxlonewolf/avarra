#!/usr/bin/env python3
"""Overlay Named Ground labels on the selected Heskoren atlas painting.

The painting stays the geographic texture. Names and relative placement come
from Named Ground / the Known Map schematic — not from incidental generated
roofs, fields, or tributaries. Rebuild:

    python3 "14 - Assets/Maps/label_heskoren_atlas.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Heskoren-Atlas.png"
OUTPUT = ROOT / "Heskoren-Atlas-Labeled.png"

# Liberation Serif ≈ the Georgia hand on the Known Map SVG.
FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF = FONT_DIR / "LiberationSerif-Regular.ttf"
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "LiberationSerif-Italic.ttf"
SERIF_BOLD_ITALIC = FONT_DIR / "LiberationSerif-BoldItalic.ttf"

INK = (36, 30, 20)
INK_MUTED = (62, 54, 40)
# Cream type, dark stroke: the painting is too dark for iron-gall fill.
TYPE = (236, 226, 196)
TYPE_MUTED = (220, 208, 176)
TYPE_WATER = (214, 228, 230)
STROKE = (28, 22, 14)
PARCHMENT = (228, 210, 170, 205)
PARCHMENT_EDGE = (92, 72, 42, 230)
DOT = (28, 24, 16)
DOT_RING = (236, 226, 200)

# Painted land, inside the bronze frame. West left, north up.
# Tuned against the Prototype 3 Heskoren master (1536×1024).
LAND = (190, 95, 1145, 905)


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def land_xy(fx: float, fy: float) -> tuple[int, int]:
    x0, y0, x1, y1 = LAND
    return int(x0 + fx * (x1 - x0)), int(y0 + fy * (y1 - y0))


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


def cartouche(canvas: Image.Image, cx: int, cy: int, width: int, height: int) -> None:
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    box = [cx - width // 2, cy - height // 2, cx + width // 2, cy + height // 2]
    draw.rounded_rectangle(box, radius=14, fill=PARCHMENT, outline=PARCHMENT_EDGE, width=2)
    inner = [box[0] + 5, box[1] + 5, box[2] - 5, box[3] - 5]
    draw.rounded_rectangle(inner, radius=10, outline=(140, 112, 64, 160), width=1)
    canvas.alpha_composite(overlay)


def settlement_dot(draw: ImageDraw.ImageDraw, xy: tuple[int, int], radius: int = 5) -> None:
    x, y = xy
    draw.ellipse((x - radius - 2, y - radius - 2, x + radius + 2, y + radius + 2), fill=DOT_RING)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=DOT)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Heskoren master, got {base.size}")

    canvas = base.copy()

    title = font(SERIF_BOLD, 36)
    subtitle = font(SERIF_ITALIC, 16)
    place = font(SERIF_BOLD, 22)
    caption = font(SERIF, 14)
    water = font(SERIF_BOLD_ITALIC, 26)
    river = font(SERIF_ITALIC, 18)
    note = font(SERIF_ITALIC, 13)

    # Continent name sits in the north-west sea so the highland spine stays visible.
    cartouche(canvas, 268, 148, 292, 92)
    ink = ImageDraw.Draw(canvas)
    halo_text(ink, (268, 132), "HESKOREN", title, INK, stroke=0)
    halo_text(ink, (268, 168), "the Sundered Reach", subtitle, INK_MUTED, stroke=0)

    paste_rotated(canvas, "the West Water", water, TYPE_WATER, (1260, 470), angle=-10)
    ink = ImageDraw.Draw(canvas)

    # Relative seats follow the Known Map schematic, mapped onto this land box.
    # Eolvaeth: vale behind the east-facing coast.
    eol = land_xy(0.74, 0.36)
    settlement_dot(ink, eol)
    halo_text(ink, (eol[0] - 16, eol[1] - 22), "Eolvaeth", place, TYPE, anchor="rm")
    halo_text(ink, (eol[0] - 16, eol[1] + 4), "Vaethorn", caption, TYPE_MUTED, anchor="rm", stroke=2)

    # Harrow's: inland live-front rise, east of the highland spine, not a capital.
    harrow = land_xy(0.47, 0.53)
    settlement_dot(ink, harrow)
    halo_text(ink, (harrow[0] + 16, harrow[1] - 20), "Harrow's", place, TYPE, anchor="lm")
    halo_text(ink, (harrow[0] + 16, harrow[1] + 4), "Saelvaeth", caption, TYPE_MUTED, anchor="lm", stroke=2)

    # Ford: hours down the Rise-water. Close on the page because the walk is short.
    ford = land_xy(0.56, 0.63)
    settlement_dot(ink, ford, radius=4)
    halo_text(ink, (ford[0] + 14, ford[1] + 2), "the ford", place, TYPE, anchor="lm")

    rise = land_xy(0.51, 0.57)
    paste_rotated(canvas, "Rise-water", river, TYPE_WATER, rise, angle=-26)
    ink = ImageDraw.Draw(canvas)

    # Power stubs: named country, seats still unnamed. No borders.
    halo_text(ink, land_xy(0.38, 0.76), "Ornled", place, TYPE)
    halo_text(ink, land_xy(0.66, 0.88), "Vaelhesk", place, TYPE)

    halo_text(ink, land_xy(0.70, 0.26), "waiting vale", note, TYPE_MUTED, anchor="mm", stroke=2)
    halo_text(ink, land_xy(0.50, 0.46), "live front", note, TYPE_MUTED, anchor="mm", stroke=2)

    footer = "Names from Named Ground. Painting is not a survey."
    halo_text(ink, (768, 988), footer, note, TYPE_MUTED, stroke=2)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
