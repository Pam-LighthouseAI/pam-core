with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Show context around line 3068
for i in range(3065, 3080):
    if i < len(lines):
        print(f'{i+1}: {lines[i].rstrip()}')
