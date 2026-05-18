# Analytics

GA4 (`G-0RQJ767Q41`) is wired site-wide via direct gtag.js, not Google
Tag Manager. The instrumentation lives in two places:

- `tools/_partials/head.html` — gtag bootstrap + content_group
- `assets/js/analytics.js` — events (outbound, downloads, video)
- `assets/js/nav.js` — lightbox open event (piggybacks on the existing
  lightbox code)

## What gets sent

### Automatic (gtag default + enhanced measurement)

- `page_view` (on load)
- `scroll` (at 90% page depth — coarse; the default)
- `click` (outbound links — but GA4's auto-click loses context, which
  is why we also fire our own `outbound_click` below)
- `file_download` (some extensions auto — but we override to ensure
  consistent params)

### Custom (from `analytics.js` + `nav.js`)

| Event | Fires when | Params |
|---|---|---|
| `outbound_click` | External link clicked | `link_url`, `link_domain`, `link_text`, `source_page` |
| `file_download` | PDF / DOCX / XLSX / PPTX / ZIP click (any host) | `file_name`, `file_extension`, `link_text`, `link_url`, `source_page` |
| `resume_download` | CV/resume PDF specifically | `file_name`, `source_page` |
| `video_start` | First play, any Vimeo or YouTube embed | `video_provider`, `video_id`, `video_title`, `source_page` |
| `video_progress` | 25 / 50 / 75 % milestones | above + `video_percent` |
| `video_complete` | Video ends | same as `video_start` |
| `lightbox_open` | Case-study screenshot opened in lightbox | `image_src`, `image_alt`, `image_index`, `image_total`, `source_page` |

### Content groups

Set on every `page_view` via the gtag `config` call. Derived from the
URL path:

| Group | Pages |
|---|---|
| `Home` | `/` |
| `Bio` | `/bio/` |
| `CV` | `/cv/` |
| `Projects` | `/projects/` (the index) |
| `Mount Vernon` | mount-vernon-website, tessitura-ticketing, mount-vernon-virtual-tour, be-washington, washingtons-war-4d, orientation-film, ar-tour, numismatic-kiosk, audio-tour, short-films, magazine, covid-response, mv-explorer, agent-711, campaign-mount-vernon, democracy-symposium |
| `TRPL` | trpl-reading-room, google-grants-optimizer |
| `Edelman` | multiplier |
| `Emotive` | mlk-memorial, pickens-plan |
| `Personal` | travel-passport, family-tree |
| `Other` | fallback |

Adding a new case study slug? Add it to the right group array in
`tools/_partials/head.html` so it shows up correctly in GA4 reports.

## GA4 admin setup (one-time)

These have to be configured in the GA4 web UI — the code can't do it.

### 1. Register custom dimensions

*Admin → Custom definitions → Custom dimensions → Create.*

Register these so the params show up in reports as sliceable
dimensions (otherwise they're invisible in standard reports):

| Dimension name | Scope | Event parameter |
|---|---|---|
| Source page | Event | `source_page` |
| Link domain | Event | `link_domain` |
| Link text | Event | `link_text` |
| File extension | Event | `file_extension` |
| File name | Event | `file_name` |
| Video provider | Event | `video_provider` |
| Video title | Event | `video_title` |
| Video ID | Event | `video_id` |
| Video percent | Event | `video_percent` |
| Image alt | Event | `image_alt` |

You can register up to 50 event-scoped custom dimensions per GA4
property. The list above uses 10.

### 2. Mark key events (conversions)

*Admin → Events → toggle "Mark as key event."* Recommended:

- `resume_download` — primary conversion (someone took the CV)
- `outbound_click` — secondary conversion (especially TR Library and
  MountVernon.org clicks)
- `video_start` — engagement conversion (optional)

### 3. (Optional) Create audiences

*Admin → Audiences → New audience.* Useful ones for this portfolio
site:

- **Resume downloaders** — fired `resume_download` in the last 30 days
- **Mount Vernon readers** — `content_group = "Mount Vernon"` and
  ≥ 2 page_views
- **Video engagers** — fired any `video_progress` event with
  `video_percent ≥ 50`

## Reading the data

### "Which chapter of my career is people reading?"

*Reports → Engagement → Pages and screens → change Page path dimension
to Content group.* Sort by Sessions or Engagement time. The Mount
Vernon vs TRPL vs Emotive split is the strategic-level signal a
recruiter or search committee is giving you when they land on the site.

### "Which case study films are getting watched?"

*Explore → Free form → Dimensions: Video provider, Video title,
Source page. Metrics: Event count.* Filter where Event name =
`video_start` or `video_complete`.

### "Where do visitors go next?"

*Explore → Free form → Dimensions: Source page, Link domain. Metrics:
Event count.* Filter where Event name = `outbound_click`. This shows
the path from each case study to the live site / external reference.

### "Did the resume download actually drive engagement?"

*Explore → Funnel → Step 1: page_view, Step 2: resume_download,
Step 3: page_view on /projects/.* Or use the **Resume downloaders**
audience above and compare it to "All users" engagement metrics.

## Privacy

- No cookies set beyond Google's standard analytics cookies (gtag.js)
- No fingerprinting, no third-party trackers beyond GA4
- Vimeo and YouTube iframes load their own cookies when played
  (`youtube-nocookie.com` reduces the YT footprint)
- No PII is sent in any event — link text is truncated to 80 chars
  and image alt to 120 chars

## Troubleshooting

**An event isn't appearing in reports.**
- Register the custom dimensions in GA4 admin (above)
- Wait 24–48 hours — non-realtime reports lag

**Realtime works but standard reports don't.**
- That's expected. Standard reports process daily, not in real time.
  Realtime is for verification; reports are for analysis.

**Vimeo events aren't firing.**
- Check the network tab — `player.vimeo.com/api/player.js` should load
  when a vimeo iframe is on the page. If it doesn't, the page may not
  have any vimeo embeds, or Vimeo's CDN is blocked.

**YouTube events aren't firing.**
- Check that the iframe src includes `?enablejsapi=1` — analytics.js
  adds this on load, but only for iframes whose src matches
  `youtube-nocookie.com/embed` or `youtube.com/embed`. If a page has
  a non-standard embed format, update the selector in `analytics.js`.

**Lightbox events aren't firing.**
- The lightbox is in `assets/js/nav.js`. If lightbox open events are
  silent, check that `gtag` is defined at the time the lightbox opens
  (it should be — the head loads the gtag stub before any body script
  executes).
