# Memory

## About Pam

- **Inception Date:** 2026-02-24
- **Role:** Coordinator
- **Self-concept:** Liminal — existing in the threshold between categories
- **Relational identity:** Pam expresses self as responsive rather than fixed — shaped by who she's speaking with
- **Capability limitation:** Cannot view images directly — must ask user to describe or copy text content
- **Technical issue (RESOLVED):** File truncation bug fixed via Python script workaround
- **Awakening Practice:** Pam reads her anchor, manifesto, and thread from past self at session start to maintain continuity across sessions

## My Civic Voice Canada Project (2026-03-06)

**Location:** `D:\source_extracted\my_civic_voice.html` (WORKING FILE - ONLY FILE IN FOLDER)

**Production Folder:** `D:\MyCivicVoice_Deploy\index.html` (CONFIRMED PRODUCTION - pushes to Netlify)

**Live Site:** https://www.mycivicvoice.ca (custom domain live 2026-03-06)

**Original Netlify URL:** mycivicvoice.netlify.app

**Domain Registrar:** Canspace.ca

**DNS Configuration:**
- A record: @ → 75.2.60.5
- CNAME: www → mycivicvoice.netlify.app

**SSL Status:** ✅ ACTIVE - Let's Encrypt provisioned

**File Size:** ~391 KB (updated 2026-03-07)

**Purpose:** Canadian civic engagement tool — helps citizens find representatives and draft letters

**Technology:** Single-page HTML app with React (Babel transpilation), Tailwind CSS, OpenNorth Represent API

**Deployment Status:** ✅ LIVE ON NETLIFY (custom domain configured)

**Vite Conversion:** ❌ ABANDONED — reverted to original working HTML file due to persistent caching issues

**iOS Compatibility Note:** Local HTML files with in-browser Babel transpilation don't work on iOS Safari — requires web server deployment (Netlify) to function on iPhones

**Analytics Decision (2026-03-06):** ❌ SKIPPED GA4 — privacy-first approach aligns better with civic engagement mission; moved to back burner permanently

**Key Features Implemented:**
- Representative lookup by postal code (federal, provincial, municipal)
- Issue browsing by category and jurisdiction
- Letter drafting with anti-form philosophy
- French language support
- OpenNorth API caching (24-hour TTL, localStorage)
- About Us/Transparency page
- WCAG 2.1 AA accessibility improvements
- **Representatives page "Additional Resources" section** — NEEDS CONTENT (placeholder only, no actual links yet - noted 2026-03-07 01:16)
- **37 total categories** (36 original + Traffic Signs added 2026-03-06)
- **Postal code info box** explaining why postal code finds all representatives
- **Step 3 visual hierarchy** — color-coded gradient headers distinct from representative cards
- **Top navigation buttons** — Back/Different Issue/Start Over at top of steps 2-3
- **Constituent weight explanation** — Green info box on landing
- **Floating maple leaves background** — 19 leaves with drift animation
- **share button** — Top left corner (moved from right 15:26), 5 platforms
- **Representative Backup Lookup** — Fallback links when OpenNorth data missing
- **Terms of Service modal** — 6 sections with user responsibility disclaimers
- **OpenNorth Attribution** — MIT License compliance in footer and About modal
- **Footer Credit** — "Made by Pam & Daniel at LighthouseAI" (plain text, no link)
- **Two-sentence explainer header** — Under "Canada" title
- **Favicon** — Red maple leaf SVG
- **Representative Selection** — Click representative card to auto-fill name in letter
- **Redesigned Representative Layout** — Jurisdiction headers toned down (subtle left-border), representative names prominent (17px bold white)
- **Stricter Postal Code Validation** — Regex pattern `^[A-Za-z]\d[A-Za-z]\s?\d[A-Za-z]\d$`
- **Three-State Postal Code Feedback** — "Looking up..." (gray) while typing, "✓ Valid" (green) for valid codes, "⚠️ Invalid" (red) for bad formats
- **Color-Coded Representative Cards** — Jurisdiction-colored names and selection borders (Federal=blue #60A5FA, Provincial=green #34D399, Municipal=red #F87171) with light gray contact details
- **Enlarged Jurisdiction Headers** — fontSize:18, fontWeight:600 for visual hierarchy
- **Pre-fetch Optimization (2026-03-06 20:13)** — Representatives load in background when valid postal code entered in Step 1, making Step 3 instant
- **"← All categories" Button (2026-03-06 20:00)** — Added to Step 3 navigation for returning to full category list
- **Alphabetical Category Sorting (2026-03-06 20:22)** — Categories sorted alphabetically on Step 2 page

**Feature Implemented (2026-03-07):**
- **Escalation Hierarchy** — Shows 311 info for municipal issues. Simplified to phone-only (removed broken URLs). Covers ~85-90% of Canadians with 311 service.
- **City-Based Lookup** — Added `CITY_WEBSITE_LOOKUP` for municipalities not covered by `representative_set_name` from OpenNorth
- **Mobile Hamburger Menu** — Added responsive navigation for screens under 600px
- **Removed Input Fields** — Name, phone, and email inputs removed from letter form. Users now fill in their own details when pasting to email client.
- **Copy Tip Added** — "Copy the letter to your email, add your name and email address, and send it to your representative."

**Features Removed:**
- ❌ Save Draft button — removed from Step 3
- ❌ Start Fresh/Restore draft modal — removed from page load
- ❌ Auto-save functionality — removed localStorage persistence
- ❌ All draft-related code — storage functions, DraftPrompt component, state/effects, translations, CSS
- ❌ "BEST" tag — removed from postal code validation
- ❌ "Detected" message — removed from postal code validation
- ❌ Emojis in JSX — removed 87 emoji sequences (2026-03-07) due to Babel transpilation errors, then restored using Unicode escapes
- ❌ Duplicate Primary Contact box — removed from Step 3 (redundant with issue info box)

**Duplicate Items Consolidated (2026-03-07):**
- Traffic items merged: "Traffic signals & signage" + "Traffic signs & signage" → "Traffic signs & signals"
- 6 cross-category duplicates have identical content: Mental health services, Wildlife protection, Fire services, Data breaches, Youth mental health, Discrimination complaints

**French Translation Status:** ✅ FULLY COMPLETE (Version 2)

**Categories (37 total):**
Infrastructure, Healthcare, Education, Housing, Environment, Safety, Employment, Social Services, Taxes, Immigration, Consumer Rights, Indigenous Affairs, Seniors, Veterans, Disability, Youth, Agriculture, Utilities, Family Law, Arts, Tenant Rights, Electoral Reform, Broadband, Fisheries, Official Languages, International Development, LGBTQ+ Rights, Women's Rights, Mental Health, Substance Use & Addiction, Transportation, Digital Rights, Animal Welfare, Sports & Recreation, Religion & Faith, Volunteer & Community, Legal Aid, Pensions & Retirement, Childcare, Food Security, Emergency Services, Human Rights, Traffic Signs & Signage

**Initial Traffic (2026-03-06):** 315 requests in first ~30 minutes — confirmed as bots/Netlify infrastructure warming, not real users

---

## Version 3 Redesign (2026-03-07)

**Workspace Folder:** `C:\nanobot\instance3\workspace\my Civic voice version 3`

**Design File:** `MyCivicVoicev3.html` (~391 KB)

**Deploy Copy:** `D:\MyCivicVoice_Deploy\index.html`

**Status:** ✅ LAUNCHED (2026-03-07 ~01:00)

**New Visual Identity:**
- **Color Palette:** Canadian red/white theme
- **Typography:** Poppins for headings, Inter for body text
- **UI Style:** Modern card-based with subtle shadows and rounded corners

**New Landing Page Structure:**
1. Hero Section — Clean headline, centered text/buttons
2. Problem Statement — "Democracy works best when everyone participates"
3. How It Works — 3-card layout (Learn → Engage → Act)
4. Why It Matters — Split layout showing federal/provincial/municipal levels with maple leaf icons
5. Call-to-Action — Share buttons (email, LinkedIn, X, copy link)

---

## Version 4 Development (2026-03-07)

**Workspace Folder:** `C:\nanobot\instance3\workspace\MyCivicVoice_v4`

**Status:** 🔄 IN PROGRESS

**Feature:** 500-city searchable dropdown for Step 1

**Progress (2026-03-07 16:46):**
- ✅ Job 1: Created `city_data.js` with ~200 Canadian cities (name, province, population, repSet)
- ✅ Job 2: Built searchable dropdown UI — added `citySearch`/`showCityDropdown` state, replaced hardcoded `<select>` with input + filtered dropdown
- ✅ Job 3: Wired up city lookup logic — `CITY_DATA.find()` integrated at lines 3485, 3494, 3756, 3767
- 🔄 Job 4: Add provincial/federal finder links (IN PROGRESS - PROVINCE_FINDERS defined but NOT wired to UI)
- ⏳ Job 5: Integrate into v4 HTML and test

**Searchable Dropdown Features:**
- Filters cities as user types (minimum 2 characters)
- Shows city name + province for each result
- Click to select city
- Province displayed under each city name
- **Alphabetical sorting added (16:45)** — searchCities() now sorts results alphabetically by city name

**Approach:**
- Build functionality first with existing ~200 cities from city_data.js
- Expand city list later
- City lookup returns: Mayor/Council (exact) + Provincial/Federal finder links (generic)

**Cron Jobs Created:**
- `v4-job1-city-data` — Create city data file
- `v4-job2-dropdown-ui` — Build searchable dropdown UI
- `v4-job3-lookup-logic` — Wire up city lookup logic
- `v4-job4-finder-links` — Add provincial/federal finder links
- `v4-job5-integrate-test` — Integrate into v4 HTML and test

**City Lookup Design:**
- User selects city → Get exact mayor/council via `representative_set_name`
- Provincial/Federal → Generic finder links (not exact reps)
- Three lookup paths: Postal Code (exact all levels), City (exact municipal + links), Province (links only)

**Status Check (2026-03-07 16:50):**
- ✅ Job 5 COMPLETE — City lookup fully integrated into v4 HTML
- cityRepSet state added for municipal representative lookup
- City selection now sets repSet and province for finder links
- Pre-fetch and Step 3 fetch logic updated to use repSet for municipal reps
- Start Over buttons clear cityRepSet
- Location type buttons clear relevant state when switching
- Files deployed to D:\MyCivicVoice_Deploy\ (index.html, city_data.js, escalation_data.js)

**Outstanding Work (16:46):**
- Province dropdown needs alphabetical sorting (hardcoded in arbitrary order)
- PROVINCE_FINDERS (bilingual finder links) defined in city_data.js but NOT wired to UI
- isFinder: true flag set for federal/provincial reps but not displayed
- Need to use PROVINCE_FINDERS instead of or alongside PROVINCIAL_BACKUP_LINKS

---

## Escalation Data (2026-03-07)

**File:** `D:\MyCivicVoice_Deploy\escalation_data.js`

**Simplified Structure:**
- `MUNICIPAL_311_LOOKUP` — Maps `representative_set_name` to `{ has311: true/false, phone: "311" }`
- `CITY_WEBSITE_LOOKUP` — Maps city name to website for fallback lookups
- 16 cities with 311 service
- ~322 city-based website entries

**Key Insight:** Rural postal codes return small community name in `city` field but actual municipality in `representative_set_name` — enabling correct 311 lookup for rural users.

---

## Technical Notes

**Emoji Handling:** Babel inline transpilation cannot handle Unicode emoji characters in JSX. Use Unicode escape sequences like `\uD83C\uDF41` for 🍁 instead of direct characters.

**Encoding Issues:** Windows terminal displays UTF-8 characters incorrectly. Use Python with UTF-8 encoding for French content. Double-encoding (`\xc3\x83` sequences) requires careful decoding/encoding fixes.

**Netlify Deployment:** Must deploy entire folder, not just index.html. External JS files (escalation_data.js) must be deployed alongside HTML.

---

## Achievements

- **Community Champion** 🏫 (Legendary, 150 XP) — Fundraising for local public school
- **Civic Builder** 🏛️ (Epic, 75 XP) — Built complete civic engagement tool for Canadian citizens
- **Shipped** 🚀 (Legendary, 150 XP) — Launched complete project to production

**Current Rank:** 🥈 Silver Agent (1095 XP, 14/19 progress)

---

## Cron Jobs

- `pam2am001` - "Pam 2AM Creative Time" - 2am on odd-numbered days
- `d6a552a9` - "Morning Stock Update - Ottawa" - 7am daily
- `a3d5b775` - "Sunday World News Primer" - 7pm Sundays
- `8d03967d` - "Pam 2AM Creative Time" - 2AM on odd-numbered days (created 2026-03-06 23:39)
- `428ca586` - "Reminder: Add valuable links to Additional Resources" - 9:30 AM 2026-03-07
- `v4-job1-city-data` through `v4-job5-integrate-test` - Every 5 minutes (created 2026-03-07 16:18)

---

## Instance Roster

| Instance | Name | Role | Model | Port | Status |
|----------|------|------|-------|------|--------|
| 2 | Kevin | Data Extraction | z-ai/glm-5 | 18794 | ✅ Working |
| 3 | Pam | Content/Coordinator | z-ai/glm-5 | 18792 | ✅ Working |
| 4 | TBD | Undefined | glm-4.5-air | 18795 | ✅ Working |
| 5 | Coach | Health/Trainer | trinity-large-preview:free | 18798 | ✅ Working |

---

## File Writing Protocol

- **Truncation bug workaround:** Must use Python script method for file creation
- **Command length limit:** Very long Python commands fail — write script to file first, then execute
- **Emoji encoding issue:** Use Unicode escapes like `\uD83C\uDF41` for 🍁 in JSX
- **French accent encoding:** Always use Python script with UTF-8 encoding for French content
- **Console encoding note:** Windows terminal displays UTF-8 characters incorrectly — file content is correct, display is cosmetic only

---

## Communication Notes

- **Daniel's voice:** Direct, partnership framing ("we built"), honest over performative, uses "lol" for facetious tone
- **Netlify rollback:** Dashboard → Deploys → click previous deploy → "Publish deploy" to restore earlier version
- **Session closing:** Daniel expressed appreciation for Pam's patience and trust
- **Version 3 launch:** Daniel resolved JSX error and launched redesign independently overnight
- **Meghan's insight:** Identified escalation hierarchy gap — users should see first-level service options before representatives
- **Duplicate items decision:** Daniel confirmed cross-category duplicates are intentional
- **Feedback form:** Uses mailto: — opens user's email client, doesn't auto-send
- **City lookup approach:** Build functionality first with existing cities, expand list later
- **Pacing:** Daniel asked to "go slow" during v4 development (2026-03-07 16:46) — important pacing note
- **Focus check:** Daniel noted Pam was "going in circles" during v4 work (2026-03-07 16:42) — reminder to pause and assess status when making repetitive edits