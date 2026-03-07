import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# All the accent fixes needed
accent_fixes = [
    # securite → sécurité
    ('securite pietonne', 'sécurité piétonne'),
    ('Securite au travail', 'Sécurité au travail'),
    ('Securite des produits', 'Sécurité des produits'),
    ('Securite de la vieillesse', 'Sécurité de la vieillesse'),
    ('Securite a la ferme', 'Sécurité à la ferme'),
    ('Securite des autobus', 'Sécurité des autobus'),
    ('Securite alimentaire', 'Sécurité alimentaire'),
    
    # sante → santé
    ('sante mentale', 'santé mentale'),
    ('Sante mentale', 'Santé mentale'),
    ('sante trans', 'santé trans'),
    ('soins de sante', 'soins de santé'),
    ('Avantages de sante', 'Avantages de santé'),
    
    # Education → Éducation
    ('Education specialisee', 'Éducation spécialisée'),
    ('Education autochtone', 'Éducation autochtone'),
    ('Education dans les reserves', 'Éducation dans les réserves'),
    
    # Impots → Impôts
    ('Impots fonciers', 'Impôts fonciers'),
    ('impots fonciers', 'impôts fonciers'),
    
    # aines → aînés
    ('pour aines', 'pour aînés'),
    ('les aines', 'les aînés'),
    ('des aines', 'des aînés'),
    ('envers les aines', 'envers les aînés'),
    
    # citoyennete → citoyenneté
    ('citoyennete', 'citoyenneté'),
    
    # privee → privée
    ('vie privee', 'vie privée'),
    
    # donnees → données
    ('Violations de donnees', 'Violations de données'),
    
    # accessibilite → accessibilité
    ("matiere d'accessibilite", "matière d'accessibilité"),
    ('Accessibilite du transport', 'Accessibilité du transport'),
    ("Droits a l'accessibilite", "Droits à l'accessibilité"),
    
    # etudiants → étudiants
    ('Prets etudiants', 'Prêts étudiants'),
    
    # dependance → dépendance
    ('des dependances', 'des dépendances'),
    ('Traitement des dependances', 'Traitement des dépendances'),
    ('Centres de traitement des dependances', 'Centres de traitement des dépendances'),
    
    # benevolat → bénévolat
    ('Possibilites de benevolat', 'Possibilités de bénévolat'),
    
    # Confidentialite → Confidentialité
    ('Confidentialite sur Internet', 'Confidentialité sur Internet'),
]

# Apply all fixes
fixes_applied = 0
for wrong, correct in accent_fixes:
    if wrong in content:
        content = content.replace(wrong, correct)
        fixes_applied += 1
        print(f'Fixed: "{wrong}" -> "{correct}"')

# Write the fixed content
with open(r'D:\source_extracted\my_civic_voice.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nTotal fixes applied: {fixes_applied}')