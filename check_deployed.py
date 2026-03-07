#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'D:\Civic voice engagement\deploy\index.html'

with open(filepath, 'rb') as f:
    content = f.read()

print(f"Deployed file size: {len(content)} bytes")

# Find step1Label line
idx = content.find(b'step1Label')
if idx != -1:
    line_start = content.rfind(b'\n', 0, idx)
    line_end = content.find(b'\n', idx)
    line = content[line_start+1:line_end]
    print(f"\nstep1Label line: {line}")
    print(f"Hex: {line.hex()}")

# Check for correct vs corrupted
print("\n=== Encoding check ===")
if b'\xc3\x89' in content:
    print("Found correct UTF-8 É (C3 89)")
if b'\xc3\x83\xc2\x89' in content:
    print("Found DOUBLE-ENCODED É (C3 83 C2 89) - CORRUPTED!")
if b'\xef\xbf\xbd' in content:
    print("Found replacement character (EF BF BD) - CORRUPTED!")

# Count occurrences
print(f"\nCorrect É (C3 89): {content.count(b'\\xc3\\x89')}")
print(f"Double-encoded É: {content.count(b'\\xc3\\x83\\xc2\\x89')}")
print(f"Replacement chars: {content.count(b'\\xef\\xbf\\xbd')}")