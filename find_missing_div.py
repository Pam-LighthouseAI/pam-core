#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Track div depth through entire file
depth = 0
print("Tracking div depth through footer section...")
print()

for i, line in enumerate(lines[4339:4410], 4340):
    opens = line.count('<div')
    closes = line.count('</div>')
    delta = opens - closes
    
    if opens > 0 or closes > 0:
        prev_depth = depth
        depth += delta
        
        # Show the line
        stripped = line.rstrip()
        print(f"Line {i}: depth {prev_depth}->{depth} (opens={opens}, closes={closes})")
        print(f"  {stripped[:75]}")
        
        if depth < 0:
            print("  ^^^ ERROR: Extra close div!")
        print()

print(f"\nFinal depth: {depth}")
print(f"Expected final depth: 0 (all divs closed)")
print(f"Missing </div> tags: {depth}")

# Show last 10 lines of file
print("\nLast 10 lines of file:")
for i, line in enumerate(lines[-10:], len(lines)-9):
    print(f"{i}: {line.rstrip()[:80]}")