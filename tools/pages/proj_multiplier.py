BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Edelman Public Relations · 2011–2014</p>
    <h1>Multiplier: Edelman&rsquo;s Largest Client-Facing Technology Investment to Date</h1>
    <p class="lede">A complete rebuild of Edelman&rsquo;s legacy <em>Grassroots Multiplier&reg;</em> advocacy platform into a modern, multi-tenant <strong>Engagement Tool</strong> built on Salesforce&rsquo;s Force.com and a Rackspace LAMP front-end. Designed around one question: how do you find people, mobilize them, and prove it happened? Shipped to 60+ client tenants spanning HP, Hyundai, Microsoft, BlackBerry, GE, Shell, Pepsi, the Embassy of Canada, the American Petroleum Institute, the Episcopal Church, and the National Health Council.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">VP, Technical Manager</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">Edelman Public Relations</span></div>
      <div class="meta-item"><span class="label">Platform</span><span class="value">Salesforce Force.com + Rackspace LAMP</span></div>
      <div class="meta-item"><span class="label">Replaced</span><span class="value">Grassroots Multiplier® (legacy)</span></div>
      <div class="meta-item"><span class="label">Tenancies</span><span class="value">60+ Edelman clients</span></div>
      <div class="meta-item"><span class="label">Launched</span><span class="value">Spring 2012</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/multiplier/hero.webp">
        <img src="/img/projects/multiplier/hero.jpg" alt="Multiplier &mdash; client tenant dashboard for Hilex showing campaigns, new-members chart, lobby-letters gauge, letters-by-action histogram, and task list" width="1600" height="1066">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Edelman&rsquo;s Grassroots Enterprise practice ran on <em>Grassroots Multiplier&reg;</em>, a first-generation advocacy and engagement platform that had powered the firm&rsquo;s public-affairs work for years. By the early 2010s the technology underneath it was aging: every campaign needed a custom build, the data model wasn&rsquo;t plug-and-play across clients, and adding the next generation of features (social listening, mobile, intelligent data appending) required more bespoke work than the practice could afford to ship at scale.</p>
  <p>The brief, internally framed as <em>Multiplier 2</em> (and ultimately just <strong>Multiplier</strong>), was to rebuild the platform from the ground up: cloud-native, multi-tenant, API-driven, and architected so the next 60 client launches were configuration rather than custom development. The Multiplier FAQ described it at the time as &ldquo;Edelman&rsquo;s largest client-facing technology investment to date.&rdquo;</p>

  <h2>The product positioning</h2>
  <blockquote>Multiplier takes an existing supporter list and multiplies recruitment and engagement.<span style="display:block;margin-top:.7rem;font-style:normal;font-size:.9rem;color:var(--ink-muted)">— Multiplier internal positioning, Edelman University deck</span></blockquote>

  <p>The internal product framing reduced every engagement campaign to three questions, and built every feature in service of one of them:</p>

  <div class="flow">
    <div class="flow-step">
      <h4>Recruiting</h4>
      <p>How do you <strong>find people</strong>? Web forms, petitions, lobby letters, events, social-share actions, and offline data capture &mdash; all flowing into a single contact database.</p>
    </div>
    <div class="flow-step">
      <h4>Mobilizing</h4>
      <p>How do you <strong>get them to do something</strong>? Segment by attributes, frame messages per audience, deliver via email/social/web, and measure response in real time.</p>
    </div>
    <div class="flow-step">
      <h4>Proof</h4>
      <p>How do you <strong>know it happened</strong>? Cross-channel attribution, A/B testing, engagement scoring, and analytics that demonstrate impact to the client and the cause.</p>
    </div>
  </div>

  <h2>The engagement spectrum</h2>
  <p>Underneath every campaign was the same model of stakeholder commitment, drawn from years of grassroots-advocacy work. Multiplier treated audience identification as a first-class workflow: every supporter ran along a commitment curve from <strong>logical interest</strong> at the bottom to <strong>fervent participation</strong> at the top, and the platform&rsquo;s job was to move the right people up the curve at the right moment.</p>
  <ul>
    <li><strong>Logical Interest</strong> &mdash; someone who&rsquo;s aware of the cause but hasn&rsquo;t signaled commitment.</li>
    <li><strong>Committed Interest</strong> &mdash; opened an email, read a post, recognized the issue.</li>
    <li><strong>Passive Support</strong> &mdash; signed a petition, clicked a link, took one action.</li>
    <li><strong>Active Support</strong> &mdash; sent a lobby letter, registered for an event, recurring participation.</li>
    <li><strong>Engaged Participation</strong> &mdash; recurring lobby actions, friends recruited, in-person meetings.</li>
    <li><strong>Fervent Participation</strong> &mdash; surrogate spokesperson, surrogate news source, embedded volunteer.</li>
  </ul>

  <h2>The feature set: a modular &ldquo;blade&rdquo; architecture</h2>
  <p>Where the legacy platform shipped as a monolith, the new Multiplier was designed as a stack of modular feature blades that could be turned on per-tenant. A small client got a CRM with a few forms; a large public-affairs client got the full advocacy and lobbying stack with social monitoring and data appending on top.</p>

  <div class="cards" style="margin-top:1.5rem">
    <div class="card">
      <div class="card-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
      </div>
      <h3>CRM &amp; Database</h3>
      <p class="muted">Contacts, organizations, affiliations, custom fields per tenant, owner assignments, notes, attachments, activity history.</p>
    </div>
    <div class="card">
      <div class="card-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 9 12 14 17 20 11"/><polyline points="14 7 20 7 20 13"/></svg>
      </div>
      <h3>Email Marketing</h3>
      <p class="muted">Blast email, A/B testing, segmentation, deliverability tracking, partnered with ExactTarget for the heavy-lift sending infrastructure.</p>
    </div>
    <div class="card">
      <div class="card-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 21h8M12 18v3"/></svg>
      </div>
      <h3>Website &amp; Forms</h3>
      <p class="muted">CMS, embeddable forms (paste an iframe into any client CMS), goals &amp; funnels, conversion tracking, website analytics.</p>
    </div>
    <div class="card">
      <div class="card-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3h18l-7 10v6l-4 2v-8z"/></svg>
      </div>
      <h3>Grassroots Advocacy</h3>
      <p class="muted">Letters to federal, state, and custom targets. Bill &amp; vote tracking. ZIP+4 district matching. Elected-official lookups. Committee memberships.</p>
    </div>
    <div class="card">
      <div class="card-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>
      </div>
      <h3>Social Monitoring &amp; Engagement</h3>
      <p class="muted">Conversation tracking, top-influencer identification, OAuth-based account linkage, sharing tools and analytics.</p>
    </div>
    <div class="card">
      <div class="card-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .3 1.8l.1.1a2 2 0 0 1-2.8 2.8l-.1-.1a1.65 1.65 0 0 0-1.8-.3 1.65 1.65 0 0 0-1 1.5V21a2 2 0 0 1-4 0v-.1A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.8.3l-.1.1a2 2 0 0 1-2.8-2.8l.1-.1a1.65 1.65 0 0 0 .3-1.8 1.65 1.65 0 0 0-1.5-1H3a2 2 0 0 1 0-4h.1A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.3-1.8l-.1-.1a2 2 0 0 1 2.8-2.8l.1.1a1.65 1.65 0 0 0 1.8.3H9a1.65 1.65 0 0 0 1-1.5V3a2 2 0 0 1 4 0v.1a1.65 1.65 0 0 0 1 1.5 1.65 1.65 0 0 0 1.8-.3l.1-.1a2 2 0 0 1 2.8 2.8l-.1.1a1.65 1.65 0 0 0-.3 1.8V9a1.65 1.65 0 0 0 1.5 1H21a2 2 0 0 1 0 4h-.1a1.65 1.65 0 0 0-1.5 1z"/></svg>
      </div>
      <h3>Reporting &amp; API</h3>
      <p class="muted">Saved reports, cross-channel attribution, A+B test results, scheduled exports, and a full API layer for client-side integrations.</p>
    </div>
  </div>

  <h2>Multiplier Intelligence: data appending</h2>
  <p>One of the platform&rsquo;s flagship differentiators was <em>Multiplier Intelligence</em> &mdash; a data-enhancement layer that took a thin contact record (name, email, ZIP) and silently appended a much richer profile from public and licensed third-party data:</p>
  <ul>
    <li><strong>Geographic context</strong> &mdash; city, state, neighborhood, congressional district, state upper/lower district, metropolitan market, lat/long, and elected officials for the contact&rsquo;s address.</li>
    <li><strong>Social influence</strong> &mdash; social networks the contact belonged to, Klout score (this was 2012), network size, message amplification score.</li>
    <li><strong>Lifestyle &amp; interests</strong> &mdash; age, gender, marital status, home ownership and value, net worth, education, investments, credit-card type, magazine subscriptions, interest topics, charitable giving, employment.</li>
  </ul>
  <p>For a public-affairs client, that meant a one-line submitted petition could turn into a fully-attributed contact you could segment, target, and route to a lobby team within a single afternoon.</p>

  <h2>What a tenant actually looked like</h2>
  <p>Below: an admin&rsquo;s view of the Hilex client tenant, showing the Multiplier home dashboard &mdash; campaign tools across the top, an admin sidebar with all the action types Hilex had configured (Contacts, Emails, Campaigns, Reports, Forms, Petitions, Lobby Letters, Tell a Friend, Events, Social Advocacy, Messages, Websites), and a real-time dashboard of new members this week, lobby letters this week, and letters by action name.</p>

  <div class="gallery cols-2">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/multiplier/hero.webp"><img src="/img/projects/multiplier/hero.jpg" alt="Hilex tenant dashboard in Multiplier showing campaigns, new-members chart, lobby-letters gauge, and letters-by-action histogram"></picture>
      <figcaption class="gallery-caption">A client tenant&rsquo;s landing dashboard &mdash; configured for Hilex, a packaging-industry advocacy client.</figcaption>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/multiplier/record.webp"><img src="/img/projects/multiplier/record.jpg" alt="A contact record in Multiplier, showing the activity navigation strip and the start of the contact detail view — click to scroll the full record"></picture>
      <figcaption class="gallery-caption">A single contact&rsquo;s record. Click to scroll the full page top-to-bottom: email results, campaign history, lobby letter actions, tell-a-friend, petition signatures, custom advocate fields, score &amp; ranking, geocoded address. PII redacted.</figcaption>
    </figure>
  </div>

  <h2>The tech stack</h2>
  <p>Multiplier was a hybrid architecture &mdash; Salesforce for what Salesforce is good at (data, security, admin UI, reporting), and a custom Rackspace-hosted LAMP layer for everything Salesforce wasn&rsquo;t (public-facing forms, advanced custom UI, content rendering).</p>

  <ul>
    <li><strong>Force.com (Salesforce platform)</strong> &mdash; tenant data model, admin UI, reporting, data management, security, user permissions.</li>
    <li><strong>Rackspace Cloud Sites (PHP + MySQL, LAMP)</strong> &mdash; all public web requests, form rendering, embeddable assets for client CMSes, temporary data storage, advanced UI.</li>
    <li><strong>SOAP API</strong> bridge between the two layers, with batch processing in chunks of 200 records, triggered by cron on Rackspace.</li>
    <li><strong>Beanstalk Git</strong> for revision control, with four environments &mdash; local development &rarr; remote development &rarr; remote staging &rarr; production &mdash; mirrored across the Salesforce Sandbox &harr; Production split.</li>
    <li><strong>ExactTarget</strong> (now Salesforce Marketing Cloud) as the email-delivery partner for high-volume sends.</li>
  </ul>

  <h2>Case studies from the portfolio</h2>

  <h3>The Partnership &mdash; financial-services thought leadership on the DC Beltway</h3>
  <p>A financial-services-industry client wanted to build an email list of the Beltway&rsquo;s most influential individuals in financial services and engage them on key messages. Multiplier did the website-and-email integration that gave the team performance tracking from inbox to web page, the A/B-test reporting that improved content/subject-line response, and the Intelligence layer identified roughly <strong>10% of recipients as political donors</strong> &mdash; with party preference. The campaign tuned for senior Hill-staff readers (for the lobby team), industry promoters (for content sharing), and issue champions (for follow-on requests), and <strong>delivered results 5&times; industry standard</strong>.</p>

  <h3>Rogers Wireless &mdash; consumer launch buzz pivoting to advocacy</h3>
  <p>Rogers Wireless used Multiplier to build consumer buzz around a new product launch, then pivot the same database into advocacy work. The platform integrated website, advertising, and email behind a single contact store, tracked performance from digital ads &rarr; web page &rarr; inbox &rarr; in-store events, and used Intelligence to map regional customer and prospect densities &mdash; informing where to schedule in-store events.</p>

  <h3>PepsiCo &mdash; tracking the top 100 influencers</h3>
  <p>PepsiCo wanted to know what the most influential voices in its category were saying, increase positive coverage, and identify conversation trends. Multiplier built the <strong>Pepsi Top 100 Influencers</strong> list, monitored their conversations in real time, and gave the PepsiCo team a single dashboard for inserting Pepsi into the trends they wanted to ride &mdash; and course-correcting off-message Pepsi chatter. The work generated alerts across social and traditional media, fed into Multiplier&rsquo;s segmentation, and let PepsiCo pivot the same audience into other campaign actions.</p>

  <h3>Connect2Canada (C2C) &mdash; the Embassy of Canada&rsquo;s diaspora platform</h3>
  <p>The Embassy of Canada used Multiplier as its <em>Connect2Canada</em> member platform &mdash; a CRM for Canadians and Canada-watchers in the U.S. with custom fields for <strong>Contact Interest Areas</strong> (U.S.&ndash;Canada border, travel, trade &amp; investment), <strong>Interested Actions</strong> (&ldquo;spread the word,&rdquo; &ldquo;connect and socialize&rdquo;), <strong>Birth Province</strong>, and newsletter subscriptions (Canada Watch, Monitor, NewsCan). The Embassy ran trainings on the platform out of Washington, with on-call support from the Edelman team in Arlington.</p>

  <h3>HP, Hyundai, BlackBerry &mdash; the named-brand engagements</h3>
  <p>Inside Multiplier&rsquo;s tenant list were some of the largest corporate-communications deployments of the era: <strong>HP&rsquo;s HPNN</strong> internal news platform (commissioned by Meg Whitman during a period of rapid leadership change), <strong>Hyundai&rsquo;s 24-hour fuel-economy reimbursement tool</strong> (built ahead of an EPA hearing &mdash; visitors entered a VIN, the tool computed the MPG discrepancy factoring in state-specific fuel prices, and Hyundai offered 120% cash value as fair compensation), and <strong>BlackBerry RIM&rsquo;s B2G site</strong> for federal buyers. Each was a different shape; each ran on the same platform.</p>

  <h2>Training &amp; rollout</h2>
  <p>Selling and operating a platform like Multiplier internally required as much training as the technology did. The rollout ran on two layered tracks:</p>
  <ul>
    <li><strong>Edelman Ambassador&rsquo;s Training</strong> &mdash; a 2-day, internal-staff certification covering selling Multiplier, architecture, navigation, action creation, reporting/analytics, ExactTarget email, Intelligence appending capabilities, API access, social monitoring, and pricing. The first cohort included a Friday-afternoon ExactTarget session and an API/developer documentation deep-dive.</li>
    <li><strong>Client Training</strong> &mdash; half-day to full-day sessions for the client-side admins on a new tenant. Topics: navigating Multiplier, website integration, the client&rsquo;s custom actions and fields, reporting, sending emails, social monitoring. Recurring clients like the Embassy of Canada and ASCD received returning trainings as their teams turned over.</li>
  </ul>

  <h2>Why it mattered</h2>
  <blockquote>Edelman&rsquo;s largest client-facing technology investment to date.<span style="display:block;margin-top:.7rem;font-style:normal;font-size:.9rem;color:var(--ink-muted)">— Multiplier internal FAQ</span></blockquote>
  <p>Multiplier was the platform that let Edelman&rsquo;s public-affairs and consumer-marketing practices ship 60+ client tenants on the same architecture &mdash; with the data, advocacy, social, and intelligence capabilities those clients increasingly expected, without rebuilding the wheel for each engagement. It taught me, hands-on, how a services firm builds proprietary technology that earns its place at the center of client relationships rather than competing with them &mdash; and how to design a multi-tenant platform that scales by configuration, not custom development.</p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/google-grants-optimizer/"><span class="dir">&larr; Previous</span><span class="title">AI Google Ad Grant Optimizer</span></a>
    <a class="next" href="/projects/mlk-memorial/"><span class="dir">Next &rarr;</span><span class="title">MLK Jr. National Memorial</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/multiplier/index.html",
        title="Multiplier — Edelman's Engagement Tool — Matt Briney",
        description="A complete rebuild of Edelman's Grassroots Multiplier® into a modern multi-tenant engagement platform on Salesforce Force.com + Rackspace LAMP — 60+ client tenants including HP, Hyundai, BlackBerry, GE, Pepsi, Embassy of Canada, and the Episcopal Church.",
        active="projects",
        canonical="https://mattbriney.com/projects/multiplier/",
        og_image="/img/projects/multiplier/hero.jpg",
        body=BODY,
    )
