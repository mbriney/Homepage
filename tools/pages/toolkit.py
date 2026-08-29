def tool(name, url, repo, desc, badge=""):
    b = f'<span class="tool-badge">{badge}</span>' if badge else ""
    live = (f'<a href="{url}" target="_blank" rel="noopener">Live</a> · '
            if url else "")
    return f'''      <div class="tool">
        <h3><a href="https://github.com/Theodore-Roosevelt-Presidential-Library/{repo}" target="_blank" rel="noopener">{name}</a>{b}</h3>
        <div class="tool-links">{live}<a href="https://github.com/Theodore-Roosevelt-Presidential-Library/{repo}" target="_blank" rel="noopener">Source</a></div>
        <p>{desc}</p>
      </div>
'''

VISITOR = [
    tool("Trip Planner", "https://trip.labs.trlibrary.com", "TripPlanner",
         "A ten-step wizard that builds a multi-day regional itinerary. Rule-based and deterministic &mdash; no AI, nothing to hallucinate. Schedules against real pace budgets, places time-anchored events only on days they run, and folds nearby stops into day trips. Regional data is JSON; the engine is generic.",
         "Adaptable"),
    tool("Ticketing Widgets", "https://ticketing.labs.trlibrary.com", "TicketingWidgets",
         "Six embeddable timed-entry availability widgets on a fifteen-minute refresh, with sell-out warnings and better-day suggestions. Models risk as supply against expected demand for that weekday rather than raw percent-sold. Requires ACME Ticketing.",
         "ACME"),
    tool("Quizzes", "https://quiz.labs.trlibrary.com", "Quizes",
         "Eighty-five embeddable fifteen-question quizzes with shareable challenge links and live head-to-head play peer-to-peer over WebRTC. Adding a quiz is one JSON file and no code changes.",
         "Fork &amp; go"),
    tool("Timeline", "https://timeline.labs.trlibrary.com", "TRTimelineWidget",
         "A dual-axis embeddable timeline &mdash; your subject's life on top, world history beneath. Two files, zero dependencies, no build step. All content lives in one data file or a JSON URL you point at.",
         "Fork &amp; go"),
    tool("Family Tree", "https://familytree.labs.trlibrary.com", "FamilyTree",
         "An interactive genealogical tree that computes its own layout, so adding people needs no coordinate work. The deploy renders the whole tree in a headless browser to confirm nobody overlaps before publishing.",
         "Adaptable"),
    tool("Photo Gallery", "https://photogallery.labs.trlibrary.com", "PhotoGallery",
         "Drop a folder of full-resolution photos, run one script, get a masonry gallery embeddable on any site. 926 MB of originals became 5.6 MB of thumbnails. The build only processes what it hasn't already built.",
         "Fork &amp; go"),
    tool("Digital Invite", "https://rsvp.labs.trlibrary.com", "DigitalInvite",
         "Paperless Post&ndash;style animated envelope invitations with per-guest name personalization, a no-code builder, and a matching email template. No backend and no JavaScript dependencies.",
         "Fork &amp; go"),
    tool("Campus Map", "https://campus.labs.trlibrary.com", "CampusMap",
         "A web 3D site model taken from a 338 MB source file to a 7.7 MB delivered asset, with points of interest that hide when a building blocks the line of sight. POIs are fully externalized and there's a visual editor.",
         "Adaptable"),
    tool("Weather", "https://weather.labs.trlibrary.com", "MedoraWeather",
         "A National Weather Service&ndash;backed weather widget plus eight hotlinkable image variants, so staff can drop conditions into an email, a CMS block or a signage screen without a developer. Falls back to the last good forecast and flags it stale.",
         "Adaptable"),
]

STAFF = [
    tool("Link Checker", "https://theodore-roosevelt-presidential-library.github.io/LinkChecker/", "LinkChecker",
         "A weekly crawl of your entire site for broken links and spelling errors, published as an interactive triage report with a local ignore list. Every organization-specific value is an environment variable &mdash; set your domain and go.",
         "Fork &amp; go"),
    tool("Reviews", "https://reviews.labs.trlibrary.com", "Reviews",
         "Daily collection of public reviews across Google, TripAdvisor, Yelp and Facebook, classified into a hand-authored theme vocabulary, with response triage and a screened pull-quote widget. A new theme only enters the vocabulary after three reviews across at least fourteen days.",
         "Adaptable"),
    tool("Social Calendar", "https://socialcalendar.labs.trlibrary.com", "SocialCalendar",
         "A read-only public view of your social publishing schedule, so colleagues can see what's going out without a seat in the scheduling tool. Scheduled posts appear on time without a rebuild. Requires Hootsuite.",
         "Hootsuite"),
    tool("Newsletter Builder", "https://newsletter.labs.trlibrary.com", "NewsletterBuilder",
         "A browser-only email newsletter builder that exports drop-in Constant Contact HTML. The saved file <em>is</em> the project format &mdash; reopen it later to keep editing.",
         "Adaptable"),
    tool("Acquia DAM Photo Embed", "https://portalphotos.labs.trlibrary.com/demo.html", "AcquiaDAM-Photo-Embed",
         "Renders any Acquia DAM press portal as native gallery tiles on your own page instead of a fixed-height iframe. Snapshots the portal on a schedule and caches thumbnails, because the vendor's preview URLs are pre-signed and expire. Add a portal to one config file.",
         "Fork &amp; go"),
    tool("Hours Embed", "https://theodore-roosevelt-presidential-library.github.io/HoursEmbed/", "HoursEmbed",
         "Publishes opening hours from one site onto another that can't read it directly. A scheduled job scrapes server-side, where the cross-origin block doesn't apply, and commits static JSON. If parsing ever fails, the last good file stays published.",
         "Adaptable"),
]

COLLECTIONS = [
    tool("Collections Search Widget", "https://trc.labs.trlibrary.com", "TRC-Widget",
         "Search and a relationship graph over 139,714 archival items across 52 partner institutions. Adds the autocomplete a controlled vocabulary needs, and caches the taxonomy as static JSON so the source archive's server carries no load.",
         "Adaptable"),
    tool("Anniversaries", "https://theodore-roosevelt-presidential-library.github.io/TRAnniversaries/", "TRAnniversaries",
         "Tracks upcoming five-year milestone anniversaries of events you define, for commemoration and content planning. Swap one data file for your own institution's dates.",
         "Fork &amp; go"),
    tool("Panorama Viewer", "https://elkhorn.labs.trlibrary.com", "elkhorn-panos",
         "Full-screen 360&deg; panorama viewing for a historic site. Drop your equirectangular images in a folder and duplicate one HTML file per view. There is no logic to change.",
         "Fork &amp; go"),
    tool("Retro Game", None, "TRRetroGame",
         "A historical figure's life as a ten-chapter 2D platformer, each ending in a mini-game and a learning recap. All audio synthesized at runtime with Web Audio &mdash; no sound files. A working reference for browser-game engineering in a museum context.",
         "Reference"),
]

BODY = '''
<section class="section">
  <div class="container">
    <p class="eyebrow">Toolkit</p>
    <h1 style="margin-bottom:.2em">Free tools for museums and nonprofits</h1>
    <p class="lede" style="max-width:64ch">Nineteen working tools built for the Theodore Roosevelt Presidential Library and released under the MIT license. Every one runs as static files on GitHub Pages with scheduled jobs doing anything that needs fresh data &mdash; so there is no server to buy, no vendor contract, and no hosting bill. Fork them, change a config file, ship.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="container" style="max-width:860px">

    <p class="muted" style="border-left:3px solid var(--gold);padding-left:1rem;margin-bottom:2.5rem">
      <strong>Why this exists.</strong> Small institutions are quoted $15,000&ndash;$60,000 per tool for things that are, underneath, a data file and a page. We built ours instead, on an architecture a two-person communications team can maintain. There is no reason for the next museum to pay for them either. <a href="/projects/trpl-labs/">How the whole system works &rarr;</a>
    </p>

    <div class="tool-group">
      <h2>Visitor-facing</h2>
      <p class="muted">Embeds and experiences for your own website.</p>
      <div class="tool-list">
''' + "".join(VISITOR) + '''      </div>
    </div>

    <div class="tool-group">
      <h2>Staff &amp; operations</h2>
      <p class="muted">Tools that save a communications or marketing team time every week.</p>
      <div class="tool-list">
''' + "".join(STAFF) + '''      </div>
    </div>

    <div class="tool-group">
      <h2>Collections &amp; interpretation</h2>
      <p class="muted">Getting people closer to the objects.</p>
      <div class="tool-list">
''' + "".join(COLLECTIONS) + '''      </div>
    </div>

    <h2 style="margin-top:3rem">How to read the labels</h2>
    <ul>
      <li><strong>Fork &amp; go</strong> &mdash; nothing institution-specific in the code. Change a data or config file and it is yours.</li>
      <li><strong>Adaptable</strong> &mdash; the engine is generic but you will need to point it at your own content, styles or data source.</li>
      <li><strong>ACME / Hootsuite</strong> &mdash; genuinely useful, but only if you already run that platform.</li>
      <li><strong>Reference</strong> &mdash; not built to be reused wholesale, but worth reading if you are building something similar.</li>
    </ul>

    <h2>The honest caveats</h2>
    <p>These were built for one institution and released because they might help another &mdash; not packaged as products. So:</p>
    <ul>
      <li>There is no support, no roadmap and no guarantee of maintenance. The licence is MIT; the warranty is none.</li>
      <li>Most READMEs document how the tool works for us, not a step-by-step setup for you. Expect to read some code.</li>
      <li>Hosting is free. A couple of tools do have small running costs &mdash; the review pipeline pays for scraping and a small language model, a few dollars a year.</li>
      <li>Brand assets, fonts and collection content are deliberately <em>not</em> included. The code is yours; the Roosevelt material is not.</li>
    </ul>

    <h2>If you use one</h2>
    <p>I would genuinely like to know &mdash; partly out of curiosity, mostly because knowing which of these are useful to other institutions is the only way to know which are worth improving. Issues and pull requests are welcome on any repository, and you can reach me at <a href="mailto:mkbriney@gmail.com">mkbriney@gmail.com</a>.</p>

    <p class="muted" style="margin-top:2rem">All source: <a href="https://github.com/orgs/Theodore-Roosevelt-Presidential-Library/repositories" target="_blank" rel="noopener">the Theodore Roosevelt Presidential Library GitHub organization</a>. Related reading: <a href="/projects/trpl-labs/">the architecture behind these tools</a>.</p>

  </div>
</section>
'''

def build():
    return dict(
        out="toolkit/index.html",
        title="Toolkit — Free Tools for Museums & Nonprofits — Matt Briney",
        description="Nineteen open-source tools built for the Theodore Roosevelt Presidential Library and released under MIT — trip planning, collections search, review monitoring, link checking and more. No servers, no licence fees.",
        active="toolkit",
        canonical="https://mattbriney.com/toolkit/",
        body=BODY,
    )
