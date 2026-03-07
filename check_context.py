import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check each issue in context
issues_to_check = [
    (r'\beducation\b', 'education'),
    (r'\bEducation\b', 'Education'),
    (r'\bsecurite\b', 'securite'),
    (r'\bdonnees\b', 'donnees'),
    (r'\baccessibilite\b', 'accessibilite'),
    (r'\bdependances\b', 'dependances'),
    (r'\bimpots\b', 'impots'),
    (r'\bmatiere\b', 'matiere'),
    (r'\bbenevolat\b', 'benevolat'),
    (r'\bca\b', 'ca'),
    (r'\bcommunaute\b', 'communaute'),
    (r'\breserves\b', 'reserves'),
    (r'\bReserve\b', 'Reserve'),
    (r'\bnumerique\b', 'numerique'),
]

for pattern, name in issues_to_check:
    matches = list(re.finditer(pattern, content))
    print(f'\n=== {name} ({len(matches)} matches) ===')
    for m in matches[:3]:  # Show first 3 matches
        start = max(0, m.start() - 40)
        end = min(len(content), m.end() + 40)
        context = content[start:end]
        print(f'  ...{context}...')