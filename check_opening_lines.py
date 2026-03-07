import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find OPENING_LINES object
opening_match = re.search(r'const OPENING_LINES = \{([\s\S]*?)\n\};', content)
if opening_match:
    opening_content = opening_match.group(1)
    # Find all tone categories
    tones = re.findall(r"(\w+):\s*\{", opening_content)
    print(f"Opening line tones: {tones}")
    
    # For each tone, find the categories
    for tone in tones:
        tone_match = re.search(rf"{tone}:\s*\{{([^}}]+)\}}", opening_content)
        if tone_match:
            cats = re.findall(r"(\w+):", tone_match.group(1))
            print(f"  {tone}: {len(cats)} categories")