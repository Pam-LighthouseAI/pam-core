#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# Track depth from line 3876 to 4106
print("Div tracking from renderStep3 start to end:")
depth = 0
for i in range(3875, 4106):
    line = lines[i]
    opens = line.count('<div')
    closes = line.count('</div>')
    if opens > 0 or closes > 0:
        prev = depth
        depth += opens - closes
        safe_line = line[:70].encode('ascii', 'replace').decode('ascii')
        print(f"{i+1}: [{prev}->{depth}] {safe_line}")

print(f"\nFinal depth at end of renderStep3: {depth}")
print("Should be 0 if all divs are balanced")