"""Zoomed review crops of the dense areas, with already-recorded labels marked.

Each crop covers SRC x SRC source pixels, upscaled to OUT px. Recorded labels get a red dot and
their id, so a reviewer only has to look for unmarked text.
"""
import csv, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None
root = Path(sys.argv[1])
SRC, OUT, GRID = 700, 1300, 100
# Dense areas (x0, y0, x1, y1) in source pixels: Right Bank core, Cite, Latin Quarter.
AREAS = [(2200, 1300, 5400, 6300), (5400, 2800, 6900, 4800), (6800, 2500, 9300, 5600)]

im = Image.open(root / "source/basel.jpg")
labels = list(csv.DictReader(open(root / "data/labels_inventory.csv")))
out = root / "work/pass2"
out.mkdir(parents=True, exist_ok=True)
font = ImageFont.load_default(size=15)
scale = OUT / SRC
n = 0
for ax0, ay0, ax1, ay1 in AREAS:
    for y0 in range(ay0, ay1, SRC - 100):
        for x0 in range(ax0, ax1, SRC - 100):
            t = im.crop((x0, y0, x0 + SRC, y0 + SRC)).resize((OUT, OUT), Image.LANCZOS)
            d = ImageDraw.Draw(t, "RGBA")
            for g in range((x0 // GRID + 1) * GRID, x0 + SRC, GRID):
                d.line([((g - x0) * scale, 0), ((g - x0) * scale, OUT)], fill=(0, 90, 255, 50))
                d.text(((g - x0) * scale + 2, 2), str(g), fill=(0, 60, 220, 255), font=font)
            for g in range((y0 // GRID + 1) * GRID, y0 + SRC, GRID):
                d.line([(0, (g - y0) * scale), (OUT, (g - y0) * scale)], fill=(0, 90, 255, 50))
                d.text((2, (g - y0) * scale + 2), str(g), fill=(0, 60, 220, 255), font=font)
            for l in labels:
                lx, ly = (int(l["x"]) - x0) * scale, (int(l["y"]) - y0) * scale
                if 0 <= lx < OUT and 0 <= ly < OUT:
                    d.ellipse([lx - 7, ly - 7, lx + 7, ly + 7], fill=(230, 0, 0, 170))
                    d.text((lx + 9, ly - 8), l["id"][1:], fill=(200, 0, 0, 255), font=font,
                           stroke_width=2, stroke_fill=(255, 255, 255, 220))
            t.save(out / f"p{n:03d}_{x0}_{y0}.jpg", quality=85)
            n += 1
print(n, "crops")
