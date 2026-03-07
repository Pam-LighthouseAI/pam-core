#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Count issues before
print(f"File size: {len(content)} characters")

# Fix corrupted copyright symbols
count_copyright = content.count('Â©')
print(f"Found {count_copyright} corrupted copyright symbols (Â©)")
content = content.replace('Â©', '©')

# Fix corrupted em dashes
count_emdash1 = content.count('â€"')
count_emdash2 = content.count('â€"')
count_emdash3 = content.count('â€\"')
print(f"Found {count_emdash1 + count_emdash2 + count_emdash3} corrupted em dashes")
content = content.replace('â€"', '—')
content = content.replace('â€"', '—')
content = content.replace('â€\"', '—')

# Fix corrupted French accents
count_eacute = content.count('Ã©')
count_egrave = content.count('Ã¨')
count_ecirc = content.count('Ãª')
count_euml = content.count('Ã«')
print(f"Found {count_eacute + count_egrave + count_ecirc + count_euml} corrupted French accents")

content = content.replace('Ã‰', 'É')
content = content.replace('Ã©', 'é')
content = content.replace('Ã¨', 'è')
content = content.replace('Ãª', 'ê')
content = content.replace('Ã«', 'ë')
content = content.replace('Ã®', 'î')
content = content.replace('Ã´', 'ô')
content = content.replace('Ã»', 'û')
content = content.replace('Ã ', 'à')
content = content.replace('Ã§', 'ç')

# Fix specific issues
content = content.replace('sur les representants', 'sur les représentants')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Encoding fixes applied successfully!")