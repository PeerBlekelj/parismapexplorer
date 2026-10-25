import io, math, base64, sys, urllib.request
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
root = sys.argv[1]
im = Image.open(f"{root}/source/basel.jpg")
# Ile de la Cite + both banks; map is east-up, rotate clockwise -> north-up
old = im.crop((5200, 2700, 7300, 5700)).rotate(-90, expand=True)
old = old.resize((1100, int(1100 * old.height / old.width)), Image.LANCZOS)
old.save(f"{root}/mockups/_old_cite.jpg", quality=80)
# label detail for the info card
im.crop((6370, 3330, 6650, 3625)).save(f"{root}/mockups/_nd_label.jpg", quality=85)

z = 16
def tile(lat, lon):
    n = 2 ** z
    x = (lon + 180) / 360 * n
    y = (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n
    return x, y
cx, cy = tile(48.8540, 2.3470)
x0, y0 = int(cx) - 2, int(cy) - 1
W, H = 5, 3
mosaic = Image.new("RGB", (W * 256, H * 256))
for i in range(W):
    for j in range(H):
        url = f"https://tile.openstreetmap.org/{z}/{x0+i}/{y0+j}.png"
        req = urllib.request.Request(url, headers={"User-Agent": "paris-1550-mockup/0.1"})
        mosaic.paste(Image.open(io.BytesIO(urllib.request.urlopen(req).read())).convert("RGB"), (i * 256, j * 256))
mosaic.save(f"{root}/mockups/_modern_cite.jpg", quality=82)
print("ok", old.size, mosaic.size)
