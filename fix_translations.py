import re

# Read the file
with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Add missing category translations to FR.categories
# Find the categories object and add missing entries
old_categories = '''categories: {
    infrastructure: "Infrastructure et transports",
    healthcare: "Soins de santé",
    education: "Éducation",
    housing: "Logement et développement",
    environment: "Environnement et climat",
    safety: "Sécurité publique et justice",
    employment: "Emploi et travail",
    social: "Services sociaux et prestations",
    taxes: "Impôts et finances",
    immigration: "Immigration et citoyenneté",
    consumer: "Droits des consommateurs",
    indigenous: "Affaires autochtones",
    seniors: "Aînés et vieillissement",
    veterans: "Anciens combattants",
    disability: "Handicap et accessibilité",
    youth: "Jeunesse et étudiants",
    agriculture: "Agriculture et milieu rural",
    utilities: "Services publics",
    family: "Droit de la famille",
    arts: "Arts et culture"
  },'''

new_categories = '''categories: {
    infrastructure: "Infrastructure et transports",
    healthcare: "Soins de santé",
    education: "Éducation",
    housing: "Logement et développement",
    environment: "Environnement et climat",
    safety: "Sécurité publique et justice",
    employment: "Emploi et travail",
    social: "Services sociaux et prestations",
    taxes: "Impôts et finances",
    immigration: "Immigration et citoyenneté",
    consumer: "Droits des consommateurs",
    indigenous: "Affaires autochtones",
    seniors: "Aînés et vieillissement",
    veterans: "Anciens combattants",
    disability: "Handicap et accessibilité",
    youth: "Jeunesse et étudiants",
    agriculture: "Agriculture et milieu rural",
    utilities: "Services publics",
    family: "Droit de la famille",
    arts: "Arts et culture",
    lgbtq: "Droits LGBTQ+",
    women: "Droits des femmes",
    mentalhealth: "Santé mentale",
    substance: "Toxicomanie et dépendance",
    transportation: "Transport",
    digital: "Droits numériques",
    animals: "Bien-être animal",
    sports: "Sports et loisirs",
    religion: "Religion et foi",
    volunteer: "Bénévolat et communauté",
    legalaid: "Aide juridique",
    pensions: "Pensions et retraite",
    childcare: "Garde d'enfants",
    food: "Sécurité alimentaire",
    emergency: "Services d'urgence",
    humanrights: "Droits de la personne"
  },'''

content = content.replace(old_categories, new_categories)

# Fix 2: Privacy section accents
privacy_fixes = [
    ('privacyTitle: "Confidentialite"', 'privacyTitle: "Confidentialité"'),
    ('privacyIntro: "Ma Voix Civique est un outil gratuit. Nous ne collectons aucune donnee. Votre vie privee est notre priorite."', 
     'privacyIntro: "Ma Voix Civique est un outil gratuit. Nous ne collectons aucune donnée. Votre vie privée est notre priorité."'),
    ('privacyData3: "Aucune donnee stockee sur nos serveurs"',
     'privacyData3: "Aucune donnée stockée sur nos serveurs"'),
    ('privacyNoDataTitle: "Ce qui arrive a vos donnees"',
     'privacyNoDataTitle: "Ce qui arrive à vos données"'),
    ('privacyNoData1: "Votre code postal sert uniquement a trouver vos representants"',
     'privacyNoData1: "Votre code postal sert uniquement à trouver vos représentants"'),
    ('privacyNoData2: "Vos brouillons sont stockes uniquement dans votre navigateur"',
     'privacyNoData2: "Vos brouillons sont stockés uniquement dans votre navigateur"'),
    ('privacyNoData3: "Tout est automatiquement supprime quand vous fermez cette page"',
     'privacyNoData3: "Tout est automatiquement supprimé quand vous fermez cette page"'),
    ('privacyStorageText: "Cet outil est gratuit, sans publicites, et sans collecte de donnees. Utilisez-le pour ameliorer votre communaute. Votre voix compte."',
     'privacyStorageText: "Cet outil est gratuit, sans publicités, et sans collecte de données. Utilisez-le pour améliorer votre communauté. Votre voix compte."'),
    ('privacyApiTitle: "Source des donnees"',
     'privacyApiTitle: "Source des données"'),
    ('privacyApiText: "Les donnees sur les representants proviennent de l\'API Represent d\'OpenNorth, une organisation a but non lucratif."',
     'privacyApiText: "Les données sur les représentants proviennent de l\'API Represent d\'OpenNorth, une organisation à but non lucratif."'),
]

for old, new in privacy_fixes:
    content = content.replace(old, new)

# Fix 3: About section accents
about_fixes = [
    ('aboutTitle: "A propos"', 'aboutTitle: "À propos"'),
    ('aboutIntro: "Ma Voix Civique Canada est un outil gratuit et a but non lucratif concu pour aider les citoyens canadiens a entrer en contact avec leurs representants elus."',
     'aboutIntro: "Ma Voix Civique Canada est un outil gratuit et à but non lucratif conçu pour aider les citoyens canadiens à entrer en contact avec leurs représentants élus."'),
    ('aboutMissionText: "Nous croyons que chaque citoyen merite de savoir qui represente ses interets et comment faire entendre sa voix. Notre mission est de simplifier le processus d\'engagement civique pour tous les Canadiens."',
     'aboutMissionText: "Nous croyons que chaque citoyen mérite de savoir qui représente ses intérêts et comment faire entendre sa voix. Notre mission est de simplifier le processus d\'engagement civique pour tous les Canadiens."'),
    ('aboutHowTitle: "Comment ca fonctionne"', 'aboutHowTitle: "Comment ça fonctionne"'),
    ('aboutHow1: "Entrez votre code postal ou votre ville pour trouver vos representants"',
     'aboutHow1: "Entrez votre code postal ou votre ville pour trouver vos représentants"'),
    ('aboutHow2: "Decrivez votre enjeu pour obtenir des conseils sur le bon niveau de gouvernement"',
     'aboutHow2: "Décrivez votre enjeu pour obtenir des conseils sur le bon niveau de gouvernement"'),
    ('aboutHow3: "Redigez une lettre personnelle avec notre modele"',
     'aboutHow3: "Rédigez une lettre personnelle avec notre modèle"'),
    ('aboutHow4: "Contactez vos representants directement par courriel ou par telephone"',
     'aboutHow4: "Contactez vos représentants directement par courriel ou par téléphone"'),
    ('aboutDataTitle: "Sources des donnees"', 'aboutDataTitle: "Sources des données"'),
    ('aboutDataText: "Les donnees sur les representants proviennent de l\'API Represent d\'OpenNorth, qui consolide les donnees d\'Elections Canada, des bureaux electoraux provinciaux et des sources municipales."',
     'aboutDataText: "Les données sur les représentants proviennent de l\'API Represent d\'OpenNorth, qui consolide les données d\'Élections Canada, des bureaux électoraux provinciaux et des sources municipales."'),
    ('aboutAccuracy: "Les donnees federales et provinciales sont generalement a jour. Les donnees municipales peuvent parfois etre obsoletes apres les elections locales."',
     'aboutAccuracy: "Les données fédérales et provinciales sont généralement à jour. Les données municipales peuvent parfois être obsolètes après les élections locales."'),
]

for old, new in about_fixes:
    content = content.replace(old, new)

# Write the fixed content
with open(r'D:\source_extracted\my_civic_voice.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Translations fixed successfully!")
print("- Added 16 missing category translations")
print("- Fixed accent issues in privacy section")
print("- Fixed accent issues in about section")