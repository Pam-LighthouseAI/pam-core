#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'D:\Civic voice engagement\deploy\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find charset
import re
match = re.search(r'charset', content[:5000])
if match:
    start = max(0, match.start() - 50)
    end = min(len(content), match.end() + 50)
    print(f"Charset context: {content[start:end]}")
else:
    print("No charset found in first 5000 chars")
    print(f"\nFirst 500 chars:\n{content[:500]}")