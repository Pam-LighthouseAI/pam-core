import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the broken span tag
for i, line in enumerate(lines, 1):
    if 'fontSize:20></span>' in line:
        print(f'Line {i}: {line.rstrip()}')
