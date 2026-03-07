// Lookup data for My Civic Voice

const MUNICIPAL_BACKUP_LINKS = {
    'Toronto': { url: 'https://www.toronto.ca/council/', name: 'Toronto City Council', find: 'Find your councillor by postal code' },
    'Montreal': { url: 'https://ville.montreal.qc.ca/portal/page?_pageid=5798,42649578&_dad=portal&_schema=PORTAL', name: 'Ville de Montréal', find: 'Trouvez votre arrondissement' },
    'Vancouver': { url: 'https://vancouver.ca/your-government/find-your-councillor.aspx', name: 'City of Vancouver', find: 'Find your councillor' },
    'Calgary': { url: 'https://www.calgary.ca/councillors/find-your-councillor.html', name: 'City of Calgary', find: 'Find your councillor' },
    'Edmonton': { url: 'https://www.edmonton.ca/city_government/municipal_elections/find-your-ward', name: 'City of Edmonton', find: 'Find your ward' },
    'Ottawa': { url: 'https://app05.ottawa.ca/sirepub/alpha.aspx', name: 'City of Ottawa', find: 'Find your councillor' },
    'Winnipeg': { url: 'https://winnipeg.ca/council/', name: 'City of Winnipeg', find: 'Find your councillor' },
    'Mississauga': { url: 'https://www.mississauga.ca/council/find-your-councillor/', name: 'City of Mississauga', find: 'Find your councillor' },
    'Halifax': { url: 'https://www.halifax.ca/council-committees/councillors-find-your-councillor', name: 'Halifax Regional Municipality', find: 'Find your councillor' },
    'Quebec City': { url: 'https://www.ville.quebec.qc.ca/conseil_municipal/conseillers/index.aspx', name: 'Ville de Québec', find: 'Trouvez votre conseiller' },
    'Hamilton': { url: 'https://www.hamilton.ca/council-committees/councillors/find-your-councillor', name: 'City of Hamilton', find: 'Find your councillor' },
    'Brampton': { url: 'https://www.brampton.ca/EN/City-Hall/Council/Pages/Welcome.aspx', name: 'City of Brampton', find: 'Find your councillor' },
    'Surrey': { url: 'https://www.surrey.ca/council/find-your-councillor', name: 'City of Surrey', find: 'Find your councillor' },
    'Laval': { url: 'https://www.laval.ca/conseil-municipal/conseillers-ville-laval', name: 'Ville de Laval', find: 'Trouvez votre conseiller' },
    'London': { url: 'https://london.ca/city-council/find-your-councillor', name: 'City of London', find: 'Find your councillor' },
    'Victoria': { url: 'https://www.victoria.ca/EN/main/government/mayor-council/councillors.html', name: 'City of Victoria', find: 'Find your councillor' },
    'Regina': { url: 'https://www.regina.ca/council/find-your-councillor/', name: 'City of Regina', find: 'Find your councillor' },
    'Saskatoon': { url: 'https://www.saskatoon.ca/city-government/mayor-city-councillors', name: 'City of Saskatoon', find: 'Find your councillor' }
  };

const PROVINCIAL_BACKUP_LINKS = {
    'Ontario': { url: 'https://www.ola.org/en/members', name: 'Ontario Legislative Assembly', find: 'Find your MPP by postal code' },
    'British Columbia': { url: 'https://www.leg.bc.ca/members', name: 'BC Legislature', find: 'Find your MLA by postal code' },
    'Quebec': { url: 'https://www.assnat.qc.ca/fr/deputes/index.html', name: 'Assemblée nationale du Québec', find: 'Trouvez votre député' },
    'Alberta': { url: 'https://www.assembly.ab.ca/members', name: 'Alberta Legislature', find: 'Find your MLA by postal code' },
    'Manitoba': { url: 'https://www.gov.mb.ca/legislature/members/mla.html', name: 'Manitoba Legislature', find: 'Find your MLA by postal code' },
    'Saskatchewan': { url: 'https://www.legassembly.sk.ca/mlas/', name: 'Saskatchewan Legislature', find: 'Find your MLA by postal code' },
    'Nova Scotia': { url: 'https://nslegislature.ca/members/profiles', name: 'Nova Scotia Legislature', find: 'Find your MLA by postal code' },
    'New Brunswick': { url: 'https://www.legnb.ca/en/members', name: 'New Brunswick Legislature', find: 'Find your MLA by postal code' },
    'Newfoundland and Labrador': { url: 'https://www.assembly.nl.ca/members', name: 'NL Legislature', find: 'Find your MHA by postal code' },
    'Prince Edward Island': { url: 'https://www.assembly.pe.ca/members', name: 'PEI Legislature', find: 'Find your MLA by postal code' },
    'Yukon': { url: 'https://yukonlegislativeassembly.ca/mlas', name: 'Yukon Legislature', find: 'Find your MLA by postal code' },
    'Northwest Territories': { url: 'https://www.ntassembly.ca/members', name: 'NWT Legislature', find: 'Find your MLA by postal code' },
    'Nunavut': { url: 'https://www.nuassembly.ca/en/members', name: 'Nunavut Legislature', find: 'Find your MLA by postal code' }
  };

const CITY_PROVINCE = {
    'Toronto': 'Ontario', 'Montreal': 'Quebec', 'Vancouver': 'British Columbia', 'Calgary': 'Alberta',
    'Edmonton': 'Alberta', 'Ottawa': 'Ontario', 'Winnipeg': 'Manitoba', 'Mississauga': 'Ontario',
    'Halifax': 'Nova Scotia', 'Quebec City': 'Quebec', 'Hamilton': 'Ontario', 'Brampton': 'Ontario',
    'Surrey': 'British Columbia', 'Laval': 'Quebec', 'London': 'Ontario', 'Markham': 'Ontario',
    'Vaughan': 'Ontario', 'Gatineau': 'Quebec', 'Saskatoon': 'Saskatchewan', 'Longueuil': 'Quebec',
    'Kitchener': 'Ontario', 'Burnaby': 'British Columbia', 'Windsor': 'Ontario', 'Regina': 'Saskatchewan',
    'Richmond': 'British Columbia', 'Burlington': 'Ontario', 'Richmond Hill': 'Ontario', 'Oakville': 'Ontario',
    'Sherbrooke': 'Quebec', 'Saint John': 'New Brunswick', "St. John's": 'Newfoundland and Labrador', 'Victoria': 'British Columbia',
    'Fredericton': 'New Brunswick', 'Charlottetown': 'Prince Edward Island', 'Yellowknife': 'Northwest Territories', 'Whitehorse': 'Yukon',
    'Iqaluit': 'Nunavut', 'Thunder Bay': 'Ontario', 'Sudbury': 'Ontario', 'Sault Ste. Marie': 'Ontario',
    'North Bay': 'Ontario', 'Trois-Rivières': 'Quebec', 'Toronto (Scarborough)': 'Ontario',
    'Toronto (North York)': 'Ontario', 'Toronto (Etobicoke)': 'Ontario', 'Montreal (Lachine)': 'Quebec',
    'Montreal (Verdun)': 'Quebec', 'Vancouver (Surrey)': 'British Columbia', 'Vancouver (Burnaby)': 'British Columbia'
  };

const PROVINCE_REPS = {
    'Ontario': { provincial: 'ontario-legislature', federal: 'house-of-commons' },
    'British Columbia': { provincial: 'bc-legislature', federal: 'house-of-commons' },
    'Quebec': { provincial: 'quebec-national-assembly', federal: 'house-of-commons' },
    'Alberta': { provincial: 'alberta-legislature', federal: 'house-of-commons' },
    'Manitoba': { provincial: 'manitoba-legislature', federal: 'house-of-commons' },
    'Saskatchewan': { provincial: 'saskatchewan-legislature', federal: 'house-of-commons' },
    'Nova Scotia': { provincial: 'nova-scotia-legislature', federal: 'house-of-commons' },
    'New Brunswick': { provincial: 'new-brunswick-legislature', federal: 'house-of-commons' },
    'Newfoundland and Labrador': { provincial: 'newfoundland-labrador-legislature', federal: 'house-of-commons' },
    'Prince Edward Island': { provincial: 'pei-legislature', federal: 'house-of-commons' },
    'Yukon': { provincial: 'yukon-legislature', federal: 'house-of-commons' },
    'Northwest Territories': { provincial: 'nwt-legislature', federal: 'house-of-commons' },
    'Nunavut': { provincial: 'nunavut-legislature', federal: 'house-of-commons' }
  };

export { MUNICIPAL_BACKUP_LINKS, PROVINCIAL_BACKUP_LINKS, CITY_PROVINCE, PROVINCE_REPS };
