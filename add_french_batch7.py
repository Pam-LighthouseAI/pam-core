import re

# Read the file
with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Batch 7: Legal Aid, Pensions, Childcare, Food Security, Emergency Services, Human Rights
translations = {
    # Legal Aid
    "Provincial legal aid plans provide free lawyers for low-income people. Eligibility varies. Contact provincial legal aid office": "Les régimes provinciaux d'aide juridique fournissent des avocats gratuits pour les personnes à faible revenu. L'admissibilité varie. Contactez le bureau provincial de l'aide juridique",
    "Legal aid duty counsel available at courthouses for criminal and family matters. Free, no eligibility test. Ask at courthouse": "Avocat de service de l'aide juridique disponible dans les palais de justice pour les questions criminelles et familiales. Gratuit, aucun test d'admissibilité. Demandez au palais de justice",
    "Provincial legal aid covers some family law matters. Contact provincial legal aid office": "L'aide juridique provinciale couvre certaines questions de droit de la famille. Contactez le bureau provincial de l'aide juridique",
    "Provincial legal aid covers serious criminal charges. Duty counsel for first appearances. Contact provincial legal aid": "L'aide juridique provinciale couvre les accusations criminelles graves. Avocat de service pour les premières comparutions. Contactez l'aide juridique provinciale",
    "Legal aid covers some immigration matters, especially refugee claims. Coverage varies by province. Contact provincial legal aid": "L'aide juridique couvre certaines questions d'immigration, surtout les demandes d'asile. La couverture varie par province. Contactez l'aide juridique provinciale",
    "Legal aid rarely covers civil disputes. Some provinces have summary legal advice. Contact provincial legal aid or community legal clinic": "L'aide juridique couvre rarement les litiges civils. Certaines provinces ont des conseils juridiques sommaires. Contactez l'aide juridique provinciale ou la clinique juridique communautaire",
    "Community legal clinics provide free legal help. Often affiliated with legal aid. Contact provincial legal aid for clinic locations": "Les cliniques juridiques communautaires fournissent de l'aide juridique gratuite. Souvent affiliées à l'aide juridique. Contactez l'aide juridique provinciale pour les emplacements des cliniques",
    "Provincial justice ministries. Federal Department of Justice. Law societies have referral services. Contact provincial justice ministry": "Ministères provinciaux de la Justice. Ministère fédéral de la Justice. Les barreaux ont des services d'aiguillage. Contactez le ministère provincial de la Justice",
    
    # Pensions
    "Service Canada administers CPP. Apply for retirement pension, disability, survivor benefits. Contact Service Canada": "Service Canada administre le RPC. Postulez pour la pension de retraite, l'invalidité, les prestations de survivant. Contactez Service Canada",
    "Provincial pension standards acts (federal for federal sector). Contact provincial pension regulator or federal OSFI": "Lois provinciales sur les normes de pension (fédéral pour le secteur fédéral). Contactez le régulateur des pensions provincial ou le BSIF fédéral",
    "Provincial pension regulators handle disputes. Federal OSFI for federal sector. Contact provincial pension regulator": "Les régulateurs des pensions provinciaux traitent les litiges. BSIF fédéral pour le secteur fédéral. Contactez le régulateur des pensions provincial",
    "CRA administers registered plans. Contribution limits set federally. Contact CRA": "L'ARC administre les régimes enregistrés. Limites de contribution fixées au niveau fédéral. Contactez l'ARC",
    "Financial Consumer Agency of Canada has resources. Provincial securities commissions regulate advisors. Contact FCAC": "L'Agence de la consommation en matière financière du Canada a des ressources. Les commissions des valeurs mobilières provinciales réglementent les conseillers. Contactez l'ACFC",
    "Provincial family law divides pensions. Federal Pension Benefits Division Act for CPP. Contact family lawyer or provincial court": "Le droit de la famille provincial divise les pensions. Loi fédérale sur la division des prestations de pension pour le RPC. Contactez un avocat en droit de la famille ou le tribunal provincial",
    "Provincial pension rules govern LIRAs and LIFs. Federal for federal sector. Contact provincial pension regulator": "Les règles provinciales sur les pensions régissent les CRI et les FERR. Fédéral pour le secteur fédéral. Contactez le régulateur des pensions provincial",
    "Provincial adult protection laws. Banks have elder abuse protocols. Contact provincial seniors office or bank": "Lois provinciales de protection des adultes. Les banques ont des protocoles d'abus des aînés. Contactez le bureau des aînés provincial ou la banque",
    
    # Childcare
    "Provincial childcare systems. Federal funding through Canada-wide early learning and childcare. Contact provincial childcare ministry": "Systèmes provinciaux de garde d'enfants. Financement fédéral via l'apprentissage et la garde d'enfants pancanadiens. Contactez le ministère provincial de la Garde d'enfants",
    "Provincial subsidy programs for low-income families. Contact provincial childcare ministry or local childcare office": "Programmes de subvention provinciaux pour les familles à faible revenu. Contactez le ministère provincial de la Garde d'enfants ou le bureau local de la garde d'enfants",
    "Provincial licensing standards. Municipal inspection in some provinces. Contact provincial childcare licensing": "Normes provinciales de permis. Inspection municipale dans certaines provinces. Contactez les permis de garde d'enfants provinciaux",
    "Provincial rules on unlicensed care. Limits on number of children. Contact provincial childcare ministry": "Règles provinciales sur la garde non autorisée. Limites sur le nombre d'enfants. Contactez le ministère provincial de la Garde d'enfants",
    "School boards or municipal programs. Provincial funding. Contact school board or municipal recreation": "Conseils scolaires ou programmes municipaux. Financement provincial. Contactez le conseil scolaire ou les loisirs municipaux",
    "Provincial funding for wage enhancement. Contact provincial childcare ministry": "Financement provincial pour l'augmentation des salaires. Contactez le ministère provincial de la Garde d'enfants",
    "Provincial licensing bodies investigate complaints. Contact provincial childcare licensing": "Les organismes provinciaux de délivrance de permis enquêtent sur les plaintes. Contactez les permis de garde d'enfants provinciaux",
    "Provincial early years programs. Municipal family centres. Contact provincial early years office": "Programmes provinciaux de la petite enfance. Centres familiaux municipaux. Contactez le bureau provincial de la petite enfance",
    
    # Food Security
    "Food banks are community organizations. Contact local food bank or 211 for locations": "Les banques alimentaires sont des organisations communautaires. Contactez la banque alimentaire locale ou 211 pour les emplacements",
    "Provincial education ministries. Municipal programs in some cities. Contact school board or provincial education ministry": "Ministères provinciaux de l'Éducation. Programmes municipaux dans certaines villes. Contactez le conseil scolaire ou le ministère provincial de l'Éducation",
    "Provincial health authorities inspect restaurants. Municipal bylaws may apply. Contact provincial health authority or municipal bylaw": "Les autorités de santé provinciales inspectent les restaurants. Les règlements municipaux peuvent s'appliquer. Contactez l'autorité de santé provinciale ou les règlements municipaux",
    "Municipal parks departments manage community gardens. Contact municipal parks or community services": "Les services municipaux des parcs gèrent les jardins communautaires. Contactez les parcs municipaux ou les services communautaires",
    "Municipal planning affects food access. Some cities have food policy councils. Contact municipal planning or public health": "L'urbanisme municipal affecte l'accès à la nourriture. Certaines villes ont des conseils de politique alimentaire. Contactez l'urbanisme municipal ou la santé publique",
    "Nutrition North Canada subsidizes food in northern communities. Contact Indigenous Services Canada": "Nutrition Nord Canada subventionne la nourriture dans les communautés nordiques. Contactez Services aux Autochtones Canada",
    "Competition Bureau for anti-competitive practices. Provincial consumer protection. Contact Competition Bureau": "Bureau de la concurrence pour les pratiques anticoncurrentielles. Protection des consommateurs provinciale. Contactez le Bureau de la concurrence",
    "Provincial health and safety rules for food handling. Contact provincial health authority": "Règles provinciales de santé et sécurité pour la manipulation des aliments. Contactez l'autorité de santé provinciale",
    
    # Emergency Services
    "Provincial 911 acts. CRTC regulates telecommunications. Contact provincial emergency services or municipal 911 office": "Lois provinciales sur le 911. Le CRTC réglemente les télécommunications. Contactez les services d'urgence provinciaux ou le bureau 911 municipal",
    "Municipal fire departments. Provincial fire marshals investigate major fires. Contact municipal fire department": "Services d'incendie municipaux. Les commissaires au feu provinciaux enquêtent sur les incendies majeurs. Contactez le service d'incendie municipal",
    "Provincial health authorities fund paramedics. Municipal delivery in some provinces. Contact provincial health authority": "Les autorités de santé provinciales financent les paramédics. Livraison municipale dans certaines provinces. Contactez l'autorité de santé provinciale",
    "Provincial emergency management organizations. Federal Public Safety Canada coordinates nationally. Contact provincial EMO": "Organisations provinciales de gestion des urgences. Sécurité publique Canada coordonne au niveau national. Contactez l'OGU provincial",
    "Provincial emergency plans. Municipal emergency management. Contact provincial EMO or municipal emergency services": "Plans d'urgence provinciaux. Gestion des urgences municipale. Contactez l'OGU provincial ou les services d'urgence municipaux",
    "Provincial SAR for land. Federal Coast Guard for water. RCMP coordinates. Contact provincial EMO": "SAR provincial pour la terre. Garde côtière fédérale pour l'eau. La GRC coordonne. Contactez l'OGU provincial",
    "National Public Alerting System. Provincial alerting systems. Contact provincial EMO": "Système national d'alertes publiques. Systèmes d'alerte provinciaux. Contactez l'OGU provincial",
    "Municipal emergency shelters. Provincial funding for disaster relief. Contact municipal emergency services": "Refuges d'urgence municipaux. Financement provincial pour le secours aux sinistrés. Contactez les services d'urgence municipaux",
    
    # Human Rights
    "Provincial human rights tribunals handle most cases. Canadian Human Rights Commission for federal matters. Contact provincial commission": "Les tribunaux provinciaux des droits de la personne traitent la plupart des cas. Commission canadienne des droits de la personne pour les questions fédérales. Contactez la commission provinciale",
    "Criminal Code prohibits hate propaganda (federal). Provincial human rights codes. Contact police or human rights commission": "Le Code criminel interdit la propagande haineuse (fédéral). Codes provinciaux des droits de la personne. Contactez la police ou la commission des droits de la personne",
    "Provincial human rights codes. Federal Canada Labour Code for federal sector. Contact provincial human rights commission": "Codes provinciaux des droits de la personne. Code canadien du travail fédéral pour le secteur fédéral. Contactez la commission provinciale des droits de la personne",
    "Provincial human rights codes prohibit housing discrimination. Contact provincial human rights commission": "Les codes provinciaux des droits de la personne interdisent la discrimination en matière de logement. Contactez la commission provinciale des droits de la personne",
    "Provincial accessibility laws (AODA in Ontario). Federal Accessible Canada Act. Contact provincial accessibility office": "Lois provinciales sur l'accessibilité (LAPHO en Ontario). Loi canadienne sur l'accessibilité fédérale. Contactez le bureau provincial de l'accessibilité",
    "Official Languages Act (federal). Provincial language rights vary. Contact Office of Commissioner of Official Languages": "Loi sur les langues officielles (fédérale). Les droits linguistiques provinciaux varient. Contactez le Commissariat aux langues officielles",
    "Immigration and Refugee Board adjudicates claims. Canadian Charter applies. Contact IRB or refugee legal aid": "La Commission de l'immigration et du statut de réfugié juge les demandes. La Charte canadienne s'applique. Contactez la CISR ou l'aide juridique pour réfugiés",
    "Canada is signatory to UN treaties. Canadian Human Rights Commission. Contact Global Affairs Canada": "Le Canada est signataire des traités de l'ONU. Commission canadienne des droits de la personne. Contactez Affaires mondiales Canada",
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