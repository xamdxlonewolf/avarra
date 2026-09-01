#!/usr/bin/env python3
"""Overlay Named Ground labels on the selected Heskoren atlas painting.

The painting stays the geographic texture. Names come from Named Ground,
the Known Map schematic, and the playable squares — not from incidental
generated roofs or field-grids. Seats follow the vault, not the largest
painted cluster. Rebuild:

    python3 "14 - Assets/Maps/label_heskoren_atlas.py"

West is left. East is right. Heskoren's east sea is the West Water
(toward Strandoren). The storm-wall is west, past the last capes.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Heskoren-Atlas.png"
OUTPUT = ROOT / "Heskoren-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF = FONT_DIR / "LiberationSerif-Regular.ttf"
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "LiberationSerif-Italic.ttf"
SERIF_BOLD_ITALIC = FONT_DIR / "LiberationSerif-BoldItalic.ttf"

TYPE = (236, 226, 196)
TYPE_MUTED = (220, 208, 176)
TYPE_WATER = (214, 228, 230)
STROKE = (28, 22, 14)
DOT = (28, 24, 16)
DOT_RING = (236, 226, 200)


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
    w, h = measure(typeface, text)
    pad = stroke * 2 + 10
    layer = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    halo_text(
        draw,
        (layer.size[0] // 2, layer.size[1] // 2),
        text,
        typeface,
        fill,
        stroke=stroke,
    )
    rotated = layer.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    canvas.paste(
        rotated,
        (centre[0] - rotated.size[0] // 2, centre[1] - rotated.size[1] // 2),
        rotated,
    )


def settlement_dot(draw: ImageDraw.ImageDraw, xy: tuple[int, int], radius: int = 5) -> None:
    x, y = xy
    draw.ellipse((x - radius - 2, y - radius - 2, x + radius + 2, y + radius + 2), fill=DOT_RING)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=DOT)


def leader(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int]) -> None:
    draw.line((start, end), fill=DOT_RING, width=3)
    draw.line((start, end), fill=STROKE, width=1)


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
    stroke: int = 3,
) -> None:
    """Dot on the painted hearth; type offset so it does not sit on the roofs."""
    settlement_dot(draw, xy, radius)
    lx, ly = xy[0] + off[0], xy[1] + off[1]
    if abs(off[0]) >= 16 or abs(off[1]) >= 16:
        tip_x = lx + (-10 if off[0] > 0 else 10 if off[0] < 0 else 0)
        tip_y = ly + (6 if off[1] < 0 else -6 if off[1] > 0 else 0)
        leader(draw, xy, (tip_x, tip_y))
    halo_text(draw, (lx, ly), name, typeface, TYPE, anchor=anchor, stroke=stroke)
    if caption and caption_font:
        cap_off = 16 if off[1] <= 0 else -16
        halo_text(
            draw,
            (lx, ly + cap_off),
            caption,
            caption_font,
            TYPE_MUTED,
            anchor=anchor,
            stroke=2,
        )


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Heskoren master, got {base.size}")

    canvas = base.copy()

    title = font(SERIF_BOLD, 32)
    subtitle = font(SERIF_ITALIC, 15)
    place_f = font(SERIF_BOLD, 20)
    hamlet_f = font(SERIF_BOLD, 16)
    caption_f = font(SERIF, 13)
    water = font(SERIF_BOLD_ITALIC, 24)
    river = font(SERIF_ITALIC, 17)
    note = font(SERIF_ITALIC, 13)

    # Continent name as sea-type in the far south-west water. No cartouche on land.
    ink = ImageDraw.Draw(canvas)
    halo_text(ink, (118, 948), "HESKOREN", title, TYPE, stroke=3)
    halo_text(ink, (118, 978), "the Sundered Reach", subtitle, TYPE_MUTED, stroke=2)

    # East sea = the West Water (Named Ground): between Heskoren and Strandoren.
    paste_rotated(canvas, "the West Water", water, TYPE_WATER, (1272, 430), angle=-10)
    paste_rotated(canvas, "to Strandoren", note, TYPE_WATER, (1288, 468), angle=-10)
    # West sea = last capes, then the storm-wall. The NE cloud bank is weather, not that wall.
    paste_rotated(canvas, "toward the storm-wall", note, TYPE_WATER, (96, 360), angle=78)
    ink = ImageDraw.Draw(canvas)

    # West face — storm-side capes, slate-shore, Ornled pocket, empty marches.
    halo_text(ink, (188, 148), "the last capes", note, TYPE_MUTED, stroke=2)
    halo_text(ink, (248, 568), "slate-shore", note, TYPE_MUTED, stroke=2)
    halo_text(ink, (400, 300), "marches", note, TYPE_MUTED, stroke=2)
    place(
        ink,
        "Ornled",
        (360, 520),
        place_f,
        caption="Outer Ledger",
        caption_font=caption_f,
        off=(-70, -8),
        anchor="rm",
    )

    # Live-front rise east of the highland spine (grove-town, not a capital).
    place(
        ink,
        "Harrow's",
        (638, 432),
        place_f,
        caption="Saelvaeth",
        caption_font=caption_f,
        off=(18, -26),
        anchor="lm",
    )
    # Rise-water is a low local stream, not the east-coast river.
    paste_rotated(canvas, "Rise-water", river, TYPE_WATER, (708, 488), angle=-32)
    ink = ImageDraw.Draw(canvas)
    settlement_dot(ink, (800, 535), radius=3)
    halo_text(ink, (800, 518), "the ford", hamlet_f, TYPE, anchor="mm", stroke=2)

    # Three hearths past the ford — Seat still does not use these names.
    # Ornath sits the "other way" toward Ornled's slate.
    place(ink, "Brenod", (778, 502), hamlet_f, off=(14, -16), anchor="lm", radius=3, stroke=2)
    place(ink, "Vaelun", (808, 552), hamlet_f, off=(18, 10), anchor="lm", radius=3, stroke=2)
    place(ink, "Ornath", (738, 588), hamlet_f, off=(-14, 10), anchor="rm", radius=3, stroke=2)
    halo_text(ink, (690, 368), "live front", note, TYPE_MUTED, stroke=2)

    # Eolvaeth: vale behind the Strandoren-facing (east) coast, NE of Harrow's.
    # Not the south-east field-grid. Not a west-coast pocket.
    place(
        ink,
        "Eolvaeth",
        (940, 392),
        place_f,
        caption="Vaethorn",
        caption_font=caption_f,
        off=(-16, -28),
        anchor="rm",
    )
    halo_text(ink, (880, 328), "waiting vale", note, TYPE_MUTED, stroke=2)
    halo_text(ink, (1210, 500), "frontier coast", note, TYPE_MUTED, stroke=2)

    # Guest-grove in the Yield, a day's walk from Vaelun away from Harrow's.
    place(
        ink,
        "the First Bowl",
        (888, 792),
        hamlet_f,
        caption="Lonasir",
        caption_font=caption_f,
        off=(18, -22),
        anchor="lm",
        radius=4,
        stroke=2,
    )
    # Vaelhesk is the land, not a cape-town.
    halo_text(ink, (800, 818), "Vaelhesk", place_f, TYPE, stroke=3)
    halo_text(ink, (800, 838), "the Far Yield", caption_f, TYPE_MUTED, stroke=2)

    footer = "Names from Named Ground. Painting is not a survey."
    halo_text(ink, (768, 992), footer, note, TYPE_MUTED, stroke=2)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
