BODY = '''
<section class="case-hero">
  <div class="container">
    <a href="/projects/" class="back">&larr; All projects</a>
    <p class="eyebrow">Case study · Theodore Roosevelt Presidential Library · 2024–present</p>
    <h1>The Reading Room: Exploring Theodore Roosevelt&rsquo;s Life Through AI</h1>
    <p class="lede">A GPT-powered way into the Theodore Roosevelt Presidential Library&rsquo;s collection &mdash; designed so anyone with a question about TR can ask in plain language and walk back out with sourced, citable answers.</p>

    <div class="meta-row">
      <div class="meta-item"><span class="label">Role</span><span class="value">Project Lead</span></div>
      <div class="meta-item"><span class="label">Organization</span><span class="value">Theodore Roosevelt Presidential Library</span></div>
      <div class="meta-item"><span class="label">Stack</span><span class="value">LLM + retrieval over digitized collection</span></div>
      <div class="meta-item"><span class="label">Status</span><span class="value">In active development</span></div>
    </div>

    <div class="case-hero-image">
      <picture>
        <source type="image/webp" srcset="/img/projects/tr-llm/hero.webp">
        <img src="/img/projects/tr-llm/hero.jpg" alt="The Reading Room — Discover the life &amp; legacy of Theodore Roosevelt" width="1600" height="856">
      </picture>
    </div>
  </div>
</section>

<div class="case-content">

  <h2>The brief</h2>
  <p>Cultural institutions sit on enormous, under-indexed collections: letters, speeches, photographs, ephemera. Finding the right object has historically required knowing the finding aid &mdash; an archivist&rsquo;s skill, not a visitor&rsquo;s. The job: lower that bar from <em>&ldquo;know the finding aid&rdquo;</em> to <em>&ldquo;ask a question.&rdquo;</em></p>

  <h2>The Reading Room</h2>
  <p>The Reading Room is the Theodore Roosevelt Presidential Library&rsquo;s public interface to its collection. A visitor &mdash; a student, a teacher, a researcher, a curious citizen &mdash; can:</p>
  <ul>
    <li>Pick from prompts: <em>I want to do research, find images, build a lesson plan, write a paper, test my knowledge&hellip;</em></li>
    <li>Or type their own question.</li>
    <li>Or pick a topic: the Square Deal, Rough Riders, Roosevelt&rsquo;s presidency, antitrust actions, the Bull Moose party, books TR authored.</li>
  </ul>
  <p>The AI does the retrieval, summarization, and synthesis &mdash; but always points back to the underlying primary source. No hallucinated quotes, no fabricated dates, no paraphrase masquerading as TR&rsquo;s voice.</p>

  <h2>How it works</h2>
  <h3>Designed around scholarly trust</h3>
  <p>The hard part of LLMs in cultural-heritage settings isn&rsquo;t getting an answer &mdash; it&rsquo;s getting an answer the institution is willing to stand behind. The Reading Room is built so that:</p>
  <ul>
    <li>Every answer cites and links to the primary sources it drew from.</li>
    <li>The model retrieves from the Library&rsquo;s digitized collection rather than from open-web speculation.</li>
    <li>An &ldquo;How we use AI&rdquo; explainer and a &ldquo;Report an issue&rdquo; pathway are first-class UI, not afterthoughts.</li>
  </ul>

  <h3>Built with curators, not around them</h3>
  <p>The project is a partnership with the collections and curatorial team from day one. The AI is a wayfinding layer over their work, not a replacement for it &mdash; and the team has authority over what the tool will and won&rsquo;t answer.</p>

  <h2>Why it matters</h2>
  <blockquote>The bar for &ldquo;research at a presidential library&rdquo; should be a question, not a finding aid.</blockquote>
  <p>The Library opens with this capability live on day one. It&rsquo;s a working model for what conversational AI looks like when an institution is serious about both accessibility and scholarly integrity &mdash; not one at the expense of the other.</p>

  <nav class="case-nav" aria-label="Case study navigation">
    <a class="prev" href="/projects/mv-explorer/"><span class="dir">&larr; Previous</span><span class="title">Mount Vernon Explorer</span></a>
    <a class="next" href="/projects/multiplier/"><span class="dir">Next &rarr;</span><span class="title">Multiplier</span></a>
  </nav>
</div>
'''

def build():
    return dict(
        out="projects/trpl-reading-room/index.html",
        title="The Reading Room (TRPL AI Collections) — Matt Briney",
        description="A GPT-powered way into the Theodore Roosevelt Presidential Library's digitized collection. Built around scholarly trust: every answer cites primary sources, with curators in the loop.",
        active="projects",
        canonical="https://mattbriney.com/projects/trpl-reading-room/",
        og_image="/img/projects/tr-llm/hero.jpg",
        body=BODY,
    )
