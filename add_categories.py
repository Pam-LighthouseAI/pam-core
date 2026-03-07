import re

# Read the file
with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add opening lines for new categories
new_opening_lines = '''
  lgbtq: {
    urgent: "I'm reaching out because LGBTQ+ people in our community are facing real harm.",
    concerned: "I'm writing about an issue affecting LGBTQ+ people in our community.",
    hopeful: "I'm reaching out because I believe in a more inclusive community for everyone.",
    frustrated: "I'm writing because LGBTQ+ rights are being undermined and it needs to stop."
  },
  women: {
    urgent: "I'm writing because women's safety and rights are under threat right now.",
    concerned: "I'm writing about an issue affecting women in our community.",
    hopeful: "I'm reaching out because I believe in equality and opportunity for all.",
    frustrated: "I'm writing because gender inequality persists and needs to be addressed."
  },
  mentalhealth: {
    urgent: "I'm reaching out because mental health support is urgently needed.",
    concerned: "I'm writing about mental health services in our community.",
    hopeful: "I'm reaching out because I believe better mental health care is possible.",
    frustrated: "I'm writing because the mental health system is failing people who need help."
  },
  substance: {
    urgent: "I'm reaching out because the addiction crisis is costing lives.",
    concerned: "I'm writing about substance use and addiction services in our community.",
    hopeful: "I'm reaching out because I believe recovery is possible with the right support.",
    frustrated: "I'm writing because people with addiction are being ignored or criminalized."
  },
  transportation: {
    urgent: "I'm reaching out because transportation is essential and people are stranded.",
    concerned: "I'm writing about transportation issues affecting our community.",
    hopeful: "I'm reaching out because I believe better transit is achievable.",
    frustrated: "I'm writing because our transportation system isn't working for people."
  },
  digital: {
    urgent: "I'm reaching out because digital privacy and rights are under threat.",
    concerned: "I'm writing about digital rights and online privacy.",
    hopeful: "I'm reaching out because I believe we can build a fairer digital world.",
    frustrated: "I'm writing because tech companies have too much power over our lives."
  },
  animals: {
    urgent: "I'm reaching out because animals are suffering and need protection now.",
    concerned: "I'm writing about animal welfare in our community.",
    hopeful: "I'm reaching out because I believe we can treat animals humanely.",
    frustrated: "I'm writing because animal cruelty is being ignored."
  },
  sports: {
    urgent: "I'm reaching out because sports and recreation access is essential.",
    concerned: "I'm writing about sports and recreation in our community.",
    hopeful: "I'm reaching out because I believe everyone deserves access to sports.",
    frustrated: "I'm writing because recreation programs are being cut or ignored."
  },
  religion: {
    urgent: "I'm reaching out because religious freedom is under threat.",
    concerned: "I'm writing about religious accommodation in our community.",
    hopeful: "I'm reaching out because I believe in respect for all faiths.",
    frustrated: "I'm writing because religious communities are facing discrimination."
  },
  volunteer: {
    urgent: "I'm reaching out because community organizations need support now.",
    concerned: "I'm writing about volunteer and community programs.",
    hopeful: "I'm reaching out because I believe in the power of community.",
    frustrated: "I'm writing because volunteer organizations are being stretched too thin."
  },
  legalaid: {
    urgent: "I'm reaching out because access to justice shouldn't depend on income.",
    concerned: "I'm writing about legal aid and access to justice.",
    hopeful: "I'm reaching out because I believe everyone deserves fair representation.",
    frustrated: "I'm writing because the justice system is failing people who can't afford lawyers."
  },
  pensions: {
    urgent: "I'm reaching out because retirement security is at risk.",
    concerned: "I'm writing about pensions and retirement security.",
    hopeful: "I'm reaching out because I believe everyone deserves a secure retirement.",
    frustrated: "I'm writing because pension problems are being ignored."
  },
  childcare: {
    urgent: "I'm reaching out because families can't find or afford childcare.",
    concerned: "I'm writing about childcare access in our community.",
    hopeful: "I'm reaching out because I believe affordable childcare is achievable.",
    frustrated: "I'm writing because the childcare system is failing families."
  },
  food: {
    urgent: "I'm reaching out because people in our community are going hungry.",
    concerned: "I'm writing about food security in our community.",
    hopeful: "I'm reaching out because I believe no one should go hungry.",
    frustrated: "I'm writing because food insecurity is being ignored."
  },
  emergency: {
    urgent: "I'm reaching out because emergency services are critical and need attention.",
    concerned: "I'm writing about emergency services in our community.",
    hopeful: "I'm reaching out because I believe we can be better prepared.",
    frustrated: "I'm writing because emergency response isn't meeting our needs."
  },
  humanrights: {
    urgent: "I'm reaching out because human rights violations need immediate attention.",
    concerned: "I'm writing about a human rights concern.",
    hopeful: "I'm reaching out because I believe in dignity and equality for all.",
    frustrated: "I'm writing because rights are being violated and nothing is changing."
  }
};'''

# Find the end of the opening lines (after arts in frustrated)
pattern = r'(arts: "I\'m reaching out because arts and culture enrich all our lives\."\s*\}\s*\};)'
replacement = r'arts: "I\'m reaching out because arts and culture enrich all our lives."\n  },' + new_opening_lines

content = re.sub(pattern, replacement, content)

# 2. Add templates for new categories
new_templates = ''',
  lgbtq: {
    subject: "LGBTQ+ Rights Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  women: {
    subject: "Women's Rights Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  mentalhealth: {
    subject: "Mental Health Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  substance: {
    subject: "Substance Use & Addiction Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  transportation: {
    subject: "Transportation Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  digital: {
    subject: "Digital Rights Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  animals: {
    subject: "Animal Welfare Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  sports: {
    subject: "Sports & Recreation Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  religion: {
    subject: "Religion & Faith Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  volunteer: {
    subject: "Volunteer & Community Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  legalaid: {
    subject: "Legal Aid Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  pensions: {
    subject: "Pensions & Retirement Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  childcare: {
    subject: "Childcare Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  food: {
    subject: "Food Security Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  emergency: {
    subject: "Emergency Services Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  humanrights: {
    subject: "Human Rights Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  }
};'''

# Find the end of templates (after arts template closes with })
pattern = r'(arts: \{\s*subject: "Arts & Culture Concern: \{\{ISSUE\}\}",\s*body: `Dear \{\{REP_NAME\}\},\s*\{\{OPENING\}\}\s*\{\{STORY\}\}\s*\{\{CONTEXT\}\}\s*\{\{CLOSING\}\}\s*\{\{SIGNATURE\}\}`\s*\}\s*\};)'
replacement = r'''arts: {
    subject: "Arts & Culture Concern: {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  }''' + new_templates

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 3. Add jurisdiction headers for new categories
new_jurisdiction = ''',
  lgbtq: {
    federal: { title: "Federal LGBTQ+ Rights", contact: "MP", items: ["Criminal Code protections", "Canadian Human Rights Act", "Conversion therapy ban", "Federal workplace protections", "Immigration for same-sex partners"] },
    provincial: { title: "Provincial LGBTQ+ Rights", contact: "MPP/MLA", items: ["Provincial human rights codes", "Healthcare coverage", "Provincial education policies", "Provincial workplace protections", "Name/gender changes"] },
    municipal: { title: "Local LGBTQ+ Support", contact: "Councillor", items: ["Pride events", "Community programs", "Municipal inclusivity policies", "Local anti-discrimination"] }
  },
  women: {
    federal: { title: "Federal Women's Programs", contact: "MP", items: ["Women and Gender Equality Canada", "Pay Equity Act", "Maternity/parental benefits", "Federal gender-based violence funding", "National inquiry follow-up"] },
    provincial: { title: "Provincial Women's Services", contact: "MPP/MLA", items: ["Provincial women's offices", "Shelter funding", "Provincial pay equity", "Reproductive healthcare", "Women's crisis lines"] },
    municipal: { title: "Local Women's Support", contact: "Councillor", items: ["Women's shelters", "Local crisis services", "Municipal women's programs", "Community safety initiatives"] }
  },
  mentalhealth: {
    federal: { title: "Federal Mental Health", contact: "MP", items: ["Mental health funding", "National mental health standards", "988 crisis line", "Federal workplace mental health", "Research funding"] },
    provincial: { title: "Provincial Mental Health", contact: "MPP/MLA", items: ["Provincial mental health plans", "Hospital psychiatric services", "Community mental health", "Provincial crisis lines", "Addiction services"] },
    municipal: { title: "Local Mental Health", contact: "Councillor", items: ["Community programs", "Local crisis response", "Public health mental health", "Community centre programs"] }
  },
  substance: {
    federal: { title: "Federal Substance Policy", contact: "MP", items: ["Controlled Drugs Act", "Safe supply programs", "Federal addiction funding", "Opioid response", "Health Canada oversight"] },
    provincial: { title: "Provincial Addiction Services", contact: "MPP/MLA", items: ["Treatment centers", "Harm reduction programs", "Provincial opioid response", "Recovery housing", "Naloxone distribution"] },
    municipal: { title: "Local Addiction Support", contact: "Councillor", items: ["Supervised consumption sites", "Local harm reduction", "Community programs", "Outreach services"] }
  },
  transportation: {
    federal: { title: "Federal Transportation", contact: "MP", items: ["National transportation policy", "Rural transit funding", "Accessibility standards", "Air passenger rights", "Rail safety"] },
    provincial: { title: "Provincial Transportation", contact: "MPP/MLA", items: ["Provincial highways", "Provincial transit funding", "Driver licensing", "Provincial road maintenance", "Paratransit standards"] },
    municipal: { title: "Local Transportation", contact: "Councillor", items: ["Local transit", "Active transportation", "Parking", "Local roads", "Accessibility"] }
  },
  digital: {
    federal: { title: "Federal Digital Rights", contact: "MP", items: ["PIPEDA privacy law", "CRTC telecom regulation", "Online Harms Act", "Digital ID standards", "Cybersecurity"] },
    provincial: { title: "Provincial Digital", contact: "MPP/MLA", items: ["Provincial privacy laws", "Provincial digital ID", "Provincial consumer protection", "Provincial cybersecurity"] },
    municipal: { title: "Local Digital Services", contact: "Councillor", items: ["Municipal digital services", "Local broadband", "Municipal data privacy", "Community Wi-Fi"] }
  },
  animals: {
    federal: { title: "Federal Animal Protection", contact: "MP", items: ["Criminal Code cruelty", "Species at Risk Act", "Health Canada pet food", "CFIA animal health", "Import/export rules"] },
    provincial: { title: "Provincial Animal Welfare", contact: "MPP/MLA", items: ["Provincial SPCAs", "Provincial animal welfare acts", "Wildlife protection", "Farm animal standards", "Exotic animal rules"] },
    municipal: { title: "Local Animal Services", contact: "Councillor", items: ["Animal control", "Pet licensing", "Local shelters", "Bylaw enforcement", "Dog parks"] }
  },
  sports: {
    federal: { title: "Federal Sport", contact: "MP", items: ["Sport Canada", "Athlete assistance", "Safe Sport", "National sport organizations", "Anti-doping"] },
    provincial: { title: "Provincial Sport", contact: "MPP/MLA", items: ["Provincial sport organizations", "Provincial funding", "Provincial games", "School sports policy"] },
    municipal: { title: "Local Recreation", contact: "Councillor", items: ["Arenas and pools", "Community centres", "Local programs", "Sports fields", "Youth athletics"] }
  },
  religion: {
    federal: { title: "Federal Religious Rights", contact: "MP", items: ["Charter of Rights", "Canadian Human Rights Act", "Official Languages", "Multiculturalism", "Interfaith initiatives"] },
    provincial: { title: "Provincial Religious Affairs", contact: "MPP/MLA", items: ["Provincial human rights", "Faith-based schools", "Religious accommodations", "Provincial multiculturalism"] },
    municipal: { title: "Local Interfaith", contact: "Councillor", items: ["Places of worship zoning", "Interfaith events", "Community partnerships", "Local multiculturalism"] }
  },
  volunteer: {
    federal: { title: "Federal Volunteer Programs", contact: "MP", items: ["Canada Service Corps", "Charitable status", "National volunteer initiatives", "Federal funding programs"] },
    provincial: { title: "Provincial Community", contact: "MPP/MLA", items: ["Provincial volunteer programs", "Nonprofit support", "Provincial grants", "Community services"] },
    municipal: { title: "Local Volunteer", contact: "Councillor", items: ["Volunteer centres", "Community grants", "Local programs", "Civic engagement"] }
  },
  legalaid: {
    federal: { title: "Federal Justice", contact: "MP", items: ["Federal courts", "Criminal Code", "Access to justice funding", "Supreme Court", "Federal legal aid (limited)"] },
    provincial: { title: "Provincial Legal Aid", contact: "MPP/MLA", items: ["Legal aid plans", "Provincial courts", "Duty counsel", "Community clinics", "Family law aid"] },
    municipal: { title: "Local Justice Support", contact: "Councillor", items: ["Community legal clinics", "Local justice programs", "Municipal bylaw courts", "Community mediation"] }
  },
  pensions: {
    federal: { title: "Federal Pensions", contact: "MP", items: ["Canada Pension Plan", "Old Age Security", "Guaranteed Income Supplement", "Federal pension standards", "RRSP rules"] },
    provincial: { title: "Provincial Pensions", contact: "MPP/MLA", items: ["Provincial pension plans", "Provincial pension standards", "Locked-in accounts", "Provincial supplements"] },
    municipal: { title: "Local Senior Support", contact: "Councillor", items: ["Senior programs", "Property tax deferral", "Local pension info", "Community services"] }
  },
  childcare: {
    federal: { title: "Federal Childcare", contact: "MP", items: ["Canada-wide early learning", "Federal funding", "Indigenous childcare", "National standards"] },
    provincial: { title: "Provincial Childcare", contact: "MPP/MLA", items: ["Provincial childcare systems", "Licensing", "Subsidies", "Fee caps", "Worker wages"] },
    municipal: { title: "Local Childcare", contact: "Councillor", items: ["Municipal programs", "Before/after school", "Local centres", "Community spaces"] }
  },
  food: {
    federal: { title: "Federal Food Security", contact: "MP", items: ["Nutrition North Canada", "Food safety", "Agriculture policy", "Food price monitoring", "Northern subsidies"] },
    provincial: { title: "Provincial Food", contact: "MPP/MLA", items: ["Provincial food security", "School nutrition", "Provincial food banks", "Food safety inspection"] },
    municipal: { title: "Local Food", contact: "Councillor", items: ["Food banks", "Community gardens", "School programs", "Local food policy"] }
  },
  emergency: {
    federal: { title: "Federal Emergency", contact: "MP", items: ["Public Safety Canada", "National alerts", "Disaster assistance", "Search and rescue", "Coast Guard"] },
    provincial: { title: "Provincial Emergency", contact: "MPP/MLA", items: ["Provincial EMO", "911 systems", "Provincial disaster response", "Search and rescue", "Emergency plans"] },
    municipal: { title: "Local Emergency", contact: "Councillor", items: ["Fire services", "Paramedics", "Local emergency plans", "Emergency shelters", "Local alerts"] }
  },
  humanrights: {
    federal: { title: "Federal Human Rights", contact: "MP", items: ["Canadian Human Rights Commission", "Charter of Rights", "Criminal Code hate provisions", "Official Languages", "International treaties"] },
    provincial: { title: "Provincial Human Rights", contact: "MPP/MLA", items: ["Provincial human rights codes", "Provincial tribunals", "Provincial accessibility laws", "Provincial anti-racism"] },
    municipal: { title: "Local Human Rights", contact: "Councillor", items: ["Municipal inclusivity", "Local human rights", "Community programs", "Anti-discrimination policies"] }
  }
};'''

# Find the end of jurisdiction headers (after arts closes with })
pattern = r'(arts: \{\s*federal:.*?municipal:.*?\}\s*\}\s*\};)'
match = re.search(pattern, content, re.DOTALL)
if match:
    replacement = match.group(0).rstrip('};') + new_jurisdiction
    content = content[:match.start()] + replacement + content[match.end():]

# Write the file
with open(r'D:\source_extracted\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Categories added successfully!")