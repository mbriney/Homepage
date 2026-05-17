BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Mount Vernon · 2017–2018 · Thea Award</p>
    <h1><em>Be Washington</em>: It&rsquo;s Your Turn to Lead</h1>
    <p class="lede">A $3.5M, 36-seat permanent interactive theater that drops visitors into Washington&rsquo;s shoes, hands them real historical inputs, and asks what they&rsquo;d do. Winner of the Thea Outstanding Achievement Award.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Director, end-to-end creation</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">George Washington&rsquo;s Mount Vernon</span></div>
      <div class="meta-item"><span class="label">Capital</span><span class="value">$3.5M</span></div>
      <div class="meta-item"><span class="label">Award</span><span class="value">Thea Outstanding Achievement (2018)</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/be-washington/hero.webp">
        <img src="/img/projects/be-washington/hero.jpg" alt="Be Washington — splash with Washington crossing the Delaware" width="1600" height="1030">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Build a permanent interpretive experience that does something most museum theaters can&rsquo;t: actually puts visitors in the seat. Not a lecture, not a film &mdash; a chamber where you weigh real historical inputs, hear advisors argue, and make Washington&rsquo;s decisions in his moment.</p>

  <h2>The experience</h2>
  <p>You sit in a 36-seat theater. A scenario unfolds: Will you accept a third term? How do you handle the Whiskey Rebellion? What do you do about the Jay Treaty? On-screen advisors, played by recognizable actors, argue every side in your ear. The room votes. The theater reveals the consensus &mdash; and what Washington actually did.</p>

  <div class="gallery cols-2">
    <figure><picture><source type="image/webp" srcset="/img/projects/be-washington/01.webp"><img src="/img/projects/be-washington/01.jpg" alt="Be Washington scenario screen"></picture></figure>
    <figure><picture><source type="image/webp" srcset="/img/projects/be-washington/02.webp"><img src="/img/projects/be-washington/02.jpg" alt="Be Washington scenario screen"></picture></figure>
    <figure><picture><source type="image/webp" srcset="/img/projects/be-washington/03.webp"><img src="/img/projects/be-washington/03.jpg" alt="Be Washington scenario screen"></picture></figure>
    <figure><picture><source type="image/webp" srcset="/img/projects/be-washington/04.webp"><img src="/img/projects/be-washington/04.jpg" alt="Be Washington scenario screen"></picture></figure>
  </div>

  <h2>What we did</h2>
  <ul>
    <li>Directed end-to-end creation of the $3.5M capital project &mdash; narrative, scripts, advisor recruitment, casting, set design, AV stack, and software.</li>
    <li>Anchored each scenario in primary-source research, with advisors&rsquo; arguments drawn from documented positions of the period.</li>
    <li>Built the real-time voting and reveal architecture and the post-show debrief that connects visitor decisions back to the historical record.</li>
    <li>Shipped a companion online platform so the experience could travel into classrooms nationally and extend the impact well beyond the 36 seats.</li>
  </ul>

  <div class="case-stats-row">
    <div class="case-stat"><strong>Thea</strong><span>Outstanding Achievement (2018)</span></div>
    <div class="case-stat"><strong>36-seat</strong><span>permanent installation</span></div>
    <div class="case-stat"><strong>$3.5M</strong><span>capital project</span></div>
    <div class="case-stat"><strong>Classrooms</strong><span>online companion nationwide</span></div>
  </div>

  <h2>Why it mattered</h2>
  <p>The Thea is the entertainment industry&rsquo;s top recognition for immersive experiences, typically awarded to major theme-park attractions. <em>Be Washington</em> winning one was a working argument that civic and historical content, given enough craft and risk, can compete with anything in the immersive-entertainment world &mdash; and a model for what permanent interpretive media at a historic site can aspire to.</p>

  <div class="gallery cols-2">
    <figure><picture><source type="image/webp" srcset="/img/projects/be-washington/05.webp"><img src="/img/projects/be-washington/05.jpg" alt="Be Washington app and website"></picture></figure>
  </div>

  <p style="margin-top:2.5rem">
    <a class="btn btn-primary" href="https://www.mountvernon.org/plan-your-visit/things-to-do/be-washington" target="_blank" rel="noopener">More about <em>Be Washington</em> &rarr;</a>
  </p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/mount-vernon-virtual-tour/"><span class="dir">&larr; Previous</span><span class="title">Mount Vernon Virtual Tour</span></a>
    <a class="next" href="/projects/short-films/"><span class="dir">Next &rarr;</span><span class="title">Short Film Series</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/be-washington/index.html",
        title="Be Washington Interactive Theater — Matt Briney",
        description="A $3.5M, 36-seat first-person interactive theater at Mount Vernon that won the 2018 Thea Outstanding Achievement Award. Visitors weigh real historical inputs and make Washington's decisions in his moment.",
        active="projects",
        canonical="https://mattbriney.com/projects/be-washington/",
        og_image="/img/projects/be-washington/hero.jpg",
        body=BODY,
    )
