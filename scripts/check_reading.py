"""Check what the card says about our reading of a label.

    npm run build && npm run preview
    ../.venv/bin/python scripts/check_reading.py http://localhost:4173

The card used to say "Unsure: the label is hard to read" for every label the transcription pass had
flagged -- including 14 that Jules Cousin printed the same way in 1875. That is a claim about the
woodcut, made on the strength of our own doubt, and contradicted by a source already cited on the
same card. These assertions exist so it cannot come back. Screenshots land in work/reading/.
"""
import json, pathlib, sys, urllib.request
from playwright.sync_api import sync_playwright

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://localhost:4173").rstrip("/")
OUT = pathlib.Path(__file__).resolve().parent.parent / "work" / "reading"
OUT.mkdir(parents=True, exist_ok=True)
CHROME = str(next(pathlib.Path.home().glob(".cache/ms-playwright/chromium-*/chrome-linux*/chrome")))
fails = []


def check(name, cond, detail=""):
    print(("  ok  " if cond else "  FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


places = json.load(urllib.request.urlopen(f"{BASE}/data/places.json"))["places"]
by = {p["id"]: p for p in places}
flagged = [p for p in places if p.get("flag") == "unsure"]
conf = [p for p in flagged if p.get("reading") == "confirmed"]
disp = [p for p in flagged if p.get("reading") == "disputed"]
unc = [p for p in flagged if p.get("reading") == "uncertain"]

print("the data:")
check("every place has a reading", all(p.get("reading") for p in places))
check("the flagged labels are classified, none left over",
      len(conf) + len(disp) + len(unc) == len(flagged), f"{len(flagged)} flagged")
check("most flagged labels turned out to be confirmed", len(conf) >= 10, f"{len(conf)} confirmed")
check("a disputed label carries the other reading", all(p.get("reading_other") for p in disp),
      ", ".join(f'{p["id"]}:{p.get("reading_other")}' for p in disp))
check("a confirmed label is not counted as open", all(p["reading"] == "confirmed" for p in conf))
check("no unflagged place was quietly marked unsure",
      all(p.get("reading") == "clear" for p in places if p.get("flag") != "unsure"))

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    c = b.new_context(viewport={"width": 1500, "height": 950})
    p = c.new_page()
    errs = []
    p.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    p.on("pageerror", lambda e: errs.append(str(e)))

    print("\na label Cousin read the same way:")
    pid = conf[0]["id"]
    p.goto(f"{BASE}/place/{pid}/")
    p.wait_for_selector(".card h2", timeout=30000)
    card = p.inner_text(".card")
    check(f"{pid} no longer calls the label hard to read", "hard to read" not in card.lower())
    check("it says Cousin agrees", "Cousin" in card and "1875" in card,
          next((l for l in card.split("\n") if "Cousin read" in l), card[:60]))
    check("and carries no unsure badge", "unsure reading" not in card.lower())
    p.screenshot(path=str(OUT / f"confirmed-{pid}.png"))

    print("\na label where the two readings differ:")
    if disp:
        d = disp[0]
        p.goto(f"{BASE}/place/{d['id']}/")
        p.wait_for_selector(".card h2", timeout=30000)
        card = p.inner_text(".card")
        check(f"{d['id']} shows both readings", d["old"].lower() in card.lower()
              and d["reading_other"].lower() in card.lower(), d["reading_other"])
        check("and is still marked as open", "unsure reading" in card.lower())
        p.screenshot(path=str(OUT / f"disputed-{d['id']}.png"))

    print("\na label with no second reading:")
    u = unc[0]
    p.goto(f"{BASE}/place/{u['id']}/")
    p.wait_for_selector(".card h2", timeout=30000)
    card = p.inner_text(".card")
    check(f"{u['id']} blames our transcription, not the woodcut",
          "transcription" in card.lower() and "hard to read" not in card.lower())
    check("and does not name Cousin", "Cousin read" not in card)

    print("\nthe filter counts what is still open:")
    p.goto(f"{BASE}/map/")
    p.wait_for_selector(".result", timeout=30000)
    p.wait_for_timeout(1200)
    p.click("#filters-btn") if p.locator("#filters-btn").count() else p.click(".filters-btn")
    p.wait_for_timeout(400)
    chip = p.inner_text('[data-chip="unsure"]')
    check("the chip counts the open ones, not all 24",
          str(len(disp) + len(unc)) in chip and "24" not in chip, chip.replace("\n", " "))

    print("\nthe other languages:")
    for lg, word in (("fr", "Cousin"), ("sv", "Cousin")):
        p.goto(f"{BASE}/{lg}/place/{pid}/")
        p.wait_for_selector(".card h2", timeout=30000)
        t = p.inner_text(".card")
        check(f"{lg}: says Cousin agrees", word in t and "1875" in t)
        check(f"{lg}: no English leaked in", "hard to read" not in t.lower())

    check("no console errors", not errs, "; ".join(errs[:2]))
    b.close()

print("\nFAILED: " + (", ".join(fails) if fails else "none"))
sys.exit(1 if fails else 0)
