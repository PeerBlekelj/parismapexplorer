"""Check the starred places and the sharing links against a running site.

    npm run dev                      # or: npm run build && npm run preview
    ../.venv/bin/python scripts/check_stars.py http://localhost:5173

Walks what a visitor does: star a place from its card and from a row, filter the list to them,
hand the list to another browser by its link, and share a view. Run it against the PREVIEW
(production) build as well as the dev server: the QR generator is a dependency, and a bundler
is where an import goes wrong. Screenshots land in work/stars-check/.
"""
import pathlib, sys
from playwright.sync_api import sync_playwright

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://localhost:5173").rstrip("/")
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "work" / "stars-check"
OUT.mkdir(parents=True, exist_ok=True)
CHROME = str(next(pathlib.Path.home().glob(".cache/ms-playwright/chromium-*/chrome-linux*/chrome")))
fails = []


def check(name, cond, detail=""):
    print(("  ok  " if cond else "  FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)

    def ctx():
        c = b.new_context(viewport={"width": 1440, "height": 900}, permissions=["clipboard-read", "clipboard-write"])
        return c

    # ---------- 1. star a place from its card ----------
    c1 = ctx()
    p = c1.new_page()
    errors = []
    # MapLibre reports a bad paint expression to the console and carries on without the layer,
    # so console.error counts as a failure here, not only an uncaught exception.
    p.on("pageerror", lambda e: errors.append(str(e)))
    p.on("console", lambda m: errors.append("console: " + m.text) if m.type == "error" else None)
    p.goto(f"{BASE}/map/")
    p.wait_for_selector(".result", timeout=20000)
    p.wait_for_timeout(1500)
    layers = p.evaluate("() => [window.pme.maps.old.getLayer('dots'), window.pme.maps.mod.getLayer('dots')].map(l => !!l)")
    check("both maps drew the place dots", layers == [True, True], str(layers))
    p.click('.result[data-id="L0006"]')
    p.wait_for_selector(".card .star-btn")
    check("card shows an unstarred button", p.inner_text(".card .star-btn").split()[-1] == "Star",
          repr(p.inner_text(".card .star-btn")))
    p.click(".card .star-btn")
    check("card button now reads Starred", p.inner_text(".card .star-btn").split()[-1] == "Starred",
          repr(p.inner_text(".card .star-btn")))
    check("aria-pressed set", p.get_attribute(".card .star-btn", "aria-pressed") == "true")
    p.screenshot(path=str(OUT / "1-card-starred.png"), clip={"x": 0, "y": 0, "width": 400, "height": 900})

    # ---------- 2. rows, the count line and the filter ----------
    p.click(".card-back")
    p.wait_for_selector(".count .stars-link")
    check("count line offers the list", "1 starred" in p.inner_text(".count .stars-link"),
          p.inner_text(".count .stars-link"))
    for pid in ("L0017", "L0025"):
        p.hover(f'.result[data-id="{pid}"]')
        p.click(f'.result[data-id="{pid}"] .star')
    check("three starred", "3 starred" in p.inner_text(".count .stars-link"), p.inner_text(".count .stars-link"))
    p.click(".count .stars-link")
    p.wait_for_selector("#stars-bar:not([hidden])")
    rows = p.eval_on_selector_all(".result", "els => els.map(e => e.dataset.id)")
    check("list shows exactly the starred places", sorted(rows) == ["L0006", "L0017", "L0025"], str(rows))
    dots = p.evaluate("""async () => {
        const d = await window.pme.maps.old.getSource('places').getData();
        return d.features.filter(f => f.properties.starred).length;
    }""")
    check("the old map marks them too", dots >= 3, f"{dots} starred dots")
    check("the filters chip is on", "on" in (p.get_attribute('.chip[data-chip="starred"]', "class") or ""))

    # ---------- 3. the hand-over panel ----------
    p.click('#stars-bar [data-act="qr"]')
    p.wait_for_selector(".handoff svg.qr")
    url = p.inner_text(".handoff .urlbox")
    check("the QR panel shows the link", "stars=" in url, url)
    modules = p.eval_on_selector("svg.qr", "e => e.getAttribute('viewBox')")
    check("the QR has a real symbol", modules not in (None, "0 0 0 0"), modules)
    # It was drawn at 92 css px once, which is where a scanner starts to lose it: a decoder reads
    # this symbol down to roughly 100 px of captured height, and a camera is never ideal.
    qrbox = p.eval_on_selector("svg.qr", "e => Math.round(e.getBoundingClientRect().width)")
    check("the QR is big enough for a camera", qrbox >= 160, f"{qrbox} css px")
    p.screenshot(path=str(OUT / "2-starred-list.png"), clip={"x": 0, "y": 0, "width": 400, "height": 900})
    p.click('#stars-bar [data-act="copy"]')
    p.wait_for_selector(".copied")
    copied = p.evaluate("() => navigator.clipboard.readText()")
    check("copy puts the same link on the clipboard", copied == url, f"{copied!r} vs {url!r}")
    p.screenshot(path=str(OUT / "3-copied.png"), clip={"x": 0, "y": 0, "width": 400, "height": 900})

    # ---------- 4. the same link in a fresh browser ----------
    c2 = ctx()
    p2 = c2.new_page()
    p2.on("pageerror", lambda e: errors.append("shared: " + str(e)))
    p2.goto(copied)
    p2.wait_for_selector("#shared:not([hidden])")
    check("the banner names the number", "3 places" in p2.inner_text("#shared"), p2.inner_text("#shared").split("\n")[0])
    rows2 = p2.eval_on_selector_all(".result", "els => els.map(e => e.dataset.id)")
    check("it shows only the shared places", sorted(rows2) == ["L0006", "L0017", "L0025"], str(rows2))
    check("they are not starred yet", p2.eval_on_selector_all(".result .star.on", "e => e.length") == 0)
    check("nothing was written to storage",
          p2.evaluate("() => localStorage.getItem('starred')") in (None, ""),
          repr(p2.evaluate("() => localStorage.getItem('starred')")))
    check("the address no longer carries the list", "stars=" not in p2.url, p2.url)
    p2.screenshot(path=str(OUT / "4-shared-link.png"), clip={"x": 0, "y": 0, "width": 400, "height": 900})
    p2.click('#shared [data-act="add"]')
    p2.wait_for_selector("#stars-bar:not([hidden])")
    check("added to the list in this browser",
          p2.evaluate("() => localStorage.getItem('starred')") == "L0006,L0017,L0025",
          repr(p2.evaluate("() => localStorage.getItem('starred')")))
    check("the banner is gone", p2.is_hidden("#shared"))
    # following the same link twice changes nothing
    p2.goto(copied)
    p2.wait_for_selector("#shared:not([hidden])")
    p2.click('#shared [data-act="add"]')
    check("following it twice changes nothing",
          p2.evaluate("() => localStorage.getItem('starred')") == "L0006,L0017,L0025",
          repr(p2.evaluate("() => localStorage.getItem('starred')")))

    # ---------- 5. share the view ----------
    p.click(".count .stars-link")  # back to all places
    p.click('#modes button[data-m="overlay"]')
    p.wait_for_timeout(400)
    p.evaluate("() => window.pme.maps.mod.jumpTo({ center: [2.3463, 48.8529], zoom: 15.4 })")
    p.wait_for_timeout(300)
    p.fill("#op", "62")
    p.dispatch_event("#op", "input")
    p.click("#share-view")
    p.wait_for_selector(".copied")
    view_url = p.evaluate("() => navigator.clipboard.readText()")
    check("the view link carries the mode", "m=overlay" in view_url, view_url)
    check("...the place and the zoom", "c=48.8529,2.3463" in view_url and "z=15.4" in view_url, view_url)
    check("...with the comma left readable", "%2C" not in view_url, view_url)
    check("...and the opacity", "o=62" in view_url, view_url)
    p.screenshot(path=str(OUT / "5-share-view.png"))

    c3 = ctx()
    p3 = c3.new_page()
    p3.on("pageerror", lambda e: errors.append("view: " + str(e)))
    p3.goto(view_url)
    p3.wait_for_selector(".result", timeout=20000)
    p3.wait_for_timeout(1200)
    mode = p3.get_attribute("#map-area", "data-mode")
    cam = p3.evaluate("() => { const c = window.pme.maps.mod.getCenter(); return [c.lng, c.lat, window.pme.maps.mod.getZoom()] }")
    check("the link opens in overlay", mode == "overlay", str(mode))
    check("at the same place", abs(cam[0] - 2.3463) < 0.002 and abs(cam[1] - 48.8529) < 0.002, str(cam))
    check("at the same zoom", abs(cam[2] - 15.4) < 0.05, str(cam[2]))
    check("with the same opacity", p3.input_value("#op") == "62", p3.input_value("#op"))
    check("the address is clean again", "m=overlay" not in p3.url, p3.url)
    p3.screenshot(path=str(OUT / "6-view-opened.png"))

    # ---------- 6. a link with an id this map does not have ----------
    p4 = c3.new_page()
    p4.on("pageerror", lambda e: errors.append("unknown: " + str(e)))
    p4.goto(f"{BASE}/map/?stars=6.99999")
    p4.wait_for_selector("#shared:not([hidden])")
    txt = p4.inner_text("#shared")
    check("an unknown id is reported, not swallowed", "1 of them is not a place" in txt, txt.replace("\n", " ")[:100])
    check("and the question is singular", "Add it to the list" in txt, txt.replace("\n", " ")[:100])
    rows4 = p4.eval_on_selector_all(".result", "els => els.map(e => e.dataset.id)")
    check("and the known one still shows", rows4 == ["L0006"], str(rows4))

    # ---------- 7. phone width ----------
    c5 = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2,
                       is_mobile=True, has_touch=True, permissions=["clipboard-read", "clipboard-write"])
    p5 = c5.new_page()
    p5.on("pageerror", lambda e: errors.append("phone: " + str(e)))
    p5.goto(copied)
    p5.wait_for_selector("#shared:not([hidden])")
    p5.click(".sheet-grip")
    p5.wait_for_timeout(500)
    p5.screenshot(path=str(OUT / "7-phone-shared.png"))
    p5.click('#shared [data-act="add"]')
    p5.wait_for_timeout(400)
    p5.screenshot(path=str(OUT / "8-phone-starred.png"))
    over = p5.evaluate("() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
    check("no sideways scroll on a phone", over <= 0, f"{over}px")

    check("no page errors anywhere", not errors, "; ".join(errors[:3]))

    # ---------- 8. the same ground in French and Swedish ----------
    errors = []  # the three languages, on the same site
    for lang, path, star_word, bar_word in [
        ("en", "/map/", "Star", "Point your phone\u2019s camera"),
        ("fr", "/fr/map/", "Mettre en favori", "Visez ceci avec l\u2019appareil photo"),
        ("sv", "/sv/map/", "Stj\u00e4rnm\u00e4rk", "Rikta telefonens kamera"),
    ]:
        c = b.new_context(viewport={"width": 1440, "height": 900})
        p = c.new_page()
        p.on("pageerror", lambda e, l=lang: errors.append(f"{l}: {e}"))
        p.on("console", lambda m, l=lang: errors.append(f"{l} console: {m.text}") if m.type == "error" else None)
        p.goto(BASE + path)
        if p.query_selector("#list") is None:
            # /fr/map/ and /sv/map/ are written by the build (vite.config.ts, sitePages), so the
            # dev server has nothing there and serves the start page instead. Say so rather than
            # wait out a timeout on a page that will never have a result row.
            print(f"  --  {lang}: /{lang}/map/ exists only in a build \u2014 run this against the preview")
            c.close()
            continue
        p.wait_for_selector(".result", timeout=20000)
        p.click('.result[data-id="L0006"]')
        p.wait_for_selector(".card .star-btn")
        check(f"{lang}: the card's star button", p.inner_text(".card .star-btn").split("\n")[-1] == star_word,
              repr(p.inner_text(".card .star-btn")))
        p.click(".card .star-btn")
        p.click(".card-back")
        p.click(".count .stars-link")
        p.wait_for_selector("#stars-bar:not([hidden])")
        p.click('#stars-bar [data-act="qr"]')
        p.wait_for_selector(".handoff svg.qr")
        paths = p.eval_on_selector("svg.qr path", "e => e.getAttribute('d').length")
        check(f"{lang}: the QR survived the bundler", paths > 200, f"{paths} chars of path")
        # innerText comes back with the CSS uppercasing applied, so compare without case
        check(f"{lang}: the hand-over is in this language",
              bar_word.lower() in p.inner_text("#stars-bar").lower(), p.inner_text(".handoff .lbl"))
        url = p.inner_text(".handoff .urlbox")
        # one id is shorter written out than packed into a bitmap, so the link says so
        check(f"{lang}: the link keeps the language", url.endswith("/map/?stars=6") and url.startswith(BASE + path), url)
        if lang != "en":
            p.screenshot(path=str(OUT / f"9-{lang}.png"), clip={"x": 0, "y": 0, "width": 400, "height": 900})
        c.close()
    check("no page errors", not errors, "; ".join(errors[:2]))
    b.close()

print()
print("FAILED:", fails if fails else "none")
sys.exit(1 if fails else 0)
