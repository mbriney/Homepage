# mattbriney.com

My personal homepage. Deployed via GitHub Pages from `main`.

## Pages

- `/` — home
- `/bio/` — bio
- `/cv/` — full CV with PDF download
- `/projects/` — projects index (teaser grid)
- `/projects/<slug>/` — eight case study detail pages

## Editing

The HTML files are generated from page templates in `tools/pages/` and shared
partials in `tools/_partials/`. To change content, edit the corresponding
`.py` file under `tools/pages/`, then rebuild:

```bash
python3 tools/build.py
```

Commit both the edited template and the regenerated `index.html`.

## Images

Optimized image variants live in `img/`. The original 20 MB portrait was
deleted from the repo after a high-quality 2400 px backup
(`img/matt-portrait-original-2400.jpg`) and small/medium derivatives were
generated. Project screenshots in `img/projects/<slug>/` were similarly
optimized down from raw screenshots — each project has a `hero.{jpg,webp}`
and a few numbered detail images.

## Layout

```
.
├── index.html                   # home
├── bio/                         # /bio/
│   └── index.html
├── cv/                          # /cv/
│   └── index.html
├── projects/                    # /projects/
│   ├── index.html
│   └── <slug>/                  # one folder per case study
│       └── index.html
├── assets/
│   ├── css/style.css
│   └── js/nav.js
├── img/
│   ├── matt-*.{jpg,webp}        # portrait variants
│   └── projects/<slug>/         # project screenshots
├── files/
│   └── Matt-Briney-Resume.pdf
├── tools/                       # build system (not deployed pages)
│   ├── build.py
│   ├── _partials/               # shared header / footer / head templates
│   └── pages/                   # one Python module per page
├── CNAME                        # mattbriney.com
└── .nojekyll                    # disable Jekyll processing on GitHub Pages
```
