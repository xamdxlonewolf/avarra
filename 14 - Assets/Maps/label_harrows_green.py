#!/usr/bin/env python3
"""Label Harrow's Green.

The live-front square. A Hand at the centre and the stone in the square.
The hamlets stay unnamed. The image model was not asked to write.

    python3 "14 - Assets/Maps/label_harrows_green.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Harrows-Green-Atlas.png"
OUTPUT = ROOT / "Harrows-Green-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"

TYPE = (48, 32, 18)
HALO = (244, 236, 214)
MARK = (42, 28, 16)


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def halo_text(draw, xy, text, typeface, fill, *, anchor="mm", stroke=3):
    draw.text(xy, text, font=typeface, fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=HALO)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1152, 864):
        raise SystemExit(f"Expected 1152×864 Harrow's Green master, got {base.size}")
    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)
    place = font(SERIF_BOLD, 20)

    # On the lower trunk, in the dirt at the roots.
    halo_text(ink, (552, 424), "The Tree", place, TYPE)

    # Open dirt against the right of the standing stone.
    halo_text(ink, (712, 410), "The stone", place, TYPE, anchor="lm")

    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
