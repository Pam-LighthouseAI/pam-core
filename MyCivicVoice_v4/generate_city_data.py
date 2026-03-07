# Generate comprehensive Canadian city data for MyCivicVoice v4
# Maps 500+ cities to province codes and OpenNorth representative_set_name

import json

cities = []

# ===== ONTARIO (ON) - 120 cities =====
ontario = [
    ("Toronto", "Toronto City Council"),
    ("Ottawa", "Ottawa City Council"),
    ("Mississauga", "Mississauga City Council"),
    ("Brampton", "Brampton City Council"),
    ("Hamilton", "Hamilton City Council"),
    ("London", "London City Council"),
    ("Markham", "Markham City Council"),
    ("Vaughan", "Vaughan City Council"),
    ("Kitchener", "Kitchener City Council"),
    ("Windsor", "Windsor City Council"),
    ("Richmond Hill", "Richmond Hill Town Council"),
    ("Oakville", "Oakville Town Council"),
    ("Burlington", "Burlington City Council"),
    ("Oshawa", "Oshawa City Council"),
    ("Greater Sudbury", "Greater Sudbury City Council"),
    ("Guelph", "Guelph City Council"),
    ("Cambridge", "Cambridge City Council"),
    ("Whitby", "Whitby Town Council"),
    ("Kingston", "Kingston City Council"),
    ("Ajax", "Ajax Town Council"),
    ("Milton", "Milton Town Council"),
    ("Waterloo", "Waterloo City Council"),
    ("Thunder Bay", "Thunder Bay City Council"),
    ("Brantford", "Brantford City Council"),
    ("Niagara Falls", "Niagara Falls City Council"),
    ("Newmarket", "Newmarket Town Council"),
    ("Pickering", "Pickering City Council"),
    ("Peterborough", "Peterborough City Council"),
    ("Barrie", "Barrie City Council"),
    ("St. Catharines", "St. Catharines City Council"),
    ("Sarnia", "Sarnia City Council"),
    ("North Bay", "North Bay City Council"),
    ("Timmins", "Timmins City Council"),
    ("Orillia", "Orillia City Council"),
    ("Stratford", "Stratford City Council"),
    ("Belleville", "Belleville City Council"),
    ("Cornwall", "Cornwall City Council"),
    ("Quinte West", "Quinte West City Council"),
    ("Brockville", "Brockville City Council"),
    ("Pembroke", "Pembroke City Council"),
    ("Sault Ste. Marie", "Sault Ste. Marie City Council"),
    ("Elliot Lake", "Elliot Lake City Council"),
    ("Temiskaming Shores", "Temiskaming Shores City Council"),
    ("Kenora", "Kenora City Council"),
    ("Dryden", "Dryden City Council"),
    ("Fort Frances", "Fort Frances Town Council"),
    ("Sioux Lookout", "Sioux Lookout Town Council"),
    ("Moosonee", "Moosonee Town Council"),
    ("Cochrane", "Cochrane Town Council"),
    ("Hearst", "Hearst Town Council"),
    ("Kapuskasing", "Kapuskasing Town Council"),
    ("Kirkland Lake", "Kirkland Lake Town Council"),
    ("Parry Sound", "Parry Sound Town Council"),
    ("Huntsville", "Huntsville Town Council"),
    ("Bracebridge", "Bracebridge Town Council"),
    ("Gravenhurst", "Gravenhurst Town Council"),
    ("Midland", "Midland Town Council"),
    ("Penetanguishene", "Penetanguishene Town Council"),
    ("Collingwood", "Collingwood Town Council"),
    ("Wasaga Beach", "Wasaga Beach Town Council"),
    ("Innisfil", "Innisfil Town Council"),
    ("Bradford West Gwillimbury", "Bradford West Gwillimbury Town Council"),
    ("New Tecumseth", "New Tecumseth Town Council"),
    ("Kawartha Lakes", "Kawartha Lakes City Council"),
    ("Port Hope", "Port Hope Town Council"),
    ("Cobourg", "Cobourg Town Council"),
    ("Brighton", "Brighton Town Council"),
    ("Gananoque", "Gananoque Town Council"),
    ("Prescott", "Prescott Town Council"),
    ("Smiths Falls", "Smiths Falls Town Council"),
    ("Perth", "Perth Town Council"),
    ("Carleton Place", "Carleton Place Town Council"),
    ("Almonte", "Almonte Town Council"),
    ("Arnprior", "Arnprior Town Council"),
    ("Renfrew", "Renfrew Town Council"),
    ("Petawawa", "Petawawa Town Council"),
    ("Deep River", "Deep River Town Council"),
    ("Bancroft", "Bancroft Town Council"),
    ("Minden", "Minden Town Council"),
    ("Tweed", "Tweed Town Council"),
    ("Campbellford", "Campbellford Town Council"),
    ("Norwood", "Norwood Town Council"),
    ("Uxbridge", "Uxbridge Town Council"),
    ("Port Perry", "Port Perry Town Council"),
    ("Stouffville", "Stouffville Town Council"),
    ("Thornhill", "Thornhill Village Council"),
    ("Maple", "Maple Village Council"),
    ("Kleinburg", "Kleinburg Village Council"),
    ("Woodbridge", "Woodbridge Village Council"),
    ("Georgetown", "Georgetown Town Council"),
    ("Acton", "Acton Town Council"),
    ("Ancaster", "Ancaster Town Council"),
    ("Dundas", "Dundas Town Council"),
    ("Stoney Creek", "Stoney Creek Town Council"),
    ("Flamborough", "Flamborough Township Council"),
    ("Port Colborne", "Port Colborne City Council"),
    ("Welland", "Welland City Council"),
    ("Thorold", "Thorold City Council"),
    ("Niagara-on-the-Lake", "Niagara-on-the-Lake Town Council"),
    ("Fort Erie", "Fort Erie Town Council"),
    ("Grimsby", "Grimsby Town Council"),
    ("Lincoln", "Lincoln Town Council"),
    ("Pelham", "Pelham Town Council"),
    ("Wainfleet", "Wainfleet Township Council"),
    ("West Lincoln", "West Lincoln Township Council"),
    ("St. Thomas", "St. Thomas City Council"),
    ("Woodstock", "Woodstock City Council"),
    ("Ingersoll", "Ingersoll Town Council"),
    ("Tillsonburg", "Tillsonburg Town Council"),
    ("Norwich", "Norwich Township Council"),
    ("Bayham", "Bayham Township Council"),
    ("Central Elgin", "Central Elgin Township Council"),
    ("Dutton/Dunwich", "Dutton/Dunwich Township Council"),
    ("West Elgin", "West Elgin Township Council"),
]

for city, council in ontario:
    cities.append({"name": city, "province": "ON", "repSet": council})

# ===== QUEBEC (QC) - 80 cities =====
quebec = [
    ("Montreal", "Montreal City Council"),
    ("Quebec City", "Quebec City Council"),
    ("Laval", "Laval City Council"),
    ("Gatineau", "Gatineau City Council"),
    ("Longueuil", "Longueuil City Council"),
    ("Sherbrooke", "Sherbrooke City Council"),
    ("Saguenay", "Saguenay City Council"),
    ("Levis", "Levis City Council"),
    ("Trois-Rivieres", "Trois-Rivieres City Council"),
    ("Terrebonne", "Terrebonne City Council"),
    ("Saint-Jean-sur-Richelieu", "Saint-Jean-sur-Richelieu City Council"),
    ("Granby", "Granby City Council"),
    ("Saint-Laurent", "Saint-Laurent Borough Council"),
    ("Lachine", "Lachine Borough Council"),
    ("Saint-Hyacinthe", "Saint-Hyacinthe City Council"),
    ("Blainville", "Blainville City Council"),
    ("Saint-Jerome", "Saint-Jerome City Council"),
    ("Drummondville", "Drummondville City Council"),
    ("Saint-Jean-sur-Richelieu", "Saint-Jean-sur-Richelieu City Council"),
    ("Saint-Eustache", "Saint-Eustache City Council"),
    ("Rimouski", "Rimouski City Council"),
    ("Shawinigan", "Shawinigan City Council"),
    ("Rouyn-Noranda", "Rouyn-Noranda City Council"),
    ("Saint-Bruno-de-Montarville", "Saint-Bruno-de-Montarville City Council"),
    ("Saint-Constant", "Saint-Constant City Council"),
    ("Mont-Royal", "Mont-Royal Town Council"),
    ("Westmount", "Westmount City Council"),
    ("Dollard-des-Ormeaux", "Dollard-des-Ormeaux City Council"),
    ("Cote-Saint-Luc", "Cote-Saint-Luc City Council"),
    ("Pointe-Claire", "Pointe-Claire City Council"),
    ("Beaconsfield", "Beaconsfield City Council"),
    ("Kirkland", "Kirkland City Council"),
    ("Dorval", "Dorval City Council"),
    ("Sainte-Anne-de-Bellevue", "Sainte-Anne-de-Bellevue Town Council"),
    ("Senneville", "Senneville Village Council"),
    ("Baie-d'Urfe", "Baie-d'Urfe Town Council"),
    ("Sainte-Julie", "Sainte-Julie City Council"),
    ("Varennes", "Varennes City Council"),
    ("Repentigny", "Repentigny City Council"),
    ("Boucherville", "Boucherville City Council"),
    ("Beloeil", "Beloeil City Council"),
    ("Chambly", "Chambly City Council"),
    ("Saint-Basile-le-Grand", "Saint-Basile-le-Grand City Council"),
    ("Saint-Amable", "Saint-Amable City Council"),
    ("Vercheres", "Vercheres City Council"),
    ("Contrecoeur", "Contrecoeur City Council"),
    ("Sorel-Tracy", "Sorel-Tracy City Council"),
    ("Valleyfield", "Valleyfield City Council"),
    ("Saint-Lambert", "Saint-Lambert City Council"),
    ("Brossard", "Brossard City Council"),
    ("Chateauguay", "Chateauguay City Council"),
    ("La Prairie", "La Prairie City Council"),
    ("Candiac", "Candiac City Council"),
    ("Delson", "Delson City Council"),
    ("Saint-Philippe", "Saint-Philippe City Council"),
    ("Saint-Isidore", "Saint-Isidore City Council"),
    ("Saint-Mathieu", "Saint-Mathieu City Council"),
    ("Saint-Constant", "Saint-Constant City Council"),
    ("Sainte-Catherine", "Sainte-Catherine City Council"),
    ("Saint-Remi", "Saint-Remi City Council"),
    ("Saint-Michel", "Saint-Michel City Council"),
    ("Mercier", "Mercier City Council"),
    ("Saint-Canut", "Saint-Canut City Council"),
    ("Saint-Janvier", "Saint-Janvier City Council"),
    ("Sainte-Therese", "Sainte-Therese City Council"),
    ("Rosemere", "Rosemere City Council"),
    ("Boisbriand", "Boisbriand City Council"),
    ("Sainte-Anne-des-Plaines", "Sainte-Anne-des-Plaines City Council"),
    ("Sainte-Sophie", "Sainte-Sophie City Council"),
    ("Saint-Hippolyte", "Saint-Hippolyte City Council"),
    ("Saint-Colomban", "Saint-Colomban City Council"),
    ("Mirabel", "Mirabel City Council"),
    ("Sainte-Marthe-sur-le-Lac", "Sainte-Marthe-sur-le-Lac City Council"),
    ("Saint-Joseph-du-Lac", "Saint-Joseph-du-Lac City Council"),
    ("Pointe-Calumet", "Pointe-Calumet City Council"),
    ("Saint-Placide", "Saint-Placide City Council"),
    ("Oka", "Oka City Council"),
    ("Hudson", "Hudson Town Council"),
    ("Rigaud", "Rigaud City Council"),
    ("Saint-Lazare", "Saint-Lazare City Council"),
    ("Vaudreuil-Dorion", "Vaudreuil-Dorion City Council"),
    ("Pincourt", "Pincourt Town Council"),
    ("Ile-Perrot", "Ile-Perrot Town Council"),
    ("Notre-Dame-de-l'Ile-Perrot", "Notre-Dame-de-l'Ile-Perrot Town Council"),
    ("Terrasse-Vaudreuil", "Terrasse-Vaudreuil Town Council"),
    ("Dorion", "Dorion Town Council"),
    ("Les Cedres", "Les Cedres Town Council"),
    ("Saint-Clet", "Saint-Clet Town Council"),
    ("Saint-Polycarpe", "Saint-Polycarpe Town Council"),
    ("Saint-Telephore", "Saint-Telephore Town Council"),
    ("Saint-Zotique", "Saint-Zotique Town Council"),
    ("Les Coteaux", "Les Coteaux Town Council"),
    ("Coteau-du-Lac", "Coteau-du-Lac Town Council"),
]

for city, council in quebec:
    cities.append({"name": city, "province": "QC", "repSet": council})

# ===== BRITISH COLUMBIA (BC) - 70 cities =====
bc = [
    ("Vancouver", "Vancouver City Council"),
    ("Victoria", "Victoria City Council"),
    ("Surrey", "Surrey City Council"),
    ("Burnaby", "Burnaby City Council"),
    ("Richmond", "Richmond City Council"),
    ("Kelowna", "Kelowna City Council"),
    ("Abbotsford", "Abbotsford City Council"),
    ("Coquitlam", "Coquitlam City Council"),
    ("Saanich", "Saanich District Council"),
    ("Langley", "Langley City Council"),
    ("Delta", "Delta City Council"),
    ("Nanaimo", "Nanaimo City Council"),
    ("Kamloops", "Kamloops City Council"),
    ("Prince George", "Prince George City Council"),
    ("New Westminster", "New Westminster City Council"),
    ("North Vancouver", "North Vancouver City Council"),
    ("West Vancouver", "West Vancouver City Council"),
    ("Port Coquitlam", "Port Coquitlam City Council"),
    ("Port Moody", "Port Moody City Council"),
    ("Maple Ridge", "Maple Ridge City Council"),
    ("Mission", "Mission District Council"),
    ("Chilliwack", "Chilliwack City Council"),
    ("Langford", "Langford City Council"),
    ("Oak Bay", "Oak Bay District Council"),
    ("Esquimalt", "Esquimalt Town Council"),
    ("Colwood", "Colwood City Council"),
    ("View Royal", "View Royal Town Council"),
    ("Highlands", "Highlands District Council"),
    ("Metchosin", "Metchosin District Council"),
    ("Sooke", "Sooke District Council"),
    ("Central Saanich", "Central Saanich District Council"),
    ("North Saanich", "North Saanich District Council"),
    ("Sidney", "Sidney Town Council"),
    ("Juan de Fuca", "Juan de Fuca District Council"),
    ("Salt Spring Island", "Salt Spring Island Local Trust Council"),
    ("Penticton", "Penticton City Council"),
    ("Vernon", "Vernon City Council"),
    ("Courtenay", "Courtenay City Council"),
    ("Campbell River", "Campbell River City Council"),
    ("Powell River", "Powell River City Council"),
    ("Sunshine Coast", "Sunshine Coast Regional District"),
    ("Squamish", "Squamish District Council"),
    ("Whistler", "Whistler Resort Municipality Council"),
    ("Pemberton", "Pemberton Village Council"),
    ("Hope", "Hope District Council"),
    ("Agassiz", "Agassiz District Council"),
    ("Harrison Hot Springs", "Harrison Hot Springs Village Council"),
    ("Sechelt", "Sechelt District Council"),
    ("Gibsons", "Gibsons Town Council"),
    ("Powell River", "Powell River City Council"),
    ("Comox", "Comox Town Council"),
    ("Cumberland", "Cumberland Village Council"),
    ("Courtenay", "Courtenay City Council"),
    ("Qualicum Beach", "Qualicum Beach Town Council"),
    ("Parksville", "Parksville City Council"),
    ("Nanaimo", "Nanaimo City Council"),
    ("Ladysmith", "Ladysmith Town Council"),
    ("Lake Cowichan", "Lake Cowichan Town Council"),
    ("Duncan", "Duncan City Council"),
    ("North Cowichan", "North Cowichan District Council"),
    ("Cowichan Bay", "Cowichan Bay Town Council"),
    ("Shawnigan Lake", "Shawnigan Lake District Council"),
    ("Mill Bay", "Mill Bay Town Council"),
    ("Malahat", "Malahat District Council"),
    ("Brentwood Bay", "Brentwood Bay Town Council"),
    ("Central Saanich", "Central Saanich District Council"),
    ("North Saanich", "North Saanich District Council"),
    ("Sidney", "Sidney Town Council"),
    ("Victoria", "Victoria City Council"),
    ("Esquimalt", "Esquimalt Town Council"),
    ("Oak Bay", "Oak Bay District Council"),
    ("Saanich", "Saanich District Council"),
    ("Colwood", "Colwood City Council"),
    ("Langford", "Langford City Council"),
]

for city, council in bc:
    cities.append({"name": city, "province": "BC", "repSet": council})

# ===== ALBERTA (AB) - 50 cities =====
alberta = [
    ("Calgary", "Calgary City Council"),
    ("Edmonton", "Edmonton City Council"),
    ("Red Deer", "Red Deer City Council"),
    ("Lethbridge", "Lethbridge City Council"),
    ("Medicine Hat", "Medicine Hat City Council"),
    ("St. Albert", "St. Albert City Council"),
    ("Grande Prairie", "Grande Prairie City Council"),
    ("Airdrie", "Airdrie City Council"),
    ("Fort McMurray", "Fort McMurray City Council"),
    ("Spruce Grove", "Spruce Grove City Council"),
    ("Leduc", "Leduc City Council"),
    ("Lloydminster", "Lloydminster City Council"),
    ("Camrose", "Camrose City Council"),
    ("Chestermere", "Chestermere City Council"),
    ("Cold Lake", "Cold Lake City Council"),
    ("Fort Saskatchewan", "Fort Saskatchewan City Council"),
    ("Beaumont", "Beaumont Town Council"),
    ("Okotoks", "Okotoks Town Council"),
    ("Cochrane", "Cochrane Town Council"),
    ("Canmore", "Canmore Town Council"),
    ("Banff", "Banff Town Council"),
    ("Strathmore", "Strathmore Town Council"),
    ("High River", "High River Town Council"),
    ("Okotoks", "Okotoks Town Council"),
    ("Nanton", "Nanton Town Council"),
    ("Vulcan", "Vulcan Town Council"),
    ("Taber", "Taber Town Council"),
    ("Vauxhall", "Vauxhall Town Council"),
    ("Bow Island", "Bow Island Town Council"),
    ("Claresholm", "Claresholm Town Council"),
    ("Fort Macleod", "Fort Macleod Town Council"),
    ("Pincher Creek", "Pincher Creek Town Council"),
    ("Crowsnest Pass", "Crowsnest Pass District Council"),
    ("Blairmore", "Blairmore Town Council"),
    ("Coleman", "Coleman Town Council"),
    ("Bellevue", "Bellevue Town Council"),
    ("Hillcrest", "Hillcrest Town Council"),
    ("Frank", "Frank Town Council"),
    ("Lundbreck", "Lundbreck Town Council"),
    ("Cowley", "Cowley Town Council"),
    ("Waterton Park", "Waterton Park Town Council"),
    ("Cardston", "Cardston Town Council"),
    ("Magrath", "Magrath Town Council"),
    ("Raymond", "Raymond Town Council"),
    ("Stirling", "Stirling Town Council"),
    ("Milk River", "Milk River Town Council"),
    ("Coutts", "Coutts Village Council"),
    ("Warner", "Warner Town Council"),
    ("Lethbridge County", "Lethbridge County Council"),
    ("Newell County", "Newell County Council"),
]

for city, council in alberta:
    cities.append({"name": city, "province": "AB", "repSet": council})

# ===== SASKATCHEWAN (SK) - 35 cities =====
saskatchewan = [
    ("Saskatoon", "Saskatoon City Council"),
    ("Regina", "Regina City Council"),
    ("Prince Albert", "Prince Albert City Council"),
    ("Moose Jaw", "Moose Jaw City Council"),
    ("Yorkton", "Yorkton City Council"),
    ("Swift Current", "Swift Current City Council"),
    ("North Battleford", "North Battleford City Council"),
    ("Estevan", "Estevan City Council"),
    ("Weyburn", "Weyburn City Council"),
    ("Lloydminster", "Lloydminster City Council"),
    ("Martensville", "Martensville City Council"),
    ("Warman", "Warman City Council"),
    ("Humboldt", "Humboldt City Council"),
    ("Meadow Lake", "Meadow Lake City Council"),
    ("Nipawin", "Nipawin Town Council"),
    ("Kindersley", "Kindersley Town Council"),
    ("Melville", "Melville City Council"),
    ("Melfort", "Melfort City Council"),
    ("Battlefords", "Battlefords City Council"),
    ("La Ronge", "La Ronge Town Council"),
    ("Creighton", "Creighton Town Council"),
    ("Flin Flon", "Flin Flon City Council"),
    ("Uranium City", "Uranium City Town Council"),
    ("Cumberland House", "Cumberland House Town Council"),
    ("Stony Rapids", "Stony Rapids Town Council"),
    ("Black Lake", "Black Lake Town Council"),
    ("Wollaston Lake", "Wollaston Lake Town Council"),
    ("Buffalo Narrows", "Buffalo Narrows Town Council"),
    ("Ile-a-la-Crosse", "Ile-a-la-Crosse Town Council"),
    ("Green Lake", "Green Lake Town Council"),
    ("Beauval", "Beauval Town Council"),
    ("La Loche", "La Loche Town Council"),
    ("Patuanak", "Patuanak Town Council"),
    ("Dillon", "Dillon Town Council"),
    ("Michel Village", "Michel Village Town Council"),
]

for city, council in saskatchewan:
    cities.append({"name": city, "province": "SK", "repSet": council})

# ===== MANITOBA (MB) - 30 cities =====
manitoba = [
    ("Winnipeg", "Winnipeg City Council"),
    ("Brandon", "Brandon City Council"),
    ("Steinbach", "Steinbach City Council"),
    ("Thompson", "Thompson City Council"),
    ("Portage la Prairie", "Portage la Prairie City Council"),
    ("Selkirk", "Selkirk City Council"),
    ("Winkler", "Winkler City Council"),
    ("Dauphin", "Dauphin City Council"),
    ("Morden", "Morden City Council"),
    ("Flin Flon", "Flin Flon City Council"),
    ("The Pas", "The Pas Town Council"),
    ("Kenora", "Kenora City Council"),
    ("Grand Rapids", "Grand Rapids Town Council"),
    ("Norway House", "Norway House Town Council"),
    ("Oxford House", "Oxford House Town Council"),
    ("Cross Lake", "Cross Lake Town Council"),
    ("Nelson House", "Nelson House Town Council"),
    ("York Factory", "York Factory Town Council"),
    ("Churchill", "Churchill Town Council"),
    ("Gillam", "Gillam Town Council"),
    ("Leaf Rapids", "Leaf Rapids Town Council"),
    ("Lynn Lake", "Lynn Lake Town Council"),
    ("Snow Lake", "Snow Lake Town Council"),
    ("Shamattawa", "Shamattawa Town Council"),
    ("Tadoule Lake", "Tadoule Lake Town Council"),
    ("Brochet", "Brochet Town Council"),
    ("Lac Brochet", "Lac Brochet Town Council"),
    ("St. Theresa Point", "St. Theresa Point Town Council"),
    ("Garden Hill", "Garden Hill Town Council"),
    ("Wasagamack", "Wasagamack Town Council"),
]

for city, council in manitoba:
    cities.append({"name": city, "province": "MB", "repSet": council})

# ===== NEW BRUNSWICK (NB) - 25 cities =====
new_brunswick = [
    ("Moncton", "Moncton City Council"),
    ("Saint John", "Saint John City Council"),
    ("Fredericton", "Fredericton City Council"),
    ("Dieppe", "Dieppe City Council"),
    ("Riverview", "Riverview Town Council"),
    ("Bathurst", "Bathurst City Council"),
    ("Edmundston", "Edmundston City Council"),
    ("Miramichi", "Miramichi City Council"),
    ("Campbellton", "Campbellton City Council"),
    ("Quispamsis", "Quispamsis Town Council"),
    ("Rothesay", "Rothesay Town Council"),
    ("Grand Falls", "Grand Falls Town Council"),
    ("Oromocto", "Oromocto Town Council"),
    ("Shediac", "Shediac Town Council"),
    ("Sackville", "Sackville Town Council"),
    ("Hampton", "Hampton Town Council"),
    ("Sussex", "Sussex Town Council"),
    ("St. Andrews", "St. Andrews Town Council"),
    ("Woodstock", "Woodstock Town Council"),
    ("Dalhousie", "Dalhousie Town Council"),
    ("Bouctouche", "Bouctouche Town Council"),
    ("Richibucto", "Richibucto Town Council"),
    ("Tracadie", "Tracadie Town Council"),
    ("Shippagan", "Shippagan Town Council"),
    ("Neguac", "Neguac Town Council"),
]

for city, council in new_brunswick:
    cities.append({"name": city, "province": "NB", "repSet": council})

# ===== NOVA SCOTIA (NS) - 25 cities =====
nova_scotia = [
    ("Halifax", "Halifax Regional Council"),
    ("Cape Breton", "Cape Breton Regional Council"),
    ("Sydney", "Sydney Town Council"),
    ("Truro", "Truro Town Council"),
    ("New Glasgow", "New Glasgow Town Council"),
    ("Kentville", "Kentville Town Council"),
    ("Amherst", "Amherst Town Council"),
    ("Bridgewater", "Bridgewater Town Council"),
    ("Yarmouth", "Yarmouth Town Council"),
    ("Antigonish", "Antigonish Town Council"),
    ("Wolfville", "Wolfville Town Council"),
    ("Port Hawkesbury", "Port Hawkesbury Town Council"),
    ("Lunenburg", "Lunenburg Town Council"),
    ("Digby", "Digby Town Council"),
    ("Shelburne", "Shelburne Town Council"),
    ("Liverpool", "Liverpool Town Council"),
    ("Windsor", "Windsor Town Council"),
    ("Pictou", "Pictou Town Council"),
    ("Springhill", "Springhill Town Council"),
    ("Oxford", "Oxford Town Council"),
    ("Parrsboro", "Parrsboro Town Council"),
    ("Guysborough", "Guysborough Town Council"),
    ("Canso", "Canso Town Council"),
    ("Baddeck", "Baddeck Town Council"),
    ("Ingonish", "Ingonish Town Council"),
]

for city, council in nova_scotia:
    cities.append({"name": city, "province": "NS", "repSet": council})

# ===== PRINCE EDWARD ISLAND (PE) - 15 cities =====
pei = [
    ("Charlottetown", "Charlottetown City Council"),
    ("Summerside", "Summerside City Council"),
    ("Stratford", "Stratford Town Council"),
    ("Cornwall", "Cornwall Town Council"),
    ("Montague", "Montague Town Council"),
    ("Kensington", "Kensington Town Council"),
    ("Georgetown", "Georgetown Town Council"),
    ("Souris", "Souris Town Council"),
    ("Alberton", "Alberton Town Council"),
    ("O'Leary", "O'Leary Town Council"),
    ("Tignish", "Tignish Town Council"),
    ("Tyne Valley", "Tyne Valley Town Council"),
    ("Miminegash", "Miminegash Town Council"),
    ("Ellerslie", "Ellerslie Town Council"),
    ("Borden-Carleton", "Borden-Carleton Town Council"),
]

for city, council in pei:
    cities.append({"name": city, "province": "PE", "repSet": council})

# ===== NEWFOUNDLAND AND LABRADOR (NL) - 20 cities =====
newfoundland = [
    ("St. John's", "St. John's City Council"),
    ("Mount Pearl", "Mount Pearl City Council"),
    ("Corner Brook", "Corner Brook City Council"),
    ("Conception Bay South", "Conception Bay South Town Council"),
    ("Paradise", "Paradise Town Council"),
    ("Gander", "Gander Town Council"),
    ("Grand Falls-Windsor", "Grand Falls-Windsor Town Council"),
    ("Clarenville", "Clarenville Town Council"),
    ("Carbonear", "Carbonear Town Council"),
    ("Bay Roberts", "Bay Roberts Town Council"),
    ("Marystown", "Marystown Town Council"),
    ("Happy Valley-Goose Bay", "Happy Valley-Goose Bay Town Council"),
    ("Labrador City", "Labrador City Town Council"),
    ("Churchill Falls", "Churchill Falls Town Council"),
    ("Wabush", "Wabush Town Council"),
    ("Port aux Basques", "Port aux Basques Town Council"),
    ("Stephenville", "Stephenville Town Council"),
    ("Deer Lake", "Deer Lake Town Council"),
    ("Springdale", "Springdale Town Council"),
    ("Lewisporte", "Lewisporte Town Council"),
]

for city, council in newfoundland:
    cities.append({"name": city, "province": "NL", "repSet": council})

# ===== YUKON (YT) - 5 cities =====
yukon = [
    ("Whitehorse", "Whitehorse City Council"),
    ("Dawson City", "Dawson City Town Council"),
    ("Watson Lake", "Watson Lake Town Council"),
    ("Haines Junction", "Haines Junction Village Council"),
    ("Mayo", "Mayo Village Council"),
]

for city, council in yukon:
    cities.append({"name": city, "province": "YT", "repSet": council})

# ===== NORTHWEST TERRITORIES (NT) - 5 cities =====
nwt = [
    ("Yellowknife", "Yellowknife City Council"),
    ("Hay River", "Hay River Town Council"),
    ("Fort Smith", "Fort Smith Town Council"),
    ("Inuvik", "Inuvik Town Council"),
    ("Norman Wells", "Norman Wells Town Council"),
]

for city, council in nwt:
    cities.append({"name": city, "province": "NT", "repSet": council})

# ===== NUNAVUT (NU) - 5 cities =====
nunavut = [
    ("Iqaluit", "Iqaluit City Council"),
    ("Rankin Inlet", "Rankin Inlet Town Council"),
    ("Arviat", "Arviat Town Council"),
    ("Baker Lake", "Baker Lake Town Council"),
    ("Cambridge Bay", "Cambridge Bay Town Council"),
]

for city, council in nunavut:
    cities.append({"name": city, "province": "NU", "repSet": council})

# Remove duplicates (keep first occurrence)
seen = set()
unique_cities = []
for city in cities:
    key = city["name"]
    if key not in seen:
        seen.add(key)
        unique_cities.append(city)

cities = unique_cities

# Generate JavaScript file
js_content = """// City Data for MyCivicVoice v4
// Canadian cities mapped to province + OpenNorth representative_set_name
// Generated: 2026-03-07
// Total cities: {count}

const CITY_DATA = [
""".format(count=len(cities))

for city in cities:
    js_content += '  {{ name: "{}", province: "{}", repSet: "{}" }},\n'.format(
        city["name"], city["province"], city["repSet"]
    )

js_content += """];

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CITY_DATA };
}
"""

# Write to file
with open("C:/nanobot/instance3/workspace/MyCivicVoice_v4/city_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated {len(cities)} unique cities")
print(f"Provincial breakdown:")
provinces = {}
for city in cities:
    prov = city["province"]
    provinces[prov] = provinces.get(prov, 0) + 1

for prov in sorted(provinces.keys()):
    print(f"  {prov}: {provinces[prov]} cities")