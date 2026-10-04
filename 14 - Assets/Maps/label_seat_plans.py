#!/usr/bin/env python3
"""Label the steep bird's-eye plans of the cities and towns.

The ink hand is shared. The ordinary house is the band card in
Map Generation Tooling. Orentel is the shore-lands house, and
Maiethlir uses the mother-core house. The image model was not
asked to write. West is left. A name sits on the feature it names.

    python3 "14 - Assets/Maps/label_seat_plans.py"
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
FONT = Path("/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf")
TYPE = (48, 32, 18)
TYPE_WATER = (28, 48, 62)
HALO = (244, 236, 214)
MARK = (42, 28, 16)

# A mark is text at (x, y). When fx, fy are set, a leader runs from the
# name to that point on the feature, the same way the Orentel city sheet
# keeps the name off the thing it names.
Mark = tuple[int, int, str, tuple[int, int, int]] | tuple[int, int, str, tuple[int, int, int], int, int]


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT), size)


def halo(draw, xy, text, face, fill):
    draw.text(xy, text, font=face, fill=fill, anchor="mm", stroke_width=3, stroke_fill=HALO)


def leader(draw, start, end):
    draw.line((start, end), fill=HALO, width=3)
    draw.line((start, end), fill=MARK, width=1)


def label(master: str, out: str, marks: list[Mark]) -> None:
    base = Image.open(ROOT / master).convert("RGBA")
    if base.size != (1152, 864):
        raise SystemExit(f"{master} is {base.size}, expected 1152×864")
    ink = ImageDraw.Draw(base)
    face = font(20)
    water = ImageFont.truetype(
        "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf", 20
    )
    for mark in marks:
        x, y, text, fill = mark[0], mark[1], mark[2], mark[3]
        if len(mark) == 6:
            leader(ink, (x, y), (mark[4], mark[5]))
        halo(ink, (x, y), text, water if fill == TYPE_WATER else face, fill)
    base.convert("RGB").save(ROOT / out, quality=95)
    print(f"Wrote {out}")


def main() -> None:
    T, W = TYPE, TYPE_WATER
    label("Seinbrun-Plan-Atlas.png", "Seinbrun-Plan-Atlas-Labeled.png", [
        (180, 160, "The hall", T, 400, 270),
        (830, 190, "The Tree", T, 640, 300),
        (470, 450, "The green", T),
    ])
    label("Rothallo-Plan-Atlas.png", "Rothallo-Plan-Atlas-Labeled.png", [
        (140, 280, "The Tree", T, 280, 430),
        (540, 420, "The Book", T, 380, 510),
        (70, 640, "The gate", T, 170, 730),
        (880, 800, "The beds", T, 620, 780),
    ])
    label("Larbril-Plan-Atlas.png", "Larbril-Plan-Atlas-Labeled.png", [
        (220, 340, "The Tree", T, 420, 480),
        (700, 460, "The meeting", T, 480, 540),
        (860, 680, "The west road", T),
        (500, 140, "Well-wash", W),
    ])
    label("Votaer-Plan-Atlas.png", "Votaer-Plan-Atlas-Labeled.png", [
        (680, 170, "The Tree", T, 480, 300),
        (90, 300, "Classification quay", T, 310, 500),
    ])
    label("Raitin-Plan-Atlas.png", "Raitin-Plan-Atlas-Labeled.png", [
        (200, 170, "The Tree", T, 380, 280),
        (840, 150, "The hall", T, 620, 240),
        (840, 540, "The river stair", T, 640, 480),
    ])
    label("Naenor-Plan-Atlas.png", "Naenor-Plan-Atlas-Labeled.png", [
        (880, 150, "The Tree", T, 690, 240),
        (900, 500, "The signing-watch", T, 700, 400),
    ])
    label("Lunbra-Plan-Atlas.png", "Lunbra-Plan-Atlas-Labeled.png", [
        (320, 260, "The Tree", T, 530, 370),
        (1000, 160, "The roll-room", T, 780, 260),
        (360, 540, "The square", T, 520, 470),
        (760, 800, "Chart-run", W),
    ])
    label("Braetu-Plan-Atlas.png", "Braetu-Plan-Atlas-Labeled.png", [
        (1040, 520, "The quote-desk", T, 880, 650),
        (280, 720, "The unlit berth", T, 520, 620),
        (800, 150, "The Tree", T, 980, 280),
        (140, 480, "West Water", W),
    ])
    label("Tasain-Plan-Atlas.png", "Tasain-Plan-Atlas-Labeled.png", [
        (200, 280, "The Tree", T, 400, 400),
        (460, 830, "The town gate", T, 700, 720),
    ])
    label("Sanbreo-Plan-Atlas.png", "Sanbreo-Plan-Atlas-Labeled.png", [
        (680, 540, "The shore gate", T, 860, 650),
        (680, 430, "The slate", T, 840, 590),
    ])
    label("Natai-Plan-Atlas.png", "Natai-Plan-Atlas-Labeled.png", [
        (320, 220, "The Tree", T, 520, 340),
        (300, 820, "The town gate", T, 540, 740),
    ])
    label("Eolvaeth-Plan-Atlas.png", "Eolvaeth-Plan-Atlas-Labeled.png", [
        (200, 170, "The Tree", T, 410, 280),
        (280, 540, "The spring", T, 490, 440),
        (920, 250, "The gift-hall", T, 700, 360),
    ])
    label("Harrows-Green-Plan-Atlas.png", "Harrows-Green-Plan-Atlas-Labeled.png", [
        (380, 240, "The Tree", T, 640, 360),
        (980, 380, "The stone", T, 790, 450),
    ])
    label("Mill-hold-Plan-Atlas.png", "Mill-hold-Plan-Atlas-Labeled.png", [
        (180, 160, "The Tree", T, 360, 280),
        (340, 460, "The culvert", T, 520, 520),
        (860, 780, "The mill-race", W),
    ])
    label("Ornsael-Plan-Atlas.png", "Ornsael-Plan-Atlas-Labeled.png", [
        (220, 210, "The Tree", T, 400, 330),
        (740, 330, "The well", T, 560, 400),
        (160, 470, "The west-road", T),
    ])
    label("Nelath-Plan-Atlas.png", "Nelath-Plan-Atlas-Labeled.png", [
        (220, 270, "The Tree", T, 400, 400),
        (760, 370, "The stone", T, 590, 450),
        (860, 180, "The scar", T, 1020, 420),
    ])
    # These two plans are the city sheets. Their labels already sit
    # on the features, including the quay and hall marks.
    for src, dst in (
        ("Orentel-City-Atlas-Labeled.png", "Orentel-Plan-Atlas-Labeled.png"),
        ("Maiethlir-City-Atlas-Labeled.png", "Maiethlir-Plan-Atlas-Labeled.png"),
    ):
        image = Image.open(ROOT / src).convert("RGB")
        image.save(ROOT / dst, quality=95)
        print(f"Wrote {dst}")


if __name__ == "__main__":
    main()
