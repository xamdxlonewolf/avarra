#!/usr/bin/env python3
"""Label the Larbril city plate.\n\nThe west road meets the Well-wash. The wash in this frame is a\nsilt-line. A Hand stands at the meeting. The image model was not\nasked to write.

    python3 "14 - Assets/Maps/label_larbril.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Larbril-Atlas.png"
OUTPUT = ROOT / "Larbril-Atlas-Labeled.png"

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
    # The Hand beside the crossing. The wash is the water, not a second road.
    leader(ink, (340, 250), (560, 400))
    halo_text(ink, (340, 250), "The Tree", place, TYPE)
    halo_text(ink, (180, 430), "The west road", place, TYPE)
    halo_text(ink, (500, 150), "Well-wash", water, TYPE_WATER)
    leader(ink, (740, 540), (540, 450))
    halo_text(ink, (740, 540), "The meeting", place, TYPE)
    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
