**Last Updated:** 2026-04-23 03:01 UTC

# Changelog

## [2026-04-23 03:01 UTC] — advised manual cleanup of Xcode DerivedData and session env size check

### Done
- Communicated safe removal of `~/Library/Developer/Xcode/DerivedData/*` to free 1.4 GB
- Provided commands to verify `~/.claude/session-env` and `~/.claude/projects` sizes

### In Progress
- Nothing (awaiting user to execute cleanup commands)

### For Produce
> Verify that disk space has been reclaimed and resume planning polish for the fish-sale site.

## [2026-04-23 02:28 UTC] — Published final drafts and documentation to GitHub

### Done
- Added `queue/drafts/aquaswap-main-post.md` with incorporated feedback
- Added `PHOTO_CATALOG.md` detailing photo source, order, and gaps
- Added `HANDOFF.md` outlining current state, blockers, and next‑session checklist
- Pushed all three files to the remote repository

### In Progress
- Photo upload to Google Drive (user must drag `Photos-3-001` folder into Drive)

### For Produce
> Next session: complete the Drive folder upload and obtain a Dragon Puffer photo for the headline.

## [2026-04-23 02:19 UTC] — Added guidance to extend ADC scopes for Claude Drive upload

### Done
- Provided command to add Drive scope to Application Default Credentials for bulk photo upload

### In Progress
- Claude Drive authentication and photo upload (awaiting user to execute the suggested `gcloud auth application-default login` command)

### For Produce
> Next session: run the ADC scope command, re‑authenticate Claude Drive, and execute the upload script to transfer the 87 photos.

## [2026-04-23 00:00 UTC] — No code changes; pending authentication for photo upload

### Done
- None (no files created or modified)

### In Progress
- Authentication flow for Claude Drive access to upload the photo folder (awaiting user action)

### For Produce
> Next session: complete Claude Drive authentication and upload the product photos to the repository.

## [2026-04-22 23:30 UTC] — Reddit MCP wired up, draft reviewed, ready to post pending photos

### Done

- Ported the Gemini CLI reddit-regional-swap-specialist skill from ichabod (`~/.gemini/skills/`) to Claude Code format at `~/.claude/skills/reddit-swap-specialist/` with 5 reference files (aquaswap-rules, ca-compliance, reddit-culture, interest-hubs, local-socal-map)
- Stored Reddit credentials (u/wowthisiseasy) in GCP Secret Manager (`pwa-id-app` project) — no plaintext anywhere
- Created `~/.claude/scripts/reddit-mcp-wrapper.sh` — pulls credentials from Secret Manager at runtime and launches the MCP server
- Installed `jordanburke/reddit-mcp-server` v1.4.5 via npx — works without a Reddit API app registration
- Added reddit-mcp to Claude Code global MCP config (`~/.claude.json`) so it loads in any session from any directory
- Confirmed authentication: MCP connects as u/wowthisiseasy with write operations enabled
- Account check: 12-year-old account, 1,437 karma, prior r/AquaSwap history — 90/10 rule satisfied
- Reviewed `queue/drafts/aquaswap-main-post.md` — copy and pricing pending owner approval before post
- Added `queue/drafts/herpbst-post.md` and `queue/drafts/plantswap-post.md` as unposted drafts for other platforms

### Blocked

- Post not submitted yet — waiting on owner pricing/copy approval and photos (r/aquaswap requires actual item photos)

### For Produce

> Reddit MCP is live and authenticated. r/aquaswap draft is written and in queue/drafts/. Blocked on photo attachment and owner copy approval before submitting. Next session: get photos, owner approves pricing, post goes live.

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
