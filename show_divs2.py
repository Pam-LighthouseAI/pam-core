#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

print("Lines 4200-4350 (showing divs):")
depth = 0
for i in range(4200, min(4350, len(lines))):
    line = lines[i]
    opens = line.count('<div')
    closes = line.count('</div>')
    if opens > 0 or closes > 0:
        prev = depth
        depth += opens - closes
        # Only print ASCII-safe parts
        safe_line = line[:70].encode('ascii', 'replace').decode('ascii')
        print(f"{i+1}: [{prev}->{depth}] {safe_line}")