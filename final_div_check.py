#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# Track depth through entire file
depth = 0
max_depth = 0
max_line = 0

for i, line in enumerate(lines):
    opens = line.count('<div')
    closes = line.count('</div>')
    depth += opens - closes
    if depth > max_depth:
        max_depth = depth
        max_line = i + 1

print(f"Total lines: {len(lines)}")
print(f"Final depth: {depth}")
print(f"Max depth: {max_depth} at line {max_line}")

# Find the last open div that's not closed
# Use a stack approach
stack = []
for i, line in enumerate(lines, 1):
    # Process opens first (push to stack)
    pos = 0
    while True:
        idx = line.find('<div', pos)
        if idx == -1:
            break
        stack.append((i, line[idx:idx+60].encode('ascii', 'replace').decode('ascii')))
        pos = idx + 1
    
    # Then process closes (pop from stack)
    closes = line.count('</div>')
    for _ in range(closes):
        if stack:
            stack.pop()

if stack:
    print(f"\nUnclosed divs: {len(stack)}")
    for line_num, snippet in stack:
        print(f"  Line {line_num}: {snippet}")
else:
    print("\nAll divs properly closed!")