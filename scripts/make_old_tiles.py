"""Cut the Basel plan scan into a 256-px WebP tile pyramid for MapLibre.

Usage:  .venv/bin/python -I scripts/make_old_tiles.py [project_root]

The scan is treated as a flat plane in Web Mercator, NOT as geography: the image's
top-left corner sits at lng/lat (0, 0) (= the centre of the world), image x runs east and
image y runs south, and at tile zoom MAX_ZOOM one image pixel is one tile pixel. So MapLibre
with bearing 0 shows the map exactly as printed (east-up). The app's `src/oldPlane.ts`
mirrors these constants; change both together.

Output (all under web/public/tiles/, which is gitignored):
  tiles/old/{z}/{x}/{y}.webp   tile pyramid, zoom MIN_ZOOM..MAX_ZOOM (edge tiles have alpha)
  tiles/old/meta.json          the parameters below, for reference
  tiles/old-overlay.webp       one downscaled copy (<= OVERLAY_MAX_W wide) for the overlay view

The source image is only read, never modified.
"""
import json
import math
import sys
import time
from pathlib import Path

from PIL import Image

Image.MAX_IMAGE_PIXELS = None

MAX_ZOOM = 14          # tile zoom with full resolution (1 image px = 1 tile px)
MIN_ZOOM = 7           # whole sheet fits in one tile well before this
TILE = 256
QUALITY = 80           # WebP quality for tiles
OVERLAY_MAX_W = 4096
OVERLAY_QUALITY = 70


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    src = root / "source" / "basel.jpg"
    out_root = root / "web" / "public" / "tiles"
    out = out_root / "old"
    out.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    full = Image.open(src)
    full.load()
    if full.mode != "RGB":
        full = full.convert("RGB")
    W, H = full.size
    print(f"source {W}x{H}")

    # Overlay copy first (from the full-resolution image, high-quality filter).
    ow = min(OVERLAY_MAX_W, W)
    oh = round(H * ow / W)
    full.resize((ow, oh), Image.LANCZOS).save(
        out_root / "old-overlay.webp", "WEBP", quality=OVERLAY_QUALITY, method=5)
    print(f"overlay {ow}x{oh}")

    total_files = 0
    total_bytes = 0
    level = full
    for z in range(MAX_ZOOM, MIN_ZOOM - 1, -1):
        if z < MAX_ZOOM:
            # Box-halve the previous level: level pixel i covers image px [i*f, (i+1)*f).
            level = level.reduce(2)
        lw, lh = level.size
        nx, ny = math.ceil(lw / TILE), math.ceil(lh / TILE)
        origin = 2 ** (z - 1)  # tile index of the world centre at this zoom
        for ty in range(ny):
            for tx in range(nx):
                box = (tx * TILE, ty * TILE, min((tx + 1) * TILE, lw), min((ty + 1) * TILE, lh))
                crop = level.crop(box)
                if crop.size != (TILE, TILE):
                    tile = Image.new("RGBA", (TILE, TILE), (0, 0, 0, 0))
                    tile.paste(crop, (0, 0))
                else:
                    tile = crop
                d = out / str(z) / str(origin + tx)
                d.mkdir(parents=True, exist_ok=True)
                p = d / f"{origin + ty}.webp"
                tmp = p.with_suffix(".webp.tmp")
                tile.save(tmp, "WEBP", quality=QUALITY, method=4)
                tmp.replace(p)
                total_files += 1
                total_bytes += p.stat().st_size
        print(f"z{z}: {lw}x{lh} -> {nx}x{ny} tiles  ({time.time() - t0:.0f}s)")

    meta = {
        "source": "source/basel.jpg",
        "width": W,
        "height": H,
        "tileSize": TILE,
        "minzoom": MIN_ZOOM,
        "maxzoom": MAX_ZOOM,
        "placement": "image top-left at lng/lat (0,0); x east, y south; 1 image px = 1 tile px at maxzoom",
        "overlay": {"file": "old-overlay.webp", "width": ow, "height": oh},
        "tiles": total_files,
        "bytes": total_bytes,
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    }
    (out / "meta.json").write_text(json.dumps(meta, indent=1), encoding="utf-8", newline="\n")
    print(f"{total_files} tiles, {total_bytes / 1e6:.1f} MB, {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
