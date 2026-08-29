BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Theodore Roosevelt Presidential Library · 2024&ndash;present</p>
    <h1>From Reading Room to Campfire: Three Years of AI at a Presidential Library</h1>
    <p class="lede">It began as a way to ask a presidential library a question in plain language. It shipped as <a href="https://campfire.trlibrary.com" target="_blank" rel="noopener">Campfire</a>, grounded in 58,000 primary sources. Then it walked out of the browser and into a gallery, where visitors talk to Theodore Roosevelt &mdash; and where, on the day the Library was dedicated, the President of the United States stopped to do exactly that.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Chief Communications &amp; Marketing Officer</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">Theodore Roosevelt Presidential Library</span></div>
      <div class="meta-item"><span class="label">Years</span><span class="value">2024&ndash;present</span></div>
      <div class="meta-item"><span class="label">Stack</span><span class="value">Retrieval over 58,000 digitized sources · four visitor modes · in-gallery installation</span></div>
      <div class="meta-item"><span class="label">Status</span><span class="value">Live in production</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/tr-llm/hero.webp">
        <img src="/img/projects/tr-llm/hero.jpg" alt="The Reading Room &mdash; Discover the life &amp; legacy of Theodore Roosevelt" width="1600" height="856">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Cultural institutions sit on enormous, under-indexed collections: letters, speeches, photographs, ephemera. Finding the right object has historically required knowing the finding aid &mdash; an archivist&rsquo;s skill, not a visitor&rsquo;s. The job: lower that bar from <em>&ldquo;know the finding aid&rdquo;</em> to <em>&ldquo;ask a question.&rdquo;</em></p>
  <p>What made it hard was never getting an answer. It was getting an answer a presidential library is willing to stand behind.</p>

  <div class="case-stats-row">
    <div class="case-stat"><strong>58,000</strong><span>Primary sources indexed</span></div>
    <div class="case-stat"><strong>87.6%</strong><span>Groundedness score</span></div>
    <div class="case-stat"><strong>8.4</strong><span>Citations per answer</span></div>
    <div class="case-stat"><strong>4</strong><span>Visitor modes</span></div>
  </div>

  <h2>2024 &mdash; The Reading Room</h2>
  <p>The first version was a public interface to the collection. A student, a teacher, a researcher, or a curious citizen could pick from prompts &mdash; <em>I want to do research, find images, build a lesson plan, write a paper, test my knowledge</em> &mdash; or type their own question, or start from a topic: the Square Deal, the Rough Riders, antitrust, the Bull Moose party, the books TR wrote.</p>
  <p>The AI did the retrieval, summarization and synthesis, but always pointed back to the underlying primary source. No hallucinated quotes, no fabricated dates, no paraphrase masquerading as Roosevelt&rsquo;s voice.</p>

  <h2>2026 &mdash; Campfire</h2>
  <p>The rename happened for a reason. &ldquo;Reading room&rdquo; describes a place where you are quiet and alone with documents. What the tool actually does is closer to sitting at a fire while somebody who knows the material tells you about it &mdash; and answers when you interrupt. The name change followed the product.</p>
  <p>Live now at <a href="https://campfire.trlibrary.com" target="_blank" rel="noopener">campfire.trlibrary.com</a>, it added:</p>
  <ul>
    <li><strong>Four modes</strong> &mdash; Discovery, Research, For Teachers, For Students. Same collection, same rules, different register.</li>
    <li><strong>Voice input</strong>, so the barrier is speaking rather than typing.</li>
    <li><strong>Scaffolded prompts</strong> for people who don&rsquo;t know what to ask: <em>Tell me a story · Do research · Build a lesson plan · Help with homework</em>.</li>
    <li><strong>&ldquo;How we use Artificial Intelligence&rdquo; and &ldquo;Report an Issue&rdquo;</strong> as first-class navigation, not footer links.</li>
  </ul>
  <p class="muted" style="margin-top:-.4rem">A naming note: the Library&rsquo;s opening-weekend program was also called <a href="https://www.trlibrary.com/video/playlist/PLIEjRP2NQLiA" target="_blank" rel="noopener">Campfire &amp; Prairie Talks</a>. Same metaphor, deliberately &mdash; different thing.</p>

  <div class="gallery cols-2">
    <figure>
      <picture>
        <source type="image/webp" srcset="/img/projects/tr-llm/01.webp">
        <img src="/img/projects/tr-llm/01.jpg" alt="A campfire at the Elkhorn Ranch site in the North Dakota Badlands" loading="lazy" width="1600" height="900">
      </picture>
      <figcaption class="gallery-caption">The metaphor the product was renamed for: not a reading room, a campfire.</figcaption>
    </figure>
    <figure>
      <picture>
        <source type="image/webp" srcset="/img/projects/tr-llm/02.webp">
        <img src="/img/projects/tr-llm/02.jpg" alt="Detail of an artifact from the Theodore Roosevelt Presidential Library collection" loading="lazy" width="1600" height="900">
      </picture>
      <figcaption class="gallery-caption">Every answer resolves to an object like this one, with a link back to the record.</figcaption>
    </figure>
  </div>

  <h2>Designed around scholarly trust</h2>
  <p>Four decisions did most of the work, and all four are about what the system <em>refuses</em> to do.</p>

  <h3>It cites, and the citations are real</h3>
  <p>Answers average <strong>8.4 citations</strong>, and each one carries the creator, recipient, date, collection, repository and a permalink to the source record. Where a field in the underlying catalogue was machine-generated rather than written by a human archivist, the record says so. An institution that publishes AI-assisted metadata without labelling it is quietly degrading its own catalogue; labelling it costs nothing and preserves the distinction permanently.</p>

  <h3>It does not fall back on general knowledge</h3>
  <p>If retrieval returns nothing relevant, the system does not answer from the model&rsquo;s own training. It says it found nothing and asks for clarification. That is a deliberate constraint, and it is the single most important one: a museum-branded assistant that quietly answers from the open web is no longer a collections tool, it is a chatbot wearing a museum&rsquo;s logo.</p>

  <h3>It knows Roosevelt died in 1919</h3>
  <p>The most common failure mode for a historical-figure AI is the anachronism question &mdash; <em>what would TR think about social media, about this election, about climate policy?</em> The tempting answer is a plausible-sounding extrapolation. The correct answer is that Roosevelt died on January&nbsp;6, 1919, and cannot have had a view.</p>
  <p>Adding that single rule moved abstention on temporal-impossibility tests <strong>from roughly 60% to 100%</strong>. One paragraph of instruction, and the system stopped inventing the opinions of a dead president.</p>

  <h3>The modes change the voice, not the retrieval</h3>
  <p>Discovery, Research, For Teachers and For Students adjust tone and reading level. They do <em>not</em> touch the retrieval, the scope check, or the fact-checking stage &mdash; so a student and a scholar asking the same question get the same sources and the same groundedness standard, in different registers. The alternative, where a &ldquo;kids mode&rdquo; quietly relaxes the evidentiary bar, is how institutions end up teaching children things they would not print.</p>

  <blockquote>The hard part of AI in a cultural-heritage setting isn&rsquo;t getting an answer. It&rsquo;s getting an answer the institution is willing to stand behind.</blockquote>

  <h2>Built with curators, not around them</h2>
  <p>The collections and curatorial teams were partners from day one, with authority over what the tool will and won&rsquo;t address. The editorial posture on difficult history came from the Library&rsquo;s own leadership, and it is not the defensive one: respond like a college professor, challenge the question, include the viewpoints and the norms of the period, don&rsquo;t defend a side, and present the material so the reader can reach their own conclusion.</p>
  <p>That is harder to build than a system that simply refuses to discuss Roosevelt&rsquo;s record on race and empire. It is also the only version worth having at a presidential library.</p>
  <p>One thing the corpus taught us: the collection is far stranger and better than a catalogue suggests. It holds roughly a hundred kinds of object &mdash; letters and telegrams, essays, speeches, sheet music, diary entries, even napkins. Among them is Roosevelt&rsquo;s diary entry for the day his wife and his mother died in the same house, which reads, in full, as a single large <strong>X</strong>. No summarization improves on that. The system&rsquo;s job is to put you in front of it.</p>

  <h2>What the evaluation showed</h2>
  <p>The system is measured rather than asserted, against a fixed test set with published baselines:</p>
  <ul>
    <li><strong>87.6% groundedness</strong> &mdash; answers supported by the retrieved sources.</li>
    <li><strong>85.7% correctness</strong> across a 252-question history quiz.</li>
    <li><strong>83% abstention</strong> on out-of-scope questions, with a tracked baseline run reaching <strong>100%</strong> on a 50-question set.</li>
    <li><strong>8.4 citations</strong> per answer on average.</li>
  </ul>
  <p>The number that matters most to me is the abstention rate, because it measures the thing a library can actually be embarrassed by. And the evaluation is reproducible by an outside party: <a href="https://www.microsoft.com/en-us/research/group/ai-for-good-research-lab/" target="_blank" rel="noopener">Microsoft&rsquo;s AI for Good Lab</a>, a partner on the project, can re-run the suite against the published baselines. Responsible-AI claims that only the vendor can verify are marketing.</p>

  <div class="gallery cols-1">
    <figure>
      <picture>
        <source type="image/webp" srcset="/img/projects/tr-llm/03.webp">
        <img src="/img/projects/tr-llm/03.jpg" alt="Visitors inside the Theodore Roosevelt Presidential Library galleries" loading="lazy" width="1600" height="900">
      </picture>
      <figcaption class="gallery-caption">The galleries. The same system that answers a question in a browser answers one out loud in the building.</figcaption>
    </figure>
  </div>

  <h2>Off the screen: AI TR in the gallery</h2>
  <p>The step that changed the project&rsquo;s public profile was moving it off the web. In the permanent exhibition, visitors hold a spoken conversation with Theodore Roosevelt &mdash; the same grounded retrieval, the same refusal to speculate past 1919, delivered as a person in a room rather than text in a box.</p>
  <p>It became the most-covered single feature of the opening. <em>Forbes</em> ran &ldquo;<a href="https://www.forbes.com/sites/lesliekatz/2026/07/01/ai-powered-theodore-roosevelt-is-ready-to-answer-your-questions/" target="_blank" rel="noopener">AI-Powered Theodore Roosevelt Is Ready To Answer Your Questions</a>.&rdquo; When the President spoke with it during the <a href="/projects/trpl-grand-opening-media/">dedication tour</a>, <a href="https://thehill.com/homenews/administration/5950575-trump-ai-teddy-roosevelt-chat/" target="_blank" rel="noopener"><em>The Hill</em></a> and <a href="https://newrepublic.com/post/212650/donald-trump-teddy-roosevelt-ai-conversation" target="_blank" rel="noopener"><em>The New Republic</em></a> both covered it &mdash; the latter under the headline &ldquo;People Think Trump Hallucinated Teddy Roosevelt. The Truth Is Weirder.&rdquo; A science-ethics publication used the exhibit to ask whether <a href="https://www.acsh.org/news/2026/07/10/talking-dead-ethical-50222" target="_blank" rel="noopener">talking with the dead is ethical at all</a>.</p>
  <p>That last one is the fair question, and the reason the guardrails were built first. An institution that animates a historical figure takes on a duty not to put words in his mouth. Every constraint above &mdash; cite or say nothing, never fall back on general knowledge, never speculate past the date of death &mdash; exists so that the answer to &ldquo;is this ethical?&rdquo; can be something more substantial than &ldquo;we were careful.&rdquo;</p>

  <h2>What I&rsquo;d carry forward</h2>
  <ul>
    <li><strong>Constrain first, capability second.</strong> Every impressive thing this system does is downstream of something it was forbidden to do.</li>
    <li><strong>Abstention is a feature you have to measure.</strong> Nobody ships a dashboard for &ldquo;questions we correctly declined,&rdquo; and it is the metric most likely to save you.</li>
    <li><strong>Label machine-generated metadata permanently.</strong> The distinction between what an archivist wrote and what a model inferred is impossible to reconstruct later.</li>
    <li><strong>Let an outside party re-run your evaluation.</strong> Otherwise your responsible-AI posture is a press release.</li>
    <li><strong>Name things after what they do.</strong> &ldquo;Reading Room&rdquo; described a building. &ldquo;Campfire&rdquo; describes the experience, and the rename clarified the roadmap as much as the marketing.</li>
  </ul>

  <h2>Why it matters</h2>
  <blockquote>The bar for &ldquo;research at a presidential library&rdquo; should be a question, not a finding aid.</blockquote>
  <p>The Library opened with this live on day one, in the browser and in the building. It is a working model for conversational AI at an institution that is serious about accessibility and scholarly integrity at the same time &mdash; and a demonstration that the second one is achievable if you are willing to let the system say &ldquo;I don&rsquo;t know.&rdquo;</p>

  <p class="muted">Try it: <a href="https://campfire.trlibrary.com" target="_blank" rel="noopener">campfire.trlibrary.com</a> · Related: <a href="/projects/trpl-grand-opening-media/">the media campaign that made it a national story</a> · <a href="/projects/google-grants-optimizer/">AI in the Google Ad Grant</a></p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/democracy-symposium/"><span class="dir">&larr; Previous</span><span class="title">Democracy Symposium</span></a>
    <a class="next" href="/projects/annual-reports/"><span class="dir">Next &rarr;</span><span class="title">A Tale of Two Annual Reports</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/trpl-reading-room/index.html",
        title="From Reading Room to Campfire: AI at a Presidential Library — Matt Briney",
        description="Three years of AI at the Theodore Roosevelt Presidential Library: grounded retrieval over 58,000 primary sources, 87.6% groundedness, and an in-gallery AI Roosevelt that became national news.",
        active="projects",
        canonical="https://mattbriney.com/projects/trpl-reading-room/",
        og_image="/img/projects/tr-llm/hero.jpg",
        body=BODY,
    )
