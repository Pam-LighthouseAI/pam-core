import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all issue objects - they have name, nameFr, primary, secondary, detail
# Pattern to match issue objects
issue_pattern = r'\{name:"([^"]+)",\s*nameFr:"([^"]+)",\s*primary:"([^"]+)",\s*secondary:\[[^\]]*\],\s*detail:"([^"]+)"'

issues = re.findall(issue_pattern, content)
print(f'Total issues found: {len(issues)}')

# Check for missing detailFr
issues_missing_detailFr = []
for name, nameFr, primary, detail in issues:
    # Find this issue in content and check if detailFr follows
    issue_start = content.find(f'name:"{name}"')
    if issue_start > 0:
        # Look for detailFr within next 500 chars
        next_chunk = content[issue_start:issue_start+1000]
        if 'detailFr:' not in next_chunk:
            issues_missing_detailFr.append(name)

print(f'\n=== ISSUES MISSING detailFr ({len(issues_missing_detailFr)}) ===')
for issue in issues_missing_detailFr:
    print(f'  - {issue}')

# Check for duplicate detailFr
duplicate_pattern = r'detailFr:"[^"]*"[^}]*detailFr:'
duplicates = re.findall(duplicate_pattern, content)
print(f'\n=== DUPLICATE detailFr INSTANCES ({len(duplicates)}) ===')
for dup in duplicates[:10]:
    print(f'  {dup[:80]}...')

# Count categories (look for category blocks)
category_pattern = r'const\s+(\w+)\s*=\s*\['
categories_found = re.findall(category_pattern, content)
print(f'\n=== VARIABLE ARRAYS FOUND ===')
for cat in categories_found[:20]:
    print(f'  - {cat}')

# Find category headers within issues
cat_header_pattern = r'//\s*(\w+)\s*\n\s*\{name:"'
cat_headers = re.findall(cat_header_pattern, content)
print(f'\n=== CATEGORY COMMENTS ({len(cat_headers)}) ===')
for h in cat_headers[:40]:
    print(f'  - {h}')