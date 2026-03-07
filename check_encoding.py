#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html'

with open(filepath, 'rb') as f:
    content = f.read()

# Find step1Label line
idx = content.find(b'step1Label')
if idx != -1:
    line_start = content.rfind(b'\n', 0, idx)
    line_end = content.find(b'\n', idx)
    line = content[line_start+1:line_end]
    print(f"step1Label line bytes: {line}")
    print(f"Hex: {line.hex()}")
    
# Check for common encodings
print("\n=== Checking for encoding issues ===")

# Check if file has BOM
if content.startswith(b'\xef\xbb\xbf'):
    print("File has UTF-8 BOM")
elif content.startswith(b'\xff\xfe'):
    print("File has UTF-16 LE BOM")
elif content.startswith(b'\xfe\xff'):
    print("File has UTF-16 BE BOM")
else:
    print("No BOM detected")

# Check for double-encoded UTF-8
# Double-encoded É would be: C3 83 C2 89 (instead of C3 89)
if b'\xc3\x83\xc2\x89' in content:
    print("Found double-encoded É (C3 83 C2 89)")
if b'\xc3\x89' in content:
    print("Found correct UTF-8 É (C3 89)")
    
# Check for replacement characters
if b'\xef\xbf\xbd' in content:
    print("Found replacement character (EF BF BD)")