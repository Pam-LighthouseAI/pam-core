import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find ISSUES array
issues_match = re.search(r'const ISSUES = \[([\s\S]*?)\];', content)
if issues_match:
    issues_content = issues_match.group(1)
    ids = re.findall(r"id:\s*['\"]([^'\"]+)['\"]", issues_content)
    print(f"Issue IDs ({len(ids)}):")
    for id in sorted(ids):
        print(f"  {id}")

# Find TEMPLATES object
templates_match = re.search(r'const TEMPLATES = \{([\s\S]*?)\n\};', content)
if templates_match:
    templates_content = templates_match.group(1)
    template_ids = re.findall(r"^\s*(\w+):\s*\{", templates_content, re.MULTILINE)
    print(f"\nTemplate IDs ({len(template_ids)}):")
    for id in sorted(template_ids):
        print(f"  {id}")

# Compare
if ids and template_ids:
    missing = set(ids) - set(template_ids)
    extra = set(template_ids) - set(ids)
    if missing:
        print(f"\nMISSING TEMPLATES for issues:")
        for m in sorted(missing):
            print(f"  {m}")
    if extra:
        print(f"\nEXTRA TEMPLATES (no matching issue):")
        for e in sorted(extra):
            print(f"  {e}")
    if not missing and not extra:
        print("\nAll IDs match!")