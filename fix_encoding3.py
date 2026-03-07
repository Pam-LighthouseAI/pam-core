#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} characters")

# Fix corrupted characters
replacements = [
    # Em dashes
    ('\xe2\x80\x9c', '\u2014'),  # â€" -> —
    ('\xe2\x80\x9d', '\u2014'),  # â€" -> —
    ('\xe2\x80\x93', '\u2014'),  # â€" -> —
    ('\xe2\x80\x94', '\u2014'),  # â€" -> —
    ('\xe2\x80\x99', "'"),       # â€™ -> '
    ('\xe2\x80\x98', "'"),       # â€˜ -> '
    ('\xe2\x80\x9c', '"'),       # â€œ -> "
    ('\xe2\x80\x9d', '"'),       # â€ -> "
    
    # Arrows
    ('\xe2\x86\x92', '\u2192'),  # â†' -> →
    
    # Checkmarks
    ('\xe2\x9c\x93', '\u2713'),  # âœ" -> ✓
    
    # Emojis - scale
    ('\xe2\x9a\x96\xef\xb8\x8f', '\u2696\ufe0f'),  # âš–ï¸ -> ⚖️
    ('\xe2\x9a\x96', '\u2696'),  # âš– -> ⚖
    
    # Lightning
    ('\xe2\x9a\xa1', '\u26a1'),  # âš¡ -> ⚡
    
    # Warning
    ('\xe2\x9a\xa0\xef\xb8\x8f', '\u26a0\ufe0f'),  # âš ï¸ -> ⚠️
    
    # Soccer
    ('\xe2\x9a\xbd', '\u26bd'),  # âš½ -> ⚽
    
    # Church
    ('\xe2\x9b\xaa', '\u26ea'),  # â›ª -> ⛪
    
    # Female sign
    ('\xe2\x99\x80\xef\xb8\x8f', '\u2640\ufe0f'),  # â™€ï¸ -> ♀️
    ('\xe2\x99\x80', '\u2640'),  # â™€ -> ♀
    
    # Wheelchair
    ('\xe2\x99\xbf', '\u267f'),  # â™¿ -> ♿
    
    # Airplane
    ('\xe2\x9c\x88\xef\xb8\x8f', '\u2708\ufe0f'),  # âœˆï¸ -> ✈️
    
    # Copyright
    ('\xc2\xa9', '\xa9'),  # Â© -> ©
    
    # French accents
    ('\xc3\x89', '\xc9'),  # Ã‰ -> É
    ('\xc3\xa9', '\xe9'),  # Ã© -> é
    ('\xc3\xa8', '\xe8'),  # Ã¨ -> è
    ('\xc3\xaa', '\xea'),  # Ãª -> ê
    ('\xc3\xab', '\xeb'),  # Ã« -> ë
    ('\xc3\xae', '\xee'),  # Ã® -> î
    ('\xc3\xb4', '\xf4'),  # Ã´ -> ô
    ('\xc3\xbb', '\xfb'),  # Ã» -> û
    ('\xc3\xa0', '\xe0'),  # Ã  -> à
    ('\xc3\xa7', '\xe7'),  # Ã§ -> ç
    ('\xc3\xb9', '\xf9'),  # Ã¹ -> ù
    ('\xc3\xa2', '\xe2'),  # Ã¢ -> â
    ('\xc3\xac', '\xec'),  # Ã¬ -> ì
    ('\xc3\xb2', '\xf2'),  # Ã² -> ò
    ('\xc3\xb3', '\xf3'),  # Ã³ -> ó
]

count = 0
for old, new in replacements:
    if old in content:
        found = content.count(old)
        content = content.replace(old, new)
        count += found
        print(f"Fixed {found} instances")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal fixes applied: {count}")
print("Done!")