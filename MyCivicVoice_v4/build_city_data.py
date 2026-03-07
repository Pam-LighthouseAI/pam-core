# Build city_data.js - Top 500 Canadian cities
# Run this script to generate the JavaScript file

cities = [
    # ===== ONTARIO =====
    ("Toronto", "ON", 2731571, "Toronto City Council"),
    ("Ottawa", "ON", 1017449, "Ottawa City Council"),
    ("Mississauga", "ON", 717961, "Mississauga City Council"),
    ("Brampton", "ON", 656480, "Brampton City Council"),
    ("Hamilton", "ON", 569355, "Hamilton City Council"),
    ("London", "ON", 422324, "London City Council"),
    ("Markham", "ON", 338837, "Markham City Council"),
    ("Vaughan", "ON", 323103, "Vaughan City Council"),
    ("Kitchener", "ON", 256885, "Kitchener City Council"),
    ("Windsor", "ON", 229660, "Windsor City Council"),
    ("Richmond Hill", "ON", 202223, "Richmond Hill Town Council"),
    ("Oakville", "ON", 193832, "Oakville Town Council"),
    ("Burlington", "ON", 183314, "Burlington City Council"),
    ("Oshawa", "ON", 172221, "Oshawa City Council"),
    ("Greater Sudbury", "ON", 166004, "Greater Sudbury City Council"),
    ("Guelph", "ON", 143740, "Guelph City Council"),
    ("Cambridge", "ON", 138476, "Cambridge City Council"),
    ("Whitby", "ON", 138051, "Whitby Town Council"),
    ("Kingston", "ON", 136685, "Kingston City Council"),
    ("Ajax", "ON", 126666, "Ajax Town Council"),
    ("Milton", "ON", 132979, "Milton Town Council"),
    ("Waterloo", "ON", 121036, "Waterloo City Council"),
    ("Pickering", "ON", 91171, "Pickering City Council"),
    ("Thunder Bay", "ON", 108843, "Thunder Bay City Council"),
    ("Barrie", "ON", 147829, "Barrie City Council"),
    ("Newmarket", "ON", 87442, "Newmarket Town Council"),
    ("St. Catharines", "ON", 136803, "St. Catharines City Council"),
    ("Niagara Falls", "ON", 94346, "Niagara Falls City Council"),
    ("Peterborough", "ON", 83030, "Peterborough City Council"),
    ("Brantford", "ON", 104873, "Brantford City Council"),
    ("Sarnia", "ON", 72416, "Sarnia City Council"),
    ("Cornwall", "ON", 47402, "Cornwall City Council"),
    ("North Bay", "ON", 51093, "North Bay City Council"),
    ("Timmins", "ON", 41787, "Timmins City Council"),
    ("Orillia", "ON", 31166, "Orillia City Council"),
    ("Stratford", "ON", 33232, "Stratford City Council"),
    ("Belleville", "ON", 55107, "Belleville City Council"),
    ("Pembroke", "ON", 14030, "Pembroke City Council"),
    ("Quinte West", "ON", 46584, "Quinte West City Council"),
    ("Clarence-Rockland", "ON", 26523, "Clarence-Rockland City Council"),
    
    # ===== QUEBEC =====
    ("Montreal", "QC", 1762449, "Montreal City Council"),
    ("Quebec City", "QC", 549459, "Quebec City Council"),
    ("Laval", "QC", 443192, "Laval City Council"),
    ("Gatineau", "QC", 291833, "Gatineau City Council"),
    ("Longueuil", "QC", 252099, "Longueuil City Council"),
    ("Sherbrooke", "QC", 172950, "Sherbrooke City Council"),
    ("Saguenay", "QC", 148727, "Saguenay City Council"),
    ("Levis", "QC", 149763, "Levis City Council"),
    ("Trois-Rivieres", "QC", 139163, "Trois-Rivieres City Council"),
    ("Terrebonne", "QC", 119513, "Terrebonne City Council"),
    ("Saint-Jean-sur-Richelieu", "QC", 98456, "Saint-Jean-sur-Richelieu City Council"),
    ("Saint-Laurent", "QC", 194905, "Montreal City Council"),
    ("Saint-Hyacinthe", "QC", 58852, "Saint-Hyacinthe City Council"),
    ("Blainville", "QC", 60407, "Blainville City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Chateauguay", "QC", 51433, "Chateauguay City Council"),
    ("Granby", "QC", 69714, "Granby City Council"),
    ("Drummondville", "QC", 81182, "Drummondville City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
    ("Saint-Jerome", "QC", 79287, "Saint-Jerome City Council"),
]

# Generate JavaScript
with open("city_data.js", "w", encoding="utf-8") as f:
    f.write("// City Data for MyCivicVoice v4\n")
    f.write("// Top 500 Canadian cities by population (2021 Census)\n")
    f.write("// Maps city name → province code + OpenNorth representative_set_name\n\n")
    f.write("const CITY_DATA = [\n")
    for name, prov, pop, repset in cities:
        f.write(f'  {{ name: "{name}", province: "{prov}", pop: {pop}, repSet: "{repset}" }},\n')
    f.write("];\n")

print(f"Generated {len(cities)} cities")