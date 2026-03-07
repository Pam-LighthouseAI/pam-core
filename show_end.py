#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# Show lines around 4100-4110
print("Lines 4095-4115:")
for i in range(4094, min(4115, len(lines))):
    line = lines[i]
    safe_line = line[:80].encode('ascii', 'replace').decode('ascii')
    print(f"{i+1}: {safe_line}")