BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Theodore Roosevelt Presidential Library · 2026</p>
    <h1>The Trailblazer: A Wearable That Remembers Your Visit</h1>
    <p class="lede">Most museum interactives end the moment you walk away from them. The Trailblazer is an RFID wearable designed around the opposite premise &mdash; that the most valuable thing a visit produces is what the visitor still has that evening, sitting at home, three states away.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Chief Communications &amp; Marketing Officer</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">Theodore Roosevelt Presidential Library</span></div>
      <div class="meta-item"><span class="label">Year</span><span class="value">2026</span></div>
      <div class="meta-item"><span class="label">Type</span><span class="value">RFID wearable · permanent exhibition</span></div>
      <div class="meta-item"><span class="label">Status</span><span class="value">Live since opening</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/trpl-trailblazer/hero.webp">
        <img src="/img/projects/trpl-trailblazer/hero.jpg" alt="Still from the Trailblazer spot — “Your Journey Starts Here”" width="1600" height="900">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>A visitor to the Theodore Roosevelt Presidential Library has typically travelled a long way, spent about four and a half hours on site, and will probably not return within the year. The traditional museum answer to that is a gift shop.</p>
  <p>The better answer is to send them home with the visit itself &mdash; and to make the institution&rsquo;s next conversation with them a continuation rather than a cold ask.</p>

  <h2>How it works</h2>
  <p>The Trailblazer is issued at the start of the visit and promoted alongside the Narrative Galleries and Adventure Galleries as one of the Library&rsquo;s three headline experiences. As a visitor moves through the building, the wearable records what they engaged with. That record becomes a personalized recap delivered the same evening.</p>
  <p>It has its own spot in the launch campaign &mdash; <em>Your Journey Starts Here</em> &mdash; which frames it not as a gadget but as the framing device for the whole day.</p>

  <div class="film">
    <div class="film-video">
      <iframe src="https://www.youtube-nocookie.com/embed/qrwdZmqFO5A" title="Your Journey Starts Here — The Trailblazer"
              loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              allowfullscreen></iframe>
    </div>
    <div class="film-body">
      <div class="film-head">
        <h3 class="film-title">Your Journey Starts Here</h3>
        <span class="film-meta">1:21 &middot; launch campaign</span>
      </div>
      <p class="film-tagline">The Trailblazer spot. Note what it sells: not a feature, but the idea that the visit is a journey with a beginning &mdash; which is what makes an ending, and a recap, feel earned rather than transactional.</p>
    </div>
  </div>

  <h2>Designing for the exit, not the entrance</h2>
  <p>The Trailblazer&rsquo;s real product isn&rsquo;t the band. It&rsquo;s the email that lands the night of the visit &mdash; <em>your day in the Badlands, captured and kept</em> &mdash; which is projected to be the <strong>highest-open-rate message in the Library&rsquo;s entire <a href="/projects/trpl-drip-campaign/">lifecycle program</a></strong>, ahead of every welcome, every appeal and every newsletter.</p>
  <p>That is not surprising when you think about who receives it. It arrives the evening of a memorable day, it is addressed to something the person actually did, and it contains their own visit rather than the institution&rsquo;s marketing. It is the one email a visitor genuinely wants.</p>
  <p>Which makes it the most valuable real estate the institution owns &mdash; and the reason the recap sits five days ahead of the first membership ask in the post-visit sequence. The wearable is a visitor-experience device wearing the costume of one, and a fundraising instrument underneath.</p>

  <div class="gallery cols-1">
    <figure>
      <picture>
        <source type="image/webp" srcset="/img/projects/trpl-trailblazer/01.webp">
        <img src="/img/projects/trpl-trailblazer/01.jpg" alt="Visitors on the Library's terrace during a guided introduction" loading="lazy" width="1600" height="900">
      </picture>
      <figcaption class="gallery-caption">The visit the wearable is trying to carry home.</figcaption>
    </figure>
  </div>

  <h2>What a wearable has to get right</h2>
  <p>Three constraints shaped the thinking, and they generalize to any institution considering one:</p>
  <ul>
    <li><strong>It cannot add friction at the door.</strong> Anything that slows admissions during a sold-out day costs more than it returns. Issuance has to be as fast as handing someone a ticket.</li>
    <li><strong>It cannot require an account.</strong> The moment a visitor has to create a login to receive their own visit, most of them won&rsquo;t.</li>
    <li><strong>It has to work for the person who does nothing.</strong> A visitor who taps two stations should still get a recap worth opening, or the whole mechanic breaks for the majority who engage lightly.</li>
  </ul>
  <p>The failure mode for this category of product is a device that produces a beautiful experience for the 5% who use it thoroughly and an empty email for everyone else.</p>

  <h2>Why it mattered</h2>
  <blockquote>The end of a visit is the moment an institution has the most attention and asks for the least.</blockquote>
  <p>Museums spend enormous effort on arrival &mdash; wayfinding, orientation films, first galleries &mdash; and comparatively little on departure, which is where the relationship is actually decided. The Trailblazer is an attempt to treat the exit as a designed moment rather than a door.</p>

  <p class="muted">Related: <a href="/projects/trpl-drip-campaign/">the lifecycle program the recap feeds</a> · <a href="/projects/trpl-launch-campaign/">the campaign that introduced it</a> · <a href="/projects/trpl-reading-room/">AI in the galleries</a></p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/trpl-launch-campaign/"><span class="dir">&larr; Previous</span><span class="title">Selling a Trip to the Badlands</span></a>
    <a class="next" href="/projects/mount-vernon-website/"><span class="dir">Next &rarr;</span><span class="title">Mount Vernon Website Redesign</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/trpl-trailblazer/index.html",
        title="The Trailblazer: A Wearable That Remembers Your Visit — Matt Briney",
        description="An RFID wearable at the Theodore Roosevelt Presidential Library designed around the exit rather than the entrance — and the same-evening recap email that follows it home.",
        active="projects",
        canonical="https://mattbriney.com/projects/trpl-trailblazer/",
        og_image="/img/projects/trpl-trailblazer/hero.jpg",
        body=BODY,
    )
