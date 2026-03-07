import re

# Read the file
with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Batch 4: Youth, Agriculture, Utilities, Family, Arts
translations = {
    # Youth
    "Canada Student Loans (federal) plus provincial loans. Apply through your province's student aid office": "Prêts canadiens aux étudiants (fédéral) plus prêts provinciaux. Postulez via le bureau d'aide financière aux étudiants de votre province",
    "Federal programs like Canada Summer Jobs and Youth Employment and Skills Strategy. Contact Employment and Social Development Canada": "Programmes fédéraux comme Emplois d'été Canada et Stratégie emploi jeunesse. Contactez Emploi et Développement social Canada",
    "Federal grant for low-income families' RESP. Up to $2,000 per child. Apply through financial institutions": "Subvention fédérale pour les REEE des familles à faible revenu. Jusqu'à 2 000 $ par enfant. Postulez via les institutions financières",
    "Federal apprenticeship incentives plus provincial trade certification. Contact ESDC for federal grants": "Incitatifs fédéraux d'apprentissage plus certification professionnelle provinciale. Contactez EDSC pour les subventions fédérales",
    "Provincial health ministries fund youth mental health services. Access through provincial health authorities and community clinics": "Les ministères provinciaux de la Santé financent les services de santé mentale pour les jeunes. Accédez via les autorités de santé provinciales et les cliniques communautaires",
    "Provincial youth justice system handles youth offenses. Federal Youth Criminal Justice Act sets framework": "Le système de justice pour les jeunes provincial traite les infractions des jeunes. La Loi sur le système de justice pénale pour les adolescents fédérale établit le cadre",
    "Provincial residential tenancy laws apply. Municipal bylaw enforcement for building standards": "Les lois provinciales sur la location résidentielle s'appliquent. Application des règlements municipaux pour les normes du bâtiment",
    
    # Agriculture
    "AgriStability and AgriInvest are federal-provincial programs. Apply through Agriculture and Agri-Food Canada or provincial agriculture ministry": "Agri-stabilité et Agri-investissement sont des programmes fédéraux-provinciaux. Postulez via Agriculture et Agroalimentaire Canada ou le ministère provincial de l'Agriculture",
    "Federal and provincial programs exist. Check AAFC and your provincial agriculture ministry for current funding opportunities": "Des programmes fédéraux et provinciaux existent. Consultez AAC et votre ministère provincial de l'Agriculture pour les possibilités de financement actuelles",
    "Federal Connect to Innovate program plus provincial broadband initiatives. Contact Innovation, Science and Economic Development Canada": "Programme fédéral Brancher les collectivités plus initiatives provinciales sur l'internet à large bande. Contactez Innovation, Sciences et Développement économique Canada",
    "Provincial occupational health and safety laws cover farms. Contact provincial labour or agriculture ministries": "Les lois provinciales sur la santé et sécurité au travail couvrent les fermes. Contactez les ministères provinciaux du Travail ou de l'Agriculture",
    "Provincial conservation authorities and agriculture ministries. Some federal programs through AAFC": "Autorités de conservation provinciales et ministères de l'Agriculture. Certains programmes fédéraux via AAC",
    "Provincial agricultural land commissions protect farmland. Municipal zoning also affects agricultural land use": "Les commissions provinciales des terres agricoles protègent les terres agricoles. Le zonage municipal affecte également l'utilisation des terres agricoles",
    
    # Utilities
    "CRTC handles complaints about internet and cable providers. File through Commission for Complaints for Telecom-television Services (CCTS) first": "Le CRTC traite les plaintes concernant les fournisseurs Internet et câble. Déposez via la Commission des plaintes relatives aux services de télécommunication-télévision (CCTS) d'abord",
    "Provincial energy boards regulate electricity rates. Contact your provincial utilities commission or energy ministry": "Les commissions provinciales de l'énergie réglementent les tarifs d'électricité. Contactez votre commission des services publics provinciale ou votre ministère de l'Énergie",
    "Provincial utilities commissions regulate gas distribution. Contact your provincial energy regulator": "Les commissions provinciales des services publics réglementent la distribution de gaz. Contactez votre régulateur provincial de l'énergie",
    "Municipal water departments handle billing. Contact your city's utility billing department for disputes": "Les services municipaux de l'eau gèrent la facturation. Contactez le service de facturation des services publics de votre ville pour les litiges",
    "CCTS (Commission for Complaints for Telecom-television Services) handles wireless and landline complaints. CRTC for regulatory issues": "La CCTS (Commission des plaintes relatives aux services de télécommunication-télévision) traite les plaintes sans fil et filaires. CRTC pour les questions réglementaires",
    "Provincial energy policies govern grid connection for solar. Contact your provincial energy ministry or local utility": "Les politiques énergétiques provinciales régissent le raccordement au réseau pour le solaire. Contactez votre ministère provincial de l'Énergie ou votre service public local",
    
    # Family
    "Provincial vital statistics issues licenses. Often obtained at municipal offices or Service Ontario locations": "Les statistiques de l'état civil provincial délivrent les licences. Souvent obtenues aux bureaux municipaux ou aux emplacements de Service Ontario",
    "Federal Divorce Act governs divorce. File through provincial superior courts. Federal Child Support Guidelines apply": "La Loi sur le divorce fédérale régit le divorce. Déposez via les cours supérieures provinciales. Les Lignes directrices fédérales sur les pensions alimentaires pour enfants s'appliquent",
    "Provincial family law acts govern custody for unmarried parents. Provincial family courts handle these matters": "Les lois provinciales sur la famille régissent la garde pour les parents non mariés. Les tribunaux de la famille provinciaux traitent ces questions",
    "Provincial maintenance enforcement programs collect and enforce support orders. Contact your provincial MEP": "Les programmes provinciaux d'exécution des obligations alimentaires perçoivent et font appliquer les ordonnances de soutien. Contactez votre PEM provincial",
    "Provincial family courts handle spousal support for unmarried couples. Federal Divorce Act for married couples divorcing": "Les tribunaux de la famille provinciaux traitent le soutien au conjoint pour les couples non mariés. La Loi sur le divorce fédérale pour les couples mariés qui divorcent",
    "Provincial family law acts govern property division. Provincial family courts handle division of assets": "Les lois provinciales sur la famille régissent le partage des biens. Les tribunaux de la famille provinciaux traitent le partage des actifs",
    "Provincial children's services ministries regulate adoptions. Private, public, and international adoptions all go through provincial systems": "Les ministères provinciaux des services à l'enfance réglementent les adoptions. Les adoptions privées, publiques et internationales passent toutes par les systèmes provinciaux",
    "Provincial child welfare agencies (CAS in Ontario) handle protection cases. Funded provincially but often delivered by independent agencies": "Les agences provinciales de bien-être de l'enfance (SPE en Ontario) traitent les cas de protection. Financées au niveau provincial mais souvent livrées par des agences indépendantes",
    
    # Arts
    "Federal arts funding body. Apply directly to Canada Council for grants to individual artists and organizations": "Organisme fédéral de financement des arts. Postulez directement au Conseil des Arts du Canada pour les subventions aux artistes individuels et aux organisations",
    "Federal department funding cultural programs, official languages, and heritage. Apply through Department of Canadian Heritage": "Ministère fédéral finançant les programmes culturels, les langues officielles et le patrimoine. Postulez via le ministère du Patrimoine canadien",
    "Ontario Arts Council, BC Arts Council, etc. Provincial funding for artists and arts organizations": "Conseil des arts de l'Ontario, Conseil des arts de la C.-B., etc. Financement provincial pour les artistes et les organisations artistiques",
    "Many cities offer arts and culture grants. Contact your municipal cultural services department": "De nombreuses villes offrent des subventions pour les arts et la culture. Contactez le service des affaires culturelles de votre municipalité",
    "Federal and provincial tax credits for film and TV production. Apply through CRA (federal) and provincial finance ministries": "Crédits d'impôt fédéraux et provinciaux pour la production cinématographique et télévisuelle. Postulez via l'ARC (fédéral) et les ministères provinciaux des Finances",
    "Provincial heritage acts protect historic buildings. Municipalities designate local heritage properties under provincial law": "Les lois provinciales sur le patrimoine protègent les bâtiments historiques. Les municipalités désignent les propriétés patrimoniales locales en vertu de la loi provinciale",
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