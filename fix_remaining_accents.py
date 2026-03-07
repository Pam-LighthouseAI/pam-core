import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix French content accents only (not English text or URLs)
# These are in French strings (nameFr, subjectFr, labelFr, etc.)

fixes = [
    # In nameFr fields
    ('nameFr:"ducation dans le', 'nameFr:"Éducation dans les réserves",'),  # Fix the full string
    ('nameFr:"Questions foncieres des reserves",', 'nameFr:"Questions foncières des réserves",'),
    ('nameFr:"Identite numerique",', 'nameFr:"Identité numérique",'),
    
    # In subjectFr fields
    ('subjectFr: "Preoccupation concernant la securite publique', 'subjectFr: "Préoccupation concernant la sécurité publique'),
    ('subjectFr: "Preoccupation concernant la securite alimentaire', 'subjectFr: "Préoccupation concernant la sécurité alimentaire'),
    ('subjectFr: "Preoccupation concernant l\'accessibilite et le handicap', 'subjectFr: "Préoccupation concernant l\'accessibilité et le handicap'),
    ('subjectFr: "Preoccupation concernant l\'usage de substances et les dependances', 'subjectFr: "Préoccupation concernant l\'usage de substances et les dépendances'),
    ('subjectFr: "Preoccupation concernant les impots et les finances', 'subjectFr: "Préoccupation concernant les impôts et les finances'),
    ('subjectFr: "Preoccupation concernant le benevolat et la communaute', 'subjectFr: "Préoccupation concernant le bénévolat et la communauté'),
    
    # In French text
    ('Attribution des donnees",', 'Attribution des données",'),
    ('Les donnees sur', 'Les données sur'),
    ('les donnees gouvernementales', 'les données gouvernementales'),
    
    # matiere -> matière
    ('en matiere d\'immigration"', 'en matière d\'immigration"'),
    ('en matiere de vie prive"', 'en matière de vie privée"'),
    ('en matiere familiale"', 'en matière familiale"'),
    
    # labelFr fixes
    ('labelFr:"ducation",', 'labelFr:"Éducation",'),
    
    # Preoccupation -> Préoccupation (in French text)
    ('Preoccupation concernant', 'Préoccupation concernant'),
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