#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} characters")

# Fix corrupted characters using byte sequences
replacements = [
    # French accents (double-encoded UTF-8)
    ('\xc3\x89', '\xc9'),  # É
    ('\xc3\xa9', '\xe9'),  # é
    ('\xc3\xa8', '\xe8'),  # è
    ('\xc3\xaa', '\xea'),  # ê
    ('\xc3\xab', '\xeb'),  # ë
    ('\xc3\xae', '\xee'),  # î
    ('\xc3\xb4', '\xf4'),  # ô
    ('\xc3\xbb', '\xfb'),  # û
    ('\xc3\xa0', '\xe0'),  # à
    ('\xc3\xa7', '\xe7'),  # ç
    ('\xc3\xb9', '\xf9'),  # ù
    ('\xc3\xa2', '\xe2'),  # â
    ('\xc3\xac', '\xec'),  # ì
    ('\xc3\xb2', '\xf2'),  # ò
    ('\xc3\xb3', '\xf3'),  # ó
    
    # Copyright
    ('\xc2\xa9', '\xa9'),  # ©
    
    # Em dash
    ('\xe2\x80\x94', '\u2014'),  # —
    ('\xe2\x80\x93', '\u2014'),  # —
    
    # Arrow
    ('\xe2\x86\x92', '\u2192'),  # →
    
    # Checkmark
    ('\xe2\x9c\x93', '\u2713'),  # ✓
    
    # Emojis
    ('\xe2\x9a\x96', '\u2696'),  # ⚖
    ('\xe2\x9a\xa1', '\u26a1'),  # ⚡
    ('\xe2\x9a\xbd', '\u26bd'),  # ⚽
    ('\xe2\x9b\xaa', '\u26ea'),  # ⛪
    ('\xe2\x99\x80', '\u2640'),  # ♀
    ('\xe2\x99\xbf', '\u267f'),  # ♿
    ('\xe2\x9c\x88', '\u2708'),  # ✈
]

count = 0
for old_bytes, new_char in replacements:
    # Convert to string representation
    try:
        old_str = old_bytes.decode('latin-1')
        if old_str in content:
            found = content.count(old_str)
            content = content.replace(old_str, new_char)
            count += found
            print(f"Fixed {found} x '{old_str}' -> '{new_char}'")
    except:
        pass

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal fixes: {count}")