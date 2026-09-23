#!/usr/bin/env python3
"""Overlay canonical labels on the selected West Water atlas painting.

The painting supplies texture only. Placement and names come from Named
Ground, the Known Map schematic, the R6 prompt, and the Netstrand note.
Rebuild:

    python3 "14 - Assets/Maps/label_west_water_atlas.py"

West is left. The West Water is the open ocean filling the left and
centre. The Night Shore is area-type on the west-and-south face; its
seat stays unnamed. The unlit berth is left unmarked. Hulls, harbour
hatches, lamp-ticks, the painted inland run, and the far-left weather
remain unnamed.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from label_curves import cubic, paste_along_path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "West-Water-Atlas.png"
OUTPUT = ROOT / "West-Water-Atlas-Labeled.png"

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


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 West Water master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    region = font(SERIF_BOLD_ITALIC, 24)
    water = font(SERIF_BOLD_ITALIC, 22)

    # One name, in the open ocean, following the swell. No header above it.
    paste_along_path(
        canvas,
        "The West Water",
        water,
        TYPE_WATER,
        cubic((180, 580), (340, 500), (500, 530), (640, 620)),
        stroke=2,
    )

    # The Night Shore is the west-and-south face. Its seat remains unnamed,
    # so the coast gets area-type rather than a settlement marker. The unlit
    # berth is a gap in the lamps, not a label — leave it for play.
    paste_rotated(canvas, "THE NIGHT SHORE", region, TYPE, (1324, 478), angle=78)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
