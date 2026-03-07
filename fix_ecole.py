import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix remaining ecole/ecoles issues
fixes = [
    ("Fermetures et consolidations d'ecoles", "Fermetures et consolidations d'écoles"),
    ("Garde avant/apres l'ecole", "Garde avant/après l'école"),
]

fixes_applied = 0
for wrong, correct in fixes:
    if wrong in content:
        content = content.replace(wrong, correct)
        fixes_applied += 1

# Write the fixed content
with open(r'D:\source_extracted\my_civic_voice.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Total fixes applied: {fixes_applied}')