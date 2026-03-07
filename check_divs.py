#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Count div tags
open_divs = content.count('<div')
close_divs = content.count('</div>')
print(f"Open divs: {open_divs}")
print(f"Close divs: {close_divs}")
print(f"Difference: {open_divs - close_divs}")

if open_divs != close_divs:
    # Find unclosed divs by tracking depth
    import re
    lines = content.split('\n')
    depth = 0
    max_depth = 0
    issues = []
    
    for i, line in enumerate(lines, 1):
        # Count opens and closes on this line
        opens = line.count('<div')
        closes = line.count('</div>')
        prev_depth = depth
        depth += opens - closes
        max_depth = max(max_depth, depth)
        
        if depth < 0:
            issues.append((i, "Extra close div", line.strip()[:60]))
    
    print(f"\nMax depth: {max_depth}")
    print(f"Final depth: {depth}")
    
    if issues:
        print("\nIssues found:")
        for line_num, issue, content in issues[:10]:
            print(f"  Line {line_num}: {issue}")
            print(f"    {content}")
    
    # Find last few div opens
    print("\nLast 5 open divs:")
    last_opens = []
    pos = 0
    while True:
        idx = content.find('<div', pos)
        if idx == -1:
            break
        last_opens.append(idx)
        pos = idx + 1
        if len(last_opens) > 5:
            last_opens.pop(0)
    
    for idx in last_opens:
        line_num = content[:idx].count('\n') + 1
        snippet = content[idx:idx+50]
        print(f"  Line {line_num}: {snippet!r}")
else:
    print("Div tags are balanced!")