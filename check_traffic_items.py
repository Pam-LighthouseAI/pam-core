import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find both traffic-related items
traffic1_match = re.search(r'\{name:"Traffic signals & signage"[^}]+\}', content)
traffic2_match = re.search(r'\{name:"Traffic signs & signage"[^}]+\}', content)

print("Traffic signals & signage:")
if traffic1_match:
    print(traffic1_match.group(0))
else:
    print("NOT FOUND")

print("\n\nTraffic signs & signage:")
if traffic2_match:
    print(traffic2_match.group(0))
else:
    print("NOT FOUND")

# Check for any duplicate names in Infrastructure
infra_match = re.search(r'\{ id:"infrastructure".*?items:\[([\s\S]*?)\]\s*\}', content)
if infra_match:
    items_str = infra_match.group(1)
    # Extract all item objects
    item_objects = re.findall(r'\{name:"[^"]+", nameFr:"[^"]+", primary:"[^"]+", secondary:\[[^\]]*\], detail:"[^"]+", detailFr:"[^"]+"\}', items_str)
    print(f"\n\nFound {len(item_objects)} item objects in Infrastructure")
    
    # Check for duplicates
    names = re.findall(r'name:"([^"]+)"', items_str)
    name_counts = {}
    for name in names:
        name_counts[name] = name_counts.get(name, 0) + 1
    
    duplicates = {k: v for k, v in name_counts.items() if v > 1}
    if duplicates:
        print(f"DUPLICATE NAMES: {duplicates}")