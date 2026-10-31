"""Check the map's top strip, the place marks and the table's starred column.

    npm run build && npm run preview
    ../.venv/bin/python scripts/check_map_controls.py http://localhost:4173

The strip (modes bar, controls, overlay note) is measured at twelve widths in both modes: it is one
wrapping flex row, and nothing in it may ever overlap anything else. Then the paper halo under the
marks, the switch that hides them (leaving the visitor's starred ones), and the starred column.
Screenshots land in work/map-controls/.
"""
import pathlib, sys
from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:4173"
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "work" / "map-controls"
OUT.mkdir(parents=True, exist_ok=True)
CHROME = str(next(pathlib.Path.home().glob(".cache/ms-playwright/chromium-*/chrome-linux*/chrome")))
fails = []


def check(name, cond, detail=""):
    print(("  ok  " if cond else "  FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


OVERLAP = """() => {
  const a = document.querySelector('#modes').getBoundingClientRect();
  const b = document.querySelector('.topright').getBoundingClientRect();
  const w = document.querySelector('#warn');
  const c = w && !w.offsetParent ? null : w.getBoundingClientRect();
  const hit = (p, q) => q && p.left < q.right && q.left < p.right && p.top < q.bottom && q.top < p.bottom;
  return { modesTopright: hit(a, b), modesWarn: hit(a, c), toprightWarn: hit(b, c),
           modes: [a.left, a.top, a.right, a.bottom].map(Math.round),
           topright: [b.left, b.top, b.right, b.bottom].map(Math.round) };
}"""

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)

    # ---------- 1. the top strip at many widths, in both modes ----------
    print("the top strip:")
    for w in (1920, 1680, 1500, 1400, 1280, 1180, 1024, 920, 820, 760, 600, 390):
        mobile = w <= 760
        c = b.new_context(viewport={"width": w, "height": 860}, is_mobile=mobile, has_touch=mobile)
        p = c.new_page()
        p.goto(f"{BASE}/map/")
        p.wait_for_selector(".result", timeout=30000)
        p.wait_for_timeout(500)
        r = p.evaluate(OVERLAP)
        check(f"{w:>5}px side-by-side: nothing overlaps", not r["modesTopright"],
              f"modes {r['modes']} vs controls {r['topright']}")
        p.click('#modes button[data-m="overlay"]')   # this is when the warn note appears
        p.wait_for_timeout(500)
        r = p.evaluate(OVERLAP)
        check(f"{w:>5}px overlay: nothing overlaps",
              not (r["modesTopright"] or r["modesWarn"] or r["toprightWarn"]),
              f"modes/controls {r['modesTopright']} modes/note {r['modesWarn']} controls/note {r['toprightWarn']}")
        if w in (1500, 1180, 920, 390):
            p.screenshot(path=str(OUT / f"strip-{w}.png"), clip={"x": 0, "y": 0, "width": w, "height": 230})
        c.close()

    # ---------- 2. the halo, the switch, the column ----------
    c = b.new_context(viewport={"width": 1500, "height": 900})
    p = c.new_page()
    errs = []
    p.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    p.on("pageerror", lambda e: errs.append(str(e)))
    p.goto(f"{BASE}/map/")
    p.wait_for_selector(".result", timeout=30000)
    print("\nthe marks:")
    # the modern map's style comes off the network, so wait for the layer rather than guess
    try:
        p.wait_for_function("() => ['old','mod'].every(k => window.pme?.maps?.[k]?.getLayer?.('casing'))",
                            timeout=25000)
    except Exception:
        pass
    layers = p.evaluate("() => ['old','mod'].map(k => !!window.pme.maps[k].getLayer('casing'))")
    check("both maps have the halo layer", layers == [True, True], str(layers))

    p.click('.result[data-id="L0006"]')
    p.wait_for_selector(".card .star-btn")
    p.click(".card .star-btn")
    p.click(".card-back")
    p.wait_for_timeout(300)
    p.click('#modes button[data-m="old"]')
    p.wait_for_timeout(400)
    p.evaluate("""() => {
        const e = window.pme.entries.find(x => x.place.id === 'L0006');
        window.pme.maps.old.jumpTo({ center: e.oldLL, zoom: 12.9 });
    }""")
    p.wait_for_timeout(2200)
    p.screenshot(path=str(OUT / "halo-on.png"), clip={"x": 380, "y": 0, "width": 1120, "height": 900})

    print("\nthe switch:")
    check("it starts pressed", p.get_attribute("#dots-toggle", "aria-pressed") == "true")
    p.click("#dots-toggle")
    p.wait_for_timeout(900)
    filt = p.evaluate("() => ['casing','dots'].map(l => JSON.stringify(window.pme.maps.old.getFilter(l)))")
    check("off leaves only the starred", filt == ['["get","starred"]', '["get","starred"]'], str(filt))
    check("aria-pressed follows", p.get_attribute("#dots-toggle", "aria-pressed") == "false")
    p.screenshot(path=str(OUT / "halo-off.png"), clip={"x": 380, "y": 0, "width": 1120, "height": 900})
    # a label is still clickable with the marks hidden
    p.evaluate("() => window.pme.maps.old.fire('click', { point: window.pme.maps.old.project(window.pme.entries.find(x => x.place.id === 'L0017').oldLL), lngLat: window.pme.maps.old.getCenter(), originalEvent: new MouseEvent('click') })")
    p.wait_for_timeout(600)
    check("a label still opens its card with the marks off", "/place/L0017/" in p.url, p.url)
    p.click(".card-back")
    p.click("#dots-toggle")
    p.wait_for_timeout(400)

    print("\nthe table:")
    p.click('.viewtabs [data-view="table"]')
    p.wait_for_selector(".table-view table")
    heads = p.eval_on_selector_all(".table-view th", "els => els.map(e => e.textContent.trim())")
    check("there is a starred column", heads and heads[0].startswith("Starred"), str(heads))
    first_on = p.eval_on_selector_all(".table-view td.sr .star.on", "e => e.length")
    check("the one starred place shows as starred", first_on == 1, str(first_on))
    p.hover('.table-view tr[data-id="L0025"]')   # unstarred stars appear under the pointer
    p.click('.table-view tr[data-id="L0025"] .star')
    p.wait_for_timeout(300)
    check("starring from the table works",
          p.evaluate("() => localStorage.getItem('starred')") == "L0006,L0025",
          repr(p.evaluate("() => localStorage.getItem('starred')")))
    check("and it did not open the place", "/place/" not in p.url, p.url)
    p.click('.table-view th[data-key="star"]')
    p.wait_for_timeout(300)
    ids = p.eval_on_selector_all(".table-view tbody tr", "els => els.slice(0,2).map(e => e.dataset.id)")
    check("sorting by starred puts them first", sorted(ids) == ["L0006", "L0025"], str(ids))
    p.screenshot(path=str(OUT / "table.png"), clip={"x": 380, "y": 0, "width": 1120, "height": 620})
    check("no console errors", not errs, "; ".join(errs[:2]))
    c.close()
    b.close()

print()
print("FAILED:", fails if fails else "none")
sys.exit(1 if fails else 0)
