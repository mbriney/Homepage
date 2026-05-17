TELLY_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l2.9 6.9 7.1.6-5.4 4.7 1.7 7L12 17.8 5.7 21.2l1.7-7L2 9.5l7.1-.6z"/></svg>'

def badge(kind, label):
    return f'<span class="telly telly-{kind}">{TELLY_ICON}{label}</span>'

BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study &middot; Mount Vernon &middot; 2018 &middot; Three Telly Awards</p>
    <h1>The Theater Where It Snows: A $3.5M Overhaul of Mount Vernon&rsquo;s Revolutionary War 4D Theater</h1>
    <p class="lede">Mount Vernon&rsquo;s second-most-visited attraction got a full reinvention &mdash; a brand-new 22-minute 4K original film (<em>Washington&rsquo;s War</em>), a curved 32 &times; 16-foot screen, a 9.2-channel surround system, upgraded seat rumblers, new snow and fog, and strobes and gobos that turn film into weather. It won a 2018 Gold Telly and a pair of Bronzes.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Executive Producer</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">George Washington&rsquo;s Mount Vernon</span></div>
      <div class="meta-item"><span class="label">Film production</span><span class="value">Wide Awake Films</span></div>
      <div class="meta-item"><span class="label">Theater integration</span><span class="value">Solomon Group · Gallagher &amp; Associates</span></div>
      <div class="meta-item"><span class="label">Year</span><span class="value">2018</span></div>
      <div class="meta-item"><span class="label">Sponsor</span><span class="value">Robert H. Smith Family Foundation</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/washingtons-war-4d/hero.webp">
        <img src="/img/projects/washingtons-war-4d/hero.jpg" alt="The Revolutionary War 4D Theater interior — curved screen lit by a Delaware-crossing scene, with snow falling on the audience" width="1600" height="1066">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>For more than a decade, the Revolutionary War Theater was Mount Vernon&rsquo;s second most-visited attraction &mdash; the place every visitor heard about before they arrived as &ldquo;the theater where it snows.&rdquo; By 2017, the original film and the original AV stack were both showing their age. The job: design a top-to-bottom reinvention &mdash; new film, new screen, new audio, new seat effects, new weather &mdash; without losing the moment that everyone remembered.</p>

  <div class="case-stats-row">
    <div class="case-stat"><strong>$3.5M</strong><span>capital investment</span></div>
    <div class="case-stat"><strong>3</strong><span>Telly Awards (Gold + 2× Bronze)</span></div>
    <div class="case-stat"><strong>200+</strong><span>actors &amp; reenactors</span></div>
    <div class="case-stat"><strong>2 years</strong><span>in production</span></div>
  </div>

  <h2><em>Washington&rsquo;s War</em>: a new original film, two years in the making</h2>
  <p>The heart of the overhaul is a brand-new 22-minute 4K original, produced with <a href="https://wideawakefilms.com/washingtons-war" target="_blank" rel="noopener">Wide Awake Films</a>. It follows General Washington through the three campaigns that won the Revolution &mdash; Boston, Trenton, and Yorktown &mdash; combining live-action reenactment, 3D animated tactical maps, a sweeping score, and the kind of booming sound the room can carry.</p>

  <div class="film" id="full-film">
    <div class="film-video">
      <iframe src="https://www.youtube-nocookie.com/embed/cFvx8n_9s9M" title="Washington&apos;s War: General George Washington and the Revolutionary War (full film)" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <div class="film-body">
      <div class="film-head">
        <h3 class="film-title"><em>Washington&rsquo;s War</em> &mdash; full 22-minute film</h3>
        <span class="film-meta">2018 &middot; 22 min &middot; 4K</span>
      </div>
      ''' + badge('gold',   'Gold Telly Award · 2018 · Non-Broadcast, General Education') + ' ' \
          + badge('bronze', 'Bronze Telly · 3D Graphics / Animation') + ' ' \
          + badge('bronze', 'Bronze Telly · Cinematography') + '''
    </div>
  </div>

  <h3>Production at scale</h3>
  <p>The shoot was a year-plus production effort:</p>
  <ul>
    <li>A cast of <strong>200+ actors and historical reenactors</strong>.</li>
    <li>A 40-person crew on the ground.</li>
    <li>A battery of 18th-century artillery &mdash; reportedly <strong>the most cannons on set since the production of <em>Last of the Mohicans</em></strong>.</li>
    <li>Filming across Virginia: Fuqua Farms (Richmond), Gadsby&rsquo;s Tavern (Alexandria), Wellbourne House (Middleburg), Goose Creek Bridge, and Mount Vernon itself.</li>
  </ul>

  <div class="gallery cols-2">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/washingtons-war-4d/02.webp"><img src="/img/projects/washingtons-war-4d/02.jpg" alt="Cannon being fired at dusk during production"></picture>
      <figcaption class="gallery-caption">A reenactment cannon firing on set &mdash; the kind of live-action plate that becomes a 4D moment in the theater.</figcaption>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/washingtons-war-4d/03.webp"><img src="/img/projects/washingtons-war-4d/03.jpg" alt="Artillery crew of reenactors with cannon smoke"></picture>
      <figcaption class="gallery-caption">An artillery crew between takes. The film leaned hard on real reenactor expertise.</figcaption>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/washingtons-war-4d/04.webp"><img src="/img/projects/washingtons-war-4d/04.jpg" alt="Camera operator on location with British reenactors in red coats"></picture>
      <figcaption class="gallery-caption">Behind the scenes &mdash; the Wide Awake Films camera team shooting British infantry on location.</figcaption>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/washingtons-war-4d/05.webp"><img src="/img/projects/washingtons-war-4d/05.jpg" alt="Film still from Washington&apos;s War showing reenactors in the field"></picture>
      <figcaption class="gallery-caption">A frame from the finished film. Live-action plates intercut with 3D-animated tactical maps.</figcaption>
    </figure>
  </div>

  <h2>The theater: a full sensory rebuild</h2>
  <p>The theater itself was rebuilt around the new film. <a href="https://solomongroup.com/projects/george-washingtons-mt-vernon" target="_blank" rel="noopener">Solomon Group</a> led AV integration, scenic fabrication, lighting, and show control, partnered with <strong>Gallagher &amp; Associates</strong> on experience design.</p>

  <ul>
    <li><strong>Image.</strong> A new <strong>curved projection screen, ~32 ft &times; 16 ft</strong>, driven by a <strong>Christie Boxer 4K</strong> projector. The curve and the cleaner edges make the cannon fire feel like it&rsquo;s coming at you.</li>
    <li><strong>Sound.</strong> Upgraded to a <strong>9.2-channel surround system</strong>, with cannon shots and musket volleys placed around the room rather than just in front of it.</li>
    <li><strong>Seats.</strong> All-new <strong>seat rumblers</strong> tuned to the score and the artillery hits.</li>
    <li><strong>Weather.</strong> A new <strong>snow and fog system</strong> &mdash; the moment everyone remembers &mdash; restaged with finer particle, better coverage, and tighter sync to the show.</li>
    <li><strong>Lighting.</strong> New theatrical lighting fixtures with <strong>strobes and gobos</strong> that transform the room itself into part of the scene &mdash; a muzzle flash on stage becomes a strobe in the audience.</li>
    <li><strong>Show control.</strong> A Medialon-based show control system synchronizes media, audio, seats, snow, fog, and lighting into a single 22-minute composition.</li>
  </ul>

  <div class="gallery cols-2">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/washingtons-war-4d/01.webp"><img src="/img/projects/washingtons-war-4d/01.jpg" alt="Panoramic view of the Revolutionary War 4D Theater interior with snow falling"></picture>
      <figcaption class="gallery-caption">The theater mid-show: snow falling on the audience, lighting bleed off the screen, and a curved 32 &times; 16-foot image driving the room.</figcaption>
    </figure>
  </div>

  <h2>Recognition</h2>
  <p>The film and the theater together earned the project three Telly Awards in 2018:</p>
  <p>
    ''' + badge('gold',   'Gold Telly · Non-Broadcast, General Education') + '<br><br>' \
        + badge('bronze', 'Bronze Telly · 3D-Graphics / Animation, General Education') + '<br><br>' \
        + badge('bronze', 'Bronze Telly · Cinematography, General Education') + '''
  </p>

  <h2>The trailer</h2>
  <p>A short version cut for ticketing and marketing pages:</p>
  <div class="film" id="trailer">
    <div class="film-video">
      <iframe src="https://www.youtube-nocookie.com/embed/oCoZ3ds34Nc" title="Washington&apos;s War 4D Theater preview trailer" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <div class="film-body">
      <div class="film-head">
        <h3 class="film-title">Theater preview trailer</h3>
        <span class="film-meta">90 sec</span>
      </div>
    </div>
  </div>

  <h2>Why it mattered</h2>
  <blockquote>Snow falling on an audience as Washington crosses the Delaware is a five-second moment that families remember for years. Earning that moment back, at a higher resolution &mdash; with a better story under it &mdash; was the whole job.</blockquote>
  <p>The Revolutionary War Theater is the kind of attraction that defines how a generation of visitors remembers Mount Vernon. Doing it right meant taking it apart entirely &mdash; new film, new room, new effects &mdash; while keeping the few specific things that made it special in the first place. The fact that the new version went on to a Gold Telly and pulled <a href="/projects/short-films/"><em>Washington&rsquo;s War</em> into the broader film series</a> meant the capital investment paid off in two directions: a better on-site experience for paying visitors, and an award-winning original asset Mount Vernon could distribute on Amazon Prime, Apple TV, Google Play, and Curiosity Stream for years afterward.</p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/be-washington/"><span class="dir">&larr; Previous</span><span class="title"><em>Be Washington</em></span></a>
    <a class="next" href="/projects/ar-tour/"><span class="dir">Next &rarr;</span><span class="title">Mount Vernon in AR</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/washingtons-war-4d/index.html",
        title="Revolutionary War 4D Theater Overhaul — Matt Briney",
        description="A $3.5M reinvention of Mount Vernon's second-most-visited attraction — a new 22-minute 4K original film 'Washington's War' with Wide Awake Films, a 32×16-foot curved screen, 9.2 surround, new seat shakers, snow/fog/strobes/gobos, and three 2018 Telly Awards.",
        active="projects",
        canonical="https://mattbriney.com/projects/washingtons-war-4d/",
        og_image="/img/projects/washingtons-war-4d/hero.jpg",
        body=BODY,
    )
