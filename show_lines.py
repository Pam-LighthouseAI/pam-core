#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Show lines 4095-4110
print("Lines 4095-4110:")
for i in range(4094, 4110):
    print(f"{i+1}: {lines[i][:80]}")