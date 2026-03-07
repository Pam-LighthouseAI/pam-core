import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Duplicates to check
duplicates = [
    ("Mental health services", "healthcare", "mentalhealth"),
    ("Wildlife protection", "environment", "animals"),
    ("Fire services", "safety", "emergency"),
    ("Data breaches", "consumer", "digital"),
    ("Youth mental health", "youth", "mentalhealth"),
    ("Discrimination complaints", "lgbtq", "humanrights"),
]

for name, cat1, cat2 in duplicates:
    print(f"\n{'='*60}")
    print(f"DUPLICATE: '{name}'")
    print(f"{'='*60}")
    
    # Find this item in each category
    for cat in [cat1, cat2]:
        # Find the category block
        cat_match = re.search(rf'\{{ id:"{cat}".*?items:\s*\[([\s\S]*?)\]\s*\}}', content)
        if cat_match:
            items_str = cat_match.group(1)
            # Find the specific item
            item_match = re.search(rf'\{{name:"{re.escape(name)}".*?\}}', items_str)
            if item_match:
                print(f"\n--- In '{cat}' category ---")
                print(item_match.group(0)[:500])
            else:
                print(f"\n--- In '{cat}' category ---")
                print(f"NOT FOUND (different spelling?)")
                # Try fuzzy find
                fuzzy = re.findall(rf'name:"[^"]*{name.split()[0]}[^"]*"', items_str)
                if fuzzy:
                    print(f"  Similar: {fuzzy[:3]}")