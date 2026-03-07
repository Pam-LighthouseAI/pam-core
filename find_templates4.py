with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find lines with "template" (case insensitive)
for i, line in enumerate(lines):
    if 'template' in line.lower() and i > 200 and i < 500:
        print(f'Line {i+1}: {line.rstrip()[:120]}')