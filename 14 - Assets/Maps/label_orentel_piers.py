#!/usr/bin/env python3
"""Label the Orentel pier sheet.

The frame is the tide. The Rise stays off the inland edge, so the Tree
stays inland. Label only First Quay, The Third, and White Note.
The image model was not asked to write.

    python3 "14 - Assets/Maps/label_orentel_piers.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Orentel-Piers-Atlas.png"
OUTPUT = ROOT / "Orentel-Piers-Atlas-Labeled.png"

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
        raise SystemExit(f"Expected 1152×864 pier master, got {base.size}")
    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)
    place = font(SERIF_BOLD, 20)

    # North-side quay. The open deck, not the roofs.
    halo_text(ink, (490, 128), "The Third", place, TYPE)

    # One desk-house on that quay. The name would sit on the roof.
    leader(ink, (700, 128), (790, 228))
    halo_text(ink, (806, 228), "White Note", place, TYPE, anchor="lm")

    # South landing, in the water under the berths.
    halo_text(ink, (520, 828), "First Quay", place, TYPE)

    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
