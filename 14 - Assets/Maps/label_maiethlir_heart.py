#!/usr/bin/env python3
"""Label the Maiethlir heart zoom.

A closer sheet of the Tree, the Slow Water, the Loft Row, and the
tablet-hall. Not a new district. The image model was not asked to write.

    python3 "14 - Assets/Maps/label_maiethlir_heart.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Maiethlir-Heart-Atlas.png"
OUTPUT = ROOT / "Maiethlir-Heart-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_BOLD_ITALIC = FONT_DIR / "LiberationSerif-BoldItalic.ttf"

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


def hall_mark(draw, xy):
    x, y = xy
    draw.rectangle((x - 14, y - 7, x + 14, y + 7), fill=HALO)
    draw.rectangle((x - 12, y - 5, x + 12, y + 5), fill=MARK)
    draw.rectangle((x - 4, y - 2, x + 4, y + 2), fill=HALO)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1152, 864):
        raise SystemExit(f"Expected 1152×864 heart master, got {base.size}")
    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)
    title = font(SERIF_BOLD, 26)
    place = font(SERIF_BOLD, 20)
    water = font(SERIF_BOLD_ITALIC, 20)

    halo_text(ink, (170, 48), "Maiethlir", title, TYPE)

    leader(ink, (560, 620), (360, 560))
    halo_text(ink, (348, 560), "The Tree", place, TYPE, anchor="rm")

    hall_mark(ink, (560, 420))
    leader(ink, (576, 412), (760, 360))
    halo_text(ink, (772, 360), "Tablet-hall", place, TYPE, anchor="lm")

    leader(ink, (500, 500), (280, 430))
    halo_text(ink, (268, 430), "Loft Row", place, TYPE, anchor="rm")

    halo_text(ink, (280, 700), "Slow Water", water, TYPE_WATER)
    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
