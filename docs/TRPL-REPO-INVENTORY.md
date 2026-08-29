# TRPL GitHub Org — Full Repository Inventory

**Compiled:** August 29, 2026
**Org:** `Theodore-Roosevelt-Presidential-Library`
**Total repos:** 39 (24 public, 15 private)
**Sole human contributor across the in-house work:** Matt Briney

---

## The headline finding

**Zero of the 39 repositories contain a LICENSE file.**

Under US copyright law, no license means all rights reserved. Right now, no nonprofit can legally fork any of this — including the six tools that are otherwise fork-and-go ready. `AcquiaDAM-Photo-Embed`'s README says "MIT," but there is no LICENSE file to back it, which is arguably worse than silence: it invites reliance on a license that was never granted.

Adding an MIT or Apache-2.0 LICENSE to ~12 repos is maybe twenty minutes of work. It is the difference between "look what we built" and "take it." Everything else in this document is downstream of that one fix.

---

## The pattern

Twenty-plus production tools share one architecture, and it's a genuine thesis rather than a coincidence:

> Static files on GitHub Pages under `*.labs.trlibrary.com`. Where fresh data is needed, a scheduled GitHub Action pays that cost — never a server. No backend exists anywhere in the in-house portfolio. No API key is ever exposed to a browser. Git is the database, which means every number on screen is also a line in version history you can diff.

Hosting cost: $0. Maintenance surface: a YAML file. A two-person communications shop operates all of it.

There is a second, entirely separate family: four Azure enterprise systems built with vendors (Reading-Room, ArchivistApp, DataFoundations, trpl-ai4g-lab). Those are zero-trust VNets, Bicep IaC, Cosmos DB, and Azure AI Search. The contrast between the two families is itself worth writing about.

---

## Tier 1 — Genuinely adoptable by other nonprofits

Ranked by how little work a small museum would need. **All need a LICENSE before any of this is real.**

| Tool | Live at | What another nonprofit gets | Adopt |
|---|---|---|---|
| **LinkChecker** | *(github.io)* | Weekly crawl of your whole site for broken links + spelling, published as an interactive report. Every org-specific value is an env var with a documented table. Set `ROOT_DOMAIN`, go. | **5/5** |
| **PhotoGallery** | photogallery.labs | Drop a folder of full-res photos, run one Python script, get a masonry gallery embeddable anywhere. Nothing TR-specific exists in it. | **5/5** |
| **AcquiaDAM-Sync** | *(scheduled job)* | Keeps Acquia DAM collections synced to saved searches — closes a real vendor gap. All specificity lives in one YAML file with a blank example template shipped. | **5/5** |
| **elkhorn-panos** | elkhorn.labs | 360° panorama viewer. Drop your JPEGs in a folder, duplicate an HTML file per image. Zero logic to change. | **5/5** |
| **AcquiaDAM-Photo-Embed** | portalphotos.labs | Renders any Acquia DAM press portal as native gallery tiles — no fixed-height iframe. Has an explicit "use it for a different portal" recipe and ~20 `data-*` options. | **5/5** |
| **TRAnniversaries** | *(github.io)* | Tracks milestone anniversaries (every 5 years) of events you define in a JSON file. Swap `events.json`. | **4/5** |
| **TRTimelineWidget** | timeline.labs | Embeddable dual-axis timeline — your subject's life on top, world history below. All content in `tr-data.js` or a `data-src` JSON URL. | **4/5** |
| **Reviews** | reviews.labs | Scrapes Google/TripAdvisor/Yelp/Facebook reviews, classifies sentiment and themes with an LLM, publishes a dashboard + pull-quote widget. `config.json` opens with an `entity` block. | **4/5** |
| **DigitalInvite** | rsvp.labs | Paperless Post–style animated envelope invitations with per-guest name personalization and no backend. ~60 documented options; includes a no-code builder UI. | **4/5** |

**The gap:** not one repo has a section titled "Configure this for your organization." LinkChecker's config table and TRTimelineWidget's "editing the content" section come closest. For the nine above, adding that section is cheap and is the difference between technically-portable and actually-adopted.

---

## Tier 2 — Strong tools, but tied to a vendor or to TRPL

| Tool | Live at | Note | Adopt |
|---|---|---|---|
| **TripPlanner** | trip.labs | 10-step rule-based itinerary wizard. *"Deterministic, no AI, nothing to hallucinate."* Regional data is Medora-specific but cleanly in JSON. | 3/5 |
| **TicketingWidgets** | ticketing.labs | Sold-out warnings and better-day suggestions from ACME. Only useful to another ACME customer — but for them, excellent. | 3/5 |
| **SocialCalendar** | socialcalendar.labs | Read-only public view of your Hootsuite schedule. Setup doc is org-agnostic; brand is in the CSS. | 3/5 |
| **Quizes** | quiz.labs | Solo + async + real-time WebRTC multiplayer quizzes, zero infrastructure. Engine is portable; the fact-checking toolchain is not. | 3/5 |
| **TRC-Widget** | trc.labs | Search + relationship graph over 139,714 archival items. Specific to the Theodore Roosevelt Center's API. | 2/5 |
| **FamilyTree** | familytree.labs | Auto-laying-out genealogical tree, 46 people. Engine is generic; data lives inside the widget source. | 3/5 |
| **MedoraWeather** | weather.labs | NWS-backed weather widget + 8 static image variants. Location is one config file; the pattern is broadly useful. | 3/5 |
| **CampusMap** | campus.labs | 3D campus model, 338 MB → 8 MB. POIs externalized well, but the model *is* the product. | 2/5 |
| **NewsletterBuilder** | newsletter.labs | Browser-only newsletter builder exporting Constant Contact HTML. Deeply TRPL-branded by design. | 2/5 |
| **LBC-Dashboard** | lbc.labs | Living Building Challenge performance dashboard. **Prototype on demo data** — EcoStruxure not yet connected. | 2/5 |
| **BenefactorKiosk** | gratitude.labs | Donor recognition on a 60" 4K touchscreen. Private (donor PII). ~5,466 records, 13 societies. | 2/5 |
| **TRRetroGame** | trgame.labs | TR's life 1858–1919 as 10 platformer chapters. Currently robots-blocked on purpose. | 2/5 |
| **HoursEmbed** | *(github.io)* | Scrapes one Drupal page's hours block to feed one Squarespace site. Built in 31 minutes. | 1/5 |

---

## Tier 3 — Internal operations

| Repo | Vis | What it is |
|---|---|---|
| **Dashboard** | Private | Marketing/visitation single source of truth. **24 API pullers** — GA4, Google Ads, Search Console, GBP, YouTube, Facebook, Instagram, Threads, LinkedIn, X, Hootsuite, ACME, Shopify, Constant Contact, Simplecast, Reviews, weather. No backend; nightly Action commits JSON. ~1,000 commits since May. |
| **Brand** | Public | Machine-readable brand spec (`brand.json`) built explicitly for AI tooling — including terminology rules and a sensitive-topics policy that flow downstream into the Reading Room's prompts. |
| **TRPLFIT-ExhibitChecklist** | Private | PowerApps daily exhibit walkthrough app. |
| **NPS-TRNP-Photos** | Private | Searchable contact sheet of NPS imagery from TR National Park. |
| **trphotos** | Private | Browser for the various TR photo collections. |
| **MapsDemo** | Private | Map treatments for the website. |
| **mbriney-planning** | Private | The drip campaign flowchart (41 emails, 5 journeys). One 230 KB HTML file. |
| **mbriney-claude** | Private | Working-folder backup. |
| **tr-books** | Private | Digitized book corpus feeding the Reading Room. Licensed content. |
| **Five-Jars** | Private | The trlibrary.com Drupal 11 website repo (vendor). |
| **mdm-enrollment** | Public | One 172-byte Apple MDM discovery file. Dormant 16 months, custom domain deleted. Footnote, not a project. |

---

## Tier 4 — The Azure stack (vendor-built)

**Reading-Room** — the system behind Campfire. Built by **Valorem Reply with Microsoft sponsorship**. Next.js 15 + Bun frontend, Python FastAPI backend, Azure OpenAI + AI Search + Redis.

The architecture is a four-stage pipeline in one `EndToEndAgent` class: a Scope agent and a Query agent run concurrently on a small model; if Scope returns out-of-scope the workflow aborts before the expensive call. Two indexes — letters and books — are searched in parallel and **round-robin interleaved** with no score threshold, because the RAG agent itself is the relevance filter: it returns `selected_sources` listing only what it actually used, and only those become citations.

Numbers worth having:

- **51,535 letter documents · 6,495 book documents**
- Groundedness **87.6%**, averaging **8.4 citations** per answer
- Correctness **85.7%** pass (216/252 quiz questions)
- Abstention **83%** — and a git-tracked baseline at **100%** on the 50-question out-of-scope set
- Latency: TTFT ~5.2s, total ~9.0s, p95 ~12.5s
- Microsoft's AI4Good team can clone the repo and re-run against published baselines — *"external accountability for Responsible AI commitments"*

Two details that belong in a case study. First, the no-fallback rule: if search returns nothing, the context is literally *"No relevant documents were found"* — **"No fallback to generalist knowledge. This is intentional for Responsible AI."** Second, the temporal guardrail: TR died January 6, 1919, and asking his view on anything after that must produce an abstention rather than speculation. An ADR records that this one prompt addition moved abstention **from ~60% to 100%** on temporal-impossibility tests.

The four modes (Discovery, Research, Teachers, Students) only prepend a persona to the answer prompt — *"the scope, search-query, and fact-checker stages are mode-agnostic so retrieval stays deterministic and the groundedness rubric is uniform."* Governance runs through ADRs with named stakeholders; ADR-002 on sensitive content was decided by you and cites TRPL leadership's own words on the voice they wanted.

⚠️ **One thing I could not confirm:** nothing in the Reading-Room repo references `campfire.trlibrary.com`. It deploys as `trpl-rr-web` on Azure App Service. If Campfire fronts this app, the mapping is in DNS, not in code. Worth verifying before the case study asserts it.

**ArchivistApp** — human-in-the-loop review queue for AI-generated archival metadata before it reaches the public index. React 19 + FastAPI on Azure. Its 8 open issues are the honest story: duplicate book ingestion under different UUIDs, noisy OCR output, preventing publication of records not yet published to TRC.

**DataFoundations** — the ingestion platform and shared Azure infra layer. Notable for a read-only, stateless outbound API serving approved records to a partner (Terentia), with **revocation as a first-class concept**: a `GET /unapproved-records` endpoint exists so partners can detect records whose approval was later withdrawn.

**trpl-ai4g-lab** — "code samples for various components of the TRPL AI experience." The likeliest home for the in-person AI TR theater code. Not yet opened.

---

## Two documents worth more than their repos

1. **`FamilyTree/docs/SOURCES.md`** — a provenance audit that caught the Library about to publish the **wrong death date for TR's own daughter** (books said Dec 3, 1977; verification found Dec 10). It also recovered a grandchild the books counted but never named — Judith Quentin Derby, *"born five years after the uncle she was named for was killed over France."* And it documents deliberately declining precision where a circulating date doesn't hold up, *"because stating it would mean publishing someone else's guess."*

2. **`LBC-Dashboard/docs/EcoStruxure-API-Access.md`** — a vendor-negotiation playbook: which Schneider product maps to which API, exactly what to ask your integrator for, what a read-only token request should contain. Any museum with a Schneider building system could use it verbatim.

---

## Things to fix before any of this goes on the portfolio

1. **No licenses, anywhere.** The whole adoption story depends on this.
2. **`AcquiaDAM-Photo-Embed` claims MIT in its README with no LICENSE file.** Fix first — it's also the most fork-ready.
3. **Two stale READMEs.** Quizes says 29 quizzes (actually **86**). Reviews says 335 reviews (actually **463**). Don't cite the README numbers.
4. **Two empty repos.** `PresidentialPublicLands` and `ConstantContactSegments` are ~90-byte README stubs, one commit each, never touched. Exclude them or label them as concepts. (`ConstantContactSegments` is a shame — "fixes limitations in Constant Contact segments for future dates" is the most universally-applicable problem statement in the org.)
5. **Quizes has self-documented pre-launch blockers** — unfinished two-source verification on Badlands content, unconfirmed font web-embedding license, Getty and Ziemendorf image clearances pending. Its README also claims Pages isn't enabled. Verify before linking publicly.
6. **`Dashboard` has 202 consecutive Google Business Profile failures** (HTTP 429, failing since July 23) and a Hootsuite token that can't write back to the `github-pages` environment secret. Unrelated to the portfolio, but it means GBP data has been dark for five weeks.
7. **Brand font licensing recurs across repos** — Dharma Gothic E, ITC Clearface and Frutiger Next are Adobe Fonts licensed and cannot be bundled in public repositories. MedoraWeather has them committed. Worth an audit.

---

## What this changes about the website plan

`TRPL-EXPANSION-PLAN.md` scoped `trpl-labs` around five repos. There are roughly **25 shippable tools**. See §3.8 of that document for the revision.

The stronger framing is no longer "five products, zero servers." It is:

> **A presidential library's communications shop shipped 25 production tools in five months, on $0 of hosting, and is giving them away.**

The giving-away part only becomes true when the LICENSE files land.
