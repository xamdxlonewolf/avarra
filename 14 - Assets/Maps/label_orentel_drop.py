#!/usr/bin/env python3
"""Label the Orentel drop zoom.

A closer sheet of the Rise, the Tree, the Drop, the First Quay, and the
White Note on the Third. Not a new district. The image model was not
asked to write.

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


def quay_mark(draw, xy):
    x, y = xy
    draw.rectangle((x - 9, y - 4, x + 9, y + 4), fill=HALO)
    draw.rectangle((x - 7, y - 2, x + 7, y + 2), fill=MARK)
    draw.line((x - 9, y - 7, x - 9, y + 7), fill=HALO, width=4)
    draw.line((x - 9, y - 6, x - 9, y + 6), fill=MARK, width=2)


def house_mark(draw, xy):
    x, y = xy
    draw.polygon(((x, y - 8), (x + 7, y - 1), (x - 7, y - 1)), fill=HALO)
    draw.polygon(((x, y - 6), (x + 5, y - 1), (x - 5, y - 1)), fill=MARK)
    draw.rectangle((x - 5, y - 1, x + 5, y + 7), fill=HALO)
    draw.rectangle((x - 3, y, x + 3, y + 5), fill=MARK)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1152, 864):
        raise SystemExit(f"Expected 1152×864 drop master, got {base.size}")
    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)
    title = font(SERIF_BOLD, 26)
    place = font(SERIF_BOLD, 20)

    halo_text(ink, (150, 40), "Orentel", title, TYPE)

    leader(ink, (520, 110), (360, 70))
    halo_text(ink, (348, 70), "The Rise", place, TYPE, anchor="rm")

    leader(ink, (590, 90), (740, 55))
    halo_text(ink, (752, 55), "The Tree", place, TYPE, anchor="lm")

    leader(ink, (610, 300), (430, 240))
    halo_text(ink, (418, 240), "The Drop", place, TYPE, anchor="rm")

    quay_mark(ink, (340, 540))
    leader(ink, (325, 548), (180, 620))
    halo_text(ink, (168, 620), "First Quay", place, TYPE, anchor="rm")

    quay_mark(ink, (980, 620))
    leader(ink, (990, 610), (1040, 540))
    halo_text(ink, (1052, 540), "The Third", place, TYPE, anchor="lm")

    house_mark(ink, (820, 520))
    leader(ink, (835, 510), (960, 460))
    halo_text(ink, (972, 460), "White Note", place, TYPE, anchor="lm")

    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
