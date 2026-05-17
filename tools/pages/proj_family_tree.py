BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Personal project · 2026</p>
    <h1>Briney Family Tree: An AI-Driven Genealogical Research Engine</h1>
    <p class="lede">An agent-powered research pipeline that scans the Briney family GEDCOM for promising leads, investigates each across cached and primary sources, and produces a human-reviewable findings report before anything touches the tree.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Status</span><span class="value">In active development</span></div>
      <div class="meta-item"><span class="label">Stack</span><span class="value">Python + LLM agents + GEDCOM</span></div>
      <div class="meta-item"><span class="label">Sources</span><span class="value">WikiTree · FamilySearch · Find&nbsp;A&nbsp;Grave · books</span></div>
      <div class="meta-item"><span class="label">Frontend</span><span class="value">Custom pedigree explorer</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/family-tree/hero.webp">
        <img src="/img/projects/family-tree/hero.jpg" alt="Briney Family Tree — pedigree view with research detail" width="1600" height="1066">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Genealogy is one of those domains where the bottleneck is not writing &mdash; it&rsquo;s checking. A finite number of public databases hold a lot of the answers; the work is figuring out which person is which, where the dates don&rsquo;t line up, who&rsquo;s missing a death record, which immigrant founder needs a closer look, which famous-cousin link is real and which is wishful thinking.</p>
  <p>An LLM agent is actually good at most of that. The trick is keeping it on a leash: the GEDCOM stays the single source of truth, and nothing gets written without a human in the loop.</p>

  <h2>What it does</h2>

  <h3>Target identification</h3>
  <p>A research session starts by scanning the GEDCOM for the kinds of patterns a genealogist would notice:</p>
  <ul>
    <li>Missing birth or death dates</li>
    <li>Zero-lifespan anomalies and date discrepancies</li>
    <li>Broken parent/child or spousal links</li>
    <li>Immigrant founders with unresolved origins</li>
    <li>Military service that could anchor a record</li>
    <li>Plausible &ldquo;famous-cousin&rdquo; links worth verifying</li>
  </ul>

  <h3>Multi-source investigation</h3>
  <p>For each target, the agent works through a layered set of sources:</p>
  <ul>
    <li>A local WikiTree cache for the family branches</li>
    <li>FamilySearch and Find&nbsp;A&nbsp;Grave</li>
    <li>Wikipedia for notable connections</li>
    <li>Targeted web search for primary-source citations</li>
    <li>A growing corpus of published family-history books</li>
  </ul>

  <h3>Findings &mdash; not edits</h3>
  <p>The agent doesn&rsquo;t write to the tree. It produces a findings report: per target, what it found, the sources, a confidence band, and a proposed GEDCOM edit. I review and approve. Approved edits run through a <em>bio_guard</em> step that protects existing biographical narrative from being clobbered.</p>

  <div class="gallery cols-2">
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/family-tree/01.webp"><img src="/img/projects/family-tree/01.jpg" alt="Family tree research view"></picture>
      <figcaption class="gallery-caption">Per-person view with sourced biography, family links, and research-confidence indicators.</figcaption>
    </figure>
    <figure>
      <picture><source type="image/webp" srcset="/img/projects/family-tree/02.webp"><img src="/img/projects/family-tree/02.jpg" alt="Family tree explorer"></picture>
      <figcaption class="gallery-caption">The pedigree explorer, with deep-linking on every name and migration paths on a map.</figcaption>
    </figure>
  </div>

  <h2>The frontend</h2>
  <p>The tree itself is a custom static site &mdash; a pedigree explorer with search, map, lines-of-descent, and notable-ancestor features, plus a sources-and-confidence panel that makes the AI&rsquo;s reasoning visible rather than hidden. Migration paths show up on a map. Everything links to the underlying citation.</p>

  <h2>Why I like it</h2>
  <blockquote>An agent that can surface 100 candidate facts in an hour, with sources and confidence, turns a hobby that used to take years into something you can move forward on a Sunday afternoon.</blockquote>
  <p>It&rsquo;s also a useful working example of where I think this technology actually belongs in cultural-heritage settings: as a research-assistant layer over real archival material, with the human in the loop and the institution&rsquo;s data as the ground truth.</p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/travel-passport/"><span class="dir">&larr; Previous</span><span class="title">Travel Passport</span></a>
    <a class="next" href="/projects/"><span class="dir">Back to &rarr;</span><span class="title">All projects</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/family-tree/index.html",
        title="Briney Family Tree & Research AI — Matt Briney",
        description="An AI-driven genealogical research engine over the Briney family GEDCOM. Identifies promising leads, investigates them across WikiTree, FamilySearch, Find A Grave, and family-history books, then produces a human-reviewable findings report.",
        active="projects",
        canonical="https://mattbriney.com/projects/family-tree/",
        og_image="/img/projects/family-tree/hero.jpg",
        body=BODY,
    )
