import re

# Read the file
with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Batch 5: LGBTQ+, Women's Rights, Mental Health, Substance Use
translations = {
    # LGBTQ+
    "Provincial human rights codes protect gender identity. Federal Canadian Human Rights Act also applies. Contact provincial human rights commission": "Les codes provinciaux des droits de la personne protègent l'identité de genre. La Loi canadienne sur les droits de la personne fédérale s'applique également. Contactez la commission provinciale des droits de la personne",
    "Federal criminal ban on conversion therapy. Report to police. Provincial health regulators may also discipline practitioners": "Interdiction criminelle fédérale de la thérapie de conversion. Signalez à la police. Les régulateurs de la santé provinciaux peuvent également discipliner les praticiens",
    "Provincial vital statistics handles name changes. Gender marker changes vary by province. Contact provincial registrar": "Les statistiques de l'état civil provincial gèrent les changements de nom. Les changements de marqueur de genre varient par province. Contactez le registraire provincial",
    "Provincial health plans cover some gender-affirming care. Coverage varies. Contact provincial health ministry or trans health programs": "Les régimes de santé provinciaux couvrent certains soins d'affirmation de genre. La couverture varie. Contactez le ministère provincial de la Santé ou les programmes de santé trans",
    "Provincial human rights tribunals handle most discrimination. Federal Canadian Human Rights Commission for federal matters": "Les tribunaux provinciaux des droits de la personne traitent la plupart des discriminations. Commission canadienne des droits de la personne fédérale pour les questions fédérales",
    "Provincial education and social services. Municipal community programs. School board GSAs protected by provincial law": "Éducation et services sociaux provinciaux. Programmes communautaires municipaux. Les alliances gays-hétéro des conseils scolaires sont protégées par la loi provinciale",
    "Provincial vital statistics and family law. All provinces recognize same-sex parents. Contact provincial vital statistics": "Statistiques de l'état civil provincial et droit de la famille. Toutes les provinces reconnaissent les parents de même sexe. Contactez les statistiques de l'état civil provincial",
    "Provincial long-term care standards. LTC homes must respect gender identity. Contact provincial LTC regulator": "Normes provinciales de soins de longue durée. Les centres de SLD doivent respecter l'identité de genre. Contactez le régulateur provincial des SLD",
    
    # Women's Rights
    "Provincial health plans cover abortion services. Federal government ensures access. Contact provincial health ministry for services": "Les régimes de santé provinciaux couvrent les services d'avortement. Le gouvernement fédéral assure l'accès. Contactez le ministère provincial de la Santé pour les services",
    "Federal Pay Equity Act for federal sector. Provincial pay equity laws for others. Contact provincial employment standards or federal Labour Program": "Loi fédérale sur l'équité salariale pour le secteur fédéral. Lois provinciales sur l'équité salariale pour les autres. Contactez les normes d'emploi provinciales ou le Programme du travail fédéral",
    "Provincial victim services and shelters. Municipal police. Federal funding through Women and Gender Equality Canada": "Services aux victimes et refuges provinciaux. Police municipale. Financement fédéral via Femmes et Égalité des genres Canada",
    "Provincial funding for shelters. Municipal bylaws may affect shelter locations. Contact provincial social services or local women's crisis line": "Financement provincial pour les refuges. Les règlements municipaux peuvent affecter les emplacements des refuges. Contactez les services sociaux provinciaux ou la ligne de crise locale pour femmes",
    "Federal EI provides maternity and parental benefits. Provincial employment standards protect job. Contact Service Canada": "L'assurance-emploi fédérale fournit les prestations de maternité et parentales. Les normes d'emploi provinciales protègent l'emploi. Contactez Service Canada",
    "Provincial childcare systems. Federal funding through Canada-wide early learning and childcare. Contact provincial childcare ministry": "Systèmes provinciaux de garde d'enfants. Financement fédéral via l'apprentissage et la garde d'enfants pancanadiens. Contactez le ministère provincial de la Garde d'enfants",
    "Elections Canada and provincial elections offices. Political parties have nomination processes. Equal Voice advocates for women in politics": "Élections Canada et les bureaux électoraux provinciaux. Les partis politiques ont des processus de nomination. Égale Voix défend les femmes en politique",
    "Provincial human rights codes and occupational health and safety. Federal Canada Labour Code for federal sector. Contact provincial labour board": "Codes provinciaux des droits de la personne et santé et sécurité au travail. Code canadien du travail fédéral pour le secteur fédéral. Contactez la commission du travail provinciale",
    
    # Mental Health
    "Provincial health plans cover psychiatric care. Community mental health clinics. Federal funding for specific programs. Contact provincial health authority": "Les régimes de santé provinciaux couvrent les soins psychiatriques. Cliniques de santé mentale communautaires. Financement fédéral pour des programmes spécifiques. Contactez l'autorité de santé provinciale",
    "Provincial health authorities fund crisis lines. 988 Suicide Prevention available nationally. Municipal programs may supplement": "Les autorités de santé provinciales financent les lignes de crise. 988 Prévention du suicide disponible nationalement. Les programmes municipaux peuvent compléter",
    "Provincial health plans cover psychiatrists. Psychologists and counselors often private pay. Some provincial programs offer free counseling": "Les régimes de santé provinciaux couvrent les psychiatres. Psychologues et conseillers souvent payants. Certains programmes provinciaux offrent du counseling gratuit",
    "Provincial occupational health and safety includes psychological safety. Federal Labour Code for federal sector. Contact provincial labour ministry": "La santé et sécurité au travail provinciale inclut la sécurité psychologique. Code canadien du travail fédéral pour le secteur fédéral. Contactez le ministère provincial du Travail",
    "Provincial child and youth mental health services. School-based programs. Contact provincial health authority or youth mental health programs": "Services provinciaux de santé mentale pour enfants et adolescents. Programmes en milieu scolaire. Contactez l'autorité de santé provinciale ou les programmes de santé mentale jeunesse",
    "Provincial health authorities provide addiction treatment. Some services free through health plan. Contact provincial addiction services": "Les autorités de santé provinciales fournissent le traitement de la toxicomanie. Certains services gratuits via le régime de santé. Contactez les services de toxicomanie provinciaux",
    "Provincial education ministries set standards. School boards deliver programs. Contact provincial education ministry or school board": "Les ministères provinciaux de l'Éducation établissent les normes. Les conseils scolaires livrent les programmes. Contactez le ministère provincial de l'Éducation ou le conseil scolaire",
    "Provincial mental health acts govern involuntary admission. Contact provincial mental health review board for rights information": "Les lois provinciales sur la santé mentale régissent l'admission involontaire. Contactez la commission de révision de la santé mentale provinciale pour les informations sur les droits",
    
    # Substance Use
    "Provincial health authorities fund treatment centers. Wait lists vary. Contact provincial addiction services or local health authority": "Les autorités de santé provinciales financent les centres de traitement. Les listes d'attente varient. Contactez les services de toxicomanie provinciaux ou l'autorité de santé locale",
    "Provincial health authorities fund supervised consumption sites and needle programs. Municipal public health delivers services": "Les autorités de santé provinciales financent les sites de consommation supervisée et les programmes d'aiguilles. La santé publique municipale livre les services",
    "Health Canada authorizes safe supply programs. Provincial health authorities implement. Currently limited programs": "Santé Canada autorise les programmes d'approvisionnement sécuritaire. Les autorités de santé provinciales mettent en œuvre. Programmes actuellement limités",
    "Federal funding through Substance Use and Addictions Program. Provincial health authorities deliver frontline services": "Financement fédéral via le Programme de consommation de substances et de dépendances. Les autorités de santé provinciales livrent les services de première ligne",
    "Provincial funding for recovery homes. Municipal zoning may affect locations. Contact provincial addiction services": "Financement provincial pour les maisons de rétablissement. Le zonage municipal peut affecter les emplacements. Contactez les services de toxicomanie provinciaux",
    "Provincial health authorities distribute free naloxone kits. Pharmacies in most provinces. Contact provincial health authority": "Les autorités de santé provinciales distribuent des trousses de naloxone gratuites. Pharmacies dans la plupart des provinces. Contactez l'autorité de santé provinciale",
    "Provincial education ministries set curriculum. School boards deliver prevention programs. Contact school board": "Les ministères provinciaux de l'Éducation établissent le programme. Les conseils scolaires livrent les programmes de prévention. Contactez le conseil scolaire",
    "Federal Controlled Drugs and Substances Act. Provincial role in health services. Contact federal Minister of Health": "Loi fédérale sur les drogues contrôlées et substances. Rôle provincial dans les services de santé. Contactez le ministre fédéral de la Santé",
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