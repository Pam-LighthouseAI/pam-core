# Check current city lookup implementation
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find city-related code
idx = content.find('cityLookup')
if idx > 0:
    section = content[idx:idx+3000]
    with open(r'C:\nanobot\instance3\workspace\city_output.txt', 'w', encoding='utf-8') as f:
        f.write(section)
    print("Written to city_output.txt")

# Also find the city list
idx2 = content.find('CITIES')
if idx2 > 0:
    section2 = content[idx2:idx2+2000]
    with open(r'C:\nanobot\instance3\workspace\cities_list.txt', 'w', encoding='utf-8') as f:
        f.write(section2)
    print("Written to cities_list.txt")