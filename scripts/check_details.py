"""Check the longer description on the card: the disclosure, its contents, and its absences.

    npm run build && npm run preview
    ../.venv/bin/python scripts/check_details.py http://localhost:4173

`detail` is English-only and most places have none, so most of what matters here is what the card
does NOT do: no empty disclosure where there is no detail, no detail shown in place of the summary,
and no claim in French or Swedish that the text is in that language. Screenshots land in
work/details/.
"""
import json, pathlib, sys, urllib.request
from playwright.sync_api import sync_playwright

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://localhost:4173").rstrip("/")
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "work" / "details"
OUT.mkdir(parents=True, exist_ok=True)
CHROME = str(next(pathlib.Path.home().glob(".cache/ms-playwright/chromium-*/chrome-linux*/chrome")))
fails = []


def check(name, cond, detail=""):
    print(("  ok  " if cond else "  FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


data = json.load(urllib.request.urlopen(f"{BASE}/data/places.json"))
places = data["places"]
withd = [p for p in places if p.get("detail")]
without = [p for p in places if not p.get("detail")]
insc = [p for p in places if p["type"] == "inscription" and p.get("detail")]

print("the data:")
check("the build carries details", len(withd) > 150, f"{len(withd)} of {len(places)}")
check("most places have none, which is normal", len(without) > len(withd), f"{len(without)} without")
check("no inscription has one", not insc, ", ".join(p["id"] for p in insc) or "none")
check("every detail is plain text", all("<" not in p["detail"] for p in withd))
check("no detail restates nothing", all(len(p["detail"].split()) >= 40 for p in withd),
      f"shortest {min(len(p['detail'].split()) for p in withd)} words")
check("a detail never stands in for a missing summary", all(p["summary"] for p in withd))
held = ROOT / "data/research/details-held.csv"
check("the held-back ids are written down", held.exists() and held.read_text().count("\n") > 1)

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    c = b.new_context(viewport={"width": 1500, "height": 950})
    p = c.new_page()
    errs = []
    p.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    p.on("pageerror", lambda e: errs.append(str(e)))

    has = withd[0]["id"]
    none_id = next(q["id"] for q in without if q["type"] != "inscription" and q["summary"])

    print("\na place that has one:")
    p.goto(f"{BASE}/place/{has}/")
    p.wait_for_selector(".card h2", timeout=30000)
    check("the disclosure is there", p.locator(".card details.more").count() == 1)
    check("it is closed to begin with", p.locator(".card details.more[open]").count() == 0)
    check("the body is hidden until asked", not p.locator(".card .more-body").is_visible())
    summary_txt = p.inner_text(".card .summary")
    check("the summary is still shown in full", summary_txt.strip() == (
        next(q for q in places if q["id"] == has)["summary"] or "").strip(), summary_txt[:50])
    p.click(".card details.more > summary")
    p.wait_for_timeout(250)
    check("it opens", p.locator(".card details.more[open]").count() == 1)
    check("and the text appears", p.locator(".card .more-body").is_visible())
    body = p.inner_text(".card .more-body")
    check("it is the detail from the data", body.strip()[:60] in withd[0]["detail"], body[:60])
    check("the summary did not move aside", p.locator(".card .summary").is_visible())
    check("in English the card does not say 'in English'", "in English" not in p.inner_text(
        ".card details.more > summary"), p.inner_text(".card details.more > summary"))
    p.screenshot(path=str(OUT / "detail-open.png"), full_page=False)

    print("\na place that has none:")
    p.goto(f"{BASE}/place/{none_id}/")
    p.wait_for_selector(".card h2", timeout=30000)
    check("no disclosure at all", p.locator(".card details.more").count() == 0, none_id)
    check("no empty caret left behind", "More about this place" not in p.inner_text(".card"))
    check("the summary is still there", p.locator(".card .summary").count() == 1)

    print("\nthe other languages say it is English:")
    for lg, word in (("fr", "en anglais"), ("sv", "på engelska")):
        p.goto(f"{BASE}/{lg}/place/{has}/")
        p.wait_for_selector(".card h2", timeout=30000)
        label = p.inner_text(".card details.more > summary")
        check(f"{lg}: the label is in this language", word in label, label.replace("\n", " "))
        p.click(".card details.more > summary")
        p.wait_for_timeout(200)
        check(f"{lg}: the text is marked as English",
              p.get_attribute(".card .more-body", "lang") == "en")
        check(f"{lg}: it is the same English text",
              p.inner_text(".card .more-body").strip()[:50] in withd[0]["detail"])
        p.screenshot(path=str(OUT / f"detail-{lg}.png"))

    check("no console errors", not errs, "; ".join(errs[:2]))
    b.close()

print("\nFAILED: " + (", ".join(fails) if fails else "none"))
print(f"screenshots in {OUT}")
sys.exit(1 if fails else 0)
