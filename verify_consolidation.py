import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check each duplicate pair
duplicates = [
    ("Mental health services", "healthcare", "mentalhealth"),
    ("Wildlife protection", "environment", "animals"),
    ("Fire services", "safety", "emergency"),
    ("Data breaches", "consumer", "digital"),
    ("Youth mental health", "youth", "mentalhealth"),
    ("Discrimination complaints", "lgbtq", "humanrights"),
]

print("Checking if duplicates now have IDENTICAL content:\n")

for name, cat1, cat2 in duplicates:
    # Find in cat1
    cat1_match = re.search(rf'\{{ id:"{cat1}".*?items:\s*\[([\s\S]*?)\]\s*\}}', content)
    cat2_match = re.search(rf'\{{ id:"{cat2}".*?items:\s*\[([\s\S]*?)\]\s*\}}', content)
    
    if cat1_match and cat2_match:
        item1 = re.search(rf'\{{name:"{re.escape(name)}".*?\}}', cat1_match.group(1))
        item2 = re.search(rf'\{{name:"{re.escape(name)}".*?\}}', cat2_match.group(1))
        
        if item1 and item2:
            if item1.group(0) == item2.group(0):
                print(f"[OK] '{name}' - IDENTICAL in both {cat1} and {cat2}")
            else:
                print(f"[X] '{name}' - DIFFERENT in {cat1} vs {cat2}")
                print(f"  {cat1}: {item1.group(0)[:100]}...")
                print(f"  {cat2}: {item2.group(0)[:100]}...")

# Check traffic items consolidated
print("\n\nChecking Traffic items:")
infra_match = re.search(r'\{ id:"infrastructure".*?items:\s*\[([\s\S]*?)\]\s*\}', content)
if infra_match:
    traffic_items = re.findall(r'name:"Traffic[^"]*"', infra_match.group(1))
    print(f"Traffic items found: {len(traffic_items)}")
    for t in traffic_items:
        print(f"  - {t}")