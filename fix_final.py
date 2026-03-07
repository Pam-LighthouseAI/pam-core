#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} characters")

# Count and fix corrupted characters
fixes = {}

# Fix É (corrupted to just 'E' or missing)
fixes['Étape'] = content.count('Étape')
fixes['tape 1'] = content.count('tape 1')  # corrupted Étape
content = content.replace('tape 1', 'Étape 1')
content = content.replace('tape 2', 'Étape 2')
content = content.replace('tape 3', 'Étape 3')

# Fix Où (corrupted)
fixes['Où'] = content.count('Où')
fixes['O habitez'] = content.count('O habitez')  # corrupted Où
content = content.replace('O habitez-vous?', 'Où habitez-vous?')

# Fix other common French corruptions
content = content.replace('Quel est votre enjeu?', 'Quel est votre enjeu?')
content = content.replace('Voici qui peut vous aider', 'Voici qui peut vous aider')

# Fix corrupted icons
content = content.replace('icon:"âš–ï¸"', 'icon:"⚖️"')
content = content.replace('icon:"âš–"', 'icon:"⚖"')
content = content.replace('icon:"âœˆï¸"', 'icon:"✈️"')
content = content.replace('icon:"âš¡"', 'icon:"⚡"')
content = content.replace('icon:"â™€ï¸"', 'icon:"♀️"')
content = content.replace('icon:"â™€"', 'icon:"♀"')
content = content.replace('icon:"â™¿"', 'icon:"♿"')
content = content.replace('icon:"âš½"', 'icon:"⚽"')
content = content.replace('icon:"â›ª"', 'icon:"⛪"')

# Fix corrupted arrows in buttons
content = content.replace('â†'', '→')
content = content.replace('â†"', '→')

# Fix corrupted em dashes
content = content.replace('â€"', '—')
content = content.replace('â€"', '—')
content = content.replace('â€"', '—')

# Fix corrupted checkmarks
content = content.replace('âœ“', '✓')

# Fix siteExplain text
content = content.replace("we\\'ll help you reach", "we'll help you reach")
content = content.replace('â€"if you spot', '— if you spot')

# Fix footer copyright
content = content.replace('Â©', '©')

# Fix French accents that got corrupted
content = content.replace('Ã‰', 'É')
content = content.replace('Ã©', 'é')
content = content.replace('Ã¨', 'è')
content = content.replace('Ãª', 'ê')
content = content.replace('Ã«', 'ë')
content = content.replace('Ã®', 'î')
content = content.replace('Ã´', 'ô')
content = content.replace('Ã»', 'û')
content = content.replace('Ã ', 'à')
content = content.replace('Ã§', 'ç')
content = content.replace('Ã¹', 'ù')
content = content.replace('Ã¢', 'â')
content = content.replace('Ã¬', 'ì')
content = content.replace('Ã²', 'ò')
content = content.replace('Ã³', 'ó')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Encoding fixes applied!")
print(f"Fixed Étape occurrences: {fixes.get('Étape', 0)}")
print(f"Fixed Où occurrences: {fixes.get('Où', 0)}")