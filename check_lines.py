with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(2726, 2740):
    if i < len(lines):
        print(f'{i+1}: {lines[i].rstrip()}')
