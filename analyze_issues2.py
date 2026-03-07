import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find duplicate detailFr - get more context
print("=== FINDING DUPLICATE detailFr ===")
# Split into lines and find lines with multiple detailFr
lines = content.split('\n')
for i, line in enumerate(lines, 1):
    if line.count('detailFr') > 1:
        print(f'Line {i}: {line[:150]}...')
        print()

# Also find the exact duplicate pattern
dup_pattern = r'(\{name:"[^"]+",\s*nameFr:"[^"]+",\s*primary:"[^"]+",\s*secondary:\[[^\]]*\],\s*detail:"[^"]+",\s*detailFr:"[^"]+",\s*detailFr:"[^"]+")'
dup_matches = re.findall(dup_pattern, content)
print(f'\n=== EXACT DUPLICATES ({len(dup_matches)}) ===')
for m in dup_matches:
    print(m[:200])

# Count categories by looking at the ISSUES array structure
# Find where ISSUES is defined
issues_start = content.find('const ISSUES = [')
if issues_start > 0:
    # Find category markers - they might be comments or separate arrays
    issues_section = content[issues_start:issues_start+50000]
    
    # Look for category pattern - items seem to be grouped
    # Let's find all unique primary values
    primaries = re.findall(r'primary:"(\w+)"', issues_section)
    print(f'\n=== PRIMARY VALUES ===')
    from collections import Counter
    primary_counts = Counter(primaries)
    for p, c in primary_counts.items():
        print(f'  {p}: {c}')
    
    # Try to find category headers another way
    # Look for patterns like "Infrastructure" appearing before items
    print(f'\n=== LOOKING FOR CATEGORY STRUCTURE ===')
    # Find all lines that might be category headers
    for i, line in enumerate(lines):
        if 'Infrastructure' in line or 'Healthcare' in line or 'Education' in line:
            if 'name:' not in line and 'nameFr:' not in line:
                print(f'Line {i+1}: {line.strip()[:100]}')