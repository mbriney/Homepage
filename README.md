# mattbriney.com

Matt Briney's personal homepage. A static site built with a small Python
templating system, deployed via GitHub Pages from `main`.

## Pages

- `/` — home (hero, "Currently" at TRPL, selected work, "Off the clock")
- `/bio/` — narrative bio with portrait sidebar
- `/cv/` — full CV with downloadable resume PDF
- `/projects/` — projects index (teaser grid, institutional + personal)
- `/projects/<slug>/` — **23 case study detail pages** (see [docs/AUTHORING.md](docs/AUTHORING.md))

## Build & deploy

```bash
# Generate every HTML file from the templates
python3 tools/build.py
```

That's it. There's no Node / Jekyll / webpack — the build is one Python
script that stitches partials together. Commit the edited template and
the regenerated `index.html` files together.

GitHub Pages deploys from `main` automatically. The `CNAME` file pins
the custom domain (`mattbriney.com`) and `.nojekyll` disables Jekyll
processing.

## Layout

```
.
├── index.html                   # home page (generated)
├── bio/                         # /bio/   (generated)
├── cv/                          # /cv/    (generated)
├── projects/                    # /projects/ + /projects/<slug>/ (generated)
├── assets/
│   ├── css/style.css            # all site styles, one file
│   └── js/
│       ├── nav.js               # mobile nav + lightbox
│       └── analytics.js         # GA4 instrumentation
├── img/
│   ├── matt-*.{jpg,webp}        # portrait variants
│   └── projects/<slug>/         # case study imagery (hero + 01..N)
├── files/
│   └── Matt-Briney-Resume.pdf
├── tools/                       # build system (NOT deployed as pages)
│   ├── build.py
│   ├── _partials/               # base / head / header / footer
│   └── pages/                   # one Python module per page
├── docs/                        # repo documentation (NOT deployed)
│   ├── AUTHORING.md             # how to add / edit a case study
│   └── ANALYTICS.md             # GA4 events + dimensions reference
├── CNAME                        # mattbriney.com
└── .nojekyll                    # disable Jekyll on GitHub Pages
```

## Editing content

The HTML files are generated. **Never edit `index.html`, `*/index.html`,
or anything under `projects/` directly** — your change will get blown
away on the next build.

To change content:

1. Edit the corresponding module in `tools/pages/` (e.g.
   `proj_mount_vernon_website.py`) or a partial in `tools/_partials/`.
2. Run `python3 tools/build.py`.
3. Commit both the edited template and the regenerated HTML.

## Adding a new case study

The recurring workflow — research → screenshots → page → wire-up — is
documented in [docs/AUTHORING.md](docs/AUTHORING.md).

## Analytics

GA4 (measurement ID `G-0RQJ767Q41`) is wired up site-wide with content
groups, Vimeo + YouTube engagement, outbound clicks, PDF downloads, and
lightbox tracking. See [docs/ANALYTICS.md](docs/ANALYTICS.md) for the
full event list and the GA4 admin setup needed to surface custom
dimensions in reports.

## Conventions

A few patterns that recur across case studies, captured here so they
don't have to be re-discovered:

- **Hero images** are 1600×900 or 1600×1000. JPG + WebP pair via
  `<picture>`.
- **Gallery images** follow the `01.jpg`, `02.jpg`, …, `hero.jpg`
  pattern. For tall scrolling captures, add an `01-full.jpg` variant
  next to `01.jpg` — the lightbox auto-detects it and switches into
  scroll mode.
- **Case-nav chain.** Every case study has a `<nav class="case-nav">`
  at the bottom with `prev`/`next` links. When you insert a new study,
  update both neighbors' case-nav as well as `tools/pages/projects_index.py`.
- **`.case-breakout`** lets a block escape the 720px `.case-content`
  column out to 1080px — used for the Issuu reader, the video grid,
  and other wide media.
- **`.video-grid-2`** is the 2×2 responsive video grid used on the
  Democracy Symposium and Campaign for Mount Vernon case studies.
- **`.issuu-embed.widescreen`** = 16:9 Issuu reader.
  **`.issuu-embed.single-page`** = portrait 8.5:11 reader.
- **`.podcast-embed`** wraps Spotify Creators mini-player iframes.

## Licensing

All content (text, images, screenshots) © Matt Briney. The build
tooling is unrestricted; do what you like with it.
