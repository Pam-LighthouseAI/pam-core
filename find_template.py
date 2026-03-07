with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find template-related code - look for generateLetter or template functions
for i, line in enumerate(lines):
    if 'generateLetter' in line or 'getTemplate' in line or 'template' in line.lower() and 'function' in line.lower():
        print(f'Line {i+1}: {line.rstrip()}')