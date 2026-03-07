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
    print(f"\n{'='*80}")
    print(f"DUPLICATE: '{name}'")
    print(f"{'='*80}")
    
    for cat in [cat1, cat2]:
        cat_match = re.search(rf'\{{ id:"{cat}".*?items:\s*\[([\s\S]*?)\]\s*\}}', content)
        if cat_match:
            items_str = cat_match.group(1)
            item_match = re.search(rf'\{{name:"{re.escape(name)}".*?\}}', items_str)
            if item_match:
                print(f"\n--- In '{cat}' category ---")
                print(item_match.group(0))
                print()