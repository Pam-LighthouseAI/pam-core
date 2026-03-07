with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the broken span (missing }})
import re
matches = re.findall(r'<span style=\{\{fontSize:20[^}]*</span>', content)
print(f'Found {len(matches)} broken spans:')
for m in matches:
    print(f'  {m}')