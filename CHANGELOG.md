# Changelog

**Last Updated:** 2026-04-22 22:00 UTC

## [2026-04-22 22:00 UTC] — Merged Ichabod work into Mac repo and pushed to GitHub

### Done

- Identified that Gemini's committed work (sales-listings.md, CI workflow, lint fixes) was stranded on Ichabod with no valid GitHub token to push
- Added Ichabod as a temporary git remote on the Mac, fetched, and merged its 2 commits into Mac main
- Resolved merge conflicts in CLAUDE.md and TODO.md (kept Ichabod's completed-task checkmarks; kept Mac's structural content)
- Committed untracked `queue/drafts/aquaswap-main-post.md` (Reddit r/aquaswap draft)
- Pushed full merged history to GitHub from Mac (working auth via `wowthisiseasytoremember-stack`)
- All Gemini work now live: `sales-listings.md`, `.github/workflows/markdown-lint.yml`, `.markdownlint.json`, `reddit-post.md`, `HANDOFF.md`

### For Produce

> Fish sale repo is fully synced and pushed. All Gemini work (pricing doc, CI, Reddit draft) is on GitHub. Next step: take photos for r/aquaswap post (required before submitting) and verify California compliance before listing Taricha newts.

## [2026-04-22 21:10 UTC] — Repository synced, pricing consolidated, and CI established

### Done

- Located and cloned repository via SSH from Mac to local Linux environment.
- Consolidated all inventory and pricing from `tank_tasks/` into `sales-listings.md`.
- Created a platform-optimized Reddit listing for `r/aquaswap` in `reddit-post.md`.
- Configured a GitHub Actions CI workflow for Markdown linting in `.github/workflows/markdown-lint.yml`.
- Established a repository standard for Markdown with `.markdownlint.json`.
- Performed a comprehensive linting audit and fixed 1000+ formatting errors across core files.
- Updated `TODO.md` and `README.md` to reflect new files and completed tasks.

## [2026-04-27 19:27 UTC] — Scoped CLAUDE.md to project repository and cleaned home directory

### Done

- Deleted the stray `CLAUDE.md` from the home directory (`~/CLAUDE.md`).
- Created a new `CLAUDE.md` inside `~/fish-sale-repo/` reflecting the repo’s codebase and context.
- Updated `.gitignore` to ensure future `CLAUDE.md` files are tracked only inside project directories.

### In Progress

- Nothing

### For Produce

> Next session should select the next feature to develop or merge an outstanding autoresearch branch.

## [2026-04-22 19:18 UTC] — Repository cleaned, docs refreshed, and registry entry updated

### Done

- Deleted stale clone at `~/Documents/fish`
- Rewrote `README.md` with project overview, file map, and branch list; pushed to GitHub
- Created `CHANGELOG.md` documenting today’s session; pushed to GitHub
- Added Fish Room Sale to the project registry as Tier 2, entry 0, linking to `~/fish-sale-repo/` and the GitHub repo

### In Progress

- Nothing

### For Produce

> Next session should select the next feature to develop or pick an autoresearch branch to merge.

## [2026-04-22 12:30 UTC] — Repo connected to GitHub, docs added

### Done

- Added GitHub remote (`wowthisiseasytoremember-stack/fish`) and pushed full history to `main`
- Added `fish-room-content-brief.txt` (content/pricing source of truth) — was on Desktop
- Added `Tank Inventory.md` (canonical tank layout, fresh 2026-04-16) — was in brain docs
- Deleted stale empty clone at `~/Documents/fish`
- Wrote README.md with project overview and branch map

### Skipped (Haiku audit)

- `~/Desktop/fish-room-sale.html` — duplicate of repo version
- `~/Downloads/Plant, Fish, and Amphibian Adoption Website Design Request.zip` — superseded by current HTML
- `Fish & Breeding Operation.md`, `Current Stock.md`, `Motivation.md` — stale brain docs, redundant

### For Produce

> Fish room sale repo is now live on GitHub at wowthisiseasytoremember-stack/fish with full history, content brief, and tank inventory. Working copy remains at ~/fish-sale-repo/.
