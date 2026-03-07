with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Show context around line 3059
for i in range(3054, 3080):
    if i < len(lines):
        print(f'{i+1}: {lines[i].rstrip()}')
