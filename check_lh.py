#!/usr/bin/env python3
filepath = r"D:\source_extracted\my_civic_voice.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
for line in content.split('\n'):
    if 'LighthouseAI' in line or 'Pam et Daniel' in line or 'Pam & Daniel' in line:
        print(line.strip())