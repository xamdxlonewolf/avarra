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
    for mark in marks:
        x, y, text, fill = mark[0], mark[1], mark[2], mark[3]
        if len(mark) == 6:
            leader(ink, (x, y), (mark[4], mark[5]))
        halo(ink, (x, y), text, face, fill)
    base.convert("RGB").save(ROOT / out, quality=95)
    print(f"Wrote {out}")


def main() -> None:
    T, W = TYPE, TYPE_WATER
    label("Seinbrun-Plan-Atlas.png", "Seinbrun-Plan-Atlas-Labeled.png", [
        (180, 200, "The hall", T, 280, 320),
        (680, 300, "The Tree", T, 500, 380),
        (250, 560, "The green", T, 420, 480),
    ])
    label("Rothallo-Plan-Atlas.png", "Rothallo-Plan-Atlas-Labeled.png", [
        (640, 80, "The Tree", T, 510, 175),
        (920, 250, "The Book", T, 760, 320),
        (900, 760, "The gate", T, 720, 640),
        (200, 800, "The beds", T, 140, 660),
    ])
    label("Larbril-Plan-Atlas.png", "Larbril-Plan-Atlas-Labeled.png", [
        (160, 150, "The Tree", T, 320, 230),
        (760, 400, "The meeting", T, 570, 455),
        (140, 560, "The west road", T, 280, 490),
        (700, 110, "Well-wash", W, 530, 180),
    ])
    label("Votaer-Plan-Atlas.png", "Votaer-Plan-Atlas-Labeled.png", [
        (1040, 220, "The Tree", T, 900, 320),
        (240, 620, "Classification quay", T, 340, 430),
    ])
    label("Raitin-Plan-Atlas.png", "Raitin-Plan-Atlas-Labeled.png", [
        (250, 140, "The hall", T, 480, 260),
        (980, 360, "The Tree", T, 800, 450),
        (480, 720, "The river stair", T, 680, 650),
    ])
    label("Naenor-Plan-Atlas.png", "Naenor-Plan-Atlas-Labeled.png", [
        (140, 120, "The Tree", T, 300, 210),
        (360, 520, "The signing-watch", T, 530, 400),
    ])
    label("Lunbra-Plan-Atlas.png", "Lunbra-Plan-Atlas-Labeled.png", [
        (250, 220, "The Tree", T, 420, 310),
        (760, 160, "The roll-room", T, 580, 240),
        (320, 440, "The square", T, 500, 400),
        (1020, 500, "Chart-run", W),
    ])
    label("Braetu-Plan-Atlas.png", "Braetu-Plan-Atlas-Labeled.png", [
        (160, 250, "The quote-desk", T, 300, 340),
        (140, 800, "The unlit berth", T, 280, 700),
        (1040, 180, "The Tree", T, 870, 270),
        (80, 70, "West Water", W),
    ])
    label("Tasain-Plan-Atlas.png", "Tasain-Plan-Atlas-Labeled.png", [
        (720, 150, "The Tree", T, 540, 250),
        (280, 800, "The town gate", T, 490, 700),
    ])
    label("Sanbreo-Plan-Atlas.png", "Sanbreo-Plan-Atlas-Labeled.png", [
        (880, 470, "The shore gate", T, 650, 530),
        (400, 740, "The slate", T, 510, 600),
    ])
    label("Natai-Plan-Atlas.png", "Natai-Plan-Atlas-Labeled.png", [
        (280, 170, "The Tree", T, 470, 280),
        (160, 800, "The town gate", T, 240, 690),
    ])
    label("Eolvaeth-Plan-Atlas.png", "Eolvaeth-Plan-Atlas-Labeled.png", [
        (260, 250, "The gift-hall", T, 460, 340),
        (760, 560, "The spring", T, 560, 480),
        (900, 280, "The Tree", T, 730, 380),
    ])
    label("Harrows-Green-Plan-Atlas.png", "Harrows-Green-Plan-Atlas-Labeled.png", [
        (300, 240, "The Tree", T, 480, 340),
        (780, 300, "The stone", T, 610, 400),
    ])
    label("Mill-hold-Plan-Atlas.png", "Mill-hold-Plan-Atlas-Labeled.png", [
        (250, 90, "The Tree", T, 430, 180),
        (250, 470, "The culvert", T, 450, 400),
        (760, 760, "The mill-race", W, 540, 650),
    ])
    label("Ornsael-Plan-Atlas.png", "Ornsael-Plan-Atlas-Labeled.png", [
        (860, 250, "The Tree", T, 700, 340),
        (380, 470, "The well", T, 555, 390),
        (180, 140, "The west-road", T, 300, 240),
    ])
    label("Nelath-Plan-Atlas.png", "Nelath-Plan-Atlas-Labeled.png", [
        (240, 270, "The Tree", T, 420, 360),
        (800, 250, "The stone", T, 630, 340),
        (900, 540, "The scar", T, 700, 470),
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
