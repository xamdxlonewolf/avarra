#!/usr/bin/env python3
"""Overlay canonical labels on the selected Live Front atlas painting.

The painting supplies texture only. Placement and names come from Named
Ground, the Known Map schematic, the R7 prompt, and the Harrow's Green /
Three Hamlets notes. Rebuild:

    python3 "14 - Assets/Maps/label_live_front_atlas.py"

West is left. Harrow's is a plain grove-town on the rise, not a capital.
The Rise-water is the low stream from that rise to the ford. Brenod,
Vaelun, and Ornath are three small downstream hearths on different
ground. The ford, the cup-rock, distant canopy-pockets, and incidental
roofs remain unnamed.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from label_curves import cubic, paste_along_path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Live-Front-Atlas.png"
OUTPUT = ROOT / "Live-Front-Atlas-Labeled.png"

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
    """A plain town or hamlet mark. Never a capital star or canopy-ring."""
    x, y = xy
    draw.ellipse(
        (x - radius - 2, y - radius - 2, x + radius + 2, y + radius + 2),
        fill=MARK_RING,
    )
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=MARK)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Live Front master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 32)
    place_f = font(SERIF_BOLD, 19)
    hamlet_f = font(SERIF_BOLD, 16)
    river = font(SERIF_BOLD_ITALIC, 18)

    # Region name in the empty north-east mist.
    halo_text(ink, (1248, 96), "THE LIVE FRONT", title, TYPE)

    # Harrow's is the grove-town on the rise. Plain settlement mark on
    # the canopy. The name sits in the open margin above the roofs.
    settlement_dot(ink, (348, 198), radius=5)
    leader(ink, (348, 198), (250, 150))
    halo_text(ink, (238, 150), "Harrow's", place_f, TYPE, anchor="rm")

    # Hydrology follows the low stream off the rise. The ford stays unnamed.
    paste_along_path(
        canvas,
        "The Rise-water",
        river,
        TYPE_WATER,
        cubic((430, 250), (500, 300), (640, 340), (760, 450)),
        stroke=2,
    )

    ink = ImageDraw.Draw(canvas)

    # Three hearths past the ford, on different ground. Small dots, not
    # a city. Folk names the Seat still does not use.
    # Brenod: sending hearth on the Harrow road, just past the crossing.
    settlement_dot(ink, (1088, 602), radius=3)
    leader(ink, (1088, 602), (1200, 528))
    halo_text(ink, (1212, 520), "Brenod", hamlet_f, TYPE, anchor="lm", stroke=2)

    # Vaelun: old taken plot on the wetter shelf by the continuing water.
    settlement_dot(ink, (1250, 708), radius=3)
    leader(ink, (1250, 708), (1360, 748))
    halo_text(ink, (1372, 742), "Vaelun", hamlet_f, TYPE, anchor="lm", stroke=2)

    # Ornath: thinner rise, furthest in the other-road direction.
    settlement_dot(ink, (980, 812), radius=3)
    leader(ink, (980, 812), (860, 872))
    halo_text(ink, (848, 866), "Ornath", hamlet_f, TYPE, anchor="rm", stroke=2)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
