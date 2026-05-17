# Helper: shared "no Telly" / Telly badge SVG (a small star)
TELLY_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l2.9 6.9 7.1.6-5.4 4.7 1.7 7L12 17.8 5.7 21.2l1.7-7L2 9.5l7.1-.6z"/></svg>'

def badge(kind, label):
    return f'<span class="telly telly-{kind}">{TELLY_ICON}{label}</span>'

# --- Page body ---
BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study &middot; Mount Vernon &middot; 2015–2023</p>
    <h1>The Mount Vernon Short Film Series: Animated History for the General Public and the Classroom</h1>
    <p class="lede">A four-film series produced with <a href="https://wideawakefilms.com/" target="_blank" rel="noopener">Wide Awake Films</a> that brings George Washington&rsquo;s war, the Constitution, and the foundations of American religious freedom to a broad audience &mdash; three Telly Awards, distribution across major streaming platforms, and free classroom-ready lesson plans.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Executive Producer</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">George Washington&rsquo;s Mount Vernon</span></div>
      <div class="meta-item"><span class="label">Production</span><span class="value">Wide Awake Films</span></div>
      <div class="meta-item"><span class="label">Years</span><span class="value">2015 — 2023</span></div>
    </div>

    <div class="case-stats-row" style="margin-top:2rem">
      <div class="case-stat"><strong>3</strong><span>Telly Awards (Silver, Silver, Bronze)</span></div>
      <div class="case-stat"><strong>4</strong><span>short films</span></div>
      <div class="case-stat"><strong>~90m</strong><span>combined runtime</span></div>
      <div class="case-stat"><strong>4</strong><span>streaming platforms</span></div>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Most Americans encounter Washington as a portrait on a wall and an outline in a textbook. The Mount Vernon short-film series was designed to do something different: give a general audience &mdash; and the millions of students in their classrooms &mdash; a cinematic, animated, primary-source-anchored way to actually see the moments that mattered. Each film is 15–25 minutes &mdash; short enough for a class period, deep enough for a curriculum unit, and good enough that families watch them at home on Apple TV.</p>

  <h2>The films</h2>

  <!-- ============================================================ -->
  <!-- Now or Never -->
  <!-- ============================================================ -->
  <div class="film" id="now-or-never">
    <div class="film-video">
      <iframe src="https://www.youtube-nocookie.com/embed/7tXmpIp6_7c" title="Now or Never: Yorktown Campaign of 1781" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <div class="film-body">
      <div class="film-head">
        <h3 class="film-title">Now or Never: Yorktown Campaign of 1781</h3>
        <span class="film-meta">2015 &middot; 23 min</span>
      </div>
      <p class="film-tagline">The Franco-American alliance, the siege of Yorktown, and the moment America&rsquo;s independence was finally won.</p>
      ''' + badge('silver', 'Silver Telly Award · 2015 · Cinematography, General Education') + '''
      <p style="margin-top:1rem">George Washington&rsquo;s Continental Army has fought for five long years to drive the British from American soil. Now, with the aid of French land and naval forces, Washington and his allies have surrounded the British at Yorktown, Virginia &mdash; and the dream of American independence hangs in the balance.</p>
      <p class="film-links">
        <a href="https://www.mountvernon.org/education/videos/films/now-or-never-yorktown" target="_blank" rel="noopener">Classroom resources &amp; lesson plans &rarr;</a>
        <a href="https://www.youtube.com/watch?v=7tXmpIp6_7c" target="_blank" rel="noopener">Watch on YouTube &rarr;</a>
      </p>
    </div>
  </div>

  <!-- ============================================================ -->
  <!-- The Winter Patriots -->
  <!-- ============================================================ -->
  <div class="film" id="winter-patriots">
    <div class="film-video">
      <iframe src="https://www.youtube-nocookie.com/embed/CbGodj0lJ2Q" title="The Winter Patriots: A Revolutionary War Tale" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <div class="film-body">
      <div class="film-head">
        <h3 class="film-title">The Winter Patriots: A Revolutionary War Tale</h3>
        <span class="film-meta">2015 &middot; 25 min</span>
      </div>
      <p class="film-tagline">Crossing the Delaware, Trenton, and Princeton &mdash; how the cause of independence survived its darkest winter.</p>
      <p style="margin-top:.75rem">Following one of the darkest moments of the American Revolution, the Continental Army &mdash; under Washington&rsquo;s command &mdash; saved the cause of independence through a brilliant late-1776/early-1777 campaign. The film covers the Declaration of Independence, Washington&rsquo;s strategies, and Washington&rsquo;s early-war decision to mandate smallpox inoculation across the army.</p>
      <p class="film-links">
        <a href="https://www.mountvernon.org/education/videos/films/the-winter-patriots" target="_blank" rel="noopener">Classroom resources &amp; lesson plans &rarr;</a>
        <a href="https://www.youtube.com/watch?v=CbGodj0lJ2Q" target="_blank" rel="noopener">Watch on YouTube &rarr;</a>
      </p>
    </div>
  </div>

  <!-- ============================================================ -->
  <!-- A More Perfect Union -->
  <!-- ============================================================ -->
  <div class="film" id="more-perfect-union">
    <div class="film-video">
      <iframe src="https://www.youtube-nocookie.com/embed/k55VdRD8DDo" title="A More Perfect Union: George Washington and the Making of the Constitution" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <div class="film-body">
      <div class="film-head">
        <h3 class="film-title">A More Perfect Union: George Washington and the Making of the Constitution</h3>
        <span class="film-meta">2017 &middot; 25 min</span>
      </div>
      <p class="film-tagline">Why this revolution didn&rsquo;t end in chaos &mdash; the 1787 Constitutional Convention, the compromises, and the document that has held for 200+ years.</p>
      ''' + badge('bronze', 'Bronze Telly Award · 2017 · Cinematography, General Education') + '''
      <p style="margin-top:1rem">Most popular revolutions in history descend into bloody chaos or fall under the sway of dictators. So how did the United States, born of its own eight-year revolution, ultimately avoid these common pitfalls? <em>A More Perfect Union</em> explores the challenges facing the new nation and how the founders, led by George Washington, created &mdash; through compromise &mdash; the United States Constitution.</p>
      <p class="film-links">
        <a href="https://www.mountvernon.org/education/videos/films/constitution" target="_blank" rel="noopener">Classroom resources &amp; lesson plans &rarr;</a>
        <a href="https://www.youtube.com/watch?v=k55VdRD8DDo" target="_blank" rel="noopener">Watch on YouTube &rarr;</a>
      </p>
    </div>
  </div>

  <!-- ============================================================ -->
  <!-- Religious Freedom -->
  <!-- ============================================================ -->
  <div class="film" id="religious-freedom">
    <div class="film-video">
      <iframe src="https://www.youtube-nocookie.com/embed/sFrndBWECI8" title="George Washington and the Pursuit of Religious Freedom" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <div class="film-body">
      <div class="film-head">
        <h3 class="film-title">George Washington and the Pursuit of Religious Freedom</h3>
        <span class="film-meta">2023 &middot; 15 min</span>
      </div>
      <p class="film-tagline">From the defeat of the British Empire to the Bill of Rights, by way of Washington&rsquo;s precedent-setting letter to the Touro Synagogue.</p>
      ''' + badge('silver', 'Silver Telly Award · 2023 · Non-Broadcast, History') + '''
      <p style="margin-top:1rem">The film covers religion in early America, the founding-era debates over its place in public life, and the steps from the Revolution to the passing of the Bill of Rights in 1791. Anchoring it: Washington&rsquo;s 1790 letter to the Hebrew Congregation at Newport &mdash; one of the clearest founding-era statements of what religious freedom would mean in the new republic.</p>
      <p class="film-links">
        <a href="https://www.mountvernon.org/education/videos/films/religious-freedom-classroom-resources" target="_blank" rel="noopener">Classroom resources &amp; lesson plans &rarr;</a>
        <a href="https://www.youtube.com/watch?v=sFrndBWECI8" target="_blank" rel="noopener">Watch on YouTube &rarr;</a>
      </p>
    </div>
  </div>

  <!-- ============================================================ -->
  <h2>Built for the classroom</h2>
  <p>Each film has a dedicated educator hub on Mount Vernon&rsquo;s site &mdash; grab-and-go lesson plans scaffolded for Elementary, Middle, and High School classrooms, primary-source documents that pair to each scene, discussion questions, and chaptered versions of the film for use in a single class period. All of it is free.</p>
  <p>The films and the lesson plans are designed together: the curriculum drives the script, the script drives the visuals, and the visuals come back into the classroom as the anchor for the lesson. The result is an interpretive package that holds up whether a student sees it on a school SmartBoard, a parent puts it on Apple TV on a Sunday afternoon, or a researcher cites it in a paper.</p>

  <h2>Distribution</h2>
  <p>The films are available far beyond Mount Vernon&rsquo;s own site &mdash; on the streaming services where audiences already are, plus DVD for the educators and gift-shop buyers who still want one.</p>
  <ul class="platforms" aria-label="Streaming platforms">
    <li>Amazon Prime Video</li>
    <li>Apple TV &amp; iTunes</li>
    <li>Google Play</li>
    <li>Curiosity Stream</li>
    <li>YouTube (free, full-length)</li>
    <li>Mount Vernon DVD</li>
  </ul>

  <h2>Why it mattered</h2>
  <blockquote>A 25-minute animated short film, watched by a class of seventh-graders, is one of the most efficient interpretive products a cultural institution can ship.</blockquote>
  <p>The series gave Mount Vernon a content asset with an unusually long tail. Each film, once shipped, kept earning attention &mdash; in classrooms via the lesson plans, on streaming services via the distribution deals, on YouTube via free access, and at the estate itself via theater screenings. It&rsquo;s the kind of work that turns a single capital investment into years of audience reach and brand authority. Three Tellys later &mdash; including a 2018 Gold for the companion 4D theater film <em>Washington&rsquo;s War</em>, also part of this production partnership &mdash; the series stands as one of the most-recognized historic-site film programs of its era.</p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/be-washington/"><span class="dir">&larr; Previous</span><span class="title"><em>Be Washington</em></span></a>
    <a class="next" href="/projects/mv-explorer/"><span class="dir">Next &rarr;</span><span class="title">Mount Vernon Explorer App</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/short-films/index.html",
        title="Mount Vernon Short Film Series — Matt Briney",
        description="Mount Vernon's four-film animated history series with Wide Awake Films — three Telly Awards, streaming distribution on Amazon Prime/Apple TV/Google Play/Curiosity Stream, and free classroom lesson plans.",
        active="projects",
        canonical="https://mattbriney.com/projects/short-films/",
        og_image="/img/matt-og-1200x630.jpg",
        body=BODY,
    )
