import sys
from playwright.sync_api import sync_playwright
root = sys.argv[1]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=sys.argv[2])
    pg = b.new_page(viewport={"width": 1600, "height": 950})
    pg.goto(f"file://{root}/mockups/layouts.html")
    for i, l in enumerate(["l1", "l2", "l3"], 1):
        pg.click(f"header.switch button[data-l={l}]")
        pg.screenshot(path=f"{root}/mockups/shot_{i}.png")
    pg.click("header.switch button[data-l=l1]")
    pg.click(".l1 .modes button[data-m=overlay]")
    pg.screenshot(path=f"{root}/mockups/shot_1_overlay.png")
    b.close()
