// Jurisdiction headers for My Civic Voice

const JURISDICTION_HEADERS = {
  infrastructure: {
    federal: { title: "National Transportation", contact: "MP", items: ["Interprovincial highways", "Rail safety", "Aviation", "Ports", "National transportation policy"] },
    provincial: { title: "Provincial Infrastructure", contact: "MPP/MLA", items: ["Provincial highways", "Provincial transit funding", "Driver licensing", "Provincial road maintenance"] },
    municipal: { title: "Local Infrastructure", contact: "Councillor", items: ["City streets", "Sidewalks", "Local transit", "Parking", "Street lighting", "Snow removal", "Potholes"] }
  },
  healthcare: {
    federal: { title: "National Health Standards", contact: "MP", items: ["Canada Health Act", "First Nations health", "Drug approval (Health Canada)", "National health research"] },
    provincial: { title: "Provincial Healthcare", contact: "MPP/MLA", items: ["Hospital funding", "Doctor licensing", "Provincial drug plans", "Wait times", "Long-term care", "Mental health services"] },
    municipal: { title: "Local Health Services", contact: "Councillor", items: ["Public health units", "Ambulance (some provinces)", "Local health programs"] }
  },
  education: {
    federal: { title: "National Education Programs", contact: "MP", items: ["Student loans", "Indigenous education funding", "Official languages", "Research grants"] },
    provincial: { title: "Provincial Education", contact: "MPP/MLA", items: ["K-12 curriculum", "School boards", "University funding", "Teacher certification", "Special education"] },
    municipal: { title: "Local School Issues", contact: "Councillor", items: ["School zones", "Crossing guards", "Municipal property taxes for schools"] }
  },
  housing: {
    federal: { title: "National Housing Programs", contact: "MP", items: ["CMHC programs", "National housing strategy", "Mortgage rules", "Affordable housing funding"] },
    provincial: { title: "Provincial Housing", contact: "MPP/MLA", items: ["Rent control", "Landlord-tenant disputes", "Provincial housing programs", "Building codes"] },
    municipal: { title: "Local Housing & Zoning", contact: "Councillor", items: ["Zoning bylaws", "Development permits", "Property taxes", "Short-term rental rules", "Homeless shelters"] }
  },
  environment: {
    federal: { title: "National Parks & Environment", contact: "MP", items: ["National parks", "Parks Canada", "Climate policy", "Species at risk", "Environmental assessments", "Ocean protection"] },
    provincial: { title: "Provincial Parks & Environment", contact: "MPP/MLA", items: ["Provincial parks", "Conservation areas", "Provincial environmental rules", "Wildlife management", "Water quality"] },
    municipal: { title: "Local Parks & Environment", contact: "Councillor", items: ["City parks", "Playgrounds", "Sports fields", "Community gardens", "Local recycling", "Garbage collection"] }
  },
  safety: {
    federal: { title: "Federal Justice & Safety", contact: "MP", items: ["Criminal law", "Federal prisons", "RCMP (contract)", "Border security", "National security"] },
    provincial: { title: "Provincial Justice", contact: "MPP/MLA", items: ["Provincial courts", "Provincial jails", "Provincial police", "Legal aid", "Victim services"] },
    municipal: { title: "Local Safety", contact: "Councillor", items: ["Municipal police", "Fire services", "Bylaw enforcement", "Emergency management", "Local safety programs"] }
  },
  employment: {
    federal: { title: "Federal Employment", contact: "MP", items: ["Employment Insurance", "Canada Labour Code", "Foreign workers", "Federal minimum wage", "Pension plan (CPP)"] },
    provincial: { title: "Provincial Employment", contact: "MPP/MLA", items: ["Employment standards", "Workers compensation", "Labour relations", "Provincial minimum wage", "Occupational health & safety"] },
    municipal: { title: "Local Employment Programs", contact: "Councillor", items: ["Local job programs", "Business licensing", "Economic development"] }
  },
  social: {
    federal: { title: "Federal Social Programs", contact: "MP", items: ["Canada Child Benefit", "Old Age Security", "Employment Insurance", "Disability tax credit", "Newcomer services"] },
    provincial: { title: "Provincial Social Services", contact: "MPP/MLA", items: ["Social assistance (welfare)", "Provincial disability programs", "Child protection", "Housing subsidies"] },
    municipal: { title: "Local Social Services", contact: "Councillor", items: ["Local shelters", "Food banks coordination", "Community services", "Recreation programs"] }
  },
  taxes: {
    federal: { title: "Federal Taxes", contact: "MP", items: ["Income tax", "GST", "Canada Child Benefit", "Carbon pricing", "Corporate tax", "Tax credits"] },
    provincial: { title: "Provincial Taxes", contact: "MPP/MLA", items: ["Provincial income tax", "Provincial sales tax", "Property assessment", "Provincial tax credits"] },
    municipal: { title: "Local Taxes & Fees", contact: "Councillor", items: ["Property tax rates", "Water bills", "Parking fines", "Permit fees", "Local improvement charges"] }
  },
  immigration: {
    federal: { title: "Immigration & Citizenship", contact: "MP", items: ["Permanent residence", "Work & study permits", "Citizenship", "Refugee claims", "Family sponsorship", "Visitor visas"] },
    provincial: { title: "Provincial Immigration", contact: "MPP/MLA", items: ["Provincial nominee programs", "Provincial settlement services"] },
    municipal: { title: "Local Newcomer Services", contact: "Councillor", items: ["Local settlement agencies", "Community integration programs", "Language classes (municipal facilities)"] }
  },
  consumer: {
    federal: { title: "Federal Consumer Protection", contact: "MP", items: ["Privacy (PIPEDA)", "Telecom complaints (CRTC)", "Banking complaints", "Product safety", "Competition law"] },
    provincial: { title: "Provincial Consumer Affairs", contact: "MPP/MLA", items: ["Consumer protection acts", "Warranty enforcement", "False advertising", "Landlord-tenant (some provinces)", "Provincial consumer tribunals"] },
    municipal: { title: "Local Consumer Issues", contact: "Councillor", items: ["Business licensing", "Local bylaw complaints", "Municipal utility billing"] }
  },
  indigenous: {
    federal: { title: "Indigenous Affairs", contact: "MP", items: ["Status cards", "Treaty rights", "Reserve land", "First Nations education", "Non-insured health benefits", "MMIWG"] },
    provincial: { title: "Provincial Indigenous Relations", contact: "MPP/MLA", items: ["Provincial Indigenous affairs", "Child welfare agreements", "Resource consultation", "Provincial programs"] },
    municipal: { title: "Local Indigenous Relations", contact: "Councillor", items: ["Urban Indigenous programs", "Municipal-First Nations relations", "Local cultural initiatives"] }
  },
  seniors: {
    federal: { title: "Federal Seniors Programs", contact: "MP", items: ["Old Age Security", "Guaranteed Income Supplement", "CPP retirement", "Canada Pension Plan", "Federal seniors initiatives"] },
    provincial: { title: "Provincial Seniors Services", contact: "MPP/MLA", items: ["Provincial seniors supplements", "Long-term care regulation", "Home care programs", "Provincial drug benefits", "Seniors' housing programs"] },
    municipal: { title: "Local Seniors Services", contact: "Councillor", items: ["Seniors' centres", "Property tax deferral", "Local seniors programs", "Community transportation"] }
  },
  veterans: {
    federal: { title: "Veterans Affairs", contact: "MP", items: ["Disability benefits", "Veterans' pension", "Veterans Independence Program", "Mental health services", "Service records", "Burial assistance"] },
    provincial: { title: "Provincial Veterans Services", contact: "MPP/MLA", items: ["Provincial veterans' benefits", "Provincial recognition programs"] },
    municipal: { title: "Local Veterans Support", contact: "Councillor", items: ["Local veterans' events", "Remembrance ceremonies", "Community support programs"] }
  },
  disability: {
    federal: { title: "Federal Disability Programs", contact: "MP", items: ["CPP Disability", "Disability Tax Credit", "Canada Disability Benefit", "Registered Disability Savings Plan", "Accessibility legislation"] },
    provincial: { title: "Provincial Disability Services", contact: "MPP/MLA", items: ["Provincial disability support (ODSP, AISH, PWD)", "Provincial accessibility laws", "Provincial disability programs"] },
    municipal: { title: "Local Accessibility", contact: "Councillor", items: ["Accessible parking permits", "Municipal accessibility standards", "Local accessibility programs", "Paratransit services"] }
  },
  youth: {
    federal: { title: "Federal Youth Programs", contact: "MP", items: ["Student loans", "Youth Employment Program", "Canada Learning Bond", "Apprenticeship grants", "Canada Service Corps"] },
    provincial: { title: "Provincial Youth & Education", contact: "MPP/MLA", items: ["Provincial student aid", "Youth justice", "Provincial youth programs", "Education funding"] },
    municipal: { title: "Local Youth Services", contact: "Councillor", items: ["Youth centres", "Recreation programs", "Local youth employment", "Community programs"] }
  },
  agriculture: {
    federal: { title: "Federal Agriculture", contact: "MP", items: ["Farm income support (AgriStability)", "Agricultural research", "Rural broadband funding", "Supply management", "Trade agreements"] },
    provincial: { title: "Provincial Agriculture", contact: "MPP/MLA", items: ["Provincial farm programs", "Agricultural land protection", "Provincial grants", "Farm safety", "Soil and water conservation"] },
    municipal: { title: "Local Rural Issues", contact: "Councillor", items: ["Rural zoning", "Local drainage", "Agricultural bylaws", "Rural road maintenance"] }
  },
  utilities: {
    federal: { title: "Federal Telecom & Utilities", contact: "MP", items: ["Internet/cable complaints (CRTC)", "Telecom regulation", "Spectrum allocation", "National broadband strategy"] },
    provincial: { title: "Provincial Utilities", contact: "MPP/MLA", items: ["Electricity rates", "Natural gas regulation", "Provincial utility boards", "Net metering rules"] },
    municipal: { title: "Local Utilities", contact: "Councillor", items: ["Water billing", "Local utility disputes", "Municipal water/sewer", "Community choice aggregation"] }
  },
  family: {
    federal: { title: "Federal Family Law", contact: "MP", items: ["Divorce Act", "Child support guidelines", "Federal family courts", "Marriage definition"] },
    provincial: { title: "Provincial Family Law", contact: "MPP/MLA", items: ["Family law courts", "Child protection (CAS)", "Provincial family services", "Property division", "Spousal support enforcement"] },
    municipal: { title: "Local Family Services", contact: "Councillor", items: ["Marriage licenses (via province)", "Local family programs", "Community services"] }
  },
  arts: {
    federal: { title: "Federal Arts & Culture", contact: "MP", items: ["Canada Council for the Arts", "Canadian Heritage", "Film/TV tax credits", "National museums", "Official languages"] },
    provincial: { title: "Provincial Arts Funding", contact: "MPP/MLA", items: ["Provincial arts councils", "Provincial heritage", "Provincial museums", "Cultural programs"] },
    municipal: { title: "Local Arts & Culture", contact: "Councillor", items: ["Municipal arts grants", "Local museums", "Community centres", "Public art", "Festivals", "Heritage designation"] }
  }
,
  lgbtq: {
    federal: { title: "Federal LGBTQ+ Rights", contact: "MP", items: ["Criminal Code protections", "Canadian Human Rights Act", "Conversion therapy ban", "Federal workplace protections", "Immigration for same-sex partners"] },
    provincial: { title: "Provincial LGBTQ+ Rights", contact: "MPP/MLA", items: ["Provincial human rights codes", "Healthcare coverage", "Provincial education policies", "Provincial workplace protections", "Name/gender changes"] },
    municipal: { title: "Local LGBTQ+ Support", contact: "Councillor", items: ["Pride events", "Community programs", "Municipal inclusivity policies", "Local anti-discrimination"] }
  },
  women: {
    federal: { title: "Federal Women's Programs", contact: "MP", items: ["Women and Gender Equality Canada", "Pay Equity Act", "Maternity/parental benefits", "Federal gender-based violence funding", "National inquiry follow-up"] },
    provincial: { title: "Provincial Women's Services", contact: "MPP/MLA", items: ["Provincial women's offices", "Shelter funding", "Provincial pay equity", "Reproductive healthcare", "Women's crisis lines"] },
    municipal: { title: "Local Women's Support", contact: "Councillor", items: ["Women's shelters", "Local crisis services", "Municipal women's programs", "Community safety initiatives"] }
  },
  mentalhealth: {
    federal: { title: "Federal Mental Health", contact: "MP", items: ["Mental health funding", "National mental health standards", "988 crisis line", "Federal workplace mental health", "Research funding"] },
    provincial: { title: "Provincial Mental Health", contact: "MPP/MLA", items: ["Provincial mental health plans", "Hospital psychiatric services", "Community mental health", "Provincial crisis lines", "Addiction services"] },
    municipal: { title: "Local Mental Health", contact: "Councillor", items: ["Community programs", "Local crisis response", "Public health mental health", "Community centre programs"] }
  },
  substance: {
    federal: { title: "Federal Substance Policy", contact: "MP", items: ["Controlled Drugs Act", "Safe supply programs", "Federal addiction funding", "Opioid response", "Health Canada oversight"] },
    provincial: { title: "Provincial Addiction Services", contact: "MPP/MLA", items: ["Treatment centers", "Harm reduction programs", "Provincial opioid response", "Recovery housing", "Naloxone distribution"] },
    municipal: { title: "Local Addiction Support", contact: "Councillor", items: ["Supervised consumption sites", "Local harm reduction", "Community programs", "Outreach services"] }
  },
  transportation: {
    federal: { title: "Federal Transportation", contact: "MP", items: ["National transportation policy", "Rural transit funding", "Accessibility standards", "Air passenger rights", "Rail safety"] },
    provincial: { title: "Provincial Transportation", contact: "MPP/MLA", items: ["Provincial highways", "Provincial transit funding", "Driver licensing", "Provincial road maintenance", "Paratransit standards"] },
    municipal: { title: "Local Transportation", contact: "Councillor", items: ["Local transit", "Active transportation", "Parking", "Local roads", "Accessibility"] }
  },
  digital: {
    federal: { title: "Federal Digital Rights", contact: "MP", items: ["PIPEDA privacy law", "CRTC telecom regulation", "Online Harms Act", "Digital ID standards", "Cybersecurity"] },
    provincial: { title: "Provincial Digital", contact: "MPP/MLA", items: ["Provincial privacy laws", "Provincial digital ID", "Provincial consumer protection", "Provincial cybersecurity"] },
    municipal: { title: "Local Digital Services", contact: "Councillor", items: ["Municipal digital services", "Local broadband", "Municipal data privacy", "Community Wi-Fi"] }
  },
  animals: {
    federal: { title: "Federal Animal Protection", contact: "MP", items: ["Criminal Code cruelty", "Species at Risk Act", "Health Canada pet food", "CFIA animal health", "Import/export rules"] },
    provincial: { title: "Provincial Animal Welfare", contact: "MPP/MLA", items: ["Provincial SPCAs", "Provincial animal welfare acts", "Wildlife protection", "Farm animal standards", "Exotic animal rules"] },
    municipal: { title: "Local Animal Services", contact: "Councillor", items: ["Animal control", "Pet licensing", "Local shelters", "Bylaw enforcement", "Dog parks"] }
  },
  sports: {
    federal: { title: "Federal Sport", contact: "MP", items: ["Sport Canada", "Athlete assistance", "Safe Sport", "National sport organizations", "Anti-doping"] },
    provincial: { title: "Provincial Sport", contact: "MPP/MLA", items: ["Provincial sport organizations", "Provincial funding", "Provincial games", "School sports policy"] },
    municipal: { title: "Local Recreation", contact: "Councillor", items: ["Arenas and pools", "Community centres", "Local programs", "Sports fields", "Youth athletics"] }
  },
  religion: {
    federal: { title: "Federal Religious Rights", contact: "MP", items: ["Charter of Rights", "Canadian Human Rights Act", "Official Languages", "Multiculturalism", "Interfaith initiatives"] },
    provincial: { title: "Provincial Religious Affairs", contact: "MPP/MLA", items: ["Provincial human rights", "Faith-based schools", "Religious accommodations", "Provincial multiculturalism"] },
    municipal: { title: "Local Interfaith", contact: "Councillor", items: ["Places of worship zoning", "Interfaith events", "Community partnerships", "Local multiculturalism"] }
  },
  volunteer: {
    federal: { title: "Federal Volunteer Programs", contact: "MP", items: ["Canada Service Corps", "Charitable status", "National volunteer initiatives", "Federal funding programs"] },
    provincial: { title: "Provincial Community", contact: "MPP/MLA", items: ["Provincial volunteer programs", "Nonprofit support", "Provincial grants", "Community services"] },
    municipal: { title: "Local Volunteer", contact: "Councillor", items: ["Volunteer centres", "Community grants", "Local programs", "Civic engagement"] }
  },
  legalaid: {
    federal: { title: "Federal Justice", contact: "MP", items: ["Federal courts", "Criminal Code", "Access to justice funding", "Supreme Court", "Federal legal aid (limited)"] },
    provincial: { title: "Provincial Legal Aid", contact: "MPP/MLA", items: ["Legal aid plans", "Provincial courts", "Duty counsel", "Community clinics", "Family law aid"] },
    municipal: { title: "Local Justice Support", contact: "Councillor", items: ["Community legal clinics", "Local justice programs", "Municipal bylaw courts", "Community mediation"] }
  },
  pensions: {
    federal: { title: "Federal Pensions", contact: "MP", items: ["Canada Pension Plan", "Old Age Security", "Guaranteed Income Supplement", "Federal pension standards", "RRSP rules"] },
    provincial: { title: "Provincial Pensions", contact: "MPP/MLA", items: ["Provincial pension plans", "Provincial pension standards", "Locked-in accounts", "Provincial supplements"] },
    municipal: { title: "Local Senior Support", contact: "Councillor", items: ["Senior programs", "Property tax deferral", "Local pension info", "Community services"] }
  },
  childcare: {
    federal: { title: "Federal Childcare", contact: "MP", items: ["Canada-wide early learning", "Federal funding", "Indigenous childcare", "National standards"] },
    provincial: { title: "Provincial Childcare", contact: "MPP/MLA", items: ["Provincial childcare systems", "Licensing", "Subsidies", "Fee caps", "Worker wages"] },
    municipal: { title: "Local Childcare", contact: "Councillor", items: ["Municipal programs", "Before/after school", "Local centres", "Community spaces"] }
  },
  food: {
    federal: { title: "Federal Food Security", contact: "MP", items: ["Nutrition North Canada", "Food safety", "Agriculture policy", "Food price monitoring", "Northern subsidies"] },
    provincial: { title: "Provincial Food", contact: "MPP/MLA", items: ["Provincial food security", "School nutrition", "Provincial food banks", "Food safety inspection"] },
    municipal: { title: "Local Food", contact: "Councillor", items: ["Food banks", "Community gardens", "School programs", "Local food policy"] }
  },
  emergency: {
    federal: { title: "Federal Emergency", contact: "MP", items: ["Public Safety Canada", "National alerts", "Disaster assistance", "Search and rescue", "Coast Guard"] },
    provincial: { title: "Provincial Emergency", contact: "MPP/MLA", items: ["Provincial EMO", "911 systems", "Provincial disaster response", "Search and rescue", "Emergency plans"] },
    municipal: { title: "Local Emergency", contact: "Councillor", items: ["Fire services", "Paramedics", "Local emergency plans", "Emergency shelters", "Local alerts"] }
  },
  humanrights: {
    federal: { title: "Federal Human Rights", contact: "MP", items: ["Canadian Human Rights Commission", "Charter of Rights", "Criminal Code hate provisions", "Official Languages", "International treaties"] },
    provincial: { title: "Provincial Human Rights", contact: "MPP/MLA", items: ["Provincial human rights codes", "Provincial tribunals", "Provincial accessibility laws", "Provincial anti-racism"] },
    municipal: { title: "Local Human Rights", contact: "Councillor", items: ["Municipal inclusivity", "Local human rights", "Community programs", "Anti-discrimination policies"] }
  }
};

// JURISDICTION HEADERS - FRENCH

const JURISDICTION_HEADERS_FR = {
  infrastructure: {
    federal: { title: "Transports nationaux", contact: "député", items: ["Autoroutes interprovinciales", "Sécurité ferroviaire", "Aviation", "Ports", "Politique nationale des transports"] },
    provincial: { title: "Infrastructure provinciale", contact: "député provincial", items: ["Autoroutes provinciales", "Financement du transport en commun", "Permis de conduire", "Entretien des routes provinciales"] },
    municipal: { title: "Infrastructure locale", contact: "conseiller", items: ["Rues municipales", "Trottoirs", "Transport en commun local", "Stationnement", "Éclairage des rues", "Dénéigement", "Nids-de-poule"] }
  },
  healthcare: {
    federal: { title: "Normes de santé nationales", contact: "député", items: ["Loi canadienne sur la santé", "Santé des Premières Nations", "Approbation des médicaments (Santé Canada)", "Recherche en santé nationale"] },
    provincial: { title: "Soins de santé provinciaux", contact: "député provincial", items: ["Financement des hôpitaux", "Permis des médecins", "Régimes médicamenteux provinciaux", "Temps d'attente", "Soins de longue durée", "Services de santé mentale"] },
    municipal: { title: "Services de santé locaux", contact: "conseiller", items: ["Unités de santé publique", "Ambulances (certaines provinces)", "Programmes de santé locaux"] }
  },
  education: {
    federal: { title: "Programmes éducatifs nationaux", contact: "député", items: ["Prêts étudiants", "Financement de l'éducation autochtone", "Langues officielles", "Subventions de recherche"] },
    provincial: { title: "Éducation provinciale", contact: "député provincial", items: ["Programme de la maternelle à la 12e année", "Conseils scolaires", "Financement universitaire", "Certification des enseignants", "Éducation spécialisée"] },
    municipal: { title: "Questions scolaires locales", contact: "conseiller", items: ["Zones scolaires", "Garderies de passage", "Impôts fonciers municipaux pour les écoles"] }
  },
  housing: {
    federal: { title: "Programmes de logement nationaux", contact: "député", items: ["Programmes de la SCHL", "Stratégie nationale sur le logement", "Règles hypothécaires", "Financement du logement abordable"] },
    provincial: { title: "Logement provincial", contact: "député provincial", items: ["Contrôle des loyers", "Litiges locataire-propriétaire", "Programmes de logement provinciaux", "Codes du bâtiment"] },
    municipal: { title: "Logement et zonage locaux", contact: "conseiller", items: ["Règlements de zonage", "Permis d'aménagement", "Impôts fonciers", "Règles sur les locations à court terme", "Refuges pour sans-abri"] }
  },
  environment: {
    federal: { title: "Parcs et environnement nationaux", contact: "député", items: ["Parcs nationaux", "Parcs Canada", "Politique climatique", "Espèces en péril", "Évaluations environnementales", "Protection des océans"] },
    provincial: { title: "Parcs et environnement provinciaux", contact: "député provincial", items: ["Parcs provinciaux", "Zones de conservation", "Règles environnementales provinciales", "Gestion de la faune", "Qualité de l'eau"] },
    municipal: { title: "Parcs et environnement locaux", contact: "conseiller", items: ["Parcs municipaux", "Terrains de jeu", "Terrains de sport", "Jardins communautaires", "Recyclage local", "Collecte des ordures"] }
  },
  safety: {
    federal: { title: "Justice et sécurité fédérales", contact: "député", items: ["Droit criminel", "Prisons fédérales", "GRC (contrat)", "Sécurité frontalière", "Sécurité nationale"] },
    provincial: { title: "Justice provinciale", contact: "député provincial", items: ["Tribunaux provinciaux", "Prisons provinciales", "Police provinciale", "Aide juridique", "Services aux victimes"] },
    municipal: { title: "Sécurité locale", contact: "conseiller", items: ["Police municipale", "Services d'incendie", "Application des règlements", "Gestion des urgences", "Programmes de sécurité locaux"] }
  },
  employment: {
    federal: { title: "Emploi fédéral", contact: "député", items: ["Assurance-emploi", "Code canadien du travail", "Travailleurs étrangers", "Salaire minimum fédéral", "Régime de pensions (RPC)"] },
    provincial: { title: "Emploi provincial", contact: "député provincial", items: ["Normes d'emploi", "Indemnisation des travailleurs", "Relations de travail", "Salaire minimum provincial", "Santé et sécurité au travail"] },
    municipal: { title: "Programmes d'emploi locaux", contact: "conseiller", items: ["Programmes d'emploi locaux", "Permis d'entreprise", "Développement économique"] }
  },
  social: {
    federal: { title: "Programmes sociaux fédéraux", contact: "député", items: ["Allocation canadienne pour enfants", "Sécurité de la vieillesse", "Assurance-emploi", "Crédit d'impôt pour personnes handicapées", "Services d'établissement"] },
    provincial: { title: "Services sociaux provinciaux", contact: "député provincial", items: ["Aide sociale", "Programmes provinciaux pour personnes handicapées", "Protection de l'enfance", "Subventions au logement"] },
    municipal: { title: "Services sociaux locaux", contact: "conseiller", items: ["Refuges locaux", "Coordination des banques alimentaires", "Services communautaires", "Programmes récréatifs"] }
  },
  taxes: {
    federal: { title: "Impôts fédéraux", contact: "député", items: ["Impôt sur le revenu", "TPS", "Allocation canadienne pour enfants", "Prix du carbone", "Impôt des sociétés", "Crédits d'impôt"] },
    provincial: { title: "Impôts provinciaux", contact: "député provincial", items: ["Impôt sur le revenu provincial", "Taxe de vente provinciale", "Évaluation foncière", "Crédits d'impôt provinciaux"] },
    municipal: { title: "Impôts et frais locaux", contact: "conseiller", items: ["Taux d'imposition foncière", "Factures d'eau", "Amendes de stationnement", "Frais de permis", "Contributions aux améliorations locales"] }
  },
  immigration: {
    federal: { title: "Immigration et citoyenneté", contact: "député", items: ["Résidence permanente", "Permis de travail et d'études", "Citoyenneté", "Demandes d'asile", "Parrainage familial", "Visas de visiteur"] },
    provincial: { title: "Immigration provinciale", contact: "député provincial", items: ["Programmes des candidats provinciaux", "Services d'établissement provinciaux"] },
    municipal: { title: "Services aux nouveaux arrivants locaux", contact: "conseiller", items: ["Agences d'établissement locales", "Programmes d'intégration communautaire", "Cours de langue (installations municipales)"] }
  },
  consumer: {
    federal: { title: "Protection des consommateurs fédérale", contact: "député", items: ["Vie privée (LPRPDE)", "Plaintes télécom (CRTC)", "Plaintes bancaires", "Sécurité des produits", "Loi sur la concurrence"] },
    provincial: { title: "Affaires consuméristes provinciales", contact: "député provincial", items: ["Lois sur la protection des consommateurs", "Exécution des garanties", "Publicité mensongère", "Locataire-propriétaire (certaines provinces)", "Tribunaux des consommateurs provinciaux"] },
    municipal: { title: "Questions consuméristes locales", contact: "conseiller", items: ["Permis d'entreprise", "Plaintes de règlements locaux", "Facturation des services municipaux"] }
  },
  indigenous: {
    federal: { title: "Affaires autochtones", contact: "député", items: ["Cartes de statut", "Droits issus des traités", "Terres de réserve", "Éducation des Premières Nations", "Avantages de santé non assurés", "Femmes autochtones disparues"] },
    provincial: { title: "Relations autochtones provinciales", contact: "député provincial", items: ["Affaires autochtones provinciales", "Accords sur le bien-être des enfants", "Consultation sur les ressources", "Programmes provinciaux"] },
    municipal: { title: "Relations autochtones locales", contact: "conseiller", items: ["Programmes autochtones urbains", "Relations municipal-Premières Nations", "Initiatives culturelles locales"] }
  },
  seniors: {
    federal: { title: "Programmes pour aînés fédéraux", contact: "député", items: ["Sécurité de la vieillesse", "Supplément de revenu garanti", "Retraite du RPC", "Régime de pensions du Canada", "Initiatives pour aînés fédérales"] },
    provincial: { title: "Services pour aînés provinciaux", contact: "député provincial", items: ["Suppléments provinciaux pour aînés", "Réglementation des soins de longue durée", "Programmes de soins à domicile", "Avantages pharmaceutiques provinciaux", "Programmes de logement pour aînés"] },
    municipal: { title: "Services pour aînés locaux", contact: "conseiller", items: ["Centres pour aînés", "Report des impôts fonciers", "Programmes locaux pour aînés", "Transport communautaire"] }
  },
  veterans: {
    federal: { title: "Affaires des anciens combattants", contact: "député", items: ["Prestations d'invalidité", "Pension des anciens combattants", "Programme pour l'autonomie des vétérans", "Services de santé mentale", "Dossiers de service", "Assistance funéraire"] },
    provincial: { title: "Services aux vétérans provinciaux", contact: "député provincial", items: ["Avantages provinciaux pour vétérans", "Programmes de reconnaissance provinciaux"] },
    municipal: { title: "Soutien aux vétérans local", contact: "conseiller", items: ["Événements locaux pour vétérans", "Cérémonies du Souvenir", "Programmes de soutien communautaire"] }
  },
  disability: {
    federal: { title: "Programmes fédéraux pour personnes handicapées", contact: "député", items: ["Pension d'invalidité du RPC", "Crédit d'impôt pour personnes handicapées", "Prestation canadienne pour personnes handicapées", "Régime enregistré d'épargne-invalidité", "Législation sur l'accessibilité"] },
    provincial: { title: "Services provinciaux pour personnes handicapées", contact: "député provincial", items: ["Soutien provincial pour personnes handicapées (ODSP, AISH, PWD)", "Lois provinciales sur l'accessibilité", "Programmes provinciaux pour personnes handicapées"] },
    municipal: { title: "Accessibilité locale", contact: "conseiller", items: ["Permis de stationnement accessible", "Normes d'accessibilité municipales", "Programmes locaux d'accessibilité", "Services de paratransit"] }
  },
  youth: {
    federal: { title: "Programmes pour la jeunesse fédéraux", contact: "député", items: ["Prêts étudiants", "Programme d'emploi pour les jeunes", "Bon d'études canadien", "Subventions pour apprentis", "Corps de service canadien"] },
    provincial: { title: "Jeunesse et éducation provinciales", contact: "député provincial", items: ["Aide financière provinciale", "Justice pour les jeunes", "Programmes provinciaux pour la jeunesse", "Financement de l'éducation"] },
    municipal: { title: "Services pour la jeunesse locaux", contact: "conseiller", items: ["Centres de jeunesse", "Programmes récréatifs", "Emploi local pour les jeunes", "Programmes communautaires"] }
  },
  agriculture: {
    federal: { title: "Agriculture fédérale", contact: "député", items: ["Soutien au revenu agricole (Agri-stabilité)", "Recherche agricole", "Financement de l'internet rural", "Gestion de l'offre", "Accords commerciaux"] },
    provincial: { title: "Agriculture provinciale", contact: "député provincial", items: ["Programmes agricoles provinciaux", "Protection des terres agricoles", "Subventions provinciales", "Sécurité à la ferme", "Conservation des sols et de l'eau"] },
    municipal: { title: "Questions rurales locales", contact: "conseiller", items: ["Zonage rural", "Drainage local", "Règlements agricoles", "Entretien des routes rurales"] }
  },
  utilities: {
    federal: { title: "Télécom et services publics fédéraux", contact: "député", items: ["Plaintes Internet/câble (CRTC)", "Réglementation télécom", "Attribution du spectre", "Stratégie nationale pour l'internet à large bande"] },
    provincial: { title: "Services publics provinciaux", contact: "député provincial", items: ["Tarifs d'électricité", "Réglementation du gaz naturel", "Commissions des services publics provinciaux", "Règles de comptage net"] },
    municipal: { title: "Services publics locaux", contact: "conseiller", items: ["Facturation de l'eau", "Litiges de services publics locaux", "Eau/égouts municipaux", "Agrégation communautaire"] }
  },
  family: {
    federal: { title: "Droit de la famille fédéral", contact: "député", items: ["Loi sur le divorce", "Lignes directrices sur la pension alimentaire", "Tribunaux familiaux fédéraux", "Définition du mariage"] },
    provincial: { title: "Droit de la famille provincial", contact: "député provincial", items: ["Tribunaux familiaux", "Protection de l'enfance (SPE)", "Services familiaux provinciaux", "Partage des biens", "Exécution de la pension alimentaire"] },
    municipal: { title: "Services familiaux locaux", contact: "conseiller", items: ["Permis de mariage (via la province)", "Programmes familiaux locaux", "Services communautaires"] }
  },
  arts: {
    federal: { title: "Arts et culture fédéraux", contact: "député", items: ["Conseil des Arts du Canada", "Patrimoine canadien", "Crédits d'impôt pour le cinéma/TV", "Musées nationaux", "Langues officielles"] },
    provincial: { title: "Financement des arts provincial", contact: "député provincial", items: ["Conseils des arts provinciaux", "Patrimoine provincial", "Musées provinciaux", "Programmes culturels"] },
    municipal: { title: "Arts et culture locaux", contact: "conseiller", items: ["Subventions artistiques municipales", "Musées locaux", "Centres communautaires", "Art public", "Festivals", "Désignation patrimoniale"] }
  },
  lgbtq: {
    federal: { title: "Droits LGBTQ+ fédéraux", contact: "député", items: ["Protections du Code criminel", "Loi canadienne sur les droits de la personne", "Interdiction de la thérapie de conversion", "Protections en milieu de travail fédéral", "Immigration pour partenaires de même sexe"] },
    provincial: { title: "Droits LGBTQ+ provinciaux", contact: "député provincial", items: ["Codes des droits de la personne provinciaux", "Couverture des soins de santé", "Politiques éducatives provinciales", "Protections en milieu de travail provincial", "Changements de nom/genre"] },
    municipal: { title: "Soutien LGBTQ+ local", contact: "conseiller", items: ["Événements Fierté", "Programmes communautaires", "Politiques d'inclusivité municipales", "Anti-discrimination local"] }
  },
  women: {
    federal: { title: "Programmes pour les femmes fédéraux", contact: "député", items: ["Femmes et Égalité des Genres Canada", "Loi sur l'équité salariale", "Prestations de maternité/parentales", "Financement fédéral contre la violence fondée sur le genre", "Suivi de l'enquête nationale"] },
    provincial: { title: "Services pour les femmes provinciaux", contact: "député provincial", items: ["Bureaux provinciaux pour les femmes", "Financement des refuges", "Équité salariale provinciale", "Soins de santé reproductive", "Lignes de crise pour les femmes"] },
    municipal: { title: "Soutien aux femmes local", contact: "conseiller", items: ["Refuges pour femmes", "Services de crise locaux", "Programmes municipaux pour les femmes", "Initiatives de sécurité communautaire"] }
  },
  mentalhealth: {
    federal: { title: "Santé mentale fédérale", contact: "député", items: ["Financement de la santé mentale", "Normes nationales de santé mentale", "Ligne de crise 988", "Santé mentale en milieu de travail fédéral", "Financement de la recherche"] },
    provincial: { title: "Santé mentale provinciale", contact: "député provincial", items: ["Plans provinciaux de santé mentale", "Services psychiatriques hospitaliers", "Santé mentale communautaire", "Lignes de crise provinciales", "Services de toxicomanie"] },
    municipal: { title: "Santé mentale locale", contact: "conseiller", items: ["Programmes communautaires", "Réponse locale aux crises", "Santé mentale en santé publique", "Programmes des centres communautaires"] }
  },
  substance: {
    federal: { title: "Politique sur les substances fédérale", contact: "député", items: ["Loi sur les drogues contrôlées", "Programmes d'approvisionnement sécuritaire", "Financement fédéral de la toxicomanie", "Réponse aux opioïdes", "Surveillance de Santé Canada"] },
    provincial: { title: "Services de toxicomanie provinciaux", contact: "député provincial", items: ["Centres de traitement", "Programmes de réduction des méfaits", "Réponse provinciale aux opioïdes", "Logements de rétablissement", "Distribution de naloxone"] },
    municipal: { title: "Soutien à la toxicomanie local", contact: "conseiller", items: ["Sites de consommation supervisée", "Réduction des méfaits locale", "Programmes communautaires", "Services d'approche"] }
  },
  transportation: {
    federal: { title: "Transports fédéraux", contact: "député", items: ["Politique nationale des transports", "Financement du transport rural", "Normes d'accessibilité", "Droits des passagers aériens", "Sécurité ferroviaire"] },
    provincial: { title: "Transports provinciaux", contact: "député provincial", items: ["Autoroutes provinciales", "Financement du transport en commun provincial", "Permis de conduire", "Entretien des routes provinciales", "Normes de paratransit"] },
    municipal: { title: "Transports locaux", contact: "conseiller", items: ["Transport en commun local", "Transport actif", "Stationnement", "Routes locales", "Accessibilité"] }
  },
  digital: {
    federal: { title: "Droits numériques fédéraux", contact: "député", items: ["Loi LPRPDE sur la vie privée", "Réglementation télécom du CRTC", "Loi sur les méfaits en ligne", "Normes d'identité numérique", "Cybersécurité"] },
    provincial: { title: "Numérique provincial", contact: "député provincial", items: ["Lois provinciales sur la vie privée", "Identité numérique provinciale", "Protection des consommateurs provinciale", "Cybersécurité provinciale"] },
    municipal: { title: "Services numériques locaux", contact: "conseiller", items: ["Services numériques municipaux", "Internet local à large bande", "Confidentialité des données municipales", "Wi-Fi communautaire"] }
  },
  animals: {
    federal: { title: "Protection des animaux fédérale", contact: "député", items: ["Cruauté du Code criminel", "Loi sur les espèces en péril", "Nourriture pour animaux de Santé Canada", "Santé animale de l'ACIA", "Règles d'importation/exportation"] },
    provincial: { title: "Bien-être animal provincial", contact: "député provincial", items: ["SPCA provinciaux", "Lois provinciales sur le bien-être animal", "Protection de la faune", "Normes pour les animaux de ferme", "Règles sur les animaux exotiques"] },
    municipal: { title: "Services animaux locaux", contact: "conseiller", items: ["Contrôle des animaux", "Permis pour animaux de compagnie", "Refuges locaux", "Application des règlements", "Parcs pour chiens"] }
  },
  sports: {
    federal: { title: "Sport fédéral", contact: "député", items: ["Sport Canada", "Aide aux athlètes", "Sport sécuritaire", "Organisations sportives nationales", "Anti-dopage"] },
    provincial: { title: "Sport provincial", contact: "député provincial", items: ["Organisations sportives provinciales", "Financement provincial", "Jeux provinciaux", "Politique sportive scolaire"] },
    municipal: { title: "Loisirs locaux", contact: "conseiller", items: ["Arénas et piscines", "Centres communautaires", "Programmes locaux", "Terrains de sport", "Athlétisme jeunesse"] }
  },
  religion: {
    federal: { title: "Droits religieux fédéraux", contact: "député", items: ["Charte des droits", "Loi canadienne sur les droits de la personne", "Langues officielles", "Multiculturalisme", "Initiatives interreligieuses"] },
    provincial: { title: "Affaires religieuses provinciales", contact: "député provincial", items: ["Droits de la personne provinciaux", "Écoles confessionnelles", "Accommodements religieux", "Multiculturalisme provincial"] },
    municipal: { title: "Interreligieux local", contact: "conseiller", items: ["Zonage des lieux de culte", "Événements interreligieux", "Partenariats communautaires", "Multiculturalisme local"] }
  },
  volunteer: {
    federal: { title: "Programmes de bénévolat fédéraux", contact: "député", items: ["Corps de service canadien", "Statut d'organisme de bienfaisance", "Initiatives nationales de bénévolat", "Programmes de financement fédéraux"] },
    provincial: { title: "Communauté provinciale", contact: "député provincial", items: ["Programmes provinciaux de bénévolat", "Soutien aux organismes sans but lucratif", "Subventions provinciales", "Services communautaires"] },
    municipal: { title: "Bénévolat local", contact: "conseiller", items: ["Centres de bénévolat", "Subventions communautaires", "Programmes locaux", "Engagement civique"] }
  },
  legalaid: {
    federal: { title: "Justice fédérale", contact: "député", items: ["Tribunaux fédéraux", "Code criminel", "Financement de l'accès à la justice", "Cour suprême", "Aide juridique fédérale (limitée)"] },
    provincial: { title: "Aide juridique provinciale", contact: "député provincial", items: ["Régimes d'aide juridique", "Tribunaux provinciaux", "Avocat de service", "Cliniques communautaires", "Aide juridique familiale"] },
    municipal: { title: "Soutien à la justice local", contact: "conseiller", items: ["Cliniques juridiques communautaires", "Programmes de justice locaux", "Tribunaux de règlements municipaux", "Médiation communautaire"] }
  },
  pensions: {
    federal: { title: "Pensions fédérales", contact: "député", items: ["Régime de pensions du Canada", "Sécurité de la vieillesse", "Supplément de revenu garanti", "Normes de pensions fédérales", "Règles des REER"] },
    provincial: { title: "Pensions provinciales", contact: "député provincial", items: ["Régimes de pension provinciaux", "Normes de pensions provinciales", "Comptes bloqués", "Suppléments provinciaux"] },
    municipal: { title: "Soutien aux aînés local", contact: "conseiller", items: ["Programmes pour aînés", "Report des impôts fonciers", "Informations sur les pensions locales", "Services communautaires"] }
  },
  childcare: {
    federal: { title: "Garde d'enfants fédérale", contact: "député", items: ["Apprentissage pancanadien pour les jeunes enfants", "Financement fédéral", "Garde d'enfants autochtone", "Normes nationales"] },
    provincial: { title: "Garde d'enfants provinciale", contact: "député provincial", items: ["Systèmes de garde provinciaux", "Permis", "Subventions", "Plafonds des frais", "Salaires des travailleurs"] },
    municipal: { title: "Garde d'enfants locale", contact: "conseiller", items: ["Programmes municipaux", "Garde avant/après l'école", "Centres locaux", "Espaces communautaires"] }
  },
  food: {
    federal: { title: "Sécurité alimentaire fédérale", contact: "député", items: ["Nutrition Nord Canada", "Sécurité alimentaire", "Politique agricole", "Surveillance des prix alimentaires", "Subventions nordiques"] },
    provincial: { title: "Alimentation provinciale", contact: "député provincial", items: ["Sécurité alimentaire provinciale", "Nutrition scolaire", "Banques alimentaires provinciales", "Inspection de la sécurité alimentaire"] },
    municipal: { title: "Alimentation locale", contact: "conseiller", items: ["Banques alimentaires", "Jardins communautaires", "Programmes scolaires", "Politique alimentaire locale"] }
  },
  emergency: {
    federal: { title: "Urgences fédérales", contact: "député", items: ["Sécurité publique Canada", "Alertes nationales", "Aide aux sinistrés", "Recherche et sauvetage", "Garde côtière"] },
    provincial: { title: "Urgences provinciales", contact: "député provincial", items: ["Organismes provinciaux de gestion des urgences", "Systèmes 911", "Réponse aux catastrophes provinciales", "Recherche et sauvetage", "Plans d'urgence"] },
    municipal: { title: "Urgences locales", contact: "conseiller", items: ["Services d'incendie", "Services paramédicaux", "Plans d'urgence locaux", "Refuges d'urgence", "Alertes locales"] }
  },
  humanrights: {
    federal: { title: "Droits de la personne fédéraux", contact: "député", items: ["Commission canadienne des droits de la personne", "Charte des droits", "Dispositions du Code criminel sur la haine", "Langues officielles", "Traités internationaux"] },
    provincial: { title: "Droits de la personne provinciaux", contact: "député provincial", items: ["Codes provinciaux des droits de la personne", "Tribunaux provinciaux", "Lois provinciales sur l'accessibilité", "Anti-racisme provincial"] },
    municipal: { title: "Droits de la personne locaux", contact: "conseiller", items: ["Inclusivité municipale", "Droits de la personne locaux", "Programmes communautaires", "Politiques anti-discrimination"] }
  }
};


// STORY PROMPTS

export { JURISDICTION_HEADERS, JURISDICTION_HEADERS_FR };
