#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Check specific lines
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'step1Label' in line:
        print(f"Line {i+1}: {line}")
    if 'step2Label' in line:
        print(f"Line {i+1}: {line}")
    if 'step3Label' in line:
        print(f"Line {i+1}: {line}")

# Verify French characters are correct
checks = [
    ('Étape', 'É in Étape'),
    ('Où', 'ù in Où'),
    ('enjeu', 'e accent'),
    ('représentants', 'é in représentants'),
    ('municipaux', 'aux'),
]

print("\n=== Character Verification ===")
for text, desc in checks:
    count = content.count(text)
    print(f"{desc}: {count} occurrences of '{text}'")