#!/usr/bin/env python3
"""Label the Lunbra city plate.\n\nThe roll-room stands on the square. The Chart-run leaves toward\nthe right. A Hand is in the square. The image model was not asked\nto write.

    python3 "14 - Assets/Maps/label_lunbra.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Lunbra-Atlas.png"
OUTPUT = ROOT / "Lunbra-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "LiberationSerif-BoldItalic.ttf"

TYPE = (48, 32, 18)
TYPE_WATER = (28, 48, 62)
HALO = (244, 236, 214)
MARK = (42, 28, 16)


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def halo_text(draw, xy, text, typeface, fill, *, anchor="mm", stroke=3):
    draw.text(xy, text, font=typeface, fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=HALO)


def leader(draw, start, end):
    draw.line((start, end), fill=HALO, width=3)
    draw.line((start, end), fill=MARK, width=1)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1152, 864):
        raise SystemExit(f"Expected 1152×864 master, got {base.size}")
    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)
    place = font(SERIF_BOLD, 20)
    water = font(SERIF_ITALIC, 20)
    leader(ink, (1000, 160), (780, 260))
    halo_text(ink, (1000, 160), "The roll-room", place, TYPE)
    leader(ink, (320, 260), (530, 370))
    halo_text(ink, (320, 260), "The Tree", place, TYPE)
    leader(ink, (360, 540), (520, 470))
    halo_text(ink, (360, 540), "The square", place, TYPE)
    halo_text(ink, (760, 800), "Chart-run", water, TYPE_WATER)
    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
