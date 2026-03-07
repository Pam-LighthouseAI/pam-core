with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the ISSUES array to see all categories
in_issues = False
for i, line in enumerate(lines):
    if 'const ISSUES = [' in line or 'const ISSUES=[' in line:
        in_issues = True
        print(f'Line {i+1}: ISSUES array starts here')
    if in_issues:
        if 'id:' in line.lower() and ('name:' in line.lower() or 'nameFr' in line):
            print(f'Line {i+1}: {line.strip()[:100]}')
        if '];' in line:
            print(f'Line {i+1}: ISSUES array ends')
            break