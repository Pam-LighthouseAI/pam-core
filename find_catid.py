import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where catId is defined/used
catid_matches = re.findall(r'(catId\s*[=:]|const catId|let catId|catId:)', content)
print(f"catId references: {len(catid_matches)}")

# Find the ISSUES structure - look at first few entries
issues_match = re.search(r'const ISSUES = \[([\s\S]{0,3000})', content)
if issues_match:
    print("\nISSUES structure (first entries):")
    print(issues_match.group(1)[:2000])