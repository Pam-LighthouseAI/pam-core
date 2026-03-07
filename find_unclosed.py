#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.split('\n')

# Track div depth through ENTIRE file
depth = 0
max_depth = 0
max_depth_line = 0

for i, line in enumerate(lines, 1):
    opens = line.count('<div')
    closes = line.count('</div>')
    delta = opens - closes
    depth += delta
    
    if depth > max_depth:
        max_depth = depth
        max_depth_line = i

print(f"Total lines: {len(lines)}")
print(f"Final depth: {depth}")
print(f"Max depth: {max_depth} at line {max_depth_line}")
print()

# Show the last 15 lines with div activity
print("Last 15 div-related lines:")
div_lines = []
for i, line in enumerate(lines, 1):
    opens = line.count('<div')
    closes = line.count('</div>')
    if opens > 0 or closes > 0:
        div_lines.append((i, opens, closes, line[:70]))

for i, opens, closes, content in div_lines[-15:]:
    print(f"  Line {i}: opens={opens}, closes={closes}")
    print(f"    {content}")

# Find all open divs and track which ones get closed
print("\n\nAnalyzing div structure...")
open_divs = []  # Stack of (line_num, div_snippet)
for i, line in enumerate(lines, 1):
    # Process closes first (LIFO)
    closes = line.count('</div>')
    for _ in range(closes):
        if open_divs:
            open_divs.pop()
    
    # Then process opens
    pos = 0
    while True:
        idx = line.find('<div', pos)
        if idx == -1:
            break
        # Extract some context
        snippet = line[idx:idx+50]
        open_divs.append((i, snippet))
        pos = idx + 1

if open_divs:
    print(f"\nUnclosed divs ({len(open_divs)}):")
    for line_num, snippet in open_divs:
        print(f"  Line {line_num}: {snippet}")
else:
    print("\nAll divs are properly closed!")