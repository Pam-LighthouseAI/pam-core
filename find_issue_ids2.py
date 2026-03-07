import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find ISSUES array - look for the pattern differently
# The issues have objects like { id: 'potholes', name: 'Potholes', ... }
issues_match = re.search(r'const ISSUES = \[([\s\S]*?)\];', content)
if issues_match:
    issues_content = issues_match.group(1)
    # Find all id: values - could be with single or double quotes
    ids = re.findall(r"id:\s*['\"]([^'\"]+)['\"]", issues_content)
    print(f"Found {len(ids)} issue IDs:")
    for id in ids[:20]:
        print(f"  {id}")
    if len(ids) > 20:
        print(f"  ... and {len(ids) - 20} more")