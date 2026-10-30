# Render the favourites mockups to PNG:
#   ../../.venv/bin/python render.py            (all three)
#   ../../.venv/bin/python render.py a-star-and-share.html
import sys, pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
CHROME = str(next(pathlib.Path.home().glob(".cache/ms-playwright/chromium-*/chrome-linux*/chrome")))
WIDTH = {"a-star-and-share.html": 1700, "b-share-view.html": 1200, "c-entry-points.html": 1290,
         "d-between-devices.html": 980}
files = sys.argv[1:] or list(WIDTH)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    for f in files:
        pg = b.new_page(viewport={"width": WIDTH.get(f, 1700), "height": 400}, device_scale_factor=1)
        pg.goto((HERE / f).as_uri())
        pg.wait_for_timeout(500)
        out = HERE / f.replace(".html", ".png")
        pg.screenshot(path=str(out), full_page=True)
        print(out.name)
        pg.close()
    b.close()
