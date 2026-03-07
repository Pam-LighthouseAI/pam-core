#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

print("Lines 3870-3900:")
for i in range(3869, min(3900, len(lines))):
    line = lines[i]
    # Highlight div tags
    if '<div' in line or '</div>' in line:
        print(f"{i+1}: >>> {line[:80]}")
    else:
        print(f"{i+1}: {line[:80]}")