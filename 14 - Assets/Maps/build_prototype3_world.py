#!/usr/bin/env python3
"""Build Prototype 3's world sheet from its continent masters.

The continent images are the geographic authority for this prototype. This
script extracts those exact painted landforms and scales them onto one shared
ocean, so the world sheet cannot drift from the zoomed sheets.
"""

from __future__ import annotations

from collections import deque
from pathlib import Path
import random

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parent
PROTOTYPE = ROOT / "prototype3"
OUTPUT = PROTOTYPE / "The-Turning-World-Atlas.png"
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
    rough = rough.filter(ImageFilter.MaxFilter(11))
    rough = rough.filter(ImageFilter.MinFilter(7))
    component = largest_component(np.asarray(rough) > 127)
    component = fill_holes(component)

    mask = Image.fromarray(np.uint8(component) * 255, "L")
    mask = mask.resize(source.size, Image.Resampling.NEAREST)
    mask = mask.filter(ImageFilter.MaxFilter(9))
    mask = mask.filter(ImageFilter.GaussianBlur(5))

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
    """Create a dark portolan ocean while retaining the established frame."""
    rng = np.random.default_rng(20260831)
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    vertical = np.linspace(0, 1, HEIGHT, dtype=np.float32)[:, None]
    base[..., 0] = 25 + 6 * vertical
    base[..., 1] = 48 + 8 * vertical
    base[..., 2] = 52 + 10 * vertical

    noise = rng.normal(0, 1, (HEIGHT // 8, WIDTH // 8)).astype(np.float32)
    texture = Image.fromarray(np.uint8(np.clip(128 + noise * 26, 0, 255)), "L")
    texture = texture.resize((WIDTH, HEIGHT), Image.Resampling.BICUBIC)
    texture = texture.filter(ImageFilter.GaussianBlur(5))
    grain = (np.asarray(texture, dtype=np.float32) - 128) / 11
    base += grain[..., None]

    image = Image.fromarray(np.uint8(np.clip(base, 0, 255)), "RGB").convert("RGBA")
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay, "RGBA")

    # Faint graticule and current-lines.
    for x in range(80, WIDTH, 112):
        draw.line((x, 24, x, HEIGHT - 24), fill=(177, 151, 100, 10), width=1)
    for y in range(72, HEIGHT, 112):
        draw.line((24, y, WIDTH - 24, y), fill=(177, 151, 100, 9), width=1)
    for offset in range(-HEIGHT, WIDTH, 210):
        draw.line(
            (offset, HEIGHT - 24, offset + HEIGHT, 24),
            fill=(177, 151, 100, 6),
            width=1,
        )

    return Image.alpha_composite(image, overlay)


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
    x = left + ((right - left) - fitted.width) // 2
    y = top + ((bottom - top) - fitted.height) // 2
    canvas.alpha_composite(fitted, (x, y))


def storm_isle() -> Image.Image:
    """Crop Kumbaan with its exact painted wall rather than a land-only mask."""
    source = Image.open(PROTOTYPE / "Kumbaan-Atlas.png").convert("RGBA")
    # Square crop excludes the sheet border and compass while retaining the
    # complete concentric storm/current/reef system.
    crop = source.crop((250, 18, 1274, 1024))
    width, height = crop.size
    yy, xx = np.mgrid[0:height, 0:width]
    dx = (xx - width / 2) / (width / 2)
    dy = (yy - height / 2) / (height / 2)
    radius = np.sqrt(dx * dx + dy * dy)
    feather = np.clip((1.0 - radius) / 0.10, 0.0, 1.0)
    existing = np.asarray(crop.getchannel("A"), dtype=np.float32) / 255
    crop.putalpha(Image.fromarray(np.uint8(255 * feather * existing), "L"))
    return crop


def draw_compass(canvas: Image.Image) -> None:
    draw = ImageDraw.Draw(canvas, "RGBA")
    cx, cy, radius = 755, 875, 61
    ink = (155, 111, 54, 205)
    faint = (205, 170, 104, 95)
    draw.ellipse(
        (cx - radius, cy - radius, cx + radius, cy + radius),
        outline=faint,
        width=2,
    )
    for step in range(16):
        angle = np.pi * step / 8
        inner = 11 if step % 2 == 0 else 19
        outer = radius if step % 2 == 0 else 43
        x1 = cx + int(np.sin(angle) * inner)
        y1 = cy - int(np.cos(angle) * inner)
        x2 = cx + int(np.sin(angle) * outer)
        y2 = cy - int(np.cos(angle) * outer)
        draw.line((x1, y1, x2, y2), fill=ink if step % 2 == 0 else faint, width=2)
    draw.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), outline=ink, width=2)


def restore_frame(canvas: Image.Image) -> None:
    """Copy the established Prototype 3 parchment frame over the composite."""
    frame = Image.open(OUTPUT).convert("RGBA")
    strips = (
        (0, 0, WIDTH, 28),
        (0, HEIGHT - 28, WIDTH, HEIGHT),
        (0, 0, 28, HEIGHT),
        (WIDTH - 28, 0, WIDTH, HEIGHT),
    )
    for box in strips:
        canvas.alpha_composite(frame.crop(box), (box[0], box[1]))


def main() -> None:
    canvas = ocean_background()

    # Placement preserves the chosen reference relationship while allowing
    # each exact continent-master silhouette to determine its own proportions.
    paste_centered(canvas, storm_isle(), (28, 30, 344, 346))
    paste_centered(
        canvas,
        extract_land(PROTOTYPE / "Heskoren-Atlas.png"),
        (34, 382, 615, 994),
    )
    paste_centered(
        canvas,
        extract_land(PROTOTYPE / "Strandoren-Atlas.png"),
        (594, 40, 1118, 754),
    )
    paste_centered(
        canvas,
        extract_land(PROTOTYPE / "Maiethorn-Atlas.png"),
        (1095, 22, 1514, 995),
    )

    draw_compass(canvas)
    restore_frame(canvas)
    canvas.convert("RGB").save(OUTPUT, quality=96)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    random.seed(20260831)
    main()
