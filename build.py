#!/usr/bin/env python3
"""Builds the standalone NOUMEN index.html: inlines app.js and embeds the astronaut images as data URIs."""
import base64, pathlib, sys
root = pathlib.Path(__file__).parent
html = (root / "noumen.html").read_text()
js = (root / "app.js").read_text()
def data_uri(p):
    return "data:image/webp;base64," + base64.b64encode((root / "assets" / p).read_bytes()).decode()
html = html.replace("/*APP_JS*/", js)
html = html.replace("%%ASTRO_FRONT%%", data_uri("astronaut-front.webp")).replace("%%ASTRO_SIDE%%", data_uri("astronaut-side.webp"))
outs = sys.argv[1:] or [str(root.parent / "public" / "noumen" / "index.html")]
for o in outs:
    p = pathlib.Path(o); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(html)
    print("wrote", p, len(html) // 1024, "KB")
