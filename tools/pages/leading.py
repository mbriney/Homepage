BODY = '''
<section class="section">
  <div class="container" style="max-width:760px">
    <p class="eyebrow">How I work</p>
    <h1 style="margin-bottom:.25em">Six things I believe about running a communications team</h1>
    <p class="lede">Every one of these came from getting it wrong first. They are the principles I actually operate by, with the decisions that produced them.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="container" style="max-width:760px">

    <h2>1. Put junior people on the biggest week</h2>
    <p>The instinct before a high-stakes moment is to staff it only with people who have done it before. That instinct is wrong, and it is wrong for a structural reason: <strong>an opening is the only time an institution runs a full-scale press operation.</strong> If you don&rsquo;t train people during one, you never train them at all, because there is no second grand opening.</p>
    <p>Four interns worked opening week at the Theodore Roosevelt Presidential Library as production assistants &mdash; a national press pool, a Secret Service perimeter, a live network riser, a sold-out ceremony. It cost the operation almost nothing. It is the part of that week I would least want to have skipped.</p>
    <p class="muted">&rarr; <a href="/projects/trpl-grand-opening-media/">The opening media campaign</a></p>

    <h2>2. Publish the bad news yourself</h2>
    <p>The <a href="https://www.trlibrary.com/visit" target="_blank" rel="noopener">Plan Your Visit</a> page tells people that August is the busiest month, that walk-up tickets may not be available, that Medora&rsquo;s hotels sell out, and that they should consider five other towns. Every one of those sentences costs same-session bookings.</p>
    <p>All of them are true, and the arithmetic is not close. <strong>A visitor who drives four hours and cannot get in is a far worse outcome than one who books next month.</strong> Destination institutions live and die on the worst arrival experience, because that visitor tells everyone. Publishing the bad news in advance is cheaper than absorbing it at the admissions desk, and it is what makes everything else on the page believable.</p>
    <p>The same principle applies to coverage. When the press wrote critically about the Library &mdash; and it did, on public lands and on Roosevelt&rsquo;s record on race and empire &mdash; the answer was not a rebuttal. An institution that only wants friendly coverage is asking to be taken less seriously than one that can survive the other kind.</p>
    <p class="muted">&rarr; <a href="/projects/trpl-launch-campaign/">The launch campaign</a></p>

    <h2>3. Buy attention, not software</h2>
    <p>A new institution with a two-person communications team was quoted between $15,000 and $60,000 per tool for things that are, underneath, a data file and a page. We built roughly twenty instead &mdash; trip planning, collections search, review monitoring, ticket availability &mdash; as static files with scheduled jobs, at zero hosting cost.</p>
    <p>This is not a technical preference. It is a capital-allocation decision. <strong>Every dollar not spent on a vendor contract is a dollar available for photography, press tours, or a person.</strong> The constraint also produced a better architecture than a budget would have: no servers means no procurement, no annual renewal, no integration consultant, and nothing that can fail at 3 a.m.</p>
    <p>The corollary matters as much: an executive who can evaluate a build should still mostly buy. The judgment is knowing which is which.</p>
    <p class="muted">&rarr; <a href="/projects/trpl-labs/">The tools, and what they cost</a></p>

    <h2>4. Design the failure before the feature</h2>
    <p>My favourite line in anything my team has shipped is a sentence about what happens when a script breaks: <em>if parsing fails, the last good file stays published.</em></p>
    <p>A layout change upstream degrades to stale-but-correct, never to blank. Most integrations do the opposite &mdash; they fail open and show nothing, at precisely the moment a visitor is trying to find out whether you are open today.</p>
    <p>This generalizes well beyond code. Before launching anything &mdash; a campaign, a membership programme, an exhibit interactive &mdash; the useful question is not &ldquo;what does success look like?&rdquo; but <strong>&ldquo;what does this do on its worst day, and who notices?&rdquo;</strong></p>
    <p class="muted">&rarr; <a href="/toolkit/hours-embed/">The tool that taught me this</a></p>

    <h2>5. Automation should raise a hand, not make the call</h2>
    <p>The trip planner&rsquo;s link checker watches every booking URL and every advertised season, and when something changes it <em>opens an issue</em>. It does not edit the data. A person makes the change.</p>
    <p>The same rule governs the AI work. <a href="/projects/trpl-reading-room/">Campfire</a> answers only from the Library&rsquo;s own sources and refuses to fall back on general knowledge; it will say it found nothing rather than improvise. Adding a single rule &mdash; Roosevelt died in 1919 and cannot have a view on anything after that &mdash; moved its abstention rate from roughly 60% to 100% on questions it should decline.</p>
    <p><strong>The measure of a system is not what it produces, but what it refuses to produce.</strong> That is a management principle as much as an engineering one.</p>

    <h2>6. Divide the story instead of rationing it</h2>
    <p>Every outlet wants an exclusive and there is only ever one opening. Hand the whole story to the wires and the <em>Times</em> loses interest; hand it to the <em>Times</em> and the regional papers that run wire copy never cover you at all.</p>
    <p>So the story got divided rather than rationed. The building went to the design press. The financing went to Bloomberg. The AI exhibit went to the technology desks. The conservation legacy went to broadcast. The politics went to the wires. <strong>One exclusive makes four enemies; five different exclusives make five partners.</strong></p>
    <p>Read the published pieces and the lanes are visible &mdash; the architects appear in the design press and nowhere else; the family appears in two broadcast segments and no print piece; the historian surfaces only in the one story that had to answer for historical accuracy. That is achievable only if you decide in advance who speaks for what.</p>
    <p class="muted">&rarr; <a href="/projects/trpl-grand-opening-media/#">How the exclusives were divided</a></p>

    <div class="divider-mark" style="text-align:center;margin:3rem 0 2rem;color:var(--gold)">&#10070;&nbsp;&nbsp;&nbsp;&#10070;&nbsp;&nbsp;&nbsp;&#10070;</div>

    <p>If there is a thread running through all six, it is that <strong>most of the leverage in this job sits in decisions nobody sees</strong> &mdash; who is in the room, what the system refuses to do, which sentence you are willing to publish against your own short-term interest. The visible work is downstream of those.</p>

    <p class="muted" style="margin-top:2rem">More: <a href="/projects/">the case studies these came from</a> &middot; <a href="/writing/institutions/">where I think cultural institutions are heading</a> &middot; <a href="/bio/">the career narrative</a></p>

  </div>
</section>
'''


def build():
    return dict(
        out="leading/index.html",
        title="How I Work — Six Principles for Running a Communications Team — Matt Briney",
        description="Six operating principles from running communications at the Theodore Roosevelt Presidential Library and George Washington's Mount Vernon — with the decisions that produced them.",
        active="",
        canonical="https://mattbriney.com/leading/",
        body=BODY,
    )
