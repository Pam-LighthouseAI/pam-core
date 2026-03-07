import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find "Traffic Signs" in the content
traffic_matches = re.findall(r'.{0,100}Traffic Signs?.{0,100}', content, re.IGNORECASE)
print("Traffic Signs references:")
for m in traffic_matches[:15]:
    print(f"  {m.strip()}")

# Check if there's a "traffic" template
if 'traffic:' in content.lower() or '"traffic"' in content.lower():
    print("\nFound 'traffic' reference in templates")
else:
    print("\nNo 'traffic' template found")

# Check TEMPLATES for traffic
templates_match = re.search(r'const TEMPLATES = \{([\s\S]*?)\n\};', content)
if templates_match:
    if 'traffic' in templates_match.group(1).lower():
        print("Traffic template EXISTS")
    else:
        print("Traffic template MISSING")