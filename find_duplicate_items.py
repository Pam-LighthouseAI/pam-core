import re
from difflib import SequenceMatcher

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all items across all categories
# Pattern: items:[{name:"...", ...}]
items_match = re.findall(r'items:\s*\[([\s\S]*?)\]\s*\}', content)

all_items = []
category_context = {}

# Find category boundaries
categories = re.finditer(r'\{ id:"([^"]+)".*?items:\s*\[([\s\S]*?)\]\s*\}', content)

for cat_match in categories:
    cat_id = cat_match.group(1)
    items_str = cat_match.group(2)
    
    # Extract item names
    item_names = re.findall(r'name:"([^"]+)"', items_str)
    for name in item_names:
        all_items.append((cat_id, name))

print(f"Total items: {len(all_items)}\n")

# Find exact duplicates
name_counts = {}
for cat, name in all_items:
    if name not in name_counts:
        name_counts[name] = []
    name_counts[name].append(cat)

print("=== EXACT DUPLICATES ===")
exact_dups = {k: v for k, v in name_counts.items() if len(v) > 1}
if exact_dups:
    for name, cats in exact_dups.items():
        print(f"  '{name}' appears in: {cats}")
else:
    print("  None found")

# Find similar items (fuzzy match)
print("\n=== SIMILAR ITEMS (potential duplicates) ===")
checked = set()
similar_pairs = []

for i, (cat1, name1) in enumerate(all_items):
    for j, (cat2, name2) in enumerate(all_items):
        if i >= j:
            continue
        pair_key = tuple(sorted([name1, name2]))
        if pair_key in checked:
            continue
        checked.add(pair_key)
        
        # Calculate similarity
        ratio = SequenceMatcher(None, name1.lower(), name2.lower()).ratio()
        if ratio > 0.7 and ratio < 1.0:  # Similar but not identical
            similar_pairs.append((name1, name2, cat1, cat2, ratio))

# Sort by similarity
similar_pairs.sort(key=lambda x: x[4], reverse=True)

for name1, name2, cat1, cat2, ratio in similar_pairs[:30]:
    print(f"  {ratio:.0%} similar:")
    print(f"    '{name1}' ({cat1})")
    print(f"    '{name2}' ({cat2})")
    print()