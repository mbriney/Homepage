BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Mount Vernon · iOS &amp; Android</p>
    <h1>Mount Vernon Explorer: The Estate in Your Pocket</h1>
    <p class="lede">A mobile app that gives every visitor a curated audio tour, on-grounds wayfinding, and the logistics of their visit &mdash; without needing a paper map or a hands-on guide.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Producer &amp; Product Owner</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">George Washington&rsquo;s Mount Vernon</span></div>
      <div class="meta-item"><span class="label">Platforms</span><span class="value">iOS &amp; Android</span></div>
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
  <p>A Mount Vernon visit is a multi-hour outdoor exploration spread across 500&nbsp;acres of grounds, half a dozen historic buildings, gardens, the distillery, the wharf, and the working farm. Most visitors arrive with a paper map and a lot of curiosity. The challenge: put a thoughtful, interpretive companion in everyone&rsquo;s pocket &mdash; one that respects their pace, their interests, and the experience of being on-site.</p>

  <h2>What it does</h2>
  <ul>
    <li>A complete, professionally narrated audio tour covering 75+ stops on the estate.</li>
    <li>On-grounds wayfinding using the estate&rsquo;s mapped paths and points of interest.</li>
    <li>Detailed information for each stop &mdash; stories, primary-source images, and curatorial context.</li>
    <li>Visit logistics: hours, ticketing, dining, the day&rsquo;s programming, members&rsquo; benefits.</li>
    <li>Designed to work offline once content is downloaded, so spotty cellular at the bottom of the hill doesn&rsquo;t break the visit.</li>
  </ul>

  <h2>Why it mattered</h2>
  <p>Mobile audio tours had been around for years, but most cultural institutions were renting clunky third-party devices at the door or pushing visitors into generic apps. Owning the app meant owning the interpretation, the data, and the relationship &mdash; the same visitors who used the app on-site became the easiest audience to bring back online, into the email list, and into membership.</p>

  <p>It&rsquo;s also one of the rare cultural-institution apps that&rsquo;s stayed in active use rather than getting shelved after launch &mdash; a function of treating it as a permanent product line rather than a one-off project.</p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/short-films/"><span class="dir">&larr; Previous</span><span class="title">Short Film Series</span></a>
    <a class="next" href="/projects/trpl-reading-room/"><span class="dir">Next &rarr;</span><span class="title">TRPL Reading Room</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/mv-explorer/index.html",
        title="Mount Vernon Explorer App — Matt Briney",
        description="Mount Vernon's iOS and Android visitor app — a professionally narrated audio tour, wayfinding, and on-grounds logistics in every visitor's pocket.",
        active="projects",
        canonical="https://mattbriney.com/projects/mv-explorer/",
        og_image="/img/projects/mv-explorer/phone-01.jpg",
        body=BODY,
    )
