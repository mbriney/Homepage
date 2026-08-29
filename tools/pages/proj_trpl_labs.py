BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Theodore Roosevelt Presidential Library · 2026</p>
    <h1>labs.trlibrary.com: Twenty-Odd Production Tools, Zero Servers</h1>
    <p class="lede">A new institution with a two-person communications shop and no engineering team. Every tool a vendor would have built cost $40,000 and an annual contract. So we built them instead &mdash; as static files on GitHub Pages, with scheduled jobs doing any work that needs fresh data. There is no backend anywhere in the portfolio, and no API key has ever reached a browser.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Chief Communications &amp; Marketing Officer &mdash; build &amp; ship</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">Theodore Roosevelt Presidential Library</span></div>
      <div class="meta-item"><span class="label">Years</span><span class="value">2025&ndash;2026</span></div>
      <div class="meta-item"><span class="label">Stack</span><span class="value">Vanilla JS · Python · GitHub Pages · GitHub Actions</span></div>
      <div class="meta-item"><span class="label">Hosting cost</span><span class="value">$0</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/trpl-labs/hero.webp">
        <img src="/img/projects/trpl-labs/hero.jpg" alt="Dusk over the river valley in the North Dakota Badlands" width="1600" height="900">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>A presidential library opening in 2026 needs roughly the same digital surface area as any modern cultural institution: trip planning, collections search, ticketing signals, donor recognition, review monitoring, email production, quizzes, maps, timelines. The standard route is to buy each one from a vendor, at somewhere between $15,000 and $60,000 a piece, plus a recurring licence and a support queue.</p>
  <p>We had a communications team of two and no engineers. The constraint turned out to be the architecture.</p>

  <div class="case-stats-row">
    <div class="case-stat"><strong>20+</strong><span>Production tools</span></div>
    <div class="case-stat"><strong>$0</strong><span>Hosting cost</span></div>
    <div class="case-stat"><strong>0</strong><span>Servers</span></div>
    <div class="case-stat"><strong>0</strong><span>Keys in the browser</span></div>
  </div>

  <h2>The pattern</h2>
  <p>Every tool follows the same shape, and the shape is the whole idea:</p>
  <ul>
    <li><strong>The product is static files</strong> served from GitHub Pages on a <code>*.labs.trlibrary.com</code> subdomain.</li>
    <li><strong>Anything needing fresh data is a scheduled GitHub Action</strong> that fetches, transforms, and <em>commits the result as JSON</em>. The site reads a file. It never calls an API at runtime.</li>
    <li><strong>Credentials live in repository secrets</strong>, used only inside Actions. Nothing sensitive is ever shipped to a browser.</li>
    <li><strong>Git is the database.</strong> Every number on screen is also a line in version history, which means every change is diffable, attributable and reversible.</li>
  </ul>
  <p>The unlock is realizing how much institutional data changes <em>daily</em> rather than <em>per request</em>. Opening hours, review counts, ticket availability, a press portal, a social calendar &mdash; none of that needs a live query. A cron job and a committed JSON file serve it perfectly, for nothing, with no uptime risk and no 3 a.m. page.</p>

  <h3>Two jobs that are really CORS proxies</h3>
  <p>My favourite pieces of the whole portfolio are the two places where a scheduled Action exists purely because a browser isn&rsquo;t allowed to do the thing.</p>
  <p><strong>HoursEmbed</strong> puts the Library restaurant&rsquo;s opening hours on a Squarespace site. The hours live in Drupal on trlibrary.com, which blocks cross-origin requests &mdash; so the browser can&rsquo;t read them. A scheduled job scrapes the page server-side, where the block doesn&rsquo;t apply, and commits static JSON. Its failure design is the best one-liner in the repo set: <em>if parsing fails, the script exits non-zero and the last good file stays published.</em> A layout change upstream degrades to stale-but-correct, never to blank.</p>
  <p><strong>AcquiaDAM-Photo-Embed</strong> renders the press portal as native gallery tiles. It downloads each thumbnail rather than hot-linking, because Acquia serves previews through pre-signed URLs that expire &mdash; so hot-linked images 403 intermittently. Same principle: do the impossible-in-a-browser part on a schedule, ship the result as a file.</p>

  <h2>Five worth describing</h2>

  <h3>Trip Planner &mdash; deliberately not AI</h3>
  <p><a href="https://trip.labs.trlibrary.com" target="_blank" rel="noopener">trip.labs.trlibrary.com</a> is a ten-step wizard that builds a Badlands itinerary. It leads with desire rather than logistics: <em>what do you want to see and do</em> is step one; where you&rsquo;re travelling from is step six.</p>
  <p>In a portfolio full of AI work, the interesting claim is the opposite one: <strong>&ldquo;It&rsquo;s a rule-based wizard &mdash; deterministic, no AI, nothing to hallucinate.&rdquo;</strong> It schedules against real pace budgets, places time-anchored events only on days they actually run, and puts meals inside real opening hours. Stops within about 110 miles fold into the Medora block as day trips; farther ones become en-route legs with gateway overnights. It recommends open-jaw airports and greys out rental companies that would strand your car.</p>
  <p>Its data integrity system deserves the credit, though. A weekly Action scrapes five regional sources, and <em>on failure preserves prior events and opens a GitHub issue</em> &mdash; one broken scrape never empties the planner. A second job checks every booking URL for rot and diffs advertised show seasons, but never edits data: <strong>automation watches the hours and tells us when to look; a person makes the change.</strong></p>

  <h3>TRC Widget &mdash; and the thing the graph revealed</h3>
  <p><a href="https://trc.labs.trlibrary.com" target="_blank" rel="noopener">trc.labs.trlibrary.com</a> makes 139,714 archival items across 52 partner institutions searchable. The problem statement is exact: the Theodore Roosevelt Center&rsquo;s advanced search exposes seven facets with no autocomplete on any of them, over a controlled Library of Congress vocabulary &mdash; so a visitor typing <em>&ldquo;henry cabot lodge&rdquo;</em> gets zero results while <em>&ldquo;lodge&rdquo;</em> surfaces <em>&ldquo;Blodgett.&rdquo;</em> The vocabulary is excellent; the door into it is the problem.</p>
  <p>The fix caches the taxonomy as static JSON on a weekly schedule, so facet searches cost the Center&rsquo;s server nothing and their flaky full-text endpoint is never in the critical path.</p>
  <p>Then the relationship graph turned up something genuinely interesting: <strong>Roosevelt sits on 51% of all edges.</strong> He is connected to everything, so he obscures everything. A second precomputed layout removes his direct links &mdash; and the real communities appear: the Army command clustering around Corbin and MacArthur, the White House staff around Loeb and Cortelyou. <em>That&rsquo;s the six degrees, and it only appears once the sun is out of the frame.</em></p>
  <p>The repo also records a reversal I like: the first version hand-rolled its force layout to stay dependency-free. <em>That was the wrong call &mdash; a graph layout is exactly the thing not to hand-roll, and the result looked it.</em></p>

  <h3>Medora Weather &mdash; built in a day</h3>
  <p><a href="https://weather.labs.trlibrary.com" target="_blank" rel="noopener">weather.labs.trlibrary.com</a> is the thesis in miniature: <strong>only the scheduled job ever calls the National Weather Service. The widget and images are static files, so no amount of visitor traffic touches the government API.</strong></p>
  <p>It ships two outputs &mdash; a JavaScript widget <em>and</em> eight hotlinkable PNG/SVG variants &mdash; which is what lets non-technical staff drop weather into an email, a Drupal block or a signage screen without asking a developer. If NWS is unreachable it falls back to the last published forecast, flags it stale, and shows a &ldquo;data delayed&rdquo; note rather than going blank. Active alerts tighten polling from fifteen minutes to five. The README keeps the honest caveat: <em>this is an ambient display, not a life-safety alerting channel.</em></p>

  <h3>Benefactor Kiosk &mdash; the v1 that was too clever</h3>
  <p>Donor recognition on a 60-inch 4K touchscreen, running unattended twelve-plus hours a day. Roughly 5,466 recognized records across 13 societies &mdash; with Founding Member and Supporter alone accounting for about 4,874 of them, which is exactly why the interaction model mattered.</p>
  <p>The version history is the lesson. <strong>v1 computed donor society from dollar thresholds. The real data didn&rsquo;t work that way</strong> &mdash; each donor already carried an assigned society value, and the kiosk should read that field rather than infer it. v1 also built a bespoke 4K on-screen keyboard with diacritic normalization; v2 deleted it in favour of a level selector and an A&ndash;Z index. Both times the answer was less cleverness.</p>
  <p>It displays no dollar amounts &mdash; recognition by tier only, which is standard donor-wall practice and a deliberate privacy decision. And it has the engineering you only write for kiosks: burn-in mitigation, and <em>any uncaught error returns the kiosk to Attract mode rather than showing an error screen.</em></p>

  <h3>Rough Rider &mdash; the one that&rsquo;s a game</h3>
  <p>Roosevelt&rsquo;s life from 1858 to 1919 as ten platformer chapters, each ending in its own mini-game and a learning recap. Forty fact achievements, twenty historically-motivated enemy types, and characters drawn entirely in code &mdash; TR visibly ages and changes costume across all ten chapters. <strong>Every sound is synthesized at runtime with Web Audio; there are no audio files at all</strong>, including ten chiptune themes.</p>
  <p>The serious engineering is the mobile work: touch controls that build nothing on desktop and feed the same key handlers, and iOS Safari&rsquo;s <code>100vh</code>-behind-the-toolbars problem solved by measuring the visual viewport and letterboxing a 16:9 box inside the actually-visible area.</p>
  <p>Content came from the Library&rsquo;s own digitized book collection with dates and quotations verified against source texts. One editorial call worth repeating: Roosevelt&rsquo;s death is placed in the closing legacy screen rather than inside the Amazon chapter, to keep each chapter period-accurate.</p>

  <div class="gallery cols-1">
    <figure>
      <picture>
        <source type="image/webp" srcset="/img/projects/trpl-labs/01.webp">
        <img src="/img/projects/trpl-labs/01.jpg" alt="Detail of an artifact from the Theodore Roosevelt Presidential Library collection" loading="lazy" width="1600" height="900">
      </picture>
      <figcaption class="gallery-caption">Most of these tools exist to put a visitor in front of an object like this one, faster.</figcaption>
    </figure>
  </div>

  <h2>The rest of the shelf</h2>
  <p>The other tools, each a scheduled job and a static file:</p>
  <ul>
    <li><strong><a href="https://reviews.labs.trlibrary.com" target="_blank" rel="noopener">Reviews</a></strong> &mdash; daily collection across Google, TripAdvisor, Yelp and Facebook, model-classified into a hand-authored theme vocabulary, with response triage and a screened pull-quote widget. A new theme only enters the vocabulary after three reviews over at least fourteen days.</li>
    <li><strong><a href="https://ticketing.labs.trlibrary.com" target="_blank" rel="noopener">Ticketing Widgets</a></strong> &mdash; six availability widgets on a fifteen-minute refresh. Risk is modelled as supply against expected demand <em>for that weekday</em>, because percent-sold alone is misleading: a day can sit at 60% the night before and still sell out from walk-ups.</li>
    <li><strong><a href="https://quiz.labs.trlibrary.com" target="_blank" rel="noopener">Quizzes</a></strong> &mdash; 85 fifteen-question quizzes, with live head-to-head play running peer-to-peer over WebRTC. The README explains why: <em>GitHub Pages is static hosting &mdash; there is nothing on it that can introduce two browsers to each other.</em></li>
    <li><strong><a href="https://campus.labs.trlibrary.com" target="_blank" rel="noopener">Campus Map</a></strong> &mdash; a 3D model taken from a 338 MB source file to a <strong>7.7 MB</strong> delivered GLB, with markers that hide when a berm blocks the line of sight, via a precomputed heightfield rather than a raycast engine.</li>
    <li><strong><a href="https://familytree.labs.trlibrary.com" target="_blank" rel="noopener">Family Tree</a></strong> &mdash; 46 people across six generations. The deploy renders the whole tree in a headless DOM to confirm nobody overlaps before publishing; a broken build never reaches the domain.</li>
    <li><strong><a href="https://timeline.labs.trlibrary.com" target="_blank" rel="noopener">Timeline</a></strong> &mdash; TR&rsquo;s life against world events, in two files with zero dependencies.</li>
    <li><strong><a href="https://photogallery.labs.trlibrary.com" target="_blank" rel="noopener">Photo Gallery</a></strong> &mdash; 926 MB of originals become 5.6 MB of thumbnails; the build only processes what it hasn&rsquo;t already built.</li>
    <li><strong><a href="https://socialcalendar.labs.trlibrary.com" target="_blank" rel="noopener">Social Calendar</a></strong> &mdash; a read-only public view of the Hootsuite schedule. Posts appear on time without a rebuild, because the page ships future items and holds each back until its send time.</li>
    <li><strong><a href="https://rsvp.labs.trlibrary.com" target="_blank" rel="noopener">Digital Invite</a></strong> &mdash; animated envelope invitations with no backend and no JavaScript dependencies.</li>
    <li><strong><a href="https://newsletter.labs.trlibrary.com" target="_blank" rel="noopener">Newsletter Builder</a></strong> &mdash; a browser-only email builder whose saved HTML file <em>is</em> its own project format.</li>
    <li><strong>Link Checker</strong> &mdash; a weekly crawl of every trlibrary.com page for broken links and spelling, published as a triage report.</li>
    <li><strong>Anniversaries</strong> &mdash; five-year milestones in TR&rsquo;s life, for commemoration planning.</li>
    <li><strong><a href="https://elkhorn.labs.trlibrary.com" target="_blank" rel="noopener">Elkhorn Panoramas</a></strong> &mdash; 360&deg; views of the Elkhorn Ranch ruins, in seven near-identical files of about 750 bytes each, because a router would have been more code than the thing itself.</li>
  </ul>

  <h2>What it cost, honestly</h2>
  <p>Hosting is genuinely zero. Compute isn&rsquo;t quite: the Reviews pipeline pays for a scraping service and a small language model, which together run to a few dollars a year, and the ticketing widgets sit on an API the Library already licenses. The claim is &ldquo;no servers and no hosting bill,&rdquo; not &ldquo;free.&rdquo;</p>
  <p>One tool is also honestly a prototype rather than a product: the <a href="https://lbc.labs.trlibrary.com" target="_blank" rel="noopener">Living Building Challenge dashboard</a> currently runs on demo data while the building-management integration is negotiated. It is on this page because its README states the constraint everything else here obeys: <em>never put an API token in a public page &mdash; route it through a scheduled job that writes a static file instead.</em></p>

  <h2>What I&rsquo;d carry forward</h2>
  <ul>
    <li><strong>Ask whether the data changes per request or per day.</strong> Almost all institutional data is the latter, and the latter doesn&rsquo;t need a server.</li>
    <li><strong>Scheduled jobs are a legitimate backend.</strong> They also make excellent CORS proxies, which is the trick that unlocks the awkward integrations.</li>
    <li><strong>Design the failure before the feature.</strong> The best line in the portfolio is &ldquo;the last good file stays published.&rdquo;</li>
    <li><strong>Automation should raise a hand, not make the call.</strong> The link-rot checker opens an issue; it never edits the data.</li>
    <li><strong>Delete the clever thing.</strong> Twice on the kiosk, the right answer was less engineering, not more.</li>
    <li><strong>Constraints beat budgets.</strong> No servers meant no procurement, no vendor, no annual contract, and nothing that can go down at 3 a.m.</li>
  </ul>

  <h2>Why it mattered</h2>
  <blockquote>A nonprofit with no engineering team can operate every one of these indefinitely, because there is nothing to operate.</blockquote>
  <p>Twenty-plus tools that would have cost several hundred thousand dollars to procure, running for the price of a domain name &mdash; and maintainable by whoever comes next, because the entire stack is files in a repository.</p>

  <p class="muted">Source: the <a href="https://github.com/orgs/Theodore-Roosevelt-Presidential-Library/repositories" target="_blank" rel="noopener">Theodore Roosevelt Presidential Library GitHub organization</a>. Related: <a href="/projects/trpl-reading-room/">AI at the Library</a> · <a href="/projects/google-grants-optimizer/">the Google Ad Grant optimizer</a></p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/trpl-potus-visit/"><span class="dir">&larr; Previous</span><span class="title">A Sitting President &amp; a Medal of Honor</span></a>
    <a class="next" href="/projects/trpl-drip-campaign/"><span class="dir">Next &rarr;</span><span class="title">Seven Systems, One Visitor</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/trpl-labs/index.html",
        title="labs.trlibrary.com: Twenty-Odd Production Tools, Zero Servers — Matt Briney",
        description="A two-person communications shop shipped 20+ production tools for a presidential library on static hosting and scheduled jobs — no backend anywhere, and no API key in a browser.",
        active="projects",
        canonical="https://mattbriney.com/projects/trpl-labs/",
        og_image="/img/projects/trpl-labs/hero.jpg",
        body=BODY,
    )
