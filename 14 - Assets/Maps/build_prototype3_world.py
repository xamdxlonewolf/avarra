#!/usr/bin/env python3
"""Build Prototype 3's world sheet from its continent masters.

The continent images are the geographic authority for this prototype. This
script extracts those exact painted landforms and scales them onto one shared
ocean, so the world sheet cannot drift from the zoomed sheets.
"""

from __future__ import annotations

from collections import deque
from pathlib import Path
import shutil

import numpy as np
from PIL import Image, ImageChops, ImageEnhance, ImageFilter


ROOT = Path(__file__).resolve().parent
PROTOTYPE = ROOT / "prototype3"
OUTPUT = PROTOTYPE / "The-Turning-World-Atlas.png"
OCEAN = PROTOTYPE / "Painted-Ocean-Background.png"
SELECTED_FILENAMES = (
    "The-Turning-World-Atlas.png",
    "Maiethorn-Atlas.png",
    "Strandoren-Atlas.png",
    "Heskoren-Atlas.png",
    "Kumbaan-Atlas.png",
)
WIDTH, HEIGHT = 1536, 1024


def largest_component(mask: np.ndarray) -> np.ndarray:
    """Keep the largest connected foreground component in a small mask."""
    height, width = mask.shape
    seen = np.zeros_like(mask, dtype=bool)
    best: list[tuple[int, int]] = []

    for y in range(height):
        for x in range(width):
            if not mask[y, x] or seen[y, x]:
                continue
            seen[y, x] = True
            queue = deque([(x, y)])
            component: list[tuple[int, int]] = []
            while queue:
                px, py = queue.popleft()
                component.append((px, py))
                for nx, ny in (
                    (px - 1, py),
                    (px + 1, py),
                    (px, py - 1),
                    (px, py + 1),
                ):
                    if (
                        0 <= nx < width
                        and 0 <= ny < height
                        and mask[ny, nx]
                        and not seen[ny, nx]
                    ):
                        seen[ny, nx] = True
                        queue.append((nx, ny))
            if len(component) > len(best):
                best = component

    result = np.zeros_like(mask, dtype=bool)
    for x, y in best:
        result[y, x] = True
    return result


def fill_holes(mask: np.ndarray) -> np.ndarray:
    """Fill enclosed gaps such as grey mountain ridges inside a landmass."""
    height, width = mask.shape
    exterior = np.zeros_like(mask, dtype=bool)
    queue: deque[tuple[int, int]] = deque()

    for x in range(width):
        for y in (0, height - 1):
            if not mask[y, x] and not exterior[y, x]:
                exterior[y, x] = True
                queue.append((x, y))
    for y in range(height):
        for x in (0, width - 1):
            if not mask[y, x] and not exterior[y, x]:
                exterior[y, x] = True
                queue.append((x, y))

    while queue:
        px, py = queue.popleft()
        for nx, ny in (
            (px - 1, py),
            (px + 1, py),
            (px, py - 1),
            (px, py + 1),
        ):
            if (
                0 <= nx < width
                and 0 <= ny < height
                and not mask[ny, nx]
                and not exterior[ny, nx]
            ):
                exterior[ny, nx] = True
                queue.append((nx, ny))

    return ~exterior


def extract_land(path: Path) -> Image.Image:
    """Extract one exact painted continent with a feathered coastal edge."""
    source = Image.open(path).convert("RGBA")
    small = source.convert("RGB").resize((384, 256), Image.Resampling.LANCZOS)
    pixels = np.asarray(small, dtype=np.int16)
    red, green, blue = pixels[..., 0], pixels[..., 1], pixels[..., 2]

    # Painted land is warmer than the slate-blue ocean. The broad morphology
    # closes forest/road gaps before selecting the continent, while the hole
    # fill retains grey mountains enclosed by the coast.
    seed = (
        (red > blue + 7)
        & (green > blue - 5)
        & ((red + green + blue) > 145)
    )
    # Exclude each source sheet's decorative frame before component selection.
    seed[:12, :] = False
    seed[-12:, :] = False
    seed[:, :12] = False
    seed[:, -12:] = False
    rough = Image.fromarray(np.uint8(seed) * 255, "L")
    rough = rough.filter(ImageFilter.MaxFilter(7))
    rough = rough.filter(ImageFilter.MinFilter(5))
    component = largest_component(np.asarray(rough) > 127)
    component = fill_holes(component)

    mask = Image.fromarray(np.uint8(component) * 255, "L")
    mask = mask.resize(source.size, Image.Resampling.NEAREST)
    mask = mask.filter(ImageFilter.MaxFilter(3))
    mask = mask.filter(ImageFilter.GaussianBlur(1.5))

    alpha = np.asarray(mask)
    ys, xs = np.where(alpha > 8)
    box = (
        max(0, int(xs.min()) - 8),
        max(0, int(ys.min()) - 8),
        min(source.width, int(xs.max()) + 9),
        min(source.height, int(ys.max()) + 9),
    )
    cutout = source.crop(box)
    cutout.putalpha(mask.crop(box))
    return cutout


def ocean_background() -> Image.Image:
    """Load the painted ocean plate shared by every composited landmass."""
    image = Image.open(OCEAN).convert("RGBA")
    if image.size != (WIDTH, HEIGHT):
        image = image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    return image


def resize_to_fit(image: Image.Image, width: int, height: int) -> Image.Image:
    """Uniformly resize a cutout to fit inside a placement box."""
    scale = min(width / image.width, height / image.height)
    size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    return image.resize(size, Image.Resampling.LANCZOS)


def paste_centered(
    canvas: Image.Image,
    image: Image.Image,
    box: tuple[int, int, int, int],
) -> None:
    left, top, right, bottom = box
    fitted = resize_to_fit(image, right - left, bottom - top)
    fitted = ImageEnhance.Color(fitted).enhance(0.92)
    fitted = ImageEnhance.Contrast(fitted).enhance(0.96)
    x = left + ((right - left) - fitted.width) // 2
    y = top + ((bottom - top) - fitted.height) // 2

    # A dark wet edge and a narrow broken-surf edge seat the cutout into the
    # shared ocean. Both derive from the exact master alpha, so neither changes
    # the coastline.
    alpha = fitted.getchannel("A")
    wet_edge = alpha.filter(ImageFilter.MaxFilter(9)).filter(
        ImageFilter.GaussianBlur(5)
    )
    wet_edge = wet_edge.point(lambda value: round(value * 0.12))
    wet_layer = Image.new("RGBA", fitted.size, (8, 25, 28, 0))
    wet_layer.putalpha(wet_edge)
    canvas.alpha_composite(wet_layer, (x, y + 2))

    outer = alpha.filter(ImageFilter.MaxFilter(5))
    surf = ImageChops.subtract(outer, alpha)
    surf = surf.filter(ImageFilter.GaussianBlur(1))
    surf = surf.point(lambda value: round(value * 0.16))
    surf_layer = Image.new("RGBA", fitted.size, (155, 176, 163, 0))
    surf_layer.putalpha(surf)
    canvas.alpha_composite(surf_layer, (x, y))
    canvas.alpha_composite(fitted, (x, y))


def storm_isle() -> Image.Image:
    """Crop Kumbaan with its exact painted wall rather than a land-only mask."""
    source = Image.open(PROTOTYPE / "Kumbaan-Atlas.png").convert("RGBA")
    # Square crop excludes the sheet border and compass while retaining the
    # complete concentric storm/current/reef system.
    crop = source.crop((250, 18, 1274, 1024))
    crop = ImageEnhance.Contrast(crop).enhance(1.16)
    crop = ImageEnhance.Brightness(crop).enhance(0.90)
    width, height = crop.size
    yy, xx = np.mgrid[0:height, 0:width]
    dx = (xx - width / 2) / (width / 2)
    dy = (yy - height / 2) / (height / 2)
    radius = np.sqrt(dx * dx + dy * dy)
    feather = np.clip((1.0 - radius) / 0.10, 0.0, 1.0)
    existing = np.asarray(crop.getchannel("A"), dtype=np.float32) / 255
    crop.putalpha(Image.fromarray(np.uint8(255 * feather * existing), "L"))
    return crop


def unify_atlas_hand(canvas: Image.Image) -> Image.Image:
    """Apply one final wash and grain over sea and land together."""
    wash = Image.new("RGBA", canvas.size, (34, 53, 46, 12))
    canvas = Image.alpha_composite(canvas, wash)

    rng = np.random.default_rng(20260831)
    noise = rng.normal(128, 18, (HEIGHT, WIDTH)).clip(0, 255).astype(np.uint8)
    grain = Image.fromarray(noise, "L").filter(ImageFilter.GaussianBlur(0.35))
    grain_layer = Image.new("RGBA", canvas.size, (174, 146, 94, 0))
    grain_layer.putalpha(grain.point(lambda value: abs(value - 128) // 5))
    return Image.alpha_composite(canvas, grain_layer)


def main() -> None:
    canvas = ocean_background()

    # The unequal scale is deliberate: Maiethorn is the largest old land,
    # Strandoren is the next great landmass, Heskoren is a smaller rugged
    # frontier, and Kumbaan is a difficult speck inside a disproportionate wall.
    paste_centered(canvas, storm_isle(), (44, 44, 256, 256))
    paste_centered(
        canvas,
        extract_land(PROTOTYPE / "Heskoren-Atlas.png"),
        (34, 456, 534, 966),
    )
    paste_centered(
        canvas,
        extract_land(PROTOTYPE / "Strandoren-Atlas.png"),
        (486, 74, 1092, 808),
    )
    paste_centered(
        canvas,
        extract_land(PROTOTYPE / "Maiethorn-Atlas.png"),
        (1032, 26, 1516, 986),
    )

    canvas = unify_atlas_hand(canvas)
    canvas.convert("RGB").save(OUTPUT, quality=96)
    print(f"Wrote {OUTPUT}")

    # Prototype 3 is the selected atlas. Keep the main handout filenames in
    # lockstep with its masters whenever the world composite is rebuilt.
    for filename in SELECTED_FILENAMES:
        source = PROTOTYPE / filename
        destination = ROOT / filename
        shutil.copyfile(source, destination)
        print(f"Selected {destination}")


if __name__ == "__main__":
    main()
