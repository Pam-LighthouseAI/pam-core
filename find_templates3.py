with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find lines with "subject:" or "body:" which are template definitions
for i, line in enumerate(lines):
    line_lower = line.lower()
    if ('subject:' in line_lower or 'body:' in line_lower) and i < 500:
        print(f'Line {i+1}: {line.rstrip()[:100]}')