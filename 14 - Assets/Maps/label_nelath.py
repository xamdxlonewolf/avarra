#!/usr/bin/env python3
"""Label Nelath.

A smaller square than the Mill-hold. The spur becomes the square.
The stone is in the square. The scar is beyond the boughs.
The image model was not asked to write.

    python3 "14 - Assets/Maps/label_nelath.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Nelath-Atlas.png"
OUTPUT = ROOT / "Nelath-Atlas-Labeled.png"

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
        raise SystemExit(f"Expected 1152×864 Nelath master, got {base.size}")
    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)
    place = font(SERIF_BOLD, 20)

    leader(ink, (140, 260), (280, 400))
    halo_text(ink, (140, 260), "The Tree", place, TYPE)
    leader(ink, (640, 360), (460, 440))
    halo_text(ink, (640, 360), "The stone", place, TYPE)
    leader(ink, (840, 420), (620, 480))
    halo_text(ink, (840, 420), "The scar", place, TYPE)

    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
