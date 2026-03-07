with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find any line with fontSize:20
for i, line in enumerate(lines):
    if 'fontSize:20' in line:
        print(f'Line {i+1}: {line.rstrip()}')