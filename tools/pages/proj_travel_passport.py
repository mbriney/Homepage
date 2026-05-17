BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Personal project · 2026</p>
    <h1>Travel Passport: A Decade of TripIt Flights, Rebuilt as a Virtual Passport</h1>
    <p class="lede">Seven tabs, no backend. A flippable customs-stamp passport, a Flighty-style stats page, a flat and spinning-globe world map, a U.S. choropleth, 130+ achievements, a timeline scrubber, and a full log &mdash; all from a decade of my TripIt history.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Status</span><span class="value">Live</span></div>
      <div class="meta-item"><span class="label">Stack</span><span class="value">Vanilla JS + D3 + Python</span></div>
      <div class="meta-item"><span class="label">Hosting</span><span class="value">GitHub Pages</span></div>
      <div class="meta-item"><span class="label">Refresh</span><span class="value">Weekly via GitHub Actions</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/travel-site/hero.webp">
        <img src="/img/projects/travel-site/hero.jpg" alt="Travel Passport — passport stamps for visited countries and US states" width="1600" height="1040">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>What it is</h2>
  <p>An interactive virtual passport built from a decade of my TripIt flight history. Click around the tabs at the top:</p>
  <ul>
    <li><strong>Passport</strong> &mdash; a flippable book with a cover, bio page, and customs-style stamp pages for every visited country and U.S. state. Tap a stamp to see every flight that contributed to it.</li>
    <li><strong>Stats</strong> &mdash; Flighty-style summary cards: distance &amp; time totals, top airports/airlines/routes, cabin class, aircraft types and specific tails, carbon footprint, region breakdown, time-of-day and day-of-week histograms.</li>
    <li><strong>World</strong> &mdash; toggleable between a flat Natural Earth map and a 3D rotating orthographic globe. Visited countries are shaded, every route is a great-circle arc, and every visited airport is a dot (top hubs in gold).</li>
    <li><strong>USA</strong> &mdash; a choropleth of visited U.S. states.</li>
    <li><strong>Achievements</strong> &mdash; 130+ TravStats-inspired badges across explorer / distance / collector / elite / special categories.</li>
    <li><strong>Timeline</strong> &mdash; a scrubber that plays the world map and stats forward in time as you drag a month slider, with milestone callouts as they unlock.</li>
    <li><strong>Log</strong> &mdash; a reverse-chronological feed of every flight.</li>
  </ul>

  <div class="gallery cols-2">
    <figure><picture><source type="image/webp" srcset="/img/projects/travel-site/02.webp"><img src="/img/projects/travel-site/02.jpg" alt="Travel Passport stats"></picture></figure>
    <figure><picture><source type="image/webp" srcset="/img/projects/travel-site/03.webp"><img src="/img/projects/travel-site/03.jpg" alt="Travel Passport world map"></picture></figure>
    <figure><picture><source type="image/webp" srcset="/img/projects/travel-site/01.webp"><img src="/img/projects/travel-site/01.jpg" alt="Travel Passport stamps"></picture></figure>
    <figure><picture><source type="image/webp" srcset="/img/projects/travel-site/04.webp"><img src="/img/projects/travel-site/04.jpg" alt="Travel Passport achievements"></picture></figure>
  </div>

  <h2>How it works</h2>
  <h3>One static site, no backend</h3>
  <p>Every map, stat, achievement, and stamp is computed client-side from a handful of JSON files. No server, no API, no auth. The whole thing deploys to GitHub Pages as a static folder.</p>

  <h3>Enrichment pipeline</h3>
  <p>TripIt gives you a flight, an aircraft type code, and a couple of timestamps. A small Python pipeline enriches that into something richer:</p>
  <ul>
    <li><strong>BTS On-Time Performance</strong> + <strong>FAA Aircraft Registry</strong> (both free) &mdash; for US-reporting carriers since 2003, this gets us the actual tail number flown and the manufacturer/model/year of that specific aircraft.</li>
    <li><strong>AeroDataBox</strong> (paid free tier) &mdash; fills in foreign-carrier segments and the most recent flights.</li>
    <li><strong>OurAirports / OpenFlights / world-atlas / us-atlas</strong> &mdash; the reference data underneath the maps.</li>
  </ul>
  <p>The pipeline is rate-limited, caches every response, and stays well within the free tier for everything.</p>

  <h3>Self-updating via GitHub Actions</h3>
  <p>A weekly workflow re-fetches my TripIt history, re-runs the enrichments, commits the data changes back to <code>main</code>, and triggers a Pages redeploy. The site is always current without me touching anything.</p>

  <div class="case-stats-row">
    <div class="case-stat"><strong>130+</strong><span>achievements</span></div>
    <div class="case-stat"><strong>0</strong><span>backend services</span></div>
    <div class="case-stat"><strong>Weekly</strong><span>auto-refresh</span></div>
    <div class="case-stat"><strong>D3</strong><span>flat + globe + choropleth</span></div>
  </div>

  <p style="margin-top:2.5rem">
    <a class="btn btn-primary" href="https://mbriney.github.io/Travel/" target="_blank" rel="noopener">Live site &rarr;</a>
    <a class="btn btn-ghost" href="https://github.com/mbriney/Travel" target="_blank" rel="noopener" style="margin-left:.5rem">Source on GitHub &rarr;</a>
  </p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/multiplier/"><span class="dir">&larr; Previous</span><span class="title">Multiplier</span></a>
    <a class="next" href="/projects/family-tree/"><span class="dir">Next &rarr;</span><span class="title">Briney Family Tree</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/travel-passport/index.html",
        title="Travel Passport — Matt Briney",
        description="A virtual passport built from a decade of my TripIt flight history. Vanilla JS + D3, no backend, self-updating weekly via GitHub Actions.",
        active="projects",
        canonical="https://mattbriney.com/projects/travel-passport/",
        og_image="/img/projects/travel-site/hero.jpg",
        body=BODY,
    )
