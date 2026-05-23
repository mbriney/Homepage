#!/usr/bin/env python3
"""
Build script for mattbriney.com.

Renders all pages from per-page content fragments + shared header/footer.
Output is pure static HTML — no server-side rendering needed at deploy time.

Run from the repo root:
    python3 tools/build.py
"""
from __future__ import annotations
import os, re, sys, html, json
from pathlib import Path
from datetime import date

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
         extra_css: str = "", extra_head: str = "",
         og_type: str = "website",
         og_article_meta: str = "",
         json_ld: str = "",
         preload_hero: str = ""):
    head = render(HEAD_TMPL, title=title, description=description,
                  canonical=canonical, og_image=og_image,
                  extra_css=extra_css, extra_head=extra_head,
                  og_type=og_type, og_article_meta=og_article_meta,
                  json_ld=json_ld, preload_hero=preload_hero)
    header = render(HEADER_TMPL,
        cls_home="active" if active=="home" else "",
        cls_bio="active" if active=="bio" else "",
        cls_proj="active" if active=="projects" else "",
        cls_recognition="active" if active=="recognition" else "",
        cls_gallery="active" if active=="gallery" else "",
        cls_cv="active" if active=="cv" else "",
    )
    html_doc = render(BASE, head=head, header=header, body=body, footer=FOOTER)
    write(out, html_doc)

# ---------- SEO metadata ----------
SITE_ORIGIN = "https://mattbriney.com"
AUTHOR_NAME = "Matt Briney"

# Person schema — reused across pages
PERSON_LD = {
    "@type": "Person",
    "@id": f"{SITE_ORIGIN}/#person",
    "name": AUTHOR_NAME,
    "alternateName": ["Matthew Briney", "Matt K. Briney"],
    "jobTitle": "Chief Communications & Marketing Officer",
    "worksFor": {
        "@type": "Organization",
        "name": "Theodore Roosevelt Presidential Library",
        "url": "https://www.trlibrary.com",
    },
    "url": SITE_ORIGIN,
    "image": f"{SITE_ORIGIN}/img/matt-portrait-1000.jpg",
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Dallas",
        "addressRegion": "TX",
        "addressCountry": "US",
    },
    "sameAs": [
        "https://www.linkedin.com/in/mbriney/",
        "https://github.com/mbriney",
        "https://x.com/mbriney",
        "https://www.instagram.com/mbriney/",
        "https://www.facebook.com/briney",
        "https://www.alltrails.com/members/matt-briney",
        "https://unsplash.com/@mbriney",
        "https://www.imdb.com/name/nm9778875/",
    ],
}

# WebSite schema — homepage / site-wide
WEBSITE_LD = {
    "@type": "WebSite",
    "@id": f"{SITE_ORIGIN}/#website",
    "name": "Matt Briney",
    "url": SITE_ORIGIN,
    "inLanguage": "en-US",
    "publisher": {"@id": f"{SITE_ORIGIN}/#person"},
}


def _ld(obj_or_list):
    """Wrap a JSON-LD object (or list of objects) in a <script type=application/ld+json>."""
    if isinstance(obj_or_list, list):
        data = {"@context": "https://schema.org", "@graph": obj_or_list}
    else:
        data = {"@context": "https://schema.org", **obj_or_list}
    return ('<script type="application/ld+json">'
            + json.dumps(data, separators=(",", ":"))
            + "</script>")


def json_ld_for(info: dict) -> str:
    """Build the JSON-LD block for a page based on its build() dict."""
    if info.get("noindex"):
        return ""  # No structured data on noindex pages
    canonical = info["canonical"]
    title = info["title"]
    description = info["description"]
    out = info["out"]
    is_case_study = out.startswith("projects/") and out != "projects/index.html"
    is_home = (out == "index.html")
    is_bio  = out.startswith("bio/")
    is_cv   = out.startswith("cv/")
    is_proj = (out == "projects/index.html")

    items = [PERSON_LD, WEBSITE_LD]

    if is_home:
        items.append({
            "@type": "WebPage",
            "@id": canonical + "#webpage",
            "url": canonical,
            "name": title,
            "description": description,
            "isPartOf": {"@id": f"{SITE_ORIGIN}/#website"},
            "about": {"@id": f"{SITE_ORIGIN}/#person"},
            "primaryImageOfPage": f"{SITE_ORIGIN}{info.get('og_image','')}",
        })
    elif is_bio:
        items.append({
            "@type": "ProfilePage",
            "@id": canonical + "#profile",
            "url": canonical,
            "name": title,
            "description": description,
            "isPartOf": {"@id": f"{SITE_ORIGIN}/#website"},
            "about": {"@id": f"{SITE_ORIGIN}/#person"},
            "mainEntity": {"@id": f"{SITE_ORIGIN}/#person"},
        })
        items.append(_breadcrumb([
            ("Home", SITE_ORIGIN + "/"),
            ("Bio", canonical),
        ]))
    elif is_cv:
        items.append({
            "@type": "WebPage",
            "@id": canonical + "#webpage",
            "url": canonical,
            "name": title,
            "description": description,
            "isPartOf": {"@id": f"{SITE_ORIGIN}/#website"},
            "about": {"@id": f"{SITE_ORIGIN}/#person"},
        })
        items.append(_breadcrumb([
            ("Home", SITE_ORIGIN + "/"),
            ("CV", canonical),
        ]))
    elif is_proj:
        items.append({
            "@type": "CollectionPage",
            "@id": canonical + "#webpage",
            "url": canonical,
            "name": title,
            "description": description,
            "isPartOf": {"@id": f"{SITE_ORIGIN}/#website"},
        })
        items.append(_breadcrumb([
            ("Home", SITE_ORIGIN + "/"),
            ("Projects", canonical),
        ]))
    elif is_case_study:
        # Strip "— Matt Briney" suffix for the article headline
        headline = title.split(" — ")[0]
        items.append({
            "@type": "Article",
            "@id": canonical + "#article",
            "headline": headline,
            "name": title,
            "description": description,
            "url": canonical,
            "image": f"{SITE_ORIGIN}{info.get('og_image','')}",
            "isPartOf": {"@id": f"{SITE_ORIGIN}/#website"},
            "author": {"@id": f"{SITE_ORIGIN}/#person"},
            "publisher": {"@id": f"{SITE_ORIGIN}/#person"},
            "datePublished": _lastmod_for(out),
            "dateModified":  _lastmod_for(out),
            "mainEntityOfPage": canonical,
        })
        items.append(_breadcrumb([
            ("Home", SITE_ORIGIN + "/"),
            ("Projects", SITE_ORIGIN + "/projects/"),
            (headline, canonical),
        ]))

    return _ld(items)


def _breadcrumb(steps):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
            for i, (name, url) in enumerate(steps)
        ],
    }


def _lastmod_for(out_rel: str) -> str:
    """Return the last-modified ISO date for an output file. Falls back to today."""
    p = ROOT / out_rel
    try:
        return date.fromtimestamp(p.stat().st_mtime).isoformat()
    except Exception:
        return date.today().isoformat()


def article_meta_for(info: dict) -> tuple[str, str]:
    """Return (og_type, og_article_meta_html) for a page."""
    out = info["out"]
    if out.startswith("projects/") and out != "projects/index.html":
        # Case study: article
        lm = _lastmod_for(out)
        meta = (
            f'<meta property="article:published_time" content="{lm}" />\n'
            f'<meta property="article:modified_time"  content="{lm}" />\n'
            f'<meta property="article:author"         content="{AUTHOR_NAME}" />\n'
            f'<meta property="article:section"        content="Case Study" />'
        )
        return ("article", meta)
    return ("website", "")


def preload_hero_for(info: dict) -> str:
    """If a page has a hero image we know about, preload it for better LCP."""
    out = info["out"]
    og  = info.get("og_image", "")
    # Only emit a preload for case-study heroes
    if og and out.startswith("projects/") and out != "projects/index.html":
        webp = og.rsplit(".", 1)[0] + ".webp"
        return (f'<link rel="preload" as="image" '
                f'href="{webp}" type="image/webp" fetchpriority="high">')
    return ""


# ---------- Sitemap.xml ----------
def build_sitemap(pages_info: list[dict]):
    """Emit sitemap.xml at the repo root. Includes <image:image> entries for
    each page's primary image so Google Image Search can pick them up."""
    today = date.today().isoformat()
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
             '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for info in pages_info:
        canonical = info["canonical"]
        out = ROOT / info["out"]
        og  = info.get("og_image", "")
        try:
            ts = date.fromtimestamp(out.stat().st_mtime).isoformat()
        except Exception:
            ts = today
        parts.append("  <url>")
        parts.append(f"    <loc>{canonical}</loc>")
        parts.append(f"    <lastmod>{ts}</lastmod>")
        if og:
            parts.append("    <image:image>")
            parts.append(f"      <image:loc>{SITE_ORIGIN}{og}</image:loc>")
            parts.append("    </image:image>")
        parts.append("  </url>")
    parts.append("</urlset>\n")
    write(ROOT / "sitemap.xml", "\n".join(parts))


def build_robots():
    body = (
        "# mattbriney.com\n"
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {SITE_ORIGIN}/sitemap.xml\n"
    )
    write(ROOT / "robots.txt", body)


def build_manifest():
    """Tiny PWA manifest so Android/Chrome 'Add to Home Screen' looks right."""
    body = json.dumps({
        "name": "Matt Briney",
        "short_name": "Briney",
        "description": "Matt Briney — Chief Communications & Marketing Officer, Theodore Roosevelt Presidential Library.",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#faf6ed",
        "theme_color": "#2d4a3e",
        "icons": [
            {"src": "/img/matt-square-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/img/matt-square-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }, indent=2)
    write(ROOT / "site.webmanifest", body + "\n")


# ---------- Build all pages ----------
def main():
    print("Building site…")
    pages_info: list[dict] = []
    # Discover every page file in tools/pages/
    for path in sorted(PAGES_DIR.rglob("*.py")):
        # Each page is a Python module that returns a dict.
        # Import via exec for simplicity (no need for package structure).
        ns = {}
        exec(path.read_text(encoding="utf-8"), ns)
        if "build" not in ns:
            continue
        info = ns["build"]()
        og_type, og_article_meta = article_meta_for(info)
        json_ld_block = json_ld_for(info)
        preload = preload_hero_for(info)
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
             extra_head=info.get("extra_head", ""),
             og_type=og_type,
             og_article_meta=og_article_meta,
             json_ld=json_ld_block,
             preload_hero=preload)
        # Skip noindex pages (e.g. 404) from the sitemap
        if not info.get("noindex"):
            pages_info.append(info)
    build_sitemap(pages_info)
    build_robots()
    build_manifest()
    print("Done.")

if __name__ == "__main__":
    main()
