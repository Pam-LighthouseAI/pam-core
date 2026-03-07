import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find where catId is assigned - search for lines around it
for i, line in enumerate(lines):
    if 'catId' in line:
        start = max(0, i-5)
        end = min(len(lines), i+6)
        print(f"\n--- Lines {start+1}-{end} ---")
        for j in range(start, end):
            marker = ">>>" if j == i else "   "
            print(f"{marker} {j+1}: {lines[j].rstrip()}")