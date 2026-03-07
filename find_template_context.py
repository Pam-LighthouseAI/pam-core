import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find lines with TEMPLATES[ usage
for i, line in enumerate(lines):
    if 'TEMPLATES[' in line:
        # Show context - 3 lines before and after
        start = max(0, i-3)
        end = min(len(lines), i+4)
        print(f"\n--- Lines {start+1}-{end} ---")
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"{marker} {j+1}: {lines[j].rstrip()}")