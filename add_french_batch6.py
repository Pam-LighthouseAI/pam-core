import re

# Read the file
with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Batch 6: Transportation, Digital Rights, Animal Welfare, Sports, Religion, Volunteer
translations = {
    # Transportation
    "Municipal transit authorities operate systems. Provincial and federal funding programs. Contact your local transit agency": "Les autorités de transport en commun municipales exploitent les systèmes. Programmes de financement provinciaux et fédéraux. Contactez votre agence de transport locale",
    "Municipal transit authorities must meet accessibility standards. Provincial human rights codes apply. Contact transit accessibility office": "Les autorités de transport en commun municipales doivent respecter les normes d'accessibilité. Les codes provinciaux des droits de la personne s'appliquent. Contactez le bureau d'accessibilité du transport",
    "Provincial transportation ministries. Some municipal programs. Federal rural transit funding. Contact provincial ministry": "Ministères provinciaux des Transports. Certains programmes municipaux. Financement fédéral du transport rural. Contactez le ministère provincial",
    "Municipal transit authorities operate paratransit. Provincial accessibility laws require it. Contact local transit agency": "Les autorités de transport en commun municipales exploitent le paratransit. Les lois provinciales sur l'accessibilité l'exigent. Contactez l'agence de transport locale",
    "Municipal planning departments design bike lanes. Provincial funding programs may apply. Contact city transportation": "Les services municipaux de l'urbanisme conçoivent les pistes cyclables. Les programmes de financement provinciaux peuvent s'appliquer. Contactez le service des transports de la ville",
    "Municipal senior transportation programs. Provincial health may fund medical transport. Contact municipal senior services": "Programmes municipaux de transport pour aînés. La santé provinciale peut financer le transport médical. Contactez les services municipaux pour aînés",
    "Provincial education ministries regulate school buses. School boards contract services. Contact provincial ministry or school board": "Les ministères provinciaux de l'Éducation réglementent les autobus scolaires. Les conseils scolaires contractent les services. Contactez le ministère provincial ou le conseil scolaire",
    "Municipal bylaws license ride-sharing. Provincial insurance rules apply. Contact municipal licensing": "Les règlements municipaux autorisent le covoiturage. Les règles d'assurance provinciales s'appliquent. Contactez les licences municipales",
    
    # Digital Rights
    "PIPEDA (Personal Information Protection and Electronic Documents Act) governs private sector. Contact Office of Privacy Commissioner": "La LPRPDE (Loi sur la protection des renseignements personnels et les documents électroniques) régit le secteur privé. Contactez le Commissariat à la protection de la vie privée",
    "Organizations must report breaches under PIPEDA. Contact Office of Privacy Commissioner. Provincial laws may also apply": "Les organisations doivent signaler les violations en vertu de la LPRPDE. Contactez le Commissariat à la protection de la vie privée. Les lois provinciales peuvent également s'appliquer",
    "CRTC regulates internet services. File complaints about unfair practices through CCTS first": "Le CRTC réglemente les services Internet. Déposez les plaintes concernant les pratiques déloyales via la CCTS d'abord",
    "Provincial digital ID programs (BC Services Card, Ontario Digital ID). Contact provincial digital services": "Programmes provinciaux d'identité numérique (Carte de services de la C.-B., Identité numérique de l'Ontario). Contactez les services numériques provinciaux",
    "Criminal harassment laws (federal). Provincial cyberbullying laws. School board policies. Contact police or provincial cyberbullying unit": "Lois sur le harcèlement criminel (fédéral). Lois provinciales sur la cyberintimidation. Politiques des conseils scolaires. Contactez la police ou l'unité provinciale de cyberintimidation",
    "Canadian Anti-Fraud Centre collects reports. RCMP investigates. Contact CAFC and local police": "Le Centre antifraude du Canada recueille les rapports. La GRC enquête. Contactez le CAFC et la police locale",
    "Federal Online Harms Act (proposed). Current laws: criminal harassment, non-consensual sharing. Contact police for criminal matters": "Loi fédérale sur les méfaits en ligne (proposée). Lois actuelles : harcèlement criminel, partage non consenti. Contactez la police pour les questions criminelles",
    "Federal government developing AI legislation. Privacy Commissioner has guidance. Contact OPC for complaints": "Le gouvernement fédéral développe la législation sur l'IA. Le Commissariat à la protection de la vie privée a des directives. Contactez le CPVP pour les plaintes",
    
    # Animal Welfare
    "Provincial SPCAs and animal welfare acts. Federal Criminal Code for animal cruelty. Contact provincial SPCA or local police": "SPCA provinciaux et lois sur le bien-être animal. Code criminel fédéral pour la cruauté envers les animaux. Contactez le SPCA provincial ou la police locale",
    "Provincial wildlife acts protect most species. Federal Species at Risk Act for endangered species. Contact provincial wildlife ministry": "Les lois provinciales sur la faune protègent la plupart des espèces. Loi fédérale sur les espèces en péril pour les espèces menacées. Contactez le ministère provincial de la Faune",
    "Municipal bylaws regulate pets (limits, licensing, leashes). Contact municipal animal control or bylaw office": "Les règlements municipaux réglementent les animaux de compagnie (limites, permis, laisses). Contactez le contrôle animalier municipal ou le bureau des règlements",
    "Provincial animal welfare acts cover farm animals. National codes of practice (voluntary). Contact provincial agriculture ministry": "Les lois provinciales sur le bien-être animal couvrent les animaux de ferme. Codes nationaux de pratique (volontaires). Contactez le ministère provincial de l'Agriculture",
    "Provincial laws restrict exotic animals. Municipal bylaws may ban specific species. Contact provincial wildlife ministry": "Les lois provinciales restreignent les animaux exotiques. Les règlements municipaux peuvent interdire des espèces spécifiques. Contactez le ministère provincial de la Faune",
    "Municipal shelters or SPCAs. Provincial oversight varies. Contact local animal shelter or municipal animal services": "Refuges municipaux ou SPCA. La surveillance provinciale varie. Contactez le refuge pour animaux local ou les services animaliers municipaux",
    "Provincial human rights codes protect service animal access. Federal accessibility laws for federal sector. Contact provincial human rights commission": "Les codes provinciaux des droits de la personne protègent l'accès des animaux d'assistance. Lois fédérales sur l'accessibilité pour le secteur fédéral. Contactez la commission provinciale des droits de la personne",
    
    # Sports
    "Municipal recreation departments run community programs. Contact your city's recreation department": "Les services municipaux de loisirs gèrent les programmes communautaires. Contactez le service des loisirs de votre ville",
    "Municipalities operate arenas, pools, community centres. Provincial funding programs exist. Contact municipal recreation": "Les municipalités exploitent les arénas, piscines et centres communautaires. Des programmes de financement provinciaux existent. Contactez les loisirs municipaux",
    "Municipal programs and fields. Provincial sport organizations. School boards. Contact municipal recreation or provincial sport org": "Programmes et terrains municipaux. Organisations sportives provinciales. Conseils scolaires. Contactez les loisirs municipaux ou l'organisation sportive provinciale",
    "Sport Canada funds national sport organizations. Canadian Centre for Ethics in Sport. Safe Sport policies. Contact national sport organization": "Sport Canada finance les organisations sportives nationales. Centre canadien pour l'éthique dans le sport. Politiques de sport sécuritaire. Contactez l'organisation sportive nationale",
    "Sport Canada athlete assistance. Provincial sport funding programs. Contact provincial sport ministry": "Aide aux athlètes de Sport Canada. Programmes provinciaux de financement sportif. Contactez le ministère provincial des Sports",
    "Municipalities must provide accessible recreation. Provincial accessibility laws. Contact municipal recreation or accessibility office": "Les municipalités doivent fournir des loisirs accessibles. Lois provinciales sur l'accessibilité. Contactez les loisirs municipaux ou le bureau de l'accessibilité",
    "Provincial education ministries. School athletic associations. Contact school board or provincial sport association": "Ministères provinciaux de l'Éducation. Associations sportives scolaires. Contactez le conseil scolaire ou l'association sportive provinciale",
    
    # Religion
    "Canadian Charter of Rights and Freedoms protects religious freedom. Provincial human rights codes. Contact Canadian Human Rights Commission": "La Charte canadienne des droits et libertés protège la liberté religieuse. Codes provinciaux des droits de la personne. Contactez la Commission canadienne des droits de la personne",
    "Municipal zoning bylaws affect places of worship. Provincial human rights may apply. Contact municipal planning department": "Les règlements de zonage municipaux affectent les lieux de culte. Les droits de la personne provinciaux peuvent s'appliquer. Contactez le service municipal de l'urbanisme",
    "Provincial education acts. Catholic school boards constitutionally protected in some provinces. Independent schools regulated provincially": "Lois provinciales sur l'éducation. Conseils scolaires catholiques protégés constitutionnellement dans certaines provinces. Écoles indépendantes réglementées au niveau provincial",
    "Provincial human rights codes require accommodation. Federal Canada Labour Code for federal sector. Contact provincial human rights commission": "Les codes provinciaux des droits de la personne exigent l'accommodement. Code canadien du travail fédéral pour le secteur fédéral. Contactez la commission provinciale des droits de la personne",
    "Provincial laws on religious symbols vary. Quebec's Bill 21. Charter challenges ongoing. Contact provincial human rights commission": "Les lois provinciales sur les symboles religieux varient. Projet de loi 21 du Québec. Défis constitutionnels en cours. Contactez la commission provinciale des droits de la personne",
    "Faith organizations provide social services. Some provincial funding. Municipal partnerships. Contact provincial social services": "Les organisations confessionnelles fournissent des services sociaux. Certains financements provinciaux. Partenariats municipaux. Contactez les services sociaux provinciaux",
    "Municipal multiculturalism and interfaith programs. Contact municipal cultural services": "Programmes municipaux de multiculturalisme et interreligieux. Contactez les services culturels municipaux",
    
    # Volunteer
    "Municipal volunteer centres. Community organizations. Contact local volunteer centre or municipal community services": "Centres de bénévolat municipaux. Organisations communautaires. Contactez le centre de bénévolat local ou les services communautaires municipaux",
    "Provincial societies acts govern nonprofits. Municipal funding programs. Contact provincial society registry or municipal grants": "Les lois provinciales sur les sociétés régissent les organismes sans but lucratif. Programmes de financement municipaux. Contactez le registre des sociétés provincial ou les subventions municipales",
    "Municipal public participation programs. Provincial and federal consultations. Contact municipal clerk's office": "Programmes municipaux de participation publique. Consultations provinciales et fédérales. Contactez le bureau du greffier municipal",
    "Canada Revenue Agency registers charities. Provincial society incorporation required first. Contact CRA Charities Directorate": "L'Agence du revenu du Canada enregistre les organismes de bienfaisance. Incorporation provinciale requise d'abord. Contactez la Direction des organismes de bienfaisance de l'ARC",
    "Provincial liability laws protect volunteers. Contact provincial attorney general or volunteer organization": "Les lois provinciales sur la responsabilité protègent les bénévoles. Contactez le procureur général provincial ou l'organisation de bénévolat",
    "Municipal community grant programs. Provincial community funding. Federal programs like Canada Service Corps. Contact municipal grants office": "Programmes municipaux de subventions communautaires. Financement communautaire provincial. Programmes fédéraux comme le Corps de service canadien. Contactez le bureau des subventions municipales",
    "Provincial community grant programs. Federal funding through various departments. Contact provincial community services or federal programs": "Programmes provinciaux de subventions communautaires. Financement fédéral via divers ministères. Contactez les services communautaires provinciaux ou les programmes fédéraux",
}

# Count matches
count = 0
for eng, fr in translations.items():
    pattern = f'detail:"{re.escape(eng)}"'
    if re.search(pattern, content):
        count += 1

print(f"Found {count} matching detail texts")

# Apply translations
for eng_detail, fr_detail in translations.items():
    pattern = f'detail:"{re.escape(eng_detail)}"'
    replacement = f'detail:"{eng_detail}",detailFr:"{fr_detail}"'
    content = re.sub(pattern, replacement, content)

# Write back
with open(r'D:\source_extracted\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Count result
new_count = content.count('detailFr:')
print(f"Total detailFr fields after update: {new_count}")