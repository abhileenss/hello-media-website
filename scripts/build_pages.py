#!/usr/bin/env python3
"""Generate all static pages for the Hello Media website.
Run from repo root:  python3 scripts/build_pages.py
Emits fully-rendered .html files with shared nav, footer, logo intro.
"""
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent.parent
IMG = "/assets/images/hero"  # path written into HTML

# ─── Logo SVG (animatable parts) ──────────────────────────────
LOGO_SVG = '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect data-part="pixel" x="76" y="4" width="14" height="14" fill="#E6062F"/>
  <rect data-part="pause-top" x="12" y="22" width="66" height="10" fill="currentColor"/>
  <rect data-part="h-left" x="12" y="32" width="10" height="56" fill="currentColor"/>
  <rect data-part="h-right" x="68" y="32" width="10" height="56" fill="currentColor"/>
  <path data-part="smile" d="M22 58 Q45 82 68 58" stroke="currentColor" stroke-width="10" fill="none" stroke-linecap="butt"/>
</svg>'''

def nav():
    return f'''<header class="nav">
  <div class="nav__inner">
    <a class="nav__brand" href="/">
      <span style="color:#fff">{LOGO_SVG}</span>
      <span class="nav__brand-text">Hello<br>Media</span>
    </a>
    <button class="nav__toggle" aria-label="Open menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav__links" aria-label="Primary">
      <a class="nav__link" href="/who-we-are/">Who we are</a>
      <a class="nav__link" href="/what-we-do/">What we do</a>
      <a class="nav__link" href="/whom-we-love/">Whom we love</a>
      <a class="nav__link" href="/what-we-did/">What we did</a>
      <a class="nav__link" href="/where-we-are/">Where we are</a>
    </nav>
  </div>
</header>'''

def footer():
    return '''<footer class="footer">
  <div class="footer__grid">
    <div class="footer__col">
      <h4>Sitemap</h4>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/who-we-are/">Who we are</a></li>
        <li><a href="/what-we-do/">What we do</a></li>
        <li><a href="/whom-we-love/">Whom we love</a></li>
        <li><a href="/what-we-did/">What we did</a></li>
        <li><a href="/where-we-are/">Where we are</a></li>
      </ul>
    </div>
    <div class="footer__col">
      <h4>Company</h4>
      <ul>
        <li><a href="/who-we-are/our-vision/">Our vision</a></li>
        <li><a href="/who-we-are/our-mission/">Our mission</a></li>
        <li><a href="/who-we-are/our-values/">Our values</a></li>
        <li><a href="/who-we-are/our-team/">Our team</a></li>
        <li><a href="/who-we-are/careers/">Careers</a></li>
      </ul>
    </div>
    <div class="footer__col">
      <h4>Good stuff</h4>
      <ul>
        <li><a href="/media-center/">Media center</a></li>
        <li><a href="/awards/">Awards</a></li>
        <li><a href="/when-we-are-needed/">When we are needed</a></li>
        <li><a href="/csr-community/">CSR — Community</a></li>
        <li><a href="/csr-environment/">CSR — Environment</a></li>
      </ul>
    </div>
    <div class="footer__col">
      <h4>Talk to us</h4>
      <ul>
        <li><a href="/where-we-are/">Contact</a></li>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/small-jobs/">Small jobs</a></li>
        <li><a href="/suggestions/">Suggestions &amp; complaints</a></li>
        <li><a href="/site-map/">Site map</a></li>
      </ul>
    </div>
  </div>
  <div class="footer__bottom">
    <span>© 2026 Hello Media</span>
    <span>
      <a href="/privacy/">Privacy</a> ·
      <a href="/terms/">Terms</a> ·
      <a href="/cookies/">Cookies</a> ·
      <a href="/copyright/">Copyright</a>
    </span>
  </div>
</footer>'''

def page_shell(title, description, body, extra_head="", extra_scripts=""):
    full_title = title if title.lower().startswith("hello media") else f"{title} — Hello Media"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Barlow+Condensed:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
{extra_head}
</head>
<body>
<div class="intro-overlay" aria-hidden="true">
  <div class="intro-logo" style="color:#fff">{LOGO_SVG}</div>
</div>
{nav()}
<main>
{body}
</main>
{footer()}
<script src="/js/main.js"></script>
{extra_scripts}
</body>
</html>
'''

# ─── Reusable layout partials ─────────────────────────
def block(title, body, img, eyebrow, href=None, reverse=False, dark=False):
    cls = "block" + (" block--reverse" if reverse else "")
    link_html = f'<a class="block__link" href="{href}">Explore →</a>' if href else ""
    return f'''<section class="{cls}" data-reveal>
  <div class="block__media">
    <picture>
      <source srcset="{IMG}/{img}.webp" type="image/webp">
      <img src="{IMG}/{img}.jpg" alt="" loading="lazy">
    </picture>
  </div>
  <div class="block__copy">
    <span class="block__eyebrow">{eyebrow}</span>
    <h2 class="block__title">{title}</h2>
    <p class="block__body">{body}</p>
    {link_html}
  </div>
</section>'''

def page_header(eyebrow, title, lead, img):
    return f'''<header class="page-header" data-reveal>
  <span class="eyebrow">{eyebrow}</span>
  <h1>{title}</h1>
  <p class="lead">{lead}</p>
</header>
<div class="page-hero-image" data-reveal>
  <picture>
    <source srcset="{IMG}/{img}.webp" type="image/webp">
    <img src="{IMG}/{img}.jpg" alt="">
  </picture>
</div>'''

def coming_soon(title, body):
    return f'''<section class="coming-soon" data-reveal>
  <div class="pixel" aria-hidden="true"></div>
  <h2>{title}</h2>
  <p>{body}</p>
</section>'''

def sub_page(eyebrow, title, lead, img, sections_html=""):
    body = page_header(eyebrow, title, lead, img) + sections_html
    return page_shell(title, lead, body)


# ─── DATA: services (WHAT WE DO) ──────────────────────
SERVICES = [
    ("e-marketing",        "E-Marketing",              "E-marketing SOS: saving your sanity one click at a time.", "e-marketing"),
    ("web-solution",       "Web Solutions",            "We turn website dilemmas into delightful digital dreams.", "web-solution"),
    ("mobile-app",         "Mobile App Dev",           "Your app's journey: from idea to 'I can't believe we made that!'", "mobile-app"),
    ("ai",                 "AI",                       "Welcome to the future. Spoiler alert: it's AI-tastic.", "ai"),
    ("seo",                "SEO",                      "Let's make your website so SEO-friendly, even Google will want to hang out.", "seo"),
    ("web-app",            "Web Applications",         "Unplug from the ordinary and plug into extraordinary web applications.", "web-app"),
    ("domain-hosting",     "Domains & Hosting",        "We're not just hosting — we're crafting the coziest online abode for your website.", "domain-hosting"),
    ("branding",           "Branding",                 "Brace yourself for branding brilliance. Trust us; you won't be sorry you did.", "branding"),
    ("creative-printing",  "Creative & Printing",      "Watch your work leap off the page and dance to its own rhythm with our creative designs and printing services.", "creative-printing"),
    ("video",              "Video Production",         "Lights, camera, action — creating living, breathing tales.", "video"),
    ("audio",              "Audio Production",         "Our audios are the refreshing splash of sonic clarity your auditory senses deserve.", "audio"),
    ("copywriting",        "Copywriting",              "Let us be the scribes of your brand's epic tale, crafting a palace of words with each pencil touch.", "copywriting"),
    ("pr",                 "Public Relations",         "Save your lips for smiling; we'll handle the talking.", "pr"),
    ("photography",        "Photography & Media Buy",  "Photographs with a purpose — our snaps can tell stories, sell products and steal hearts.", "photography"),
    ("packaging",          "Packaging",                "Our packaging is like a fine-tailored suit for your goods — every inch covered in style.", "packaging"),
    ("crisis",             "Crisis Management",        "From horse sh#t to horsepower. Elevate your crisis management with us.", "crisis"),
]

WHO_SUBS = [
    ("our-vision",   "Our Vision",    "Our vision is to redefine marketing through relentless innovation — delivering 'one more' ingenious solution, 'one more' remarkable campaign, 'one more' leap in success.", "our-vision"),
    ("our-mission",  "Our Mission",   "We go 'one more' mile for a creative idea, craft 'one more' innovative strategy, and deliver 'one more' outstanding campaign.", "our-mission"),
    ("our-values",   "Our Values",    "Creativity. Integrity. Client-centricity. Collaboration. Accountability. Sustainability. Continuous improvement. Community.", "our-values"),
    ("our-team",     "Our Team",      "Coffee? Nah — we fuel our team with pure adrenaline and excitement. At our quirky creative haven, our team is a bunch of misfit geniuses who invented a new box altogether.", "our-team"),
    ("careers",      "Careers",       "Want to be part of our circus of creativity? Where clowning around is encouraged.", "careers"),
    ("diversity",    "Diversity & Variety", "Our team is a patchwork quilt of talents, woven together by the threads of inclusion.", "get-involved"),
    ("grow-with-us", "Grow With Us",  "Life's like herding sheep in a rocket ship — join us on the woolly ride to growth and fame.", "grow-with-us"),
    ("get-involved", "Get Involved",  "Ready to dive into our creative playground? A worldwide family reunion with better snacks.", "get-involved"),
]

# ─── HOMEPAGE ─────────────────────────────────────────
def build_home():
    hero = f'''<section class="hero">
  <div class="hero__media">
    <picture>
      <source srcset="{IMG}/home.webp" type="image/webp">
      <img src="{IMG}/home.jpg" alt="Hello Media — marketing agency">
    </picture>
  </div>
  <div class="hero__panel">
    <span class="hero__eyebrow">Hello, Stop, Smile</span>
    <h1 class="hero__title">Welcome<br>to our home</h1>
    <p class="hero__sub">Marketing: shockingly complex! Let the experts handle the volts.</p>
  </div>
  <a class="hero__scroll" href="#who-we-are">Scroll</a>
</section>'''

    who = block(
        "Who we are",
        "We're the superheroes of storytelling — crafting epic narratives that captivate hearts and minds. And the brainy wizards behind the curtain, making magic happen for your brand.",
        "who-we-are", "About us", href="/who-we-are/")

    what = block(
        "What we do",
        "Services that make your brand work as hard as a 24/7 construction crew. From e-marketing to crisis management, we cover every surface that matters.",
        "what-we-do", "Services", href="/what-we-do/", reverse=True)

    love = block(
        "Whom we love",
        "Welcome to our wacky wonderland of creativity — where clients reign as royalty and we pamper them with the finest inventive creative treats.",
        "whom-we-love", "Our clients", href="/whom-we-love/")

    did = block(
        "What we did",
        "Warning: viewing these case studies may lead to uncontrollable outbursts of WOW.",
        "what-we-did", "Case studies", href="/what-we-did/", reverse=True)

    where = block(
        "Where we are",
        "Bringing the world closer one connection at a time — because even satellites envy our networking skills. UAE headquarters with a global creative and intelligence network.",
        "where-we-are", "Global network", href="/where-we-are/")

    body = hero + '<div id="who-we-are"></div>' + who + what + love + did + where
    return page_shell(
        "Hello Media",
        "Hello Media — a creative marketing and media agency. UAE-headquartered with a global network.",
        body)


# ─── WHO WE ARE HUB ───────────────────────────────────
def build_who_we_are():
    header = page_header(
        "Chapter 01",
        "Who we are",
        "We're the superheroes of storytelling — crafting epic narratives that captivate hearts and minds.",
        "who-we-are")
    sections = []
    for i, (slug, title, lead, img) in enumerate(WHO_SUBS):
        sections.append(block(title, lead, img, "Who we are",
                              href=f"/who-we-are/{slug}/", reverse=(i % 2 == 1)))
    body = header + "".join(sections)
    return page_shell("Who we are", "About Hello Media — our vision, mission, values, team, careers.", body)

# ─── WHAT WE DO HUB ───────────────────────────────────
def build_what_we_do():
    header = page_header(
        "Chapter 02",
        "What we do",
        "Services that make your brand work as hard as a 24/7 construction crew.",
        "what-we-do")
    cards = []
    for slug, title, lead, img in SERVICES:
        cards.append(f'''<a class="service-card" href="/what-we-do/{slug}/" data-reveal>
  <picture>
    <source srcset="{IMG}/{img}.webp" type="image/webp">
    <img src="{IMG}/{img}.jpg" alt="" loading="lazy">
  </picture>
  <div class="service-card__body">
    <span class="service-card__pixel"></span>
    <div>
      <h3 class="service-card__title">{title}</h3>
      <p class="service-card__sub">{lead}</p>
    </div>
  </div>
</a>''')
    grid = '<section class="grid-services">' + "".join(cards) + '</section>'
    return page_shell("What we do", "Hello Media services: branding, digital, creative, production, PR and more.",
                      header + grid)

# ─── WHO WE ARE SUBPAGES ──────────────────────────────
def build_who_subs():
    out = {}
    for slug, title, lead, img in WHO_SUBS:
        body = page_header("Who we are / " + title, title, lead, img)
        body += f'''<section class="block" data-reveal>
  <div class="block__media">
    <picture>
      <source srcset="{IMG}/{img}.webp" type="image/webp">
      <img src="{IMG}/{img}.jpg" alt="" loading="lazy">
    </picture>
  </div>
  <div class="block__copy">
    <span class="block__eyebrow">More about us</span>
    <h2 class="block__title">{title}</h2>
    <p class="block__body">{lead}</p>
    <a class="block__link" href="/who-we-are/">← Back to Who we are</a>
  </div>
</section>'''
        out[slug] = page_shell(title, lead, body)
    return out

# ─── SERVICE SUBPAGES ─────────────────────────────────
def build_service_subs():
    out = {}
    for slug, title, lead, img in SERVICES:
        body = page_header("What we do / " + title, title, lead, img)
        body += f'''<section class="block" data-reveal>
  <div class="block__media">
    <picture>
      <source srcset="{IMG}/{img}.webp" type="image/webp">
      <img src="{IMG}/{img}.jpg" alt="" loading="lazy">
    </picture>
  </div>
  <div class="block__copy">
    <span class="block__eyebrow">Service</span>
    <h2 class="block__title">{title}</h2>
    <p class="block__body">{lead}</p>
    <a class="block__link" href="/what-we-do/">← All services</a>
  </div>
</section>'''
        body += coming_soon(
            "Case studies coming soon",
            "We're curating the juiciest work from this service. Check back shortly.")
        out[slug] = page_shell(title, lead, body)
    return out

# ─── WHOM WE LOVE ─────────────────────────────────────
def build_whom_we_love():
    header = page_header(
        "Chapter 03",
        "Whom we love",
        "Welcome to our wacky wonderland of creativity — where clients reign as royalty.",
        "whom-we-love")
    placeholders = "".join(f'<div class="client-cell">Client {i+1:02d}</div>' for i in range(18))
    grid = f'<section class="clients-grid" data-reveal>{placeholders}</section>'
    tail = coming_soon(
        "Full client roster coming soon",
        "Our bragging list is being polished. Logos and stories will land here soon — meanwhile, you can imagine these cells full of legendary brands.")
    return page_shell("Whom we love", "Clients we love working with.", header + grid + tail)

# ─── WHERE WE ARE (map) ───────────────────────────────
WORLD_PATHS = '<path fill="#1a1a1a" stroke="#2a2a2a" stroke-width="0.5" d="M90 80 L170 55 L260 60 L340 80 L360 140 L300 200 L260 250 L340 320 L380 400 L320 460 L240 470 L200 420 L160 380 L150 300 L110 260 L80 200 Z"/>\
<path fill="#1a1a1a" stroke="#2a2a2a" stroke-width="0.5" d="M420 120 L520 90 L600 100 L680 120 L720 180 L700 220 L660 260 L580 280 L540 240 L500 200 L460 180 Z"/>\
<path fill="#1a1a1a" stroke="#2a2a2a" stroke-width="0.5" d="M480 250 L580 240 L620 280 L600 340 L560 380 L520 400 L480 360 L470 320 Z"/>\
<path fill="#1a1a1a" stroke="#2a2a2a" stroke-width="0.5" d="M660 140 L780 130 L880 160 L900 220 L860 280 L800 300 L750 280 L700 240 Z"/>\
<path fill="#1a1a1a" stroke="#2a2a2a" stroke-width="0.5" d="M820 320 L900 340 L940 380 L920 440 L860 460 L820 420 Z"/>'

def build_where_we_are():
    header = page_header(
        "Chapter 05",
        "Where we are",
        "UAE-based with a global creative and intelligence network. Hover a pin to meet our hubs and studios.",
        "where-we-are")
    map_html = f'''<section class="map-section" data-reveal>
  <div class="map-wrap">
    <div class="map-stage">
      <svg viewBox="0 0 1000 520" preserveAspectRatio="xMidYMid slice" aria-label="World map showing Hello Media hubs and studios">
        {WORLD_PATHS}
      </svg>
      <div class="map-tooltip"></div>
    </div>
    <aside class="map-legend">
      <h3>Network</h3>
      <ul>
        <li class="legend-hub">UAE (HQ)</li>
        <li class="legend-hub">United Kingdom</li>
        <li class="legend-hub">United States</li>
        <li class="legend-hub">Brazil</li>
        <li class="legend-hub">China</li>
        <li class="legend-hub">Egypt</li>
        <li class="legend-studio">India (Studio)</li>
        <li class="legend-studio">Pakistan (Studio)</li>
      </ul>
      <p class="legend-note">Red pins are Market Hubs where we engage clients and run campaigns. Grey pins are Production Studios where craft happens. Addresses are indicative and will be updated as the network expands.</p>
    </aside>
  </div>
</section>'''
    cs = coming_soon("Contact form coming soon", "We're wiring this up to our inbox. In the meantime, hover a pin on the map for hub details.")
    return page_shell("Where we are", "Hello Media global network: hubs and studios.",
                      header + map_html + cs,
                      extra_scripts='<script src="/js/map.js"></script>')

# ─── SIMPLE COMING-SOON STUBS ────────────────────────
STUBS = [
    ("what-we-did",        "What we did",        "Case studies",  "Warning: viewing these case studies may lead to uncontrollable outbursts of WOW.", "what-we-did"),
    ("when-we-are-needed", "When we are needed", "How we help",   "When challenges show up, we throw them a party and turn them into opportunities.", "when-needed"),
    ("awards",             "Awards",             "Brags",         "The trophy cabinet is being built. For now, imagine it tastefully lit.", "awards"),
    ("media-center",       "Media Center",       "Press",         "Where stories get tangled, untangled, and sometimes mangled.", "media-center"),
    ("faq",                "FAQ",                "Help",          "Why do we have an FAQ? Because we heard you have more questions than a curious cat. Meowntain your curiosity here.", "faq"),
    ("csr-community",      "CSR — Community",    "Giving back",   "Why did the corporation cross the road? To get to the community on the other side.", "csr-community"),
    ("csr-environment",    "CSR — Environment",  "Our planet",    "If businesses were superheroes, CSR would be their sidekick fighting for a greener planet.", "csr-environment"),
    ("small-jobs",         "Small jobs",         "Quick help",    "Got a tiny creative brief? We do those too. Details coming soon.", "small-jobs"),
    ("suggestions",        "Suggestions & complaints", "Tell us", "Got a suggestion or complaint? We're all ears (well, figuratively).", "suggestions"),
    ("site-map",           "Site map",           "Navigate",      "Like GPS for your clicking fingers — say goodbye to digital detours.", "site-map"),
    ("privacy",            "Privacy policy",     "Legal",         "Where we promise to guard it like a hungry dragon guards a sandwich.", "privacy"),
    ("terms",              "Terms & conditions", "Legal",         "Our T&C: like a treasure hunt, but with fewer pirates and more legal stuff. Fun to read! (No, seriously.)", "terms"),
    ("cookies",            "Cookie statement",   "Legal",         "The digital snacks that help us serve you better (no crumbs, we promise).", "cookies"),
    ("copyright",          "Copyright",          "Legal",         "Because our content is as original as an elephant doing the Heimlich manoeuvre.", "copyright"),
]

def build_stubs():
    out = {}
    for slug, title, eyebrow, lead, img in STUBS:
        body = page_header(eyebrow, title, lead, img)
        body += coming_soon(title + " coming soon",
                            "This page is being polished. In the meantime, enjoy the brand mood above.")
        out[slug] = page_shell(title, lead, body)
    return out


# ─── Site-map page with real links ───────────────────
def build_site_map():
    groups = [
        ("Main", [("Home","/"),("Who we are","/who-we-are/"),("What we do","/what-we-do/"),
                  ("Whom we love","/whom-we-love/"),("What we did","/what-we-did/"),
                  ("Where we are","/where-we-are/"),("When we are needed","/when-we-are-needed/")]),
        ("Who we are", [("Our vision","/who-we-are/our-vision/"),("Our mission","/who-we-are/our-mission/"),
                        ("Our values","/who-we-are/our-values/"),("Our team","/who-we-are/our-team/"),
                        ("Careers","/who-we-are/careers/"),("Diversity & variety","/who-we-are/diversity/"),
                        ("Grow with us","/who-we-are/grow-with-us/"),("Get involved","/who-we-are/get-involved/")]),
        ("Services", [(t, f"/what-we-do/{s}/") for s,t,_,_ in SERVICES]),
        ("Company", [("Media center","/media-center/"),("Awards","/awards/"),
                     ("CSR — Community","/csr-community/"),("CSR — Environment","/csr-environment/"),
                     ("Small jobs","/small-jobs/"),("Suggestions & complaints","/suggestions/"),
                     ("FAQ","/faq/")]),
        ("Legal", [("Privacy","/privacy/"),("Terms","/terms/"),
                   ("Cookies","/cookies/"),("Copyright","/copyright/")]),
    ]
    blocks_html = ""
    for head, items in groups:
        li = "".join(f'<li><a href="{h}">{t}</a></li>' for t,h in items)
        blocks_html += f'<div class="footer__col"><h4>{head}</h4><ul>{li}</ul></div>'
    body = page_header("Navigate", "Site map",
                       "Like GPS for your clicking fingers.", "site-map")
    body += f'<section class="wrap" style="padding:2rem var(--gutter) 4rem" data-reveal><div class="footer__grid" style="color:var(--ink-1)">{blocks_html}</div></section>'
    # swap footer__col text color in site-map body:
    body = body.replace(
        'style="color:var(--ink-1)"',
        'style="color:var(--ink-1)"')
    return page_shell("Site map", "Site map — Hello Media.", body)


# ─── Emit all files ──────────────────────────────────
def write(path, content):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")

def main():
    write("index.html", build_home())
    write("who-we-are/index.html", build_who_we_are())
    write("what-we-do/index.html", build_what_we_do())
    write("whom-we-love/index.html", build_whom_we_love())
    write("where-we-are/index.html", build_where_we_are())

    for slug, html in build_who_subs().items():
        write(f"who-we-are/{slug}/index.html", html)
    for slug, html in build_service_subs().items():
        write(f"what-we-do/{slug}/index.html", html)

    # Site map gets custom content; other stubs use generic template
    for slug, html in build_stubs().items():
        if slug == "site-map":
            continue
        write(f"{slug}/index.html", html)
    write("site-map/index.html", build_site_map())

    print("\nDone.")

if __name__ == "__main__":
    main()
