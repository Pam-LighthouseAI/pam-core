#!/usr/bin/env python3
filepath = r"D:\source_extracted\my_civic_voice.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
for line in content.split('\n'):
    if 'LighthouseAI' in line or 'Crée par' in line or 'Made by' in line:
        print(line.strip())