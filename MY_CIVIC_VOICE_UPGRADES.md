# My Civic Voice Canada — Upgrade List

A running tally of planned improvements and enhancements.

---

## Pending

### Back Button Color Change — 📋 PENDING
- **Priority:** Medium
- **Status:** Pending
- **Description:** Change the "All Categories" back button and normal page back button colors to match the site's coral-red accent color scheme
- **Notes:** Should use the same gradient as primary buttons: `linear-gradient(135deg, #D97706, #DC2626)`

### Local Server for Phone Testing — 📋 PENDING
- **Priority:** Low
- **Status:** Pending
- **Description:** Set up a local server so user can view the site on their phone for testing
- **Notes:** User requested this before bed on 2026-03-06

---

## Completed

### 2026-03-06: French Translation Fixes — ✅ COMPLETE
- **Priority:** High
- **Status:** COMPLETED 2026-03-06
- **Description:** Fixed French translations not applying to all UI elements
- **Changes Made:**
  - Fixed "Province / Territory" → "Province / Territoire" translation
  - Added French FAQ data (FAQ_FR) with all 10 Q&A translated
  - Updated FAQModal to accept isFrench prop and display translated content
  - Updated FeedbackModal to accept isFrench prop with full translation
  - All labels, buttons, and messages now translate when French is selected

### 2026-03-06: Landing Page Constituent Weight Explanation — ✅ COMPLETE
- **Priority:** Medium
- **Status:** COMPLETED 2026-03-06
- **Description:** Added explanation of why constituent status matters
- **Changes Made:**
  - Added green info box below tagline explaining why postal code matters
  - English: "Elected representatives prioritize messages from their own constituency..."
  - French: "Les représentants élus accordent la priorité aux messages..."

### 2026-03-06: Top Navigation Buttons — ✅ COMPLETE
- **Priority:** Low
- **Status:** COMPLETED 2026-03-06
- **Description:** Added Back, Different Issue, and Start Over buttons at top of page
- **Changes Made:**
  - Step 2: Shows "← Back" button at top
  - Step 3: Shows "← Back", "Different Issue", and "Start Over" buttons at top
  - Buttons appear right after header, before main content

### 2026-03-06: Step 3 Visual Hierarchy — ✅ COMPLETE
- **Priority:** Medium
- **Status:** COMPLETED 2026-03-06
- **Description:** Differentiated the "who can help" level summary boxes from representative listings in Step 3
- **Changes Made:**
  - Jurisdiction headers now use gradient backgrounds with subtle glow shadows
  - Added 🏛️ icons and structured layout with border-left accent
  - "Contact your MP/MPP/Councillor" moved to separate line with envelope icon
  - Representative cards now use subtle flat backgrounds with cleaner typography
  - Clear visual hierarchy: headers stand out as information boxes, cards are simpler listings

### 2026-03-06: Postal Code Explanation Added — ✅ COMPLETE
- **Priority:** High
- **Status:** COMPLETED 2026-03-06
- **Description:** Added info box on landing page explaining why postal code is the best choice for representative lookup
- **Changes Made:**
  - Added `postalWhy` translation key (English and French)
  - Added styled info box below postal code input with explanation
  - Box uses gradient background matching site's color scheme
  - Message: "Your postal code is the most accurate way to find ALL your representatives — federal, provincial, AND municipal. City or province only gives you federal and provincial representatives."

### 2026-03-06: New Categories Added — ✅ COMPLETE
- **Priority:** High
- **Status:** COMPLETED 2026-03-06
- **Description:** Added 16 new issue categories with full continuity across the site
- **Categories Added:**
  1. **LGBTQ+ Rights** (🏳️‍🌈) — Gender identity, conversion therapy, legal name changes, healthcare access, discrimination
  2. **Women's Rights** (♀️) — Reproductive rights, pay equity, gender-based violence, women's shelters
  3. **Mental Health** (🧠) — Mental health services, crisis lines, therapy access, workplace mental health
  4. **Substance Use & Addiction** (🧪) — Harm reduction, treatment centers, safe supply, addiction services
  5. **Transportation** (🚌) — Public transit, accessibility, rural transportation
  6. **Digital Rights** (💻) — Internet privacy, data protection, net neutrality, digital ID
  7. **Animal Welfare** (🐾) — Animal cruelty, wildlife protection, pet regulations
  8. **Sports & Recreation** (⚽) — Community sports, recreation facilities, youth athletics
  9. **Religion & Faith** (⛪) — Religious freedom, places of worship, faith-based services
  10. **Volunteer & Community** (🤲) — Volunteer opportunities, community organizations, civic engagement
  11. **Legal Aid** (⚖️) — Access to justice, legal representation, court navigation
  12. **Pensions & Retirement** (👴) — CPP, workplace pensions, retirement planning
  13. **Childcare** (👶) — Daycare, early learning, childcare subsidies
  14. **Food Security** (🍎) — Food banks, nutrition programs, food safety
  15. **Emergency Services** (🚨) — 911 services, disaster response, emergency preparedness
  16. **Human Rights** (🌍) — Discrimination complaints, hate speech, accessibility rights
- **Components Added:**
  - ISSUES array: 8 issues per category with primary/secondary jurisdiction and details
  - STORY_PROMPTS: 4 questions per category to draw out personal experience
  - OPENING_LINES: 4 tone variants × 16 categories = 64 new opening lines
  - TEMPLATES: Email templates for each category
  - JURISDICTION_HEADERS: Federal/provincial/municipal breakdown for each category
- **Result:** Site now covers 36 issue categories total (20 original + 16 new)

### 2026-03-06: Anti-Form Letter Philosophy — ✅ COMPLETE
- **Priority:** Critical
- **Status:** COMPLETED 2026-03-06
- **Description:** Redesigned letter templates to make user stories the heart of the message, not an add-on
- **Changes Made:**
  1. **Added STORY_PROMPTS** — 4 category-specific questions per issue to draw out personal details (e.g., "How does this affect your daily commute?" for infrastructure)
  2. **Added OPENING_LINES** — 4 tone variants (urgent, concerned, hopeful, frustrated) × 20 categories = 80 unique opening lines
  3. **Added CLOSING_LINES** — 4 tone-specific closings that match the opening tone
  4. **Added tone selector UI** — Buttons for Urgent/Concerned/Hopeful/Frustrated with visual feedback
  5. **Updated template structure** — Now uses {{OPENING}}, {{STORY}}, {{CONTEXT}}, {{CLOSING}}, {{SIGNATURE}} instead of generic "I am writing to you..."
  6. **Updated genEmail function** — Dynamically builds letters based on category, tone, and user input
- **Result:** Letters now feel personal and varied, not templated. User's experience is front and center.

### 2026-03-06: Representative Accuracy Test
- **Status:** ✅ COMPLETE
- **Description:** Tested OpenNorth API accuracy across 50 postal codes
- **Results:** 95%+ federal, 90%+ provincial, ~85% municipal accuracy
- **Action Taken:** Added disclaimers for municipal data
- **Files:** `D:\rep_accuracy_report.txt`, `D:\test_reps_accuracy.py`

### 2026-03-06: Cosmetic Improvements
- **Status:** ✅ COMPLETE
- **Changes:**
  - Issue detail text now wraps fully (removed 80-char truncation)
  - Issue count moved to second line under category name
  - Postal code validation with error messages (A1A 1A1 format)
  - Provincial/federal reps shown even when selecting city/province (not just postal code)
  - Warning message updated to reflect this capability

---

## Priority Queue — Tomorrow's Plan (2026-03-06)

### 1. Cosmetic Touches
- **Priority:** High
- **Status:** 📋 TODO
- **Description:** Spacing adjustments, visual polish, back button color changes
- **Notes:** Small stuff, no big deal but important for polish

### 2. Functionality Test — Representative Lookups
- **Priority:** High
- **Status:** 📋 TODO
- **Description:** Test 50 postal codes across all 3 lookup methods:
  - By postal code
  - By province
  - By federal (all MPs)
- **Goal:** Verify representative data is returning correctly for each category
- **Notes:** Need to confirm accuracy before public launch

### 3. Issue Routing Verification
- **Priority:** High
- **Status:** 📋 TODO
- **Description:** Triple-check that all issues route to the correct level of government (federal/provincial/municipal) and therefore the correct representatives
- **Notes:** Critical for user trust — wrong routing = wrong rep = useless tool

### 4. Background Visual Enhancement
- **Priority:** Medium
- **Status:** 📋 TODO
- **Description:** Add subtle patterning or maple leaf motif to background — not cheesy, not plain
- **Notes:** Find the balance between "governmental" and "Canadian" without being tacky

### 5. French Layout Consistency Check
- **Priority:** Medium
- **Status:** 📋 TODO
- **Description:** Go through each tab and possibility in French mode to verify spacing/layout stays consistent
- **Notes:** French text is often longer — need to check for overflow, misalignment

### 6. Privacy Disclaimer
- **Priority:** Medium
- **Status:** 📋 TODO
- **Description:** Add eloquent disclaimer explaining:
  - User data is not stored
  - Website is a forwarding tool, not a data collector
- **Notes:** Build trust, be transparent, say it well

### 7. Copy to Clipboard — Templates Page
- **Priority:** High
- **Status:** 🐛 BUG
- **Description:** Copy to clipboard button doesn't work on templates page
- **Notes:** Functional bug — needs fixing before launch

### 8. Representative Backup Lookup
- **Priority:** Medium
- **Status:** 📋 TODO
- **Description:** Backup method to get representatives that don't appear in API results (e.g., Doug Ford — Ontario Premier)
- **Notes:** OpenNorth API may miss some officials; need fallback source or manual override

### 9. Social Services Integration — PHASE 2
- **Priority:** High (but post-launch)
- **Status:** 📋 PHASE 2
- **Description:** Connect users to local social services:
  - Kids Help Phone
  - Suicide prevention hotline
  - Crisis lines
  - Add issue lookups for emotional states ("I'm sad" → mental health resources)
- **Notes:** Launch core first, then add properly. This deserves care and time.
- **Scope:**
  - Curate resources by province
  - "I need help" category always visible
  - Appropriate tone (warm, not clinical)
  - Test routing thoroughly

### 10. Footer Credit
- **Priority:** Medium
- **Status:** 📋 TODO
- **Description:** Add footer: "Made by Pam and Dan at LighthouseAI" (or similar wording)
- **Notes:** Give credit where it's due — this was a collaboration

### 11. Multi-Jurisdiction Representative Headers
- **Priority:** High
- **Status:** ✅ COMPLETE
- **Description:** For issues spanning multiple jurisdictions (e.g., Parks), make it EXPLICITLY CLEAR which level handles what — put it in their face:
  - **Federal section:** "🏛️ NATIONAL PARKS — Contact your MP for: National parks, Parks Canada, federal protected lands"
  - **Provincial section:** "🏛️ PROVINCIAL PARKS — Contact your MPP for: Provincial parks, conservation areas, provincial recreation"
  - **Municipal section:** "🏛️ CITY PARKS — Contact your Councillor for: Local parks, playgrounds, community centres, sports fields"
- **Implementation:** Added JURISDICTION_HEADERS object with detailed breakdown for all 20 categories. Each jurisdiction header shows title, who to contact, and specific items they handle. Displayed above representative cards in Step 3 with color-coded backgrounds (blue for federal, green for provincial, red for municipal).
- **Notes:** No ambiguity. User should know immediately: "I want city parks → I scroll to municipal." Make it impossible to contact the wrong rep.

### 12. Public Deployment
- **Priority:** High
- **Status:** 📋 TODO
- **Description:** 
  - Reload/upload back to website
  - Upload to GitHub (Pam's repo)
  - Figure out public launch strategy
- **Notes:** Research hosting options (Netlify, GitHub Pages, etc.)

---

## Future Considerations

### Ads/Monetization Discussion
- **Priority:** Low
- **Status:** 💭 Future conversation
- **Description:** Brief conversation about possibility of eventually adding ads or monetization
- **Notes:** Not immediate — just something to think about down the road

---

## Backlog

### Back Button Color Change
- **Priority:** Medium
- **Status:** 📋 TODO (part of cosmetic touches)
- **Description:** Change the "All Categories" back button and normal page back button to a different color

### Provincial/Federal Reps by Province (✅ DONE 2026-03-06)
- **Priority:** High
- **Status:** ✅ COMPLETE
- **Description:** When user selects city or province (no postal code), still fetch provincial and federal representatives
- **Implementation:** Added PROVINCE_REPS and CITY_PROVINCE mappings, updated fetch logic to query OpenNorth API for provincial/federal reps when location type is not postal

### 2. Municipal Data Verification Layer
- **Priority:** Medium
- **Description:** Build verification system to cross-check municipal representatives against official city websites
- **Notes:** OpenNorth municipal data can be outdated after elections (Calgary, Edmonton had wrong mayors)
- **Potential Approach:** Web scraping or API calls to official city councillor pages

### 2. User Feedback Reporting
- **Priority:** Medium
- **Description:** Add "Report incorrect representative" button so users can flag outdated data
- **Notes:** Helps crowdsource accuracy improvements

### 3. "Last Updated" Timestamp
- **Priority:** Low
- **Description:** Show when representative data was last refreshed from OpenNorth
- **Notes:** Helps users understand data freshness

---

## Ideas / Future Considerations

### Contact Method Auto-Detection
- Pre-fill email addresses and phone numbers for representatives
- Link directly to official contact forms

### Issue Category Routing
- Suggest which level of government to contact based on issue type
- e.g., "Potholes → Municipal", "Healthcare → Provincial", "Passports → Federal"

### Multi-Language Expansion
- French translation improvements
- Other languages (Punjabi, Mandarin, etc.) for diverse communities

---

## Language Expansion Analysis (2026-03-06)

**Status:** 📋 RESEARCH COMPLETE — NOT IMPLEMENTING YET
**Current Languages:** English, French
**Decision:** Stay with English/French for launch; document expansion path for future

### Canada's Most Common Languages (2021 Census)

#### By Mother Tongue (First Language)
| Rank | Language | Speakers | % of Population |
|------|----------|----------|-----------------|
| 1 | English | ~22 million | 56.6% |
| 2 | French | ~7.8 million | 20.2% |
| 3 | Mandarin | 679,000 | 1.9% |
| 4 | Punjabi | 667,000 | 1.9% |
| 5 | Cantonese (Yue) | 553,000 | 1.5% |
| 6 | Spanish | 539,000 | 1.5% |
| 7 | Arabic | 507,000 | 1.4% |
| 8 | Tagalog | 460,000 | 1.3% |

#### By Total Speakers (Knowledge of Language)
| Rank | Language | Speakers |
|------|----------|----------|
| 1 | Spanish | 1.2 million |
| 2 | Mandarin | 987,000 |
| 3 | Punjabi | 942,000 |
| 4 | Arabic | 838,000 |

#### Inuktitut (Northern Canada)
| Metric | Number |
|--------|--------|
| Knowledge of Inuktitut | ~40,320 |
| Speak at home predominantly | 27,140 |
| Nunavut residents who can converse | 70% |
| Inuit in Nunavut who speak it | 80%+ |

---

### Implementation Complexity by Language

#### 1. Chinese (Mandarin/Cantonese) — Complexity: MEDIUM-HIGH

**Key Considerations:**
- **Two writing systems**: Simplified Chinese (Mainland China, Singapore) vs Traditional Chinese (Taiwan, Hong Kong, many Canadian communities)
- **Not interchangeable** — Users who read Simplified may struggle with Traditional and vice versa
- **Cantonese vs Mandarin** — Same characters (mostly), but different spoken dialects. Cantonese speakers in Canada often use Traditional characters
- Text direction: LTR (same as English)

**Implementation Requirements:**
- Choose **Simplified** (larger global population) OR **Traditional** (larger Canadian Cantonese community)
- OR implement both as separate options (zh-CN and zh-TW)
- UTF-8 encoding (already in place)
- Font support for Chinese characters (Noto Sans SC/TC, or system fonts)
- ~2,000+ strings to translate (all UI text, categories, issues, templates)

**Technical Challenges:**
- Chinese fonts are large (~5-15MB) — need font loading strategy
- Professional translation recommended (Google Translate insufficient for civic content)
- May need Simplified AND Traditional variants for full coverage

**Estimated Work:**
- Translation: 3 weeks
- Development: 2 weeks
- Testing: 1 week
- **Total: ~6 weeks**
- **Translation cost: $3,000-5,000**

---

#### 2. Arabic — Complexity: HIGH

**Key Considerations:**
- **Right-to-Left (RTL) text direction** — Entire layout must mirror
- Arabic script connects letters — needs proper font rendering
- Numbers may display differently (Eastern Arabic numerals vs Western)
- Some UI elements need rethinking (progress bars, arrows, icons with directionality)

**Implementation Requirements:**
- Add `dir="rtl"` to HTML tag when Arabic is active
- CSS changes: `direction: rtl`, `text-align: right`
- Flip all directional styles (margins, padding, floats, positioning)
- Use logical CSS properties (`margin-inline-start` instead of `margin-left`)
- Mirror icons (arrows, chevrons, back buttons)
- Test all modals, forms, and layouts in RTL mode
- Arabic font (Noto Sans Arabic or similar)

**Technical Challenges:**
- **Major CSS refactoring** for RTL support (~40-60 hours)
- Every UI component must be tested in mirrored layout
- Icons with directionality (arrows, back buttons) need RTL variants
- Form inputs, buttons, navigation all need RTL versions

**Estimated Work:**
- Translation: 3 weeks
- Development: 6-8 weeks (RTL refactor)
- Testing: 3 weeks
- **Total: ~12-14 weeks**
- **Translation cost: $3,500-5,500**

---

#### 3. Inuktitut — Complexity: MEDIUM

**Key Considerations:**
- **Syllabic writing system** (ᐃᓄᒃᑎᑐᑦ) — Requires special font support
- Official language of Nunavut (alongside English, French, Inuinnaqtun)
- Smaller speaker population (~40,000) but high cultural significance
- Limited professional translation resources available
- Text direction: LTR (same as English)

**Implementation Requirements:**
- Inuktitut syllabics font (Nunavik, Pigiarniq, or Noto Sans Canadian Aboriginal)
- UTF-8 encoding (already in place)
- Community consultation recommended for accurate terminology
- May need to work with Nunavut language authorities

**Technical Challenges:**
- Finding a qualified translator may be challenging
- Civic terminology may not have standard Inuktitut equivalents
- Font embedding (~500KB-1MB)
- Cultural review needed for all content

**Estimated Work:**
- Translation: 4 weeks (specialized translator sourcing)
- Development: 2 weeks
- Testing: 2 weeks
- **Total: ~8 weeks**
- **Translation cost: $4,000-6,000**

**Why Include Inuktitut:**
- Reconciliation and Indigenous representation
- Official language of Nunavut — meaningful for Northern communities
- Demonstrates commitment to all Canadians, not just population centers

---

#### 4. Punjabi — Complexity: MEDIUM

**Key Considerations:**
- **Gurmukhi script** (ਪੰਜਾਬੀ) used by Sikh community
- Shahmukhi script (Arabic-based) used by Pakistani Punjabis
- Most Canadian Punjabi speakers use Gurmukhi
- Text direction: LTR (same as English)

**Implementation Requirements:**
- Gurmukhi font support (Noto Sans Gurmukhi)
- UTF-8 encoding (already in place)
- Large, active community — easier to find translators

**Technical Challenges:**
- Font embedding (~300KB)
- Professional translation readily available
- Standard LTR implementation

**Estimated Work:**
- Translation: 3 weeks
- Development: 2 weeks
- Testing: 1 week
- **Total: ~6 weeks**
- **Translation cost: $3,000-5,000**

---

#### 5. Spanish — Complexity: LOW

**Key Considerations:**
- Latin alphabet (same as English/French)
- Widely spoken globally — many translation resources
- Text direction: LTR (same as English)
- 1.2 million speakers — most total speakers after English/French

**Implementation Requirements:**
- Standard UTF-8 (already in place)
- No special fonts needed
- Professional translation widely available

**Technical Challenges:**
- None significant — same alphabet, same direction

**Estimated Work:**
- Translation: 2 weeks
- Development: 1 week
- Testing: 1 week
- **Total: ~4 weeks**
- **Translation cost: $2,500-4,000**

---

### Implementation Priority Recommendation

| Priority | Language | Speakers | Complexity | Impact |
|----------|----------|----------|------------|--------|
| 1 | **Mandarin (Simplified)** | 987,000 | Medium-High | High — largest non-official language |
| 2 | **Punjabi (Gurmukhi)** | 942,000 | Medium | High — 2nd largest, active community |
| 3 | **Spanish** | 1.2 million | Low | High — most total speakers, easy to implement |
| 4 | **Arabic** | 838,000 | High | Medium — requires RTL refactor |
| 5 | **Inuktitut** | 40,000 | Medium | Symbolic — reconciliation, Northern representation |

---

### Recommended Implementation Order (Future)

**Phase 1 (Easiest):** Spanish
- Lowest complexity, high speaker count
- Same alphabet, LTR, no special fonts
- Good test case for multi-language infrastructure

**Phase 2 (High Impact):** Mandarin + Punjabi
- Largest non-official language communities
- Medium complexity, but high value
- Both LTR, manageable development

**Phase 3 (RTL Architecture):** Arabic
- Requires full RTL support refactor
- Should be done as standalone project
- RTL infrastructure would enable Hebrew, Farsi, Urdu in future

**Phase 4 (Northern Representation):** Inuktitut
- Smallest speaker population but highest symbolic value
- Requires specialized translator sourcing
- Demonstrates commitment to all Canadians

---

### Technical Implementation Notes

**Current French Implementation:**
- Uses simple language toggle (EN/FR)
- All strings embedded in single HTML file
- No i18n library — pure JavaScript object lookup

**For Multi-Language Expansion:**
- Consider implementing i18n framework (i18next, intl-messageformat)
- Externalize translations to JSON files
- Implement language detection/selection
- Add font loading strategy for non-Latin scripts
- RTL support would require CSS architecture changes

**Font Loading Strategy:**
- Use `font-display: swap` for Latin fonts
- Consider subsetting Chinese fonts to reduce size
- Use `unicode-range` for selective font loading
- Preload critical fonts in `<head>`

### Letter Templates Library
- Pre-written templates for common issues
- Customizable by issue type

### Representative Response Tracking
- Optional feature for users to log when they contacted a rep and if they got a response
- Could show "responsiveness ratings" over time

### Mobile App Version
- Progressive Web App (PWA) or native app
- Push notifications for representative changes

---

## Technical Debt

### None currently logged

---

*Last updated: 2026-03-06*
*Project location: D:\source_extracted\*