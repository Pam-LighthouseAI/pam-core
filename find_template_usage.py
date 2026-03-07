import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the generateLetter function or where templates are used
# Look for "TEMPLATES[" or "getTemplate" or similar
matches = re.findall(r'(TEMPLATES\[[^\]]+\]|getTemplate[^\)]*\)|template.*=.*TEMPLATES)', content)
print("Template usage patterns:")
for m in matches[:10]:
    print(f"  {m}")

# Also find the function that handles generating the letter
gen_match = re.search(r'(const generateLetter[\s\S]{0,500}|function generateLetter[\s\S]{0,500})', content)
if gen_match:
    print(f"\nGenerate letter function start:")
    print(gen_match.group(0)[:500])