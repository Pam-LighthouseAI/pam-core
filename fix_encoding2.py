#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} characters")

# Fix corrupted em dashes
replacements = [
    ('â€"', '—'),
    ('â€"', '—'),
    ('â€"', '—'),
    ('â€”', '—'),
    ('â€“', '—'),
    ('â€˜', "'"),
    ('â€™', "'"),
    ('â€œ', '"'),
    ('â€', '"'),
    ('â€¦', '...'),
]

# Fix corrupted arrows
replacements.extend([
    ('â†'', '→'),
    ('â†'', '→'),
    ('â†'', '→'),
    ('â†"', '↓'),
])

# Fix corrupted checkmarks and symbols
replacements.extend([
    ('âœ“', '✓'),
    ('âœ"', '✓'),
    ('âœ—', '✗'),
    ('âœ¨', '✨'),
    ('âœˆï¸', '✈️'),
    ('âœˆ', '✈'),
])

# Fix corrupted emojis
replacements.extend([
    ('âš–ï¸', '⚖️'),
    ('âš–', '⚖'),
    ('âš¡', '⚡'),
    ('âš ï¸', '⚠️'),
    ('âš ', '⚠'),
    ('âš½', '⚽'),
    ('âš¾', '⚾'),
    ('â›ª', '⛪'),
    ('â›½', '⛽'),
    ('â™€ï¸', '♀️'),
    ('â™€', '♀'),
    ('â™‚ï¸', '♂️'),
    ('â™‚', '♂'),
    ('â™¿', '♿'),
    ('â™¥', '♥'),
    ('â™¦', '♦'),
    ('â™£', '♣'),
    ('â™ ', '♠'),
])

# Fix corrupted French accents
replacements.extend([
    ('Ã‰', 'É'),
    ('Ã©', 'é'),
    ('Ã¨', 'è'),
    ('Ãª', 'ê'),
    ('Ã«', 'ë'),
    ('Ã®', 'î'),
    ('Ã´', 'ô'),
    ('Ã»', 'û'),
    ('Ã ', 'à'),
    ('Ã§', 'ç'),
    ('Ã¹', 'ù'),
    ('Ã¢', 'â'),
    ('Ã¬', 'ì'),
    ('Ã²', 'ò'),
    ('Ã³', 'ó'),
])

# Fix corrupted copyright
replacements.extend([
    ('Â©', '©'),
    ('Â®', '®'),
    ('â„¢', '™'),
])

# Fix specific known issues
replacements.extend([
    ('sur les representants', 'sur les représentants'),
    ('d\'Ã‰lections Canada', 'd\'Élections Canada'),
    ('à â€"', 'à —'),
])

count = 0
for old, new in replacements:
    if old in content:
        found = content.count(old)
        content = content.replace(old, new)
        count += found
        print(f"Fixed {found} instances of '{old}' -> '{new}'")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal fixes applied: {count}")
print("Done!")