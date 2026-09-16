#!/usr/bin/env python3
"""Overlay canonical labels on the selected Sacred Core atlas painting.

The painting supplies texture only. Placement and names come from Named
Ground, the Known Map schematic, the settlement notes, and the R2 prompt.
Rebuild:

    python3 "14 - Assets/Maps/label_sacred_core_atlas.py"

West is left. Thaeloren is the sole exceptional Tree. The Inner Close is a
walled town inside Orenbren, the Third Hearth is a Near Mile road-house, and
Maiethlir is the counted river-city. None receives a capital star.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Sacred-Core-Atlas.png"
OUTPUT = ROOT / "Sacred-Core-Atlas-Labeled.png"

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF = FONT_DIR / "LiberationSerif-Regular.ttf"
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "LiberationSerif-Italic.ttf"

TYPE = (236, 226, 196)
TYPE_MUTED = (220, 208, 176)
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


def hearth_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """A modest road-house diamond, not a settlement or power marker."""
    x, y = xy
    outer = ((x, y - 7), (x + 7, y), (x, y + 7), (x - 7, y))
    inner = ((x, y - 4), (x + 4, y), (x, y + 4), (x - 4, y))
    draw.polygon(outer, fill=MARK_RING)
    draw.polygon(inner, fill=MARK)


def tree_mark(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    """Concentric canopy rings for the one Awakening Tree."""
    x, y = xy
    draw.ellipse((x - 15, y - 15, x + 15, y + 15), outline=MARK_RING, width=3)
    draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill=MARK)
    draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=TYPE_MUTED)


def build() -> Image.Image:
    base = Image.open(SOURCE).convert("RGBA")
    if base.size != (1536, 1024):
        raise SystemExit(f"Expected 1536×1024 Sacred Core master, got {base.size}")

    canvas = base.copy()
    ink = ImageDraw.Draw(canvas)

    title = font(SERIF_BOLD, 32)
    subtitle = font(SERIF_ITALIC, 15)
    place_f = font(SERIF_BOLD, 19)
    caption_f = font(SERIF, 13)
    note = font(SERIF_ITALIC, 13)

    # Sheet title is a scale handle, not a fifth mapped place.
    halo_text(ink, (1255, 90), "SACRED CORE", title, TYPE)
    halo_text(ink, (1255, 120), "the Motherwood", subtitle, TYPE_MUTED, stroke=2)

    # The exceptional canopy in the deep central grove. The college in its
    # shadow is not given a separate throne or capital marker.
    tree_mark(ink, (744, 510))
    leader(ink, (744, 510), (700, 463))
    halo_text(ink, (688, 451), "Thaeloren", place_f, TYPE, anchor="rm")
    halo_text(
        ink,
        (688, 470),
        "the Awakening Tree",
        caption_f,
        TYPE_MUTED,
        anchor="rm",
        stroke=2,
    )

    # The compact's visible walls sit a day's walk from the grove, inside
    # Orenbren lodging-country. The square mark is explicitly not a star.
    close_mark(ink, (374, 770))
    leader(ink, (374, 770), (414, 739))
    halo_text(ink, (424, 730), "Inner Close", place_f, TYPE, anchor="lm")
    halo_text(
        ink,
        (424, 749),
        "walled town, one day out",
        caption_f,
        TYPE_MUTED,
        anchor="lm",
        stroke=2,
    )

    # The old road-house is three days outward on the same Near Mile. It gets
    # a small site glyph rather than a city dot or an invented neighbour label.
    hearth_mark(ink, (267, 333))
    leader(ink, (267, 333), (310, 304))
    halo_text(ink, (320, 295), "Third Hearth", place_f, TYPE, anchor="lm")
    halo_text(
        ink,
        (320, 314),
        "Near Mile road-house",
        caption_f,
        TYPE_MUTED,
        anchor="lm",
        stroke=2,
    )

    # The counted city lies where the Core-thaw slows east of the grove. The
    # river road differs from Orenbren's Near Mile.
    settlement_dot(ink, (1228, 593))
    leader(ink, (1228, 593), (1188, 558))
    halo_text(ink, (1178, 548), "Maiethlir", place_f, TYPE, anchor="rm")
    halo_text(
        ink,
        (1178, 567),
        "counted river-city",
        caption_f,
        TYPE_MUTED,
        anchor="rm",
        stroke=2,
    )

    footer = "Names from Named Ground. Painting is not a survey."
    halo_text(ink, (1190, 991), footer, note, TYPE_MUTED, stroke=2)

    return canvas.convert("RGB")


def main() -> None:
    labeled = build()
    labeled.save(OUTPUT, quality=95)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
