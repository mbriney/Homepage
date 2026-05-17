BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Mount Vernon · 2018–2024</p>
    <h1>An Immersive Virtual Mount Vernon, Used in Classrooms Nationwide</h1>
    <p class="lede">A custom-built virtual tour built on HDR photography, layered stories, and curatorial commentary. Reached 4M+ visitors with an 18-minute average dwell time &mdash; museum-grade engagement for a website experience.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Executive Producer</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">George Washington&rsquo;s Mount Vernon</span></div>
      <div class="meta-item"><span class="label">Audience</span><span class="value">Classrooms nationwide</span></div>
      <div class="meta-item"><span class="label">Format</span><span class="value">Web-native interactive</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/mv-virtual-tour/hero.webp">
        <img src="/img/projects/mv-virtual-tour/hero.jpg" alt="Mount Vernon Virtual Tour — the Mansion view with interactive hotspots" width="1600" height="1040">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Build an online estate that lets anyone &mdash; student, teacher, researcher, or armchair traveler &mdash; walk Mount Vernon&rsquo;s grounds, peek into the rooms, and follow Washington&rsquo;s stories without ever leaving home. Make it good enough that a school district could use it instead of a field trip when the field trip wasn&rsquo;t possible.</p>

  <div class="case-stats-row">
    <div class="case-stat"><strong>4M+</strong><span>visitors</span></div>
    <div class="case-stat"><strong>18m</strong><span>average dwell time</span></div>
    <div class="case-stat"><strong>5</strong><span>languages supported</span></div>
    <div class="case-stat"><strong>100s</strong><span>of interpretive hotspots</span></div>
  </div>

  <h2>What we did</h2>

  <h3>HDR photography of the estate</h3>
  <p>We shot every major site &mdash; the Mansion, the outbuildings, the gardens, the distillery, the gristmill, the library &mdash; in vivid HDR panoramic photography, capturing the place under the kind of light most visitors never get to see it in.</p>

  <h3>Stories layered on the photography</h3>
  <p>Each hotspot is a doorway: into a video, a primary-source document, a piece of curatorial commentary, a Washington letter, or a deeper room you can step inside. The interaction loop kept people exploring for an average of <strong>18 minutes per session</strong> &mdash; a number that puts it in the top tier of any cultural-institution digital experience anywhere.</p>

  <div class="gallery cols-2">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/mv-virtual-tour/01.webp"><img src="/img/projects/mv-virtual-tour/01.jpg" alt="Virtual tour interior view"></picture>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/mv-virtual-tour/02.webp"><img src="/img/projects/mv-virtual-tour/02.jpg" alt="Virtual tour grounds view"></picture>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/mv-virtual-tour/03.webp"><img src="/img/projects/mv-virtual-tour/03.jpg" alt="Virtual tour interpretive view"></picture>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/mv-virtual-tour/hero.webp"><img src="/img/projects/mv-virtual-tour/hero.jpg" alt="Virtual tour mansion view with hotspots"></picture>
    </figure>
  </div>

  <h3>Built for classrooms</h3>
  <p>The tour was designed with teachers in mind from day one: clean navigation, accessible language toggling across five languages, and an interpretive depth that supports a real lesson plan. It became a fixture in social studies curricula nationwide and a quiet workhorse for schools that couldn&rsquo;t bring kids to Virginia.</p>

  <h2>Why it mattered</h2>
  <blockquote>An 18-minute dwell time on a website is museum-grade engagement &mdash; proof that depth and craft online can rival the visit itself.</blockquote>
  <p>For a sector that often treats digital as a brochure, the virtual tour was a working argument for what a great cultural-institution digital product can be &mdash; not a marketing asset, but a destination in its own right.</p>

  <p style="margin-top:2.5rem">
    <a class="btn btn-primary" href="https://virtualtour.mountvernon.org/" target="_blank" rel="noopener">Take the tour &rarr;</a>
  </p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/mount-vernon-website/"><span class="dir">&larr; Previous</span><span class="title">Mount Vernon Website</span></a>
    <a class="next" href="/projects/be-washington/"><span class="dir">Next &rarr;</span><span class="title"><em>Be Washington</em></span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/mount-vernon-virtual-tour/index.html",
        title="Mount Vernon Virtual Tour — Matt Briney",
        description="An immersive web-based virtual tour of George Washington's Mount Vernon with HDR photography, layered storytelling, and 5-language support. Reached 4M+ visitors at an 18-minute dwell.",
        active="projects",
        canonical="https://mattbriney.com/projects/mount-vernon-virtual-tour/",
        og_image="/img/projects/mv-virtual-tour/hero.jpg",
        body=BODY,
    )
