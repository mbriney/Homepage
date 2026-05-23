BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study &middot; Mount Vernon &middot; 2015&ndash;2017</p>
    <h1>Plan Your Day: A Custom Ticketing Workflow on Tessitura&rsquo;s API That Took Online Sales from 12% to 45%</h1>
    <p class="lede">When Matt arrived, Mount Vernon was selling roughly 12% of its tickets online through its legacy stack &mdash; Raiser&rsquo;s Edge for constituents and fundraising, Gateway for ticketing. He was part of the team that implemented Tessitura and migrated the institution off those systems &mdash; then rebuilt the visitor-facing purchase path from scratch on the Tessitura API. The custom &ldquo;Plan Your Day&rdquo; workflow walks visitors through date selection, general admission, the timed-entry Mansion tour, specialty add-ons, enhancement items, and discounts &mdash; on desktop and on the phone the visitor was already holding. Online ticket share went to <strong>45%</strong>, and mobile became Mount Vernon&rsquo;s single largest sales channel.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">VP, New Media (digital lead)</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">George Washington&rsquo;s Mount Vernon</span></div>
      <div class="meta-item"><span class="label">Platform</span><span class="value">Tessitura (custom build on the Tessitura API)</span></div>
      <div class="meta-item"><span class="label">Migrated from</span><span class="value">Raiser&rsquo;s Edge + Gateway</span></div>
      <div class="meta-item"><span class="label">Online share</span><span class="value">12% &rarr; 45%</span></div>
      <div class="meta-item"><span class="label">Mobile result</span><span class="value">#1 sales channel by Jul 2016</span></div>
      <div class="meta-item"><span class="label">Featured by</span><span class="value">Tessitura Success Stories, 2017</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/tessitura/hero.webp">
        <img src="/img/projects/tessitura/hero.jpg" alt="Plan Your Day — the custom Mount Vernon ticketing workflow built on the Tessitura API, showing three of the funnel steps as connected cards" width="1600" height="900">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Tessitura is the unified CRM / ticketing / fundraising platform that powers most of the world&rsquo;s major cultural institutions. Mount Vernon <em>wasn&rsquo;t</em> running on it when Matt arrived. The estate was on Raiser&rsquo;s Edge for fundraising and constituent data and on Gateway for ticketing &mdash; two separate systems, and a legacy web purchase path that was leaving most of the institution&rsquo;s ticket sales at the gate. Roughly <strong>12% of tickets</strong> were being sold online; the rest of the audience was showing up to the visitor center and standing in line. With foot traffic above a million people a year and a growing share of visitors arriving from a hotel room in D.C. with their phones already out, that ratio was leaving conversion, revenue, and visitor experience all on the table at once.</p>

  <h2>Implementing Tessitura &amp; retiring the old stack</h2>
  <p>Matt was part of the team that brought Tessitura to Mount Vernon and migrated the institution off Raiser&rsquo;s Edge and Gateway &mdash; consolidating constituent records, ticketing inventory, membership, and fundraising onto a single platform. That consolidation was the precondition for everything that followed: once the data lived in one place and the platform exposed it through an open API, the visitor-facing purchase path could finally be rebuilt around how people actually plan a visit.</p>

  <h2>What we built &mdash; the &ldquo;Plan Your Day&rdquo; workflow</h2>
  <p>We started from scratch with the Tessitura API rather than wrapping the standard web purchase path. The result was a guided, step-by-step funnel that treats the ticket purchase as the act of planning a day at Mount Vernon &mdash; not just buying a single bar-coded item. Each step is a deliberate decision point, and each step earns the upsell.</p>

  <h3>Step 1 &mdash; Pick the day</h3>
  <div class="gallery cols-1">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/tessitura/01-date.webp"><img src="/img/projects/tessitura/01-date.jpg" alt="Step 1 of the Plan Your Day workflow — a calendar UI for selecting the date of visit, with the Mansion tour timed-entry availability shown alongside"></picture>
      <figcaption class="gallery-caption">Step 1: the visitor picks a date. Behind the scenes, this is what unlocks every downstream availability check &mdash; Mansion timed-entry slots, specialty tours that don&rsquo;t run every day, member-only events.</figcaption>
    </figure>
  </div>

  <h3>Step 2 &mdash; General admission</h3>
  <div class="gallery cols-1">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/tessitura/02-ground-pass.webp"><img src="/img/projects/tessitura/02-ground-pass.jpg" alt="Step 2 — the general admission Ground Pass selector with adult, youth, and senior pricing tiers"></picture>
      <figcaption class="gallery-caption">Step 2: the general-admission Ground Pass &mdash; adult, youth, senior tiers; the institutional bread and butter.</figcaption>
    </figure>
  </div>

  <h3>Step 3 &mdash; The timed-entry Mansion tour</h3>
  <div class="gallery cols-1">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/tessitura/03-mansion.webp"><img src="/img/projects/tessitura/03-mansion.jpg" alt="Step 3 — the Mansion tour timed-entry selector, with available 15-minute time slots through the day"></picture>
      <figcaption class="gallery-caption">Step 3: the timed-entry Mansion tour &mdash; the visitor reserves a specific 15-minute window so the building doesn&rsquo;t get crowded. Inventory pulled live from Tessitura.</figcaption>
    </figure>
  </div>

  <h3>Step 4 &mdash; Specialty tours &amp; add-ons</h3>
  <div class="gallery cols-1">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/tessitura/04-addons.webp"><img src="/img/projects/tessitura/04-addons.jpg" alt="Step 4 — the Add-Ons screen, showing specialty tour cards including the National Treasure tour, the Slave Life tour, and Behind the Scenes tours"></picture>
      <figcaption class="gallery-caption">Step 4: the moment the upsell actually works. With the visitor&rsquo;s date and Mansion-tour time already locked in, the system can show only the specialty tours that fit their day &mdash; National Treasure, Slave Life, Behind the Scenes, Distillery &amp; Gristmill. <em>Tap the image to scroll the full page.</em></figcaption>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/tessitura/07-addons-detail.webp"><img src="/img/projects/tessitura/07-addons-detail.jpg" alt="Add-on detail — an individual specialty tour with date/time selector and per-person pricing"></picture>
      <figcaption class="gallery-caption">An add-on detail card: dates, times, available slots, per-person price &mdash; the same calendar logic as the Mansion tour, applied to every specialty experience on the estate.</figcaption>
    </figure>
  </div>

  <h3>Step 5 &mdash; Enhancement items</h3>
  <div class="gallery cols-1">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/tessitura/05-enhancements.webp"><img src="/img/projects/tessitura/05-enhancements.jpg" alt="Step 5 — Enhancement Items: audio tour rentals, guidebooks, and other physical add-ons available for pickup at the gate"></picture>
      <figcaption class="gallery-caption">Step 5: the things the visitor can carry through the gate &mdash; audio tour rentals, guidebooks, parking. Captured at the moment of intent, not at the register.</figcaption>
    </figure>
  </div>

  <h3>Step 6 &mdash; Discounts &amp; membership</h3>
  <div class="gallery cols-1">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/tessitura/06-discounts.webp"><img src="/img/projects/tessitura/06-discounts.jpg" alt="Step 6 — Discounts: member, AAA, military, and promotional code application"></picture>
      <figcaption class="gallery-caption">Step 6: discounts and membership. AAA, military, members, promo codes &mdash; pulled live from Tessitura&rsquo;s constituent records, so a member sign-in unlocks every member benefit across the cart in one move.</figcaption>
    </figure>
  </div>

  <h2>Launch day</h2>
  <p>The new platform went live in January 2016 &mdash; the culmination of the migration off Raiser&rsquo;s Edge and Gateway and the build of the custom purchase path on top of it.</p>
  <div class="gallery cols-2">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/tessitura/launch-01.webp"><img src="/img/projects/tessitura/launch-01.jpg" alt="The Mount Vernon team at the Tessitura launch, January 2016" loading="lazy"></picture>
      <figcaption class="gallery-caption">The team at the Tessitura launch &mdash; January 20, 2016.</figcaption>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/tessitura/launch-02.webp"><img src="/img/projects/tessitura/launch-02.jpg" alt="Mount Vernon staff at workstations during the Tessitura go-live" loading="lazy"></picture>
      <figcaption class="gallery-caption">Go-live at the visitor center.</figcaption>
    </figure>
  </div>

  <h2>Watch the testimonial</h2>
  <div class="film" id="testimonial">
    <div class="film-video">
      <iframe src="https://www.youtube-nocookie.com/embed/jGoua0nLGIE" title="Tessitura helps George Washington's Mount Vernon grow online and mobile ticketing" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <div class="film-body">
      <div class="film-head">
        <h3 class="film-title">From 12% to 45% online &mdash; on Matt&rsquo;s own words</h3>
        <span class="film-meta">1:40 &middot; Tessitura, 2017</span>
      </div>
      <p class="film-tagline">A short testimonial produced by Tessitura covering the workflow, the mobile shift, and the conversion numbers from the team that built it.</p>
    </div>
  </div>

  <h2>Why the new workflow works</h2>

  <h3>It treats a ticket as a plan, not an item</h3>
  <p>The single most important design choice was sequencing. Date first, then admission, then the timed Mansion tour, <em>then</em> specialty tours, <em>then</em> add-ons, <em>then</em> discounts. By the time the visitor sees a Slave Life tour on screen, the system already knows what day they&rsquo;re coming and what time their Mansion entry is, so it can show only the specialty tours that fit. That&rsquo;s why the cross-sell works &mdash; it&rsquo;s not a generic upsell card stapled onto the checkout; it&rsquo;s an offer that actually fits the day the visitor just told us they&rsquo;re planning.</p>

  <h3>It was built mobile-first</h3>
  <p>The biggest insight in the rollout was where the buyers actually were. As Matt put it on the Tessitura case film:</p>
  <blockquote>People are coming to Washington, D.C. They&rsquo;re in their hotel room. They&rsquo;re looking for things to do, and they&rsquo;re on their smartphones. Because of what we&rsquo;ve done with the Tessitura database and the customer API integration, we&rsquo;ve been able to create a ticketing workflow that allows them to purchase right from their mobile device, and then they can go right up to the gate and scan it. In July 2016, we sold more tickets through our mobile device than any other platform.<span style="display:block;margin-top:.7rem;font-style:normal;font-size:.9rem;color:var(--ink-muted)">&mdash; Matt Briney, VP New Media, Mount Vernon (Tessitura case study, 2017)</span></blockquote>

  <h3>It runs on Tessitura&rsquo;s API, not Tessitura&rsquo;s default web purchase path</h3>
  <p>The platform&rsquo;s out-of-the-box web purchase path is fine for many institutions. For Mount Vernon &mdash; a million-plus visitors a year, dozens of specialty tours, member discount cascades, complex timed-entry inventory across the Mansion and outbuildings &mdash; the default flow couldn&rsquo;t do the upsell math at the speed of the conversation. So we wrote the front end ourselves and pointed it at Tessitura&rsquo;s APIs for everything: inventory, holds, constituent records, member benefits, fulfillment. That openness is the thing Mount Vernon couldn&rsquo;t have gotten from any other platform we evaluated.</p>

  <h2>The results</h2>

  <div class="case-stats-row">
    <div class="case-stat"><strong>12% &rarr; 45%</strong><span>online share of ticket sales</span></div>
    <div class="case-stat"><strong>#1</strong><span>mobile as top sales channel</span></div>
    <div class="case-stat"><strong>Specialty tours</strong><span>conversion lift across the catalog</span></div>
    <div class="case-stat"><strong>2017</strong><span>featured by Tessitura as a success story</span></div>
  </div>

  <p>Three things moved at once:</p>
  <ul>
    <li><strong>Online share of sales went from ~12% to ~45%.</strong> Quadrupling the digital channel is the headline result &mdash; less line at the gate, better data on every visitor, more capacity at the register for everything that <em>does</em> still happen in person.</li>
    <li><strong>Mobile became the top sales channel.</strong> By July 2016, the first full year after launch, the Plan Your Day workflow was selling more tickets via smartphones than any other channel including the gate window itself.</li>
    <li><strong>Specialty tours lifted across the catalog.</strong> Tours that had historically under-performed &mdash; National Treasure, Slave Life, Distillery &amp; Gristmill, Behind the Scenes &mdash; got a much larger share of attention now that they were being offered to visitors who&rsquo;d already committed to a date and were genuinely planning their day.</li>
  </ul>

  <h2>What we learned</h2>
  <ul>
    <li><strong>Don&rsquo;t fight your platform; extend it.</strong> Building the custom workflow on the Tessitura API meant we kept everything we needed (constituent records, inventory, member benefits, reporting, fulfillment) and only re-built the layer the visitor actually touches.</li>
    <li><strong>The right sequence sells more than the right copy.</strong> Showing the specialty tours <em>after</em> the visitor has committed to a date and a Mansion time is what made the upsell work. The order is the offer.</li>
    <li><strong>Mobile isn&rsquo;t a sidecar.</strong> If a third of the people buying tickets are on a phone in their hotel room, the phone is the primary purchase environment &mdash; not a stripped-down version of the &ldquo;real&rdquo; site. We built the flow to work on the small screen first and let the desktop be a wider version of the same thing.</li>
  </ul>

  <h2>Why it mattered</h2>
  <blockquote>It has been a tremendous change. With our previous ticketing system we were only selling about 12% of our tickets online. We now are seeing about 45% of our tickets sold online&hellip; The openness of the platform, access to the data that in other systems is really normally very restricted: it&rsquo;s been a fantastic experience that has allowed us to develop something that really is more tailored toward our business and our customers&rsquo; needs.<span style="display:block;margin-top:.7rem;font-style:normal;font-size:.9rem;color:var(--ink-muted)">&mdash; Matt Briney, Tessitura Success Story, July 2017</span></blockquote>
  <p>The ticketing system isn&rsquo;t the thing visitors come to Mount Vernon for. But it&rsquo;s the system the institution sees the visitor through &mdash; the door, the cross-sell, the membership upgrade, the renewal, the data trail that feeds everything that comes after. Quadrupling the share of that experience that happens online &mdash; and putting it in the visitor&rsquo;s pocket the day they decide to come &mdash; is one of the highest-leverage product moves a place like Mount Vernon can make.</p>

  <p class="muted" style="margin-top:2rem;font-size:.9rem;">References: <a href="https://www.tessitura.com/items/articles/success-stories/mt-vernon-matthew-briney" target="_blank" rel="noopener">Tessitura Success Story (July 2017)</a> &middot; <a href="https://www.youtube.com/watch?v=jGoua0nLGIE" target="_blank" rel="noopener">Tessitura testimonial video on YouTube</a></p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/mount-vernon-website/"><span class="dir">&larr; Previous</span><span class="title">Mount Vernon Website</span></a>
    <a class="next" href="/projects/mount-vernon-virtual-tour/"><span class="dir">Next &rarr;</span><span class="title">Mount Vernon Virtual Tour</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/tessitura-ticketing/index.html",
        title="Plan Your Day — Mount Vernon's Custom Tessitura Ticketing Workflow — Matt Briney",
        description="How Mount Vernon migrated off Raiser's Edge and Gateway to Tessitura, then went from 12% to 45% online ticket sales — and made mobile the #1 sales channel — by building a custom Plan Your Day purchase workflow on the Tessitura API. Six-step funnel: date, ground pass, timed Mansion tour, specialty add-ons, enhancement items, discounts.",
        active="projects",
        canonical="https://mattbriney.com/projects/tessitura-ticketing/",
        og_image="/img/projects/tessitura/hero.jpg",
        body=BODY,
    )
