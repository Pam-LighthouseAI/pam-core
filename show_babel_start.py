with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Show lines 340-400 to find where templates are defined
for i in range(340, 450):
    if i < len(lines):
        print(f'{i+1}: {lines[i].rstrip()}')