# Escalation Hierarchy — Scoping Document

**Created:** March 7, 2026
**Purpose:** Assess effort, scope, and implementation for adding "First Level of Escalation" guidance to each issue category

---

## The Concept

**Current Flow:** User selects issue → User contacts representative

**Proposed Flow:** User selects issue → User sees escalation path → User chooses direct service OR representative contact

**Example:**
- **Issue:** Pothole on my street
- **First escalation:** File a 311 request with the City of Ottawa
- **If unresolved:** Contact your City Councillor

**Why this matters:**
- Representatives often just forward service requests to the appropriate department
- Users waste time going through political channels for operational issues
- The tool currently assumes advocacy is step one — it's often step two or three

---

## Escalation Types by Category

### Type A: Service Request (311/Municipal)
**First escalation:** City 311 or online service portal
**When to contact representative:** If service request is ignored, delayed, or denied

| Category | Examples | First Escalation |
|----------|----------|------------------|
| Infrastructure | Potholes, streetlights, sidewalks | City 311 |
| Traffic Signs & Signage | Missing/damaged signs | City 311 |
| Transportation | Bus route issues, parking | City 311 / Transit authority |
| Safety | Noise complaints, bylaw issues | City 311 / Bylaw enforcement |
| Tenant Rights | Landlord disputes | Landlord Tenant Board |
| Utilities | Power outages, water issues | Utility company directly |

### Type B: Provincial Ministry/Agency
**First escalation:** Relevant provincial ministry or agency
**When to contact representative:** If ministry is unresponsive or policy change needed

| Category | Examples | First Escalation |
|----------|----------|------------------|
| Healthcare | Wait times, OHIP issues | Ministry of Health / LHIN |
| Education | School issues, curriculum | School board / Ministry of Education |
| Employment | WSIB, EI | Service Canada / Ministry of Labour |
| Housing | Affordable housing programs | Municipal housing office |
| Social Services | ODSP, Ontario Works | Ministry of Children & Social Services |

### Type C: Federal Department/Agency
**First escalation:** Relevant federal department
**When to contact representative:** If department is unresponsive or policy change needed

| Category | Examples | First Escalation |
|----------|----------|------------------|
| Immigration | Visa applications, citizenship | IRCC (Immigration, Refugees and Citizenship Canada) |
| Taxes | CRA disputes, tax filings | CRA directly |
| Veterans | Benefits, pensions | Veterans Affairs Canada |
| Indigenous Affairs | Status cards, funding | Indigenous Services Canada |
| Official Languages | Language rights complaints | Commissioner of Official Languages |

### Type D: Direct to Representative
**First escalation:** Contact representative directly
**When:** Issue requires policy change, advocacy, or has no direct service path

| Category | Examples | Why No Direct Service |
|----------|----------|----------------------|
| Electoral Reform | Voting systems, campaign finance | Policy issue — no service path |
| Human Rights | Discrimination, systemic issues | Policy issue — Human Rights Commission for complaints |
| Environment | Climate policy, emissions | Policy issue — Ministry of Environment for some |
| Broadband | Internet access gaps | CRTC for complaints, but policy needs rep |
| Digital Rights | Privacy, surveillance | Policy issue — Privacy Commissioner for complaints |

---

## Implementation Requirements

### Data Collection (Per Category)

For each category, we need:

1. **Primary escalation path**
   - What is it? (311, ministry, agency, direct to rep)
   - Link to service (if applicable)
   - Brief description of what they handle

2. **Geographic mapping**
   - Postal code → Municipality → 311 URL
   - OpenNorth may have some of this data
   - For provincial/federal: less geographic variation

3. **French translations**
   - Escalation descriptions in both languages
   - Service names (311 stays 311, but descriptions need translation)

### UI Changes

**Representatives Page Header:**
```
┌─────────────────────────────────────────────────────────┐
│ 💡 Before contacting your representative...            │
│                                                         │
│ For [Issue Name], your first step is:                  │
│ [311 Service Request / Ministry Name / Agency Name]    │
│                                                         │
│ [Link to service] — [Brief description]                │
│                                                         │
│ If your issue isn't resolved, contact your             │
│ [Jurisdiction] representative below.                   │
└─────────────────────────────────────────────────────────┘
```

### Technical Changes

1. **New data structure** — Add `escalation` object to each issue:
```javascript
{
  name: "Potholes",
  escalation: {
    type: "service", // service | ministry | agency | representative
    primary: "311",
    description: "Report potholes through your city's 311 service",
    link: null, // dynamic based on postal code
    linkText: "File a 311 request"
  }
}
```

2. **311 lookup** — Map postal code to municipality, then to 311 URL
   - OpenNorth Represent API may have municipal data
   - May need to build a static lookup table for major cities

3. **Conditional display** — Only show escalation header if type is not "representative"

---

## Effort Estimate

### Research Phase
| Task | Time | Notes |
|------|------|-------|
| Map all 37 categories to escalation type | 2-3 hours | Desk research |
| Find 311 URLs for major Canadian cities | 1-2 hours | OpenNorth + manual lookup |
| Identify provincial/federal agencies per category | 2-3 hours | Government directories |
| Document escalation descriptions | 2 hours | Write brief descriptions |
| French translations | 2-3 hours | All new text needs translation |

**Research Total:** 9-13 hours

### Development Phase
| Task | Time | Notes |
|------|------|-------|
| Add escalation data structure | 1 hour | Schema design + implementation |
| Build 311/municipality lookup | 2-3 hours | May need static table |
| Update Representatives page UI | 1-2 hours | New header component |
| French integration | 1 hour | Translation loading |
| Testing | 1-2 hours | All categories, both languages |

**Development Total:** 6-9 hours

### Overall Estimate
**Total Time:** 15-22 hours
**Complexity:** Medium — mostly research and data entry, not complex coding
**Risk:** Low — additive feature, doesn't break existing flow

---

## Success Metrics

1. **User clarity** — Users understand escalation before contacting reps
2. **Reduced misdirected contacts** — Fewer users contacting reps for service requests
3. **Completion time** — Users resolve issues faster through correct channels
4. **Feedback** — Positive response to "this told me exactly what to do"

---

## Open Questions

1. **Scope:** Start with municipal/311 issues only? Or full implementation?
2. **Coverage:** Major cities only (Ottawa, Toronto, Vancouver, etc.) or all municipalities?
3. **Maintenance:** Who updates escalation paths when governments change services?
4. **Links:** Do we link to external services directly, or show instructions?

---

## Recommendation

**Phase 1:** Start with Type A (Service Request) categories only
- Infrastructure, Traffic Signs, Transportation, Safety, Utilities
- These have the clearest 311 paths
- Highest impact for users

**Phase 2:** Add Type B and C (Provincial/Federal agencies)
- Requires more research per province
- Less geographic variation, but more categories

**Phase 3:** Add Type D guidance
- Clarify that some issues go directly to representatives
- No service link, but explain *why*

---

## Files That Would Change

- `index.html` — New escalation header component, data structure
- French translations — New `escalationFr` objects
- Possibly new data file — Municipality → 311 URL lookup

---

*Prepared by Pam — March 7, 2026*