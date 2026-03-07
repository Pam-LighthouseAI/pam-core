import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find ISSUES array
issues_match = re.search(r'const ISSUES = \[([\s\S]*?)\];', content)
if issues_match:
    issues_content = issues_match.group(1)
    # Find all id: values
    ids = re.findall(r"id:\s*'([^']+)'", issues_content)
    print(f"Found {len(ids)} issue IDs:")
    for id in ids:
        print(f"  {id}")

# Find TEMPLATES object
templates_match = re.search(r'const TEMPLATES = \{([\s\S]*?)\n\};', content)
if templates_match:
    templates_content = templates_match.group(1)
    # Find all template keys (the category names before the colon)
    template_ids = re.findall(r"^\s*(\w+):\s*\{", templates_content, re.MULTILINE)
    print(f"\nFound {len(template_ids)} template IDs:")
    for id in template_ids:
        print(f"  {id}")

# Compare
if ids and template_ids:
    missing = set(ids) - set(template_ids)
    if missing:
        print(f"\nMISSING TEMPLATES for:")
        for m in missing:
            print(f"  {m}")
    else:
        print("\nAll issue IDs have templates!")