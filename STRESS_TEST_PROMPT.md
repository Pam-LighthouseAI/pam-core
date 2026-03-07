# My Civic Voice — 100-Point Stress Test

**Start Time:** [Send this prompt to both Pam (Instance 3) and Kevin (Instance 2)]

**Objective:** Execute a comprehensive stress test of the My Civic Voice website located at `D:\source_extracted\my_civic_voice.html`. Test 100 discrete elements and log all results.

---

## Test Categories

### 1. French Translations (25 tests)
Open the HTML file and verify French translations are present and grammatically correct for:

- [ ] Landing page tagline (EN + FR)
- [ ] All 36 category names (EN + FR)
- [ ] All category descriptions (EN + FR)
- [ ] All issue detail text (EN + FR)
- [ ] Navigation buttons (Back, Start Over, Different Issue)
- [ ] Step 1, 2, 3 headers
- [ ] FAQ modal content
- [ ] Privacy modal content
- [ ] About Us page content
- [ ] Representative contact box labels
- [ ] Letter template placeholders
- [ ] Error messages
- [ ] Jurisdiction headers (Federal/Provincial/Municipal in FR)
- [ ] Share button labels

**Method:** Use web search to verify official French government terminology where applicable (e.g., "député" for MP, "conseiller municipal" for councillor).

---

### 2. Navigation Flow (15 tests)
Test the user journey:

- [ ] Landing → Step 1 (postal code entry)
- [ ] Step 1 → Step 2 (category selection)
- [ ] Step 2 → Step 3 (issue detail + representatives)
- [ ] Step 3 → Letter composition
- [ ] Back button from Step 2 (returns to Step 1)
- [ ] Back button from Step 3 (returns to Step 2)
- [ ] "Different Issue" button (returns to Step 2)
- [ ] "Start Over" button (returns to landing)
- [ ] Language toggle EN → FR (all content switches)
- [ ] Language toggle FR → EN (all content switches)
- [ ] Share button opens modal
- [ ] Privacy link opens modal
- [ ] About Us link opens page
- [ ] FAQ accordion expands/collapses
- [ ] Postal code validation (valid vs invalid format)

---

### 3. Category & Issue Routing (30 tests)
For each category, verify the primary jurisdiction is correct via web search:

Test these 30 categories:
1. Healthcare → Provincial
2. Education → Provincial (Federal for Indigenous)
3. Infrastructure → Municipal/Provincial
4. Housing → Multi-level
5. Environment → Federal/Provincial/Municipal
6. Safety → Multi-level
7. Employment → Federal/Provincial
8. Social Services → Provincial/Municipal
9. Taxes → Federal/Provincial/Municipal
10. Immigration → Federal
11. Consumer Rights → Federal/Provincial
12. Indigenous Affairs → Federal
13. Seniors → Federal/Provincial
14. Veterans → Federal
15. Disability → Federal/Provincial
16. Youth → Provincial/Municipal
17. Agriculture → Federal/Provincial
18. Utilities → Provincial/Municipal
19. Family Law → Provincial
20. Arts → Federal/Provincial/Municipal
21. Tenant Rights → Provincial
22. Electoral Reform → Federal/Provincial
23. Broadband → Federal/Provincial
24. Fisheries → Federal
25. Official Languages → Federal
26. Mental Health → Provincial/Federal
27. Transportation → Municipal/Provincial/Federal
28. Digital Rights → Federal
29. Animal Welfare → Provincial/Municipal
30. Emergency Services → Municipal/Provincial

**Method:** Web search "Canada [issue] government responsibility" and verify the `primary` field in the HTML matches the correct level.

---

### 4. Representative Lookup (30 tests)
Test 30 postal codes across all provinces/territories. For each:

1. Query OpenNorth API: `https://represent.opennorth.ca/postcodes/[POSTAL]/?format=json`
2. Web search the elected representative name to verify they're current
3. Check that federal, provincial, and municipal levels are all populated (where available)

**Postal Codes to Test:**

| # | Location | Postal Code |
|---|----------|-------------|
| 1 | Ottawa ON | K1A0A1 |
| 2 | Toronto ON | M5V3L9 |
| 3 | Vancouver BC | V6B1A1 |
| 4 | Calgary AB | T2P1B9 |
| 5 | Montreal QC | H2Y1C6 |
| 6 | Winnipeg MB | R3C4G6 |
| 7 | Halifax NS | B3J2S7 |
| 8 | Saskatoon SK | S7K5A3 |
| 9 | Regina SK | S4P3E2 |
| 10 | Edmonton AB | T5J1N2 |
| 11 | Quebec City QC | G1K3H2 |
| 12 | Hamilton ON | L8N1H2 |
| 13 | London ON | N6A3N7 |
| 14 | Victoria BC | V8W1P2 |
| 15 | Fredericton NB | E3B1B3 |
| 16 | Charlottetown PE | C1A1A1 |
| 17 | St. John's NL | A1C1A1 |
| 18 | Whitehorse YT | Y1A1A1 |
| 19 | Yellowknife NT | X1A2L3 |
| 20 | Iqaluit NU | X0A0H0 |
| 21 | Mississauga ON | L5B1N2 |
| 22 | Brampton ON | L6Y1H4 |
| 23 | Surrey BC | V3W1E2 |
| 24 | Laval QC | H7G1G1 |
| 25 | Gatineau QC | J8X1C1 |
| 26 | Burnaby BC | V5H1N1 |
| 27 | Kitchener ON | N2G1B5 |
| 28 | Windsor ON | N9A1J1 |
| 29 | Sherbrooke QC | J1H1H1 |
| 30 | Thunder Bay ON | P7A5K3 |

**Method:** 
1. Call OpenNorth API
2. Extract representative names
3. Web search "[Name] [riding/district] current representative"
4. Verify name is still current (not outdated)

---

## Reporting Format

Create a file `STRESS_TEST_RESULTS.md` with:

```markdown
# Stress Test Results — [Instance Name]
**Date:** 2026-03-06
**Instance:** Pam (Instance 3) / Kevin (Instance 2)

## Summary
- Total Tests: 100
- Passed: X
- Failed: X
- Warnings: X

## Detailed Results

### 1. French Translations (25 tests)
| # | Element | EN | FR | Status |
|---|---------|----|----|--------|
| 1 | Tagline | "No accounts..." | "Pas de comptes..." | ✅/❌ |

### 2. Navigation Flow (15 tests)
[Results]

### 3. Category Routing (30 tests)
[Results with web search verification links]

### 4. Representative Lookup (30 tests)
[Results with API response + web search verification]

## Issues Found
- [List any bugs, missing translations, incorrect routing, outdated reps]

## Recommendations
- [Any improvements needed]
```

---

## Execution Rules

1. **Do NOT start until both instances receive this prompt.**
2. Work independently — do not coordinate with the other instance.
3. Use web search to verify all representative names and government jurisdictions.
4. Log every test result — pass, fail, or warning.
5. Create your results file in your instance workspace.
6. Report completion when finished.

**Begin stress test now.**