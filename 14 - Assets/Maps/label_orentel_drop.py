#!/usr/bin/env python3
"""Label the Orentel drop zoom.

The same span as the city plate, from the Rise to the quays. A
neighborhood of roofs stays between the Tree and the docks. The Third
and the White Note are the north pier in this frame. Not a new district.
The image model was not asked to write.

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

    halo_text(ink, (130, 36), "Orentel", title, TYPE)

    # Square in the upper left, still inland of the roofs.
    leader(ink, (220, 240), (120, 150))
    halo_text(ink, (108, 150), "The Rise", place, TYPE, anchor="rm")

    leader(ink, (270, 215), (390, 140))
    halo_text(ink, (402, 140), "The Tree", place, TYPE, anchor="lm")

    # The long street through the roofs, not the waterfront.
    leader(ink, (450, 360), (330, 450))
    halo_text(ink, (318, 450), "The Drop", place, TYPE, anchor="rm")

    # Long south landing, after the neighborhood.
    quay_mark(ink, (800, 490))
    leader(ink, (815, 505), (960, 600))
    halo_text(ink, (972, 600), "First Quay", place, TYPE, anchor="lm")

    # North pier, same side as on the city plate.
    quay_mark(ink, (760, 145))
    leader(ink, (748, 138), (640, 80))
    halo_text(ink, (628, 80), "The Third", place, TYPE, anchor="rm")

    house_mark(ink, (880, 175))
    leader(ink, (892, 168), (1020, 120))
    halo_text(ink, (1032, 120), "White Note", place, TYPE, anchor="lm")

    return canvas.convert("RGB")


def main() -> None:
    image = build()
    image.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
