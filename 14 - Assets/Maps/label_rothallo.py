#!/usr/bin/env python3
"""Label the Rothallo city plate.\n\nOrenbren's walled capital. The gate, the beds outside, and a Hand\ninside the walls. The Book is on the gate sheet. The image model\nwas not asked to write.

    python3 "14 - Assets/Maps/label_rothallo.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Rothallo-Atlas.png"
OUTPUT = ROOT / "Rothallo-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"

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
    leader(ink, (320, 140), (530, 260))
    halo_text(ink, (320, 140), "The Tree", place, TYPE)
    leader(ink, (90, 600), (270, 690))
    halo_text(ink, (90, 600), "The gate", place, TYPE)
    leader(ink, (320, 830), (150, 800))
    halo_text(ink, (320, 830), "The beds", place, TYPE)
    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
