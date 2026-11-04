"""Check the sheet's own inscriptions: the dot, the card, and the link into the texts page.

    npm run build && npm run preview
    ../.venv/bin/python scripts/check_inscriptions.py http://localhost:4173

An inscription is ink on the paper, so the things worth asserting are mostly absences: no modern
name, no status badge, no position on the ground, and no mark on the modern map. Screenshots land
in work/inscriptions/.
"""
import pathlib, sys
from playwright.sync_api import sync_playwright

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://localhost:4173").rstrip("/")
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "work" / "inscriptions"
OUT.mkdir(parents=True, exist_ok=True)
CHROME = str(next(pathlib.Path.home().glob(".cache/ms-playwright/chromium-*/chrome-linux*/chrome")))
fails = []


def check(name, cond, detail=""):
    print(("  ok  " if cond else "  FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    c = b.new_context(viewport={"width": 1500, "height": 950})
    p = c.new_page()
    errs = []
    p.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    p.on("pageerror", lambda e: errs.append(str(e)))
    p.goto(f"{BASE}/map/")
    p.wait_for_selector(".result", timeout=30000)
    p.wait_for_timeout(1500)

    print("the count and the list:")
    check("the count still says 457 places", "457 places" in p.inner_text("#count"), p.inner_text("#count"))
    check("...and names the inscriptions apart", "13 inscriptions" in p.inner_text("#count"), p.inner_text("#count"))

    print("\nfinding one:")
    p.fill("#q", "septentriones")
    p.wait_for_timeout(500)
    rows = p.eval_on_selector_all(".result", "els => els.map(e => e.dataset.id)")
    check("search finds SEPTENTRIONES", rows == ["L0164"], str(rows))
    p.click('.result[data-id="L0164"]')
    p.wait_for_selector(".card h2")
    card = p.inner_text(".card")
    # innerText comes back with the kicker's CSS uppercasing applied
    check("the card calls it an inscription", "inscription on the map" in card.lower(),
          card.replace("\n", " ")[:60])
    check("no status badge", "Not researched yet" not in card)
    check("no position on the ground", "Position today" not in card)
    check("it keeps its position on the sheet", "Position (1550)" in card)
    check("it is explained", "printed east-up" in card or "east-up" in card, card[-200:].replace("\n", " ")[:80])
    link = p.get_attribute(".card .reads a", "href")
    check("it links into the texts page", link == "/texts/#winds", str(link))
    p.screenshot(path=str(OUT / "1-card.png"), clip={"x": 0, "y": 0, "width": 400, "height": 950})

    print("\nthe link lands on the right sentence:")
    p2 = c.new_page()
    p2.goto(f"{BASE}{link}")
    tgt = p2.eval_on_selector("li#winds", "e => e.textContent.slice(0, 40)")
    check("the anchor exists on the texts page", "wind" in tgt.lower(), tgt)
    # The page is long and its images settle late, so the browser corrects the jump over the
    # first second or so. Wait for it to come to rest rather than measure mid-flight.
    try:
        p2.wait_for_function(
            "() => { const r = document.querySelector('li#winds').getBoundingClientRect();"
            " return r.top > -80 && r.top < 200 }", timeout=8000)
        landed = True
    except Exception:
        landed = False
    check("and the browser lands on it", landed,
          str(p2.evaluate("() => Math.round(document.querySelector('li#winds').getBoundingClientRect().top)")))
    p2.screenshot(path=str(OUT / "2-texts.png"))
    p2.close()

    print("\nwhat must not happen:")
    # with the search box still filled, the map is showing one result; clear it first
    p.fill("#q", "")
    p.wait_for_timeout(500)
    onmod = p.evaluate("""async () => {
        const d = await window.pme.maps.mod.getSource('places').getData();
        return d.features.filter(f => f.properties.id.match(/^L0(16[1-6]|47[1-7])$/)).length;
    }""")
    check("no inscription is marked on the modern map", onmod == 0, f"{onmod} marks")
    onold = p.evaluate("""async () => {
        const d = await window.pme.maps.old.getSource('places').getData();
        return d.features.filter(f => f.properties.id.match(/^L0(16[1-6]|47[1-7])$/)).length;
    }""")
    check("all 13 are marked on the 1550 sheet, the poem twice", onold == 14, f"{onold} marks")

    print("\nthe poem, in two panels:")
    p.goto(f"{BASE}/place/L0475/")
    p.wait_for_selector(".card h2", timeout=30000)
    card = p.inner_text(".card")
    check("the poem has its own page", "GILLES CORROSET" in card, card.replace("\n", " ")[:70])
    check("it links to the poem, not the notes", p.get_attribute(".card .reads a", "href") == "/texts/#poem",
          str(p.get_attribute(".card .reads a", "href")))
    also = p.evaluate("() => window.pme.entries.find(e => e.place.id === 'L0475').alsoLL.length")
    check("both panels are clickable", also == 1, f"{also} extra panel(s)")

    print("\na device, which carries no words:")
    p.goto(f"{BASE}/place/L0472/")
    p.wait_for_selector(".card h2", timeout=30000)
    check("it is named, not transcribed", p.inner_text(".card h2") == "Arms of France", p.inner_text(".card h2"))
    check("and says so", "carries no words" in p.inner_text(".card"), p.inner_text(".card").replace("\n", " ")[:90])
    check("the title is not set as a reading",
          "named" in (p.get_attribute(".card h2", "class") or ""), str(p.get_attribute(".card h2", "class")))
    p.screenshot(path=str(OUT / "3-device.png"), clip={"x": 0, "y": 0, "width": 400, "height": 950})

    print("\nthe filter:")
    p.goto(f"{BASE}/map/")
    p.wait_for_selector(".result", timeout=30000)
    p.click("#filters-btn")
    p.wait_for_timeout(300)
    chip = p.query_selector('.chip[data-type="inscription"]')
    check("there is an Inscriptions chip", bool(chip), chip.inner_text() if chip else "")
    if chip:
        chip.click()
        p.wait_for_timeout(500)
        n = p.eval_on_selector_all(".result", "e => e.length")
        check("it shows the 13", n == 13, f"{n} rows")
        check("the count reads as inscriptions only", p.inner_text("#count").startswith("13 inscriptions"),
              p.inner_text("#count"))
        p.screenshot(path=str(OUT / "4-filtered.png"), clip={"x": 0, "y": 0, "width": 400, "height": 950})

    # French and Swedish are parked (2026-11-04); put them back here when they return.
    print("\nin the other languages: skipped (parked)")
    for lang, path, want in ():
        p.goto(f"{BASE}{path}")
        p.wait_for_selector(".card h2", timeout=30000)
        check(f"{lang}: the device is named in this language", p.inner_text(".card h2") == want,
              p.inner_text(".card h2"))

    check("no console errors", not errs, "; ".join(errs[:2]))
    c.close()
    b.close()

print()
print("FAILED:", fails if fails else "none")
sys.exit(1 if fails else 0)
