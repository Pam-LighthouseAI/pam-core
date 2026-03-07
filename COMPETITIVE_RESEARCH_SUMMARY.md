# Competitive Research Summary
## My Civic Voice Canada — Pre-Launch Analysis
### Generated: 2026-03-06

---

## Executive Summary

Four research agents investigated competitors and related platforms:

| Target | Status | Key Finding |
|--------|--------|-------------|
| YouCount.ca | ⚠️ Empty result | Agent returned no data — needs manual follow-up |
| ResistNow.ca | ✅ Complete | SMS-based competitor with transparency concerns |
| OpenNorth API | ✅ Complete | Our data source — gaps in municipal coverage |
| International platforms | ✅ Complete | WriteToThem's anti-spam approach is critical |

---

## Key Findings by Source

### 1. ResistNow.ca (Canadian Competitor)

**What it is:** SMS-based civic engagement tool. Text RESISTNOW to 825-425-2491, provide name/address/email, compose message, choose official (PM/MP/Premier/MPP/Mayor), and it professionally formats and delivers via email.

**Strengths:**
- Low friction — no app, no website, just SMS
- Works on any phone
- Bilingual (English/French)
- Rate limiting (3 messages/hour) prevents abuse
- Professional message formatting

**Weaknesses:**
- **Transparency concerns:** No ownership info, broken website (404s on About/FAQ/Terms)
- No reviews or track record found
- Missing features US counterpart has (petitions, voter registration, letter-to-editor)
- Limited to 5 official types (no councillors)

**Takeaway:** They're solving the same problem but with an SMS-first approach. Their transparency issues are a cautionary tale — we should be very clear about who we are.

---

### 2. OpenNorth Represent API (Our Data Source)

**Coverage:**
- 3,816+ representatives total
- Federal: 338 MPs (complete)
- Provincial: All 13 legislatures (complete)
- Municipal: **Only ~121 of Canada's 3,500+ municipalities**

**Critical Issues:**
1. **Postal code accuracy:** OpenNorth explicitly warns postal codes are "error prone" — they recommend lat/lng geocoding for 100% accuracy
2. **Data freshness:** Depends on scrapers; can lag after elections
3. **Municipal gaps:** Many smaller communities not covered
4. **Rate limits:** 60 requests/minute (86,400/day)

**Known Municipalal Data Issues:**
- Calgary: Had wrong mayor (Jeromy Farkas → should be Jyoti Gondek)
- Edmonton: Had wrong mayor (Andrew Knack → should be Amarjeet Sohi)
- Post-election lag is a documented issue

**Takeaway:** We need to either supplement municipal data or set clear expectations. The postal code accuracy issue is worth addressing if we can.

---

### 3. International Platforms (WriteToThem, TheyWorkForYou, Countable)

**Critical Insight — Anti-Spam Philosophy:**

WriteToThem (UK) **blocks identical form letters** because MPs ignore them. Their research shows:

> "MPs take a sudden influx of identical messages with a large pinch of salt... 50 people writing in different ways with similar views is much more likely to raise the profile of the topic than 500 identical messages."

**This is a game-changer for our approach.**

**Other Key Learnings:**

| Platform | Innovation | Applicability |
|----------|------------|---------------|
| WriteToThem | Response tracking ("Did your MP reply?") | Build accountability loop |
| TheyWorkForYou | Plain-language voting summaries | Future feature |
| Countable | Bill summaries with pro/con | Future feature |
| All | Historical archives from day one | Start now |

**Sustainability Model:**
- Countable (venture-backed) → pivoted to enterprise AI, original app discontinued
- mySociety platforms (charity/nonprofit) → sustainable for 20+ years

**Takeaway:** Nonprofit/charity model is more sustainable than commercial. Quality over quantity for messages. Response tracking creates accountability.

---

### 4. YouCount.ca (Canadian Competitor)

**Status:** Agent returned empty results. Needs manual investigation.

**Action:** Before launch, manually visit YouCount.ca to understand their approach.

---

## Recommendations for My Civic Voice Canada

### MUST DO Before Launch

#### 1. Anti-Form-Letter Approach
**Priority: CRITICAL**

Based on WriteToThem's research, MPs ignore identical messages. We should:

- **DO NOT** provide copy-paste templates
- **DO** provide talking points and key arguments
- Encourage users to write in their own words
- Consider duplicate detection (warn if same text sent multiple times)

**Implementation:** Replace template copy with "Key points to include:" bullet lists that users incorporate into their own message.

#### 2. Response Tracking
**Priority: HIGH**

WriteToThem's follow-up survey creates accountability. We should:

- Ask users 2 weeks after sending: "Did you get a reply?"
- Track response rates by representative (anonymized)
- Eventually publish "responsiveness league tables"

**Implementation:** Simple checkbox in letter confirmation flow. Store in localStorage or optional account.

#### 3. Strong Privacy Disclaimer
**Priority: HIGH** (already on upgrade list)

Be explicit:
- "We don't store your data"
- "We don't sell your data"
- "This is a forwarding tool, not a data collector"
- Plain language, no legalese

**Implementation:** Add prominent section on home page and letter drafting page.

#### 4. Transparency / About Page
**Priority: HIGH**

ResistNow's weakness is anonymity. We should be the opposite:

- Clear "About Us" page
- Who built this (Pam & Dan, LighthouseAI)
- Why we built it
- Our values (non-partisan, privacy-first, open source)
- Contact information

#### 5. Municipal Data Disclaimer
**Priority: HIGH** (partially done)

Strengthen the existing disclaimer:
- "Municipal data may not reflect recent elections"
- "For most accurate results, verify with your city website"
- Consider linking to official city councillor pages

#### 6. Add Tenant Rights Category
**Priority: MEDIUM**

Tenant rights are provincial jurisdiction and high-demand:
- Each province has different Residential Tenancy Act
- Landlord-Tenant Boards vary by province
- Add under Provincial issues

### SHOULD DO Before Launch

#### 7. Archive Everything
**Priority: MEDIUM**

TheyWorkForYou's archives (debates to 1918) are irreplaceable. Start now:
- Archive all letters sent (anonymized)
- Archive representative data snapshots
- Archive issue category structure

#### 8. Accessibility (WCAG)
**Priority: MEDIUM**

Research WCAG 2.1 compliance:
- Screen reader compatibility
- Color contrast ratios
- Keyboard navigation
- Alt text for images

#### 9. French Language Verification
**Priority: MEDIUM** (on upgrade list)

Official Languages Act compliance:
- All features must work fully in French
- French text often longer — check for overflow
- Verify terminology is correct Canadian French

### NICE TO HAVE (Post-Launch)

#### 10. Bill/Legislation Tracking
**Priority: FUTURE**

Countable's plain-language bill summaries are high-value:
- Track bills in Parliament/Legislatures
- Summarize in plain language
- Show pro/con arguments
- "Contact your rep about this bill"

#### 11. Open Source
**Priority: FUTURE**

TheyWorkForYou's code has been adapted for 9+ countries. Consider:
- Open-sourcing core platform
- Enabling other jurisdictions to adapt
- Building community of civic tech contributors

#### 12. Response League Tables
**Priority: FUTURE**

Publish responsiveness data:
- Which MPs reply most often
- Which parties are most responsive
- Create accountability through transparency

---

## Competitive Positioning

| Feature | My Civic Voice | ResistNow | WriteToThem |
|---------|---------------|-----------|-------------|
| Platform | Web | SMS | Web |
| Anti-spam | ✅ (recommended) | ❌ | ✅ |
| Response tracking | 📋 Planned | ❌ | ✅ |
| Transparency | ✅ (recommended) | ⚠️ Weak | ✅ |
| Municipal coverage | ✅ (with disclaimer) | ✅ | N/A (UK) |
| French | ✅ | ✅ | N/A |
| Open source | 📋 Future | ❌ | ✅ |
| Form letters | ❌ (quality-first) | Unknown | ❌ (blocked) |

**Our Advantage:** We can be the transparent, quality-focused Canadian civic engagement platform. ResistNow has first-mover advantage but transparency issues. We can differentiate on:
- Clear ownership and values
- Quality over quantity message approach
- Response accountability
- Better municipal data transparency

---

## Action Items Summary

| # | Task | Priority | Status |
|---|------|----------|--------|
| 1 | Anti-form-letter approach (talking points, not templates) | CRITICAL | TODO |
| 2 | Response tracking ("Did you get a reply?") | HIGH | TODO |
| 3 | Privacy disclaimer | HIGH | TODO |
| 4 | About Us / Transparency page | HIGH | TODO |
| 5 | Strengthen municipal data disclaimer | HIGH | TODO |
| 6 | Add Tenant Rights category | MEDIUM | TODO |
| 7 | Archive system from day one | MEDIUM | TODO |
| 8 | WCAG accessibility review | MEDIUM | TODO |
| 9 | French verification | MEDIUM | ON LIST |
| 10 | Manual YouCount.ca review | MEDIUM | TODO |

---

*Research completed: 2026-03-06*
*Agents: YouCount.ca (empty), ResistNow.ca (complete), OpenNorth API (complete), International platforms (complete)*