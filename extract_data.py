#!/usr/bin/env python3
"""
Extract data from my_civic_voice.html and create separate JS files for Vite build.
"""

import re
import os

# Read the original file
with open(r"D:\source_extracted\my_civic_voice.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Create output directory
output_dir = r"C:\nanobot\instance3\workspace\src\data"
os.makedirs(output_dir, exist_ok=True)

# Extract ISSUES array
issues_match = re.search(r'const ISSUES = \[([\s\S]*?)\];', content)
if issues_match:
    issues_content = issues_match.group(0)
    # Write to file
    with open(os.path.join(output_dir, 'issues.js'), 'w', encoding='utf-8') as f:
        f.write("// Issues data for My Civic Voice\n")
        f.write("// This file is auto-generated\n\n")
        f.write(issues_content)
        f.write("\n\nexport default ISSUES;\n")
    print("Created issues.js")

# Extract FAQ_EN and FAQ_FR
faq_en_match = re.search(r'const FAQ_EN = \[([\s\S]*?)\];', content)
if faq_en_match:
    faq_en_content = faq_en_match.group(0)
    faq_fr_match = re.search(r'const FAQ_FR = \[([\s\S]*?)\];', content)
    faq_fr_content = faq_fr_match.group(0) if faq_fr_match else ""
    
    with open(os.path.join(output_dir, 'faq.js'), 'w', encoding='utf-8') as f:
        f.write("// FAQ data for My Civic Voice\n\n")
        f.write(faq_en_content)
        f.write("\n\n")
        f.write(faq_fr_content)
        f.write("\n\nexport { FAQ_EN, FAQ_FR };\n")
    print("Created faq.js")

# Extract JURISDICTION_HEADERS
jh_match = re.search(r'const JURISDICTION_HEADERS = \{([\s\S]*?)\};\s*\n\s*// JURISDICTION HEADERS - FRENCH', content)
if jh_match:
    jh_content = jh_match.group(0)
    jh_fr_match = re.search(r'const JURISDICTION_HEADERS_FR = \{([\s\S]*?)\};\s*\n\s*\n\s*// STORY PROMPTS', content)
    jh_fr_content = jh_fr_match.group(0) if jh_fr_match else ""
    
    with open(os.path.join(output_dir, 'jurisdiction.js'), 'w', encoding='utf-8') as f:
        f.write("// Jurisdiction headers for My Civic Voice\n\n")
        f.write(jh_content)
        f.write("\n\n")
        f.write(jh_fr_content)
        f.write("\n\nexport { JURISDICTION_HEADERS, JURISDICTION_HEADERS_FR };\n")
    print("Created jurisdiction.js")

# Extract STORY_PROMPTS
sp_match = re.search(r'const STORY_PROMPTS = \{([\s\S]*?)\};\s*\n\s*// STORY PROMPTS - FRENCH', content)
if sp_match:
    sp_content = sp_match.group(0)
    sp_fr_match = re.search(r'const STORY_PROMPTS_FR = \{([\s\S]*?)\};\s*\n\s*\n\s*// OPENING LINES', content)
    sp_fr_content = sp_fr_match.group(0) if sp_fr_match else ""
    
    with open(os.path.join(output_dir, 'storyPrompts.js'), 'w', encoding='utf-8') as f:
        f.write("// Story prompts for My Civic Voice\n\n")
        f.write(sp_content)
        f.write("\n\n")
        f.write(sp_fr_content)
        f.write("\n\nexport { STORY_PROMPTS, STORY_PROMPTS_FR };\n")
    print("Created storyPrompts.js")

# Extract OPENING_LINES
ol_match = re.search(r'const OPENING_LINES = \{([\s\S]*?)\};\s*\n\s*// OPENING LINES - FRENCH', content)
if ol_match:
    ol_content = ol_match.group(0)
    ol_fr_match = re.search(r'const OPENING_LINES_FR = \{([\s\S]*?)\};\s*\n\s*\n\s*// CLOSING LINES', content)
    ol_fr_content = ol_fr_match.group(0) if ol_fr_match else ""
    
    with open(os.path.join(output_dir, 'openingLines.js'), 'w', encoding='utf-8') as f:
        f.write("// Opening lines for My Civic Voice\n\n")
        f.write(ol_content)
        f.write("\n\n")
        f.write(ol_fr_content)
        f.write("\n\nexport { OPENING_LINES, OPENING_LINES_FR };\n")
    print("Created openingLines.js")

# Extract CLOSING_LINES
cl_match = re.search(r'const CLOSING_LINES = \{([\s\S]*?)\};\s*\n\s*// CLOSING LINES - FRENCH', content)
if cl_match:
    cl_content = cl_match.group(0)
    cl_fr_match = re.search(r'const CLOSING_LINES_FR = \{([\s\S]*?)\};\s*\n\s*\n\s*// OPENING LINES - FRENCH VERSIONS', content)
    cl_fr_content = cl_fr_match.group(0) if cl_fr_match else ""
    
    with open(os.path.join(output_dir, 'closingLines.js'), 'w', encoding='utf-8') as f:
        f.write("// Closing lines for My Civic Voice\n\n")
        f.write(cl_content)
        f.write("\n\n")
        f.write(cl_fr_content)
        f.write("\n\nexport { CLOSING_LINES, CLOSING_LINES_FR };\n")
    print("Created closingLines.js")

# Extract TEMPLATES
tpl_match = re.search(r'const TEMPLATES = \{([\s\S]*?)\};\s*\n\s*\n\s*// LANGUAGE TOGGLE', content)
if tpl_match:
    tpl_content = tpl_match.group(0)
    
    with open(os.path.join(output_dir, 'templates.js'), 'w', encoding='utf-8') as f:
        f.write("// Email templates for My Civic Voice\n\n")
        f.write(tpl_content)
        f.write("\n\nexport default TEMPLATES;\n")
    print("Created templates.js")

# Extract lookup data (MUNICIPAL_BACKUP_LINKS, PROVINCIAL_BACKUP_LINKS, CITY_PROVINCE, PROVINCE_REPS)
lookup_content = ""

municipal_match = re.search(r'const MUNICIPAL_BACKUP_LINKS = \{([\s\S]*?)\};', content)
if municipal_match:
    lookup_content += municipal_match.group(0) + "\n\n"

provincial_match = re.search(r'const PROVINCIAL_BACKUP_LINKS = \{([\s\S]*?)\};', content)
if provincial_match:
    lookup_content += provincial_match.group(0) + "\n\n"

city_match = re.search(r'const CITY_PROVINCE = \{([\s\S]*?)\};', content)
if city_match:
    lookup_content += city_match.group(0) + "\n\n"

province_reps_match = re.search(r'const PROVINCE_REPS = \{([\s\S]*?)\};', content)
if province_reps_match:
    lookup_content += province_reps_match.group(0) + "\n"

if lookup_content:
    with open(os.path.join(output_dir, 'lookup.js'), 'w', encoding='utf-8') as f:
        f.write("// Lookup data for My Civic Voice\n\n")
        f.write(lookup_content)
        f.write("\nexport { MUNICIPAL_BACKUP_LINKS, PROVINCIAL_BACKUP_LINKS, CITY_PROVINCE, PROVINCE_REPS };\n")
    print("Created lookup.js")

print("\nData extraction complete!")