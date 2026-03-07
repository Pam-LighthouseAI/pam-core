#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

print("Lines 3870-4100 (showing divs):")
depth = 0
for i in range(3869, min(4100, len(lines))):
    line = lines[i]
    opens = line.count('<div')
    closes = line.count('</div>')
    if opens > 0 or closes > 0:
        prev = depth
        depth += opens - closes
        print(f"{i+1}: [{prev}->{depth}] {line[:75]}")