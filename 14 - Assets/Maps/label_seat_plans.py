#!/usr/bin/env python3
"""Label the overhead plans of the cities and towns.

Each plan is a new painting, strictly overhead, not a crop of an oblique
plate. The image model was not asked to write. West is left.

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


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT), size)


def halo(draw, xy, text, face, fill):
    draw.text(xy, text, font=face, fill=fill, anchor="mm", stroke_width=3, stroke_fill=HALO)


def label(master: str, out: str, marks: list[tuple[int, int, str, tuple[int, int, int]]]) -> None:
    base = Image.open(ROOT / master).convert("RGBA")
    if base.size != (1152, 864):
        raise SystemExit(f"{master} is {base.size}, expected 1152×864")
    ink = ImageDraw.Draw(base)
    face = font(20)
    for x, y, text, fill in marks:
        halo(ink, (x, y), text, face, fill)
    base.convert("RGB").save(ROOT / out, quality=95)
    print(f"Wrote {out}")


def main() -> None:
    T, W = TYPE, TYPE_WATER
    label("Seinbrun-Plan-Atlas.png", "Seinbrun-Plan-Atlas-Labeled.png", [
        (570, 370, "The Tree", T),
        (700, 500, "The hall", T),
        (450, 450, "The green", T),
    ])
    label("Rothallo-Plan-Atlas.png", "Rothallo-Plan-Atlas-Labeled.png", [
        (570, 360, "The Tree", T),
        (576, 700, "The gate", T),
        (250, 800, "The beds", T),
        (576, 530, "The Book", T),
    ])
    label("Larbril-Plan-Atlas.png", "Larbril-Plan-Atlas-Labeled.png", [
        (400, 300, "The Tree", T),
        (180, 432, "The west road", T),
        (578, 180, "Well-wash", T),
        (640, 455, "The meeting", T),
    ])
    label("Votaer-Plan-Atlas.png", "Votaer-Plan-Atlas-Labeled.png", [
        (510, 430, "The Tree", T),
        (340, 230, "Classification quay", T),
    ])
    label("Raitin-Plan-Atlas.png", "Raitin-Plan-Atlas-Labeled.png", [
        (576, 430, "The hall", T),
        (780, 500, "The Tree", T),
        (576, 690, "The river stair", T),
    ])
    label("Naenor-Plan-Atlas.png", "Naenor-Plan-Atlas-Labeled.png", [
        (560, 300, "The signing-watch", T),
        (930, 280, "The Tree", T),
    ])
    label("Lunbra-Plan-Atlas.png", "Lunbra-Plan-Atlas-Labeled.png", [
        (500, 310, "The Tree", T),
        (720, 300, "The roll-room", T),
        (610, 350, "The square", T),
        (280, 530, "Chart-run", W),
    ])
    label("Braetu-Plan-Atlas.png", "Braetu-Plan-Atlas-Labeled.png", [
        (240, 145, "The quote-desk", T),
        (220, 430, "The unlit berth", T),
        (760, 450, "The Tree", T),
        (80, 80, "West Water", W),
    ])
    label("Maiethlir-Plan-Atlas.png", "Maiethlir-Plan-Atlas-Labeled.png", [
        (500, 250, "The Tree", T),
        (780, 340, "Tablet-hall", T),
        (640, 280, "Loft Row", T),
        (576, 70, "Grove Bank", T),
        (80, 400, "Down Gate", T),
        (500, 780, "Slow Water", W),
    ])
    label("Orentel-Plan-Atlas.png", "Orentel-Plan-Atlas-Labeled.png", [
        (360, 120, "The Tree", T),
        (280, 200, "The Rise", T),
        (480, 280, "The Drop", T),
        (520, 640, "First Quay", T),
        (700, 310, "The Third", T),
        (735, 345, "White Note", T),
        (160, 720, "Chart mouth", W),
        (1080, 520, "Crossing-mouth", W),
    ])
    label("Tasain-Plan-Atlas.png", "Tasain-Plan-Atlas-Labeled.png", [
        (690, 370, "The Tree", T),
        (576, 760, "The town gate", T),
    ])
    label("Sanbreo-Plan-Atlas.png", "Sanbreo-Plan-Atlas-Labeled.png", [
        (767, 460, "The slate", T),
        (790, 530, "The shore gate", T),
    ])
    label("Natai-Plan-Atlas.png", "Natai-Plan-Atlas-Labeled.png", [
        (576, 520, "The town gate", T),
        (790, 430, "The Tree", T),
    ])
    label("Eolvaeth-Plan-Atlas.png", "Eolvaeth-Plan-Atlas-Labeled.png", [
        (570, 340, "The Tree", T),
        (680, 420, "The spring", T),
        (576, 520, "The gift-hall", T),
    ])
    label("Harrows-Green-Plan-Atlas.png", "Harrows-Green-Plan-Atlas-Labeled.png", [
        (620, 370, "The Tree", T),
        (620, 500, "The stone", T),
    ])
    label("Mill-hold-Plan-Atlas.png", "Mill-hold-Plan-Atlas-Labeled.png", [
        (576, 400, "The Tree", T),
        (576, 560, "The culvert", T),
        (400, 820, "The mill-race", T),
    ])
    label("Ornsael-Plan-Atlas.png", "Ornsael-Plan-Atlas-Labeled.png", [
        (545, 450, "The Tree", T),
        (470, 490, "The well", T),
        (180, 430, "The west-road", T),
    ])
    label("Nelath-Plan-Atlas.png", "Nelath-Plan-Atlas-Labeled.png", [
        (400, 230, "The Tree", T),
        (500, 480, "The stone", T),
        (980, 360, "The scar", T),
    ])


if __name__ == "__main__":
    main()
