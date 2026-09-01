#!/usr/bin/env python3
"""Build selected regional sheets as literal Prototype 3 master enlargements.

These four sheets previously drifted because image generation reinterpreted
their geography. Each output now starts with an exact crop of its continent
master. Resampling reveals the existing terrain at regional scale without
inventing a new coastline, watershed, or river network.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, PngImagePlugin


ROOT = Path(__file__).resolve().parent
PROTOTYPE = ROOT / "prototype3"
SIZE = (1536, 1024)


@dataclass(frozen=True)
class Region:
    output: str
    parent: str
    crop: tuple[int, int, int, int]


# Crop boxes are (left, top, right, bottom) in the 1536 x 1024 masters.
# Every box preserves the output's 3:2 aspect ratio.
REGIONS = (
    Region(
        "Sacred-Core-Atlas.png",
        "Maiethorn-Atlas.png",
        (450, 330, 930, 650),
    ),
    Region(
        "Rain-Wall-Atlas.png",
        "Maiethorn-Atlas.png",
        (500, 30, 1100, 430),
    ),
    Region(
        "Chart-Run-Atlas.png",
        "Strandoren-Atlas.png",
        (360, 160, 1320, 800),
    ),
    Region(
        "West-Water-Atlas.png",
        "Strandoren-Atlas.png",
        (0, 280, 960, 920),
    ),
)


def apply_master_frame(image: Image.Image, master: Image.Image) -> Image.Image:
    """Apply the parent's exact bronze rules and corner ornament."""
    result = image.copy()
    band = 24
    result.paste(master.crop((0, 0, SIZE[0], band)), (0, 0))
    result.paste(
        master.crop((0, SIZE[1] - band, SIZE[0], SIZE[1])),
        (0, SIZE[1] - band),
    )
    result.paste(master.crop((0, 0, band, SIZE[1])), (0, 0))
    result.paste(
        master.crop((SIZE[0] - band, 0, SIZE[0], SIZE[1])),
        (SIZE[0] - band, 0),
    )

    # The corner flourishes extend beyond the rule. Copy only warm bronze
    # pixels so no square of the master's ocean comes with the ornament.
    master_pixels = np.asarray(master, dtype=np.int16)
    red, green, blue = (
        master_pixels[..., 0],
        master_pixels[..., 1],
        master_pixels[..., 2],
    )
    warm = (
        (red > blue + 14)
        & (green > blue + 4)
        & (red > green + 4)
        & ((red + green + blue) > 125)
    )
    corner_mask = np.zeros((SIZE[1], SIZE[0]), dtype=np.uint8)
    corner = 96
    for left, top in (
        (0, 0),
        (SIZE[0] - corner, 0),
        (0, SIZE[1] - corner),
        (SIZE[0] - corner, SIZE[1] - corner),
    ):
        area = warm[top : top + corner, left : left + corner]
        corner_mask[top : top + corner, left : left + corner] = area * 255
    mask = Image.fromarray(corner_mask, "L").filter(ImageFilter.GaussianBlur(0.4))
    result.paste(master, (0, 0), mask)
    return result


def build(region: Region) -> None:
    parent_path = PROTOTYPE / region.parent
    master = Image.open(parent_path).convert("RGB")
    if master.size != SIZE:
        raise ValueError(f"{parent_path} must be {SIZE}, found {master.size}")

    crop = master.crop(region.crop)
    image = crop.resize(SIZE, Image.Resampling.LANCZOS)
    # A restrained local-scale lift compensates for enlargement without
    # changing Prototype 3's palette or weather.
    image = ImageEnhance.Sharpness(image).enhance(1.12)
    image = ImageEnhance.Contrast(image).enhance(1.02)
    image = apply_master_frame(image, master)

    metadata = PngImagePlugin.PngInfo()
    metadata.add_text("atlas_parent", f"prototype3/{region.parent}")
    metadata.add_text("atlas_crop", ",".join(map(str, region.crop)))
    metadata.add_text(
        "canon_note",
        "Exact parent geography; incidental painted texture remains non-canon.",
    )
    output = ROOT / region.output
    image.save(output, pnginfo=metadata, optimize=True)
    print(f"Wrote {output} from {parent_path} crop {region.crop}")


def main() -> None:
    for region in REGIONS:
        build(region)


if __name__ == "__main__":
    main()
