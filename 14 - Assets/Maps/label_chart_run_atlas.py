#!/usr/bin/env python3
"""Overlay canonical labels on the selected Chart-run atlas painting.

The painting supplies texture only. Placement and names come from Named
Ground, the Known Map schematic, the R5 prompt, and the Orentel / White
Note House notes. Rebuild:

    python3 "14 - Assets/Maps/label_chart_run_atlas.py"

West is left. The Chart-run is the interior river running east into the
Salt Quay estuary. The first quay is the old landing below the rise, not
a capital. The White Note is a desk-house on the third quay's north side,
not a crown. Leap-frog warehouses, the south-mouth yards, and filed
river-towns remain unnamed.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Chart-Run-Atlas.png"
OUTPUT = ROOT / "Chart-Run-Atlas-Labeled.png"

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


def quay_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """A small landing, deliberately unlike a settlement or a crown."""
    x, y = xy
    draw.rectangle((x - 9, y - 4, x + 9, y + 4), fill=MARK_RING)
    draw.rectangle((x - 7, y - 2, x + 7, y + 2), fill=MARK)
    draw.line((x - 9, y - 7, x - 9, y + 7), fill=MARK_RING, width=4)
    draw.line((x - 9, y - 6, x - 9, y + 6), fill=MARK, width=2)


def house_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """A desk-house, deliberately unlike a capital star."""
    x, y = xy
    roof = ((x, y - 8), (x + 7, y - 1), (x - 7, y - 1))
    draw.polygon(roof, fill=MARK_RING)
    draw.polygon(((x, y - 6), (x + 5, y - 1), (x - 5, y - 1)), fill=MARK)
    draw.rectangle((x - 5, y - 1, x + 5, y + 7), fill=MARK_RING)
    draw.rectangle((x - 3, y, x + 3, y + 5), fill=MARK)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Chart-run master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 32)
    subtitle = font(SERIF_ITALIC, 15)
    place_f = font(SERIF_BOLD, 19)
    caption_f = font(SERIF, 13)
    river = font(SERIF_BOLD_ITALIC, 19)
    note = font(SERIF_ITALIC, 13)

    # Sheet title sits over the filed hinterland, not in the Old Crossing.
    halo_text(ink, (268, 86), "THE CHART-RUN", title, TYPE)
    halo_text(ink, (268, 116), "Salt Quay hinterland", subtitle, TYPE_MUTED, stroke=2)

    # Hydrology follows the interior river east into the estuary. Do not
    # redraw the water; the label sits on the painted run.
    paste_rotated(canvas, "The Chart-run", river, TYPE_WATER, (490, 492), angle=-9, stroke=2)

    ink = ImageDraw.Draw(canvas)

    # The first quay is the Salt Walk's old landing on the inner south
    # waterfront, below the rise. A landing mark, not a city or capital.
    quay_mark(ink, (1020, 428))
    leader(ink, (1020, 428), (888, 458))
    halo_text(ink, (876, 450), "First Quay", place_f, TYPE, anchor="rm")
    halo_text(ink, (876, 469), "old landing", caption_f, TYPE_MUTED, anchor="rm", stroke=2)

    # The White Note is a desk-house on the third quay, north side. The
    # mark sits on the salt, not on a throne in the Tree-town.
    house_mark(ink, (1098, 352))
    leader(ink, (1098, 352), (1218, 278))
    halo_text(ink, (1230, 270), "The White Note", place_f, TYPE, anchor="lm")
    halo_text(
        ink,
        (1230, 289),
        "desk, not a crown",
        caption_f,
        TYPE_MUTED,
        anchor="lm",
        stroke=2,
    )

    footer = "Names from Named Ground. Painting is not a survey."
    halo_text(ink, (1192, 991), footer, note, TYPE_MUTED, stroke=2)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
