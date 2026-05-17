BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Edelman Public Relations · 2011–2014</p>
    <h1>Multiplier: Edelman&rsquo;s Engagement Platform</h1>
    <p class="lede">A Salesforce-based proprietary marketing platform built from scratch &mdash; the engine behind Edelman&rsquo;s advocacy, fundraising, internal-comms, and engagement work for HP, Hyundai, Microsoft, BlackBerry, GE, Shell, Pepsi, and dozens of other clients.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">VP, Technical Manager</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">Edelman Public Relations</span></div>
      <div class="meta-item"><span class="label">Stack</span><span class="value">Salesforce.com platform</span></div>
      <div class="meta-item"><span class="label">Portfolio</span><span class="value">60+ projects</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/multiplier/hero.webp">
        <img src="/img/projects/multiplier/hero.jpg" alt="Multiplier dashboard — Hilex tenant view" width="1600" height="1066">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Edelman&rsquo;s big clients didn&rsquo;t need another campaign agency &mdash; they needed an engagement <em>platform</em>: a single place to run grassroots advocacy, fundraising, internal communications, and engagement analytics across web, social, email, and offline together. Buying that off the shelf was expensive and rigid. Building it gave Edelman the kind of proprietary capability competitors couldn&rsquo;t match.</p>

  <h2>What it did</h2>
  <p>Multiplier was a multi-tenant marketing platform on top of Salesforce.com. Every Edelman client got their own branded tenant with the modules they needed:</p>
  <ul>
    <li><strong>Campaigns</strong> &mdash; advocacy, petition, lobby-letter, write-to-Congress workflows</li>
    <li><strong>Emails</strong> &mdash; segmented sends with engagement tracking</li>
    <li><strong>Forms &amp; petitions</strong> &mdash; data capture with downstream CRM logic</li>
    <li><strong>Events</strong> &mdash; ticketed and free, with attendance tracking</li>
    <li><strong>Reports</strong> &mdash; cross-channel engagement analytics</li>
    <li><strong>Lobby Letters, Tell-A-Friend, Social Advocacy, Messages, Websites</strong> &mdash; specialized modules for the work Edelman&rsquo;s public-affairs practice actually did</li>
  </ul>

  <div class="gallery cols-2">
    <figure><picture><source type="image/webp" srcset="/img/projects/multiplier/01.webp"><img src="/img/projects/multiplier/01.jpg" alt="Multiplier screen"></picture></figure>
    <figure><picture><source type="image/webp" srcset="/img/projects/multiplier/02.webp"><img src="/img/projects/multiplier/02.jpg" alt="Multiplier screen"></picture></figure>
    <figure><picture><source type="image/webp" srcset="/img/projects/multiplier/03.webp"><img src="/img/projects/multiplier/03.jpg" alt="Multiplier screen"></picture></figure>
    <figure><picture><source type="image/webp" srcset="/img/projects/multiplier/04.webp"><img src="/img/projects/multiplier/04.jpg" alt="Multiplier screen"></picture></figure>
  </div>

  <h2>Notable deployments</h2>
  <ul>
    <li><strong>HP</strong> &mdash; HPNN, an internal news platform for the C-suite, built on the same Multiplier foundations. Commissioned by Meg Whitman during a period of rapid leadership change.</li>
    <li><strong>Hyundai</strong> &mdash; in 24 hours, we shipped an interactive reimbursement tool using Multiplier to address an EPA fuel-economy miscalculation. Owners entered their VIN; the tool computed the discrepancy, factored in state-specific fuel prices, and offered 120% cash value as fair compensation &mdash; ahead of Hyundai&rsquo;s EPA hearing with competitors.</li>
    <li><strong>BlackBerry RIM</strong> &mdash; a B2G (Business-to-Government) site highlighting BlackBerry&rsquo;s secure-communications stack for federal buyers.</li>
    <li><strong>GE, Chevron</strong> &mdash; bespoke internal communication and publishing systems, with the privacy and security posture each company required.</li>
    <li><strong>Microsoft, Walmart, Pfizer, API, Pepsi</strong> and dozens more &mdash; grassroots advocacy campaigns at national scale.</li>
  </ul>

  <h2>Why it mattered</h2>
  <p>Multiplier was a working argument that the right answer to &ldquo;build vs. buy&rdquo; in agency-land is sometimes <em>build</em> &mdash; and that a PR firm with a real platform behind it is doing something fundamentally different from a PR firm with a stack of point tools. It&rsquo;s also where I learned, hands-on, how big enterprises move and what it takes to build technology that serves communications work rather than competing with it.</p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/trpl-reading-room/"><span class="dir">&larr; Previous</span><span class="title">TRPL Reading Room</span></a>
    <a class="next" href="/projects/travel-passport/"><span class="dir">Next &rarr;</span><span class="title">Travel Passport</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/multiplier/index.html",
        title="Multiplier (Edelman Engagement Platform) — Matt Briney",
        description="Multiplier was Edelman's proprietary Salesforce-based engagement platform — the engine behind 60+ projects for HP, Hyundai, Microsoft, BlackBerry, GE, Shell, Pepsi and others.",
        active="projects",
        canonical="https://mattbriney.com/projects/multiplier/",
        og_image="/img/projects/multiplier/hero.jpg",
        body=BODY,
    )
