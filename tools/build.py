#!/usr/bin/env python3
"""
Build script for mattbriney.com.

Renders all pages from per-page content fragments + shared header/footer.
Output is pure static HTML — no server-side rendering needed at deploy time.

Run from the repo root:
    python3 tools/build.py
"""
from __future__ import annotations
import os, re, sys, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "tools" / "pages"
PARTIALS = ROOT / "tools" / "_partials"

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")

def write(p: Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")
    print(f"  wrote {p.relative_to(ROOT)}  ({len(s):,} bytes)")

def render(template: str, **ctx) -> str:
    """Render a {{var}} template. Missing vars become empty strings."""
    def sub(m):
        return str(ctx.get(m.group(1).strip(), ""))
    return re.sub(r"\{\{\s*([\w_-]+)\s*\}\}", sub, template)

# ---------- Shared partials ----------
HEAD_TMPL = read(PARTIALS / "head.html")
HEADER_TMPL = read(PARTIALS / "header.html")
FOOTER = read(PARTIALS / "footer.html")
BASE = read(PARTIALS / "base.html")

def page(slug: str, out: Path, *, title: str, description: str,
         active: str, canonical: str, body: str,
         og_image: str = "/img/matt-og-1200x630.jpg",
         extra_css: str = "", extra_head: str = ""):
    head = render(HEAD_TMPL, title=title, description=description,
                  canonical=canonical, og_image=og_image,
                  extra_css=extra_css, extra_head=extra_head)
    header = render(HEADER_TMPL,
        cls_home="active" if active=="home" else "",
        cls_bio="active" if active=="bio" else "",
        cls_proj="active" if active=="projects" else "",
        cls_cv="active" if active=="cv" else "",
    )
    html_doc = render(BASE, head=head, header=header, body=body, footer=FOOTER)
    write(out, html_doc)

# ---------- Build all pages ----------
def main():
    print("Building site…")
    # Discover every page file in tools/pages/
    for path in sorted(PAGES_DIR.rglob("*.py")):
        # Each page is a Python module that returns a dict.
        # Import via exec for simplicity (no need for package structure).
        ns = {}
        exec(path.read_text(encoding="utf-8"), ns)
        if "build" not in ns:
            continue
        info = ns["build"]()
        out = ROOT / info["out"]
        page(slug=info.get("slug", path.stem),
             out=out,
             title=info["title"],
             description=info["description"],
             active=info.get("active", ""),
             canonical=info["canonical"],
             body=info["body"],
             og_image=info.get("og_image", "/img/matt-og-1200x630.jpg"),
             extra_css=info.get("extra_css", ""),
             extra_head=info.get("extra_head", ""))
    print("Done.")

if __name__ == "__main__":
    main()
