# CLAUDE.md

**Last Updated:** 2026-04-29 UTC

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## What This Is

A single-file static site for a fish room downsizing sale — fish, amphibians, plants, and equipment. No build step, no framework, no dependencies. The entire site is one self-contained HTML file (`index.html`) with inline CSS and JS.

**Live URL:** <https://wowthisiseasytoremember-stack.github.io/fish/>

The site is deployed via GitHub Pages directly from the `main` branch root. There is no build step and no server-side rendering.

---

## File Structure

| File / Folder | Purpose |
| :--- | :--- |
| `index.html` | The site. Everything lives here — CSS, JS, and all content. (Renamed from `fish-room-sale.html` for GitHub Pages.) |
| `fish-room-content-brief.txt` | Source of truth for species inventory, quantities, care notes, and pricing policy. Update here first; HTML reflects it. |
| `Tank Inventory.md` | Physical tank layout and current contents. Cross-check species availability against this. |
| `tank_tasks/` | ~123 per-tank Markdown task files. Reference only — not rendered on the site. |
| `scripts/` | Python utility scripts for HTML generation, enrichment, minification, and sanitization. Not part of the site — run manually when needed. |
| `listings/` | Platform-specific Reddit post drafts (r/aquaswap, r/plantswap, r/hardwareswap, etc.) |
| `queue/drafts/` | Active posting drafts. `READY-TO-POST.md` lists what's ready to go. |
| `PHOTO_CATALOG.md` | Catalog of ~90 photos in local `Photos-3-001/` folder (not committed). Maps photos to subreddits and posting order. |
| `sales-listings.md` | Consolidated human-readable inventory with pricing and care notes. |
| `HANDOFF.md` | Session-to-session context for ongoing work. Update at end of every session. |
| `CHANGELOG.md` | Append-only record of all significant changes. Update when committing meaningful work. |
| `.github/workflows/markdown-lint.yml` | CI: runs `markdownlint-cli2` on all `*.md` files on push/PR to `main`. |
| `.markdownlint.json` | Markdownlint rule config (MD013 line-length disabled). |
| `.autoresearch/config.yaml` | Config for autoresearch agent (time budget, scope). Not site-related. |

---

## Branches

- `main` — stable, deployed to GitHub Pages. All content changes land here.
- Feature branches follow the pattern `claude/<description>-<id>` and are merged via PR.

---

## HTML Architecture

`index.html` (3,246 lines) is structured top-to-bottom as:

1. **CSS custom properties** — color palette and font stack
   - Category colors: `--color-fish` (#00b4d8), `--color-herp` (#f4a261), `--color-invert` (#b07aff), `--color-plant` (#2dc653), `--color-fungi` (#e07cff)
   - Status colors: `--color-empty` (#3a3f4a), `--color-storage` (#2a2e38)
   - Fonts: Cormorant Garamond (headings), DM Sans (body), JetBrains Mono (accents) — loaded from Google Fonts
2. **Animated canvas background** — `#bg-canvas` fixed full-screen canvas with particle/bubble animation. Keep it lightweight.
3. **Hero section** — title, subtitle, last-updated timestamp. Update the timestamp when publishing content changes.
4. **Stats bar** — animated counters for years, species count, etc.
5. **Racks/tank overview section** — physical room layout
6. **Species search** — `#species-search` input filters across all compendium panels in real time
7. **Media panels** — side-by-side photo carousel (`#main-carousel`) and video player (`#video-main`), each with an expand-to-modal button. Photos load from Google Drive thumbnail URLs. Videos are Google Drive embeds.
8. **Media modal** — `#media-modal` full-screen overlay; DOM nodes are moved in/out (not cloned) to preserve carousel/video state.
9. **Compendium** — tabbed species browser with animated slide transitions between panels:
   - Rail nav (`.rail-item`) for Fish / Herps / Inverts / Plants
   - Four panels: `#fish-list`, `#herp-list`, `#invert-list`, `#plant-list`
   - `switchCategory()` handles directional CSS transitions (`translateX`)
10. **Equipment section** — hardcoded HTML cards grouped by type (tanks, filtration, lighting, hardscape)
11. **Footer** — three-column grid: contact form, Abigail Breslin memorial, freelance pitch

**No data layer.** All species content is hardcoded HTML. To add or update an animal, edit its card in `index.html` and keep `fish-room-content-brief.txt` in sync.

---

## Photo / Video Assets

Photos and videos are **not committed to git** — they live locally at `/Users/justin/Downloads/Photos-3-001/` and are served via Google Drive share links. The site uses:

```text
https://drive.google.com/thumbnail?id=<FILE_ID>&sz=w1000   ← static images
https://drive.google.com/file/d/<FILE_ID>/preview           ← video embeds
```

`PHOTO_CATALOG.md` maps each filename to its Google Drive ID and target subreddit. Update it when new photos are added.

---

## Python Scripts (`scripts/`)

These are standalone utilities — none are called by the site or CI:

| Script | What it does |
| :--- | :--- |
| `generate_html.py` | Generates species card HTML from a JSON data file |
| `enrich_html.py` | Enriches HTML cards with data from `task_data.json` |
| `inject_verified_data.py` | Injects verified scientific names / care data into HTML |
| `sanitize_sale_site.py` | Strips internal location strings and prevents content bleed |
| `update_html.py` | General HTML patching utility |
| `consolidate_json.py` | Merges multiple task JSON files into one |
| `clean_enrichment.py` | Removes stale enrichment artifacts |
| `minify_css.py` / `minify_js.py` | CSS/JS minification helpers |
| `xray_report.py` | Generates a diagnostic report of site content |
| `generate_listings.py` (root) | Scrapes `tank_tasks/*.md` for inventory entries and pricing to build `sales-listings.md` |

---

## CI

GitHub Actions runs on every push/PR to `main`:

```text
.github/workflows/markdown-lint.yml
```

Uses `markdownlint-cli2-action@v16`. All `*.md` files must pass. Rules are in `.markdownlint.json` (MD013 disabled). Fix lint errors before pushing — the `tank_tasks/` directory is included.

---

## Content Source of Truth

`fish-room-content-brief.txt` is the canonical species list and pricing policy. Before editing card content in `index.html`, check this file. If the brief and the HTML disagree, the brief is correct.

- Quantities marked "TBD" → display as "Inquire" in HTML. Never invent a number.
- Local pickup preferred (LA/Orange County). Shipping is last resort.
- No location info displayed publicly on the site.
- Native herps (Taricha, CA tree frogs): always include chytrid fungus release warning.

---

## Previewing Changes

Open `index.html` directly in a browser — no server needed.

```bash
open index.html          # macOS — opens in default browser
```

---

## Testing Changes

Always verify after edits:

1. Category rail (Fish, Herps, Inverts, Plants) — click all four, confirm animated slide transitions work
2. Species search — type a term, confirm cards filter correctly across active panel
3. Photo carousel — prev/next and dots, auto-advance, expand modal
4. Video carousel — prev/next, caption text, counter
5. Equipment section — scrolls and renders
6. Mobile layout — resize or DevTools; media panels stack single-column, footer cards stack vertically
7. Canvas background animation still runs
8. No console errors

---

## Common Edits

**Update a species quantity:** Edit the card in `index.html` (find by species name) AND update `fish-room-content-brief.txt`.

**Add a photo to the carousel:** Add a `{id: '<DRIVE_FILE_ID>', alt: '...'}` entry to the `photos` array near line 3011 in `index.html`. Photos load via the Google Drive thumbnail URL pattern.

**Update the hero timestamp:** Change the `<p class="hero-timestamp">` value in the hero section (~line 1349).

**Add a Reddit post draft:** Create a new `.md` file in `listings/` or `queue/drafts/`. Update `queue/drafts/READY-TO-POST.md` with posting order. Run markdownlint locally before committing.
