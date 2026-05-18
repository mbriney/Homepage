BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study &middot; Emotive &middot; 2008&ndash;2010</p>
    <h1>The Pickens Plan: Marketing Infrastructure for a $58M Self-Funded Energy Campaign</h1>
    <p class="lede">In July 2008, Texas oil billionaire T. Boone Pickens spent his own money on a national grassroots campaign to wean the U.S. off OPEC oil &mdash; wind farms, natural gas vehicles, a 21st-century grid. Emotive built and operated the marketing infrastructure underneath it: the CRM, the petition platform, the live-streaming stack for nationwide town halls, the social presence, the email program, and the daily reporting that kept it all aligned with the broadcast media flights &mdash; including the Super Bowl XLIII ad placement that put pickensplan.com in front of 95 million viewers in a single evening.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Senior Account Director (digital infrastructure lead)</span></div>
      <div class="meta-item"><span class="label">Client</span><span class="value">T. Boone Pickens &middot; Pickens Plan</span></div>
      <div class="meta-item"><span class="label">Launched</span><span class="value">July 8, 2008</span></div>
      <div class="meta-item"><span class="label">Media spend</span><span class="value">$58M self-funded</span></div>
      <div class="meta-item"><span class="label">Movement</span><span class="value">3M+ members in &ldquo;Pickens Army&rdquo;</span></div>
      <div class="meta-item"><span class="label">Marquee placement</span><span class="value">Super Bowl XLIII, Feb 1, 2009</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/pickens-plan/hero.webp">
        <img src="/img/projects/pickens-plan/hero.jpg" alt="Pickens Plan logo on the campaign&rsquo;s signature sky-blue brand color" width="1600" height="900">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Pickens had a thesis: America was sending nearly $700&nbsp;billion a year to OPEC for imported oil, and that money &mdash; the largest transfer of wealth in human history, in his telling &mdash; was killing the economy, distorting foreign policy, and starving the domestic energy infrastructure that could replace it. He proposed using domestic natural gas as a transportation bridge fuel, building out the largest wind power deployment in U.S. history, and modernizing the electrical grid. He also proposed paying for the campaign himself.</p>

  <p>What he needed was the apparatus around him: somewhere for the millions of people who would see his face on TV to land, sign their name, learn the plan, be reactivated week after week, show up to town halls, watch the next event live, and contact their elected officials. That apparatus was Emotive&rsquo;s job.</p>

  <div class="case-stats-row">
    <div class="case-stat"><strong>$58M</strong><span>self-funded media spend</span></div>
    <div class="case-stat"><strong>3M+</strong><span>Pickens Army members</span></div>
    <div class="case-stat"><strong>1.6M</strong><span>signatures by end of year 1</span></div>
    <div class="case-stat"><strong>95M</strong><span>Super Bowl XLIII reach in one night</span></div>
  </div>

  <h2>Watch the spot</h2>
  <div class="film" id="launch-ad">
    <div class="film-video">
      <iframe src="https://www.youtube-nocookie.com/embed/R2bOug1d20c" title="T. Boone Pickens TV Commercial — Pickens Plan launch" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <div class="film-body">
      <div class="film-head">
        <h3 class="film-title">&ldquo;I&rsquo;ve been an oil man my whole life, but this is one emergency we can&rsquo;t drill our way out of.&rdquo;</h3>
        <span class="film-meta">1:02 &middot; launch spot, July 2008</span>
      </div>
      <p class="film-tagline">The 60-second commercial that announced the Pickens Plan. A 30-second cutdown of this same campaign ran during Super Bowl XLIII the following February. Every airing sent traffic to pickensplan.com.</p>
    </div>
  </div>

  <h2>What we built</h2>

  <h3>The CRM &mdash; the &ldquo;Pickens Army&rdquo; database</h3>
  <p>The single most important piece of infrastructure was the one nobody outside the campaign ever saw: the member database. Every televised mention of pickensplan.com pushed people to a sign-up form. The CRM had to ingest the surge during a TV flight, deduplicate, geocode by ZIP to a U.S. congressional district, segment by state and topic interest, and then expose all of that for downstream activation. By the end of 2008 it held the records of more than one million signed-up members. By the end of 2009, more than 1.6 million. Pickens&rsquo;s own published count reached over three million all-time.</p>

  <h3>The petition &amp; activist platform</h3>
  <p>Membership was the top of the funnel; <em>contact your representative</em> was the political payoff. The platform routed members&rsquo; petition signatures and follow-on advocacy actions to the correct congressional and senate offices &mdash; by district, in real time &mdash; and reported back to the campaign on which districts were activating, where coverage was thin, and where Pickens should consider scheduling a town hall next. By the end of the campaign, two U.S. senators, 37 U.S. representatives, and nine governors had publicly pledged support.</p>

  <h3>Live streaming for the town hall tour</h3>
  <p>Pickens crisscrossed the country with town halls and educational sessions for lawmakers. We built the live-streaming stack that broadcast those events out of arenas, university auditoriums, and statehouse rooms to the members who couldn&rsquo;t be there in person &mdash; with chat, Q&amp;A capture, registration walls, and post-event email follow-ups tied back to who actually attended. Live streaming a town hall to tens of thousands of geographically-dispersed members in 2008&ndash;2009 was a technical lift; we made it look routine.</p>

  <h3>Social: Facebook, Twitter, and the @PickensPlan YouTube channel</h3>
  <p>The PickensPlan presence on social was operated as a daily newsroom. The YouTube channel hosted the launch spot, the second 30-second cutdown, the natural-gas spot, and dozens of follow-on videos &mdash; town hall clips, lawmaker meetings, &ldquo;Meet the Army&rdquo; profiles of state-level captains. Twitter ran live during every televised appearance and every town hall. Facebook hosted the longest-tail community conversation, where state leaders coordinated their own local activity. The launch ad alone has been viewed more than 130,000 times on YouTube since.</p>

  <h3>Email: the daily reactivation channel</h3>
  <p>If TV brought people in, email kept them. We built and operated a high-volume email program with weekly newsletters from Boone himself, urgent action alerts timed to legislative votes, town hall RSVPs, fundraising appeals, and segmented re-engagement flows for members who&rsquo;d stopped opening. Lists were sliced by congressional district, by interest (wind / natural gas / efficiency / policy), and by engagement tier &mdash; so the right member got the right ask at the right moment.</p>

  <h3>Reporting tied to broadcast flights</h3>
  <p>The campaign was running cable, network, and digital ad flights at the same time as town halls, social posts, and major-media appearances on <em>The NewsHour with Jim Lehrer</em>, <em>Good Morning America</em>, <em>The Tonight Show with Jay Leno</em>, <em>Larry King Live</em>, <em>Fox News</em>, and <em>The Daily Show with Jon Stewart</em>. We built a reporting layer that correlated sign-ups, petition signatures, video views, and email engagement back to specific broadcast flights and specific airings &mdash; so we could tell the campaign, the morning after, exactly which spot, which appearance, and which time slot had moved the most people.</p>

  <h2>T. Boone explains the plan</h2>
  <div class="film" id="whiteboard">
    <div class="film-video">
      <iframe src="https://www.youtube-nocookie.com/embed/iUfGokx2Ulk" title="T. Boone Pickens — full whiteboard presentation of the Pickens Plan" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <div class="film-body">
      <div class="film-head">
        <h3 class="film-title">The whiteboard presentation</h3>
        <span class="film-meta">10:37 &middot; @PickensPlan, Sept 2010</span>
      </div>
      <p class="film-tagline">Boone&rsquo;s full whiteboard walk-through of the plan: the import slope from 24%&rarr;42%&rarr;70%, the $700B annual transfer of wealth, why the U.S. has the best wind quarter in the world, and the natural-gas-for-transportation pivot that would cut foreign oil imports by 38%. This was the substance under all the marketing infrastructure we built.</p>
    </div>
  </div>

  <h2>The Super Bowl moment</h2>
  <p>Super Bowl XLIII, February 1, 2009. Steelers vs. Cardinals, watched by an estimated 95 million Americans on a single Sunday evening. Pickens bought into the rotation, and pickensplan.com had to be ready to absorb the resulting spike. We pre-scaled the registration system, the email queue, and the database write paths days in advance, monitored live during and after the broadcast, and absorbed the surge cleanly. That single airing was the single biggest sign-up day of the campaign &mdash; and the playbook for how to scale a marketing stack ahead of a megabudget broadcast moment is something I&rsquo;ve carried into every campaign infrastructure project since.</p>

  <h2>A cross-ideological coalition</h2>
  <p>One of the more remarkable things about the Pickens Plan, given who Pickens was, is that it built a coalition that included the <a href="https://www.sierraclub.org/" target="_blank" rel="noopener">Sierra Club</a>, the <a href="https://www.lung.org/" target="_blank" rel="noopener">American Lung Association</a>, and the <a href="https://www.americanprogress.org/" target="_blank" rel="noopener">Center for American Progress</a> alongside oil-and-gas allies. The digital infrastructure had to serve all of them &mdash; advocacy actions co-signed by environmental groups, member content speaking to natural-gas industry stakeholders, town hall guests ranging from wind-power developers to Detroit truck-fleet operators &mdash; without fracturing the message. The CRM did the segmentation; the email and social platforms did the personalization; the reporting kept everyone honest about what was working.</p>

  <h2>What we learned</h2>
  <ul>
    <li><strong>A megabudget TV spend is only as good as the digital surface it lands on.</strong> $58M in broadcast media generates demand. If the pipe between the ad and the database is too small, you lose the conversion. The pre-flight scale-up before Super Bowl XLIII was as strategically important as the ad creative itself.</li>
    <li><strong>Geocoding by congressional district is a force multiplier.</strong> The moment a sign-up becomes routable to a district, the campaign can convert membership into political pressure on the right office. That single feature did more for the campaign&rsquo;s policy goals than any single broadcast flight.</li>
    <li><strong>The reporting is the steering wheel.</strong> Same-morning attribution from broadcast flight to sign-up surge meant the campaign could move money between media buys, town halls, and email cadence in days instead of weeks.</li>
    <li><strong>One database is not a CRM &mdash; the operating model around it is.</strong> The Pickens Army was meaningful because the apparatus around the database (advocacy, email, live streaming, reporting) treated every member as a person to be reactivated, not a row to be counted.</li>
  </ul>

  <h2>Why it mattered</h2>
  <blockquote>The single biggest sign-up day of the campaign was the Sunday of the Super Bowl. The infrastructure on the other side of that URL had to absorb the moment, hold the line, and convert the surge into a movement the morning after.</blockquote>
  <p>The Pickens Plan didn&rsquo;t end the way Pickens hoped &mdash; the Texas wind farm was cancelled in 2009 as natural gas prices collapsed, and the plan&rsquo;s political momentum cooled in 2010. But the digital infrastructure underneath it &mdash; the CRM, the petition platform, the streaming stack, the email program, the broadcast-aligned reporting &mdash; was a working blueprint for how to run a self-funded, megabudget, national policy campaign in the social-media era. Emotive built and operated all of it, and the muscle memory of pre-scaling for the Super Bowl spike, segmenting a multimillion-member list by congressional district, and reporting attribution back to specific TV airings became part of how I&rsquo;ve thought about campaign architecture ever since.</p>

  <p class="muted" style="margin-top:2rem;font-size:.9rem;">References: <a href="https://pickensplan.com/" target="_blank" rel="noopener">pickensplan.com</a> &middot; <a href="https://pickensplan.com/about/index.html" target="_blank" rel="noopener">About the Pickens Plan</a> &middot; <a href="https://pickensplan.com/the-plan/index.html" target="_blank" rel="noopener">The Plan</a> &middot; <a href="https://en.wikipedia.org/wiki/Pickens_Plan" target="_blank" rel="noopener">Wikipedia &mdash; Pickens Plan</a> &middot; <a href="https://www.youtube.com/@pickensplan" target="_blank" rel="noopener">@PickensPlan on YouTube</a></p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/mlk-memorial/"><span class="dir">&larr; Previous</span><span class="title">MLK Jr. National Memorial</span></a>
    <a class="next" href="/projects/travel-passport/"><span class="dir">Next &rarr;</span><span class="title">Travel Passport</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/pickens-plan/index.html",
        title="Pickens Plan — Marketing Infrastructure for a $58M Self-Funded Energy Campaign — Matt Briney",
        description="How Emotive built and operated the CRM, petition platform, live-streaming stack, social presence, email program, and broadcast-aligned reporting for T. Boone Pickens' $58M Pickens Plan campaign — including the Super Bowl XLIII ad placement that drove the single biggest sign-up day of the campaign.",
        active="projects",
        canonical="https://mattbriney.com/projects/pickens-plan/",
        og_image="/img/projects/pickens-plan/hero.jpg",
        body=BODY,
    )
