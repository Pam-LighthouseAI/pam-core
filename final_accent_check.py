import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Common French words that should have accents
# Format: (wrong, correct, context_pattern)
accent_checks = [
    # e -> é/è/ê
    (r'\beleve\b', 'élève', 'student'),
    (r'\beleves\b', 'élèves', 'students'),
    (r'\beducation\b', 'éducation', 'education'),
    (r'\bEducation\b', 'Éducation', 'Education'),
    (r'\bsante\b', 'santé', 'health'),
    (r'\bSante\b', 'Santé', 'Health'),
    (r'\bsecurite\b', 'sécurité', 'security'),
    (r'\bSecurite\b', 'Sécurité', 'Security'),
    (r'\bprivee?\b', 'privée', 'private'),
    (r'\bPrivee?\b', 'Privée', 'Private'),
    (r'\bdonnees?\b', 'données', 'data'),
    (r'\bDonnees?\b', 'Données', 'Data'),
    (r'\baccessibilite\b', 'accessibilité', 'accessibility'),
    (r'\bAccessibilite\b', 'Accessibilité', 'Accessibility'),
    (r'\bdeveloppement\b', 'développement', 'development'),
    (r'\bDeveloppement\b', 'Développement', 'Development'),
    (r'\bdependances?\b', 'dépendances', 'dependencies'),
    (r'\bDependances?\b', 'Dépendances', 'Dependencies'),
    (r'\bimpots\b', 'impôts', 'taxes'),
    (r'\bImpots\b', 'Impôts', 'Taxes'),
    (r'\bcitoyennete\b', 'citoyenneté', 'citizenship'),
    (r'\bCitoyennete\b', 'Citoyenneté', 'Citizenship'),
    
    # a -> à/â
    (r'\bA propos\b', 'À propos', 'About'),
    (r'\bA la\b', 'À la', 'To the'),
    
    # e -> ê
    (r'\bmatiere\b', 'matière', 'matter'),
    (r'\bMatiere\b', 'Matière', 'Matter'),
    
    # i -> î
    (r'\bConfidentialite\b', 'Confidentialité', 'Privacy'),
    
    # u -> û
    (r'\bbenevolat\b', 'bénévolat', 'volunteering'),
    (r'\bBenevolat\b', 'Bénévolat', 'Volunteering'),
    
    # c -> ç
    (r'\bca\b', 'ça', 'it/that'),
    (r'\bfrancais\b', 'français', 'French'),
    (r'\bFrancais\b', 'Français', 'French'),
    
    # a -> â
    (r'\baines\b', 'aînés', 'seniors'),
    (r'\bAines\b', 'Aînés', 'Seniors'),
    
    # e -> é
    (r'\bcommunaute\b', 'communauté', 'community'),
    (r'\bCommunaute\b', 'Communauté', 'Community'),
    (r'\bspecialisee?\b', 'spécialisée', 'specialized'),
    (r'\bSpecialisee?\b', 'Spécialisée', 'Specialized'),
    (r'\breserve?s?\b', 'réserve', 'reserve'),
    (r'\bReserve?s?\b', 'Réserve', 'Reserve'),
    (r'\bnumeriqe?u?es?\b', 'numériques', 'digital'),
    (r'\bNumeriqe?u?es?\b', 'Numériques', 'Digital'),
    (r'\bprets\b', 'prêts', 'loans'),
    (r'\bPrets\b', 'Prêts', 'Loans'),
    
    # a -> à
    (r'\bDroits a\b', 'Droits à', 'Rights to'),
    (r'\bSecurite a\b', 'Sécurité à', 'Security to'),
]

print('=== COMPREHENSIVE FRENCH ACCENT CHECK ===\n')

issues_found = []

for pattern, correct, context in accent_checks:
    matches = re.findall(pattern, content)
    if matches:
        issues_found.append(f'FOUND: "{matches[0]}" should be "{correct}" ({context})')

if issues_found:
    print('ISSUES FOUND:')
    for issue in issues_found:
        print(f'  {issue}')
else:
    print('NO ACCENT ISSUES FOUND!')

# Also check for specific known issues from Kevin's report
print('\n=== CHECKING SPECIFIC ISSUES FROM KEVIN\'S REPORT ===\n')

specific_checks = [
    ('Confidentialite', 'Confidentialité'),
    ('Confidentialité', 'Already correct'),
    ('A propos', 'À propos'),
    ('À propos', 'Already correct'),
    ('Telephone', 'Téléphone'),
    ('Téléphone', 'Already correct'),
    ('Representation', 'Représentation'),
    ('Représentation', 'Already correct'),
]

for term, expected in specific_checks:
    if 'Already correct' in expected:
        if term in content:
            print(f'OK: "{term}" is present (correct)')
        else:
            print(f'MISSING: "{term}" should be present')
    else:
        if term in content:
            print(f'ISSUE: "{term}" should be "{expected}"')
        else:
            print(f'OK: "{term}" not found (already fixed)')