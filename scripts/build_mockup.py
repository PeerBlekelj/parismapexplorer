import base64, sys
root = sys.argv[1]
def uri(p): return "data:image/jpeg;base64," + base64.b64encode(open(f"{root}/mockups/{p}", "rb").read()).decode()
html = open(f"{root}/mockups/template.html").read()
for k, f in {"OLD": "_old_cite.jpg", "MOD": "_modern_cite.jpg", "ND": "_nd_label.jpg"}.items():
    html = html.replace("{{%s}}" % k, uri(f))
open(f"{root}/mockups/layouts.html", "w").write(html)
