# CLAUDE.md

**Last Updated:** 2026-04-22 12:40 UTC

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## What This Is

A single-file static site for a fish room downsizing sale — fish, amphibians, plants, and equipment. No build step, no framework, no dependencies. The entire site is one self-contained HTML file with inline CSS and JS.

The site is deployed as a static file. There is no server-side rendering.

---

## File Structure

| File | Purpose |
| :--- | :--- |
| `fish-room-sale.html` | The site. Everything is here — CSS, JS, and all content. |
| `fish-room-content-brief.txt` | Source of truth for species inventory, quantities, care notes, and pricing policy. Update here first; HTML reflects it. |
| `Tank Inventory.md` | Physical tank layout and current contents. Used to cross-check species availability. |
| `tank_tasks/` | Per-tank task files, one per physical tank or area. ~123 files. Reference only — not rendered on the site. |

---

## Branches

Single branch: `main`. All work goes here. Feature branches are created for larger experiments and merged back when done.

---

## HTML Architecture

The single file (`fish-room-sale.html`) is structured as:

1. **CSS custom properties** — color palette (`--color-fish`, `--color-herp`, `--color-invert`, `--color-plant`) and font stack (Cormorant Garamond headings, DM Sans body, JetBrains Mono accents)
2. **Animated canvas background** — `#bg-canvas` is a fixed full-screen canvas with a particle/bubble animation driven by vanilla JS. Keep it visually lightweight.
3. **Species cards** — each animal/plant has a card with category color-coding. Cards are generated from inline HTML, not from a JS data structure.
4. **Filter/nav system** — JS-driven category filter (Fish, Herps, Inverts, Plants, Equipment). No external library.
5. **Contact section** — Reddit username + email + contact form. No location info is displayed.

There is no data layer. All content is hardcoded HTML. To add or update an animal, edit the card directly in the HTML and keep `fish-room-content-brief.txt` in sync.

---

## Previewing Changes

Open `fish-room-sale.html` directly in a browser — no server needed. For a worktree, open the `index.html` in that worktree folder.

To do a quick sanity check in the terminal:

```bash
open fish-room-sale.html          # macOS — opens in default browser
open worktrees/<branch>/index.html
```

---

## Content Source of Truth

`fish-room-content-brief.txt` is the canonical species list. Before editing card content in HTML, check this file. If the brief and the HTML disagree, the brief is correct.

Quantities marked "TBD" in the brief should stay as "Inquire" or similar in the HTML — never invent a number.

---

## Testing Changes

Open `fish-room-sale.html` directly in a browser — no server needed. Always verify:

1. Filter buttons work across all categories (Fish, Herps, Inverts, Plants, Equipment)
2. Mobile layout holds up (resize browser or DevTools)
3. Canvas background animation still runs
