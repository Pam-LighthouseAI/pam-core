# Build comprehensive municipal lookup data for Canada
# This script generates the escalation_data.js file

# Major cities with 311 service - add website field
cities_with_311 = {
    "Ottawa City Council": {"has311": True, "phone": "311", "website": "ottawa.ca"},
    "Toronto City Council": {"has311": True, "phone": "311", "website": "toronto.ca"},
    "Vancouver City Council": {"has311": True, "phone": "311", "website": "vancouver.ca"},
    "Calgary City Council": {"has311": True, "phone": "311", "website": "calgary.ca"},
    "Edmonton City Council": {"has311": True, "phone": "311", "website": "edmonton.ca"},
    "Winnipeg City Council": {"has311": True, "phone": "311", "website": "winnipeg.ca"},
    "Mississauga City Council": {"has311": True, "phone": "311", "website": "mississauga.ca"},
    "Montreal City Council": {"has311": True, "phone": "311", "website": "montreal.ca"},
    "Brampton City Council": {"has311": True, "phone": "311", "website": "brampton.ca"},
    "Laval City Council": {"has311": True, "phone": "311", "website": "laval.ca"},
    "Halifax Regional Council": {"has311": True, "phone": "311", "website": "halifax.ca"},
    "Gatineau City Council": {"has311": True, "phone": "311", "website": "gatineau.ca"},
    "Longueuil City Council": {"has311": True, "phone": "311", "website": "longueuil.quebec"},
    "Greater Sudbury City Council": {"has311": True, "phone": "311", "website": "greatersudbury.ca"},
    "Windsor City Council": {"has311": True, "phone": "311", "website": "citywindsor.ca"},
    "St. John's City Council": {"has311": True, "phone": "311", "website": "stjohns.ca"},
}

# Cities without 311 - need main website
cities_without_311 = {
    "Quebec City Council": {"has311": False, "website": "quebec.ca"},
    "Hamilton City Council": {"has311": False, "website": "hamilton.ca"},
    "Surrey City Council": {"has311": False, "website": "surrey.ca"},
    "London City Council": {"has311": False, "website": "london.ca"},
    "Victoria City Council": {"has311": False, "website": "victoria.ca"},
    "Regina City Council": {"has311": False, "website": "regina.ca"},
    "Saskatoon City Council": {"has311": False, "website": "saskatoon.ca"},
    "Saint John City Council": {"has311": False, "website": "saintjohn.ca"},
    "Fredericton City Council": {"has311": False, "website": "fredericton.ca"},
    "Charlottetown City Council": {"has311": False, "website": "charlottetown.ca"},
    "Yellowknife City Council": {"has311": False, "website": "yellowknife.ca"},
    "Whitehorse City Council": {"has311": False, "website": "whitehorse.ca"},
    "Iqaluit City Council": {"has311": False, "website": "iqaluit.ca"},
}

# City-based lookup for smaller municipalities (when OpenNorth doesn't return representative_set_name)
# Keyed by the 'city' field from OpenNorth API
city_website_lookup = {
    # Ontario - Greater Toronto Area
    "RICHMOND HILL": {"website": "richmondhill.ca"},
    "MARKHAM": {"website": "markham.ca"},
    "VAUGHAN": {"website": "vaughan.ca"},
    "NEWMARKET": {"website": "newmarket.ca"},
    "AJAX": {"website": "ajax.ca"},
    "PICKERING": {"website": "pickering.ca"},
    "WHITBY": {"website": "whitby.ca"},
    "OSHAWA": {"website": "oshawa.ca"},
    "SCARBOROUGH": {"website": "toronto.ca"},  # Part of Toronto
    "ETOBICOKE": {"website": "toronto.ca"},  # Part of Toronto
    "NORTH YORK": {"website": "toronto.ca"},  # Part of Toronto
    
    # Ontario - Other Major Cities
    "KITCHENER": {"website": "kitchener.ca"},
    "WATERLOO": {"website": "waterloo.ca"},
    "CAMBRIDGE": {"website": "cambridge.ca"},
    "GUELPH": {"website": "guelph.ca"},
    "BURLINGTON": {"website": "burlington.ca"},
    "OAKVILLE": {"website": "oakville.ca"},
    "MILTON": {"website": "milton.ca"},
    "BARRIE": {"website": "barrie.ca"},
    "PETERBOROUGH": {"website": "peterborough.ca"},
    "KINGSTON": {"website": "cityofkingston.ca"},
    "THUNDER BAY": {"website": "thunderbay.ca"},
    "SAULT STE. MARIE": {"website": "saultstemarie.ca"},
    "NORTH BAY": {"website": "northbay.ca"},
    "TIMMINS": {"website": "timmins.ca"},
    "CORNWALL": {"website": "cornwall.ca"},
    "BELLEVILLE": {"website": "belleville.ca"},
    "QUINTE WEST": {"website": "quintewest.ca"},
    "COBOURG": {"website": "cobourg.ca"},
    "PORT HOPE": {"website": "porthope.ca"},
    "BRIGHTON": {"website": "brighton.ca"},
    
    # Ontario - Townships and Smaller Municipalities
    "SELWYN": {"website": "selwyntownship.ca"},
    "SMITH-ENNISMORE-LAKEFIELD": {"website": "selwyntownship.ca"},  # Former name
    "LAKEFIELD": {"website": "selwyntownship.ca"},  # Part of Selwyn
    "ENNISMORE": {"website": "selwyntownship.ca"},  # Part of Selwyn
    "PETERBOROUGH COUNTY": {"website": "ptbocounty.ca"},
    "HALLIBURTON": {"website": "haliburtoncounty.ca"},
    "MINDEN HILLS": {"website": "mindenhills.ca"},
    "DYSART ET AL": {"website": "dysartetal.ca"},
    "MUSKOKA": {"website": "muskoka.on.ca"},
    "BRACEBRIDGE": {"website": "bracebridge.ca"},
    "HUNTSVILLE": {"website": "huntsville.ca"},
    "GRAVENHURST": {"website": "gravenhurst.ca"},
    "GEORGIAN BAY": {"website": "georgianbay.ca"},
    "SIMCOE COUNTY": {"website": "simcoe.ca"},
    "BARRIE": {"website": "barrie.ca"},
    "ORILLIA": {"website": "orillia.ca"},
    "BRADFORD WEST GWILLIMBURY": {"website": "townofbwg.com"},
    "INNISFIL": {"website": "innisfil.ca"},
    "BRAMPTON": {"website": "brampton.ca"},
    "MISSISSAUGA": {"website": "mississauga.ca"},
    "CALEDON": {"website": "caledon.ca"},
    "PEEL REGION": {"website": "peelregion.ca"},
    "DURHAM REGION": {"website": "durham.ca"},
    "YORK REGION": {"website": "york.ca"},
    "HALTON REGION": {"website": "halton.ca"},
    
    # Ontario - Eastern Ontario
    "PRESCOTT": {"website": "prescott.ca"},
    "BROCKVILLE": {"website": "brockville.ca"},
    "SMITHS FALLS": {"website": "smithsfalls.ca"},
    "PERTH": {"website": "perth.ca"},
    "CARLETON PLACE": {"website": "carletonplace.ca"},
    "ALMONTE": {"website": "mississippimills.ca"},
    "LANARK COUNTY": {"website": "lanarkcounty.ca"},
    "LEEDS AND GRENVILLE": {"website": "uclg.on.ca"},
    "STORMONT, DUNDAS AND GLENGARRY": {"website": "sdgcounties.ca"},
    "CORNWALL": {"website": "cornwall.ca"},
    "ALEXANDRIA": {"website": "glengarry.ca"},
    
    # Ontario - Northern Ontario
    "SUDBURY": {"website": "greatersudbury.ca"},
    "SUDBURY DISTRICT": {"website": "sudburydistrict.ca"},
    "COCHRANE DISTRICT": {"website": "cochranedistrict.ca"},
    "TIMMINS": {"website": "timmins.ca"},
    "COCHRANE": {"website": "cochraneontario.ca"},
    "MOOSONEE": {"website": "moosonee.ca"},
    "NIPAWIN": {"website": "nipawin.com"},
    "NORTH BAY": {"website": "northbay.ca"},
    "NIPISSING": {"website": "nipissing.ca"},
    "SAULT STE. MARIE": {"website": "saultstemarie.ca"},
    "ALGOMA DISTRICT": {"website": "algomadistrict.ca"},
    "WAWA": {"website": "wawa.cc"},
    "THUNDER BAY": {"website": "thunderbay.ca"},
    "THUNDER BAY DISTRICT": {"website": "thunderbay.ca"},
    "KENORA": {"website": "kenora.ca"},
    "DRYDEN": {"website": "dryden.ca"},
    "FORT FRANCES": {"website": "fortfrances.ca"},
    
    # Ontario - Southwestern Ontario
    "WINDSOR": {"website": "citywindsor.ca"},
    "ESSEX COUNTY": {"website": "countyofessex.ca"},
    "LEAMINGTON": {"website": "leamington.ca"},
    "KINGSVILLE": {"website": "kingsville.ca"},
    "AMHERSTBURG": {"website": "amherstburg.ca"},
    "LAKESHORE": {"website": "lakeshore.ca"},
    "LASALLE": {"website": "lasalle.ca"},
    "TECUMSEH": {"website": "tecumseh.ca"},
    "CHATHAM-KENT": {"website": "chatham-kent.ca"},
    "SARNIA": {"website": "sarnia.ca"},
    "LAMBTON COUNTY": {"website": "lambtononline.ca"},
    "LONDON": {"website": "london.ca"},
    "MIDDLESEX COUNTY": {"website": "middlesex.ca"},
    "ST. THOMAS": {"website": "stthomas.ca"},
    "WOODSTOCK": {"website": "woodstock.ca"},
    "OXFORD COUNTY": {"website": "oxfordcounty.ca"},
    "INGERSOLL": {"website": "ingersoll.ca"},
    "TILLSONBURG": {"website": "tillsonburg.ca"},
    "STRATFORD": {"website": "stratford.ca"},
    "PERTH COUNTY": {"website": "perthcounty.ca"},
    "KITCHENER": {"website": "kitchener.ca"},
    "WATERLOO": {"website": "waterloo.ca"},
    "CAMBRIDGE": {"website": "cambridge.ca"},
    "REGION OF WATERLOO": {"website": "regionofwaterloo.ca"},
    "GUELPH": {"website": "guelph.ca"},
    "WELLINGTON COUNTY": {"website": "wellington.ca"},
    "HAMILTON": {"website": "hamilton.ca"},
    "HALDIMAND COUNTY": {"website": "haldimandcounty.ca"},
    "NIAGARA FALLS": {"website": "niagarafalls.ca"},
    "ST. CATHARINES": {"website": "stcatharines.ca"},
    "WELLAND": {"website": "welland.ca"},
    "NIAGARA REGION": {"website": "niagararegion.ca"},
    "FORT ERIE": {"website": "forterie.ca"},
    "NIAGARA-ON-THE-LAKE": {"website": "notl.org"},
    "GRIMSBY": {"website": "grimsby.ca"},
    "LINCOLN": {"website": "lincoln.ca"},
    "PELHAM": {"website": "pelham.ca"},
    "THOROLD": {"website": "thorold.ca"},
    "WAINFLEET": {"website": "wainfleet.ca"},
    "WEST LINCOLN": {"website": "westlincoln.ca"},
    
    # Ontario - Central Ontario
    "BRANTFORD": {"website": "brantford.ca"},
    "BRANT COUNTY": {"website": "brant.ca"},
    "PARIS": {"website": "countyofbrant.ca"},
    "NORFOLK COUNTY": {"website": "norfolkcounty.ca"},
    "SIMCOE": {"website": "norfolkcounty.ca"},  # Town of Simcoe is in Norfolk
    "HALDIMAND COUNTY": {"website": "haldimandcounty.ca"},
    "CAYUGA": {"website": "haldimandcounty.ca"},
    "HAGERSVILLE": {"website": "haldimandcounty.ca"},
    "DUNNVILLE": {"website": "haldimandcounty.ca"},
    "JARVIS": {"website": "haldimandcounty.ca"},
    
    # Ontario - Golden Horseshoe Extended
    "OAKVILLE": {"website": "oakville.ca"},
    "MILTON": {"website": "milton.ca"},
    "BURLINGTON": {"website": "burlington.ca"},
    "HALTON HILLS": {"website": "haltonhills.ca"},
    "GEORGETOWN": {"website": "haltonhills.ca"},
    "ACTON": {"website": "haltonhills.ca"},
    
    # British Columbia
    "VANCOUVER": {"website": "vancouver.ca"},
    "SURREY": {"website": "surrey.ca"},
    "BURNABY": {"website": "burnaby.ca"},
    "RICHMOND": {"website": "richmond.ca"},
    "COQUITLAM": {"website": "coquitlam.ca"},
    "SURREY": {"website": "surrey.ca"},
    "DELTA": {"website": "delta.ca"},
    "LANGLEY": {"website": "langley.ca"},
    "LANGLEY TOWNSHIP": {"website": "tol.ca"},
    "ABBOTSFORD": {"website": "abbotsford.ca"},
    "MISSION": {"website": "mission.ca"},
    "MAPLE RIDGE": {"website": "mapleridge.ca"},
    "PITT MEADOWS": {"website": "pittmeadows.ca"},
    "NEW WESTMINSTER": {"website": "newwestminster.ca"},
    "PORT COQUITLAM": {"website": "portcoquitlam.ca"},
    "PORT MOODY": {"website": "portmoody.ca"},
    "NORTH VANCOUVER CITY": {"website": "cnv.org"},
    "NORTH VANCOUVER DISTRICT": {"website": "dnv.org"},
    "WEST VANCOUVER": {"website": "westvancouver.ca"},
    "VICTORIA": {"website": "victoria.ca"},
    "SAANICH": {"website": "saanich.ca"},
    "ESQUIMALT": {"website": "esquimalt.ca"},
    "OAK BAY": {"website": "oakbay.ca"},
    "VIEW ROYAL": {"website": "viewroyal.ca"},
    "LANGFORD": {"website": "langford.ca"},
    "COLWOOD": {"website": "colwood.ca"},
    "SIDNEY": {"website": "sidney.ca"},
    "KELOWNA": {"website": "kelowna.ca"},
    "VERNON": {"website": "vernon.ca"},
    "PENTICTON": {"website": "penticton.ca"},
    "KAMLOOPS": {"website": "kamloops.ca"},
    "CHILLIWACK": {"website": "chilliwack.com"},
    "NANAIMO": {"website": "nanaimo.ca"},
    "PRINCE GEORGE": {"website": "princegeorge.ca"},
    "TERRACE": {"website": "terrace.ca"},
    "PRINCE RUPERT": {"website": "princerupert.ca"},
    "CAMPBELL RIVER": {"website": "campbellriver.ca"},
    "COURTENAY": {"website": "courtenay.ca"},
    "COMOX": {"website": "comox.ca"},
    "CRANBROOK": {"website": "cranbrook.ca"},
    "DUNCAN": {"website": "duncan.ca"},
    "NANOOSE BAY": {"website": "rdn.bc.ca"},
    "PARKSVILLE": {"website": "parksville.ca"},
    "QUALICUM BEACH": {"website": "qualicumbeach.ca"},
    "SUNSHINE COAST": {"website": "scrd.ca"},
    "SECHelt": {"website": "sechelt.ca"},
    "GIBSONS": {"website": "gibsons.ca"},
    
    # Alberta
    "CALGARY": {"website": "calgary.ca"},
    "EDMONTON": {"website": "edmonton.ca"},
    "RED DEER": {"website": "reddeer.ca"},
    "LETHBRIDGE": {"website": "lethbridge.ca"},
    "MEDICINE HAT": {"website": "medicinehat.ca"},
    "GRANDE PRAIRIE": {"website": "cityofgp.com"},
    "FORT MCMURRAY": {"website": "rmwb.ca"},
    "WOOD BUFFALO": {"website": "rmwb.ca"},
    "ST. ALBERT": {"website": "stalbert.ca"},
    "SPRUCE GROVE": {"website": "sprucegrove.org"},
    "LEDCUC": {"website": "leduc.ca"},
    "FORT SASKATCHEWAN": {"website": "fortsask.ca"},
    "GRANDE CACHE": {"website": "grandecache.ca"},
    "HINTON": {"website": "hinton.ca"},
    "JASPER": {"website": "jasper-alberta.ca"},
    "CANMORE": {"website": "canmore.ca"},
    "BANFF": {"website": "banff.ca"},
    "AIRDRIE": {"website": "airdrie.ca"},
    "CHESTERMERE": {"website": "chestermere.ca"},
    "OKOTOKS": {"website": "okotoks.ca"},
    "HIGH RIVER": {"website": "highriver.ca"},
    "STRATHMORE": {"website": "strathmore.ca"},
    "DRUMHELLER": {"website": "drumheller.ca"},
    "BROOKS": {"website": "brooks.ca"},
    "COLD LAKE": {"website": "coldlake.ca"},
    "LLOYDMINSTER": {"website": "lloydminster.ca"},
    "PEACE RIVER": {"website": "peaceriver.ca"},
    "SLAVE LAKE": {"website": "slavelake.ca"},
    
    # Saskatchewan
    "SASKATOON": {"website": "saskatoon.ca"},
    "REGINA": {"website": "regina.ca"},
    "PRINCE ALBERT": {"website": "citypa.ca"},
    "MOOSE JAW": {"website": "moosejaw.ca"},
    "YORKTON": {"website": "yorkton.ca"},
    "SWIFT CURRENT": {"website": "swiftcurrent.ca"},
    "NORTH BATTLEFORD": {"website": "cityofnb.ca"},
    "ESTEVAN": {"website": "estevan.ca"},
    "WEYBURN": {"website": "weyburn.ca"},
    "MELFORT": {"website": "melfort.ca"},
    "HUMBOLDT": {"website": "humboldt.ca"},
    "LLOYDMINSTER": {"website": "lloydminster.ca"},
    "KINDERSLEY": {"website": "kindersley.ca"},
    "MEADOW LAKE": {"website": "meadowlake.ca"},
    "NIPAWIN": {"website": "nipawin.com"},
    "WATROUS": {"website": "watrous.ca"},
    
    # Manitoba
    "WINNIPEG": {"website": "winnipeg.ca"},
    "BRANDON": {"website": "brandon.ca"},
    "THOMPSON": {"website": "thompson.ca"},
    "PORTAGE LA PRAIRIE": {"website": "cityofportage.ca"},
    "SELKIRK": {"website": "cityofselkirk.ca"},
    "STEINBACH": {"website": "steinbach.ca"},
    "WINKLER": {"website": "winkler.ca"},
    "MORDEN": {"website": "morden.ca"},
    "DAUPHIN": {"website": "dauphin.ca"},
    "Flin Flon": {"website": "flinflon.ca"},
    "THE PAS": {"website": "thepas.ca"},
    "SWAN RIVER": {"website": "swanriver.ca"},
    
    # Quebec
    "MONTREAL": {"website": "montreal.ca"},
    "LAVAL": {"website": "laval.ca"},
    "QUEBEC CITY": {"website": "quebec.ca"},
    "GATINEAU": {"website": "gatineau.ca"},
    "LONGUEUIL": {"website": "longueuil.quebec"},
    "SHERBROOKE": {"website": "sherbrooke.ca"},
    "SAGUENAY": {"website": "ville.saguenay.ca"},
    "TROIS-RIVIERES": {"website": "troisrivieres.ca"},
    "TROIS-RIVI\u00c8RES": {"website": "troisrivieres.ca"},
    "LEVIS": {"website": "ville.levis.qc.ca"},
    "L\u00c9VIS": {"website": "ville.levis.qc.ca"},
    "TERREBONNE": {"website": "ville.terrebonne.qc.ca"},
    "TERREBONNE": {"website": "ville.terrebonne.qc.ca"},
    "SAINT-JEAN-SUR-RICHELIEU": {"website": "ville.saint-jean-sur-richelieu.qc.ca"},
    "BLAINVILLE": {"website": "ville.blainville.qc.ca"},
    "CHATEAUGUAY": {"website": "ville.chateauguay.qc.ca"},
    "CH\u00c2TEAUGUAY": {"website": "ville.chateauguay.qc.ca"},
    "SAINT-LAURENT": {"website": "ville.saint-laurent.qc.ca"},
    "SAINT-JEROME": {"website": "saint-jerome.ca"},
    "SAINT-J\u00c9ROME": {"website": "saint-jerome.ca"},
    "DRUMMONDVILLE": {"website": "ville.drummondville.qc.ca"},
    "GRANBY": {"website": "ville.granby.qc.ca"},
    "SAINT-HYACINTHE": {"website": "ville.saint-hyacinthe.qc.ca"},
    "MASCOUTENCHE": {"website": "ville.mascouche.qc.ca"},
    "MIRABEL": {"website": "ville.mirabel.qc.ca"},
    "VARENNES": {"website": "ville.varennes.qc.ca"},
    "REPENTIGNY": {"website": "ville.repentigny.qc.ca"},
    "BROSSARD": {"website": "brossard.ca"},
    "BOUCHERVILLE": {"website": "ville.boucherville.qc.ca"},
    "MONTREAL-NORD": {"website": "montreal.ca"},
    "MONTREAL NORTH": {"website": "montreal.ca"},
    "POINTE-CLAIRE": {"website": "pointe-claire.ca"},
    "DOLLARD-DES-ORMEAUX": {"website": "ville.ddo.qc.ca"},
    "KIRKLAND": {"website": "kirkland.ca"},
    "BEACONSFIELD": {"website": "beaconsfield.ca"},
    "BAIE-D'URFE": {"website": "baie-d-urfe.qc.ca"},
    "SAINTE-ANNE-DE-BELLEVUE": {"website": "sainte-anne-de-bellevue.ca"},
    "SENNEVILLE": {"website": "ville.senneville.qc.ca"},
    
    # New Brunswick
    "MONCTON": {"website": "moncton.ca"},
    "SAINT JOHN": {"website": "saintjohn.ca"},
    "FREDERICTON": {"website": "fredericton.ca"},
    "BATHURST": {"website": "bathurst.ca"},
    "EDMUNDSTON": {"website": "edmundston.ca"},
    "CAMPBELLTON": {"website": "campbellton.ca"},
    "DIEPPE": {"website": "dieppe.ca"},
    "MIRAMICHI": {"website": "miramichi.org"},
    "RIVIERE-DU-LOUP": {"website": "riviereduloup.ca"},
    "RIMOUSKI": {"website": "ville.rimouski.qc.ca"},
    "GRAND FALLS": {"website": "grandfalls.com"},
    "QUISPAMSIS": {"website": "quispamsis.ca"},
    "ROTHESEAY": {"website": "rothesay.ca"},
    "OSHAWA": {"website": "oshawa.ca"},
    
    # Nova Scotia
    "HALIFAX": {"website": "halifax.ca"},
    "SYDNEY": {"website": "cba-ns.ca"},
    "CAPE BRETON": {"website": "cba-ns.ca"},
    "TRURO": {"website": "truro.ca"},
    "NEW GLASGOW": {"website": "newglasgow.ca"},
    "GLACE BAY": {"website": "cba-ns.ca"},
    "LUNENBURG": {"website": "townoflunenburg.ca"},
    "MAHONE BAY": {"website": "mahonebay.ca"},
    "BRIDGEWATER": {"website": "bridgewater.ca"},
    "WOLFVILLE": {"website": "wolfville.ca"},
    "KENTVILLE": {"website": "kentville.ca"},
    "ANTIGONISH": {"website": "townofantigonish.ca"},
    "PORT HAWKESBURY": {"website": "porthawkesbury.ca"},
    "YARMOUTH": {"website": "townofyarmouth.ca"},
    "DIGBY": {"website": "digby.ca"},
    "SHELBURNE": {"website": "townofshelburne.ca"},
    
    # Prince Edward Island
    "CHARLOTTETOWN": {"website": "charlottetown.ca"},
    "SUMMERSIDE": {"website": "city.summerside.pe.ca"},
    "STRATFORD": {"website": "stratfordpei.ca"},
    "KENSINGTON": {"website": "kensington.pe.ca"},
    "SOURIS": {"website": "townofsouris.ca"},
    "GEORGETOWN": {"website": "georgetownpei.ca"},
    "ALBERTON": {"website": "alberton.ca"},
    
    # Newfoundland and Labrador
    "ST. JOHN'S": {"website": "stjohns.ca"},
    "MOUNT PEARL": {"website": "mountpearl.ca"},
    "CONCEPTION BAY SOUTH": {"website": "conceptionbaysouth.ca"},
    "PARADISE": {"website": "townofparadise.ca"},
    "CORNER BROOK": {"website": "cornerbrook.com"},
    "GRAND FALLS-WINDSOR": {"website": "gfw.ca"},
    "GANDER": {"website": "townofgander.ca"},
    "CLARENVILLE": {"website": "clarenville.ca"},
    "STEPHENVILLE": {"website": "stephenville.ca"},
    "LABRADOR CITY": {"website": "labradorcity.ca"},
    "HAPPY VALLEY-GOOSE BAY": {"website": "happyvalleygoosebay.com"},
    
    # Yukon
    "WHITEHORSE": {"website": "whitehorse.ca"},
    "DAWSON CITY": {"website": "dawsoncity.ca"},
    "WATSON LAKE": {"website": "watsonlake.ca"},
    "HAINES JUNCTION": {"website": "hainesjunctionyukon.com"},
    
    # Northwest Territories
    "YELLOWKNIFE": {"website": "yellowknife.ca"},
    "HAY RIVER": {"website": "hayriver.com"},
    "FORT SMITH": {"website": "fortsmith.ca"},
    "INUVIK": {"website": "inuvik.ca"},
    "BEHCHOKO": {"website": "behchoko.com"},
    
    # Nunavut
    "IQALUIT": {"website": "iqaluit.ca"},
    "RANKIN INLET": {"website": "rankininlet.ca"},
    "CAMBRIDGE BAY": {"website": "cambridgebay.ca"},
    "ARVIAT": {"website": "arviat.ca"},
    "BAKER LAKE": {"website": "bakerlake.ca"},
}

# Generate the JavaScript file
output = """// MUNICIPAL 311 LOOKUP DATA - COMPREHENSIVE
// Maps representative_set_name from OpenNorth API to 311 phone info and website
// Used to show users where to report issues BEFORE contacting representatives

const MUNICIPAL_311_LOOKUP = {
  // Cities with 311 service
"""

for city, data in cities_with_311.items():
    output += f'  "{city}": {{ has311: true, phone: "311", website: "{data["website"]}" }},\n'

output += """
  // Cities without 311 (need to call main number or visit website)
"""

for city, data in cities_without_311.items():
    output += f'  "{city}": {{ has311: false, website: "{data["website"]}" }},\n'

output += """};

// CITY-BASED WEBSITE LOOKUP
// Used when OpenNorth doesn't return representative_set_name (smaller municipalities)
// Keyed by the 'city' field from OpenNorth API (uppercase for case-insensitive matching)

const CITY_WEBSITE_LOOKUP = {
"""

for city, data in city_website_lookup.items():
    # Escape any special characters in city name
    escaped_city = city.replace("'", "\\'")
    output += f'  "{escaped_city}": {{ website: "{data["website"]}" }},\n'

output += """};

// Fallback message for cities without 311
const FALLBACK_MESSAGE = {
  en: "Contact your municipal office directly for local services. Search '[your city] report a problem' online.",
  fr: "Contactez directement votre bureau municipal pour les services locaux. Recherchez '[votre ville] signaler un probl\\u00e8me' en ligne."
};

// CATEGORY TO ESCALATION TYPE MAPPING
// Maps issue categories to the appropriate escalation type
const CATEGORY_ESCALATION_MAP = {
  // Infrastructure issues → municipal 311
  infrastructure: {
    type: "municipal_311",
    priority: "high",
    keywords: ["potholes", "streetlights", "signs", "snow", "sidewalks", "traffic"]
  },
  // Environment issues → often municipal
  environment: {
    type: "municipal_311",
    priority: "medium",
    keywords: ["garbage", "recycling", "trees", "water quality"]
  },
  // Safety issues → mix (bylaw is municipal)
  safety: {
    type: "municipal_311",
    priority: "medium",
    keywords: ["bylaw", "noise", "parking"]
  },
  // Housing → some municipal aspects
  housing: {
    type: "municipal_311",
    priority: "medium",
    keywords: ["zoning", "permits", "bylaw"]
  },
  // Default: no escalation
  default: {
    type: "representative_direct",
    priority: "low"
  }
};

// Helper function to get 311 info for a municipality
function get311Info(representativeSetName, isFrench = false) {
  const data = MUNICIPAL_311_LOOKUP[representativeSetName];
  if (!data) {
    return null;
  }
  
  if (data.has311) {
    return {
      has311: true,
      phone: "311",
      website: data.website,
      message: isFrench 
        ? "Pour les questions municipales, appelez le 311."
        : "For municipal issues, call 311."
    };
  } else {
    return {
      has311: false,
      website: data.website,
      message: isFrench ? FALLBACK_MESSAGE.fr : FALLBACK_MESSAGE.en
    };
  }
}

// Helper function to get website by city name
function getWebsiteByCity(cityName) {
  if (!cityName) return null;
  const upperCity = cityName.toUpperCase();
  return CITY_WEBSITE_LOOKUP[upperCity]?.website || null;
}
"""

# Write to file
with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\escalation_data.js', 'w', encoding='utf-8') as f:
    f.write(output)

print("Generated escalation_data.js with:")
print(f"  - {len(cities_with_311)} cities with 311 service")
print(f"  - {len(cities_without_311)} cities without 311")
print(f"  - {len(city_website_lookup)} city-based website lookups")
print(f"  - Total: {len(cities_with_311) + len(cities_without_311) + len(city_website_lookup)} entries")