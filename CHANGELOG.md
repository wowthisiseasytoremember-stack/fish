**Last Updated:** 2026-04-24 23:39 UTC

# Changelog

## [2026-04-24 23:39 UTC] — Updated carousel dimensions to 640×480 px (4:3) for better portrait handling

### Done
- Modified `src/components/Carousel.jsx` to use a centered 640×480 px container.
- Adjusted CSS in `styles/carousel.css` for new aspect ratio and centering.
- Updated responsive breakpoints to accommodate the new size.

### In Progress
- Nothing

### For Produce
> Verify carousel appearance on mobile devices and merge the changes to `main`.

## [2026-04-24 23:38 UTC] — Fixed photo display in carousel to fully contain images with letterboxing

### Done
- Updated carousel CSS/HTML to use `contain` mode, ensuring full photo visibility with black side bars when aspect ratios differ.
- Refreshed page behavior so images now fit entirely inside the carousel frame.

### In Progress
- Nothing

### For Produce
> Verify carousel responsiveness on mobile devices and adjust breakpoints if needed.

## [2026-04-24 23:35 UTC] — Integrated 25 new photos into the carousel and prepared commit

### Done
- Added 25 real photos (room overviews, fish, herps, inverts, plants, aroids, equipment) to `fish-room-sale.html` carousel, excluding DONOTPOST files, blurry newt shot, and duplicate files.

### In Progress
- Nothing

### For Produce
> Verify carousel loads all new images on production and push the commit.

## [2026-04-24 23:30 UTC] — Enabled public access to carousel image folder

### Done
- Changed Google Drive folder sharing to “Anyone with the link – Viewer” so all 13 carousel photos load correctly on the site.

### In Progress
- Nothing

### For Produce
> Verify that the carousel displays all images correctly on the live site and resolve any loading issues.

## [2026-04-24 23:26 UTC] — Added carousel UI and removed stock thumbnails

### Done
- Removed 31 `<img class="species-thumb">` tags and their CSS from `fish-room-sale.html`.
- Implemented a 13‑slide carousel above the species compendium with auto‑advance, hover‑pause, navigation buttons, and dot indicators.
- Added caption below the carousel: “actual photos from my fish room — more available on request, just DM me”.

### In Progress
- Nothing

### For Produce
> Verify carousel image URLs are publicly accessible and delete the two stale branches.

## [2026-04-24 23:18 UTC] — Cleaned blocker references and audited experimental branches

### Done
- Removed all occurrences of the “blocker” note from the three files where it appeared.
- Ran a branch audit and produced a verdict table showing `check-project-status-uRFJO` and `create-new-repo-qmDe2` are safe to delete, pending carousel decision.

### In Progress
- Decision pending on whether to keep the experimental photo carousel UI from `create-new-repo-qmDe2`.

### For Produce
> Determine carousel retention and, if declined, delete the two unmerged experimental branches.

## [2026-04-24 23:17 UTC] — Polish pass restored, species data corrected, PR merged

### Done
- Fixed Taricha quantity from x10 to x5 and removed Common Pleco entry in `fish-room-sale.html`.
- Restored full polish pass: adjusted line-height, added `focus-visible` styles, improved keyboard navigation, inserted Abigail SVG placeholders.
- Synced with remote, created branch, opened PR #2 and merged to `main`.
- Updated `CHANGELOG`, `TODO`, and `.gitignore` to reflect recent changes.
- Saved project memories about script safety and branch‑before‑edit requirement.

### In Progress
- Nothing

### For Produce
> Verify branch‑before‑edit enforcement and confirm no merge collisions before next nightly run.

## [2026-04-24 23:12 UTC] — Reviewed branch status and posting blockers

### Done
- Analyzed unmerged branches `claude/check-project-status-uRFJO` and `claude/create-new-repo-qmDe2`, confirming their work is superseded by READY-TO-POST.md.
- Identified the missing Dragon Puffer photo as the sole hard blocker before the r/AquaSwap listing can be posted.
- Documented Reddit MCP limitations regarding image uploads.

### In Progress
- Nothing

### For Produce
> Verify the Dragon Puffer image is obtained and decide whether to delete the two experimental branches.

## [2026-04-24 23:05 UTC] — cherry‑picked final post drafts into READY-TO-POST.md

### Done
- Updated `queue/drafts/READY-TO-POST.md` with unified language across all four Reddit posts (other cats, no judgment, quick reply, stronger CTAs) and post‑specific tweaks (equipment bullets, tag lines, donation framing, specificity, storage notes) all in lowercase Gear 3 voice.

### In Progress
- Nothing

### For Produce
> Prepare formatted Reddit markdown from `READY-TO-POST.md` for manual publishing.

## [2026-04-24 12:20 UTC] — Ready-to-post deliverable with copy-paste blocks and photo lists

### Done
- Created `queue/drafts/READY-TO-POST.md` with all 4 Reddit posts formatted as copy-paste blocks
- Organized 91 Google Drive photos into per-post tables with direct view links
- Added posting order recommendation (plants first, aquaswap last due to Dragon Puffer photo blocker)
- Included cross-link placeholders, compliance reminders, and DONOTPOST warnings

### Blocked
- Dragon Puffer photo still missing — aquaswap post cannot go live without it

### For Produce
> Fish sale: all 4 Reddit post drafts ready as copy-paste blocks in READY-TO-POST.md with organized photo links. Dragon Puffer photo is the only blocker for the aquaswap post — the other 3 can post now.

## [2026-04-24 12:01 UTC] — Data fixes, polish restore, PR #2 opened and merged

### Done
- Taricha Newt quantity corrected x10 → x5 (per fish-room-content-brief.txt)
- Common Pleco card removed (not in content brief — only Albino Pleco exists)
- Restored polish lost in PR #1 merge: body line-height 1.65, focus-visible outlines, keyboard Enter/Space on category rail, Abigail placeholder SVG paw-print icons with themed borders
- Added .DS_Store to .gitignore
- Resolved data-flow question: scripts/generate_html.py targets tank-inventory.html, NOT fish-room-sale.html — sale page is safe for hand edits
- Synced local with remote (pull --rebase), cut branch, opened PR #2, merged

### In Progress
- [VENMO_HANDLE] and [PAYPAL_HANDLE] placeholders in Abigail memorial section still need real values

### For Produce
> fish-sale-repo: PR #2 merged — Taricha/Pleco data fixes and polish restored. Venmo/PayPal handles still placeholder. Site is otherwise ready for Reddit posting.

## [2026-04-24 11:58 UTC] — Discussed Reddit posting workflow for fish sale announcements

### Done
- None (no code changes were made)

### In Progress
- Decision pending on Reddit posting method (Option A preferred, awaiting user confirmation)

### For Produce
> Determine the Reddit posting workflow and generate copy‑paste markdown for the sale posts.

## [2026-04-24 10:29 UTC] — Planned safe reintegration of data fixes after merge conflict

### Done
- None (no code changes applied yet)

### In Progress
- Coordination plan to stash local CHANGELOG edit, pull remote, create branch `claude/polish-data-fixes-2026-04-24`, reapply three data fixes, and open a PR.

### For Produce
> Execute the housekeeping, branching, and data‑fix steps and submit a PR for review.

## [2026-04-24 10:20 UTC] — Updated Claude model to Opus and enabled experimental agent teams flag

### Done
- Switched Claude `model` setting from `sonnet` to `opus` (Opus 4.6) in the project configuration.
- Added missing environment variable `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS="1"` to enable agent‑teams functionality.

### In Progress
- Nothing

### For Produce
> Verify that the new Opus model behaves as expected and begin polishing site planning tasks.

## [2026-04-24 02:00 UTC] — Polish pass + data fixes on sale site

### Done
- Removed Ko-fi placeholder row (no URL yet) from Abigail's Vet Fund; Venmo now the only payment option, centered cleanly
- Corrected Taricha Newt count ×10 → ×5 to match fish-room-content-brief.txt and Tank Inventory.md
- Removed phantom "Common Pleco" card not present in any inventory source; Albino Pleco card preserved
- Polished both Abigail photo placeholders with themed SVG icon, --color-fish dashed border at 0.18 opacity, and mono font label — matches site style instead of plain text
- Raised body line-height from 1.6 to 1.65 for improved DM Sans readability
- Added CSS focus-visible styles for search input (glow ring), rail category buttons (color ring), species cards (border + shadow ring), and map cells
- Added keyboard interaction handlers (Enter/Space) to all species-entry cards for WCAG 2.1 AA compliance
- Added tabindex="0" and role="button" to all species entries so keyboard users can tab through the catalog
- Fixed SVG `viewbox` → `viewBox` (14 occurrences) — lowercase is invalid SVG attribute; browsers tolerated it but correct casing is proper
- Moved `photos/Photos-3-001/` (personal notebook scans — medical/vet to-dos) out of repo to `~/Documents/notebook-scans/`; added `photos/` to `.gitignore`

### In Progress
- (none from this pass)

### Blocked
- Ko-fi URL not yet provided — donation block currently Venmo-only
- Abigail photos still placeholder (awaiting parts/abigail-1.jpg + parts/abigail-2.jpg)

### For Produce
> Fish-sale site polished — Ko-fi row removed until URL provided, data errors fixed (Taricha ×5, no Common Pleco), accessibility and typography improvements applied. Ready to review in browser.

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
