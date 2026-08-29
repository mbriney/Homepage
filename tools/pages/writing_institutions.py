BODY = '''
<section class="section">
  <div class="container" style="max-width:760px">
    <p class="eyebrow">Essay &middot; August 2026</p>
    <h1 style="margin-bottom:.25em">The Institutions That Will Matter in 2035</h1>
    <p class="lede">American cultural institutions are about to be sorted &mdash; not by collection quality or endowment size, but by four decisions most of them are currently making by default. Here is what I think separates the ones that will still be growing in ten years.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="container" style="max-width:760px">

    <p>I have spent twenty years inside cultural institutions, most recently opening one from scratch. What follows is not a forecast. It is an argument about four choices that look technical or tactical from the inside, and turn out to be existential.</p>

    <h2>1. The AI question is not &ldquo;should we?&rdquo; It is &ldquo;what will we refuse to do?&rdquo;</h2>
    <p>Most institutional conversations about AI are still framed as adoption &mdash; whether to, how fast, what vendor. That framing will age badly, because the technology is arriving regardless and the interesting variable is restraint.</p>
    <p>A museum that deploys a conversational interface over its collection has made an implicit promise: that what comes out is the institution speaking. If the system quietly falls back on a model&rsquo;s training data when retrieval fails, the institution is now publishing claims it has never reviewed, under its own name, at scale. That is not a technology risk. It is the same risk as a curator inventing a provenance.</p>
    <p>The version worth building refuses. When we built <a href="/projects/trpl-reading-room/">Campfire</a> at the Theodore Roosevelt Presidential Library, the load-bearing decisions were all negative ones: answer only from the collection, cite every claim, and abstain entirely on anything after Roosevelt&rsquo;s death in 1919 rather than speculate about what he &ldquo;would have thought.&rdquo; That last rule alone moved abstention on impossible questions from roughly 60% to 100%.</p>
    <p>The measurable consequence is a groundedness score and a citation count. The institutional consequence is that a curator can stand behind the output. <strong>Institutions that treat AI as a capability will get demos. Institutions that treat it as an editorial system will get something they can defend in ten years.</strong></p>
    <p>The corollary nobody likes: if your catalogue now contains machine-generated fields, label them permanently. The distinction between what an archivist wrote and what a model inferred is impossible to reconstruct later, and every year you don&rsquo;t label it, the problem compounds.</p>

    <h2>2. Software procurement is quietly eating small institutions</h2>
    <p>A regional museum today is asked to license a ticketing platform, a CRM, an email tool, a digital asset manager, a collections system, a website CMS, an events calendar, a review monitor and a wayfinding app. Each is defensible. Together they consume a share of operating budget that would have been unthinkable in 2010, and they compound annually while admissions revenue does not.</p>
    <p>Much of what is being licensed is, underneath, a data file and a page.</p>
    <p>I am not arguing that institutions should build their own software &mdash; most should not, and an executive who reflexively builds is as dangerous as one who reflexively buys. I am arguing that <strong>the ability to tell the difference has become a core executive competency</strong>, and that most leadership teams currently have no one who can.</p>
    <p>The test is simple: does this data change per request, or per day? Ticket availability, opening hours, review counts, a social calendar, a press portal &mdash; all of it changes daily at most. Anything in that category can be a scheduled job writing a static file, which costs nothing to host and cannot go down. We built about twenty such tools for a presidential library and <a href="/toolkit/">released them under an open licence</a>, because there is no reason the next institution should pay for them either.</p>
    <p>The institutions that will have money for programming in 2035 are the ones that stop paying rent on their own operational data.</p>

    <h2>3. Interpretation is a distribution problem now</h2>
    <p>The traditional model assumed the visit was the product and everything else was marketing for it. That assumption is now backwards for most institutions, and the numbers have been saying so for a decade.</p>
    <p>At Mount Vernon we rebuilt the website around content rather than conversion and watched it go from 2.5 million to more than eight million annual visitors &mdash; against roughly a million people who came through the gate. The website was not marketing for the estate. <strong>It had become the largest classroom the institution operated</strong>, by a factor of eight, and it took years to reorganize around that fact.</p>
    <p>This has an uncomfortable implication for how institutions are structured. If your digital audience is an order of magnitude larger than your physical one, then digital interpretation is not a function that supports curatorial &mdash; it is a primary channel that should be resourced, staffed and evaluated like one. Most org charts still say otherwise.</p>
    <p>It also changes what &ldquo;access&rdquo; means. A free-admission day serves a few thousand people. A collections interface that answers a question in plain language serves anyone with a phone, permanently, and its marginal cost is close to zero.</p>

    <h2>4. Honest institutions will outperform careful ones</h2>
    <p>This is the argument I hold most strongly and can defend least with data, so I will make it plainly.</p>
    <p>Cultural institutions are structurally cautious. They interpret contested figures gently, decline to publish inconvenient operational facts, and treat critical coverage as a crisis to be managed. Each choice is individually rational and collectively corrosive, because audiences now have every other source and can tell when they are being handled.</p>
    <p>The Theodore Roosevelt Presidential Library opened with a blessing from the Mandan, Hidatsa and Arikara Nation before it opened with a speech, and with a permanent exhibition that addresses Roosevelt&rsquo;s record on race and empire directly rather than around it. The press that covered those subjects critically &mdash; and several outlets did &mdash; was treated as journalism to engage rather than a problem to solve. Prairie Public&rsquo;s headline, about a beautiful presidential library that won&rsquo;t shy away from ugly history, was closer to the institution&rsquo;s actual posture than anything we could have written for ourselves.</p>
    <p>The editorial instruction the Library&rsquo;s own leadership gave for its AI system is the clearest statement of this I have encountered: respond like a college professor, challenge the question, include the viewpoints and the norms of the period, don&rsquo;t defend a side, and present the material so the reader can reach their own conclusion.</p>
    <p><strong>That is harder to build than a system that refuses to discuss the difficult parts. It is also the only version that will still be credible in a decade.</strong></p>

    <div class="divider-mark" style="text-align:center;margin:3rem 0 2rem;color:var(--gold)">&#10070;&nbsp;&nbsp;&nbsp;&#10070;&nbsp;&nbsp;&nbsp;&#10070;</div>

    <h2>What this adds up to</h2>
    <p>None of these four is a technology problem, though three of them look like one. They are all questions about what an institution is willing to say, spend, staff and refuse &mdash; which is to say they are executive questions, and they are being answered by default in most places right now.</p>
    <p>The institutions that will matter in 2035 will not be the ones with the best AI, the biggest digital team or the cleverest architecture. They will be the ones that decided early what they would not do with any of it, wrote that down, and held to it when it was inconvenient.</p>

    <p class="muted" style="margin-top:2.5rem">Matt Briney is Chief Communications &amp; Marketing Officer at the Theodore Roosevelt Presidential Library, which opened in July 2026. He previously spent ten years as Vice President of Media &amp; Communications at George Washington&rsquo;s Mount Vernon. More: <a href="/leading/">how he runs a team</a> &middot; <a href="/projects/">the case studies</a> &middot; <a href="/toolkit/">the open-source toolkit</a></p>

  </div>
</section>
'''


def build():
    return dict(
        out="writing/institutions/index.html",
        title="The Institutions That Will Matter in 2035 — Matt Briney",
        description="Four decisions that will separate the cultural institutions still growing in 2035: what AI should refuse to do, the cost of software procurement, digital as a primary channel, and why honest institutions outperform careful ones.",
        active="",
        canonical="https://mattbriney.com/writing/institutions/",
        body=BODY,
    )
