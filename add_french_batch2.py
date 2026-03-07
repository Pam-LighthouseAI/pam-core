import re

# Read the file
with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Batch 2: Safety, Employment, Social Services, Taxes
translations = {
    # Safety
    "Municipal police services boards for local police. Provincial oversight for provincial police (OPP, SQ)": "Commissions des services policiers municipaux pour la police locale. Surveillance provinciale pour la police provinciale (OPP, SQ)",
    "Provincial courts handle most matters. Federal courts for federal issues. Provincial attorney general oversees courts": "Les tribunaux provinciaux traitent la plupart des affaires. Tribunaux fédéraux pour les questions fédérales. Le procureur général provincial supervise les tribunaux",
    "Provincial jails for sentences under 2 years. Federal penitentiaries for longer sentences": "Prisons provinciales pour les peines de moins de 2 ans. Pénitenciers fédéraux pour les peines plus longues",
    "Municipal fire departments. Provincial fire marshals investigate major incidents": "Services d'incendie municipaux. Les commissaires au feu provinciaux enquêtent sur les incidents majeurs",
    "Provincial emergency management organizations. Federal Public Safety Canada coordinates nationally": "Organisations provinciales de gestion des urgences. Sécurité publique Canada coordonne au niveau national",
    "Provincial victim services programs. Contact provincial attorney general or justice ministry": "Programmes provinciaux de services aux victimes. Contactez le procureur général provincial ou le ministère de la Justice",
    "Provincial legal aid plans provide services. Contact provincial legal aid office": "Les régimes provinciaux d'aide juridique fournissent des services. Contactez le bureau provincial de l'aide juridique",
    "Municipal bylaw officers enforce local bylaws. Contact city hall or 311": "Les agents municipaux de réglementation appliquent les règlements locaux. Contactez l'hôtel de ville ou le 311",
    
    # Employment
    "Provincial employment standards acts for most workers. Federal Canada Labour Code for federal sector": "Lois provinciales sur les normes d'emploi pour la plupart des travailleurs. Code canadien du travail fédéral pour le secteur fédéral",
    "Service Canada administers EI. Apply online or at Service Canada centres": "Service Canada administre l'assurance-emploi. Postulez en ligne ou dans les centres Service Canada",
    "Provincial workers compensation boards. WSIB in Ontario, WCB in other provinces": "Commissions provinciales d'indemnisation des travailleurs. WSIB en Ontario, WCB dans les autres provinces",
    "Provincial labour relations acts for most. Federal for federal sector and interprovincial industries": "Lois provinciales sur les relations de travail pour la plupart. Fédéral pour le secteur fédéral et les industries interprovinciales",
    "Provincial human rights commissions and labour boards. Occupational health and safety also applies": "Commissions provinciales des droits de la personne et commissions du travail. Santé et sécurité au travail s'applique également",
    "Federal EI provides benefits. Provincial employment standards protect job": "L'assurance-emploi fédérale fournit les prestations. Les normes d'emploi provinciales protègent l'emploi",
    "Immigration, Refugees and Citizenship Canada administers. Employment and Social Development Canada for LMIA": "Immigration, Réfugiés et Citoyenneté Canada administre. Emploi et Développement social Canada pour les EIMT",
    "Provincial trades colleges and apprenticeship authorities. Red Seal for interprovincial standards": "Collèges de métiers provinciaux et autorités d'apprentissage. Sceau rouge pour les normes interprovinciales",
    
    # Social Services
    "Provincial social assistance programs. Ontario Works, BC Income Assistance, etc. Contact provincial social services": "Programmes provinciaux d'aide sociale. Ontario Works, aide au revenu de la C.-B., etc. Contactez les services sociaux provinciaux",
    "Canada Child Benefit (federal). Provincial child benefits vary by province. Apply through CRA and provincial programs": "Allocation canadienne pour enfants (fédérale). Les prestations provinciales pour enfants varient par province. Postulez via l'ARC et les programmes provinciaux",
    "Provincial disability support programs (ODSP, AISH, PWD). Federal CPP-D and Disability Tax Credit": "Programmes provinciaux de soutien aux personnes handicapées (ODSP, AISH, PWD). RPC-I et crédit d'impôt pour personnes handicapées fédéraux",
    "Service Canada administers Old Age Security and Guaranteed Income Supplement": "Service Canada administre la Sécurité de la vieillesse et le Supplément de revenu garanti",
    "Provincial child welfare agencies. Children's Aid Societies in Ontario. Contact provincial ministry for complaints": "Agences provinciales de bien-être de l'enfance. Sociétés d'aide à l'enfance en Ontario. Contactez le ministère provincial pour les plaintes",
    "Municipal social services often coordinate. Community organizations deliver services": "Les services sociaux municipaux coordonnent souvent. Les organisations communautaires livrent les services",
    "Municipal housing departments administer subsidies. Provincial and federal funding": "Les services municipaux du logement administrent les subventions. Financement provincial et fédéral",
    "Immigration, Refugees and Citizenship Canada funds settlement services. Provincial programs also exist": "Immigration, Réfugiés et Citoyenneté Canada finance les services d'établissement. Les programmes provinciaux existent également",
    
    # Taxes
    "Canada Revenue Agency administers federal and provincial income taxes (except Quebec). Revenu Quebec for Quebec": "L'Agence du revenu du Canada administre les impôts fédéraux et provinciaux (sauf Québec). Revenu Québec pour le Québec",
    "Provincial assessment agencies determine values. Municipalities set rates and collect": "Les agences provinciales d'évaluation déterminent les valeurs. Les municipalités fixent les taux et perçoivent",
    "CRA administers GST and HST. Provincial programs for separate PST (BC, Saskatchewan, Manitoba)": "L'ARC administre la TPS et la TVH. Programmes provinciaux pour la TVP distincte (C.-B., Saskatchewan, Manitoba)",
    "CRA administers federal and most provincial corporate taxes. Revenu Quebec for Quebec": "L'ARC administre les impôts fédéraux et la plupart des impôts des sociétés provinciaux. Revenu Québec pour le Québec",
    "Tax Court of Canada and CRA appeals process. Provincial tax tribunals for provincial matters": "Cour canadienne de l'impôt et processus d'appel de l'ARC. Tribunaux fiscaux provinciaux pour les questions provinciales",
    "Federal carbon pricing with rebate. Provincial systems in some provinces. CRA administers rebate": "Tarification fédérale du carbone avec remboursement. Systèmes provinciaux dans certaines provinces. L'ARC administre le remboursement",
    "CRA administers most credits. Provincial credits on provincial tax returns": "L'ARC administre la plupart des crédits. Crédits provinciaux sur les déclarations d'impôt provinciales",
    "Financial Consumer Agency of Canada. Provincial securities commissions for investments": "Agence de la consommation en matière financière du Canada. Commissions des valeurs mobilières provinciales pour les investissements",
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