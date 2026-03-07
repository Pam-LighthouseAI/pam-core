import re

# Read the file
with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Translation mapping based on common patterns in the detail texts
# Each entry maps English detail text to French translation
translations = {
    # Municipal infrastructure
    "City or town public works department. Use municipal 311 service or report online through your city's website": "Service des travaux publics de la ville ou de la municipalité. Utilisez le service 311 municipal ou signalez en ligne sur le site web de votre ville",
    "Municipal transit authorities (TTC, STM, TransLink). Provincial ministries fund major projects": "Autorités de transport en commun municipales (TTC, STM, TransLink). Les ministères provinciaux financent les grands projets",
    "Municipal traffic engineering departments handle signals and signs on city streets": "Les services municipaux de génie de la circulation gèrent les feux et la signalisation sur les rues de la ville",
    "City engineering or transportation departments. Report through 311 or municipal apps": "Services d'ingénierie ou de transport de la ville. Signalez via le 311 ou les applications municipales",
    "Municipal planning departments design bike lanes. Provincial funding programs may apply": "Les services municipaux de l'urbanisme conçoivent les pistes cyclables. Les programmes de financement provinciaux peuvent s'appliquer",
    "Municipal public works handles local streets. Provincial highways are provincial responsibility": "Les travaux publics municipaux s'occupent des rues locales. Les autoroutes provinciales sont de responsabilité provinciale",
    "City or town maintains streetlights. Report outages through 311 or utility company": "La ville ou la municipalité entretient l'éclairage des rues. Signalez les pannes via le 311 ou la compagnie de services publics",
    "Municipal parking authority or bylaw enforcement. Appeal through city parking tribunal": "Autorité de stationnement municipale ou application des règlements. Appelez via le tribunal de stationnement de la ville",
    
    # Healthcare
    "Provincial health ministries fund and regulate hospitals. Contact hospital patient relations first, then provincial ministry": "Les ministères provinciaux de la Santé financent et réglementent les hôpitaux. Contactez d'abord les relations patients de l'hôpital, puis le ministère provincial",
    "Provincial health ministries manage physician licensing. Many provinces have registry programs to find doctors": "Les ministères provinciaux de la Santé gèrent les permis des médecins. Plusieurs provinces ont des programmes de registre pour trouver des médecins",
    "Provincial health ministries set priorities. Federal Canada Health Act sets national standards": "Les ministères provinciaux de la Santé établissent les priorités. La Loi canadienne sur la santé fédérale fixe les normes nationales",
    "Provincial health ministries fund mental health. Federal government funds research and some programs": "Les ministères provinciaux de la Santé financent la santé mentale. Le gouvernement fédéral finance la recherche et certains programmes",
    "Provincial drug benefit programs vary. Federal government setting national pharmacare standards": "Les programmes provinciaux d'assurance médicaments varient. Le gouvernement fédéral établit les normes nationales de l'assurance médicaments",
    "Provincial ministries license and inspect LTC homes. File complaints with provincial inspectorate": "Les ministères provinciaux délivrent les permis et inspectent les centres de soins de longue durée. Déposez les plaintes auprès de l'inspecteurat provincial",
    "Provincial colleges of physicians and surgeons regulate doctors. Other health colleges for other professions": "Les collèges provinciaux des médecins et chirurgiens réglementent les médecins. Autres collèges de santé pour les autres professions",
    "Provincial health ministries fund ambulance services. Municipal land ambulances in some provinces": "Les ministères provinciaux de la Santé financent les services d'ambulance. Ambulances terrestres municipales dans certaines provinces",
    
    # Education
    "Provincial education ministries set curriculum and fund schools. School boards manage local schools": "Les ministères provinciaux de l'Éducation établissent les programmes et financent les écoles. Les conseils scolaires gèrent les écoles locales",
    "Provincial ministries fund universities and colleges. Federal student loans and grants also apply": "Les ministères provinciaux financent les universités et collèges. Les prêts et bourses fédéraux s'appliquent également",
    "Provincial education ministries mandate special education. School boards deliver programs": "Les ministères provinciaux de l'Éducation mandatent l'éducation spécialisée. Les conseils scolaires livrent les programmes",
    "Provincial regulations, school boards contract services. Municipal traffic bylaws may apply": "Règlements provinciaux, les conseils scolaires contractent les services. Les règlements municipaux sur la circulation peuvent s'appliquer",
    "Provincial education ministry sets curriculum. School boards implement provincially": "Le ministère provincial de l'Éducation établit le programme. Les conseils scolaires mettent en œuvre au niveau provincial",
    "Provincial teacher certification bodies regulate the profession. Contact provincial college of teachers": "Les organismes provinciaux de certification des enseignants réglementent la profession. Contactez l'ordre provincial des enseignants",
    "School boards make closure decisions. Provincial funding formulas drive decisions": "Les conseils scolaires prennent les décisions de fermeture. Les formules de financement provincial orientent les décisions",
    "Federal Indigenous Services funds First Nations schools. Provincial schools for other Indigenous students": "Services aux Autochtones Canada finance les écoles des Premières Nations. Écoles provinciales pour les autres élèves autochtones",
    
    # Housing
    "Provincial residential tenancy acts. Landlord-tenant boards or tribunals handle disputes": "Lois provinciales sur la location résidentielle. Les commissions ou tribunaux des relations propriétaire-locataire traitent les litiges",
    "CMHC (federal) funds programs. Provincial housing ministries and municipal housing departments deliver": "La SCHL (fédérale) finance les programmes. Les ministères provinciaux du logement et les services municipaux du logement les livrent",
    "Municipal tax departments assess and collect. Provincial property assessment agencies may set values": "Les services fiscaux municipaux évaluent et perçoivent. Les agences provinciales d'évaluation foncière peuvent fixer les valeurs",
    "City planning departments handle zoning. Committee of Adjustment for minor variances": "Les services municipaux de l'urbanisme gèrent le zonage. Comité de dérogation pour les variances mineures",
    "Municipal shelters and outreach. Provincial and federal funding programs support services": "Refuges et services d'approche municipaux. Les programmes de financement provincial et fédéral soutiennent les services",
    "Provincial residential tenancy legislation sets rent increase limits. Provincial tribunals enforce": "La législation provinciale sur la location résidentielle fixe les limites d'augmentation de loyer. Les tribunaux provinciaux font appliquer",
    "Municipal building departments issue permits. Provincial building codes set standards": "Les services municipaux du bâtiment délivrent les permis. Les codes du bâtiment provinciaux établissent les normes",
    "Municipal bylaws regulate short-term rentals. Provincial rules may apply for taxation": "Les règlements municipaux réglementent les locations à court terme. Les règles provinciales peuvent s'appliquer pour la fiscalité",
    
    # Environment
    "Provincial environment ministries monitor air quality. Federal standards under Canadian Environmental Protection Act": "Les ministères provinciaux de l'Environnement surveillent la qualité de l'air. Normes fédérales en vertu de la Loi canadienne sur la protection de l'environnement",
    "Provincial standards. Municipal water treatment plants. Health Canada sets federal guidelines": "Normes provinciales. Usines municipales de traitement de l'eau. Santé Canada établit les lignes directrices fédérales",
    "Municipal garbage and recycling programs. Provincial recycling regulations and EPR programs": "Programmes municipaux d'ordures et de recyclage. Règlements provinciaux sur le recyclage et programmes de responsabilité élargie des producteurs",
    "Provincial environment ministries order cleanup. Federal rules for federal lands": "Les ministères provinciaux de l'Environnement ordonnent l'assainissement. Règles fédérales pour les terres fédérales",
    "Federal government sets national climate targets. Provincial carbon pricing and policies vary": "Le gouvernement fédéral fixe les cibles climatiques nationales. La tarification et les politiques provinciales sur le carbone varient",
    "Provincial parks under provincial ministries. National parks under Parks Canada. Municipal parks locally": "Parcs provinciaux sous les ministères provinciaux. Parcs nationaux sous Parcs Canada. Parcs municipaux localement",
    "Provincial wildlife acts protect most species. Federal Species at Risk Act for endangered species": "Les lois provinciales sur la faune protègent la plupart des espèces. Loi fédérale sur les espèces en péril pour les espèces menacées",
    "Federal Impact Assessment Act for major projects. Provincial environmental assessment acts apply provincially": "Loi fédérale sur l'évaluation d'impact pour les grands projets. Lois provinciales sur l'évaluation environnementale s'appliquent au niveau provincial",
}

# Count matches
count = 0
for eng, fr in translations.items():
    pattern = f'detail:"{re.escape(eng)}"'
    if re.search(pattern, content):
        count += 1

print(f"Found {count} matching detail texts out of {len(translations)} translations")

# Apply translations
for eng_detail, fr_detail in translations.items():
    # Pattern: detail:"English text"}
    # Replace with: detail:"English text",detailFr:"French text"}
    pattern = f'detail:"{re.escape(eng_detail)}"'
    replacement = f'detail:"{eng_detail}",detailFr:"{fr_detail}"'
    content = re.sub(pattern, replacement, content)

# Write back
with open(r'D:\source_extracted\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Count result
new_count = content.count('detailFr:')
print(f"Total detailFr fields after update: {new_count}")