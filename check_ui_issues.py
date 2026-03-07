import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check for remaining issues
issues = [
    ('Confidentialite', 'Confidentialite without accent'),
    ('A propos', 'A propos without accent'),
    ('Telephone', 'Telephone without accent'),
    ('Representation', 'Representation without accent'),
    ('Acune', 'Acune (should be Aucune)'),
    ('ca fonctionne', 'ca without cedilla'),
]

print('Checking for remaining issues:')
for term, desc in issues:
    if term in content:
        # Find context
        idx = content.find(term)
        start = max(0, idx - 20)
        end = min(len(content), idx + len(term) + 20)
        context = content[start:end]
        print(f'FOUND: {desc}')
        print(f'  Context: ...{context}...')
    else:
        print(f'OK: {desc}')