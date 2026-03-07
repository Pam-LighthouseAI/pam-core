#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

# Read file as bytes
with open(filepath, 'rb') as f:
    content_bytes = f.read()

print("Fixing encoding issues...")

# Fix double-encoded UTF-8 characters
replacements = [
    # French accents (double-encoded UTF-8 -> proper UTF-8)
    (b'\xc3\x83\xc2\xa9', b'\xc3\xa9'),  # é
    (b'\xc3\x83\xc2\xa8', b'\xc3\xa8'),  # è
    (b'\xc3\x83\xc2\xa0', b'\xc3\xa0'),  # à
    (b'\xc3\x83\xc2\xa7', b'\xc3\xa7'),  # ç
    (b'\xc3\x83\xc2\xb9', b'\xc3\xb9'),  # ù
    (b'\xc3\x83\xc2\xbb', b'\xc3\xbb'),  # û
    (b'\xc3\x83\xc2\xb4', b'\xc3\xb4'),  # ô
    (b'\xc3\x83\xc2\xae', b'\xc3\xae'),  # î
    (b'\xc3\x83\xc2\xab', b'\xc3\xab'),  # ë
    (b'\xc3\x83\xe2\x82\xac', b'\xc3\x89'),  # É
    (b'\xc3\x83\xc2\x89', b'\xc3\x89'),  # É (alternate)
    (b'\xc3\x83\xc2\xaa', b'\xc3\xaa'),  # ê
    (b'\xc3\x83\xc2\xa2', b'\xc3\xa2'),  # â
    (b'\xc3\x83\xc2\xac', b'\xc3\xac'),  # ì
    (b'\xc3\x83\xc2\xb2', b'\xc3\xb2'),  # ò
    (b'\xc3\x83\xc2\xb3', b'\xc3\xb3'),  # ó
    # Emojis and special characters
    (b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9c', b'\xe2\x80\x99'),  # apostrophe
    (b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d', b'\xe2\x80\x94'),  # em dash
    (b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9c', b'\xe2\x80\x9c'),  # left quote
    (b'\xc3\xa2\xe2\x82\xac\xe2\x84\xa2', b'\xe2\x80\x9d'),  # right quote
]

count = 0
for old_bytes, new_bytes in replacements:
    if old_bytes in content_bytes:
        occurrences = content_bytes.count(old_bytes)
        content_bytes = content_bytes.replace(old_bytes, new_bytes)
        count += occurrences
        print(f"  Fixed {occurrences} instances of corrupted character")

# Add UTF-8 BOM if not present
if not content_bytes.startswith(b'\xef\xbb\xbf'):
    content_bytes = b'\xef\xbb\xbf' + content_bytes
    print("  Added UTF-8 BOM")

# Write back
with open(filepath, 'wb') as f:
    f.write(content_bytes)

print(f"\nTotal fixes: {count}")
print("File saved with UTF-8 BOM")

# Verify the fix
print("\nVerifying...")
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Check key French phrases
key_checks = [
    ('Étape 1 sur 3', 'Step 1 label'),
    ('Où habitez-vous', 'Where do you live'),
    ('représentants', 'representatives'),
    ('enjeu', 'issue'),
]

for phrase, desc in key_checks:
    if phrase in content:
        print(f"  OK: '{phrase}' ({desc})")
    else:
        print(f"  MISSING: '{phrase}' ({desc})")

print("\nDone!")