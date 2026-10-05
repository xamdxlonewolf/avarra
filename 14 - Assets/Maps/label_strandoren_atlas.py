#!/usr/bin/env python3
"""Overlay canonical labels on the selected Strandoren atlas painting.

The painting supplies texture only. Placement and names come from Named
Ground, the Known Map schematic, and the C2 prompt. Rebuild:

    python3 "14 - Assets/Maps/label_strandoren_atlas.py"

West is left. Orentel sits at the large eastern estuary on the Old
Crossing face. Lunbra is on the Chart-run, days upriver. Raitin is the
river behind that coast, and that river is not the Chart-run. Naenor
keeps its own coast. Braetu is the Night Shore. No capital star.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from label_curves import cubic, paste_along_path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Strandoren-Atlas.png"
OUTPUT = ROOT / "Strandoren-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "LiberationSerif-Italic.ttf"
SERIF_BOLD_ITALIC = FONT_DIR / "LiberationSerif-BoldItalic.ttf"

TYPE = (236, 226, 196)
TYPE_MUTED = (220, 208, 176)
TYPE_WATER = (214, 228, 230)
STROKE = (28, 22, 14)
MARK = (28, 24, 16)
MARK_RING = (236, 226, 200)


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def halo_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    typeface: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    *,
    anchor: str = "mm",
    stroke: int = 3,
) -> None:
    draw.text(
        xy,
        text,
        font=typeface,
        fill=fill,
        anchor=anchor,
        stroke_width=stroke,
        stroke_fill=STROKE,
    )


def measure(typeface: ImageFont.FreeTypeFont, text: str) -> tuple[int, int]:
    bbox = typeface.getbbox(text)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def paste_rotated(
    canvas: Image.Image,
    text: str,
    typeface: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    centre: tuple[int, int],
    angle: float,
    stroke: int = 3,
) -> None:
    width, height = measure(typeface, text)
    pad = stroke * 2 + 10
    layer = Image.new("RGBA", (width + pad * 2, height + pad * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    halo_text(
        draw,
        (layer.width // 2, layer.height // 2),
        text,
        typeface,
        fill,
        stroke=stroke,
    )
    rotated = layer.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    canvas.paste(
        rotated,
        (centre[0] - rotated.width // 2, centre[1] - rotated.height // 2),
        rotated,
    )


def settlement_dot(draw: ImageDraw.ImageDraw, xy: tuple[int, int], radius: int = 5) -> None:
    x, y = xy
    draw.ellipse(
        (x - radius - 2, y - radius - 2, x + radius + 2, y + radius + 2),
        fill=MARK_RING,
    )
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=MARK)


def leader(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int]) -> None:
    draw.line((start, end), fill=MARK_RING, width=3)
    draw.line((start, end), fill=STROKE, width=1)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Strandoren master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 32)
    region = font(SERIF_BOLD_ITALIC, 24)
    place_f = font(SERIF_BOLD, 20)
    river = font(SERIF_BOLD_ITALIC, 19)

    halo_text(ink, (1358, 92), "STRANDOREN", title, TYPE)

    # Orentel is the large salt-city at the eastern estuary. A plain dot marks
    # the settlement; it is Lestrand's seat without becoming a capital star.
    settlement_dot(ink, (1088, 454))
    leader(ink, (1088, 454), (1222, 431))
    halo_text(ink, (1232, 422), "Orentel", place_f, TYPE, anchor="lm")

    # The broad interior run reaches Orentel from the west.
    paste_along_path(
        canvas,
        "The Chart-run",
        river,
        TYPE_WATER,
        cubic((500, 545), (660, 575), (820, 560), (990, 530)),
        stroke=2,
    )

    # Trenledd is the filed country. Lunbra is the city on the Chart-run,
    # inland of the salt, not a second Orentel and not a filed river-town.
    paste_rotated(canvas, "TRENLEDD", region, TYPE, (820, 393), angle=-4)
    ink = ImageDraw.Draw(canvas)
    settlement_dot(ink, (662, 488))
    leader(ink, (662, 488), (560, 430))
    halo_text(ink, (548, 430), "Lunbra", place_f, TYPE, anchor="rm")

    # Raitin is behind the premier coast, on a river that is not the
    # Chart-run. The six charter-towns stay unnamed.
    settlement_dot(ink, (920, 640))
    leader(ink, (920, 640), (860, 700))
    halo_text(ink, (848, 708), "Raitin", place_f, TYPE, anchor="rm")

    # Naenor is its own indented coast, south of the filed interior.
    # Not the estuary, not the Night Shore, not the Chart-run.
    settlement_dot(ink, (782, 842))
    leader(ink, (782, 842), (700, 768))
    halo_text(ink, (688, 768), "Naenor", place_f, TYPE, anchor="rm")

    # Netstrand names the open-ocean west and south face. Braetu is the
    # harbour on that face. The coast stays area-type.
    paste_rotated(canvas, "NETSTRAND", region, TYPE, (340, 700), angle=11)
    ink = ImageDraw.Draw(canvas)
    settlement_dot(ink, (450, 640))
    leader(ink, (450, 640), (520, 590))
    halo_text(ink, (532, 582), "Braetu", place_f, TYPE, anchor="lm")

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
