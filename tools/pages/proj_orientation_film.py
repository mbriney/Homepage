TELLY_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l2.9 6.9 7.1.6-5.4 4.7 1.7 7L12 17.8 5.7 21.2l1.7-7L2 9.5l7.1-.6z"/></svg>'

def badge(kind, label):
    return f'<span class="telly telly-{kind}">{TELLY_ICON}{label}</span>'

BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study &middot; Mount Vernon &middot; 2022 &middot; Gold Telly Award</p>
    <h1>The 10-Minute Orientation Film That Replaced 30 Minutes of Friction at the Front Door</h1>
    <p class="lede">When you visit a 180-acre historic site for the first time, the question isn&rsquo;t whether you should watch the orientation film &mdash; it&rsquo;s whether you can afford to. The new Mount Vernon orientation film, produced with <a href="https://wideawakefilms.com/mount-vernon-orientation" target="_blank" rel="noopener">Wide Awake Films</a>, replaced a sprawling 30-minute legacy production with a tight, 10-minute, 4K film designed to do one thing well: give every visitor exactly what they need to make their on-site time count. It won the 2022 Gold Telly Award.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">VP, Media &amp; Communications</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">George Washington&rsquo;s Mount Vernon</span></div>
      <div class="meta-item"><span class="label">Production</span><span class="value">Wide Awake Films · Dir. Shane Seley</span></div>
      <div class="meta-item"><span class="label">Released</span><span class="value">2022</span></div>
      <div class="meta-item"><span class="label">Runtime</span><span class="value">10:30 (was ~30:00)</span></div>
      <div class="meta-item"><span class="label">Recognition</span><span class="value">2022 Gold Telly Award &mdash; General Museums &amp; Galleries (non-broadcast)</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/orientation-film/hero.webp">
        <img src="/img/projects/orientation-film/hero.jpg" alt="Aerial shot of George Washington&rsquo;s Mount Vernon from the orientation film, with the title 'George Washington&rsquo;s Mount Vernon' overlaid above the Mansion, gardens, and Potomac River" width="1600" height="900">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>For years, Mount Vernon&rsquo;s orientation experience was a <strong>30-minute legacy film</strong>: roughly three minutes of actual orientation followed by twenty-seven minutes of loosely organized Washington biography that <em>didn&rsquo;t even cover his presidency</em>. It played in two theaters that ran on rotation, so guests routinely had to wait up to 15 minutes to even get in &mdash; before sitting through the half-hour.</p>
  <p>The result was predictable. School groups, who get 1.5–2.5 hours at the estate, skipped the film entirely. Other guests &mdash; families on a half-day visit, tour groups on a clock, anyone trying to get out to the grounds while the weather held &mdash; either skipped it too, or sat through it and lost a third of their visit to the wrong thing. The "orientation" wasn&rsquo;t orienting anyone.</p>
  <p>The brief: replace it with a single, short film that gives every visitor exactly what they need &mdash; about Washington, about Martha, about the Mount Vernon Ladies&rsquo; Association who saved the place, about the enslaved community whose lives shaped it &mdash; to hand cleanly off to the interpreters waiting on the grounds and in the Mansion.</p>

  <div class="case-stats-row">
    <div class="case-stat"><strong>10:30</strong><span>new runtime (vs. ~30:00 legacy)</span></div>
    <div class="case-stat"><strong>~65%</strong><span>shorter &mdash; with more useful content</span></div>
    <div class="case-stat"><strong>Gold Telly</strong><span>General Museums &amp; Galleries, 2022</span></div>
    <div class="case-stat"><strong>180 acres</strong><span>of estate the film now sets up</span></div>
  </div>

  <h2>Watch the film</h2>
  <div class="film" id="full-film">
    <div class="film-video">
      <iframe src="https://www.youtube-nocookie.com/embed/T30tqyu2j8c" title="George Washington&apos;s Mount Vernon — Orientation Film" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <div class="film-body">
      <div class="film-head">
        <h3 class="film-title">George Washington&rsquo;s Mount Vernon &mdash; Orientation Film</h3>
        <span class="film-meta">2022 &middot; 10:30 &middot; 4K</span>
      </div>
      ''' + badge('gold', 'Gold Telly Award · 2022 · General Museums & Galleries (non-broadcast)') + '''
    </div>
  </div>

  <h2>What the film actually does</h2>
  <p>Where the legacy production tried to be a biography, the new film is an <strong>orientation</strong> in the literal sense &mdash; it orients you to the place, the people, and the day ahead. Its job is to deliver the foundation, then hand off cleanly to the on-grounds interpreters who do the deep dives.</p>
  <ul>
    <li><strong>George and Martha Washington as residents,</strong> not just figures &mdash; framing the Mansion you&rsquo;re about to walk through as a home.</li>
    <li><strong>The estate as a system</strong> &mdash; the Mansion, the gardens, the distillery, the gristmill, the working farm, the museum &amp; education center, and the Library, with quick context on how each one connects to the Washingtons&rsquo; lives.</li>
    <li><strong>The Mount Vernon Ladies&rsquo; Association</strong> &mdash; America&rsquo;s oldest national historic preservation organization, founded in 1853 by Ann Pamela Cunningham, who saved Mount Vernon when the federal government would not.</li>
    <li><strong>The enslaved community at Mount Vernon</strong> &mdash; explicitly recognized, with cues to where on the estate visitors can connect with that history.</li>
    <li><strong>Practical wayfinding</strong> &mdash; a brief, cinematic tour of the 180-acre property so visitors arrive at the front gate already knowing where they want to go.</li>
  </ul>

  <div class="gallery cols-2">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/orientation-film/01.webp"><img src="/img/projects/orientation-film/01.jpg" alt="The Mansion at golden hour from the orientation film"></picture>
      <figcaption class="gallery-caption">4K hero coverage of the Mansion at golden hour &mdash; the film opens with the place itself.</figcaption>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/orientation-film/03.webp"><img src="/img/projects/orientation-film/03.jpg" alt="Aerial view of Mount Vernon, the Potomac River, and the surrounding landscape"></picture>
      <figcaption class="gallery-caption">An aerial pass over the Potomac. The film uses original drone work and cutting-edge 3D animated maps to make the 180 acres legible.</figcaption>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/orientation-film/02.webp"><img src="/img/projects/orientation-film/02.jpg" alt="Period-costumed visitors silhouetted in front of the Mansion under dramatic clouds — depicting the MVLA preservation era"></picture>
      <figcaption class="gallery-caption">A staged 19th-century scene: the Mount Vernon Ladies&rsquo; Association arriving to a Mansion in disrepair. The MVLA story gets its own beat.</figcaption>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/orientation-film/04.webp"><img src="/img/projects/orientation-film/04.jpg" alt="Reenactors portraying the Mount Vernon Ladies' Association meeting at a tea table inside the estate"></picture>
      <figcaption class="gallery-caption">An interior reenactment scene: Ann Pamela Cunningham and the founding generation of the MVLA &mdash; the women who saved the estate.</figcaption>
    </figure>
  </div>

  <h2>Distribution: not just a theater anymore</h2>
  <p>The legacy 30-minute production existed in exactly one place: two on-site theaters that played it on rotation. The new film was designed from the start to live in three different places that all reinforce each other:</p>
  <div class="cards" style="margin-top:1.5rem">
    <div class="card">
      <div class="card-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="1.5"/><path d="M6 19v2M18 19v2"/></svg>
      </div>
      <h3>In the Ford Orientation Center</h3>
      <p class="muted">Plays at the start of the visitor experience, on a tight 10:30 loop. New guests get a complete orientation in the time it used to take to find a seat.</p>
    </div>
    <div class="card">
      <div class="card-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="14" rx="2"/><polygon points="10 8 16 11 10 14" fill="currentColor"/></svg>
      </div>
      <h3>Public on YouTube</h3>
      <p class="muted">Permanently free and embeddable. Anyone considering a visit can watch it before they go &mdash; or in lieu of going, if they live too far away.</p>
    </div>
    <div class="card">
      <div class="card-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
      </div>
      <h3>Pre-Visit Drip &amp; Tour-Operator Use</h3>
      <p class="muted">Embedded in Mount Vernon&rsquo;s pre-visit email sequence and offered to tour operators &mdash; groups can show it on the bus and skip the on-site theater entirely.</p>
    </div>
  </div>

  <h2>What we did</h2>

  <h3>Started with the audience, not the institution</h3>
  <p>Most legacy museum films are built around what the institution wants to say. This one was built around what the visitor needs to know in the first ten minutes of their day. The script was written backwards from the on-grounds interpreter handoff &mdash; what do they assume guests already understand when guests walk up? &mdash; and the runtime was set before a frame was shot.</p>

  <h3>Production at film quality, with the estate as the location</h3>
  <p>Mount Vernon and <a href="https://wideawakefilms.com/mount-vernon-orientation" target="_blank" rel="noopener">Wide Awake Films</a> shot in <strong>4K</strong> across the Mansion, the estate, the gardens, the distillery, and the Library &mdash; working around the estate&rsquo;s operating hours so visitors never saw a film crew. Cutting-edge 3D animated maps were layered over the live footage to make 180 acres feel legible from a single screen.</p>

  <h3>Recognized the enslaved community explicitly</h3>
  <p>The legacy film handled slavery glancingly, if at all. The new film names it as part of the institution&rsquo;s story and explicitly directs visitors to where, on the estate, they can engage with that history &mdash; a deliberate, curatorial choice that matched Mount Vernon&rsquo;s broader institutional priorities.</p>

  <h3>Made it ship beyond the theater</h3>
  <p>The film&rsquo;s public release on YouTube and its use in pre-visit email and by tour operators were planned from day one, not retrofitted afterward. Treating an orientation film as a piece of <em>distributable content</em> &mdash; not a building fixture &mdash; was the strategic shift that made the production worth doing at all.</p>

  <blockquote>Our goal for this new film was to provide our guests with the highest quality experience when visiting George Washington&rsquo;s Mount Vernon. This prestigious award signals that we succeeded. This innovative film provides our guests with a brief but in-depth overview of how to navigate the 180-acre property and its rich history so visitors can fully experience all that Mount Vernon has to offer.
    <span style="display:block;margin-top:.7rem;font-style:normal;font-size:.9rem;color:var(--ink-muted)">— Douglas Bradburn, President and CEO, George Washington&rsquo;s Mount Vernon (2022 Telly Award announcement)</span>
  </blockquote>

  <h2>Why it mattered</h2>
  <blockquote>The best institutional film isn&rsquo;t the longest one. It&rsquo;s the one that leaves the most time for the actual visit.</blockquote>
  <p>The orientation film replaced a thirty-minute friction point at the front door with a ten-minute experience that actually does what its name says. School groups stopped skipping it because they finally had time for it. Tour operators stopped working around it because they could now use it. Online viewers became pre-qualified visitors, arriving on-site already knowing what they wanted to see. And the Gold Telly was the working proof that institutional orientation, done with the same craft you&rsquo;d give a feature production, is a discipline worth taking seriously.</p>

  <p class="muted" style="margin-top:2rem;font-size:.9rem;">Press: <a href="https://www.mountvernon.org/about/news/article/george-washington-s-mount-vernon-wins-prestigious-telly-award-for-innovative-guest-orientation-film" target="_blank" rel="noopener">Mount Vernon — Gold Telly press release</a> · <a href="https://wideawakefilms.com/mount-vernon-orientation" target="_blank" rel="noopener">Wide Awake Films &mdash; Orientation Film</a></p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/washingtons-war-4d/"><span class="dir">&larr; Previous</span><span class="title">Revolutionary War 4D Theater</span></a>
    <a class="next" href="/projects/ar-tour/"><span class="dir">Next &rarr;</span><span class="title">Mount Vernon in AR</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/orientation-film/index.html",
        title="Mount Vernon Orientation Film (Gold Telly, 2022) — Matt Briney",
        description="The 10:30 orientation film that replaced Mount Vernon's 30-minute legacy production. Produced with Wide Awake Films, distributed on-site + YouTube + pre-visit drip + tour-operator licensing. Winner, 2022 Gold Telly Award for General Museums & Galleries.",
        active="projects",
        canonical="https://mattbriney.com/projects/orientation-film/",
        og_image="/img/projects/orientation-film/hero.jpg",
        body=BODY,
    )
