# Hello Media — Website v2 Status & Partner Brief

_Last updated: 2026-04-22 · Branch: `main` · Commit: `4c9fbe1`_
_Preview: https://hello-media-website.vercel.app/ (currently behind Vercel Deploy Protection)_

---

## TL;DR

v2 is built: 43 pages, 49 optimised images (852 MB → 24.5 MB), brand CSS with proper motion language, animated logo intro, image-dominant hero (fixes the "half-image" feedback), interactive world map with hub tooltips, branded 404, security headers, SEO meta, accessibility basics.

What's blocking a public launch is **content from the group** (case studies, client logos, real addresses, legal text) and one Vercel setting (Deploy Protection). None of it is design or engineering — it's inputs.

---

## ✅ What's done

### Design & brand
- Black / white / `#E6062F` throughout — correct brand colours
- **Closest-free fonts** used as stand-ins: Archivo Black (display), Barlow Condensed (caps/eyebrow), Inter (body) — swap in licensed Geometr415 Blk + EngraversGothic BT when available
- Animated logo SVG with five moving parts (pause, H-left, H-right, smile, pixel) — intro assembly on first visit, then parked in nav
- Motion language: Pause / Smile / Wink custom easings applied consistently across hover, reveal, and tooltip transitions
- Hero rebuilt image-dominant per Chaadi's feedback (full-bleed image, text panel bottom-left)

### Structure
- **43 pages** total:
  - Home
  - 5 main hubs: Who we are, What we do, Whom we love, What we did, Where we are
  - 8 Who-we-are subpages (vision, mission, values, team, careers, diversity, grow-with-us, get-involved)
  - 16 service pages (e-marketing, web, mobile, AI, SEO, web-app, domain/hosting, branding, creative/printing, video, audio, copywriting, PR, photography/media-buy, packaging, crisis)
  - 13 support/legal stubs (each with its own wording so the footer doesn't look copy-pasted)
- Interactive world map on `/where-we-are/`: 6 red market-hub pins pulsing (UAE, UK, USA, Brazil, China, Egypt), 2 grey studio pins (India, Pakistan), hover tooltip

### Technical
- Images: WebP + JPG fallback via `<picture>`, `fetchpriority="high"` above the fold, lazy-load below
- Accessibility: real alt text, skip-to-content link, keyboard focus styles, `prefers-reduced-motion` respected
- SEO: proper `<title>` with positioning, OpenGraph + Twitter meta, theme-color, favicon
- Security headers via `vercel.json`: CSP, X-Frame-Options DENY, HSTS preload, Referrer-Policy, Permissions-Policy
- Caching: immutable for `/assets/`, 1 h for CSS/JS
- Branded 404 page
- Mobile nav, scroll reveals (with no-JS fallback so content is never invisible)

### Tooling
- `scripts/build_pages.py` — single Python generator emits all pages; nav/footer/logo shared via one template
- Local crawl script verifies 131 refs across 43 pages; zero broken links/assets/orphans

---

## 🔨 What's left to build (engineering-side, blocked only by decisions or content)

| # | Task | Blocker |
|---|---|---|
| 1 | Contact form on `/where-we-are/` | Need email destination + form backend choice (Formspree / Resend / Vercel Forms / SMTP) |
| 2 | `sitemap.xml` + `robots.txt` | Need final domain |
| 3 | Analytics snippet | Need provider choice (GA4 / Plausible / Vercel Analytics) |
| 4 | Swap in licensed brand fonts | Need font files from Chaadi |
| 5 | Replace stand-in logo SVG with pixel-perfect vector | Need clean SVG export from `Logo.ai` |
| 6 | Populate client logos on Whom we love | Need logo files |
| 7 | Build out case study template + 3–5 stories | Need case study content |
| 8 | Real map pin addresses | Need per-country office addresses |
| 9 | Legal copy on privacy / terms / cookies / copyright | Need legal-reviewed text |
| 10 | FAQ content | Need Q&A list |
| 11 | Team page with photos + bios | Need photos + bios |
| 12 | Awards page content | Need verified awards list |
| 13 | Social media icons in footer | Need active handles |
| 14 | Arabic version / hreflang (optional) | Need go/no-go from client |
| 15 | Cookie consent banner (if GDPR/PDPL requires) | Need legal confirmation |

---

## 🤝 What we need from the group

One combined list — send to whoever owns each item.

### Brand & design
- [ ] **Clean SVG** of the logomark (just the H+smile+pixel) and the wordmark ("HELLO MEDIA"), as separate files
- [ ] **Font licence decision**: ship Geometr415 Blk + EngraversGothic BT (provide files) OR approve current Archivo Black + Barlow Condensed substitutes
- [ ] **Brand red confirmation**: I'm using `#E6062F` — confirm exact hex / Pantone
- [ ] **Sign-off** on homepage hero layout, intro overlay animation, motion language (Pause / Smile / Wink easings)
- [ ] **Image crop guidance** for any source photo that doesn't work at 16:8 — flag focal points

### Client content (Hello Media)
- [ ] **Final domain** (is it `hellomedia.ae`?)
- [ ] **Contact email** — destination for form + footer
- [ ] **Phone numbers** per country for the footer and Where-we-are
- [ ] **Real office addresses** for each pin: UAE (HQ), UK, USA, Brazil, China, Egypt, India studio, Pakistan studio
- [ ] **Client logos** for Whom we love (currently 18 placeholder cells)
- [ ] **Case studies** — at least 3–5 to launch: title, hero image, copy, outcomes/numbers
- [ ] **Team**: photo + name + title + short bio for each person you want featured
- [ ] **Awards list**: title, year, category, optional badge image
- [ ] **FAQ content**: 8–12 Q&A pairs
- [ ] **Small-jobs offering**: what's included, pricing bands, turnaround
- [ ] **Social handles** — LinkedIn, Instagram, X, YouTube, etc.
- [ ] **Hero subline sign-off**: current is "Marketing: shockingly complex! Let the experts handle the volts." Feedback said this frames marketing as the problem. Three alternatives proposed — pick one or write your own:
  - A. _"Marketing that makes your brand work as hard as you do."_
  - B. _"We turn attention into growth — from Dubai to everywhere."_
  - C. _"Strategy, craft, and just enough mischief to get noticed."_
- [ ] **Nav decision**: "Whom we love" and "What we did" are currently in the primary nav but link to coming-soon stubs. Option to hide them from nav until content ships — confirm
- [ ] **Optional**: brand intro video for hero

### Legal
- [ ] Privacy policy text
- [ ] Terms & conditions text
- [ ] Cookie statement text
- [ ] Copyright statement
- [ ] Cookie consent banner requirement (GDPR / UAE PDPL)?

### Ops / IT
- [ ] **Disable Vercel Deploy Protection** on the project (Settings → Deployment Protection → Disabled) OR add public access so the live build can be reviewed end-to-end
- [ ] **Analytics choice**: GA4, Plausible, or Vercel Analytics?
- [ ] **Form backend choice**: Formspree, Resend, Vercel Forms, or custom SMTP?
- [ ] **DNS**: once domain is confirmed, pointing to Vercel
- [ ] Confirm PR workflow going forward: feature branch → PR → review → merge to `main`

---

## 📅 Suggested sequencing

1. **Now** — group ships inputs above, Vercel Deploy Protection flipped off
2. **This week** — live inputs wired in (logos, real addresses, contact form, analytics, sitemap)
3. **Next week** — first 3 case studies, team page, FAQ
4. **Before public launch** — legal sign-off, font licence, final domain, client logos on Whom we love
