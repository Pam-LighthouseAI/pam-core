#!/usr/bin/env python3
filepath = r"D:\source_extracted\my_civic_voice.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

if 'Créé par' in content:
    print("SUCCESS: 'Créé par' with proper accents is in the file")
else:
    print("ERROR: accent missing")
    
# Find and show
idx = content.find("isFrench ? 'Cr")
print("Found at index:", idx)
print("Text:", content[idx:idx+80])