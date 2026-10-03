#!/usr/bin/env python3
"""Label Ornsael.

A well-town. The Tree stands beside the well. The west-road is the
main street and leaves toward the pass. The image model was not asked
to write.

    python3 "14 - Assets/Maps/label_ornsael.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Ornsael-Atlas.png"
OUTPUT = ROOT / "Ornsael-Atlas-Labeled.png"

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
        raise SystemExit(f"Expected 1152×864 Ornsael master, got {base.size}")
    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)
    place = font(SERIF_BOLD, 20)

    # The canopy. The name sits in the open planting, not on a roof.
    leader(ink, (700, 340), (900, 430))
    halo_text(ink, (912, 430), "The Tree", place, TYPE, anchor="lm")

    # Open dust below the well-mouth.
    halo_text(ink, (620, 500), "The well", place, TYPE)

    # On the open road, clear of the roofs above it.
    halo_text(ink, (150, 310), "The west-road", place, TYPE)

    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
