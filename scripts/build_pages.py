#!/usr/bin/env python3
"""Generate all static pages for the Hello Media website.
Run from repo root:  python3 scripts/build_pages.py
Emits fully-rendered .html files with shared nav, footer, logo intro.
"""
from pathlib import Path
from textwrap import dedent
import time

ROOT = Path(__file__).resolve().parent.parent
IMG = "/assets/images/hero"  # path written into HTML
# Cache-buster: bump automatically at build time so browsers always
# refetch CSS and JS when we redeploy.
VER = time.strftime("%Y%m%d%H%M")

# Focal-point metadata per hero image.
# Graphics can tune these without touching CSS; defaults to "center" when unset.
# Values map 1:1 to CSS object-position (X Y, e.g. "50% 30%" or "center top").
FOCAL_POINTS = {
    "home":           "50% 55%",
    "who-we-are":     "50% 40%",
    "what-we-do":     "50% 45%",
    "whom-we-love":   "50% 50%",
    "what-we-did":    "50% 45%",
    "where-we-are":   "50% 50%",
    "when-needed":    "50% 40%",
    # Services — faces and product detail generally in the upper third
    "e-marketing":    "50% 35%",
    "web-solution":   "50% 45%",
    "mobile-app":     "50% 40%",
    "ai":             "50% 40%",
    "seo":            "50% 45%",
    "web-app":        "50% 45%",
    "domain-hosting": "50% 45%",
    "branding":       "50% 40%",
    "creative-printing": "50% 45%",
    "video":          "50% 40%",
    "audio":          "50% 45%",
    "copywriting":    "50% 45%",
    "pr":             "50% 40%",
    "photography":    "50% 40%",
    "packaging":      "50% 45%",
    "crisis":         "50% 40%",
    # Who-we-are subpages
    "our-vision":     "50% 40%",
    "our-mission":    "50% 40%",
    "our-values":     "50% 45%",
    "our-team":       "50% 35%",
    "careers":        "50% 40%",
    "get-involved":   "50% 40%",
    "grow-with-us":   "50% 40%",
    # Country contacts
    "contact-uae":    "50% 50%",
    "contact-uk":     "50% 45%",
    "contact-usa":    "50% 45%",
    "contact-brazil": "50% 45%",
    "contact-china":  "50% 50%",
    "contact-egypt":  "50% 50%",
    "contact":        "50% 50%",
}

def focal(img_slug):
    return FOCAL_POINTS.get(img_slug, "center")

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

# ─── Social icons (inline SVG, no external deps) ───
# Handles are placeholders; platforms are locked in Chaadi's requested order.
SOCIAL_LINKS = [
    ("Facebook",  "#", '<path d="M13.5 3h-2.25A3.75 3.75 0 0 0 7.5 6.75V9H5.25v3H7.5v9h3v-9h2.4l.3-3h-2.7V7.125c0-.62.505-1.125 1.125-1.125H13.5V3z"/>'),
    ("Instagram", "#", '<path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3H7zm5 3.5A4.5 4.5 0 1 1 7.5 12 4.5 4.5 0 0 1 12 7.5zm0 2A2.5 2.5 0 1 0 14.5 12 2.5 2.5 0 0 0 12 9.5zm5-3.25a1 1 0 1 1-1 1 1 1 0 0 1 1-1z"/>'),
    ("Snapchat",  "#", '<path d="M12 2c3.1 0 5.5 2.1 5.5 5.3 0 1 .1 2.1.3 2.7.3.6 1.2.8 1.9.9.4 0 .6.3.5.6-.3.7-1.7 1-2.5 1.2-.2.1-.2.3-.1.6.3.7 1.7 2.5 3.9 2.9.3.1.4.4.2.6-.6.7-2.1.9-3.1 1-.1 0-.2.1-.2.3-.2.9-.3 1.2-.5 1.3-.2.1-1.5-.4-2.5-.4-1.3 0-2.1 1.3-4.4 1.3s-3-1.3-4.4-1.3c-1 0-2.3.5-2.5.4-.2-.1-.3-.4-.5-1.3 0-.2-.1-.3-.2-.3-1 0-2.5-.3-3.1-1-.2-.2-.1-.5.2-.6 2.2-.4 3.6-2.2 3.9-2.9.1-.3.1-.5-.1-.6-.8-.2-2.2-.5-2.5-1.2-.1-.3.1-.6.5-.6.7-.1 1.6-.3 1.9-.9.2-.6.3-1.7.3-2.7C6.5 4.1 8.9 2 12 2z"/>'),
    ("X",         "#", '<path d="M18.9 3h2.8l-6.1 7 7.2 11h-5.7l-4.5-6.7L7.4 21H4.6l6.5-7.5L4.2 3h5.8l4 6.1zm-1 16.5h1.6L7.2 4.4H5.5z"/>'),
    ("TikTok",    "#", '<path d="M16.5 2h-3v13.1a3.1 3.1 0 1 1-3.1-3.1c.33 0 .64.05.94.14V8.95a6.55 6.55 0 1 0 5.16 6.4V8.9a7.3 7.3 0 0 0 4.5 1.52V7.3a4.2 4.2 0 0 1-4.5-3.36V2z"/>'),
    ("YouTube",   "#", '<path d="M23 7.5s-.2-1.5-.8-2.2c-.8-.8-1.6-.8-2-.9C17 4.1 12 4.1 12 4.1s-5 0-8.2.3c-.5.1-1.3.1-2 .9C1.2 6 1 7.5 1 7.5S.8 9.3.8 11v1.7c0 1.8.2 3.5.2 3.5s.2 1.5.8 2.2c.8.8 1.8.8 2.3.9 1.6.2 7.9.3 7.9.3s5 0 8.2-.3c.5-.1 1.3-.1 2-.9.6-.7.8-2.2.8-2.2s.2-1.8.2-3.5V11c0-1.8-.2-3.5-.2-3.5zM9.75 14.4V8.6l5.3 2.9-5.3 2.9z"/>'),
    ("Pinterest", "#", '<path d="M12 2a10 10 0 0 0-3.64 19.31c-.09-.82-.17-2.08.04-2.97.18-.77 1.18-4.93 1.18-4.93s-.3-.6-.3-1.5c0-1.4.82-2.45 1.83-2.45.86 0 1.28.65 1.28 1.43 0 .87-.56 2.17-.84 3.38-.24 1.01.51 1.83 1.51 1.83 1.81 0 3.2-1.91 3.2-4.66 0-2.44-1.75-4.14-4.25-4.14-2.9 0-4.6 2.17-4.6 4.42 0 .88.34 1.82.76 2.33.08.1.09.19.07.29-.07.3-.24.96-.27 1.09-.04.18-.14.22-.33.13-1.21-.56-1.97-2.33-1.97-3.76 0-3.06 2.23-5.88 6.42-5.88 3.37 0 5.99 2.4 5.99 5.61 0 3.35-2.11 6.05-5.05 6.05-.99 0-1.91-.51-2.23-1.12l-.61 2.3c-.22.84-.81 1.9-1.2 2.54A10 10 0 1 0 12 2z"/>'),
    ("Flickr",    "#", '<path d="M7 7.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9zm10 0a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9z"/>'),
    ("LinkedIn",  "#", '<path d="M6.94 5A1.94 1.94 0 1 1 5 6.94 1.94 1.94 0 0 1 6.94 5zM5 9h3.88v12H5V9zm6.63 0h3.72v1.64h.05a4.08 4.08 0 0 1 3.67-2c3.93 0 4.65 2.58 4.65 5.94V21h-3.87v-5.43c0-1.3-.02-2.97-1.81-2.97s-2.09 1.41-2.09 2.87V21H11.6V9z"/>'),
]

def social_icons_html():
    items = []
    for name, href, path in SOCIAL_LINKS:
        items.append(
            f'<a href="{href}" aria-label="{name}" rel="noopener">'
            f'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">{path}</svg>'
            f'</a>'
        )
    return (
        '<div class="footer__social">'
        '<span class="footer__social-label">Follow</span>'
        + "".join(items)
        + '</div>'
    )

def footer():
    return f'''<footer class="footer">
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
  {social_icons_html()}
  <div class="footer__bottom">
    <span>© 2026 Hello Media</span>
    <span>
      <a href="/privacy/">Privacy</a> ·
      <a href="/terms/">Terms</a> ·
      <a href="/cookies/">Cookie statement</a> ·
      <a href="/copyright/">Copyright</a>
    </span>
  </div>
</footer>'''

def page_shell(title, description, body, extra_head="", extra_scripts="", og_image="/assets/images/hero/home.jpg"):
    if title.strip().lower() == "hello media":
        full_title = "Hello Media — Creative marketing agency, UAE + global"
    elif title.lower().startswith("hello media"):
        full_title = title
    else:
        full_title = f"{title} — Hello Media"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#000000">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/icons/icon-192.png">
<link rel="icon" type="image/png" sizes="512x512" href="/assets/icons/icon-512.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/icon-180.png">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Barlow+Condensed:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css?v={VER}">
{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="intro-overlay" aria-hidden="true">
  <div class="intro-logo" style="color:#fff">{LOGO_SVG}</div>
</div>
{nav()}
<main id="main">
{body}
</main>
{footer()}
<script src="/js/main.js?v={VER}"></script>
{extra_scripts}
</body>
</html>
'''

# ─── Reusable layout partials ─────────────────────────
def block(title, body, img, eyebrow, href=None, reverse=False, dark=False, alt=None, priority=False):
    cls = "block" + (" block--reverse" if reverse else "")
    link_html = f'<a class="block__link" href="{href}">Explore →</a>' if href else ""
    img_alt = alt if alt is not None else f"{title} — Hello Media"
    load_attrs = 'fetchpriority="high"' if priority else 'loading="lazy" decoding="async"'
    pos = focal(img)
    return f'''<section class="{cls}" data-reveal>
  <div class="block__media">
    <picture>
      <source srcset="{IMG}/{img}.webp" type="image/webp">
      <img src="{IMG}/{img}.jpg" alt="{img_alt}" style="object-position: {pos}" {load_attrs}>
    </picture>
  </div>
  <div class="block__copy">
    <span class="block__eyebrow">{eyebrow}</span>
    <h2 class="block__title">{title}</h2>
    <p class="block__body">{body}</p>
    {link_html}
  </div>
</section>'''

def page_header(eyebrow, title, lead, img, alt=None):
    img_alt = alt if alt is not None else f"{title} — Hello Media"
    pos = focal(img)
    return f'''<header class="page-header" data-reveal>
  <span class="eyebrow">{eyebrow}</span>
  <h1>{title}</h1>
  <p class="lead">{lead}</p>
</header>
<div class="page-hero-image" data-reveal>
  <picture>
    <source srcset="{IMG}/{img}.webp" type="image/webp">
    <img src="{IMG}/{img}.jpg" alt="{img_alt}" style="object-position: {pos}" fetchpriority="high">
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
    hero_pos = focal("home")
    hero = f'''<section class="hero">
  <div class="hero__media">
    <picture>
      <source srcset="{IMG}/home.webp" type="image/webp">
      <img src="{IMG}/home.jpg" alt="Hello Media — creative marketing agency, UAE &amp; global" style="object-position: {hero_pos}" fetchpriority="high">
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
        "who-we-are", "About us", href="/who-we-are/",
        alt="The Hello Media team in studio", priority=True)

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
        pos = focal(img)
        cards.append(f'''<a class="service-card" href="/what-we-do/{slug}/" data-reveal>
  <picture>
    <source srcset="{IMG}/{img}.webp" type="image/webp">
    <img src="{IMG}/{img}.jpg" alt="" style="object-position: {pos}" loading="lazy">
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
        pos = focal(img)
        body = page_header("Who we are / " + title, title, lead, img)
        body += f'''<section class="block" data-reveal>
  <div class="block__media">
    <picture>
      <source srcset="{IMG}/{img}.webp" type="image/webp">
      <img src="{IMG}/{img}.jpg" alt="" style="object-position: {pos}" loading="lazy">
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
        pos = focal(img)
        body = page_header("What we do / " + title, title, lead, img)
        body += f'''<section class="block" data-reveal>
  <div class="block__media">
    <picture>
      <source srcset="{IMG}/{img}.webp" type="image/webp">
      <img src="{IMG}/{img}.jpg" alt="" style="object-position: {pos}" loading="lazy">
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
                      extra_scripts=f'<script src="/js/map.js?v={VER}"></script>')

# ─── STUB PAGES — each with its own voice so the footer
#     doesn't read as mass copy-paste
#     Fields: (slug, title, eyebrow, lead, img, soon_title, soon_body)
STUBS = [
    ("what-we-did", "What we did", "Case studies",
     "Proof, not promises — a look at the work behind the words.",
     "what-we-did",
     "Case studies launching soon",
     "Our first three case studies are being written. Expect the full playbook: brief, craft, numbers, the good and the unexpected."),

    ("when-we-are-needed", "When we are needed", "How we help",
     "Launches, pivots, bad weeks, good weeks — the moments where marketing stops being a checkbox.",
     "when-needed",
     "Detailed scenarios coming soon",
     "We're putting together scenario pages — product launches, reputation management, rebrands and the in-between moments."),

    ("awards", "Awards", "Recognition",
     "We don't chase trophies, but when our clients' work earns them, we're proud to list them here.",
     "awards",
     "Trophy cabinet under construction",
     "We're pulling together the shortlist of wins — by client, by year, by craft. Live once verified with our partners."),

    ("media-center", "Media Center", "Press",
     "Press mentions, interviews, and the stories we've been part of.",
     "media-center",
     "Press room opening soon",
     "We're compiling press coverage, spokesperson bios, and logo kits. If you're a journalist needing something now, reach out directly."),

    ("faq", "FAQ", "Help",
     "The questions we hear most from new clients — answered honestly.",
     "faq",
     "FAQ being populated",
     "We're writing answers to the most common client questions: scope, timelines, pricing bands, how we work across countries. Check back soon."),

    ("csr-community", "CSR — Community", "Giving back",
     "Where we operate, we participate — local causes, pro-bono work and partnerships.",
     "csr-community",
     "Community initiatives launching soon",
     "We're documenting the partnerships, volunteer hours, and pro-bono engagements across our network. Honest numbers, not vanity."),

    ("csr-environment", "CSR — Environment", "Our planet",
     "A creative agency isn't carbon-free — we measure, reduce and report what we can.",
     "csr-environment",
     "Our environmental commitments coming soon",
     "Baseline measurements and reduction targets are being drafted. We'd rather publish real numbers than a green-washed statement."),

    ("small-jobs", "Small jobs", "Quick help",
     "Not every brief needs a retainer. A new logo, a one-off campaign, a deck that needs dressing — those too.",
     "small-jobs",
     "Small-jobs pricing coming soon",
     "We're finalising the package, turnaround windows and pricing tiers for small jobs. Until then, drop us a note and we'll quote directly."),

    ("suggestions", "Suggestions & complaints", "Tell us",
     "Feedback loops only work when both sides show up. Tell us what we got right, and where we missed.",
     "suggestions",
     "Feedback form coming soon",
     "We're wiring up a form that routes to the right person based on the type of feedback. Until then, please email us directly."),

    ("site-map", "Site map", "Navigate",
     "Every page on the site, in one place.",
     "site-map",
     "", ""),  # site-map has its own body builder; stub not used

    ("privacy", "Privacy policy", "Legal",
     "How we collect, use and protect your data when you visit this site or work with us.",
     "privacy",
     "Policy awaiting legal review",
     "Our privacy policy is being finalised with counsel for UAE PDPL, UK/EU GDPR and US compliance. The live version will land here before any form collects data."),

    ("terms", "Terms & conditions", "Legal",
     "The rules of engagement — what you can expect from us, what we expect from you.",
     "terms",
     "T&Cs awaiting legal review",
     "Our terms of service and engagement terms are with counsel — the consolidated version will publish here on sign-off. In the meantime, note: by using this site you agree to these terms as they stand, and to any updates we publish on this page. Content, imagery and ideas on the site are for informational use only, carry no warranty, and any reliance on them is at your own risk. You have no claim against Hello Media for decisions or actions taken on the basis of material on this site."),

    ("cookies", "Cookie statement", "Legal",
     "What cookies this site uses, why, and how to turn them off.",
     "cookies",
     "Cookie statement — pending legal sign-off",
     "The full statement is with counsel. In the meantime: this site currently uses only a session cookie to remember the intro animation has played. No third-party cookies or advertising trackers are set. By continuing to browse, you agree to this minimal use. Turning off cookies in your browser will not affect functionality."),

    ("copyright", "Copyright", "Legal",
     "Content, imagery and brand marks on this site — what's ours, what's licensed, what's yours.",
     "copyright",
     "Copyright notice being finalised",
     "We're documenting attributions for every third-party asset. Until that's complete, assume everything here is © Hello Media unless noted otherwise."),
]

def build_stubs():
    out = {}
    for slug, title, eyebrow, lead, img, soon_title, soon_body in STUBS:
        if slug == "site-map":
            continue  # custom builder
        if slug == "what-we-did":
            continue  # custom builder — hub lists case studies
        body = page_header(eyebrow, title, lead, img)
        body += coming_soon(soon_title, soon_body)
        out[slug] = page_shell(title, lead, body)
    return out

# ─── CASE STUDIES ─────────────────────────────────────
# Each: slug, title, client, tagline, hero_img, problem, analysis, solution, result
CASE_STUDIES = [
    (
        "sample",
        "Sample case study",
        "Placeholder client",
        "A walk-through of the template — real case studies will replace this.",
        "what-we-did",
        # Problem
        "This is a placeholder. When a real case study lands, this section states the client's situation before we got involved — the business problem, not a brief we were handed. Short, specific, honest.",
        # Analysis
        "What we investigated before proposing anything: audience research, category audit, competitive set, internal interviews, and any data we could put our hands on. The output is usually one insight that reframes the problem.",
        # Solution
        "The response: strategy headline, then craft. Campaign platform, channels, key assets, rollout timing, and the supporting work no one sees but that held everything together.",
        # Result
        "What moved. Business numbers first (sales, share, signups), then brand numbers (awareness, consideration, sentiment), then the softer signals (earned mentions, internal lift, award shortlists).",
    ),
]

def build_case_study(slug, title, client, tagline, img, problem, analysis, solution, result):
    pos = focal(img)
    hero = f'''<section class="case-hero">
  <div class="case-hero__media">
    <picture>
      <source srcset="{IMG}/{img}.webp" type="image/webp">
      <img src="{IMG}/{img}.jpg" alt="{title} — case study" style="object-position: {pos}" fetchpriority="high">
    </picture>
  </div>
  <div class="case-hero__panel">
    <span class="case-hero__eyebrow">Case study</span>
    <h1 class="case-hero__title">{title}</h1>
    <span class="case-hero__client">{client}</span>
    <p style="max-width:60ch;margin-top:0.75rem;font-family:var(--font-caps);letter-spacing:0.06em;text-transform:uppercase;opacity:0.9;">{tagline}</p>
  </div>
</section>'''

    def section(num, label, body_html, has_media=True, media_label="Photo / video placeholder"):
        media = f'<div class="case-section__media">{media_label}</div>' if has_media else ""
        return f'''<section class="case-section" data-reveal>
  <div class="case-section__label">{num}<span>{label}</span></div>
  <div class="case-section__body">{body_html}{media}</div>
</section>'''

    sections = (
        section("01", "Problem", f"<p>{problem}</p>")
        + section("02", "Analysis", f"<p>{analysis}</p>")
        + section("03", "Solution", f"<p>{solution}</p>")
        + section(
            "04", "Result",
            f"<p>{result}</p>"
            '<div class="case-metrics">'
            '<div class="case-metric"><strong>+ 00%</strong><span>Metric one</span></div>'
            '<div class="case-metric"><strong>+ 00%</strong><span>Metric two</span></div>'
            '<div class="case-metric"><strong>+ 00%</strong><span>Metric three</span></div>'
            '</div>',
            has_media=False,
        )
    )

    back = ('<section class="country-back" data-reveal>'
            '<a class="block__link" href="/what-we-did/">← All case studies</a>'
            '</section>')

    body = hero + sections + back
    return page_shell(
        f"{title}",
        f"Hello Media case study: {title} for {client}. {tagline}",
        body,
        og_image=f"{IMG}/{img}.jpg",
    )

def build_what_we_did_hub():
    header = page_header(
        "Chapter 04",
        "What we did",
        "Proof, not promises — Problem · Analysis · Solution · Result.",
        "what-we-did")
    if len(CASE_STUDIES) > 1:
        cards = []
        for slug, title, client, tagline, img, *_ in CASE_STUDIES:
            pos = focal(img)
            cards.append(f'''<a class="case-card" href="/what-we-did/{slug}/" data-reveal>
  <div class="case-card__media">
    <picture>
      <source srcset="{IMG}/{img}.webp" type="image/webp">
      <img src="{IMG}/{img}.jpg" alt="{title} — case study" style="object-position: {pos}" loading="lazy">
    </picture>
  </div>
  <div class="case-card__body">
    <span class="case-card__eyebrow">{client}</span>
    <h3 class="case-card__title">{title}</h3>
    <p class="case-card__sub">{tagline}</p>
  </div>
</a>''')
        body = header + '<section class="case-card-grid">' + "".join(cards) + "</section>"
    else:
        # Single placeholder — show the template link + the usual "coming soon" copy
        slug, title, client, tagline, img, *_ = CASE_STUDIES[0]
        pos = focal(img)
        placeholder = f'''<section class="case-card-grid">
  <a class="case-card" href="/what-we-did/{slug}/" data-reveal>
    <div class="case-card__media">
      <picture>
        <source srcset="{IMG}/{img}.webp" type="image/webp">
        <img src="{IMG}/{img}.jpg" alt="Template preview" style="object-position: {pos}" loading="lazy">
      </picture>
    </div>
    <div class="case-card__body">
      <span class="case-card__eyebrow">Template preview</span>
      <h3 class="case-card__title">{title}</h3>
      <p class="case-card__sub">{tagline}</p>
    </div>
  </a>
</section>'''
        body = header + placeholder + coming_soon(
            "Case studies launching soon",
            "Our first three real case studies are being written. Expect the full playbook: brief, craft, numbers, the good and the unexpected.")
    return page_shell("What we did", "Hello Media case studies — Problem, Analysis, Solution, Result.", body)


# ─── COUNTRY PAGES (/where-we-are/<country>/) ─────────
COUNTRIES = [
    ("uae",    "United Arab Emirates", "Headquarters", "Dubai Media City, Dubai, UAE",
     "contact-uae",
     "Real content — full address and team details will replace the placeholder once Management confirms."),
    ("uk",     "United Kingdom",       "Market Hub",   "Central London, UK",
     "contact-uk",
     "Indicative location pending Management sign-off."),
    ("usa",    "United States",        "Market Hub",   "Midtown Manhattan, New York, USA",
     "contact-usa",
     "Indicative location pending Management sign-off."),
    ("brazil", "Brazil",               "Market Hub",   "Avenida Paulista, São Paulo, Brazil",
     "contact-brazil",
     "Indicative location pending Management sign-off."),
    ("china",  "China",                "Market Hub",   "The Bund, Shanghai, China",
     "contact-china",
     "Indicative location pending Management sign-off."),
    ("egypt",  "Egypt",                "Market Hub",   "Smart Village, Cairo, Egypt",
     "contact-egypt",
     "Indicative location pending Management sign-off."),
]

def build_country_pages():
    out = {}
    for slug, country, tier, address, img, note in COUNTRIES:
        lead = f"{tier}. Part of the Hello Media global network."
        body = page_header("Where we are / " + country, country, lead, img)
        body += f'''<section class="country-facts" data-reveal>
  <div class="country-fact">
    <h3>Address</h3>
    <p>{address}</p>
    <small>Indicative location</small>
  </div>
  <div class="country-fact">
    <h3>Phone</h3>
    <p>+00 0 0000 0000</p>
    <small>Placeholder</small>
  </div>
  <div class="country-fact">
    <h3>Tier</h3>
    <p>{tier}</p>
    <small>{note}</small>
  </div>
</section>'''
        body += f'''<section class="country-back" data-reveal>
  <a class="block__link" href="/where-we-are/">← Back to the world map</a>
</section>'''
        out[slug] = page_shell(
            country,
            f"Hello Media {country} — {tier}. Indicative location; real address on sign-off.",
            body,
            og_image=f"{IMG}/{img}.jpg",
        )
    return out


# ─── MOTION PREVIEW (private QA page, not in nav) ─────
def build_motion_preview():
    header = page_header(
        "Internal / QA",
        "Motion preview",
        "Private preview of the motion language for sign-off. Not linked in the main nav.",
        "home")
    note = '<p class="motion-note">Hover the tiles to trigger hover-based motion. The intro overlay fires once per session — clear sessionStorage to replay. All animations respect prefers-reduced-motion.</p>'
    tiles = '''<section class="motion-grid" data-reveal>
  <div class="motion-tile">
    <h3>Pause</h3>
    <p>Hard stop easing on bars and reveals. Used for intro and scroll reveals.</p>
    <div class="motion-stage"><div class="motion-pause"></div></div>
  </div>
  <div class="motion-tile">
    <h3>Smile</h3>
    <p>Arc-up easing — used on image scale and block entries.</p>
    <div class="motion-stage"><div class="motion-smile"></div></div>
  </div>
  <div class="motion-tile">
    <h3>Wink</h3>
    <p>Quick twist — used on service-card pixel and nav underline.</p>
    <div class="motion-stage"><div class="motion-wink"></div></div>
  </div>
  <div class="motion-tile">
    <h3>Pixel</h3>
    <p>Blink — the brand punctuation mark.</p>
    <div class="motion-stage"><div class="motion-pixel"></div></div>
  </div>
  <div class="motion-tile">
    <h3>Reveal</h3>
    <p>Scroll-in reveal — fires once per element when it enters the viewport.</p>
    <div class="motion-stage"><div class="motion-reveal"></div></div>
  </div>
  <div class="motion-tile">
    <h3>Intro overlay</h3>
    <p>Logo assembly, once per session. <button id="replay-intro" style="color:var(--red);font-family:var(--font-caps);text-transform:uppercase;letter-spacing:0.2em;font-size:0.8rem;border-bottom:2px solid var(--red);padding-bottom:2px;">Replay →</button></p>
    <div class="motion-stage" id="intro-mini" style="background:var(--black);"></div>
  </div>
</section>'''
    script = '''<script>
(function () {
  var btn = document.getElementById("replay-intro");
  if (btn) {
    btn.addEventListener("click", function () {
      try { sessionStorage.removeItem("hm_intro_seen"); } catch (e) {}
      location.reload();
    });
  }
})();
</script>'''
    return page_shell(
        "Motion preview",
        "Hello Media — internal motion preview page.",
        header + note + tiles,
        extra_head='<meta name="robots" content="noindex, nofollow">',
        extra_scripts=script,
    )


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
    write("what-we-did/index.html", build_what_we_did_hub())

    for slug, html in build_who_subs().items():
        write(f"who-we-are/{slug}/index.html", html)
    for slug, html in build_service_subs().items():
        write(f"what-we-do/{slug}/index.html", html)

    # Case studies
    for case in CASE_STUDIES:
        slug = case[0]
        write(f"what-we-did/{slug}/index.html", build_case_study(*case))

    # Country pages under /where-we-are/
    for slug, html in build_country_pages().items():
        write(f"where-we-are/{slug}/index.html", html)

    # Site map gets custom content; other stubs use generic template
    for slug, html in build_stubs().items():
        if slug == "site-map":
            continue
        write(f"{slug}/index.html", html)
    write("site-map/index.html", build_site_map())

    # Private QA page — not linked in primary nav
    write("motion-preview/index.html", build_motion_preview())

    # Sitemap — auto-generated so routes stay in sync with the build.
    write("sitemap.xml", build_sitemap())

    print("\nDone.")


# ─── Sitemap ──────────────────────────────────────────
def build_sitemap(base="https://hellomedia.site"):
    # Canonical placeholder domain — swap when Management confirms.
    today = time.strftime("%Y-%m-%d")
    routes = ["/"]
    routes += ["/who-we-are/", "/what-we-do/", "/whom-we-love/",
               "/what-we-did/", "/where-we-are/",
               "/when-we-are-needed/", "/media-center/", "/awards/",
               "/csr-community/", "/csr-environment/",
               "/small-jobs/", "/suggestions/", "/faq/", "/site-map/",
               "/privacy/", "/terms/", "/cookies/", "/copyright/"]
    routes += [f"/who-we-are/{s}/" for s, *_ in WHO_SUBS]
    routes += [f"/what-we-do/{s}/" for s, *_ in SERVICES]
    routes += [f"/what-we-did/{c[0]}/" for c in CASE_STUDIES]
    routes += [f"/where-we-are/{c[0]}/" for c in COUNTRIES]
    # motion-preview is intentionally excluded (private QA page)
    urls = "".join(
        f"<url><loc>{base}{r}</loc><lastmod>{today}</lastmod></url>" for r in routes
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f'{urls}'
        '</urlset>\n'
    )

if __name__ == "__main__":
    main()
