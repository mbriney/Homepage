BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Theodore Roosevelt Presidential Library · 2026</p>
    <h1>Six Systems, One Visitor: An Automated Lifecycle for a New Institution</h1>
    <p class="lede">A donor who buys a ticket and eats lunch is three different contacts in three different databases. Opening weekend was going to generate tens of thousands of them. This is the design that turns six partial views of a person into one profile &mdash; and then decides, without a human in the loop, which of five journeys they belong in.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Chief Communications &amp; Marketing Officer</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">Theodore Roosevelt Presidential Library</span></div>
      <div class="meta-item"><span class="label">Year</span><span class="value">2026</span></div>
      <div class="meta-item"><span class="label">Stack</span><span class="value">Constant Contact · ACME · Shopify · Clover · DonorPerfect · wealth screening</span></div>
      <div class="meta-item"><span class="label">Scope</span><span class="value">41 emails · 5 journeys · 9-level hierarchy</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/trpl-drip-campaign/hero.webp">
        <img src="/img/projects/trpl-drip-campaign/hero.jpg" alt="Detail of an artifact from the Theodore Roosevelt Presidential Library collection" width="1600" height="900">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Six systems each held a partial view of the same human being: web forms, ACME ticketing, ACME membership, Shopify, Clover point-of-sale, and DonorPerfect. None of them agreed on who anyone was.</p>
  <p>That is survivable at a thousand contacts. At opening scale it produces the failure every institution recognizes: a $10,000 donor receiving a first-time-visitor welcome email, a member being asked to become a member, a family getting four versions of the same message because they exist four times.</p>

  <div class="case-stats-row">
    <div class="case-stat"><strong>41</strong><span>Emails drafted</span></div>
    <div class="case-stat"><strong>5</strong><span>Lifecycle journeys</span></div>
    <div class="case-stat"><strong>9</strong><span>Priority levels</span></div>
    <div class="case-stat"><strong>6</strong><span>Source systems unified</span></div>
  </div>

  <h2>One profile, permanent signals</h2>
  <p>Matching runs on email first, then source-system contact ID, with a manual review queue for anything ambiguous. The rule that makes it durable: <strong>source is a permanent tag that is never overwritten.</strong> Signals stack rather than replace. Someone who arrives as a shop customer and later becomes a member is both, forever, and both facts stay available to segmentation.</p>
  <p>The named data-quality metric is match success rate &mdash; because a lifecycle program silently degrades when matching degrades, and nobody notices until the wrong person gets the wrong ask.</p>

  <h2>The priority hierarchy</h2>
  <p>The core design decision is what happens when a person qualifies for several journeys at once, which is most people. Nine levels, evaluated in order. The counterintuitive one is near the top:</p>
  <div class="lane-table">
    <div class="lane">
      <div class="lane-outlet">Cumulative giving outranks membership</div>
      <div class="lane-who">At $1,000 and above, a donor who is <em>also</em> a member gets the donor journey, not the member journey. The higher-value relationship wins, even when the lower-value one is more recent. Most systems get this backwards because membership status is the easier field to read.</div>
    </div>
    <div class="lane">
      <div class="lane-outlet">Tier 5 is suppressed entirely</div>
      <div class="lane-who">Donors at $50,000+ receive no automated mail at all. At that level the relationship belongs to a major gifts officer, and an automated touch is worse than silence.</div>
    </div>
    <div class="lane">
      <div class="lane-outlet">Recency breaks ties below the giving threshold</div>
      <div class="lane-who">Under $1,000, the most recent meaningful action wins — a visit outranks a year-old shop order.</div>
    </div>
  </div>

  <h2>Five journeys</h2>
  <ul>
    <li><strong>Soft Lead Nurture</strong> &mdash; 4 emails, for people who raised a hand but haven&rsquo;t transacted.</li>
    <li><strong>Visit Prep</strong> &mdash; 5 emails before, 6 after.</li>
    <li><strong>Member</strong> &mdash; 14 emails across the membership year.</li>
    <li><strong>Donor</strong> &mdash; 9 emails, tiered.</li>
    <li><strong>Cross-cutting</strong> &mdash; 3 more that run alongside the others.</li>
  </ul>

  <h3>The lead-time gate</h3>
  <p>The detail I&rsquo;m proudest of is that the pre-visit sequence compresses to fit the buyer instead of firing on a fixed calendar. Book five or more days out and you get the full five-touch cadence. Book two to four days out and it skips the T-5 email. Book same-day or next-day and T+0 merges with the T-24h content, leaning on a morning-of SMS instead.</p>
  <p>A visitor who books tomorrow should not receive an email telling them what to pack next week. That sounds obvious and almost no automated program does it, because sequences are usually written as fixed timelines rather than as a function of how much runway you have.</p>

  <h3>Two membership asks, deliberately different</h3>
  <p>The post-visit sequence makes the membership case twice, in two registers. <strong>T+5 is tactical</strong> &mdash; apply the price of today&rsquo;s ticket toward a membership. <strong>T+30 is narrative</strong> &mdash; come for the man, leave with a mission. Those land with different people, and sending only one of them means losing whichever half doesn&rsquo;t respond to that frame.</p>

  <div class="gallery cols-1">
    <figure>
      <picture>
        <source type="image/webp" srcset="/img/projects/trpl-drip-campaign/01.webp">
        <img src="/img/projects/trpl-drip-campaign/01.jpg" alt="Visitors gathered around an interactive station in the Library galleries" loading="lazy" width="1600" height="900">
      </picture>
      <figcaption class="gallery-caption">Every one of these people is a row in six different systems. The program&rsquo;s job is to make them one person again.</figcaption>
    </figure>
  </div>

  <h2>Wealth screening that never blocks a send</h2>
  <p>Capacity screening runs as a nightly asynchronous batch, by design. Today&rsquo;s email uses today&rsquo;s capacity tags; tomorrow&rsquo;s uses updated ones. Nothing waits on a third-party lookup, because a screening API having a slow night should never delay a visit-prep email.</p>
  <p>It produces two flags for human review &mdash; <code>member_prospect</code> and <code>upgrade_candidate</code> &mdash; which go to a major gifts officer rather than triggering an automated ask. The argument for doing it at all:</p>
  <blockquote>Without ongoing screening, a high-capacity member sits in standard automation giving $150 a year when they could be giving thousands.</blockquote>

  <h2>Guardrails</h2>
  <p>The rules that stop the program from doing damage, enforced platform-wide rather than per-sequence &mdash; which matters, because per-sequence limits are exactly how people end up receiving four emails from four journeys that each individually behaved:</p>
  <ul>
    <li>Maximum one email per 48 hours, and eight per 30 days, across everything.</li>
    <li>Tier 5 donors suppressed from all automation.</li>
    <li>Donors at $5,000+ never receive an automated ask below their lifetime average gift.</li>
    <li>New members protected from upgrade asks for 60 days.</li>
  </ul>
  <p>That third one is the rule I&rsquo;d put on a wall: <strong>the rule that prevents $100 asks from preventing $10,000 gifts.</strong> An automated ask that anchors low is not neutral &mdash; it actively costs money, and it does so invisibly.</p>

  <h2>250 miles</h2>
  <p>Member content splits on a distance band, on the premise that a substantial share of members will rarely or never visit. Inside 250 miles, membership is framed around return visits and events. Outside it, the digital benefits lead &mdash; because selling &ldquo;free admission all year&rdquo; to someone in Atlanta is selling something they cannot use, and they will notice.</p>

  <h2>Configuration, not engineering</h2>
  <p>All of it runs in Constant Contact rather than a custom build. <strong>The work is configuration, not engineering</strong> &mdash; which is the only responsible choice for an institution whose communications team is two people. A bespoke marketing-automation platform would have been more elegant and would have become unmaintainable the moment I left.</p>

  <h2>What I&rsquo;d carry forward</h2>
  <ul>
    <li><strong>Decide the priority hierarchy before writing a single email.</strong> Everything downstream is an argument about precedence, and it&rsquo;s cheaper to have that argument on paper.</li>
    <li><strong>Never overwrite source.</strong> Signals should accumulate; the moment you replace one, you have destroyed a segment you&rsquo;ll want later.</li>
    <li><strong>Enforce frequency caps globally.</strong> Per-journey limits guarantee the failure they&rsquo;re meant to prevent.</li>
    <li><strong>Suppress your best relationships.</strong> The most valuable thing automation can do for a major donor is leave them alone.</li>
    <li><strong>Fit the sequence to the runway.</strong> Lead time is a variable, not a constant.</li>
  </ul>

  <h2>Why it mattered</h2>
  <blockquote>An institution&rsquo;s email program is the only conversation it has with almost everyone who will ever care about it.</blockquote>
  <p>Most of the 150,000&ndash;200,000 people expected annually will visit once. What happens in the six weeks around that visit determines whether they become a member, a donor, an advocate, or a person who went to a museum once. That is worth designing properly, and it is worth designing before the doors open rather than after the first season&rsquo;s data disappoints.</p>

  <p class="muted">Related: <a href="/projects/trpl-launch-campaign/">the launch campaign that fills the funnel</a> · <a href="/projects/trpl-trailblazer/">the wearable that triggers the recap email</a> · <a href="/projects/trpl-grand-opening-media/">the opening that generated the volume</a></p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/trpl-labs/"><span class="dir">&larr; Previous</span><span class="title">Twenty-Odd Tools, Zero Servers</span></a>
    <a class="next" href="/projects/trpl-launch-campaign/"><span class="dir">Next &rarr;</span><span class="title">Selling a Trip to the Badlands</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/trpl-drip-campaign/index.html",
        title="Six Systems, One Visitor: An Automated Visitor Lifecycle — Matt Briney",
        description="Designing the Theodore Roosevelt Presidential Library's automated visitor lifecycle: 41 emails, 5 journeys, a 9-level priority hierarchy, and six source systems unified into one profile.",
        active="projects",
        canonical="https://mattbriney.com/projects/trpl-drip-campaign/",
        og_image="/img/projects/trpl-drip-campaign/hero.jpg",
        body=BODY,
    )
