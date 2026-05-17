BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study &middot; Mount Vernon &middot; 2015–2024</p>
    <h1>Mount Vernon Explorer: How the Native App Became a Mobile-Web Companion That Nearly Tripled Adoption</h1>
    <p class="lede">The Mount Vernon Explorer launched in 2015 as a native iOS &amp; Android app built with <strong>XCO Software</strong> &mdash; a thoughtful, feature-rich visitor companion that almost nobody downloaded. We learned the hard lesson every cultural institution eventually learns: nobody downloads a native app for a one-day visit. We rebuilt it as a mobile-web experience and adoption climbed from <strong>under 5%</strong> of visitors to <strong>nearly 13%</strong>. Same content, no install friction, and a wider feature set than the app ever had.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Producer &amp; Product Owner</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">George Washington&rsquo;s Mount Vernon</span></div>
      <div class="meta-item"><span class="label">v1 Platform</span><span class="value">Native iOS &amp; Android · XCO Software (2015)</span></div>
      <div class="meta-item"><span class="label">v2 Platform</span><span class="value">Mobile web · no install required</span></div>
      <div class="meta-item"><span class="label">Adoption</span><span class="value">&lt;5% → ~13% (≈2.6&times;)</span></div>
      <div class="meta-item"><span class="label">Audience</span><span class="value">On-site visitors</span></div>
    </div>

    <div class="phone-strip" aria-label="Mount Vernon Explorer app screenshots">
      <div class="phone"><picture><source type="image/webp" srcset="/img/projects/mv-explorer/phone-01.webp"><img src="/img/projects/mv-explorer/phone-01.jpg" alt="Mount Vernon Explorer splash" width="420" height="745"></picture></div>
      <div class="phone"><picture><source type="image/webp" srcset="/img/projects/mv-explorer/phone-02.webp"><img src="/img/projects/mv-explorer/phone-02.jpg" alt="App screen" width="420" height="745"></picture></div>
      <div class="phone"><picture><source type="image/webp" srcset="/img/projects/mv-explorer/phone-03.webp"><img src="/img/projects/mv-explorer/phone-03.jpg" alt="App screen" width="420" height="745"></picture></div>
      <div class="phone"><picture><source type="image/webp" srcset="/img/projects/mv-explorer/phone-04.webp"><img src="/img/projects/mv-explorer/phone-04.jpg" alt="App screen" width="420" height="745"></picture></div>
      <div class="phone"><picture><source type="image/webp" srcset="/img/projects/mv-explorer/phone-05.webp"><img src="/img/projects/mv-explorer/phone-05.jpg" alt="App screen" width="420" height="745"></picture></div>
      <div class="phone"><picture><source type="image/webp" srcset="/img/projects/mv-explorer/phone-06.webp"><img src="/img/projects/mv-explorer/phone-06.jpg" alt="App screen" width="420" height="745"></picture></div>
      <div class="phone"><picture><source type="image/webp" srcset="/img/projects/mv-explorer/phone-07.webp"><img src="/img/projects/mv-explorer/phone-07.jpg" alt="App screen" width="420" height="745"></picture></div>
      <div class="phone"><picture><source type="image/webp" srcset="/img/projects/mv-explorer/phone-08.webp"><img src="/img/projects/mv-explorer/phone-08.jpg" alt="App screen" width="420" height="745"></picture></div>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>A Mount Vernon visit is a multi-hour outdoor exploration across 384 acres of grounds, 26 historic structures, gardens, a working farm, a distillery and gristmill, a museum, and a library. Most visitors arrive with a paper map and a lot of curiosity. The challenge: put a thoughtful, interpretive companion in everyone&rsquo;s pocket &mdash; one that works on their pace, their interests, and the experience of being on-site &mdash; <em>without</em> asking them to install anything they wouldn&rsquo;t still use a week later.</p>

  <div class="case-stats-row">
    <div class="case-stat"><strong>&lt;5%</strong><span>adoption with the native app (v1)</span></div>
    <div class="case-stat"><strong>~13%</strong><span>adoption after the mobile-web pivot (v2)</span></div>
    <div class="case-stat"><strong>≈2.6&times;</strong><span>uplift on the same content base</span></div>
    <div class="case-stat"><strong>0 install</strong><span>required &mdash; just a URL</span></div>
  </div>

  <h2>Version 1 — The native app (2015)</h2>
  <p>Mount Vernon Explorer launched in April 2015 as a free download on the Apple App Store and Google Play, built in partnership with <strong>XCO Software</strong>, a McLean, Virginia firm specializing in apps for museums and cultural institutions. The estate concurrently rolled out <strong>free WiFi across the full 50+ public acres</strong> with Blue Door Networks so the app could actually work on-site.</p>
  <p>For its time, the app was unusually full-featured:</p>
  <ul>
    <li><strong>Location-aware maps</strong> with more than 400 clickable points of interest &mdash; one of the most complete digital references for the estate.</li>
    <li>A searchable <strong>Plant Finder</strong> that filtered Mount Vernon&rsquo;s gardens by season, color, and location (funded by Bartlett Tree Experts).</li>
    <li><strong>Colonial Selfie</strong> &mdash; an early-AR feature that overlaid 18th-century tricorn hats, powdered wigs, and bonnets onto the camera, shareable to social.</li>
    <li>An estate-wide <strong>scavenger hunt</strong>, photo puzzles, and Washington quizzes.</li>
    <li>The day&rsquo;s programming, hours, restaurant info, member benefits.</li>
    <li>An optional <strong>$2.99 audio-tour</strong> upgrade unlocking five themed walks.</li>
  </ul>
  <p>It was thoughtful product work, and on its own merits, it shipped well. The visitors who installed it loved it. But that group was always small &mdash; under 5% of the people on the grounds on any given day. The same problem every cultural institution&rsquo;s native app eventually hits: <strong>asking someone to install an app, sign in to an app store, agree to permissions, and download 80MB of content just so they can use it for the next four hours doesn&rsquo;t survive contact with reality at the front gate</strong>. School groups can&rsquo;t install on chaperone phones, international visitors don&rsquo;t want to risk roaming data, older guests don&rsquo;t want to give an unfamiliar app camera access. The friction was the friction.</p>

  <h2>The pivot &mdash; Version 2: mobile web</h2>
  <p>So we rebuilt the entire visitor companion as a <strong>mobile-web experience</strong>. Same content philosophy, no download, no app store account, no permissions dialog. Visitors scan a QR code or hit a short URL and they&rsquo;re in.</p>
  <p>The migration also let us do something the native app architecture had quietly held back: <strong>syndicate the best interpretive content from mountvernon.org</strong> directly into the visitor companion. The website was the institution&rsquo;s strongest content asset; the mobile experience now drank from the same well.</p>

  <h3>The new feature surface</h3>
  <ul>
    <li><strong>The best of mountvernon.org, mobile-first.</strong> Building biographies, room-by-room interpretation, primary-source images, the curated content that already lived on the institution&rsquo;s flagship site &mdash; surfaced in the visitor companion without duplicating the production pipeline.</li>
    <li><strong>Real-time shuttle tracker.</strong> Mount Vernon runs shuttle buses around the estate and on the drive to the Distillery &amp; Gristmill, several miles down the road. Before the mobile-web pivot, finding the next shuttle was &ldquo;walk to the stop and wait.&rdquo; Now visitors see <strong>where every shuttle is on the property, in real time</strong> &mdash; the bus tracking the same way Uber riders track a car.</li>
    <li><strong>Themed audio tours.</strong> Special-topic walks (the enslaved community at Mount Vernon, the gardens, the Distillery &amp; Gristmill, Revolutionary War history) extended onto the mobile platform &mdash; complementing the on-site <a href="/projects/audio-tour/">Guide ID hardware audio tour</a> rather than replacing it.</li>
    <li><strong>Web video.</strong> Short-form interpretive video &mdash; including content originally produced for the website &mdash; surfaced at the relevant on-grounds locations.</li>
    <li><strong>All the original visitor logistics.</strong> Hours, dining, ticketing, the day&rsquo;s programming, accessibility, member benefits &mdash; carried over from v1.</li>
  </ul>

  <h3>The adoption math</h3>
  <p>Adoption climbed from <strong>under 5% with the native app</strong> to <strong>nearly 13% with the mobile-web version</strong> &mdash; roughly a 2.6&times; uplift, on the same audience and largely the same content. The shift wasn&rsquo;t about better marketing or a more compelling app. It was about <em>removing every step between a visitor and the content they wanted</em>.</p>

  <blockquote>The best app for a one-day visit is the one your visitors don&rsquo;t have to install.</blockquote>

  <h2>What we learned</h2>
  <ul>
    <li><strong>Install friction is the entire ballgame for visitor-companion apps.</strong> A free download is still a download. If the experience can live behind a URL, it should.</li>
    <li><strong>Native is the right answer when usage extends beyond the visit.</strong> Sports apps, banking apps, frequent-flyer apps &mdash; install once, use for years. Visitor-companion apps almost never qualify.</li>
    <li><strong>Content syndication beats content duplication.</strong> Once we let the mobile experience pull from the website&rsquo;s production pipeline directly, we stopped maintaining two parallel content libraries &mdash; and the mobile content got better as the website got better.</li>
    <li><strong>Real-time operational data &mdash; like shuttle tracking &mdash; is high-leverage.</strong> It&rsquo;s the kind of feature visitors actively need <em>during</em> the visit, which is exactly when the mobile experience is open.</li>
  </ul>

  <h2>Why it mattered</h2>
  <p>The Mount Vernon Explorer is one of the rare cultural-institution &ldquo;mobile companion&rdquo; products that&rsquo;s stayed in active use rather than getting shelved after launch. The reason isn&rsquo;t that it was the perfect app on day one &mdash; it wasn&rsquo;t &mdash; but that we treated it as a <em>permanent product line</em>, made the hard call to pivot off native when the data demanded it, and let it inherit the website&rsquo;s content engine and the estate&rsquo;s real-time operational signal. Same visitors, same grounds, same brief &mdash; nearly 3&times; the reach.</p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/magazine/"><span class="dir">&larr; Previous</span><span class="title">Mount Vernon Magazine</span></a>
    <a class="next" href="/projects/agent-711/"><span class="dir">Next &rarr;</span><span class="title">Agent 711: Spy Adventure</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/mv-explorer/index.html",
        title="Mount Vernon Explorer (Native App → Mobile Web) — Matt Briney",
        description="How Mount Vernon's visitor-companion app evolved from a native iOS/Android download with under-5% adoption to a mobile-web experience that reached nearly 13% of visitors — with a real-time shuttle tracker, themed audio tours, web video, and content syndicated from mountvernon.org.",
        active="projects",
        canonical="https://mattbriney.com/projects/mv-explorer/",
        og_image="/img/projects/mv-explorer/phone-01.jpg",
        body=BODY,
    )
