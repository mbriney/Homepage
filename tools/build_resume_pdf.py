"""Generate Matt-Briney-Resume.pdf in the site's visual style.

Uses reportlab + the actual website fonts (Fraunces serif for headings,
Inter sans for body) and the site's exact color palette (cream/ink/
forest green/brass). Output:  files/Matt-Briney-Resume.pdf

Run:  python3 tools/build_resume_pdf.py
"""
import os
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table,
    TableStyle, KeepTogether, HRFlowable
)
from reportlab.platypus.flowables import Flowable

# -------------------------------------------------------------- palette
INK         = HexColor("#1c1a17")
INK_MUTED   = HexColor("#6b6357")
ACCENT      = HexColor("#2d4a3e")   # forest green
ACCENT_DARK = HexColor("#1f3329")
GOLD        = HexColor("#a06b2c")   # warm brass
GOLD_SOFT   = HexColor("#d9b87a")
CREAM       = HexColor("#faf6ed")
CREAM_SOFT  = HexColor("#f3ede0")
BORDER      = HexColor("#e4d9c0")

# -------------------------------------------------------------- fonts
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FDIR = os.path.join(ROOT, "tools", "fonts")
pdfmetrics.registerFont(TTFont("Inter",        os.path.join(FDIR, "Inter-400.ttf")))
pdfmetrics.registerFont(TTFont("Inter-Sb",     os.path.join(FDIR, "Inter-600.ttf")))
pdfmetrics.registerFont(TTFont("Inter-Bold",   os.path.join(FDIR, "Inter-700.ttf")))
pdfmetrics.registerFont(TTFont("Fraunces",     os.path.join(FDIR, "Fraunces-400.ttf")))
pdfmetrics.registerFont(TTFont("Fraunces-Sb",  os.path.join(FDIR, "Fraunces-600.ttf")))
pdfmetrics.registerFont(TTFont("Fraunces-Bold",os.path.join(FDIR, "Fraunces-700.ttf")))

# -------------------------------------------------------------- styles
S = {}
S["name"] = ParagraphStyle(
    "name", fontName="Fraunces-Bold", fontSize=30, leading=34,
    textColor=INK, spaceAfter=2,
)
S["eyebrow"] = ParagraphStyle(
    "eyebrow", fontName="Inter-Sb", fontSize=8.5, leading=10,
    textColor=GOLD, spaceAfter=4,
)
S["role"] = ParagraphStyle(
    "role", fontName="Fraunces", fontSize=12, leading=15,
    textColor=ACCENT, spaceAfter=4,
)
S["contact"] = ParagraphStyle(
    "contact", fontName="Inter", fontSize=9, leading=13,
    textColor=INK_MUTED, alignment=TA_RIGHT,
)
S["h2"] = ParagraphStyle(
    "h2", fontName="Fraunces-Sb", fontSize=13, leading=16,
    textColor=ACCENT, spaceBefore=9, spaceAfter=3,
)
S["body"] = ParagraphStyle(
    "body", fontName="Inter", fontSize=9, leading=13,
    textColor=INK, spaceAfter=4, alignment=TA_LEFT,
)
S["summary"] = ParagraphStyle(
    "summary", fontName="Inter", fontSize=9, leading=13,
    textColor=INK_MUTED, spaceAfter=5, alignment=TA_LEFT,
)
S["lead"] = ParagraphStyle(
    "lead", fontName="Inter", fontSize=10, leading=14,
    textColor=INK, spaceAfter=5, alignment=TA_LEFT,
)
S["role_title"] = ParagraphStyle(
    "role_title", fontName="Fraunces-Sb", fontSize=11, leading=13,
    textColor=INK, spaceAfter=1,
)
S["role_dates"] = ParagraphStyle(
    "role_dates", fontName="Inter-Sb", fontSize=8.5, leading=13,
    textColor=GOLD, alignment=TA_RIGHT,
)
S["role_company"] = ParagraphStyle(
    "role_company", fontName="Inter-Sb", fontSize=9, leading=12,
    textColor=ACCENT, spaceAfter=2,
)
S["bullet"] = ParagraphStyle(
    "bullet", fontName="Inter", fontSize=8.6, leading=12,
    textColor=INK, spaceAfter=2, alignment=TA_LEFT,
    leftIndent=11, bulletIndent=0,
)
S["expertise"] = ParagraphStyle(
    "expertise", fontName="Inter-Sb", fontSize=8.6, leading=11,
    textColor=ACCENT,
)
S["board"] = ParagraphStyle(
    "board", fontName="Inter", fontSize=9, leading=13,
    textColor=INK, spaceAfter=2,
)


# -------------------------------------------------------------- helpers
def gold_rule():
    return HRFlowable(width="100%", thickness=0.6,
                      color=GOLD, spaceBefore=2, spaceAfter=8)


def h2(text):
    return [Paragraph(text.upper(), S["h2"]), gold_rule()]


def role(title, dates, company, summary, bullets):
    """Render a single career role block."""
    # Title row: title left, dates right (two-column table)
    head = Table(
        [[Paragraph(title, S["role_title"]),
          Paragraph(dates or "", S["role_dates"])]],
        colWidths=[5.7 * inch, 1.6 * inch],
        style=TableStyle([
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("LEFTPADDING", (0,0), (-1,-1), 0),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
            ("TOPPADDING", (0,0), (-1,-1), 0),
            ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ]),
    )
    parts = [head, Paragraph(company, S["role_company"])]
    if summary:
        parts.append(Paragraph(summary, S["summary"]))
    for b in bullets:
        parts.append(Paragraph(f"<font color='#a06b2c'>▪</font>&nbsp;&nbsp;{b}",
                               S["bullet"]))
    parts.append(Spacer(1, 3))
    return parts


def expertise_grid(items, cols=3):
    """Three-column grid of expertise tags with a tiny gold bullet."""
    rows = []
    for i in range(0, len(items), cols):
        row = []
        for j in range(cols):
            if i + j < len(items):
                row.append(Paragraph(
                    f"<font color='#a06b2c'>•</font>&nbsp;&nbsp;{items[i+j]}",
                    S["expertise"]))
            else:
                row.append("")
        rows.append(row)
    col_w = (7.3 * inch) / cols
    t = Table(rows, colWidths=[col_w] * cols,
              style=TableStyle([
                  ("VALIGN", (0,0), (-1,-1), "TOP"),
                  ("LEFTPADDING", (0,0), (-1,-1), 0),
                  ("RIGHTPADDING", (0,0), (-1,-1), 6),
                  ("TOPPADDING", (0,0), (-1,-1), 2),
                  ("BOTTOMPADDING", (0,0), (-1,-1), 2),
              ]))
    return t


# -------------------------------------------------------------- content
CV_NAME      = "Matt Briney"
CV_ROLE      = "Museum &amp; Cultural Institution Executive"
CV_CONTACT   = ("mkbriney@gmail.com<br/>"
                '<a href="https://www.linkedin.com/in/mbriney/" color="#2d4a3e">linkedin.com/in/mbriney</a><br/>'
                "Dallas, TX  ·  (214) 538-6840<br/>"
                '<a href="https://mattbriney.com" color="#2d4a3e">mattbriney.com</a>')

SUMMARY = [
    ("Senior museum and cultural institution leader with a strong track record of advancing "
     "presidential libraries and historic sites through strategic vision, integrated planning, "
     "visitor-centered experiences, and measurable audience growth."),
    ("Results-oriented executive with deep experience leading complex, mission-driven organizations "
     "through strategic planning, large-scale initiatives, and cross-functional collaboration. "
     "Proven ability to translate institutional vision into executable roadmaps spanning "
     "exhibitions, visitor experience, education, operations, and public engagement. Adept at "
     "guiding organizations through periods of growth and change, leveraging data, audience "
     "insight, and sound judgment to inform decision-making and deliver measurable results."),
]

EXPERTISE = [
    "Museum Operations &amp; Strategy",
    "Exhibitions &amp; Interpretive Experiences",
    "Education &amp; Civic Engagement",
    "Strategic Planning &amp; Execution",
    "Leadership &amp; Staff Development",
    "Budgeting, P&amp;L &amp; Forecasting",
    "Project &amp; Program Management",
    "Membership &amp; Earned Revenue",
    "Public Programming &amp; Events",
    "Institutional Communications",
    "Interpretive Storytelling",
    "Audience Development",
    "Analytics &amp; Reporting",
    "Cross-Functional Collaboration",
    "Technology Implementation",
]

ROLES = [
    dict(
        title="Chief Communications &amp; Marketing Officer",
        dates="2024 — Present",
        company="Theodore Roosevelt Presidential Library — Remote",
        summary=(
            "Built the communications and marketing function from zero at a nonprofit startup, "
            "reporting to the CEO on a $1.3M budget. Led institutional communications and "
            "public-facing strategy through the Library's July 4, 2026 opening as a key member "
            "of the leadership team — delivering an opening covered nationally from the AP to "
            "Architectural Digest, with $98M in earned media across 312 placements."
        ),
        bullets=[
            "Hired and manage the in-house communications team, and previously built out web content editing and group tour sales roles — scaling the function deliberately as a nonprofit startup rather than staffing ahead of need.",
            "Served on the leadership team responsible for developing the Library's operations plan, including business and earned-revenue components, using benchmarking and planning data from peer presidential and cultural institutions.",
            "Led a daily historical storytelling initiative focused on Theodore Roosevelt's life and legacy, tripling social media engagement while using performance data to inform interpretation and audience engagement.",
            "Direct and manage all press relations for the Presidential Library, overseeing an external agency and serving as institutional spokesperson. Built the press center, press kit, and open photo portal behind opening coverage in the AP, Reuters, the New York Times, the Wall Street Journal, the Washington Post, NPR, CNN, and Architectural Digest.",
            "Managed opening-week visual coverage — three Getty photographers, two photo editors, an in-house photographer, and a documentary team — producing 2,400+ press assets published without gatekeeping.",
            "Developed and maintained an institution-wide talking-points framework covering construction, exhibitions, outreach, and Theodore Roosevelt's legacy, ensuring consistency across leadership and partners.",
            "Oversee a documentary video team capturing the Library's construction and development, producing interpretive and archival assets used for education, exhibitions, and public engagement.",
            "Led the selection of ticketing, e-commerce, and database systems, evaluating platforms for scalability, reporting capabilities, data integrity, and visitor experience.",
            "Established the Library's membership and annual giving programs, defining value propositions and baseline metrics for acquisition, retention, and engagement.",
            "Led the development of an AI-driven, GPT-powered collections platform, working closely with collections and curatorial teams to improve access to and exploration of the Library's collection.",
            "Built an AI-driven Google Ad Grant optimizer for the TRPL Foundation that crawls the institution's sitemap and manages campaigns via the Google Ads &amp; GA4 APIs, sustaining a 16.46% average click-through rate (peak 25.78%) — more than 3× the Grant minimum.",
        ],
    ),
    dict(
        title="Vice President, Media &amp; Communications",
        dates="2014 — 2024",
        company="George Washington's Mount Vernon — Mount Vernon, VA",
        summary=(
            "Senior executive at one of the nation's most-visited historic sites, responsible "
            "for leading integrated communications, interpretive media, and public-facing "
            "initiatives in coordination with museum leadership, curatorial, education, guest "
            "services, and operations teams. Reported to the President &amp; CEO and led a "
            "13-person department across graphic design, marketing, media relations, video "
            "production and social media, on a $2.5M annual operating budget."
        ),
        bullets=[
            "Led a 13-person department spanning graphic design, marketing, media relations, video production and social media, with hiring, structure and development responsibility for the function.",
            "Led website redesign for Mount Vernon, prioritizing content marketing to enhance educational outreach and drive increased visitation via organic SEO impact, boosting annual visitation from 2.5M to 8M+ visitors and 18M+ pageviews per year.",
            "Produced Mount Vernon's immersive virtual tour, attracting 4M+ visitors with average dwell time of 18 minutes. Widely used in classrooms nationwide.",
            "Achieved major growth in e-commerce revenue from $1.1M in 2015 to $8.6M in 2021 by leading strategic initiatives, marketing innovations, and seamless online shopping experiences.",
            "Directed end-to-end creation of award-winning <i>Be Washington</i> interactive theater — a $3.5M capital project that received the 2018 Thea Outstanding Achievement Award.",
            "Functioned as Executive Producer of award-winning short films including <i>Yorktown Now or Never</i>, <i>The Winter Patriots</i>, <i>A More Perfect Union</i>, <i>Washington's War</i>, and <i>George Washington and the Pursuit of Religious Freedom</i>. Films received Telly Awards and distribute on Amazon Prime, Apple TV, Google Play, and Curiosity Stream.",
            "Administered public affairs logistics for high-profile VVIP visits, including President Biden, President Trump, King Charles, Benjamin Netanyahu, and President Zelensky.",
            "Led successful revamping of the estate's pricing models, leading to a 30% increase in new members within the first year.",
            "Replatformed and produced the estate's audio tour on Guide ID's Podcatcher Pro, replacing a $7 add-on with a free-with-admission tour of 53+ stops, 4+ hours of podcast-style audio, and accessibility in five languages.",
            "Served as the editor of <i>Mount Vernon Magazine</i> (Winter 2020 — Spring 2024), overseeing the tri-annual print publication combining long-form scholarship from working historians and curators with donor stewardship.",
            "Created a groundbreaking augmented-reality tour utilizing Epson Moverio smartglasses with ARtGlass — making Mount Vernon one of the first U.S. historic sites with a regular wearable-AR visitor offering.",
            "Steered end-to-end migration of Mount Vernon's web and database platforms to AWS, yielding a 35% reduction in operating costs.",
            "Implemented an enhanced email program achieving a 38% revenue increase through meticulous segmentation, A/B testing, and mobile optimization.",
        ],
    ),
    dict(
        title="Vice President, Technical Manager",
        dates="2011 — 2014",
        company="Edelman Public Relations — Washington, DC",
        summary=(
            "Orchestrated design and execution of Edelman's exclusive Salesforce.com database "
            "marketing platform, Multiplier, offering efficient engagement analytics spanning "
            "web, social, email, and offline initiatives. Delivered strategic marketing "
            "insights and technical guidance to prominent brands across a portfolio of 60+ projects."
        ),
        bullets=[
            "Implemented and managed grassroots advocacy campaigns for prominent organizations including American Petroleum Institute, Pfizer, Microsoft, Walmart, Pepsi, Halliburton, the Episcopal Church, and the Embassy of Canada.",
            "Hired by HP CEO Meg Whitman to lead internal communications amid rapid leadership changes. Created HPNN, an internal news platform using native HP technologies.",
            "Headed development and deployment of a B2G (Business-to-Government) website for BlackBerry RIM, highlighting the robust security features of BlackBerry systems for secure government communications.",
            "In 24 hours, created an interactive tool using Multiplier technology to tackle Hyundai's fuel economy miscalculation, calculating MPG discrepancies by VIN, factoring in state-specific fuel prices, and allowing owners to file fuel reimbursement claims.",
            "Engineered a bespoke digital publishing system for Chevron, enabling safe internal communication while prioritizing data confidentiality and employee privacy.",
            "Designed a user-friendly internal communications tool using Salesforce.com for seamless employee communication and collaboration within General Electric.",
        ],
    ),
    dict(
        title="Vice President",
        dates="2005 — 2011",
        company="Emotive, LLC — Arlington, VA",
        summary=(
            "Pioneered the establishment of an interactive direct marketing agency, leading from "
            "conceptualization to execution. Offered strategic marketing consulting to 40+ "
            "prestigious non-profit organizations, political candidates, and trade associations "
            "including the Pickens Plan, the Alzheimer's Association, the Republican National "
            "Committee, and the Martin Luther King, Jr. National Memorial Project."
        ),
        bullets=[
            "Designed and executed marketing and fundraising strategies for the Martin Luther King, Jr. National Memorial capital campaign — managed digital ticketing for the 2006 groundbreaking, distributed Morgan Freeman's celebrity advocacy spots, and raised $15M+ through digital outreach toward the memorial's ~$120M total cost.",
            "Headed digital marketing for T. Boone Pickens' Pickens Plan campaign to reduce US gasoline dependency. Managed a Super Bowl ad campaign and a live-stream event that attracted millions; the petition amassed millions of signatures.",
            "Executed digital fundraising campaigns for high-profile political figures including Governors Schwarzenegger, Kasich, and Haslam; Senator McConnell, Senator Bennett, and Senator Allen; and the Republican National, Congressional, and Senatorial Committees.",
            "Transformed open-source CRM CiviCRM for political campaigns, contributing source code to enhance the platform's email throughput via efficient server multi-threading.",
            "Managed and maintained Emotive's technology alliances with Blackbaud Sphere, Blackbaud Convio 360, and Blackbaud Raiser's Edge.",
            "Unified and spearheaded a multidisciplinary team comprising account managers, graphic designers, and web application developers.",
            "Grew company's annual revenue to $5.7M through effective management and execution of business strategies.",
        ],
    ),
]

ADDITIONAL = [
    ("Director of Strategic Marketing",
     "American International Automobile Dealers Association — Alexandria, VA"),
    ("Web Properties Manager",
     "DCI Group — Washington, DC"),
]

EDUCATION = ("Bachelor of Arts, Interdisciplinary Studies",
             "Virginia Tech — Blacksburg, VA",
             "Minors in Communications, Graphic Design, and Humanities")

BOARDS = [
    "<b>Board Member, Secretary</b> — Visit Fairfax (2019–2022)",
    "<b>Participating Member</b> — Mount Vernon Tourism Taskforce (2019–2022)",
    "<b>Board Member</b> — The Campagna Center, Alexandria (2013–2016)",
]


# -------------------------------------------------------------- header
def _draw_header(canvas, doc):
    """Page header — name + contact lockup on page 1; running title on later pages."""
    canvas.saveState()
    page = canvas.getPageNumber()
    if page == 1:
        return  # the in-flow header is the page 1 header
    # Pages 2+: thin running header
    canvas.setFont("Fraunces-Sb", 9)
    canvas.setFillColor(INK)
    canvas.drawString(doc.leftMargin, LETTER[1] - 0.5 * inch,
                      "Matt Briney  ·  Curriculum Vitae")
    canvas.setFont("Inter", 8)
    canvas.setFillColor(INK_MUTED)
    canvas.drawRightString(LETTER[0] - doc.rightMargin,
                           LETTER[1] - 0.5 * inch,
                           f"Page {page}  ·  mattbriney.com")
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.4)
    canvas.line(doc.leftMargin, LETTER[1] - 0.58 * inch,
                LETTER[0] - doc.rightMargin, LETTER[1] - 0.58 * inch)
    canvas.restoreState()


def _draw_footer(canvas, doc):
    """Site-style footer with name + contact."""
    canvas.saveState()
    page = canvas.getPageNumber()
    canvas.setFont("Inter", 7.5)
    canvas.setFillColor(INK_MUTED)
    canvas.drawString(doc.leftMargin, 0.4 * inch,
                      f"Matt Briney  ·  mkbriney@gmail.com  ·  Dallas, TX")
    canvas.drawRightString(LETTER[0] - doc.rightMargin, 0.4 * inch,
                           f"mattbriney.com  ·  Page {page}")
    canvas.restoreState()


# -------------------------------------------------------------- build
def build_pdf(out_path):
    doc = BaseDocTemplate(
        out_path,
        pagesize=LETTER,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
        title="Matt Briney — Curriculum Vitae",
        author="Matt Briney",
        subject="Resume",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin,
                  doc.width, doc.height, id="normal",
                  leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="all", frames=[frame],
                     onPage=lambda c, d: (_draw_header(c, d), _draw_footer(c, d))),
    ])

    story = []

    # --- Header block (page 1 only — flowable, not canvas)
    header = Table(
        [[
            [Paragraph("CURRICULUM VITAE", S["eyebrow"]),
             Paragraph(CV_NAME, S["name"]),
             Paragraph(CV_ROLE, S["role"])],
            Paragraph(CV_CONTACT, S["contact"]),
        ]],
        colWidths=[4.7 * inch, 2.6 * inch],
        style=TableStyle([
            ("VALIGN", (0,0), (0,0), "TOP"),
            ("VALIGN", (1,0), (1,0), "TOP"),
            ("LEFTPADDING", (0,0), (-1,-1), 0),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
            ("TOPPADDING", (0,0), (-1,-1), 0),
            ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ]),
    )
    story.append(header)
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=GOLD,
                            spaceBefore=0, spaceAfter=4))

    # --- Summary
    story += h2("Summary")
    story.append(Paragraph(SUMMARY[0], S["lead"]))
    story.append(Paragraph(SUMMARY[1], S["body"]))

    # --- Expertise
    story += h2("Areas of Expertise")
    story.append(expertise_grid(EXPERTISE, cols=3))
    story.append(Spacer(1, 6))

    # --- Career
    story += h2("Career Experience")
    for r in ROLES:
        story += role(r["title"], r["dates"], r["company"],
                      r["summary"], r["bullets"])

    # --- Additional
    story += h2("Additional Experience")
    for title, company in ADDITIONAL:
        story.append(Paragraph(title, S["role_title"]))
        story.append(Paragraph(company, S["role_company"]))
        story.append(Spacer(1, 4))

    # --- Education
    story += h2("Education")
    title, company, sub = EDUCATION
    story.append(Paragraph(title, S["role_title"]))
    story.append(Paragraph(company, S["role_company"]))
    story.append(Paragraph(sub, S["summary"]))

    # --- Boards
    story += h2("Boards &amp; Affiliations")
    for b in BOARDS:
        story.append(Paragraph(f"<font color='#a06b2c'>▪</font>&nbsp;&nbsp;{b}",
                               S["board"]))

    doc.build(story)


if __name__ == "__main__":
    out = os.path.join(ROOT, "files", "Matt-Briney-Resume.pdf")
    build_pdf(out)
    print(f"Wrote {out}  ({os.path.getsize(out)/1024:.1f} KB)")
