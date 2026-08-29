"""Generates one detail page per Toolkit tool at /toolkit/<slug>/.

Data-driven: every page comes from the TOOLS list below, so adding a tool is
one dict. build() returns a LIST of page dicts (see build.py::main).

Each page targets its own long-tail search intent — "free broken link checker
for museums", "embeddable photo gallery nonprofit" — rather than competing on
the owner's name.
"""

ORG = "https://github.com/Theodore-Roosevelt-Presidential-Library"
SITE = "https://mattbriney.com"

# ---------------------------------------------------------------- tool data
# slug, name, shot, live, repo, category, badge, tagline, search_desc,
# problem, how, detail, adopt (list), stack, related (slugs)
TOOLS = [
dict(
  slug="trip-planner", name="Trip Planner", shot="trip-planner",
  live="https://trip.labs.trlibrary.com", repo="TripPlanner",
  category="Visitor planning", badge="Adaptable",
  tagline="A rule-based itinerary wizard that turns a visit into a trip.",
  search_desc="A free, open-source trip planner for museums and destinations. Ten-step wizard, deterministic scheduling, .ics export, shareable links. No AI, no backend, MIT licensed.",
  problem="Destination institutions have a harder marketing problem than city museums: nobody is ever nearby. The visitor has to plan a journey, book a flight, and find somewhere to sleep — and most museum websites hand them a hours-and-directions page and wish them luck.",
  how="A ten-step wizard that leads with desire rather than logistics. <em>What do you want to see and do</em> is step one; where you're travelling from is step six. It schedules against real pace budgets (roughly six, eight or ten-hour days), places time-anchored events only on days they actually run, and puts meals inside real opening hours.",
  detail="The line worth quoting from the repo: <strong>&ldquo;It's a rule-based wizard — deterministic, no AI, nothing to hallucinate.&rdquo;</strong> In a portfolio full of AI work, choosing not to use a model is the more interesting decision. An itinerary that invents an attraction, or a closing time, is worse than no itinerary at all.<br><br>The data-integrity system is the other half. A weekly job scrapes regional sources and, <em>on failure, preserves the previous data and opens a GitHub issue</em> — one broken scrape never empties the planner. A second job checks every booking link for rot and diffs advertised seasons, but never edits anything: automation raises a hand, a person makes the call.",
  adopt=["Replace the regional data JSON with your own attractions, lodging and events.",
         "Set your own pace budgets and the radius at which a stop becomes a day trip.",
         "Point it at your own booking URLs; the link-rot checker will watch them."],
  stack="Vanilla JavaScript · Python scrapers · GitHub Actions · GitHub Pages",
  related=["ticketing-widgets", "weather", "campus-map"]),

dict(
  slug="link-checker", name="Link Checker", shot="link-checker",
  live="https://theodore-roosevelt-presidential-library.github.io/LinkChecker/", repo="LinkChecker",
  category="Site maintenance", badge="Fork &amp; go",
  tagline="Weekly crawl of your whole site for broken links and spelling errors.",
  search_desc="A free, open-source broken link checker and spell checker for nonprofit and museum websites. Weekly automated crawl, interactive triage report, no server required. MIT licensed.",
  problem="Every institutional website rots. Partner links die, PDFs move, a typo ships in a headline and sits there for two years. Commercial crawlers start around $50 a month and most small organizations simply never check.",
  how="A scheduled job crawls every page on your domain once a week, validates every link, and runs a spell check against a custom dictionary you control. The output is an interactive report you can triage — with a browser-local Ignore button for one-offs and a committed ignore file for permanent exceptions.",
  detail="This is the most immediately adoptable tool here: <strong>every organization-specific value is an environment variable.</strong> Set your root domain and your sitemap URL and it runs. Nothing in the code knows or cares that it was written for a presidential library.<br><br>It also documents its own false positives honestly — video and playlist pages are excluded from spell checking, because YouTube titles generate too much noise to be useful.",
  adopt=["Set ROOT_DOMAIN and SITEMAP_URLS to your own.",
         "Add institution-specific vocabulary to the custom words file.",
         "Enable GitHub Pages; the weekly report publishes itself."],
  stack="Python 3.12 · GitHub Actions (weekly cron) · GitHub Pages",
  related=["reviews", "hours-embed", "social-calendar"]),

dict(
  slug="photo-gallery", name="Photo Gallery", shot="photo-gallery",
  live="https://photogallery.labs.trlibrary.com", repo="PhotoGallery",
  category="Media", badge="Fork &amp; go",
  tagline="Drop in a folder of photos, get an embeddable masonry gallery.",
  search_desc="A free, open-source embeddable photo gallery for museums and nonprofits. Automatic thumbnails, lightbox, works on any website. No plugin, no backend, MIT licensed.",
  problem="Publishing a few hundred event photographs usually means a CMS plugin, a media library that chokes on full-resolution files, and a page that takes twenty seconds to load.",
  how="Put full-resolution originals in a folder and run one script. It generates thumbnails and web-sized images, writes the gallery, and gives you a single script tag you can paste into any website.",
  detail="The compression is the headline: <strong>926 MB of originals became 5.6 MB of thumbnails</strong>, with larger versions loaded only when someone opens the lightbox. The build is also idempotent — it only processes images it hasn't already built, so adding fifty photos to a gallery of a thousand takes seconds.<br><br>A small touch that matters in practice: the embed script works out its own URL, so if you ever move the files, the same snippet keeps working.",
  adopt=["Drop your photos into a named folder and run the build script.",
         "Paste the embed snippet into any CMS that allows a script tag.",
         "Adjust the size and quality constants at the top of the script if you want."],
  stack="Python + Pillow · vanilla JavaScript embed · GitHub Pages",
  related=["dam-embed", "panoramas", "digital-invite"]),

dict(
  slug="reviews", name="Reviews", shot="reviews",
  live="https://reviews.labs.trlibrary.com", repo="Reviews",
  category="Audience insight", badge="Adaptable",
  tagline="Daily review monitoring, sentiment and response triage across four platforms.",
  search_desc="A free, open-source review monitoring dashboard for museums and attractions. Collects Google, TripAdvisor, Yelp and Facebook reviews daily, classifies themes, and flags what needs a reply. MIT licensed.",
  problem="Reputation platforms charge hundreds a month to tell a small institution what its visitors are saying. Most nonprofits instead check Google reviews manually, occasionally, and never systematically enough to spot a trend.",
  how="A daily job collects reviews from Google, TripAdvisor, Yelp and Facebook, classifies each against a theme vocabulary your team writes by hand, tracks sentiment over time, and flags which reviews still need a response. It also screens quotes for a public pull-quote widget you can embed.",
  detail="Two design decisions worth stealing. <strong>New themes have to earn their place</strong> — a theme only enters the vocabulary after appearing in three reviews across at least fourteen days, so a single unusual complaint doesn't become a permanent category.<br><br>And the failure handling came from a real incident, documented in the repo: a model endpoint began returning a retirement error, the fallback silently swallowed it, and <em>the pipeline produced pure regex output under a model's name for several days without complaint.</em> The validation step that now blocks bad output exists because of that.",
  adopt=["Set your organization and listing IDs in the config file.",
         "Write your own theme vocabulary — this is the part that shouldn't be automated.",
         "Note the small running cost: a scraping service and a small model, a few dollars a year."],
  stack="Python 3.12 · GitHub Actions (daily) · static HTML dashboard",
  related=["link-checker", "social-calendar", "ticketing-widgets"]),

dict(
  slug="collections-search", name="Collections Search", shot="collections",
  live="https://trc.labs.trlibrary.com", repo="TRC-Widget",
  category="Collections", badge="Adaptable",
  tagline="Search and a relationship graph over 139,714 archival items.",
  search_desc="A free, open-source archival collections search widget with autocomplete and a relationship graph. Embeddable on any museum or library website. Caches its taxonomy so the source archive carries no load. MIT licensed.",
  problem="Controlled vocabularies are excellent and almost unusable without autocomplete. A visitor typing <em>&ldquo;henry cabot lodge&rdquo;</em> gets zero results while <em>&ldquo;lodge&rdquo;</em> surfaces <em>&ldquo;Blodgett.&rdquo;</em> The vocabulary isn't the problem — the door into it is.",
  how="The widget caches the archive's controlled vocabulary as static JSON on a weekly schedule and adds the autocomplete the original search lacks. Facet lookups then cost the source archive nothing, and its slower full-text endpoint is never in the critical path.",
  detail="The relationship graph turned up something genuinely interesting. <strong>Roosevelt sits on 51% of all edges</strong> — he is connected to everything, so he obscures everything. A second precomputed layout removes his direct links, and the real communities appear: the Army command clustering around Corbin and MacArthur, the White House staff around Loeb and Cortelyou. <em>That's the six degrees, and it only appears once the sun is out of the frame.</em><br><br>The repo also records a reversal: the first version hand-rolled its force layout to stay dependency-free. <em>That was the wrong call — a graph layout is exactly the thing not to hand-roll, and the result looked it.</em>",
  adopt=["Point it at your own collections API and taxonomy endpoint.",
         "The caching pattern transfers even if your API is completely different.",
         "The graph needs relationship data; without it the search still works standalone."],
  stack="Vanilla JavaScript (6.9 KB gzipped) · GitHub Actions · GitHub Pages",
  related=["timeline", "anniversaries", "family-tree"]),

dict(
  slug="ticketing-widgets", name="Ticketing Widgets", shot="ticketing",
  live="https://ticketing.labs.trlibrary.com", repo="TicketingWidgets",
  category="Visitor planning", badge="Needs ACME",
  tagline="Live availability, sell-out warnings and better-day suggestions.",
  search_desc="Free, open-source embeddable ticket availability widgets for museums using ACME Ticketing. Sell-out warnings, timed-entry grids, weekday demand modelling. No exposed API keys. MIT licensed.",
  problem="A visitor who drives four hours and can't get in is a worse outcome than one who books next month — but most ticketing systems give you no way to say &ldquo;this day is nearly gone, try Tuesday&rdquo; on your own website.",
  how="Six embeddable widgets refresh every fifteen minutes from your ticketing system's reporting API via a scheduled job. Your website reads a static file; no key ever reaches a browser.",
  detail="The modelling is smarter than a percentage. <strong>Percent-sold alone is misleading</strong> — a day can sit at 60% sold the night before and still sell out mid-morning from walk-up demand. Risk is therefore modelled as supply against <em>expected demand for that weekday</em>.<br><br>And it fails loudly by design: if the report structure ever changes, the job errors rather than quietly publishing wrong availability to visitors.",
  adopt=["Requires ACME Ticketing — the API client is the coupling.",
         "Thresholds and messaging live in a config file.",
         "The scheduled-job-writes-static-file pattern transfers to any ticketing platform."],
  stack="Python (stdlib only) · GitHub Actions (15 min) · vanilla JS widgets",
  related=["trip-planner", "weather", "hours-embed"]),

dict(
  slug="quizzes", name="Quizzes", shot="quizzes",
  live="https://quiz.labs.trlibrary.com", repo="Quizes",
  category="Education", badge="Fork &amp; go",
  tagline="Embeddable quizzes with shareable challenges and live head-to-head play.",
  search_desc="Free, open-source embeddable quizzes for museums and educators. Shareable challenge links and live two-player games over WebRTC, with no server. Add a quiz by writing one JSON file. MIT licensed.",
  problem="Quiz platforms want a subscription and put their branding on your content. Museums want a quiz embedded in their own page, in their own type, that a teacher can share with a class.",
  how="Each quiz is a single JSON file of fifteen questions. The widget mounts into a shadow root, so it can't inherit or fight your site's CSS. Results compress into a short shareable link, and two people can play head-to-head live.",
  detail="The multiplayer explanation is the clearest statement of the whole architecture: <strong>&ldquo;GitHub Pages is static file hosting — there is nothing on it that can introduce two browsers to each other, and GitHub offers no service that does.&rdquo;</strong> So live play runs peer-to-peer over WebRTC, using a free public broker purely to exchange connection details. No game state ever touches a server, because there is no server.<br><br>The repo is also honest that the score checksum is obfuscation, not security — if you attach a prize to a result, validate it somewhere you control.",
  adopt=["Copy an existing quiz JSON, change the questions, commit. No code changes.",
         "Facets and categories are defined in one index file.",
         "Live play depends on a free third-party broker; self-host it if usage grows."],
  stack="Vanilla JavaScript · shadow DOM · WebRTC · GitHub Pages",
  related=["timeline", "retro-game", "anniversaries"]),

dict(
  slug="timeline", name="Timeline", shot="timeline",
  live="https://timeline.labs.trlibrary.com", repo="TRTimelineWidget",
  category="Interpretation", badge="Fork &amp; go",
  tagline="A dual-axis timeline putting one life against world history.",
  search_desc="A free, open-source embeddable historical timeline widget. Shows a subject's life against contemporary world events. Two files, zero dependencies, works from a local file. MIT licensed.",
  problem="Dates mean nothing without context. &ldquo;1901&rdquo; is inert; &ldquo;1901, the year Marconi sent a signal across the Atlantic&rdquo; is a story. Most timeline plugins give you one track and a lot of JavaScript.",
  how="Two axes — your subject's life along the top, world and national events beneath — with a density weighting so the timeline stays readable at any zoom. Two files, no dependencies, no build step.",
  detail="It bootstraps itself: <strong>the script finds its own URL and loads its data file from the same folder</strong>, so the entire embed is one tag. The data is wrapped as a one-line JavaScript file rather than raw JSON specifically so the whole thing works when opened directly from disk — useful for a curator reviewing content without a web server.<br><br>One content rule worth adopting: wars are entered as two points, a beginning and an end, not as spans. Spans imply a continuity that a timeline can't honestly represent.",
  adopt=["Replace the data file with your own dated events, or point it at a JSON URL.",
         "Set the visible window and density weighting in the embed code.",
         "Only the content is subject-specific; the widget knows nothing about Roosevelt."],
  stack="Vanilla JavaScript · shadow DOM · zero dependencies",
  related=["anniversaries", "collections-search", "family-tree"]),

dict(
  slug="family-tree", name="Family Tree", shot="family-tree",
  live="https://familytree.labs.trlibrary.com", repo="FamilyTree",
  category="Interpretation", badge="Adaptable",
  tagline="An interactive genealogical tree that lays itself out.",
  search_desc="A free, open-source interactive family tree widget for museums and historic sites. Computes its own layout, includes sourced biographies, and gates its own deploy with a headless render check. MIT licensed.",
  problem="Family trees are usually published as a flat image, which means they can't be searched, can't be read on a phone, and have to be redrawn by a designer every time a fact changes.",
  how="People and relationships go in as data; the widget computes positions at runtime. Adding a person requires no coordinate work. Each person opens a sourced biography.",
  detail="The deploy is the part I'd copy. <strong>The workflow renders the entire tree in a headless browser and confirms every person places without overlapping and every biography opens — and only then publishes.</strong> A broken layout never reaches the live domain.<br><br>There's also a documented browser quirk worth knowing if you build shadow-DOM widgets: font-face rules are injected into the document head rather than the shadow root, because Chromium ignores <code>@font-face</code> declared inside a shadow tree.<br><br>The provenance work behind the data caught the Library about to publish the wrong death date for Roosevelt's own daughter, and recovered a grandchild the published books counted but never named.",
  adopt=["Replace the people and families data structures with your own.",
         "Layout is computed, so you never position anyone by hand.",
         "Keep the headless render check — it is the reason the tree never ships broken."],
  stack="Vanilla JavaScript · shadow DOM · GitHub Actions render gate",
  related=["timeline", "collections-search", "anniversaries"]),

dict(
  slug="campus-map", name="Campus Map", shot="campus-map",
  live="https://campus.labs.trlibrary.com", repo="CampusMap",
  category="Wayfinding", badge="Adaptable",
  tagline="A web 3D site model with occlusion-aware markers.",
  search_desc="A free, open-source 3D campus map for museums, parks and historic sites. Compresses a 338 MB model to 7.7 MB, with points of interest that hide behind buildings. MIT licensed.",
  problem="Architectural models arrive as hundreds of megabytes of geometry that no visitor will ever wait to download, so most institutions fall back to a flat illustrated map.",
  how="A processing pipeline converts the source model to binary, collapses scattered nodes into GPU instances, and applies geometry compression. Points of interest live in a separate file and can be edited visually.",
  detail="<strong>338 MB of source geometry became a 7.7 MB delivered file</strong> — roughly 102,000 scattered nodes collapsed into GPU instances, then compressed.<br><br>The clever part is the markers. Labels hide when a building or a berm blocks the line of sight, which normally requires a raycasting engine. Instead it uses a precomputed heightfield of about 145 KB — the occlusion is calculated once at build time rather than sixty times a second in the visitor's browser.",
  adopt=["The model is obviously yours to supply; the pipeline is documented.",
         "Points of interest are fully externalized, with a visual editor for placing them.",
         "Large source files need Git LFS and are excluded from the published site."],
  stack="Google model-viewer · Draco compression · Git LFS · GitHub Pages",
  related=["panoramas", "trip-planner", "weather"]),

dict(
  slug="weather", name="Weather", shot="weather",
  live="https://weather.labs.trlibrary.com", repo="MedoraWeather",
  category="Visitor planning", badge="Adaptable",
  tagline="Weather for your location as a widget and as hotlinkable images.",
  search_desc="A free, open-source weather widget for museums, parks and outdoor attractions. Backed by the National Weather Service, ships both a JavaScript widget and static images for email and signage. MIT licensed.",
  problem="Outdoor sites need weather in three places — the website, the visitor email, and the lobby screen — and only one of those can run JavaScript.",
  how="A scheduled job fetches the forecast and writes both a data file and a set of rendered images. The website uses the widget; email and signage hotlink a PNG.",
  detail="This is the architecture in miniature: <strong>only the scheduled job ever calls the weather API. The widget and images are static files, so no amount of visitor traffic touches the government service.</strong><br><br>The dual output is what makes it useful in a real organization — a communications assistant can put live weather in a newsletter without asking a developer for anything. Failure handling is explicit: if the source is unreachable it falls back to the last published forecast, marks it stale, and shows a &ldquo;data delayed&rdquo; note rather than going blank. Active alerts tighten polling from fifteen minutes to five.<br><br>The README keeps an honest caveat: this is an ambient display, not a life-safety alerting channel.",
  adopt=["Change the location coordinates in the config.",
         "US National Weather Service is free and keyless; swap the client for another provider elsewhere.",
         "Restyle the image variants to your own brand colours."],
  stack="Python · GitHub Actions · SVG/PNG rendering · GitHub Pages",
  related=["ticketing-widgets", "hours-embed", "trip-planner"]),

dict(
  slug="social-calendar", name="Social Calendar", shot="social-calendar",
  live="https://socialcalendar.labs.trlibrary.com", repo="SocialCalendar",
  category="Communications", badge="Needs Hootsuite",
  tagline="A read-only public view of what's scheduled to post.",
  search_desc="A free, open-source public view of your social media publishing schedule, pulled from Hootsuite. Lets colleagues see what's going out without a paid seat. MIT licensed.",
  problem="Scheduling tools charge per seat, so the people who most need to know what's publishing — curators, development, the director — are exactly the people who don't have a login.",
  how="A scheduled job pulls the upcoming schedule and publishes it as a read-only month and agenda view. Anyone with the link can see what's going out and when.",
  detail="A neat trick closes the gap between refreshes: <strong>scheduled posts appear on time without a rebuild</strong>, because the published file includes future items and the page holds each one back until its send time passes.<br><br>Preview images are downloaded and committed rather than hot-linked, because the platform serves media through pre-signed URLs that expire within minutes. And the credential check reports only whether a secret is <em>present</em> — never its value and never its length, which would leak information about short secrets.",
  adopt=["Requires Hootsuite; the API client is the coupling.",
         "Brand colours are pulled from a separate brand definition file.",
         "The hold-until-send-time pattern works for any scheduled content."],
  stack="Python · Pillow · GitHub Actions (3-hourly) · GitHub Pages",
  related=["newsletter", "reviews", "link-checker"]),

dict(
  slug="newsletter", name="Newsletter Builder", shot="newsletter",
  live="https://newsletter.labs.trlibrary.com", repo="NewsletterBuilder",
  category="Communications", badge="Adaptable",
  tagline="Build a newsletter in the browser, export drop-in email HTML.",
  search_desc="A free, open-source email newsletter builder that runs entirely in the browser and exports Constant Contact-ready HTML. No account, no backend, no subscription. MIT licensed.",
  problem="Email platform editors are slow, fight your brand, and lock the layout inside their account. Building a clean template by hand means writing table-based HTML in 2026.",
  how="A single page that runs entirely in your browser. Assemble blocks, then export HTML you can paste straight into your email platform.",
  detail="The persistence model is the interesting bit: <strong>the saved HTML file <em>is</em> the project format.</strong> Download the email with its design data embedded, and reopen it later to keep editing. There is no account, no cloud storage and nothing to lose access to.<br><br>The exported template comes in well under Constant Contact's size limit, which is the constraint that usually bites people who paste in image-heavy designs.",
  adopt=["Replace the brand template with your own colours and wordmark.",
         "The block engine is generic; the styling is the part that's specific.",
         "Works with any platform that accepts pasted HTML."],
  stack="Single-file HTML + JavaScript · no dependencies · no backend",
  related=["digital-invite", "social-calendar", "photo-gallery"]),

dict(
  slug="digital-invite", name="Digital Invite", shot="digital-invite",
  live="https://rsvp.labs.trlibrary.com", repo="DigitalInvite",
  category="Events", badge="Fork &amp; go",
  tagline="Animated envelope invitations with per-guest personalization.",
  search_desc="A free, open-source animated invitation embed for nonprofit events and galas. Paperless Post-style envelope, per-guest names, no backend and no subscription. MIT licensed.",
  problem="Paperless Post and its competitors charge per invitation and put their brand on your gala. For an organization sending a few thousand invitations a year, that adds up fast.",
  how="A JavaScript embed that turns any invitation artwork into an animated envelope, with the guest's name pulled from the link. Includes a no-code builder for staff who won't touch HTML.",
  detail="It ships with a genuinely rare piece of security honesty. Because the details block is markup in the host page, <strong>the browser parses it before the script loads</strong> — so a script tag placed there executes as part of the page and no embed can prevent it. The README says so plainly and offers a safe alternative, which is more than most commercial widgets do.<br><br>The download bundle is written by a small built-in archive writer rather than a library, so the whole thing still has zero JavaScript dependencies.",
  adopt=["Swap the brand palette; eight approved combinations all clear WCAG AA.",
         "Licensed brand fonts can't ship in a public repo — it degrades cleanly to web fonts.",
         "Everything is configured with data attributes on the embed tag."],
  stack="Vanilla JavaScript · no dependencies · GitHub Pages",
  related=["newsletter", "photo-gallery", "quizzes"]),

dict(
  slug="dam-embed", name="DAM Photo Embed", shot="dam-embed",
  live="https://portalphotos.labs.trlibrary.com/demo.html", repo="AcquiaDAM-Photo-Embed",
  category="Media", badge="Fork &amp; go",
  tagline="Render a digital asset portal as native tiles, not an iframe.",
  search_desc="A free, open-source embed that renders an Acquia DAM (Widen) press portal as native gallery tiles on your own page. Caches thumbnails to survive expiring URLs. MIT licensed.",
  problem="Digital asset platforms give you an iframe with a fixed height that looks nothing like your site, or nothing at all. Journalists then can't find your press images, and you end up emailing zip files.",
  how="A scheduled job snapshots the portal structure into cached JSON and downloads each thumbnail. The embed renders native, auto-sizing tiles in your own styling, with a lightbox.",
  detail="This exists because of a specific failure mode worth knowing about: <strong>the vendor serves preview images through pre-signed URLs that expire</strong>, so hot-linking them makes your gallery return broken images intermittently and unpredictably. The job downloads and commits each thumbnail instead.<br><br>It also runs server-side, where the vendor's cross-origin block doesn't apply — a browser genuinely cannot do this. It's one of two tools here where a scheduled job exists purely to be a CORS proxy.",
  adopt=["Add your portal shortcode to a config file barely a hundred bytes long.",
         "Works with any Acquia DAM portal — it was written to be generic.",
         "Twenty-one data attributes control tile size, spacing and behaviour."],
  stack="Node 18+ · GitHub Actions (6-hourly) · vanilla JS embed",
  related=["photo-gallery", "hours-embed", "panoramas"]),

dict(
  slug="hours-embed", name="Hours Embed", shot="hours-embed",
  live="https://theodore-roosevelt-presidential-library.github.io/HoursEmbed/", repo="HoursEmbed",
  category="Site maintenance", badge="Adaptable",
  tagline="Publish opening hours from one site onto another that can't read it.",
  search_desc="A free, open-source opening-hours embed that syncs hours from one website to another across a CORS block, using a scheduled job. Degrades to the last good data. MIT licensed.",
  problem="A restaurant, shop or partner site needs to show hours that live in your main CMS. The browser can't read them because of cross-origin restrictions, so the hours get copied by hand and quietly go stale.",
  how="A scheduled job scrapes the source page server-side — where the cross-origin block doesn't apply — and commits static JSON. The second site reads the file.",
  detail="This is the single clearest illustration of the whole approach, and its failure design is the best line in the entire toolkit: <strong>if the page structure changes and parsing fails, the script exits non-zero and the last good file stays published.</strong><br><br>A layout change upstream degrades to <em>stale but correct</em>, never to blank or wrong. Most integrations do the opposite — they fail open and publish nothing, at the exact moment a visitor is trying to work out whether you're open.",
  adopt=["The parser targets a specific markup structure — expect to adapt it.",
         "Theming is entirely CSS variables; it adopts the host page's fonts.",
         "The pattern transfers to any cross-origin content you need to mirror."],
  stack="Node 20 · GitHub Actions (scheduled) · vanilla JS embed",
  related=["dam-embed", "weather", "link-checker"]),

dict(
  slug="anniversaries", name="Anniversaries", shot="anniversaries",
  live="https://theodore-roosevelt-presidential-library.github.io/TRAnniversaries/", repo="TRAnniversaries",
  category="Planning", badge="Fork &amp; go",
  tagline="Track upcoming milestone anniversaries for content planning.",
  search_desc="A free, open-source milestone anniversary tracker for museums and historic sites. Surfaces upcoming five-year anniversaries of events you define, for commemoration and content planning. MIT licensed.",
  problem="Institutions miss their own anniversaries. The 125th of something significant arrives with three weeks' notice, and the content, the press pitch and the programme all get made in a hurry or not at all.",
  how="You supply dated events. It surfaces every five-year milestone falling in the current year and the next five, in tabs you can plan against.",
  detail="Small and useful rather than clever, which is the point — the whole thing is four files and a data file of curated events. The data rule that makes it forgiving: <strong>month and day are optional.</strong> An event you only know the year of still appears in the right year's tab, sorted to the bottom, rather than being excluded for incomplete data.<br><br>The sourcing note in the repo is a good habit to copy: it names the reference work the dates came from and tells you to verify any single date before publication.",
  adopt=["Replace the events data file with your own institution's dates.",
         "The milestone logic is pure date arithmetic — nothing to configure.",
         "Change the logo and a line of copy and it is entirely yours."],
  stack="Vanilla JavaScript · no build step · GitHub Pages",
  related=["timeline", "social-calendar", "collections-search"]),

dict(
  slug="panoramas", name="Panorama Viewer", shot="panoramas",
  live="https://elkhorn.labs.trlibrary.com", repo="elkhorn-panos",
  category="Interpretation", badge="Fork &amp; go",
  tagline="Full-screen 360° views of a place people can't easily reach.",
  search_desc="A free, open-source 360-degree panorama viewer for historic sites and remote locations. Drop in equirectangular images and duplicate one HTML file per view. MIT licensed.",
  problem="Some of the most important places an institution interprets are hard to visit — a ruin down a gravel road, a site that floods, a room that can't take foot traffic.",
  how="Drop equirectangular images into a folder and duplicate one small HTML file per view. The viewer libraries are vendored, so there's no CDN dependency and nothing to install.",
  detail="This is the smallest thing here and deliberately so: <strong>seven near-identical files of about 750 bytes each</strong>, rather than a router, a build step and a configuration format. For seven panoramas, a framework would have been more code than the thing itself.<br><br>It's a useful counterexample to the instinct to generalize early. If you add an eighth panorama, you copy a file — which takes ten seconds and will never break.",
  adopt=["Put your own equirectangular JPEGs in the panos folder.",
         "Duplicate one HTML file per view and change the filename it points at.",
         "Zero configuration, zero build, zero dependencies to install."],
  stack="Three.js + Panolens (vendored) · static HTML · GitHub Pages",
  related=["campus-map", "photo-gallery", "collections-search"]),

dict(
  slug="retro-game", name="Retro Game", shot="retro-game",
  live=None, repo="TRRetroGame",
  category="Education", badge="Reference",
  tagline="A historical life as a ten-chapter browser platformer.",
  search_desc="An open-source browser platform game teaching a historical figure's life across ten chapters. All audio synthesized at runtime, no sound files, works on mobile. MIT licensed reference implementation.",
  problem="Museum games are usually commissioned for tens of thousands of dollars, ship as a native app nobody downloads, and stop working after two OS updates.",
  how="Ten chapters spanning a life, each a short 2D platformer ending in its own mini-game and a learning recap. Forty fact achievements and twenty historically-motivated enemy types.",
  detail="Two things make this worth reading even if you never ship a game. <strong>Every sound is synthesized at runtime with Web Audio — there are no audio files at all</strong>, including ten chiptune themes and per-enemy defeat sounds. And the characters are drawn entirely in code, with the protagonist visibly ageing and changing costume across all ten chapters.<br><br>The mobile handling is the genuinely reusable part: touch controls build nothing on desktop and feed the same key handlers, and the iOS Safari <code>100vh</code>-behind-the-toolbars problem is solved by measuring the visual viewport and letterboxing a 16:9 box inside the actually-visible area.<br><br>Content came from the institution's own digitized book collection, with dates and quotations verified against source texts.",
  adopt=["Listed as a reference rather than a fork-and-go — the content is deeply specific.",
         "The Web Audio, mobile-viewport and code-drawn-sprite techniques all transfer.",
         "Currently robots-blocked pending a public launch decision."],
  stack="Vanilla JavaScript · Canvas · Web Audio · GitHub Pages",
  related=["quizzes", "timeline", "family-tree"]),
]

BY_SLUG = {t["slug"]: t for t in TOOLS}

ICON_LIVE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>'
             '<polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>')
ICON_SRC = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>')


def render(t):
    live_btn = (f'<a class="btn-tool btn-tool-live" href="{t["live"]}" target="_blank" '
                f'rel="noopener">{ICON_LIVE} Try it live</a>') if t["live"] else ''
    adopt = "".join(f"    <li>{a}</li>\n" for a in t["adopt"])
    rel = "".join(
        f'''      <a class="tool-rel" href="/toolkit/{s}/">
        <picture><source type="image/webp" srcset="/img/toolkit/{BY_SLUG[s]["shot"]}.webp">
        <img src="/img/toolkit/{BY_SLUG[s]["shot"]}.jpg" alt="" loading="lazy" width="800" height="500"></picture>
        <span>{BY_SLUG[s]["name"]}</span>
      </a>
''' for s in t["related"] if s in BY_SLUG)

    return f'''
<section class="section section--tight">
  <div class="container" style="max-width:820px">
    <a href="/toolkit/" class="back">&larr; All tools</a>
    <p class="eyebrow">Toolkit &middot; {t["category"]}</p>
    <h1 style="margin-bottom:.25em">{t["name"]}</h1>
    <p class="lede">{t["tagline"]}</p>

    <div class="tool-actions" style="padding-left:0;margin:1.25rem 0 1.75rem">
      {live_btn}
      <a class="btn-tool btn-tool-src" href="{ORG}/{t["repo"]}" target="_blank" rel="noopener">{ICON_SRC} Source on GitHub</a>
    </div>

    <div class="tool-shot" style="border-radius:8px;border:1px solid var(--border);margin-bottom:2rem">
      <picture>
        <source type="image/webp" srcset="/img/toolkit/{t["shot"]}.webp">
        <img src="/img/toolkit/{t["shot"]}.jpg" alt="Screenshot of {t["name"]}" width="800" height="500">
      </picture>
    </div>

    <h2>The problem</h2>
    <p>{t["problem"]}</p>

    <h2>How it works</h2>
    <p>{t["how"]}</p>

    <h2>Worth knowing</h2>
    <p>{t["detail"]}</p>

    <h2>Using it at your organization</h2>
    <ul>
{adopt}    </ul>
    <p class="muted"><strong>Stack:</strong> {t["stack"]}<br>
    <strong>Licence:</strong> MIT &mdash; use, modify and redistribute freely, commercially or not.<br>
    <strong>Hosting:</strong> static files; no server required.</p>

    <div class="tool-actions" style="padding-left:0;margin:1.75rem 0">
      {live_btn}
      <a class="btn-tool btn-tool-src" href="{ORG}/{t["repo"]}" target="_blank" rel="noopener">{ICON_SRC} Source on GitHub</a>
    </div>

    <h2>Related tools</h2>
    <div class="tool-rel-grid">
{rel}    </div>

    <p class="muted" style="margin-top:2rem">Built for the <a href="https://www.trlibrary.com" target="_blank" rel="noopener">Theodore Roosevelt Presidential Library</a> and released for anyone to use. See <a href="/toolkit/">all 19 tools</a>, or read <a href="/projects/trpl-labs/">how the whole system is built</a>.</p>
  </div>
</section>
'''


def software_ld(t):
    node = {
        "@type": "SoftwareApplication",
        "@id": f"{SITE}/toolkit/{t['slug']}/#software",
        "name": t["name"],
        "applicationCategory": "WebApplication",
        "operatingSystem": "Any (web browser)",
        "description": t["search_desc"],
        "url": f"{SITE}/toolkit/{t['slug']}/",
        "image": f"{SITE}/img/toolkit/{t['shot']}.jpg",
        "license": "https://opensource.org/licenses/MIT",
        "isAccessibleForFree": True,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "author": {"@id": f"{SITE}/#person"},
        "codeRepository": f"{ORG}/{t['repo']}",
    }
    if t["live"]:
        node["installUrl"] = t["live"]
    return node


def breadcrumb(t):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Toolkit", "item": SITE + "/toolkit/"},
            {"@type": "ListItem", "position": 3, "name": t["name"],
             "item": f"{SITE}/toolkit/{t['slug']}/"},
        ],
    }


def build():
    pages = []
    for t in TOOLS:
        pages.append(dict(
            out=f"toolkit/{t['slug']}/index.html",
            slug=t["slug"],
            title=f"{t['name']} — Free Open-Source Tool for Museums & Nonprofits",
            description=t["search_desc"],
            active="toolkit",
            canonical=f"{SITE}/toolkit/{t['slug']}/",
            og_image=f"/img/toolkit/{t['shot']}.jpg",
            body=render(t),
            extra_ld=[software_ld(t), breadcrumb(t)],
        ))
    return pages
