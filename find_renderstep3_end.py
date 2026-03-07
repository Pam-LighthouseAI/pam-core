#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# Find where renderStep3 ends
print("Looking for renderStep3 function end...")
for i in range(3870, 4200):
    line = lines[i]
    if ');' in line and line.strip() == ');':
        print(f"Line {i+1}: {line}")
    if 'const render' in line or 'function render' in line:
        print(f"Line {i+1}: {line[:70]}")

print("\n\nLines 3920-3980 (renderStep3 area):")
depth = 0
for i in range(3920, min(3980, len(lines))):
    line = lines[i]
    opens = line.count('<div')
    closes = line.count('</div>')
    if opens > 0 or closes > 0:
        prev = depth
        depth += opens - closes
        safe_line = line[:70].encode('ascii', 'replace').decode('ascii')
        print(f"{i+1}: [{prev}->{depth}] {safe_line}")