"""Link-preview images: one crop of the scan per place, plus one for the site.

Each place gets a 800x420 JPEG around its label, as printed (east at top), so the label reads
the way it was cut. Output goes to web/public/og/ (gitignored like the tiles; regenerate with
this script). Usage: .venv/bin/python scripts/make_og_images.py .
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw

root = Path(sys.argv[1])
Image.MAX_IMAGE_PIXELS = None
scan = Image.open(root / "source/basel.jpg").convert("RGB")
W, H = scan.size
out = root / "web/public/og"
out.mkdir(parents=True, exist_ok=True)

OW, OH = 800, 420
ZOOM = 1.0  # scan px per output px: the label at its printed size, readable in a small card


def crop(cx, cy, zoom):
    w, h = OW * zoom, OH * zoom
    x0 = min(max(cx - w / 2, 0), W - w)
    y0 = min(max(cy - h / 2, 0), H - h)
    img = scan.crop((round(x0), round(y0), round(x0 + w), round(y0 + h)))
    if img.size != (OW, OH):
        img = img.resize((OW, OH), Image.LANCZOS)
    return img, (cx - x0) / zoom, (cy - y0) / zoom


def ring(img, x, y, orient):
    """A thin red ellipse round the label, wide or tall to follow the lettering."""
    d = ImageDraw.Draw(img)
    rx, ry = (50, 120) if orient == "v" else (120, 50)
    box = (x - rx, y - ry, x + rx, y + ry)
    d.ellipse(box, outline=(255, 255, 255), width=7)
    d.ellipse(box, outline=(178, 34, 34), width=4)


places = json.load(open(root / "web/public/data/places.json"))["places"]
for p in places:
    x, y = p["px"]
    img, mx, my = crop(x, y, ZOOM)
    ring(img, mx, my, p["orient"])
    img.save(out / f"{p['id']}.jpg", quality=60, optimize=True, progressive=True)

# The site card: the Cité and both banks, Notre-Dame near the middle.
img, _, _ = crop(6500, 4100, 4.8)
img.save(out / "site.jpg", quality=80, optimize=True, progressive=True)

total = sum(f.stat().st_size for f in out.glob("*.jpg"))
print(f"{len(places) + 1} images, {total / 1e6:.1f} MB in {out}")
