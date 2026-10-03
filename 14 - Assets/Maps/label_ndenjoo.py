#!/usr/bin/env python3
"""Label Ndenjoo.

One hill and a hall under the turf. No Tree. The image model was not
asked to write.

    python3 "14 - Assets/Maps/label_ndenjoo.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Ndenjoo-Atlas.png"
OUTPUT = ROOT / "Ndenjoo-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"

TYPE = (48, 32, 18)
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
        raise SystemExit(f"Expected 1152×864 Ndenjoo master, got {base.size}")
    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)
    place = font(SERIF_BOLD, 20)

    # The lit turf door, low on the slope. The name sits in the open turf beside it.
    leader(ink, (512, 628), (400, 590))
    halo_text(ink, (388, 590), "The hall", place, TYPE, anchor="rm")

    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
