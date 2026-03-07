import re

file_path = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Skip the yourFullName and yourPhone lines
    if 'yourFullName:' in line or 'yourPhone:' in line:
        continue
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Removed unused translations')