#!/usr/bin/env python3
"""Label the Rothallo gate sheet.\n\nThe city plate could not hold the beds outside and the Book inside.\nThis is that gate. The image model was not asked to write.

    python3 "14 - Assets/Maps/label_rothallo_gate.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Rothallo-Gate-Atlas.png"
OUTPUT = ROOT / "Rothallo-Gate-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"

TYPE = (48, 32, 18)
TYPE_WATER = (28, 48, 62)
HALO = (244, 236, 214)


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def halo_text(draw, xy, text, typeface, fill, *, anchor="mm", stroke=3):
    draw.text(xy, text, font=typeface, fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=HALO)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1152, 864):
        raise SystemExit(f"Expected 1152×864 master, got {base.size}")
    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)
    place = font(SERIF_BOLD, 20)
    # Same gatehouse as the city plate. Beds outside. Book inside the wall.
    halo_text(ink, (520, 500), "The gate", place, TYPE)
    halo_text(ink, (160, 430), "The beds", place, TYPE)
    halo_text(ink, (610, 290), "The Book", place, TYPE)
    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
