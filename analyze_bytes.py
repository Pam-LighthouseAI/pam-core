#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

# Read file as bytes
with open(filepath, 'rb') as f:
    content_bytes = f.read()

print("Analyzing byte patterns...")

# Find "tape 1" to see what's before it
idx = content_bytes.find(b'tape 1')
if idx > 0:
    print(f"\nBytes around 'tape 1':")
    before = content_bytes[idx-10:idx]
    after = content_bytes[idx:idx+20]
    print(f"  Before: {before}")
    print(f"  After: {after}")
    print(f"  Hex before: {before.hex()}")
    print(f"  Hex after: {after.hex()}")

# Check for UTF-8 É (C3 89)
utf8_e_acute = b'\xc3\x89'
count = content_bytes.count(utf8_e_acute)
print(f"\nUTF-8 É (C3 89): {count} occurrences")

# Check for double-encoded É (C3 83 C2 89)
double_e_acute = b'\xc3\x83\xc2\x89'
count = content_bytes.count(double_e_acute)
print(f"Double-encoded É (C3 83 C2 89): {count} occurrences")

# Check for replacement character
replacement = b'\xef\xbf\xbd'
count = content_bytes.count(replacement)
print(f"Replacement character (EF BF BD): {count} occurrences")

# Check file start
print(f"\nFile starts with BOM: {content_bytes[:3] == b'\\xef\\xbb\\xbf'}")
print(f"First 20 bytes: {content_bytes[:20]}")
print(f"First 20 hex: {content_bytes[:20].hex()}")

# Look for common French patterns
print("\nLooking for French patterns:")

# "Où" should be O + C3 B9
o_u_grave = b'O\xc3\xb9'
count = content_bytes.count(o_u_grave)
print(f"  Où (O + C3 B9): {count} occurrences")

# "représentants" should have é (C3 A9)
representants = b'repr\xc3\xa9sentants'
count = content_bytes.count(representants)
print(f"  représentants: {count} occurrences")

# "enjeu" - no accents
enjeu = b'enjeu'
count = content_bytes.count(enjeu)
print(f"  enjeu: {count} occurrences")