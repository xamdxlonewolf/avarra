#!/usr/bin/env python3
"""Label the Orentel drop zoom.

The Rise inside the city. The Tree is a mature Hand: a broad dark
hardwood filling its square, not the First Hand. The Drop leaves that
square through houses. The quays are not in this frame.
Not a new district. The image model was not asked to write.

    python3 "14 - Assets/Maps/label_orentel_drop.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Orentel-Drop-Atlas.png"
OUTPUT = ROOT / "Orentel-Drop-Atlas-Labeled.png"

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
        raise SystemExit(f"Expected 1152×864 drop master, got {base.size}")
    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)
    title = font(SERIF_BOLD, 26)
    place = font(SERIF_BOLD, 20)

    halo_text(ink, (140, 40), "Orentel", title, TYPE)

    # The square under the mature Hand. Roofs continue past every edge.
    leader(ink, (430, 470), (260, 400))
    halo_text(ink, (248, 400), "The Rise", place, TYPE, anchor="rm")

    leader(ink, (470, 230), (300, 150))
    halo_text(ink, (288, 150), "The Tree", place, TYPE, anchor="rm")

    # The street leaving the square, still among houses. The quay is off the sheet.
    leader(ink, (740, 750), (560, 820))
    halo_text(ink, (548, 820), "The Drop", place, TYPE, anchor="rm")

    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
