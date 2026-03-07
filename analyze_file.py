#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} characters")

# Find all corrupted characters (replacement character or mojibake)
import re

# Find replacement characters
replacements = content.count('\ufffd')
print(f"Replacement characters: {replacements}")

# Find lines with issues
lines = content.split('\n')
for i, line in enumerate(lines):
    if '\ufffd' in line:
        print(f"Line {i+1}: {line[:150]}...")

# Count specific patterns
patterns = {
    'Étape': content.count('Étape'),
    'tape 1': content.count('tape 1'),
    'Où': content.count('Où'),
    'O habitez': content.count('O habitez'),
}

print("\nPattern counts:")
for p, c in patterns.items():
    print(f"  '{p}': {c}")