import re

# Read the file
with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# French translations for issue details (common patterns)
translations = {
    # Infrastructure
    "City or town public works department. Use municipal 311 service or report online through your city's website": "Service des travaux publics de la ville ou de la municipalité. Utilisez le service 311 municipal ou signalez en ligne sur le site web de votre ville",
    "City engineering or transportation department. Check municipal website for capital project plans": "Service d'ingénierie ou des transports de la ville. Consultez le site municipal pour les projets d'infrastructure",
    "Municipal sidewalks and pathways department. Request through city's online service portal": "Service des trottoirs et sentiers municipaux. Faites une demande via le portail en ligne de la ville",
    "City traffic engineering department. Report through municipal 311 or traffic concerns portal": "Service de la circulation de la ville. Signalez via le 311 municipal ou le portail des questions de circulation",
    "Municipal parking authority. Contact city hall or use online parking services portal": "Autorité municipale de stationnement. Contactez l'hôtel de ville ou utilisez le portail de stationnement en ligne",
    "City water department or utility. Report leaks through municipal 311 or utility website": "Service de l'eau de la ville ou services publics. Signalez les fuites via le 311 municipal ou le site de l'utilité",
    "Municipal transit authority. Contact through transit agency website or customer service": "Autorité municipale de transport en commun. Contactez via le site de l'agence de transport ou le service client",
    "City bylaw enforcement. Report through municipal 311 or online complaint system": "Service d'application des règlements municipaux. Signalez via le 311 municipal ou le système de plaintes en ligne",
    "Municipal planning department. Attend city council meetings or submit written comments": "Service de l'urbanisme municipal. Participez aux conseils municipaux ou soumettez des commentaires écrits",
    "City parks and recreation department. Contact through municipal website or community center": "Service des parcs et loisirs de la ville. Contactez via le site municipal ou le centre communautaire",
    
    # Healthcare
    "Provincial Ministry of Health. Contact your local Member of Provincial Parliament (MPP)": "Ministère provincial de la Santé. Contactez votre député provincial (MPP)",
    "Provincial health authority. Contact your MLA/MPP/MNA through their constituency office": "Autorité provinciale de santé. Contactez votre député provincial via son bureau de circonscription",
    "Provincial health ministry. Reach out through your provincial representative's office": "Ministère provincial de la santé. Contactez via le bureau de votre représentant provincial",
    "Local Health Integration Network (LHIN) or provincial health authority. Contact your MPP": "Réseau local d'intégration des services de santé (LHIN) ou autorité provinciale. Contactez votre MPP",
    "Provincial mental health and addictions office. Contact through your MPP or health authority": "Bureau provincial de santé mentale et dépendances. Contactez via votre MPP ou l'autorité de santé",
    
    # Education
    "Local school board trustees. Contact your elected school board representative": "Conseillers scolaires élus. Contactez votre représentant élu au conseil scolaire",
    "Provincial Ministry of Education. Contact your local Member of Provincial Parliament": "Ministère provincial de l'Éducation. Contactez votre député provincial",
    "School board and provincial Ministry of Education. Attend board meetings or contact trustees": "Conseil scolaire et ministère provincial de l'Éducation. Participez aux réunions ou contactez les conseillers",
    "Provincial education ministry and local school board. Submit concerns to trustees and MPP": "Ministère provincial de l'éducation et conseil scolaire local. Soumettez vos préoccupations aux conseillers et à votre MPP",
    
    # Housing
    "Municipal housing department or provincial housing ministry. Contact city council or MPP": "Service municipal du logement ou ministère provincial. Contactez le conseil municipal ou votre MPP",
    "Provincial residential tenancy office. File disputes through provincial tribunal or board": "Bureau provincial des locations résidentielles. Déposez les litiges via le tribunal provincial",
    "Municipal planning and zoning department. Attend city council or committee meetings": "Service municipal de l'urbanisme et du zonage. Participez aux conseils municipaux ou aux réunions de comité",
    "Provincial housing ministry and federal CMHC. Contact your MPP and MP for policy issues": "Ministère provincial du logement et SCHL fédéral. Contactez votre MPP et député pour les questions de politique",
    
    # Environment
    "Federal Environment and Climate Change Canada. Contact your Member of Parliament": "Environnement et Changement climatique Canada (fédéral). Contactez votre député fédéral",
    "Provincial Ministry of Environment. Contact your MPP/MLA/MNA": "Ministère provincial de l'Environnement. Contactez votre MPP/MLA/MNA",
    "Municipal waste management department. Contact city council or use 311 service": "Service municipal de gestion des déchets. Contactez le conseil municipal ou utilisez le 311",
    "Federal and provincial environment ministries. Contact your MP and MPP for policy matters": "Ministères fédéral et provinciaux de l'environnement. Contactez votre député et MPP pour les questions de politique",
    
    # Safety
    "Municipal police services board or provincial solicitor general. Attend board meetings": "Commission des services policiers municipaux ou solliciteur général provincial. Participez aux réunions",
    "Municipal fire department. Contact city council for service levels and bylaw concerns": "Service d'incendie municipal. Contactez le conseil municipal pour les niveaux de service et les règlements",
    "Provincial Ministry of Transportation and municipal traffic engineering. Contact MPP and city council": "Ministère provincial des Transports et service de circulation municipal. Contactez votre MPP et le conseil municipal",
    "Provincial Ministry of Public Safety. Contact your MPP/MLA/MNA": "Ministère provincial de la Sécurité publique. Contactez votre MPP/MLA/MNA",
    
    # Employment
    "Federal Employment and Social Development Canada. Contact your Member of Parliament": "Emploi et Développement social Canada (fédéral). Contactez votre député fédéral",
    "Provincial Ministry of Labour. Contact your MPP/MLA/MNA": "Ministère provincial du Travail. Contactez votre MPP/MLA/MNA",
    "Federal Canada Revenue Agency and provincial tax ministry. Contact MP and MPP": "Agence du revenu du Canada et ministère provincial du revenu. Contactez votre député et MPP",
    
    # Social Services
    "Provincial Ministry of Social Services. Contact your MPP/MLA/MNA": "Ministère provincial des Services sociaux. Contactez votre MPP/MLA/MNA",
    "Provincial Ministry of Children and Family Services. Contact your MPP/MLA/MNA": "Ministère provincial des Services à l'enfance et à la famille. Contactez votre MPP/MLA/MNA",
    "Federal Immigration, Refugees and Citizenship Canada. Contact your Member of Parliament": "Immigration, Réfugiés et Citoyenneté Canada (fédéral). Contactez votre député fédéral",
    
    # Taxes
    "Federal Canada Revenue Agency. Contact your Member of Parliament": "Agence du revenu du Canada (fédéral). Contactez votre député fédéral",
    "Provincial Ministry of Finance. Contact your MPP/MLA/MNA": "Ministère provincial des Finances. Contactez votre MPP/MLA/MNA",
    "Municipal tax department. Contact city council or use 311 for assessment questions": "Service des taxes municipales. Contactez le conseil municipal ou utilisez le 311 pour les questions d'évaluation",
    
    # Consumer Rights
    "Provincial consumer protection office. Contact your MPP/MLA/MNA": "Bureau provincial de la protection du consommateur. Contactez votre MPP/MLA/MNA",
    "Federal Competition Bureau. Contact your Member of Parliament": "Bureau de la concurrence (fédéral). Contactez votre député fédéral",
    
    # Indigenous Affairs
    "Federal Crown-Indigenous Relations and Northern Affairs. Contact your Member of Parliament": "Relations Couronne-Autochtones et Affaires du Nord Canada (fédéral). Contactez votre député fédéral",
    "Provincial Ministry of Indigenous Relations. Contact your MPP/MLA/MNA": "Ministère provincial des Relations autochtones. Contactez votre MPP/MLA/MNA",
    
    # Seniors
    "Federal Employment and Social Development Canada (Old Age Security). Contact your MP": "Emploi et Développement social Canada (Sécurité de la vieillesse). Contactez votre député fédéral",
    "Provincial Ministry for Seniors. Contact your MPP/MLA/MNA": "Ministère provincial pour les Aînés. Contactez votre MPP/MLA/MNA",
    
    # Veterans
    "Federal Veterans Affairs Canada. Contact your Member of Parliament": "Anciens Combattants Canada (fédéral). Contactez votre député fédéral",
    
    # Disability
    "Provincial accessibility office. Contact your MPP/MLA/MNA": "Bureau provincial de l'accessibilité. Contactez votre MPP/MLA/MNA",
    "Federal Accessibility Commissioner. Contact your Member of Parliament": "Commissaire fédéral à l'accessibilité. Contactez votre député fédéral",
    
    # Youth
    "Provincial Ministry of Youth. Contact your MPP/MLA/MNA": "Ministère provincial de la Jeunesse. Contactez votre MPP/MLA/MNA",
    "Municipal youth services. Contact city council or youth advisory committee": "Services municipaux pour la jeunesse. Contactez le conseil municipal ou le comité consultatif jeunesse",
    
    # Agriculture
    "Federal Agriculture and Agri-Food Canada. Contact your Member of Parliament": "Agriculture et Agroalimentaire Canada (fédéral). Contactez votre député fédéral",
    "Provincial Ministry of Agriculture. Contact your MPP/MLA/MNA": "Ministère provincial de l'Agriculture. Contactez votre MPP/MLA/MNA",
    
    # Utilities
    "Provincial utilities commission or energy board. Contact your MPP/MLA/MNA": "Commission des services publics ou régie de l'énergie provinciale. Contactez votre MPP/MLA/MNA",
    "Municipal water utility. Contact city council or utility customer service": "Service municipal de l'eau. Contactez le conseil municipal ou le service client de l'utilité",
    
    # Family Law
    "Provincial Ministry of Justice and Attorney General. Contact your MPP/MLA/MNA": "Ministère provincial de la Justice et Procureur général. Contactez votre MPP/MLA/MNA",
    "Federal Department of Justice. Contact your Member of Parliament": "Ministère fédéral de la Justice. Contactez votre député fédéral",
    
    # Arts
    "Federal Canada Council for the Arts. Contact your Member of Parliament": "Conseil des arts du Canada (fédéral). Contactez votre député fédéral",
    "Provincial arts council. Contact your MPP/MLA/MNA": "Conseil des arts provincial. Contactez votre MPP/MLA/MNA",
    "Municipal arts and culture department. Contact city council or cultural advisory committee": "Service municipal des arts et de la culture. Contactez le conseil municipal ou le comité consultatif culturel",
    
    # Tenant Rights
    "Provincial residential tenancy board. Contact your MPP/MLA/MNA for policy issues": "Commission provinciale des locations résidentielles. Contactez votre MPP/MLA/MNA pour les questions de politique",
    "Municipal rental housing office. Contact city council for bylaw concerns": "Bureau municipal du logement locatif. Contactez le conseil municipal pour les questions de règlement",
    
    # Electoral Reform
    "Federal Elections Canada. Contact your Member of Parliament": "Élections Canada (fédéral). Contactez votre député fédéral",
    "Provincial elections office. Contact your MPP/MLA/MNA": "Bureau provincial des élections. Contactez votre MPP/MLA/MNA",
    
    # Broadband
    "Federal Innovation, Science and Economic Development Canada. Contact your MP": "Innovation, Sciences et Développement économique Canada (fédéral). Contactez votre député",
    "Provincial Ministry of Infrastructure. Contact your MPP/MLA/MNA": "Ministère provincial de l'Infrastructure. Contactez votre MPP/MLA/MNA",
    
    # Fisheries
    "Federal Fisheries and Oceans Canada. Contact your Member of Parliament": "Pêches et Océans Canada (fédéral). Contactez votre député fédéral",
    "Provincial Ministry of Natural Resources. Contact your MPP/MLA/MNA": "Ministère provincial des Ressources naturelles. Contactez votre MPP/MLA/MNA",
    
    # Official Languages
    "Federal Office of the Commissioner of Official Languages. Contact your MP": "Commissariat aux langues officielles (fédéral). Contactez votre député fédéral",
    "Provincial language rights office. Contact your MPP/MLA/MNA": "Bureau provincial des droits linguistiques. Contactez votre MPP/MLA/MNA",
    
    # International Development
    "Federal Global Affairs Canada. Contact your Member of Parliament": "Affaires mondiales Canada (fédéral). Contactez votre député fédéral",
    
    # LGBTQ+ Rights
    "Federal Department of Justice. Contact your Member of Parliament": "Ministère fédéral de la Justice. Contactez votre député fédéral",
    "Provincial Ministry of Justice. Contact your MPP/MLA/MNA": "Ministère provincial de la Justice. Contactez votre MPP/MLA/MNA",
    
    # Women's Rights
    "Federal Women and Gender Equality Canada. Contact your Member of Parliament": "Femmes et Égalité des genres Canada (fédéral). Contactez votre député fédéral",
    "Provincial Ministry of Women's Issues. Contact your MPP/MLA/MNA": "Ministère provincial de la Condition féminine. Contactez votre MPP/MLA/MNA",
    
    # Mental Health
    "Provincial Ministry of Health and Mental Health. Contact your MPP/MLA/MNA": "Ministère provincial de la Santé et de la Santé mentale. Contactez votre MPP/MLA/MNA",
    "Local health authority. Contact your MPP/MLA/MNA for mental health services": "Autorité de santé locale. Contactez votre MPP/MLA/MNA pour les services de santé mentale",
    
    # Substance Use & Addiction
    "Provincial Ministry of Health and Addictions. Contact your MPP/MLA/MNA": "Ministère provincial de la Santé et des Dépendances. Contactez votre MPP/MLA/MNA",
    "Federal Health Canada. Contact your Member of Parliament": "Santé Canada (fédéral). Contactez votre député fédéral",
    
    # Transportation
    "Provincial Ministry of Transportation. Contact your MPP/MLA/MNA": "Ministère provincial des Transports. Contactez votre MPP/MLA/MNA",
    "Municipal transportation department. Contact city council": "Service municipal des transports. Contactez le conseil municipal",
    
    # Digital Rights
    "Federal Innovation, Science and Economic Development Canada. Contact your MP": "Innovation, Sciences et Développement économique Canada (fédéral). Contactez votre député",
    "Federal Privacy Commissioner. Contact your Member of Parliament": "Commissariat à la protection de la vie privée (fédéral). Contactez votre député fédéral",
    
    # Animal Welfare
    "Provincial Ministry of Agriculture and Animal Welfare. Contact your MPP/MLA/MNA": "Ministère provincial de l'Agriculture et du Bien-être animal. Contactez votre MPP/MLA/MNA",
    "Municipal animal services. Contact city council for bylaw concerns": "Services municipaux des animaux. Contactez le conseil municipal pour les questions de règlement",
    
    # Sports & Recreation
    "Municipal parks and recreation department. Contact city council or community centers": "Service municipal des parcs et loisirs. Contactez le conseil municipal ou les centres communautaires",
    "Provincial Ministry of Sport. Contact your MPP/MLA/MNA": "Ministère provincial du Sport. Contactez votre MPP/MLA/MNA",
    
    # Religion & Faith
    "Provincial Ministry of Justice. Contact your MPP/MLA/MNA for religious freedom issues": "Ministère provincial de la Justice. Contactez votre MPP/MLA/MNA pour les questions de liberté religieuse",
    "Federal Department of Justice. Contact your Member of Parliament": "Ministère fédéral de la Justice. Contactez votre député fédéral",
    
    # Volunteer & Community
    "Municipal community services. Contact city council or community organizations": "Services municipaux communautaires. Contactez le conseil municipal ou les organisations communautaires",
    "Federal Employment and Social Development Canada. Contact your MP for volunteer programs": "Emploi et Développement social Canada (fédéral). Contactez votre député pour les programmes de bénévolat",
    
    # Legal Aid
    "Provincial Legal Aid office. Contact your MPP/MLA/MNA": "Bureau provincial de l'aide juridique. Contactez votre MPP/MLA/MNA",
    "Federal Department of Justice. Contact your Member of Parliament": "Ministère fédéral de la Justice. Contactez votre député fédéral",
    
    # Pensions & Retirement
    "Federal Employment and Social Development Canada (CPP/OAS). Contact your MP": "Emploi et Développement social Canada (RPC/SV). Contactez votre député fédéral",
    "Provincial Ministry of Finance. Contact your MPP/MLA/MNA for provincial pensions": "Ministère provincial des Finances. Contactez votre MPP/MLA/MNA pour les régimes provinciaux",
    
    # Childcare
    "Provincial Ministry of Education or Childcare. Contact your MPP/MLA/MNA": "Ministère provincial de l'Éducation ou des Services de garde. Contactez votre MPP/MLA/MNA",
    "Municipal childcare services. Contact city council for local programs": "Services municipaux de garde d'enfants. Contactez le conseil municipal pour les programmes locaux",
    
    # Food Security
    "Federal Agriculture and Agri-Food Canada. Contact your Member of Parliament": "Agriculture et Agroalimentaire Canada (fédéral). Contactez votre député fédéral",
    "Provincial Ministry of Agriculture. Contact your MPP/MLA/MNA": "Ministère provincial de l'Agriculture. Contactez votre MPP/MLA/MNA",
    "Municipal food policy council. Contact city council": "Conseil municipal de la politique alimentaire. Contactez le conseil municipal",
    
    # Emergency Services
    "Municipal fire and emergency services. Contact city council": "Services d'incendie et d'urgence municipaux. Contactez le conseil municipal",
    "Provincial Ministry of Public Safety. Contact your MPP/MLA/MNA": "Ministère provincial de la Sécurité publique. Contactez votre MPP/MLA/MNA",
    "Federal Public Safety Canada. Contact your Member of Parliament": "Sécurité publique Canada (fédéral). Contactez votre député fédéral",
    
    # Human Rights
    "Federal Canadian Human Rights Commission. Contact your Member of Parliament": "Commission canadienne des droits de la personne (fédéral). Contactez votre député fédéral",
    "Provincial human rights commission. Contact your MPP/MLA/MNA": "Commission provinciale des droits de la personne. Contactez votre MPP/MLA/MNA",
}

# Function to add detailFr after each detail field
def add_french_details(content):
    for eng_detail, fr_detail in translations.items():
        # Escape special regex characters
        eng_escaped = re.escape(eng_detail)
        # Find pattern: detail:"English text"}
        pattern = f'detail:"{eng_escaped}"'
        replacement = f'detail:"{eng_detail}",detailFr:"{fr_detail}"'
        content = re.sub(pattern, replacement, content)
    return content

# Process the content
new_content = add_french_details(content)

# Write back
with open(r'D:\source_extracted\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Count how many detailFr we added
original_count = content.count('detailFr:')
new_count = new_content.count('detailFr:')
print(f"Added {new_count - original_count} French detail translations")
print(f"Total detailFr fields: {new_count}")