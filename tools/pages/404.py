BODY = '''
<section class="hero" style="padding-top:6rem;padding-bottom:6rem">
  <div class="container" style="text-align:center;max-width:780px">

    <p class="eyebrow" style="display:inline-block;letter-spacing:.25em">PAGE NOT FOUND &middot; 404</p>

    <h1 style="font-size:clamp(2.5rem, 7vw, 5rem);margin:.5rem auto .75rem;max-width:22ch;line-height:1.05">
      Looks like you&rsquo;re off the map.
    </h1>

    <p class="lede" style="max-width:60ch;margin:0 auto 2.5rem">
      Theodore Roosevelt spent three months lost on the River of Doubt in 1914 and came back with one of the great adventure stories in American history. This is a less dramatic version of that &mdash; the page you were looking for doesn&rsquo;t exist, but here&rsquo;s how to find your way back.
    </p>

    <blockquote style="font-family:Fraunces,serif;font-size:1.4rem;line-height:1.35;font-style:italic;color:var(--ink);max-width:50ch;margin:0 auto 2.5rem;padding:1.5rem 2rem;border-left:3px solid var(--gold);background:var(--cream-soft);text-align:left;border-radius:4px">
      &ldquo;It is not the critic who counts &hellip; the credit belongs to the man who is actually in the arena.&rdquo;
      <span style="display:block;margin-top:.7rem;font-style:normal;font-size:.85rem;color:var(--ink-muted);font-family:Inter,sans-serif">&mdash; Theodore Roosevelt, Sorbonne, April 23, 1910</span>
    </blockquote>

    <p style="margin-bottom:2rem;font-size:1.05rem;color:var(--ink-muted)">
      Let&rsquo;s get you back to high ground. Try one of these:
    </p>

    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:1rem;margin-bottom:3rem">
      <a class="btn btn-primary" href="/">&larr; Home</a>
      <a class="btn btn-gold" href="/projects/">Browse the case studies</a>
      <a class="btn btn-ghost" href="/cv/">Read the CV</a>
    </div>

    <p style="font-size:.9rem;color:var(--ink-muted);margin-top:3rem">
      Still stuck? ''' + mail_link('Drop me a line', subject='Broken%20link%20on%20mattbriney.com') + ''' and I&rsquo;ll get you where you were trying to go.
    </p>

  </div>
</section>
'''

def build():
    return dict(
        out="404.html",
        title="404 &mdash; Off the Map &mdash; Matt Briney",
        description="The page you were looking for doesn't exist. Find your way back to the homepage, the case studies, or the CV.",
        active="",
        canonical="https://mattbriney.com/404.html",
        body=BODY,
        noindex=True,
        extra_head='<meta name="robots" content="noindex">',
    )
