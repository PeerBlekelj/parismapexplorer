"""Crop a region of the scan, upscale, and draw a fine labelled grid (for picking feature pixels).
usage: crop_grid.py ROOT OUT x0 y0 x1 y1 [grid=50] [scale=2]"""
import sys
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None
root, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
grid = int(sys.argv[7]) if len(sys.argv) > 7 else 50
sc = float(sys.argv[8]) if len(sys.argv) > 8 else 2
im = Image.open(f"{root}/source/basel.jpg").crop((x0, y0, x1, y1))
im = im.resize((int((x1 - x0) * sc), int((y1 - y0) * sc)), Image.LANCZOS)
d = ImageDraw.Draw(im, "RGBA"); f = ImageFont.load_default(size=14)
for g in range((x0 // grid + 1) * grid, x1, grid):
    X = (g - x0) * sc; strong = g % (grid * 2) == 0
    d.line([(X, 0), (X, im.height)], fill=(0, 80, 255, 120 if strong else 55))
    if strong: d.text((X + 2, 2), str(g), fill=(0, 50, 220), font=f)
for g in range((y0 // grid + 1) * grid, y1, grid):
    Y = (g - y0) * sc; strong = g % (grid * 2) == 0
    d.line([(0, Y), (im.width, Y)], fill=(0, 80, 255, 120 if strong else 55))
    if strong: d.text((2, Y + 2), str(g), fill=(0, 50, 220), font=f)
im.save(out, quality=88)
