import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all nameFr, subjectFr, labelFr, detailFr, bodyFr fields and check for missing accents
patterns = [
    (r'nameFr:"([^"]+)"', 'nameFr'),
    (r'subjectFr:\s*"([^"]+)"', 'subjectFr'),
    (r'labelFr:"([^"]+)"', 'labelFr'),
    (r'detailFr:"([^"]+)"', 'detailFr'),
    (r'bodyFr:\s*"([^"]+)"', 'bodyFr'),
]

# French words that should have accents (wrong -> correct)
accent_issues = [
    ('education', 'éducation'),
    ('Education', 'Éducation'),
    ('ecole', 'école'),
    ('Ecole', 'École'),
    ('ecoles', 'écoles'),
    ('Ecoles', 'Écoles'),
    ('preoccupation', 'préoccupation'),
    ('Preoccupation', 'Préoccupation'),
    ('securite', 'sécurité'),
    ('Securite', 'Sécurité'),
    ('sante', 'santé'),
    ('Sante', 'Santé'),
    ("a l'ecole", "à l'école"),
    ("a l'ecole", "à l'école"),
]

issues_found = []

for pattern, field_name in patterns:
    matches = re.finditer(pattern, content)
    for m in matches:
        value = m.group(1)
        for wrong, correct in accent_issues:
            if wrong in value:
                issues_found.append(f'{field_name}: "{value}" - found "{wrong}" should be "{correct}"')

if issues_found:
    print('ISSUES FOUND:')
    for issue in issues_found[:20]:  # Show first 20
        print(f'  {issue}')
    print(f'\nTotal: {len(issues_found)} issues')
else:
    print('NO ACCENT ISSUES FOUND IN FRENCH CONTENT!')