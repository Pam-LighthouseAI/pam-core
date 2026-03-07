#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Track div depth through ENTIRE file
depth = 0
min_depth = 0
first_negative_line = None

for i, line in enumerate(lines, 1):
    opens = line.count('<div')
    closes = line.count('</div>')
    delta = opens - closes
    prev_depth = depth
    depth += delta
    
    if depth < min_depth:
        min_depth = depth
    
    if depth < 0 and first_negative_line is None:
        first_negative_line = (i, prev_depth, depth, line.rstrip()[:60])

print(f"Total lines: {len(lines)}")
print(f"Final depth: {depth}")
print(f"Minimum depth: {min_depth}")
print()

if first_negative_line:
    print(f"First negative depth at line {first_negative_line[0]}:")
    print(f"  Depth went from {first_negative_line[1]} to {first_negative_line[2]}")
    print(f"  Content: {first_negative_line[3]}")
    print()
    
    # Show context around that line
    start = max(1, first_negative_line[0] - 10)
    print(f"Context (lines {start}-{first_negative_line[0]+5}):")
    depth2 = 0
    for i, line in enumerate(lines[start-1:first_negative_line[0]+5], start):
        opens = line.count('<div')
        closes = line.count('</div>')
        delta = opens - closes
        depth2 += delta
        marker = " <-- FIRST NEGATIVE" if i == first_negative_line[0] else ""
        if opens > 0 or closes > 0:
            print(f"  {i}: depth={depth2} {line.rstrip()[:60]}{marker}")