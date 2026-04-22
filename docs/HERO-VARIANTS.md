# Hero variants — for Chaadi sign-off

Two hero treatments are live on `index.html`. Switch between them via the `?hero=` query parameter. Neither deletes the other; only the query string changes which one renders.

## A — Default (current)

URL: `https://hellomedia.site/` (no query param)

- Image fills the visible area **below** the fixed dark nav bar (nav height ≈ 76 px desktop / 64 px mobile).
- Nav has an opaque black background + subtle bottom border, so it reads as a separate frame.
- Text panel bottom-left, red eyebrow ("Hello, Stop, Smile"), white display title, caps subline.
- This is the treatment shipped in session 1–3 and reviewed internally.

**Screenshot description** — if rendered at 1440×900:
- Top 76 px: black nav (logo + links).
- Below nav: hero image filling the viewport to just above the fold. Dark gradient overlay at the bottom 45% to keep the text legible.
- Panel sits at bottom-left, ~520 px wide, with the red "Hello, Stop, Smile" eyebrow above the "Welcome to our home" title.
- "Scroll" marker at bottom-right.

## B — Edge-to-edge (Chaadi's request)

URL: `https://hellomedia.site/?hero=edge`

- Image fills the **entire viewport** (100 svh). Nav overlays the image instead of sitting above it.
- Nav background drops to transparent; no bottom border. The top of the hero has a stronger darkening gradient so the nav links stay legible.
- Text panel and scroll marker are unchanged — same position and type.
- Visually there is no white/black "frame" around the image; it reads as a single full-bleed picture with nav floating over it.

**Screenshot description** — if rendered at 1440×900:
- Full 900-px tall image from top of viewport.
- Nav links are visible at top, readable thanks to a top-edge black-to-transparent gradient on the image overlay.
- Everything else in the panel matches variant A.

## Implementation notes

- The variant toggle is done in `js/main.js` very early — it reads `?hero=edge` from `location.search` and adds `body.hero-edge`. CSS in `css/style.css` (search for `body.hero-edge`) flips the nav background, strips the top padding on `main`, and extends `.hero__media` to full viewport height.
- If we ship variant B as the default, the JS toggle becomes a no-op and the CSS block can move to the default rule. Both are a one-line change.
- Fallback behaviour: if the URL has the param but JS is disabled, the default hero renders. That is acceptable for review purposes — Chaadi can still screenshot the default.

## How to preview locally

```bash
python3 scripts/build_pages.py       # rebuild
python3 -m http.server 8000          # serve
```

Open:
- `http://localhost:8000/`  → variant A (default)
- `http://localhost:8000/?hero=edge` → variant B

## Headless screenshots

`wkhtmltoimage` / Puppeteer are not installed in this environment. Ship the variants to Vercel preview (blocked today by Deploy Protection — see tracker) and screenshot from a browser, or install one of the above on a workstation and run:

```bash
wkhtmltoimage --width 1440 http://localhost:8000/           hero-variant-a.png
wkhtmltoimage --width 1440 http://localhost:8000/?hero=edge hero-variant-b.png
```
