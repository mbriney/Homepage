BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study &middot; Theodore Roosevelt Presidential Library Foundation &middot; 2024–present</p>
    <h1>An AI-Driven Google Ad Grant Optimizer Pulling 16.46% Average CTR</h1>
    <p class="lede">Google gives qualifying non-profits up to <strong>$10,000 / month</strong> of free advertising through its Ad Grants program. Most institutions leave most of that money on the table because keeping a Grant account healthy at scale is a full-time job. I built one that runs itself &mdash; an AI optimizer that crawls our sitemap, builds and tests campaigns, talks to the Google Ads and Analytics APIs directly, and bids the budget for conversions every month.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Architect &amp; Operator</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">TRPL Foundation</span></div>
      <div class="meta-item"><span class="label">Stack</span><span class="value">Claude · Google Ads API · GA4 API</span></div>
      <div class="meta-item"><span class="label">Cadence</span><span class="value">Monthly, fully automated</span></div>
    </div>

    <div class="metric-hero">
      <div class="metric-big">
        <span class="num">16.46<span class="unit">%</span></span>
        <span class="lbl">Average click-through rate, sustained month over month.</span>
        <span class="sub">Peak month: <strong style="color:var(--gold)">25.78%</strong>. The Google Ad Grants program requires a 5% minimum.</span>
      </div>
      <div class="metric-chart" role="img" aria-label="Click-through rate comparison: industry average 3.17 percent, Grant minimum 5 percent, TRPL average 16.46 percent, TRPL peak 25.78 percent">
        <div class="bar-row">
          <span class="bar-label">Google Ads industry avg</span>
          <div class="bar"><div class="bar-fill" style="width: 12.3%"></div><span class="bar-val">3.17%</span></div>
        </div>
        <div class="bar-row">
          <span class="bar-label">Grant minimum (required)</span>
          <div class="bar"><div class="bar-fill" style="width: 19.4%"></div><span class="bar-val">5.00%</span></div>
        </div>
        <div class="bar-row">
          <span class="bar-label">TRPL Foundation &mdash; avg</span>
          <div class="bar"><div class="bar-fill bar-fill--accent" style="width: 63.8%"></div><span class="bar-val">16.46%</span></div>
        </div>
        <div class="bar-row">
          <span class="bar-label">TRPL Foundation &mdash; peak</span>
          <div class="bar"><div class="bar-fill bar-fill--gold" style="width: 100%"></div><span class="bar-val">25.78%</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Google&rsquo;s Ad Grants program is one of the most generous standing offers in non-profit funding: any eligible 501(c)(3) can use up to <strong>$10,000 a month of search advertising</strong>, free. The catch is that the account has to be actively maintained at a Google Ads professional&rsquo;s level of care &mdash; with a sustained click-through rate above 5%, ad groups under tight quality-score thresholds, conversion tracking wired into Analytics, and a steady drip of new keywords, ad copy, and tests. Most non-profits hire an agency, do it badly themselves, or quietly let the Grant lapse below 5% and lose the spend.</p>
  <p>I wanted the third path: turn the entire Grant operation into a once-a-month, push-button run that audits the account, finds the gaps, proposes a plan, and &mdash; after I approve &mdash; ships changes via API.</p>

  <h2>How it works</h2>
  <p>The optimizer runs as a Claude skill against a live Google Ads account. Every monthly run follows the same loop:</p>

  <div class="flow">
    <div class="flow-step">
      <h4>Crawl the sitemap</h4>
      <p>Pulls the institution&rsquo;s <code>sitemap.xml</code>, reads every public page, and infers the topical structure of the organization.</p>
    </div>
    <div class="flow-step">
      <h4>Discover campaigns</h4>
      <p>Maps content clusters to campaign &amp; ad-group structure. Surfaces topics the existing account is missing entirely.</p>
    </div>
    <div class="flow-step">
      <h4>Generate variants</h4>
      <p>Drafts headline and description variants per ad group, anchored to the page they point at and tuned for Grant compliance.</p>
    </div>
    <div class="flow-step">
      <h4>Pull live performance</h4>
      <p>Reads click, impression, CTR, conversion, and cost data live from the Google Ads API &mdash; plus engagement and revenue from the GA4 API.</p>
    </div>
    <div class="flow-step">
      <h4>Audit &amp; plan</h4>
      <p>Cross-checks the account against the Grant compliance rules, identifies under-performers, and proposes a change plan in a human-readable report.</p>
    </div>
    <div class="flow-step">
      <h4>Approve &amp; execute</h4>
      <p>After I sign off on the plan, the optimizer writes the changes back to Google Ads via API mutations &mdash; no CSV exports, no Ads Editor, no manual edits.</p>
    </div>
  </div>

  <h2>What it actually does, in detail</h2>

  <h3>Sitemap-driven campaign discovery</h3>
  <p>The traditional Google Ads workflow starts with a marketer guessing what their organization does and writing campaigns from intuition. This one starts with the institution&rsquo;s actual website. Every page that gets discovered in the sitemap is a candidate landing destination; every cluster of related pages becomes a candidate campaign. New content that ships during the month gets picked up automatically on the next run.</p>

  <h3>Ad-unit variants, automatically A/B tested</h3>
  <p>For every ad group, the optimizer ships at least three responsive search-ad variants &mdash; varying headlines, descriptions, and call-to-action phrasing. Google&rsquo;s own ad-rotation handles serving; the optimizer watches the results in the next run and prunes anything underperforming relative to peers in the same ad group, then drafts replacements. This is a continuous A+B loop, not a one-time setup.</p>

  <h3>Direct API integration</h3>
  <p>Earlier versions of this kind of workflow ran on CSV exports through the Google Ads Editor desktop app &mdash; brittle, manual, easy to break. This one talks to the <strong>Google Ads API</strong> and the <strong>Google Analytics Data API (GA4)</strong> directly. Every read is live; every change is a programmatic mutation; every run is auditable.</p>

  <h3>Conversion- and revenue-aware bidding</h3>
  <p>Because the GA4 API is wired in, the optimizer can see what visitors do after they click &mdash; donations, ticketing flows, newsletter signups, content engagement. Budget shifts toward the campaigns and keywords that actually convert, not just the ones with the highest CTR.</p>

  <h3>Grant compliance, automated</h3>
  <p>Google enforces specific rules on Ad Grant accounts: minimum CTR thresholds, geo-targeting requirements, prohibited single-word and overly generic keywords, mandatory conversion tracking, two ads per group, two ad groups per campaign, and so on. The optimizer treats those rules as first-class constraints &mdash; every plan it proposes is pre-validated against them.</p>

  <h2>Results</h2>
  <div class="case-stats-row">
    <div class="case-stat"><strong>16.46%</strong><span>average CTR (vs. 5% Grant minimum)</span></div>
    <div class="case-stat"><strong>25.78%</strong><span>peak monthly CTR</span></div>
    <div class="case-stat"><strong>5&times;</strong><span>industry-average performance</span></div>
    <div class="case-stat"><strong>$10K/mo</strong><span>Grant budget, fully deployed</span></div>
  </div>
  <p>The numbers do the talking. The TRPL Foundation&rsquo;s Ad Grant account has sustained an average <strong>16.46% CTR</strong> across all campaigns &mdash; <strong>more than 3&times; the Grant minimum and roughly 5&times; the industry average</strong> for Google Ads broadly. The best month hit <strong>25.78%</strong>. And because the optimizer is bidding for the available spend each cycle, the Foundation is actually <em>using</em> the Grant rather than letting it sit idle.</p>

  <blockquote>The point of an Ad Grant isn&rsquo;t the badge &mdash; it&rsquo;s the donors, the readers, the ticket buyers, and the researchers it puts in front of your work. An automated optimizer is what turns a passive line on the budget into an active acquisition channel.</blockquote>

  <h2>Why I built it</h2>
  <p>The Theodore Roosevelt Presidential Library is opening from a standing start. Every channel we build now &mdash; email, social, web, ads &mdash; has to be a long-term capability, not a one-off launch. Hiring an agency for the Grant would have meant the work happens at someone else&rsquo;s pace, on someone else&rsquo;s clock, with reporting we don&rsquo;t fully own. Building the optimizer meant the institution&rsquo;s acquisition channel is something we run ourselves, in an afternoon a month, with all the data and all the decisions inside the building.</p>
  <p>It&rsquo;s also a working argument for what I think AI in non-profit operations should actually look like: an agent that reads your real data, proposes a real plan, and only executes after you approve. Not a chatbot, not a content generator &mdash; an analyst-and-operator that compounds your monthly capacity.</p>

  <h2>What&rsquo;s next</h2>
  <ul>
    <li>Open the optimizer to other Library Foundation programs and other cultural-institution non-profits as a packaged Claude skill.</li>
    <li>Extend the same architecture to paid search (beyond Grants), Meta, and audience-platform CRM &mdash; the same sitemap-driven, conversion-aware loop.</li>
    <li>Plug in the Library&rsquo;s eventual ticketing and membership conversion events so the bidding is steering toward institutional revenue, not just web events.</li>
  </ul>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/trpl-reading-room/"><span class="dir">&larr; Previous</span><span class="title">TRPL Reading Room</span></a>
    <a class="next" href="/projects/multiplier/"><span class="dir">Next &rarr;</span><span class="title">Multiplier</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/google-grants-optimizer/index.html",
        title="AI-Driven Google Ad Grant Optimizer — Matt Briney",
        description="An AI optimizer for the TRPL Foundation's $10K/month Google Ad Grant. Crawls the sitemap, builds and tests campaigns, talks to the Google Ads & GA4 APIs directly, and sustains a 16.46% average click-through rate (peak 25.78%) — more than 3× the Grant minimum.",
        active="projects",
        canonical="https://mattbriney.com/projects/google-grants-optimizer/",
        body=BODY,
    )
