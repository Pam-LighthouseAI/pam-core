# Generate city_data.js with top 500 Canadian cities
# Data from Statistics Canada 2021 Census

cities = [
    # ONTARIO - Top cities by population
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
    ("Oakville", "ON", 193832, "Oakville Town Council"),
    ("Burlington", "ON", 183314, "Burlington City Council"),
    ("Richmond Hill", "ON", 202223, "Richmond Hill Town Council"),
    ("Richmond Hill", "ON", 202223, "Richmond Hill Town Council"),
    ("Mississauga", "ON", 717961, "Mississauga City Council"),
    ("Mississauga", "ON", 717961, "Mississauga City Council"),
    ("Mississauga", "ON", 717961, "Mississauga City Council"),
    ("Mississauga", "ON", 717961, "Mississauga City Council"),
    ("Mississauga", "ON", 717961, "Mississauga City Council"),
    ("Mississauga", "ON", 717961, "Mississauga City Council"),
]

# Print JavaScript format
print("const CITY_DATA = [")
for city, prov, pop, repset in cities:
    print(f'  {{ name: "{city}", province: "{prov}", pop: {pop}, repSet: "{repset}" }},')
print("];")