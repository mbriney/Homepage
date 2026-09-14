BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Theodore Roosevelt Presidential Library · 2024&ndash;present</p>
    <h1>The Living Library: AI-Driven Access to a Presidential Library&rsquo;s Collections</h1>
    <p class="lede">Theodore Roosevelt&rsquo;s papers sit scattered across more than forty repositories &mdash; partially catalogued, and reachable in practice only by specialists willing to travel and navigate archival finding aids. This is the work of lowering that bar to a question asked in plain language: a governed corpus of roughly 300,000 records, a researcher-facing interface called <a href="https://campfire.trlibrary.com" target="_blank" rel="noopener">Campfire</a>, and an exhibit where visitors speak with Roosevelt himself. The framework behind it &mdash; <a href="http://labs.trlibrary.com/living-library" target="_blank" rel="noopener">the Living Library</a> &mdash; is now published, and I&rsquo;m a co-author.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Chief Communications &amp; Marketing Officer</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">Theodore Roosevelt Presidential Library</span></div>
      <div class="meta-item"><span class="label">Years</span><span class="value">2024&ndash;present</span></div>
      <div class="meta-item"><span class="label">Stack</span><span class="value">Four-layer framework &middot; ~300,000-record governed corpus &middot; hybrid dense/semantic retrieval &middot; in-gallery digital human</span></div>
      <div class="meta-item"><span class="label">Published</span><span class="value">arXiv:2609.09368 &middot; co-author</span></div>
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
  <p>The access problem is the whole point, and it is not unique to Roosevelt. Most cultural institutions hold collections that are technically public and practically unreachable: catalogued to different standards, split across repositories, and searchable only by people who already know what they are looking for. A conversational interface is not the achievement. The achievement is a corpus governed well enough that a conversational interface can be pointed at it without embarrassing the institution.</p>

  <div class="case-stats-row">
    <div class="case-stat"><strong>~300,000</strong><span>Records in the governed corpus</span></div>
    <div class="case-stat"><strong>40+</strong><span>Repositories aggregated</span></div>
    <div class="case-stat"><strong>87.6%</strong><span>Groundedness score</span></div>
    <div class="case-stat"><strong>2.80s</strong><span>Mean response, in gallery</span></div>
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

  <h2>The framework: four layers</h2>
  <p>What started as one institution&rsquo;s tool turned out to generalize, and the published framework describes it as four layers &mdash; each independently useful, and each one a place another institution could reasonably stop.</p>
  <ol>
    <li><strong>Digitization and corpus creation.</strong> Material moves into institution-controlled storage with source identifiers and rights metadata preserved. The institution owns the corpus; that is not a detail.</li>
    <li><strong>AI-powered processing.</strong> OCR and structured metadata enrichment, with original metadata kept immutable and separate from anything a model generated. Curators correct machine output in place through the <strong>Archivist App</strong>.</li>
    <li><strong>Retrieval and reasoning.</strong> A hybrid dense/semantic index over the governed corpus. This is the layer that produces <strong>Campfire</strong>, the researcher-facing interface &mdash; and the layer where most of the public value actually lives.</li>
    <li><strong>An embodied conversational interface &mdash; optional.</strong> Voice, avatar, physical presence. This produces <strong>Talk to TR</strong> in the permanent exhibition.</li>
  </ol>
  <p>The fourth layer is the one that gets photographed, and it is the one I would tell a peer institution to skip first. Stop after layer three and you still have the thing that matters: a collection your visitors can actually ask questions of. The avatar is a choice about audience and budget, not a prerequisite for access.</p>

  <h2>The governance inversion</h2>
  <p>The part I expect to age best is not a model decision at all. Traditional archival workflow gatekeeps: nothing publishes until a human has reviewed it, which is why enormous quantities of digitized material sit unreachable for years waiting on staff time that will never exist.</p>
  <p>The Living Library inverts it. Records publish continuously to the index, each one carrying its review status and its OCR confidence score alongside it. Curators exercise quality control through <em>correction</em> rather than through <em>permission</em>. Access starts immediately and improves continuously, instead of waiting for a completeness that never arrives.</p>
  <p>That only works because the provenance labelling is rigorous &mdash; a record openly says what a machine produced and what an archivist verified. Take the labelling away and this becomes a way to quietly launder machine output into a scholarly catalogue.</p>

  <h2>Designed around scholarly trust</h2>
  <p>Four decisions did most of the work, and all four are about what the system <em>refuses</em> to do.</p>

  <h3>It cites, and the citations are real</h3>
  <p>Answers average <strong>8.4 citations</strong>, and each one carries the creator, recipient, date, collection, repository and a permalink to the source record. Where a field in the underlying catalogue was machine-generated rather than written by a human archivist, the record says so. An institution that publishes AI-assisted metadata without labelling it is quietly degrading its own catalogue; labelling it costs nothing and preserves the distinction permanently.</p>

  <h3>It does not fall back on general knowledge</h3>
  <p>If retrieval returns nothing relevant, the system does not answer from the model&rsquo;s own training. It says it found nothing and asks for clarification. That is a deliberate constraint, and it is the single most important one: a museum-branded assistant that quietly answers from the open web is no longer a collections tool, it is a chatbot wearing a museum&rsquo;s logo.</p>

  <h3>It knows Roosevelt died in 1919</h3>
  <p>The most common failure mode for a historical-figure AI is the anachronism question &mdash; <em>what would TR think about social media, about this election, about climate policy?</em> The tempting answer is a plausible-sounding extrapolation. The correct answer is that Roosevelt died on January&nbsp;6, 1919, and cannot have had a view.</p>
  <p>Adding that single rule moved abstention on temporal-impossibility tests <strong>from roughly 60% to 100%</strong>. One paragraph of instruction, and the system stopped inventing the opinions of a dead president.</p>
  <p>Refusal, though, is a blunt instrument in a gallery. A visitor who asks the Roosevelt avatar about social media and gets a lecture on his date of death has been corrected rather than served. The framework&rsquo;s answer to this is <strong>Cross-Era Analogical Grounding</strong>: the system reframes a present-day question through a documented historical parallel and answers from that. Asked about social media, it retrieves Roosevelt on the bully pulpit &mdash; going over the heads of the press to speak to citizens directly &mdash; and answers there, from attested material.</p>
  <p>It is a real distinction and worth being precise about it. The system is not extrapolating what Roosevelt <em>would have thought</em> about a thing that did not exist. It is answering the durable question underneath the modern one, out of what he actually said. The paper is candid that the boundary holds imperfectly &mdash; whether grounding reliably prevents synthesis from drifting into anachronism is, in its own words, open.</p>

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

  <h2>What running it unattended actually takes</h2>
  <p>A demo works when someone is watching it. An exhibit has to work at 4:40 on a Saturday with a line of people and no staff nearby, and that requirement drove more engineering than the model work did.</p>
  <p>Across one exhibition period, 653 push-to-talk releases produced 457 completed answers. The rest is the texture of a real gallery: 156 were superseded by a visitor interrupting or re-asking, and two smaller groups asked for a repeat or held the button too long. On the completed answers, the delay from releasing the button to Roosevelt&rsquo;s first spoken word averaged <strong>2.80 seconds</strong> &mdash; median 2.55, with 97% under five seconds and 69% under three.</p>
  <p>Underneath that: presence detection admits a visitor, each conversation is an isolated session, responses stream through dialogue, retrieval, avatar and voice, layered watchdogs recover any failed layer, and the session resets in place for the next person &mdash; no restart, no staff intervention. In the first two weeks of public operation in July 2026 it engaged close to <strong>5,000 visitors</strong>.</p>
  <p class="muted">Honest framing, and the paper says so plainly: this is observational evidence from a live exhibit, not a controlled study.</p>

  <h2>Published, so somebody else can build it</h2>
  <p>In September 2026 the framework was published with Microsoft&rsquo;s AI for Good Lab: <strong>&ldquo;The Living Library: Transforming Archival Collections into Conversational Knowledge Systems &mdash; Lessons from the Theodore Roosevelt Presidential Library&rdquo;</strong> (<a href="https://arxiv.org/abs/2609.09368" target="_blank" rel="noopener">arXiv:2609.09368</a>). I&rsquo;m one of eleven authors, and the Library&rsquo;s voice in it.</p>
  <p>Publishing it was the point. A single institution demonstrating a clever exhibit changes nothing for the field; a documented, transferable framework &mdash; with the failure modes named &mdash; is something a museum with a fraction of our budget can pick up and use at layer three. The paper is unusually candid about limits: OCR errors propagate into retrieval despite expert review, a corpus centred on one man&rsquo;s correspondence over-represents his perspective, and the boundary between inference and fabrication is inherently imperfect. Those belong in the record. A framework that only reports its wins is a brochure.</p>
  <p>The approach is already travelling. A sibling project, <em>Ukuvula</em>, applies the same pipeline to the Nelson Mandela Foundation&rsquo;s oral-history archive &mdash; a different medium, a different continent, the same four layers.</p>
  <p class="muted">TRPL&rsquo;s own write-up of the framework: <a href="http://labs.trlibrary.com/living-library" target="_blank" rel="noopener">labs.trlibrary.com/living-library</a></p>

  <h2>What I&rsquo;d carry forward</h2>
  <ul>
    <li><strong>Constrain first, capability second.</strong> Every impressive thing this system does is downstream of something it was forbidden to do.</li>
    <li><strong>Abstention is a feature you have to measure.</strong> Nobody ships a dashboard for &ldquo;questions we correctly declined,&rdquo; and it is the metric most likely to save you.</li>
    <li><strong>Label machine-generated metadata permanently.</strong> The distinction between what an archivist wrote and what a model inferred is impossible to reconstruct later.</li>
    <li><strong>Let an outside party re-run your evaluation.</strong> Otherwise your responsible-AI posture is a press release.</li>
    <li><strong>Publish the framework, not just the demo.</strong> The transferable thing is the four-layer model and the governance inversion &mdash; and an institution that documents its failure modes in public is making a far stronger claim than one that doesn&rsquo;t.</li>
    <li><strong>Layer three is the deliverable.</strong> The avatar is the photograph; the governed, queryable corpus is the access.</li>
    <li><strong>Name things after what they do.</strong> &ldquo;Reading Room&rdquo; described a building. &ldquo;Campfire&rdquo; describes the experience, and the rename clarified the roadmap as much as the marketing.</li>
  </ul>

  <h2>Why it matters</h2>
  <blockquote>The bar for &ldquo;research at a presidential library&rdquo; should be a question, not a finding aid.</blockquote>
  <p>The Library opened with this live on day one, in the browser and in the building. It is a working model for conversational AI at an institution that is serious about accessibility and scholarly integrity at the same time &mdash; and a demonstration that the second one is achievable if you are willing to let the system say &ldquo;I don&rsquo;t know.&rdquo;</p>

  <p class="muted">Try it: <a href="https://campfire.trlibrary.com" target="_blank" rel="noopener">campfire.trlibrary.com</a> · Read the paper: <a href="https://arxiv.org/abs/2609.09368" target="_blank" rel="noopener">arXiv:2609.09368</a> · Related: <a href="/projects/trpl-grand-opening-media/">the media campaign that made it a national story</a> · <a href="/projects/google-grants-optimizer/">AI in the Google Ad Grant</a></p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/democracy-symposium/"><span class="dir">&larr; Previous</span><span class="title">Democracy Symposium</span></a>
    <a class="next" href="/projects/annual-reports/"><span class="dir">Next &rarr;</span><span class="title">A Tale of Two Annual Reports</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/trpl-reading-room/index.html",
        title="The Living Library: AI-Driven Access to Library Collections — Matt Briney",
        description="AI-driven access to a presidential library's collections: a governed ~300,000-record corpus across 40+ repositories, 87.6% groundedness, and an in-gallery AI Roosevelt. Framework published with Microsoft's AI for Good Lab (arXiv:2609.09368).",
        active="projects",
        canonical="https://mattbriney.com/projects/trpl-reading-room/",
        og_image="/img/projects/tr-llm/hero.jpg",
        body=BODY,
    )
