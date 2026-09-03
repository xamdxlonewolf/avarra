#!/usr/bin/env python3
"""Overlay Named Ground labels on the selected world atlas painting.

The painting stays the geographic texture. Names come from Named Ground
and the Known Map schematic only — four lands and the two waters, west
to east. Extra painted isles, decorative stars, and weather stay unnamed.
Rebuild:

    python3 "14 - Assets/Maps/label_world_atlas.py"

West is left. East is right. No fifth land. No graft on Kumbaan.
The Rain-Wall is Maiethorn's spine, not Heskoren's highlands.
"""

from __future__ import annotations

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


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 world master, got {base.size}")

    canvas = base.copy()

    title = font(SERIF_BOLD, 34)
    subtitle = font(SERIF_ITALIC, 16)
    land = font(SERIF_BOLD, 28)
    land_small = font(SERIF_BOLD, 20)
    caption = font(SERIF_ITALIC, 14)
    water = font(SERIF_BOLD_ITALIC, 22)
    feature = font(SERIF_ITALIC, 16)
    note = font(SERIF_ITALIC, 13)

    ink = ImageDraw.Draw(canvas)

    # Quiet north water — sheet title, not a fifth land.
    halo_text(ink, (560, 56), "THE TURNING", title, TYPE, stroke=3)
    halo_text(ink, (560, 86), "the Known Lands", subtitle, TYPE_MUTED, stroke=2)

    # Kumbaan — small storm-walled isle, upper left. Type sits in the water
    # below the hills. No city, no Tree, no safe channel. Do not name a graft.
    halo_text(ink, (152, 252), "Kumbaan", land_small, TYPE, stroke=3)
    halo_text(ink, (152, 274), "the Sundering Isle", caption, TYPE_MUTED, stroke=2)
    paste_rotated(canvas, "the storm-wall", feature, TYPE_WATER, (282, 118), angle=-16)
    ink = ImageDraw.Draw(canvas)

    # Heskoren — south-west frontier, distinctly south of the Old World pair.
    halo_text(ink, (300, 924), "HESKOREN", land, TYPE, stroke=3)
    halo_text(ink, (300, 950), "the Sundered Reach", caption, TYPE_MUTED, stroke=2)

    # West Water — the wide emptiness between Heskoren and Strandoren.
    # Not the narrow eastern channel. Not Kumbaan's wall.
    paste_rotated(canvas, "the West Water", water, TYPE_WATER, (400, 360), angle=-8)

    # Strandoren — maritime Old-World neighbour, centre of the sheet.
    # Type sits in the water just north of the coast, not on the roofs.
    halo_text(ink, (800, 164), "STRANDOREN", land, TYPE, stroke=3)
    halo_text(ink, (800, 190), "the Shore-lands", caption, TYPE_MUTED, stroke=2)

    # Old Crossing — the crowded strait between Strandoren and Maiethorn.
    # Type sits in the water north of the pinch so it does not become a border.
    paste_rotated(canvas, "the Old Crossing", water, TYPE_WATER, (1088, 220), angle=-72)

    # Maiethorn — far east, largest old land. Name on the wet west, not the dry.
    halo_text(ink, (1228, 232), "MAIETHORN", land, TYPE, stroke=3)
    halo_text(ink, (1228, 258), "the Motherland", caption, TYPE_MUTED, stroke=2)

    # Rain-Wall — Maiethorn's north–south divide, on the ridge, not the dry east.
    # Not Heskoren's spines.
    paste_rotated(canvas, "the Rain-Wall", feature, TYPE, (1372, 498), angle=-82)

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
