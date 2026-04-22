# Prompt for the next Claude Code session

_Copy-paste the block below at the start of a fresh Claude Code session in this repo._

---

You are picking up work on the Hello Media agency website (v2 build). The repo is `abhileenss/hello-media-website`, working branch is `main`. Before making changes, read these three files in order:

1. `docs/CONVERSATION-NOTES.md` — project context, decisions locked in, who's responsible for what
2. `docs/PARTNER-BRIEF.md` — status summary
3. `docs/TRACKER.csv` — 124 tasks with owners and priorities

## Current state (as of this commit)
- 43 pages generated from `scripts/build_pages.py`
- Brand CSS in `css/style.css`, site JS in `js/main.js` + `js/map.js`
- 49 hero images optimised at `assets/images/hero/`
- Deployed at https://hello-media-website.vercel.app (behind Deploy Protection — you can't reach it)
- Local preview: `python3 -m http.server 8000` from repo root, then open `http://localhost:8000/`
- Rebuild after edits: `python3 scripts/build_pages.py`
- Every CSS/JS reference is cache-busted with `?v=<timestamp>` auto-stamped at build

## Do these in this order
_(All unblocked by partner input — pure engineering/design work.)_

### 1. Edge-to-edge hero variant for Chaadi sign-off
Chaadi asked for a screenshot test showing the hero with image "from edge to edge — no white rounded frame". Build this as an **A/B variant** — keep current hero as-is, add a second version on `index.html` controlled by `?hero=edge` query param. Document both in `docs/HERO-VARIANTS.md` with screenshots (use `wkhtmltoimage` or similar if available, otherwise describe clearly). Don't delete the current hero.

### 2. Slogan readability fix on hero
Chaadi flagged that the red slogan ("HELLO, STOP, SMILE") doesn't look clear vs the rest of the text — size/contrast is off. Bump the eyebrow size on mobile and tighten the letter-spacing; consider adding a subtle text-shadow for contrast over busy images. Test visually at phone + tablet widths.

### 3. Add social-media-icons placeholder in footer
Handles aren't final but the scaffolding should be ready. Add a row of icons (SVG inline, no external fonts) linking to `#` for now, above the `.footer__bottom`. Platforms in Chaadi's requested order: FB, Instagram, Snapchat, X, TikTok, YouTube, Pinterest, Flickr, LinkedIn. Keep icons 20–22 px, hover to red, accessible names via `aria-label`.

### 4. Cookie statement link in footer + "you agree" clause
Chaadi confirmed: **no cookie popup**. Just a footer link to `/cookies/` (already exists as a stub) and a sentence inside `/terms/` saying "by using this site you agree to these terms and have no claim etc." Update the terms stub copy accordingly.

### 5. Case study page template
Chaadi locked the structure: **Problem · Analysis · Solution · Result** with photos/videos. Build a reusable case-study template at `/what-we-did/<slug>/` that takes this shape. For now, seed one placeholder at `/what-we-did/sample/` so the layout is reviewable. Update the `/what-we-did/` hub to list case studies as cards once there's more than one.

### 6. Sitemap.xml + robots.txt
Use placeholder canonical `https://hellomedia.site/` (Chaadi's proposed domain — can swap when Management confirms). `robots.txt` allows all, references sitemap.

### 7. manifest.webmanifest + PNG icon fallbacks
Generate PNG icons at 180×180, 192×192, 512×512 from `favicon.svg` (use Pillow). Add `<link rel="apple-touch-icon" ...>` and `<link rel="manifest" ...>` to page shell.

### 8. Country page scaffolding
Chaadi said UAE gets real content, others mock first. Build 6 country pages: `/where-we-are/uae/`, `/where-we-are/uk/`, `/where-we-are/usa/`, `/where-we-are/brazil/`, `/where-we-are/china/`, `/where-we-are/egypt/`. Each: hero image from the optimised set (`contact-<country>.jpg`), mock address (label clearly as "Indicative location"), placeholder phone, link back to the world map. Link each from the map pin's tooltip as "Visit →" once hovered.

### 9. Motion language audit
Chaadi said "I did not see any motions." Verify: (a) intro overlay fires on first visit (sessionStorage-gated), (b) service-card pixel-wink on hover is visible, (c) scroll-reveal runs on desktop. Add a `/motion-preview/` page — private link, not in nav — that showcases all motion primitives side-by-side so Chaadi can review them explicitly. Note: `prefers-reduced-motion` kills all animations; check Chaadi isn't stuck with that OS setting.

### 10. Image focal-point metadata
For every hero image, compute a sensible `object-position` value (currently all `center`) and store them in a Python dict in `scripts/build_pages.py` so the generator emits `style="object-position: X Y"` per image. Default to `center` if not specified. This lets Graphics override focal points without touching CSS.

## Rules

- **Never** push straight to `main` without running the local crawl first: `python3 -m http.server 8765 &`, then any crawl script you copy into `/tmp/`. Verify 0 broken links.
- **Commit messages**: first line ≤ 72 chars, imperative mood. Body explains the "why." No markdown in messages.
- **Do not** add or change content that needs partner approval — logos, fonts, legal copy, real addresses, client names, case study content. Only scaffold structure.
- **Do not** break the current homepage or any of the 43 pages. Use query params, branches, or new routes for A/B tests.
- Cache-bust is automatic — don't hand-version.
- Responsive breakpoints already defined: `400 / 600 / 860 px`. Stay inside them.

## When you're done
Update `docs/TRACKER.csv` — change Status to "Done" on every task you shipped, fill the **Result** column with a one-line summary + commit SHA. Update `docs/CONVERSATION-NOTES.md` with a dated entry under "Session log" summarising what changed. Commit, push to `main`, tell the user which items are ready for partner review.

---

_End of prompt._
