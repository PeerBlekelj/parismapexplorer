"""Cut the scan into overlapping reading tiles with a coordinate grid (full-image pixels)."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None
root = Path(sys.argv[1])
SIZE, STEP, GRID = 1300, 1000, 100
im = Image.open(root / "source/basel.jpg")
out = root / "work/tiles"
out.mkdir(parents=True, exist_ok=True)
font = ImageFont.load_default(size=16)

cols = range(0, im.width - 100, STEP)
rows = range(0, im.height - 100, STEP)
for r, y0 in enumerate(rows):
    for c, x0 in enumerate(cols):
        x1, y1 = min(x0 + SIZE, im.width), min(y0 + SIZE, im.height)
        t = im.crop((x0, y0, x1, y1)).convert("RGB")
        d = ImageDraw.Draw(t, "RGBA")
        for gx in range((x0 // GRID + 1) * GRID, x1, GRID):
            d.line([(gx - x0, 0), (gx - x0, t.height)], fill=(0, 90, 255, 70), width=1)
            d.text((gx - x0 + 2, 2), str(gx), fill=(0, 60, 220, 255), font=font)
        for gy in range((y0 // GRID + 1) * GRID, y1, GRID):
            d.line([(0, gy - y0), (t.width, gy - y0)], fill=(0, 90, 255, 70), width=1)
            d.text((2, gy - y0 + 2), str(gy), fill=(0, 60, 220, 255), font=font)
        t.save(out / f"r{r:02d}c{c:02d}.jpg", quality=88)

# index sheet: overview with tile ids
ov = im.resize((im.width // 6, im.height // 6))
d = ImageDraw.Draw(ov)
for r, y0 in enumerate(rows):
    for c, x0 in enumerate(cols):
        d.rectangle([x0 // 6, y0 // 6, (x0 + STEP) // 6, (y0 + STEP) // 6], outline=(255, 0, 0))
        d.text((x0 // 6 + 4, y0 // 6 + 4), f"r{r}c{c}", fill=(255, 0, 0), font=font)
ov.save(out.parent / "tile_index.jpg", quality=85)
print(len(rows), "rows x", len(cols), "cols")
