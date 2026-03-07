import os

file_path = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace uName || namePlaceholder with just namePlaceholder
old = 'uName || namePlaceholder'
new = 'namePlaceholder'

if old in content:
    content = content.replace(old, new)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Replaced successfully')
else:
    print('Pattern not found')