# Performance

**Baseline (PageSpeed Insights, Aug 29 2026, Moto G Power / Slow 4G):**

| | Mobile | Desktop |
|---|---|---|
| Performance | **74** | 84 |
| First Contentful Paint | 3.6 s | 0.8 s |
| Largest Contentful Paint | 4.5 s | 1.2 s |
| Total Blocking Time | **0 ms** | 290 ms |
| Cumulative Layout Shift | **0** | 0.012 |
| Speed Index | 4.9 s | 1.1 s |

Accessibility 95 · Best Practices 100 · SEO 100.

## The diagnosis

TBT of 0 ms and CLS of 0 mean JavaScript execution and layout stability were
already perfect. The entire mobile deficit was **time to first paint** — the
browser had nothing to render for 3.6 seconds.

PSI's top insight said it plainly: **Render-blocking requests — est. savings
1,350 ms.**

The site's own assets were never the problem. Over the wire they are tiny:
HTML 6.9 KB, CSS 9.9 KB, JS 5.4 KB. The cost was **Google Fonts**, which forced
a serialized three-hop chain on the critical path:

```
HTML → [new origin: fonts.googleapis.com, DNS+TLS] → font CSS (15.5 KB)
     → [another origin: fonts.gstatic.com, DNS+TLS] → ~113 KB of woff2
```

Nothing could paint until all of that completed. Measured TLS handshake to
fonts.gstatic.com alone was ~170 ms from a fast connection; on emulated Slow 4G
it is far worse.

## What was changed

### 1. Self-hosted the fonts — the main fix

Fraunces and Inter are both SIL OFL 1.1, which expressly permits
redistribution. The Latin subsets now live in `assets/fonts/`:

| File | Size |
|---|---|
| `fraunces-roman-latin.woff2` | 65.8 KB |
| `fraunces-italic-latin.woff2` | 41.1 KB |
| `inter-roman-latin.woff2` | 47.3 KB |

These are variable fonts, so one file per style covers every weight the site
uses — `assets/css/fonts.css` declares just three `@font-face` rules with
`font-weight: 100 900`.

This removes **two origins and two TLS handshakes** from the critical path, and
collapses the three-hop chain into one same-origin request on an
already-open connection.

It also enables something that was previously impossible: **preloading the font
files directly.** Google's URLs are content-hashed and change without notice,
so they can't be preloaded. Ours can, and both above-the-fold faces now are.

### 2. Preloaded the LCP image

`preload_hero_for()` in `build.py` previously only fired for case studies. It
now covers:

- **Homepage and `/bio/`** — the portrait, which is the mobile LCP element.
  Preloaded with `imagesrcset` + `imagesizes` that exactly match the `<source>`
  element, so the browser picks the same variant and does not download twice.
- **Toolkit detail pages** — the tool screenshot.

### 3. Deferred Google Analytics

`gtag.js` was ~70 KB of mostly-unused JavaScript plus a third-party connection,
competing with first paint for no benefit. It now loads on the first user
interaction (`pointerdown`, `keydown`, `scroll`, `touchstart`) or after 3 s of
idle, whichever comes first. Pageviews are still recorded.

### 4. Minified CSS

`build.py` now emits `style.min.css` (47.6 KB → 37.4 KB) and `fonts.min.css`,
and the pages link the minified files. Sources stay readable.

## Critical path, before and after

| | Before | After |
|---|---|---|
| Origins on critical path | 3 | **1** |
| Extra DNS + TLS handshakes | 2 | **0** |
| Serialized round trips before paint | 3 | **1** |
| Render-blocking bytes (wire) | ~132 KB | ~128 KB |
| LCP image preloaded | no | **yes** |
| Analytics on critical path | yes (~70 KB) | **no** |

Total bytes barely moved — that was never the issue. **The number of blocking
round trips went from three to one**, which is what the 1,350 ms estimate was
measuring.

## Known remaining items

**"Use efficient cache lifetimes — 521 KiB" — cannot be fixed on GitHub Pages.**
GitHub serves everything with `Cache-Control: max-age=600` and provides no way
to configure headers. The only real fix is putting a CDN (Cloudflare's free tier
would do) in front of the domain, which would also let you set long cache
lifetimes on the fingerprinted font files. Worth doing eventually; not worth
doing for this alone.

**"Improve image delivery — 347 KiB"** — teaser thumbnails use full 1600 px hero
images for cards that render around 350 px wide. Fixing it means generating
smaller variants and adding `srcset` to the teaser markup in `home.py` and
`projects_index.py`. Worth doing, but note these images are lazy-loaded and
below the fold: this reduces total page weight, it does not improve LCP.

**Accessibility 95** — one flagged contrast pair. Worth locating and correcting.

## Re-measuring

The PageSpeed Insights API has a daily quota that was exhausted during this
work, so the improvements here are **predicted, not verified**. Re-run
https://pagespeed.web.dev against `https://mattbriney.com/` after deploying and
compare FCP and LCP against the 3.6 s / 4.5 s baseline above.
