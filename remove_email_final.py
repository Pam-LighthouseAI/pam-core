import re

file_path = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Skip email input lines
    if 'type="email"' in line and 'form.email' in line:
        continue
    # Skip yourEmail translation
    if 'yourEmail:' in line:
        continue
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Removed remaining email elements')