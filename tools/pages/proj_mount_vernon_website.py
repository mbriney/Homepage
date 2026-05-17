BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Mount Vernon · 2014–2024</p>
    <h1>Mount Vernon&rsquo;s Website Reborn as the Country&rsquo;s Largest Open Classroom on George Washington</h1>
    <p class="lede">A ten-year content-and-SEO rebuild that grew the website from 2.5M to 8M+ annual visitors and turned digital into a self-funding pillar of the operating model.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">VP, Media &amp; Communications</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">George Washington&rsquo;s Mount Vernon</span></div>
      <div class="meta-item"><span class="label">Years</span><span class="value">2014 — 2024</span></div>
      <div class="meta-item"><span class="label">Team</span><span class="value">Digital, content, design, engineering</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/mount-vernon-website/hero.webp">
        <img src="/img/projects/mount-vernon-website/hero.jpg" alt="Mount Vernon website — Buy Tickets / itinerary builder" width="1600" height="1066">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>For most of America, Mount Vernon&rsquo;s website is the first &mdash; and sometimes only &mdash; visit to the estate they&rsquo;ll ever take. When I joined in 2014, the site was a serviceable brochure: hours, tickets, a few exhibits. The job was to turn it into something else entirely &mdash; the country&rsquo;s definitive online resource on George Washington and the founding era, and a sustainable engine for visitation, e-commerce, membership, and earned revenue.</p>

  <div class="case-stats-row">
    <div class="case-stat"><strong>8M+</strong><span>annual visitors (from 2.5M)</span></div>
    <div class="case-stat"><strong>3.5m</strong><span>average dwell time</span></div>
    <div class="case-stat"><strong>$8.6M</strong><span>e-commerce (from $1.1M)</span></div>
    <div class="case-stat"><strong>35%</strong><span>infrastructure cost reduction</span></div>
  </div>

  <h2>What we did</h2>

  <h3>Content as the front door</h3>
  <p>Rather than build pages around tickets, we built them around topics &mdash; long-form, primary-source-anchored explorations of Washington&rsquo;s life, the Revolutionary era, the founding, slavery at Mount Vernon, the landscape, the architecture. Each topic became its own SEO target. Over a decade, dozens of those pages claimed the top 2&ndash;3 organic search positions for their query and turned the site into the place teachers, students, journalists, and the curious actually land.</p>

  <div class="gallery cols-2">
    <figure>
      <picture>
        <source type="image/webp" srcset="/img/projects/mount-vernon-website/01.webp">
        <img src="/img/projects/mount-vernon-website/01.jpg" alt="Mount Vernon homepage" width="1600" height="1066">
      </picture>
    </figure>
    <figure>
      <picture>
        <source type="image/webp" srcset="/img/projects/mount-vernon-website/03.webp">
        <img src="/img/projects/mount-vernon-website/03.jpg" alt="George Washington biography landing page" width="1600" height="1066">
      </picture>
    </figure>
  </div>

  <h3>A revenue engine, not a checkout</h3>
  <p>We replatformed e-commerce on a custom stack that brought tickets, donations, memberships, and donor retention into a single system. We rebuilt the membership pricing model, hit a 30% lift in new members in year one, and grew online revenue from $1.1M to $8.6M over six years. Email got segmented, mobile got prioritized, and a centralized CRM tied the whole loop together.</p>

  <h3>Infrastructure that scaled with the audience</h3>
  <p>We migrated the entire web and database stack to AWS, cut operating costs ~35%, and gave the platform the headroom to keep up with growth. The website that opened in 2014 doing 4M visits closed out 2021 at 9M.</p>

  <div class="gallery cols-2">
    <figure>
      <picture>
        <source type="image/webp" srcset="/img/projects/mount-vernon-website/02.webp">
        <img src="/img/projects/mount-vernon-website/02.jpg" alt="Plant Finder educational tool on Mount Vernon's site" width="1600" height="1066">
      </picture>
      <figcaption class="gallery-caption">The Plant Finder &mdash; one of dozens of purpose-built tools that gave the site reasons to come back.</figcaption>
    </figure>
    <figure>
      <picture>
        <source type="image/webp" srcset="/img/projects/mount-vernon-website/hero.webp">
        <img src="/img/projects/mount-vernon-website/hero.jpg" alt="Ticketing add-ons" width="1600" height="1066">
      </picture>
      <figcaption class="gallery-caption">The visit-builder: tickets, time slots, and add-on experiences in one flow.</figcaption>
    </figure>
  </div>

  <h2>Why it mattered</h2>
  <p>Treating the website as the front door rather than the brochure changed the institution&rsquo;s reach by an order of magnitude. The number of Americans who could say they&rsquo;d &ldquo;been to Mount Vernon&rdquo; (in any meaningful sense) jumped from ~1M physical visitors a year to ~10M digital-or-physical. And the work became a model the rest of the historic-site sector started looking to: <em>content depth, not feature breadth, is what turns a cultural institution&rsquo;s website into a public good.</em></p>

  <p style="margin-top:2.5rem">
    <a class="btn btn-primary" href="https://www.mountvernon.org/" target="_blank" rel="noopener">Visit MountVernon.org &rarr;</a>
  </p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/"><span class="dir">&larr; Back</span><span class="title">All projects</span></a>
    <a class="next" href="/projects/mount-vernon-virtual-tour/"><span class="dir">Next &rarr;</span><span class="title">Mount Vernon Virtual Tour</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/mount-vernon-website/index.html",
        title="Mount Vernon Website Redesign — Matt Briney",
        description="How we rebuilt Mount Vernon's website around SEO-led content marketing, grew annual visitors from 2.5M to 8M+, and grew e-commerce from $1.1M to $8.6M.",
        active="projects",
        canonical="https://mattbriney.com/projects/mount-vernon-website/",
        og_image="/img/projects/mount-vernon-website/hero.jpg",
        body=BODY,
    )
