ORG = "https://github.com/Theodore-Roosevelt-Presidential-Library"

ICON_LIVE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>'
             '<polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>')
ICON_SRC = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>')


def tool(name, shot, url, repo, desc, badge, alt):
    live = (f'<a class="btn-tool btn-tool-live" href="{url}" target="_blank" rel="noopener">'
            f'{ICON_LIVE} Try it live</a>') if url else ''
    return f'''      <div class="tool-card">
        <div class="tool-shot">
          <picture>
            <source type="image/webp" srcset="/img/toolkit/{shot}.webp">
            <img src="/img/toolkit/{shot}.jpg" alt="{alt}" loading="lazy" width="800" height="500">
          </picture>
        </div>
        <div class="tool-body">
          <span class="tool-badge">{badge}</span>
          <h3 style="margin-top:.5rem">{name}</h3>
          <p>{desc}</p>
        </div>
        <div class="tool-actions">
          {live}
          <a class="btn-tool btn-tool-src" href="{ORG}/{repo}" target="_blank" rel="noopener">{ICON_SRC} Source</a>
        </div>
      </div>
'''


VISITOR = [
    tool("Trip Planner", "trip-planner", "https://trip.labs.trlibrary.com", "TripPlanner",
         "A ten-step wizard that builds a multi-day regional itinerary. Rule-based and deterministic &mdash; no AI, nothing to hallucinate. Schedules against real pace budgets and folds nearby stops into day trips.",
         "Adaptable", "The Trip Planner wizard asking what a visitor wants to see and do"),
    tool("Ticketing Widgets", "ticketing", "https://ticketing.labs.trlibrary.com", "TicketingWidgets",
         "Six embeddable timed-entry availability widgets on a fifteen-minute refresh, with sell-out warnings and better-day suggestions. Models risk as supply against expected demand for that weekday.",
         "Needs ACME", "Sell-out alert banner and timed-entry availability grid"),
    tool("Quizzes", "quizzes", "https://quiz.labs.trlibrary.com", "Quizes",
         "Eighty-five embeddable fifteen-question quizzes with shareable challenge links and live head-to-head play peer-to-peer over WebRTC. Adding a quiz is one JSON file and no code changes.",
         "Fork &amp; go", "The quiz embed documentation and preview page"),
    tool("Timeline", "timeline", "https://timeline.labs.trlibrary.com", "TRTimelineWidget",
         "A dual-axis embeddable timeline &mdash; your subject&rsquo;s life on top, world history beneath. Two files, zero dependencies, no build step. All content lives in one data file.",
         "Fork &amp; go", "The Roosevelt timeline comparison view"),
    tool("Family Tree", "family-tree", "https://familytree.labs.trlibrary.com", "FamilyTree",
         "An interactive genealogical tree that computes its own layout, so adding people needs no coordinate work. The deploy renders the whole tree in a headless browser to confirm nobody overlaps before publishing.",
         "Adaptable", "Family Tree — 46 people across six generations"),
    tool("Photo Gallery", "photo-gallery", "https://photogallery.labs.trlibrary.com", "PhotoGallery",
         "Drop a folder of full-resolution photos, run one script, get a masonry gallery embeddable on any site. 926 MB of originals became 5.6 MB of thumbnails, and the build only processes what it hasn&rsquo;t already built.",
         "Fork &amp; go", "Photo Gallery — 926 MB of originals reduced to 5.6 MB"),
    tool("Digital Invite", "digital-invite", "https://rsvp.labs.trlibrary.com", "DigitalInvite",
         "Paperless Post&ndash;style animated envelope invitations with per-guest personalization, a no-code builder, and a matching email template. No backend and no JavaScript dependencies.",
         "Fork &amp; go", "The digital invitation builder with brand colour options"),
    tool("Campus Map", "campus-map", "https://campus.labs.trlibrary.com", "CampusMap",
         "A web 3D site model taken from a 338 MB source file to 7.7 MB delivered, with points of interest that hide when a building blocks the line of sight. POIs are externalized and there&rsquo;s a visual editor.",
         "Adaptable", "The 3D campus model showing the building and trail network"),
    tool("Weather", "weather", "https://weather.labs.trlibrary.com", "MedoraWeather",
         "A National Weather Service&ndash;backed widget plus eight hotlinkable image variants, so staff can drop conditions into an email, a CMS block or a signage screen without a developer.",
         "Adaptable", "The Medora weather widget showing a five-day forecast"),
]

STAFF = [
    tool("Link Checker", "link-checker", "https://theodore-roosevelt-presidential-library.github.io/LinkChecker/", "LinkChecker",
         "A weekly crawl of your entire site for broken links and spelling errors, published as an interactive triage report with a local ignore list. Every organization-specific value is an environment variable.",
         "Fork &amp; go", "The link and spelling report dashboard showing pages crawled and issues found"),
    tool("Reviews", "reviews", "https://reviews.labs.trlibrary.com", "Reviews",
         "Daily collection of public reviews across Google, TripAdvisor, Yelp and Facebook, classified into a hand-authored theme vocabulary, with response triage and a screened pull-quote widget.",
         "Adaptable", "The reviews dashboard showing rating trend and theme breakdown"),
    tool("Social Calendar", "social-calendar", "https://socialcalendar.labs.trlibrary.com", "SocialCalendar",
         "A read-only public view of your social publishing schedule, so colleagues can see what&rsquo;s going out without a seat in the scheduling tool. Scheduled posts appear on time without a rebuild.",
         "Needs Hootsuite", "Social Calendar — month, agenda and filter views"),
    tool("Newsletter Builder", "newsletter", "https://newsletter.labs.trlibrary.com", "NewsletterBuilder",
         "A browser-only email newsletter builder that exports drop-in Constant Contact HTML. The saved file <em>is</em> the project format &mdash; reopen it later to keep editing.",
         "Adaptable", "The newsletter builder with its block palette and live preview"),
    tool("DAM Photo Embed", "dam-embed", "https://portalphotos.labs.trlibrary.com/demo.html", "AcquiaDAM-Photo-Embed",
         "Renders any Acquia DAM press portal as native gallery tiles instead of a fixed-height iframe. Snapshots the portal on a schedule and caches thumbnails, because the vendor&rsquo;s preview URLs expire.",
         "Fork &amp; go", "A press portal rendered as native gallery tiles"),
    tool("Hours Embed", "hours-embed", "https://theodore-roosevelt-presidential-library.github.io/HoursEmbed/", "HoursEmbed",
         "Publishes opening hours from one site onto another that can&rsquo;t read it directly. A scheduled job scrapes server-side, where the cross-origin block doesn&rsquo;t apply. If parsing fails, the last good file stays published.",
         "Adaptable", "The hours embed shown in light and dark themes"),
]

COLLECTIONS = [
    tool("Collections Search", "collections", "https://trc.labs.trlibrary.com", "TRC-Widget",
         "Search and a relationship graph over 139,714 archival items across 52 partner institutions. Adds the autocomplete a controlled vocabulary needs, and caches the taxonomy so the source archive carries no load.",
         "Adaptable", "The collections search widget with autocomplete over 139,714 items"),
    tool("Anniversaries", "anniversaries", "https://theodore-roosevelt-presidential-library.github.io/TRAnniversaries/", "TRAnniversaries",
         "Tracks upcoming five-year milestone anniversaries of events you define, for commemoration and content planning. Swap one data file for your own institution&rsquo;s dates.",
         "Fork &amp; go", "The anniversaries view listing upcoming milestone dates by year"),
    tool("Panorama Viewer", "panoramas", "https://elkhorn.labs.trlibrary.com", "elkhorn-panos",
         "Full-screen 360&deg; panorama viewing for a historic site. Drop your equirectangular images in a folder and duplicate one HTML file per view. There is no logic to change.",
         "Fork &amp; go", "A 360-degree panorama of the Elkhorn Ranch site"),
    tool("Retro Game", "retro-game", None, "TRRetroGame",
         "A historical figure&rsquo;s life as a ten-chapter 2D platformer, each ending in a mini-game and a learning recap. All audio synthesized at runtime &mdash; no sound files. A working reference for browser-game engineering in a museum context.",
         "Reference", "The Rough Rider game title screen"),
]

BODY = '''
<section class="section">
  <div class="container">
    <p class="eyebrow">Toolkit</p>
    <h1 style="margin-bottom:.2em">Free tools for museums and nonprofits</h1>
    <p class="lede" style="max-width:64ch">Nineteen working tools built for the Theodore Roosevelt Presidential Library and released under the MIT license. Every one runs as static files with scheduled jobs doing anything that needs fresh data &mdash; so there is no server to buy, no vendor contract, and no hosting bill. Fork them, change a config file, ship.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="container">

    <p class="muted" style="border-left:3px solid var(--gold);padding-left:1rem;margin-bottom:1rem;max-width:70ch">
      <strong>Why this exists.</strong> Small institutions are quoted $15,000&ndash;$60,000 per tool for things that are, underneath, a data file and a page. We built ours instead, on an architecture a two-person communications team can maintain. There is no reason for the next museum to pay for them either. <a href="/projects/trpl-labs/">How the whole system works &rarr;</a>
    </p>

    <div class="tool-group">
      <h2>Visitor-facing</h2>
      <p class="muted">Embeds and experiences for your own website.</p>
      <div class="tool-grid">
''' + "".join(VISITOR) + '''      </div>
    </div>

    <div class="tool-group">
      <h2>Staff &amp; operations</h2>
      <p class="muted">Tools that save a communications or marketing team time every week.</p>
      <div class="tool-grid">
''' + "".join(STAFF) + '''      </div>
    </div>

    <div class="tool-group">
      <h2>Collections &amp; interpretation</h2>
      <p class="muted">Getting people closer to the objects.</p>
      <div class="tool-grid">
''' + "".join(COLLECTIONS) + '''      </div>
    </div>

    <div style="max-width:70ch">
      <h2 style="margin-top:3.5rem">How to read the labels</h2>
      <ul>
        <li><strong>Fork &amp; go</strong> &mdash; nothing institution-specific in the code. Change a data or config file and it is yours.</li>
        <li><strong>Adaptable</strong> &mdash; the engine is generic, but you will need to point it at your own content, styles or data source.</li>
        <li><strong>Needs ACME / Hootsuite</strong> &mdash; genuinely useful, but only if you already run that platform.</li>
        <li><strong>Reference</strong> &mdash; not built to be reused wholesale, but worth reading if you are building something similar.</li>
      </ul>

      <h2>The honest caveats</h2>
      <p>These were built for one institution and released because they might help another &mdash; not packaged as products. So:</p>
      <ul>
        <li>There is no support, no roadmap and no guarantee of maintenance. The licence is MIT; the warranty is none.</li>
        <li>Most READMEs document how the tool works for us, not a step-by-step setup for you. Expect to read some code.</li>
        <li>Hosting is free. A couple of tools do have small running costs &mdash; the review pipeline pays for scraping and a small language model, a few dollars a year.</li>
        <li>Brand assets, fonts and collection content are deliberately <em>not</em> included. The code is yours; the Roosevelt material is not.</li>
        <li>Three previews above are labelled cards rather than screenshots &mdash; those tools render their content live in the browser, which automated capture can&rsquo;t wait out. Use the live links.</li>
      </ul>

      <h2>If you use one</h2>
      <p>I would genuinely like to know &mdash; partly out of curiosity, mostly because knowing which of these are useful to other institutions is the only way to know which are worth improving. Issues and pull requests are welcome on any repository, and you can reach me at <a href="mailto:mkbriney@gmail.com">mkbriney@gmail.com</a>.</p>

      <p class="muted" style="margin-top:2rem">All source: <a href="https://github.com/orgs/Theodore-Roosevelt-Presidential-Library/repositories" target="_blank" rel="noopener">the Theodore Roosevelt Presidential Library GitHub organization</a>. Related reading: <a href="/projects/trpl-labs/">the architecture behind these tools</a>.</p>
    </div>

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
        og_image="/img/toolkit/trip-planner.jpg",
        body=BODY,
    )
