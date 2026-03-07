import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the infrastructure category and its items
infra_match = re.search(r'\{ id:"infrastructure".*?items:\[([\s\S]*?)\]\s*\}', content)
if infra_match:
    items = infra_match.group(1)
    # Count items
    item_names = re.findall(r'name:"([^"]+)"', items)
    print(f"Infrastructure category has {len(item_names)} items:")
    for name in item_names:
        print(f"  - {name}")

# Check if "traffic" is a top-level category
issues_match = re.search(r'const ISSUES = \[([\s\S]*?)\];', content)
if issues_match:
    issues = issues_match.group(1)
    # Find all top-level category IDs
    cat_ids = re.findall(r'\{ id:"([^"]+)"', issues)
    print(f"\nTop-level categories ({len(cat_ids)}):")
    for id in cat_ids:
        print(f"  {id}")
    
    if 'traffic' in cat_ids:
        print("\n'traffic' IS a top-level category")
    else:
        print("\n'traffic' is NOT a top-level category - it's an item within another category")