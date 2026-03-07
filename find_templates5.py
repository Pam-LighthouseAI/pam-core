with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find lines with "TEMPLATES" or category template definitions
for i, line in enumerate(lines):
    if 'TEMPLATES' in line or ('subject:' in line.lower() and 'body:' not in line.lower()):
        print(f'Line {i+1}: {line.rstrip()[:100]}')