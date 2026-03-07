#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} characters")

# Find Commencer
idx = content.find('Commencer')
print(f"Commencer at position: {idx}")
if idx != -1:
    print(f"Context: {content[idx-50:idx+200]}")