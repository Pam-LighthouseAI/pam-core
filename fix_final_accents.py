import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix remaining accent issues
fixes = [
    # subjectFr missing accent
    ('subjectFr: "Préoccupation concernant l\'education :', 'subjectFr: "Préoccupation concernant l\'éducation :'),
    
    # nameFr Ecoles -> Écoles
    ('nameFr:"Ecoles primaires', 'nameFr:"Écoles primaires'),
    ('nameFr:"Ecoles confessionnelles', 'nameFr:"Écoles confessionnelles'),
    
    # Preoccupations -> Préoccupations
    ('nameFr:"Preoccupations concernant', 'nameFr:"Préoccupations concernant'),
    
    # a l'ecole -> à l'école
    ('Santé mentale a l\'ecole"', 'Santé mentale à l\'école"'),
    ('Consommation de substances a l\'ecole"', 'Consommation de substances à l\'école"'),
    
    # Other missing accents in French content
    ('nameFr:"Questions foncieres des reserves",', 'nameFr:"Questions foncières des réserves",'),
    ('nameFr:"Identite numerique",', 'nameFr:"Identité numérique",'),
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