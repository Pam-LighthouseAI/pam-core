with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where templates are defined and accessed
import re

# Look for template object definitions
template_match = re.search(r'const templates = \{[\s\S]*?\n\};', content)
if template_match:
    print("Found templates object:")
    print(template_match.group(0)[:500])
    print("...")

# Find generateLetter function
gen_match = re.search(r'const generateLetter[\s\S]*?\n\}', content)
if gen_match:
    print("\n\nFound generateLetter function:")
    print(gen_match.group(0)[:1000])