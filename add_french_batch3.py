import re

# Read the file
with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Batch 3: Immigration, Consumer, Indigenous, Seniors, Veterans, Disability
translations = {
    # Immigration
    "Immigration, Refugees and Citizenship Canada processes all PR applications. Apply online through IRCC portal": "Immigration, Réfugiés et Citoyenneté Canada traite toutes les demandes de RP. Postulez en ligne via le portail d'IRCC",
    "IRCC processes work permits. Some need LMIA from Employment and Social Development Canada first": "IRCC traite les permis de travail. Certains ont besoin d'une EIMT d'Emploi et Développement social Canada d'abord",
    "IRCC processes study permits. Provincial attestation may be required (PAL)": "IRCC traite les permis d'études. Une attestation provinciale peut être requise (PAL)",
    "IRCC processes sponsorship applications. Sponsor must meet income requirements": "IRCC traite les demandes de parrainage. Le répondant doit répondre aux exigences de revenu",
    "Immigration and Refugee Board adjudicates claims. IRCC processes resettled refugees": "La Commission de l'immigration et du statut de réfugié juge les demandes. IRCC traite les réfugiés réinstallés",
    "IRCC processes citizenship applications. Must meet residency and other requirements": "IRCC traite les demandes de citoyenneté. Doit répondre aux exigences de résidence et autres",
    "IRCC processes visitor visas and eTAs. Apply online through IRCC portal": "IRCC traite les visas de visiteur et les AVE. Postulez en ligne via le portail d'IRCC",
    "Canada Border Services Agency detains. Immigration Division of IRB reviews detention": "L'Agence des services frontaliers du Canada détient. La Division de l'immigration de la CISR révise la détention",
    
    # Consumer
    "Provincial consumer protection acts. Contact provincial consumer affairs ministry or consumer protection office": "Lois provinciales de protection des consommateurs. Contactez le ministère provincial des affaires des consommateurs ou le bureau de la protection du consommateur",
    "Office of Privacy Commissioner of Canada for federal private sector. Provincial commissioners for provincial matters": "Commissariat à la protection de la vie privée du Canada pour le secteur privé fédéral. Commissaires provinciaux pour les questions provinciales",
    "CRTC regulates. File complaints with Commission for Complaints for Telecom-television Services (CCTS)": "Le CRTC réglemente. Déposez les plaintes auprès de la Commission des plaintes relatives aux services de télécommunication-télévision (CCTS)",
    "Financial Consumer Agency of Canada. Banking Ombudsman for specific bank complaints": "Agence de la consommation en matière financière du Canada. Ombudsman bancaire pour les plaintes spécifiques aux banques",
    "Health Canada for consumer products. Provincial health authorities also have jurisdiction": "Santé Canada pour les produits de consommation. Les autorités de santé provinciales ont également juridiction",
    "Provincial consumer protection acts prohibit false advertising. Competition Act (federal) also applies": "Les lois provinciales de protection des consommateurs interdisent la publicité mensongère. La Loi sur la concurrence (fédérale) s'applique également",
    "Provincial consumer protection acts set warranty rules. Provincial consumer tribunals handle disputes": "Les lois provinciales de protection des consommateurs établissent les règles de garantie. Les tribunaux des consommateurs provinciaux traitent les litiges",
    "Office of Privacy Commissioner of Canada. PIPEDA requires notification of breaches": "Commissariat à la protection de la vie privée du Canada. La LPRPDE exige la notification des violations",
    
    # Indigenous
    "Indigenous Services Canada processes status cards. Indian Register maintained by ISC": "Services aux Autochtones Canada traite les cartes de statut. Registre des Indiens maintenu par SAC",
    "Band councils are elected governments under Indian Act. ISC oversees elections process": "Les conseils de bande sont des gouvernements élus en vertu de la Loi sur les Indiens. SAC supervise le processus électoral",
    "Crown-Indigenous Relations and Northern Affairs handles treaties. Provincial obligations also apply": "Relations Couronne-Autochtones et Affaires du Nord gère les traités. Les obligations provinciales s'appliquent également",
    "Indigenous Services Canada manages reserve lands. Band councils have increasing control under self-government": "Services aux Autochtones Canada gère les terres de réserve. Les conseils de bande ont un contrôle croissant en vertu de l'autonomie gouvernementale",
    "Provincial child welfare laws apply but Indigenous communities have right to self-govern. Federal Indigenous child welfare law": "Les lois provinciales sur le bien-être de l'enfance s'appliquent mais les communautés autochtones ont le droit à l'autonomie gouvernementale. Loi fédérale sur le bien-être de l'enfance autochtone",
    "Indigenous Services Canada administers NIHB for First Nations and Inuit": "Services aux Autochtones Canada administre le Programme des services de santé non assurés pour les Premières Nations et les Inuits",
    "Indigenous Services Canada funds education. Many communities have taken control of education": "Services aux Autochtones Canada finance l'éducation. De nombreuses communautés ont pris le contrôle de l'éducation",
    "National inquiry completed. Contact MMIWG support services. RCMP for criminal matters": "Enquête nationale terminée. Contactez les services de soutien aux femmes autochtones disparues et assassinées. GRC pour les questions criminelles",
    
    # Seniors
    "Federal pension program for seniors 65+. Contact Service Canada for eligibility, payments, and appeals": "Programme de pension fédéral pour les aînés de 65 ans et plus. Contactez Service Canada pour l'admissibilité, les paiements et les appels",
    "Federal supplement for low-income OAS recipients. Apply through Service Canada": "Supplément fédéral pour les bénéficiaires de la SV à faible revenu. Postulez via Service Canada",
    "Provincial top-ups like Ontario's GAINS or BC's Senior's Supplement. Contact your provincial social services ministry": "Suppléments provinciaux comme le SRG de l'Ontario ou le Supplément pour aînés de la C.-B. Contactez votre ministère provincial des services sociaux",
    "Provincial ministries regulate LTC homes. Municipalities operate some local homes. File complaints with provincial inspectors": "Les ministères provinciaux réglementent les centres de SLD. Les municipalités exploitent certains centres locaux. Déposez les plaintes auprès des inspecteurs provinciaux",
    "Provincial adult protection laws apply. Contact local police for criminal matters or provincial helplines for support services": "Les lois provinciales de protection des adultes s'appliquent. Contactez la police locale pour les questions criminelles ou les lignes d'aide provinciales pour les services de soutien",
    "Many municipalities offer tax deferral programs for eligible seniors. Contact your city's tax department": "De nombreuses municipalités offrent des programmes de report d'impôt pour les aînés admissibles. Contactez le service des impôts de votre ville",
    "Provincial pharmacare programs cover seniors. Ontario's ODB, BC's PharmaCare, etc. Contact provincial health ministry": "Les programmes provinciaux d'assurance médicaments couvrent les aînés. PSO de l'Ontario, PharmaCare de la C.-B., etc. Contactez le ministère provincial de la Santé",
    "Provincial health ministries fund home care. Apply through provincial health authorities or LHINs in Ontario": "Les ministères provinciaux de la Santé financent les soins à domicile. Postulez via les autorités de santé provinciales ou les RISSO en Ontario",
    
    # Veterans
    "Veterans Affairs Canada (VAC) provides disability pensions and benefits. Apply through My VAC Account or VAC offices": "Anciens Combattants Canada (ACC) fournit les pensions d'invalidité et les prestations. Postulez via Mon dossier ACC ou les bureaux d'ACC",
    "Federal pension for eligible veterans. Contact Veterans Affairs Canada for eligibility and application": "Pension fédérale pour les anciens combattants admissibles. Contactez Anciens Combattants Canada pour l'admissibilité et la demande",
    "VAC's home care program for veterans. Covers housekeeping, grounds maintenance, and personal care": "Programme de soins à domicile d'ACC pour les anciens combattants. Couvre l'entretien ménager, l'entretien des terrains et les soins personnels",
    "VAC offers mental health support including OSIs clinics. Access through Veterans Affairs Canada or the VAC Assistance Service": "ACC offre du soutien en santé mentale incluant les cliniques pour troubles de stress opérationnel. Accédez via Anciens Combattants Canada ou le Service d'aide d'ACC",
    "Veterans Affairs Canada maintains veteran grave sites and provides burial assistance. Contact VAC for applications": "Anciens Combattants Canada entretient les tombes des anciens combattants et fournit de l'aide funéraire. Contactez ACC pour les demandes",
    "Request military service records through Library and Archives Canada or Veterans Affairs Canada": "Demandez les dossiers de service militaire via Bibliothèque et Archives Canada ou Anciens Combattants Canada",
    "Apply for Veteran's Service Card through Veterans Affairs Canada. Proves veteran status for benefits and discounts": "Demandez la Carte de service d'ancien combattant via Anciens Combattants Canada. Prouve le statut d'ancien combattant pour les avantages et les rabais",
    
    # Disability
    "Federal disability pension for those who contributed to CPP. Apply through Service Canada. Appeals go to Social Security Tribunal": "Pension fédérale d'invalidité pour ceux qui ont cotisé au RPC. Postulez via Service Canada. Les appels vont au Tribunal de la sécurité sociale",
    "New federal benefit for working-age adults with disabilities. Contact Service Canada for eligibility and applications": "Nouvelle prestation fédérale pour les adultes en âge de travailler ayant une incapacité. Contactez Service Canada pour l'admissibilité et les demandes",
    "Ontario's ODSP, Alberta's AISH, BC's PWD. Income and employment support. Apply through provincial social services": "PSO de l'Ontario, AISH de l'Alberta, PVD de la C.-B. Soutien au revenu et à l'emploi. Postulez via les services sociaux provinciaux",
    "Federal non-refundable tax credit. Apply through CRA with medical practitioner certification. Opens RDSP eligibility": "Crédit d'impôt fédéral non remboursable. Postulez via l'ARC avec certification d'un praticien médical. Ouvre l'admissibilité au REEI",
    "Provincial laws like Ontario's AODA. File complaints with provincial human rights or accessibility tribunals": "Lois provinciales comme la LAPHO de l'Ontario. Déposez les plaintes auprès des tribunaux provinciaux des droits de la personne ou de l'accessibilité",
    "Issued by municipalities through Service Ontario or equivalent provincial offices. Apply with medical documentation": "Délivrés par les municipalités via Service Ontario ou les bureaux provinciaux équivalents. Postulez avec documentation médicale",
    "Federal savings plan with grants and bonds. Open at financial institutions. Must qualify for DTC": "Régime d'épargne fédéral avec subventions et bons. Ouvrez dans les institutions financières. Doit être admissible au CIPH",
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