#!/usr/bin/env python3
"""Label the Orentel drop zoom.

A closer sheet of the same Rise, Tree, Drop, and First Quay as the city
plate. The Third and the White Note stay on the city plate, on the north
pier above this frame. Not a new district. The image model was not asked
to write.

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

    halo_text(ink, (140, 36), "Orentel", title, TYPE)

    # Same square as the city plate: left side, roofs around it.
    leader(ink, (250, 200), (140, 130))
    halo_text(ink, (128, 130), "The Rise", place, TYPE, anchor="rm")

    leader(ink, (300, 230), (400, 160))
    halo_text(ink, (412, 160), "The Tree", place, TYPE, anchor="lm")

    # Same street, still running from the square down to the berths.
    leader(ink, (560, 400), (430, 340))
    halo_text(ink, (418, 340), "The Drop", place, TYPE, anchor="rm")

    # The long quay this street reaches. The north pier is off this frame.
    quay_mark(ink, (900, 620))
    leader(ink, (915, 635), (1020, 700))
    halo_text(ink, (1032, 700), "First Quay", place, TYPE, anchor="lm")

    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
