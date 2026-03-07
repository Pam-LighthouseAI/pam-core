# WCAG 2.1 Accessibility Requirements for Canadian Government Websites
## Civic Engagement Tool Compliance Checklist

---

## Legal Requirements for Canadian Government Websites

### Federal Requirements

1. **Accessible Canada Act (ACA)** - Enacted July 2019
   - Requires Parliament, federal government, and federally regulated employers to eliminate barriers
   - Applies to: federal government departments, agencies, Crown corporations, and private sector organizations under federal jurisdiction (banking, telecommunications, transportation)

2. **Standard on Web Accessibility** (Treasury Board Secretariat)
   - **Current Standard**: WCAG 2.1 Level AA conformance required
   - Government of Canada departments must make websites and web applications compliant
   - Compliance scores are monitored and reported (target: 95%+ compliance)

3. **CAN/ASC-EN 301 549**
   - Canada has adopted this standard for ICT accessibility
   - Incorporates WCAG 2.1 Level AA as the benchmark for web accessibility
   - Aligns with European EN 301 549 standard

### Provincial Requirements (Key Provinces)

| Province | Legislation | Requirement |
|----------|-------------|-------------|
| Ontario | AODA (Accessibility for Ontarians with Disabilities Act) | WCAG 2.0 Level AA (excludes 1.2.4, 1.2.5) |
| British Columbia | AccessibleBC Act | WCAG 2.x Level AA + Reading Level (AAA) |
| Manitoba | Accessibility for Manitobans Act | WCAG 2.1 Level AA |
| Nova Scotia | Nova Scotia Accessibility Act | Information & Communication standards |
| Newfoundland & Labrador | Accessibility Act | Information & Communication included |

---

## Key Compliance Points for Civic Engagement Tools

Civic engagement tools require special attention to accessibility because they:
- Collect citizen input and feedback
- Enable democratic participation
- Must be usable by all citizens regardless of ability

---

## WCAG 2.1 Level AA Compliance Checklist

### 1. PERCEIVABLE

#### 1.1 Text Alternatives (Guideline 1.1)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **1.1.1 Non-text Content** | A | All non-text content has text alternatives | ☐ All images have meaningful alt text<br>☐ Decorative images use alt="" (empty alt)<br>☐ Icons have accessible names<br>☐ Charts/graphs have text descriptions or data tables<br>☐ Form buttons with images have accessible names<br>☐ CAPTCHAs have alternative access methods |

**Civic Engagement Tool Specifics:**
- ☐ Event photos have descriptive alt text
- ☐ Profile pictures of candidates/officials have alt text
- ☐ Maps have text alternatives describing locations
- ☐ Infographics about civic issues have text summaries
- ☐ Logo images have appropriate alt text (site name or empty if decorative)

---

#### 1.2 Time-based Media (Guideline 1.2)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **1.2.1 Audio-only/Video-only** | A | Alternative for prerecorded media | ☐ Audio content has transcripts<br>☐ Video content has audio descriptions or text alternatives |
| **1.2.2 Captions (Prerecorded)** | A | Captions for prerecorded video | ☐ All videos have accurate captions<br>☐ Captions include speaker identification when needed<br>☐ Captions synchronized with audio |
| **1.2.3 Audio Description** | A | Audio description for video | ☐ Videos have audio descriptions OR text alternatives<br>☐ Important visual content described |
| **1.2.4 Captions (Live)** | AA | Captions for live audio | ☐ Live streams have real-time captions |
| **1.2.5 Audio Description (Prerecorded)** | AA | Audio description provided | ☐ Extended audio descriptions when needed |

**Civic Engagement Tool Specifics:**
- ☐ Town hall recordings have captions and transcripts
- ☐ Public meeting videos are captioned
- ☐ Live stream events have real-time captioning
- ☐ Candidate debates/interviews have captions

---

#### 1.3 Adaptable (Guideline 1.3)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **1.3.1 Info and Relationships** | A | Structure conveyed programmatically | ☐ Headings use proper h1-h6 hierarchy<br>☐ Lists use ul/ol/dl elements<br>☐ Data tables use proper th/td markup<br>☐ Form labels are programmatically associated |
| **1.3.2 Meaningful Sequence** | A | Reading order makes sense | ☐ DOM order matches visual order<br>☐ Tab order follows logical sequence<br>☐ Screen reader reads content in correct order |
| **1.3.3 Sensory Characteristics** | A | Instructions don't rely solely on shape/position | ☐ No "click the round button"<br>☐ No "click the button on the right"<br>☐ Instructions include text alternatives |
| **1.3.4 Orientation** | AA | Works in portrait and landscape | ☐ Content reflows in both orientations<br>☐ No locked orientation unless essential |
| **1.3.5 Identify Input Purpose** | AA | Input purpose can be programmatically determined | ☐ Form fields use autocomplete attributes<br>☐ User-specific input purposes identified |
| **1.3.6 Identify Purpose** | AA | Purpose of UI components can be determined | ☐ Icons have programmatically determinable purpose<br>☐ ARIA landmarks used appropriately |

**Civic Engagement Tool Specifics:**
- ☐ Survey forms have proper heading structure
- ☐ Petition signing process has logical flow
- ☐ Comment submission forms have clear labels
- ☐ Poll questions use proper semantic markup

---

#### 1.4 Distinguishable (Guideline 1.4)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **1.4.1 Use of Color** | A | Color not sole means of conveying info | ☐ Error states not indicated by color alone<br>☐ Links distinguished by more than color<br>☐ Required fields not indicated by color alone |
| **1.4.2 Audio Control** | A | No audio plays automatically for >3 seconds | ☐ No auto-playing audio<br>☐ If audio plays, pause/stop control available<br>☐ Volume control available |
| **1.4.3 Contrast (Minimum)** | AA | Text contrast ratio ≥ 4.5:1 | ☐ Normal text: 4.5:1 minimum contrast<br>☐ Large text (18pt+ or 14pt bold): 3:1 minimum<br>☐ Test with contrast checker tool |
| **1.4.4 Resize Text** | AA | Text resizable to 200% without loss | ☐ Text scales properly at 200%<br>☐ No horizontal scrolling required<br>☐ No content overlap at 200% |
| **1.4.5 Images of Text** | AA | Real text used instead of images of text | ☐ Logos are only exception<br>☐ Navigation uses real text<br>☐ Headings use real text |
| **1.4.10 Reflow** | AA | Content reflows without horizontal scrolling | ☐ At 320px width, no horizontal scrolling<br>☐ At 256 CSS pixels wide at 400% zoom<br>☐ Vertical scrolling content reflows properly |
| **1.4.11 Non-text Contrast** | AA | UI components contrast ≥ 3:1 | ☐ Form field borders: 3:1 minimum<br>☐ Buttons have 3:1 contrast<br>☐ Icons have 3:1 contrast<br>☐ Focus indicators have 3:1 contrast |
| **1.4.12 Text Spacing** | AA | No loss of content with style overrides | ☐ Line height 1.5x font size works<br>☐ Paragraph spacing 2x font size works<br>☐ Letter spacing 0.12x font size works<br>☐ Word spacing 0.16x font size works |
| **1.4.13 Content on Hover or Focus** | AA | Dismissible, hoverable, persistent | ☐ Tooltips can be dismissed<br>☐ Tooltips don't disappear on hover<br>☐ Tooltips remain visible until dismissed |

**Color Contrast Requirements Summary:**
| Element Type | Minimum Ratio |
|--------------|---------------|
| Normal text (< 18pt or < 14pt bold) | 4.5:1 |
| Large text (≥ 18pt or ≥ 14pt bold) | 3:1 |
| UI components (buttons, form borders) | 3:1 |
| Graphical objects (icons, focus indicators) | 3:1 |

---

### 2. OPERABLE

#### 2.1 Keyboard Accessible (Guideline 2.1)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **2.1.1 Keyboard** | A | All functionality available via keyboard | ☐ All interactive elements focusable<br>☐ No keyboard traps<br>☐ Custom controls have keyboard support<br>☐ No scripting that blocks keyboard access |
| **2.1.2 No Keyboard Trap** | A | Focus can be moved away from all components | ☐ Modals can be closed with Escape<br>☐ Focus can tab out of all widgets<br>☐ No plugins that trap focus |
| **2.1.4 Character Key Shortcuts** | A | Single-key shortcuts can be turned off | ☐ No single-character shortcuts by default<br>☐ Shortcuts can be remapped or disabled<br>☐ Modifier keys used for shortcuts |

**Keyboard Navigation Best Practices:**
- ☐ Tab order follows logical reading order
- ☐ tabindex="0" for custom interactive elements
- ☐ tabindex="-1" for programmatic focus only
- ☐ Arrow keys for navigation within widgets
- ☐ Enter/Space for activating controls
- ☐ Escape for closing/canceling

**Civic Engagement Tool Specifics:**
- ☐ Petition signing can be completed with keyboard only
- ☐ Survey forms navigable via keyboard
- ☐ Comment input areas keyboard accessible
- ☐ Voting/polling interfaces keyboard accessible
- ☐ Date pickers for event registration keyboard accessible
- ☐ Dropdown menus keyboard accessible

---

#### 2.2 Enough Time (Guideline 2.2)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **2.2.1 Timing Adjustable** | A | Time limits can be turned off/adjusted | ☐ Session timeouts can be extended<br>☐ Warning before timeout<br>☐ At least 10x extension available |
| **2.2.2 Pause, Stop, Hide** | A | Moving content can be paused | ☐ Carousels have pause controls<br>☐ Auto-updating content can be paused<br>☐ Animations can be stopped |

**Civic Engagement Tool Specifics:**
- ☐ Form submission warnings before session timeout
- ☐ Long surveys allow saving progress
- ☐ Live feed/updates can be paused

---

#### 2.3 Seizures and Physical Reactions (Guideline 2.3)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **2.3.1 Three Flashes or Below Threshold** | A | No more than 3 flashes per second | ☐ No rapidly flashing content<br>☐ Animations tested for flash frequency |

---

#### 2.4 Navigable (Guideline 2.4)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **2.4.1 Bypass Blocks** | A | Skip to content link provided | ☐ "Skip to main content" link present<br>☐ Skip link visible on focus<br>☐ Skip link works correctly |
| **2.4.2 Page Titled** | A | Web pages have descriptive titles | ☐ Page titles describe content<br>☐ Page titles unique within site<br>☐ Titles follow consistent format |
| **2.4.3 Focus Order** | A | Focus order preserves meaning | ☐ Tab order logical<br>☐ Focus order matches visual order<br>☐ No unexpected focus jumps |
| **2.4.4 Link Purpose (In Context)** | A | Link purpose clear from context | ☐ Link text describes destination<br>☐ No "click here" links<br>☐ Links with same text go to same place |
| **2.4.5 Multiple Ways** | AA | Multiple ways to find pages | ☐ Search functionality available<br>☐ Navigation menu present<br>☐ Sitemap or similar available |
| **2.4.6 Headings and Labels** | AA | Headings and labels describe content | ☐ Headings are descriptive<br>☐ Form labels are clear<br>☐ Section headings used appropriately |
| **2.4.7 Focus Visible** | AA | Focus indicator visible | ☐ Focus indicator has 3:1 contrast<br>☐ Focus indicator clearly visible<br>☐ Custom focus styles implemented |

**Focus Visibility Checklist:**
- ☐ Visible focus ring on all interactive elements
- ☐ Focus indicator color contrasts with background
- ☐ Focus indicator doesn't rely on color alone
- ☐ Focus visible in both light and dark modes

---

#### 2.5 Input Modalities (Guideline 2.5)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **2.5.1 Pointer Gestures** | A | Multipoint gestures have single-pointer alternatives | ☐ Swipe gestures have button alternatives<br>☐ Pinch-zoom has +/- buttons<br>☐ No gesture-only interactions |
| **2.5.2 Pointer Cancellation** | A | Actions can be aborted | ☐ Actions trigger on up-event<br>☐ Abort mechanism available<br>☐ No accidental submissions |
| **2.5.3 Label in Name** | AA | Visible label matches accessible name | ☐ Button visible text in accessible name<br>☐ No mismatch between visible and accessible name<br>☐ aria-label includes visible label text |
| **2.5.4 Motion Actuation** | A | Motion-triggered input has alternatives | ☐ Shake-to-undo has button alternative<br>☐ Motion controls can be disabled<br>☐ No motion-only inputs |

---

### 3. UNDERSTANDABLE

#### 3.1 Readable (Guideline 3.1)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **3.1.1 Language of Page** | A | Page language declared | ☐ `<html lang="en">` (or appropriate language)<br>☐ Language attribute correct |
| **3.1.2 Language of Parts** | AA | Language of content changes declared | ☐ Foreign language phrases marked up<br>☐ `<span lang="fr">` used appropriately |

---

#### 3.2 Predictable (Guideline 3.2)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **3.2.1 On Focus** | A | No unexpected context changes | ☐ Focus doesn't trigger new window<br>☐ Focus doesn't submit forms<br>☐ Focus doesn't change content unexpectedly |
| **3.2.2 On Input** | A | Context changes predictable | ☐ Form changes don't auto-submit<br>☐ No unexpected redirects<br>☐ Changes announced before happening |
| **3.2.3 Consistent Navigation** | AA | Navigation consistent across pages | ☐ Same navigation order on all pages<br>☐ Same labels for same functions<br>☐ Consistent layout across site |
| **3.2.4 Consistent Identification** | AA | Components identified consistently | ☐ Same icons mean same things<br>☐ Same controls have same labels<br>☐ Consistent naming throughout |

---

#### 3.3 Input Assistance (Guideline 3.3)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **3.3.1 Error Identification** | A | Input errors described in text | ☐ Error messages in text (not just color)<br>☐ Error messages identify the field<br>☐ Error messages describe the problem |
| **3.3.2 Labels or Instructions** | A | Labels and instructions provided | ☐ All form fields have labels<br>☐ Required fields indicated<br>☐ Input format specified<br>☐ Instructions provided where needed |
| **3.3.3 Error Suggestion** | AA | Suggestions for fixing errors | ☐ Form errors include suggestions<br>☐ Invalid format shows correct format<br>☐ Suggestions are helpful and specific |
| **3.3.4 Error Prevention (Legal, Financial)** | AA | Submissions reversible/confirmed/checked | ☐ Important submissions can be reviewed<br>☐ Confirmation before final submission<br>☐ Ability to undo submissions |

**Form Accessibility Checklist:**
- ☐ All form fields have programmatically associated labels
- ☐ Required fields marked with text (not just asterisk)
- ☐ Error messages linked to fields via aria-describedby
- ☐ aria-invalid="true" on fields with errors
- ☐ Error messages appear adjacent to fields
- ☐ Success messages announced to screen readers
- ☐ Forms can be submitted via keyboard

**Civic Engagement Tool Specifics:**
- ☐ Petition sign-up form has clear labels and error handling
- ☐ Comment submission form validates input accessibly
- ☐ Survey questions have clear instructions
- ☐ Email/phone validation errors provide suggestions
- ☐ Address forms have proper autocomplete attributes

---

### 4. ROBUST

#### 4.1 Compatible (Guideline 4.1)

| Criterion | Level | Requirement | Checklist |
|-----------|-------|-------------|-----------|
| **4.1.2 Name, Role, Value** | A | UI components have accessible names/roles | ☐ Custom widgets have appropriate ARIA roles<br>☐ All interactive elements have accessible names<br>☐ State changes announced (aria-expanded, etc.)<br>☐ Value changes announced for range controls |
| **4.1.3 Status Messages** | AA | Status messages announced | ☐ Success messages use role="status"<br>☐ Error messages use role="alert"<br>☐ Loading states announced<br>☐ Live regions used appropriately |

**Screen Reader Compatibility Checklist:**
- ☐ All interactive elements have accessible names
- ☐ Buttons have descriptive text (not "Click here")
- ☐ Links have descriptive text (not "Read more")
- ☐ Form fields have labels
- ☐ Images have appropriate alt text
- ☐ Headings create logical outline
- ☐ Landmarks used (main, nav, aside)
- ☐ Tables have proper headers
- ☐ ARIA used appropriately (not overused)
- ☐ Live regions announce dynamic content

---

## Screen Reader Testing Checklist

### Required Testing with Screen Readers

| Screen Reader | Browser | Platform | Test Areas |
|---------------|---------|----------|------------|
| NVDA | Firefox/Chrome | Windows | Full navigation |
| JAWS | Chrome/Edge | Windows | Full navigation |
| VoiceOver | Safari | macOS/iOS | Full navigation |
| TalkBack | Chrome | Android | Mobile testing |

### Screen Reader Testing Points

- ☐ Page title announced correctly
- ☐ Landmarks announced (navigation, main, etc.)
- ☐ Heading structure navigable via heading shortcuts
- ☐ All form fields announced with labels
- ☐ Error messages announced when they appear
- ☐ Buttons and links announced with their names
- ☐ Tables navigable by row/column
- ☐ Dynamic content changes announced
- ☐ Focus moves logically through page
- ☐ No confusing announcements

---

## Keyboard Navigation Testing Checklist

### Required Keyboard Tests

| Key | Expected Behavior |
|-----|-------------------|
| Tab | Move forward through interactive elements |
| Shift + Tab | Move backward through interactive elements |
| Enter | Activate links and buttons |
| Space | Activate buttons, toggle checkboxes |
| Arrow keys | Navigate within widgets (menus, tabs, etc.) |
| Escape | Close modals, menus, dropdowns |
| Home | Jump to beginning of content |
| End | Jump to end of content |

### Keyboard Testing Checklist

- ☐ All interactive elements reachable by Tab
- ☐ Tab order logical and predictable
- ☐ Focus visible on all elements
- ☐ No keyboard traps
- ☐ Modal dialogs trap focus appropriately
- ☐ Modals return focus on close
- ☐ Dropdown menus keyboard accessible
- ☐ Custom widgets keyboard accessible
- ☐ Skip links work correctly
- ☐ No keyboard shortcuts conflicting with AT

---

## Color Contrast Testing Checklist

### Required Contrast Tests

| Element | Requirement | Tool |
|---------|-------------|------|
| Normal text | 4.5:1 minimum | Contrast checker |
| Large text | 3:1 minimum | Contrast checker |
| UI components | 3:1 minimum | Contrast checker |
| Focus indicators | 3:1 minimum | Contrast checker |

### Testing Tools

- WebAIM Contrast Checker
- Chrome DevTools Accessibility Audit
- WAVE Accessibility Tool
- axe DevTools Browser Extension
- Colour Contrast Analyser (CCA)

### Contrast Testing Checklist

- ☐ All text meets minimum contrast
- ☐ Text over images has sufficient contrast
- ☐ Placeholder text meets contrast requirements
- ☐ Disabled states still readable
- ☐ Focus indicators visible
- ☐ Error states not indicated by color alone
- ☐ Links distinguished from surrounding text
- ☐ Charts and graphs have accessible colors
- ☐ Dark mode maintains contrast
- ☐ High contrast mode compatible

---

## Alt Text Requirements Checklist

### When Alt Text is Required

| Image Type | Alt Text Requirement |
|------------|---------------------|
| Informative images | Descriptive text conveying same information |
| Functional images (buttons, links) | Describe the function/destination |
| Complex images (charts, diagrams) | Brief description + long description |
| Images of text | Text in the image |
| Logos | Organization name or empty if decorative |
| Decorative images | Empty alt="" (null alt) |

### Alt Text Best Practices

- ☐ Alt text describes the image content/purpose
- ☐ Alt text doesn't include "image of" or "picture of"
- ☐ Alt text is concise (usually under 125 characters)
- ☐ Alt text doesn't repeat adjacent text
- ☐ Decorative images have empty alt=""
- ☐ Complex images have extended descriptions
- ☐ Linked images describe the link destination
- ☐ Form button images describe the action

### Civic Engagement Tool Alt Text Examples

| Image | Good Alt Text | Bad Alt Text |
|-------|---------------|--------------|
| Candidate photo | "Jane Smith, candidate for City Council" | "Photo of Jane" |
| Event flyer | "Community Town Hall, March 15, 7pm, City Hall" | "Flyer" |
| Chart showing survey results | "Bar chart: 65% support, 25% oppose, 10% undecided" | "Chart" |
| Submit button with checkmark | "Submit" | "Checkmark" |
| Decorative separator | "" (empty) | "Decorative line" |

---

## Civic Engagement Tool Specific Requirements

### Forms and Input

- ☐ Petition forms have clear labels and error handling
- ☐ Comment fields have proper labels and instructions
- ☐ Survey questions have accessible markup
- ☐ File upload fields have accessible alternatives
- ☐ CAPTCHA has accessible alternative (audio or alternative method)
- ☐ Email/phone validation provides helpful error messages
- ☐ Address forms use autocomplete attributes
- ☐ Date inputs have accessible date pickers

### Interactive Elements

- ☐ Voting/polling interfaces are keyboard accessible
- ☐ Progress indicators announced to screen readers
- ☐ Dynamic content updates announced
- ☐ Drag-and-drop has keyboard alternative
- ☐ Auto-complete suggestions keyboard accessible
- ☐ Infinite scroll has alternative navigation
- ☐ Sorting/filtering accessible via keyboard

### Multimedia

- ☐ Town hall recordings have captions
- ☐ Live streams have real-time captioning
- ☐ Audio content has transcripts
- ☐ Video content has audio descriptions
- ☐ Media players are keyboard accessible

### Documents

- ☐ PDF documents are accessible
- ☐ Downloadable forms are accessible
- ☐ Alternative formats available upon request

---

## Testing Methodology

### Automated Testing Tools

1. **axe DevTools** - Browser extension for automated testing
2. **WAVE** - Web Accessibility Evaluation Tool
3. **Lighthouse** - Chrome DevTools accessibility audit
4. **Siteimprove** - Enterprise accessibility testing
5. **SortSite** - Website accessibility checker

### Manual Testing Requirements

1. **Keyboard Testing** - Navigate entire site without mouse
2. **Screen Reader Testing** - Test with NVDA, JAWS, VoiceOver
3. **Color Contrast Testing** - Verify all text/UI contrast ratios
4. **Zoom Testing** - Test at 200% and 400% zoom
5. **Mobile Testing** - Test on mobile devices with accessibility features

### Testing Checklist

- ☐ Automated scan passed with no critical errors
- ☐ Keyboard-only navigation completed successfully
- ☐ Screen reader testing completed (NVDA + VoiceOver minimum)
- ☐ Color contrast verified for all text and UI elements
- ☐ 200% zoom tested without loss of functionality
- ☐ Mobile accessibility tested
- ☐ Forms tested for error handling and submission
- ☐ All pages tested

---

## Compliance Reporting

### Required Documentation

- ☐ Accessibility statement published
- ☐ Feedback mechanism available
- ☐ Response timeline for accessibility issues (usually 2 business days)
- ☐ Alternative format request process documented
- ☐ Known accessibility issues documented
- ☐ Remediation timeline for known issues

### Ongoing Monitoring

- ☐ Regular automated scans scheduled
- ☐ Manual testing schedule established
- ☐ User feedback collection process
- ☐ Issue tracking and resolution process
- ☐ Staff training on accessibility

---

## Quick Reference: WCAG 2.1 Level AA Success Criteria

| # | Criterion | Level | Key Requirement |
|---|-----------|-------|-----------------|
| 1.1.1 | Non-text Content | A | Alt text for images |
| 1.2.1 | Audio-only/Video-only | A | Transcripts for media |
| 1.2.2 | Captions (Prerecorded) | A | Captions for videos |
| 1.2.3 | Audio Description | A | Audio descriptions |
| 1.2.4 | Captions (Live) | AA | Live captions |
| 1.2.5 | Audio Description | AA | Extended descriptions |
| 1.3.1 | Info and Relationships | A | Semantic structure |
| 1.3.2 | Meaningful Sequence | A | Logical reading order |
| 1.3.3 | Sensory Characteristics | A | Not shape/position only |
| 1.3.4 | Orientation | AA | Works portrait/landscape |
| 1.3.5 | Identify Input Purpose | AA | Autocomplete attributes |
| 1.3.6 | Identify Purpose | AA | UI purpose programmable |
| 1.4.1 | Use of Color | A | Not color-only |
| 1.4.2 | Audio Control | A | No auto-play audio |
| 1.4.3 | Contrast (Minimum) | AA | 4.5:1 text contrast |
| 1.4.4 | Resize Text | AA | 200% resizable |
| 1.4.5 | Images of Text | AA | Use real text |
| 1.4.10 | Reflow | AA | No horizontal scroll |
| 1.4.11 | Non-text Contrast | AA | 3:1 UI contrast |
| 1.4.12 | Text Spacing | AA | Style override works |
| 1.4.13 | Content on Hover/Focus | AA | Hoverable content |
| 2.1.1 | Keyboard | A | Full keyboard access |
| 2.1.2 | No Keyboard Trap | A | No focus traps |
| 2.1.4 | Character Key Shortcuts | A | Can turn off shortcuts |
| 2.2.1 | Timing Adjustable | A | Time limits adjustable |
| 2.2.2 | Pause, Stop, Hide | A | Pause moving content |
| 2.3.1 | Three Flashes | A | No rapid flashing |
| 2.4.1 | Bypass Blocks | A | Skip links |
| 2.4.2 | Page Titled | A | Descriptive titles |
| 2.4.3 | Focus Order | A | Logical tab order |
| 2.4.4 | Link Purpose | A | Clear link text |
| 2.4.5 | Multiple Ways | AA | Multiple navigation |
| 2.4.6 | Headings and Labels | AA | Descriptive headings |
| 2.4.7 | Focus Visible | AA | Visible focus |
| 2.5.1 | Pointer Gestures | A | Alternatives for gestures |
| 2.5.2 | Pointer Cancellation | A | Abort actions |
| 2.5.3 | Label in Name | AA | Visible = accessible name |
| 2.5.4 | Motion Actuation | A | Alternatives for motion |
| 3.1.1 | Language of Page | A | lang attribute |
| 3.1.2 | Language of Parts | AA | lang for foreign text |
| 3.2.1 | On Focus | A | No focus changes |
| 3.2.2 | On Input | A | Predictable input |
| 3.2.3 | Consistent Navigation | AA | Same navigation |
| 3.2.4 | Consistent Identification | AA | Same labels |
| 3.3.1 | Error Identification | A | Text error messages |
| 3.3.2 | Labels or Instructions | A | Form labels |
| 3.3.3 | Error Suggestion | AA | Error suggestions |
| 3.3.4 | Error Prevention | AA | Confirm submissions |
| 4.1.2 | Name, Role, Value | A | Accessible widgets |
| 4.1.3 | Status Messages | AA | Announce status |

---

## Resources

- [WCAG 2.1 Guidelines (W3C)](https://www.w3.org/TR/WCAG21/)
- [Understanding WCAG 2.1 (W3C)](https://www.w3.org/WAI/WCAG21/Understanding/)
- [WCAG Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM WCAG 2 Checklist](https://webaim.org/standards/wcag/checklist)
- [Accessible Canada Act](https://www.parl.ca/DocumentViewer/en/42-1/bill/C-81/royal-assent)
- [Standard on Web Accessibility (Canada)](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=23601)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WAVE Accessibility Tool](https://wave.webaim.org/)
- [axe DevTools](https://www.deque.com/axe/)

---

*Document created: March 2026*
*Based on WCAG 2.1 Level AA requirements*
*For Canadian government civic engagement tool compliance*