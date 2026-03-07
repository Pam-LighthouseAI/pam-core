import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all nameFr fields
namefr_pattern = r'nameFr:\s*"([^"]+)"'
matches = list(re.finditer(namefr_pattern, content))

# Common French words that should have accents
accent_issues = []

# Words that should have accents
checks = [
    ('Confidentialite', 'Confidentialité'),
    ('confidentialite', 'confidentialité'),
    ('donnee', 'donnée'),
    ('Donnee', 'Donnée'),
    ('privee', 'privée'),
    ('Privee', 'Privée'),
    ('Internet', 'Internet'),  # This one is correct
    ('federales', 'fédérales'),
    ('Federales', 'Fédérales'),
    ('provinciales', 'provinciales'),  # correct
    ('municipales', 'municipales'),  # correct
    ('elus', 'élus'),
    ('Elus', 'Élus'),
    ('electoraux', 'électoraux'),
    ('Electoraux', 'Électoraux'),
    ('education', 'éducation'),
    ('Education', 'Éducation'),
    ('sante', 'santé'),
    ('Sante', 'Santé'),
    ('securite', 'sécurité'),
    ('Securite', 'Sécurité'),
    ('environnement', 'environnement'),  # correct
    ('climat', 'climat'),  # correct
    ('transport', 'transport'),  # correct
    ('transports', 'transports'),  # correct
    ('logement', 'logement'),  # correct
    ('developpement', 'développement'),
    ('Developpement', 'Développement'),
    ('travail', 'travail'),  # correct
    ('emploi', 'emploi'),  # correct
    ('prestations', 'prestations'),  # correct
    ('impots', 'impôts'),
    ('Impots', 'Impôts'),
    ('citoyennete', 'citoyenneté'),
    ('Citoyennete', 'Citoyenneté'),
    ('consommateurs', 'consommateurs'),  # correct
    ('autochtones', 'autochtones'),  # correct
    ('aines', 'aînés'),
    ('Aines', 'Aînés'),
    ('vieillissement', 'vieillissement'),  # correct
    ('anciens', 'anciens'),  # correct
    ('combattants', 'combattants'),  # correct
    ('handicap', 'handicap'),  # correct
    ('accessibilite', 'accessibilité'),
    ('Accessibilite', 'Accessibilité'),
    ('etudiants', 'étudiants'),
    ('Etudiants', 'Étudiants'),
    ('agriculture', 'agriculture'),  # correct
    ('rural', 'rural'),  # correct
    ('services', 'services'),  # correct
    ('publics', 'publics'),  # correct
    ('famille', 'famille'),  # correct
    ('culture', 'culture'),  # correct
    ('femmes', 'femmes'),  # correct
    ('mentale', 'mentale'),  # correct
    ('toxicomanie', 'toxicomanie'),  # correct
    ('dependance', 'dépendance'),
    ('Dependance', 'Dépendance'),
    ('numeriques', 'numériques'),
    ('Numeriques', 'Numériques'),
    ('animal', 'animal'),  # correct
    ('loisirs', 'loisirs'),  # correct
    ('religion', 'religion'),  # correct
    ('foi', 'foi'),  # correct
    ('benevolat', 'bénévolat'),
    ('Benevolat', 'Bénévolat'),
    ('communaute', 'communauté'),
    ('Communaute', 'Communauté'),
    ('juridique', 'juridique'),  # correct
    ('retraite', 'retraite'),  # correct
    ('enfants', 'enfants'),  # correct
    ('alimentaire', 'alimentaire'),  # correct
    ('urgence', 'urgence'),  # correct
    ('personne', 'personne'),  # correct
    ('droits', 'droits'),  # correct
    ('eleves', 'élèves'),
    ('Eleves', 'Élèves'),
    ('francais', 'français'),
    ('Francais', 'Français'),
    ('anglais', 'anglais'),  # correct
    ('internet', 'internet'),  # correct
    ('large bande', 'large bande'),  # correct
    ('donnees', 'données'),
    ('Donnees', 'Données'),
    ('locales', 'locales'),  # correct
]

issues_found = []

for m in matches:
    name_fr = m.group(1)
    for wrong, correct in checks:
        if wrong in name_fr and correct not in name_fr:
            issues_found.append(f'nameFr: "{name_fr}" - contains "{wrong}", should be "{correct}"')

with open('accent_issues.txt', 'w', encoding='utf-8') as f:
    f.write(f'Checking {len(matches)} nameFr fields...\n\n')
    if issues_found:
        f.write('ISSUES FOUND:\n')
        for issue in issues_found:
            f.write(f'  {issue}\n')
    else:
        f.write('No accent issues found in nameFr fields!\n')