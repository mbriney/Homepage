# SEO — why mattbriney.com doesn't rank for "Matt Briney," and what fixes it

**Diagnosed:** August 29, 2026

## The finding

A search for `"Matt Briney"` returns, in order: Instagram (×2), X, the trlibrary.com
staff page, Unsplash, the TRPL press center, LinkedIn (×2), a Wikipedia article
about a different person, and **a San Diego potter with the same name**.

mattbriney.com appears nowhere on page one.

## It is not an on-page problem

The technical SEO is already good, and further tweaking it will not help:

| Check | Status |
|---|---|
| `robots.txt` allows all, points to sitemap | ✅ |
| `<title>` and `<h1>` both carry the name | ✅ |
| Canonical URLs on every page | ✅ |
| JSON-LD `Person` with `sameAs` | ✅ |
| `ProfilePage` schema on `/bio/` | ✅ |
| Sitemap with 38 URLs, honest `lastmod` dates | ✅ |
| Only 2 `noindex` pages (404, annual-report viewer) | ✅ correct |
| Open Graph + Twitter card on every page | ✅ |

## It is a link and age problem

Two facts explain the ranking:

1. **The domain is ~3.5 months old** (first commit May 10, 2026).
2. **Almost nothing links to it.** Of the 9 profiles the `sameAs` block claims,
   only **github.com/mbriney** actually links back.

`sameAs` is a *claim* the site makes about itself. Google confirms identity by
checking the other direction. One-way claims carry very little weight — which is
why LinkedIn and Instagram, which have both authority and corroboration, win the
name query.

The single most damaging gap: **trlibrary.com has a staff page about Matt and a
press center naming him as media contact, and neither links to mattbriney.com.**
That is a high-authority domain — one that just absorbed 312 press placements —
declining to vouch for the personal site.

---

## The fix, in priority order

### Tier 1 — free, ~30 minutes, do these first

Each of these adds a reciprocal link that confirms the entity. All are under
Matt's own control.

| # | Where | What to do |
|---|---|---|
| 1 | **trlibrary.com/staff-members/matt-briney** | Add `mattbriney.com` to the bio. Highest-authority link available. |
| 2 | **LinkedIn** | Profile → Contact info → Website → `https://mattbriney.com`. LinkedIn is the #1 result for the name; a link from it transfers both authority and identity. |
| 3 | **X / Twitter** | Profile → Edit → Website field. |
| 4 | **Instagram** (`@mbriney`) | Edit profile → Links → add the site. |
| 5 | **Unsplash** (`@mbriney`) | Account → Profile → Personal site. |
| 6 | **IMDb** (`nm9778875`) | Contribute → Personal details → Official sites. |
| 7 | **GitHub** (`mbriney`) | ✅ already links back — nothing to do. |

### Tier 2 — infrastructure

8. **Google Search Console** — verify the domain (DNS TXT record), submit
   `https://mattbriney.com/sitemap.xml`, then use *URL Inspection → Request
   indexing* on the homepage. This is the only way to know whether the site is
   indexed at all, and it surfaces crawl errors that are otherwise invisible.
9. **Bing Webmaster Tools** — same steps. Worth doing because Bing's index also
   feeds Copilot and several AI search products.

### Tier 3 — earn authority over time

10. **The `/toolkit/` page is the most winnable target.** Nobody competes for
    "free open source tools for museums." Long-tail traffic builds the domain
    authority that eventually lifts the name query. Already optimized (below).
11. Link `mattbriney.com` from the TRPL GitHub org profile README.
12. When speaking or being quoted, ask for the personal site in the bio line
    rather than only a job title.

---

## What was changed in the repo (Aug 29, 2026)

### Person schema enrichment (`tools/build.py`)

- Added `description`, `alumniOf` (Virginia Tech), `knowsAbout` (8 topics),
  and `award` (Thea, Telly).
- Added `worksFor.sameAs` pointing at the Wikipedia article for the Library.
- **Added `https://www.trlibrary.com/staff-members/matt-briney` as the first
  `sameAs` entry** — an authoritative third-party page *about* this person is a
  stronger entity signal than a self-managed social profile.
- Homepage `WebPage` now declares `mainEntity` (not just `about`) pointing at the
  Person node — "this page *is* this person," not "this page mentions them."

### Toolkit page optimization (`tools/pages/toolkit.py`)

- Title changed from `Toolkit — Free Tools for Museums & Nonprofits` to
  **`Free Open-Source Tools for Museums & Nonprofits`** — leads with the words
  people actually search rather than an internal label.
- Meta description rewritten around real queries: trip planner, collections search
  widget, review monitoring, broken-link checker.
- **Stable `id` anchor on all 19 tool cards** (`#trip-planner`, `#link-checker`,
  …), each heading self-linking, so individual tools can be linked and cited.
- **`FAQPage` schema with 5 questions** — eligible for rich results and matches
  how people phrase these searches ("are these really free", "do I need a
  developer", "will this work with WordPress").
- A generic `extra_ld` hook was added to `build.py` so any page can contribute
  its own schema nodes.

---

## Expectations

A three-month-old personal domain competing against LinkedIn for a person's name
is a genuinely hard fight. Once the Tier 1 links land, expect **weeks to a few
months**, not days. The Toolkit page will likely rank for its long-tail terms
well before the homepage ranks for the name.

Re-check with `site:mattbriney.com` in Google in two weeks. If nothing is
indexed by then, the problem is discovery, and Search Console will say why.
