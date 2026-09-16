#!/usr/bin/env python3
"""Overlay canonical labels on the selected Maiethorn atlas painting.

The painting supplies texture only. Placement and names come from Named
Ground, the Known Map schematic, and the C1 prompt. Rebuild:

    python3 "14 - Assets/Maps/label_maiethorn_atlas.py"

West is left. The Rain-Wall divides the wet Motherland from the dry
Rain-Shadow. Thaeloren is the sole exceptional Tree; its marker is a
canopy ring, never a capital star. The Inner Close remains inside
Orenbren and is not a sixteenth power.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Maiethorn-Atlas.png"
OUTPUT = ROOT / "Maiethorn-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF = FONT_DIR / "LiberationSerif-Regular.ttf"
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


def leader(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int]) -> None:
    draw.line((start, end), fill=MARK_RING, width=3)
    draw.line((start, end), fill=STROKE, width=1)


def settlement_dot(draw: ImageDraw.ImageDraw, xy: tuple[int, int], radius: int = 5) -> None:
    x, y = xy
    draw.ellipse(
        (x - radius - 2, y - radius - 2, x + radius + 2, y + radius + 2),
        fill=MARK_RING,
    )
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=MARK)


def close_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """A small walled-town square, deliberately unlike a capital star."""
    x, y = xy
    draw.rectangle((x - 7, y - 7, x + 7, y + 7), fill=MARK_RING)
    draw.rectangle((x - 5, y - 5, x + 5, y + 5), fill=MARK)
    draw.rectangle((x - 2, y - 2, x + 2, y + 2), fill=TYPE_MUTED)


def tree_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """Concentric canopy rings for the one Awakening Tree."""
    x, y = xy
    draw.ellipse((x - 14, y - 14, x + 14, y + 14), outline=MARK_RING, width=3)
    draw.ellipse((x - 9, y - 9, x + 9, y + 9), fill=MARK)
    draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=TYPE_MUTED)


def place(
    draw: ImageDraw.ImageDraw,
    name: str,
    xy: tuple[int, int],
    typeface: ImageFont.FreeTypeFont,
    *,
    caption: str | None = None,
    caption_font: ImageFont.FreeTypeFont | None = None,
    off: tuple[int, int] = (16, -18),
    anchor: str = "lm",
    radius: int = 5,
) -> None:
    settlement_dot(draw, xy, radius)
    label_xy = (xy[0] + off[0], xy[1] + off[1])
    leader(
        draw,
        xy,
        (
            label_xy[0] + (-10 if off[0] > 0 else 10),
            label_xy[1] + (6 if off[1] < 0 else -6),
        ),
    )
    halo_text(draw, label_xy, name, typeface, TYPE, anchor=anchor)
    if caption and caption_font:
        caption_y = label_xy[1] + (17 if off[1] <= 0 else -17)
        halo_text(
            draw,
            (label_xy[0], caption_y),
            caption,
            caption_font,
            TYPE_MUTED,
            anchor=anchor,
            stroke=2,
        )


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Maiethorn master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 32)
    subtitle = font(SERIF_ITALIC, 15)
    region = font(SERIF_BOLD_ITALIC, 24)
    area = font(SERIF_BOLD, 20)
    place_f = font(SERIF_BOLD, 19)
    caption_f = font(SERIF, 13)
    terrain = font(SERIF_ITALIC, 17)
    small = font(SERIF_ITALIC, 14)
    note = font(SERIF_ITALIC, 13)

    # Quiet western water carries the sheet title, away from the wind-rose.
    halo_text(ink, (160, 94), "MAIETHORN", title, TYPE)
    halo_text(ink, (160, 124), "the Motherland", subtitle, TYPE_MUTED, stroke=2)

    # The Old Crossing face: a coast-region, not a single invented port.
    paste_rotated(canvas, "the Hinge Shore", region, TYPE_WATER, (244, 466), angle=78)

    # The exceptional canopy sits in the circular old-growth heart.
    ink = ImageDraw.Draw(canvas)
    tree_mark(ink, (622, 468))
    leader(ink, (622, 468), (594, 433))
    halo_text(ink, (586, 420), "Thaeloren", place_f, TYPE, anchor="rm")
    halo_text(ink, (586, 439), "the Awakening Tree", caption_f, TYPE_MUTED, anchor="rm", stroke=2)

    # Orenbren is the lodging country around the grove. The Close is a town
    # inside it, one day's walk from Thaeloren, and receives no capital star.
    halo_text(ink, (562, 592), "ORENBREN", area, TYPE)
    halo_text(ink, (562, 613), "lodging country", caption_f, TYPE_MUTED, stroke=2)
    close_mark(ink, (686, 510))
    leader(ink, (686, 510), (716, 488))
    halo_text(ink, (724, 481), "Inner Close", place_f, TYPE, anchor="lm")
    halo_text(ink, (724, 500), "inside Orenbren", caption_f, TYPE_MUTED, anchor="lm", stroke=2)

    # Core-thaw leaves the west face of the divide and slows near Maiethlir.
    paste_rotated(canvas, "the Core-thaw", terrain, TYPE_WATER, (594, 337), angle=8, stroke=2)
    ink = ImageDraw.Draw(canvas)
    place(
        ink,
        "Maiethlir",
        (514, 354),
        place_f,
        caption="Threnmaieth",
        caption_font=caption_f,
        off=(-22, -29),
        anchor="rm",
    )

    # Two distinct notches through the irregular Rain-Wall. Noon is the older,
    # higher northern notch; Shelf-gate is the lower road left after the Break.
    paste_rotated(canvas, "Noon Pass", small, TYPE, (833, 300), angle=67, stroke=2)
    paste_rotated(canvas, "Shelf-gate", small, TYPE, (802, 604), angle=72, stroke=2)

    # Broad climate label east of the watershed, not a border or polity fill.
    paste_rotated(canvas, "RAIN-SHADOW", region, TYPE, (1124, 646), angle=-8)
    paste_rotated(canvas, "dry hills and well-country", small, TYPE_MUTED, (1124, 677), angle=-8, stroke=2)

    footer = "Names from Named Ground. Painting is not a survey."
    halo_text(ink, (1192, 991), footer, note, TYPE_MUTED, stroke=2)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
