#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html'

with open(filepath, 'rb') as f:
    content_bytes = f.read()

print(f"File size: {len(content_bytes)} bytes")

# Find 'tape 1' in bytes
idx = content_bytes.find(b'tape 1')
if idx != -1:
    print(f"\n'tape 1' found at byte {idx}")
    print(f"Bytes before: {content_bytes[idx-20:idx+30]}")
    # Show hex
    print(f"Hex: {content_bytes[idx-20:idx+30].hex()}")

# Find 'O habitez' in bytes  
idx2 = content_bytes.find(b'O habitez')
if idx2 != -1:
    print(f"\n'O habitez' found at byte {idx2}")
    print(f"Bytes: {content_bytes[idx2-10:idx2+20]}")
    print(f"Hex: {content_bytes[idx2-10:idx2+20].hex()}")