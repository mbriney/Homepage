# Authoring case studies

The recurring workflow for adding or editing a project case study on
mattbriney.com. Optimized for the way these have actually been built
across the existing 23 studies.

## Quick reference

Every case study has the same six artifacts:

1. **A Python module** at `tools/pages/proj_<slug>.py`
2. **Image folder** at `img/projects/<slug>/` with `hero.{jpg,webp}` and numbered figures
3. **A teaser block** in `tools/pages/projects_index.py`
4. **Case-nav links** updated on the two neighbors in the chain
5. (sometimes) **An entry in the CV** at `tools/pages/cv.py`
6. (rarely) **A swap on the homepage Selected Work slate** in `tools/pages/home.py`

## Step-by-step

### 1. Pick a slug

URL-friendly, hyphen-separated, lowercase. The same slug is used for:
- The Python module name (`proj_<slug>.py` — underscores in module, hyphens in URL)
- The output folder (`projects/<slug>/`)
- The image folder (`img/projects/<slug>/`)
- The teaser `href` and case-nav `href`

### 2. Research first, build second

Don't open the Python template until you have:
- The headline metric (the number that tells the story in one breath)
- A timeline (start year → end year)
- The role you played
- 2–3 specific quotes / press references / dates
- The imagery (hero + 2–6 supporting figures)

Pages built on thin research read as thin. Get the source material
together first.

### 3. Process the imagery

All images live at `img/projects/<slug>/`. Conventions:

| File | Purpose | Typical size |
|------|---------|--------------|
| `hero.jpg` + `hero.webp` | Hero image (above the fold) | 1600×900 or 1600×1000 |
| `01.jpg`, `02.jpg`, … + `.webp` siblings | Numbered gallery figures | 1600×variable |
| `01-full.jpg` + `.webp` | Optional "scrollable full page" variant | 1600×any-height |
| `*.jpg` quality 86, `*.webp` quality 82 | progressive JPG, WebP method 6 | — |

**Tall scrolling screenshots** (full webpage captures, e.g. the Mount
Vernon Multiplier records or the Tessitura Add-Ons page) follow the
`-top` + `-full` pattern: `04.jpg` is a top-crop ≤ 1100px tall for inline
display, `04-full.jpg` is the entire 1600×N page. The lightbox in
`assets/js/nav.js` auto-detects the `-full` variant and switches to
scrollable mode for aspect ratios > 1.6 and width ≥ 800px.

A typical processing pipeline (one-off bash):

```bash
python3 - <<'PY'
from PIL import Image
def fit(im, w):
    r = w / im.width
    return im.resize((w, int(im.height * r)), Image.LANCZOS)
src = Image.open("raw-screenshot.png").convert("RGB")
out = fit(src, 1600)
out.save("01.jpg", "JPEG", quality=86, optimize=True, progressive=True)
out.save("01.webp", "WEBP", quality=82, method=6)
if out.height > 1100:
    top = out.crop((0, 0, 1600, 900))
    top.save("01.jpg", "JPEG", quality=86, optimize=True, progressive=True)
    top.save("01.webp", "WEBP", quality=82, method=6)
    out.save("01-full.jpg", "JPEG", quality=86, optimize=True, progressive=True)
    out.save("01-full.webp", "WEBP", quality=82, method=6)
PY
```

### 4. Write the case study module

Create `tools/pages/proj_<slug>.py`. Start by copying a recent module
with a similar structure as a template (e.g. `proj_campaign_mount_vernon.py`
for a multi-video case study, `proj_tessitura_ticketing.py` for a
step-by-step product walkthrough, `proj_pickens_plan.py` for an
infrastructure-heavy story).

Every module exports a `build()` function returning a dict:

```python
def build():
    return dict(
        out="projects/<slug>/index.html",
        title="<Title> — Matt Briney",
        description="<140-char description for og:description / SEO>",
        active="projects",
        canonical="https://mattbriney.com/projects/<slug>/",
        og_image="/img/projects/<slug>/hero.jpg",
        body=BODY,                          # the HTML string above
    )
```

The page itself follows a consistent skeleton:

```html
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">← All projects</a>
    <p class="eyebrow">Case study · <Organization> · <Years></p>
    <h1><Headline></h1>
    <p class="lede"><1-2 paragraph lede that names the result></p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">…</span></div>
      <!-- 4–6 meta items: Role / Organization / Years / Stack / Result / Partner -->
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/<slug>/hero.webp">
        <img src="/img/projects/<slug>/hero.jpg" alt="…" width="1600" height="900">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">
  <h2>The brief</h2>
  <p>…</p>

  <div class="case-stats-row">     <!-- 3–4 hero stats -->
    <div class="case-stat"><strong>…</strong><span>…</span></div>
  </div>

  <h2>What we did / built</h2>
  <h3>Subsection</h3>
  <p>…</p>

  <div class="gallery cols-1">     <!-- or cols-2 -->
    <figure>
      <picture>…</picture>
      <figcaption class="gallery-caption">…</figcaption>
    </figure>
  </div>

  <h2>What we learned</h2>
  <ul>…</ul>

  <h2>Why it mattered</h2>
  <blockquote>…</blockquote>
  <p>…</p>

  <p class="muted">References: <a>…</a> · <a>…</a></p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/<prev-slug>/"><span class="dir">← Previous</span><span class="title"><Prev title></span></a>
    <a class="next" href="/projects/<next-slug>/"><span class="dir">Next →</span><span class="title"><Next title></span></a>
  </nav>
</div>
```

### 5. Wire up neighbors

Insert the new study between two existing ones in the case-nav chain.
Always update **both** neighbors:

- **Previous neighbor:** change their `class="next"` link to point at the new slug.
- **Next neighbor:** change their `class="prev"` link to point at the new slug.

### 6. Add a teaser to the projects index

Open `tools/pages/projects_index.py` and add a new `<a class="teaser">`
block in the right grid section. Keep teaser copy short — one
short paragraph plus 2 stat cells. Match the existing pattern.

### 7. Build & verify

```bash
python3 tools/build.py
```

Then spot-check:

```bash
# New page renders
ls projects/<slug>/index.html

# Hero image present
grep -c "/img/projects/<slug>/hero" projects/<slug>/index.html

# Case-nav chain holds
grep -oE 'class="(prev|next)"[^>]*href="[^"]*"' projects/<slug>/index.html
grep -oE 'class="next"[^>]*href="[^"]*"'   projects/<prev-slug>/index.html
grep -oE 'class="prev"[^>]*href="[^"]*"'   projects/<next-slug>/index.html

# Teaser on the index
grep -c 'href="/projects/<slug>/"' projects/index.html
```

## Reusable components

A few of the CSS / structural patterns that earn their keep across case
studies — use them as-is, don't reinvent.

### `.case-breakout`

Lets a block escape the 720px `.case-content` column out to ~1080px.
Use for wide media (Issuu reader, video grids, large composites).

```html
<div class="case-breakout">
  <!-- wide content -->
</div>
```

### `.video-grid-2`

A 2×2 responsive video grid with 16:9 boxes that stack to one column
under 760px. Used on the Democracy Symposium (celebrity videos) and the
Campaign for Mount Vernon (priority film shorts). Wrap in
`.case-breakout` so it actually has room to breathe.

```html
<div class="case-breakout">
  <div class="video-grid-2">
    <figure>
      <div class="film-video">
        <iframe src="https://player.vimeo.com/video/…" title="…"
                loading="lazy" allow="autoplay; fullscreen; picture-in-picture"
                allowfullscreen></iframe>
      </div>
      <figcaption><strong>Title</strong> — caption</figcaption>
    </figure>
    <!-- … -->
  </div>
</div>
```

### `.film` (single featured video)

For one big featured video with side copy. Used on Pickens Plan
(launch ad + whiteboard), Mount Vernon orientation film, AR tour
trailer, etc.

```html
<div class="film">
  <div class="film-video">
    <iframe src="https://www.youtube-nocookie.com/embed/<id>" title="…"
            loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen></iframe>
  </div>
  <div class="film-body">
    <div class="film-head">
      <h3 class="film-title">Title</h3>
      <span class="film-meta">duration · context</span>
    </div>
    <p class="film-tagline">Description</p>
  </div>
</div>
```

### `.issuu-embed`

Wraps an Issuu reader iframe. Two modifiers:

- `.widescreen` → 16:9 aspect (good for two-page spreads or single-page
  with the gold side fill, used on the Democracy Poll).
- `.single-page` → 8.5×11 portrait (rare; use only when you genuinely
  want a tall column).

```html
<div class="case-breakout">
  <div class="issuu-embed widescreen">
    <iframe src="https://e.issuu.com/embed.html?d=<doc>&u=<user>&pageLayout=singlePage" title="…" loading="lazy" allowfullscreen></iframe>
  </div>
</div>
```

### `.podcast-embed`

Wraps a Spotify Creators / Apple Podcasts mini-player iframe. Caps
width at 540px, rounded corners, deep background.

```html
<div class="podcast-embed">
  <iframe src="https://creators.spotify.com/pod/…/embed/…" title="…"
          height="102" width="100%" frameborder="0" scrolling="no" loading="lazy"></iframe>
</div>
```

## When to update the homepage Selected Work

The three teasers on the home page are the highest-priority pitch
surface on the site. Most new case studies do NOT replace one of those
three — they slot into `/projects/` and get linked from there.

Only swap a homepage teaser when a new study is unambiguously stronger
than what's there. Edit `tools/pages/home.py` directly.

## Common gotchas

- **Don't edit generated `index.html` files.** Always edit the template
  and rebuild.
- **Update the case-nav chain on BOTH neighbors.** A one-sided update
  creates a dead-end.
- **`.case-content` is 720px max.** Anything wider (videos, Issuu, big
  galleries) needs `.case-breakout`.
- **Hero dimensions matter** — set `width` and `height` attributes on
  the `<img>` so the browser reserves space and CLS stays low.
- **Smart quotes / em-dashes** use HTML entities (`&rsquo;`, `&mdash;`,
  `&ldquo;`, `&rdquo;`) for portability — but Unicode in the Python
  template strings is fine and gets through the build untouched.
