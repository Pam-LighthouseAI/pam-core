with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
removed = 0
for i, line in enumerate(lines):
    if '<span style={{fontSize:20}}></span>' in line:
        print(f'Removing line {i+1}: {line.strip()}')
        removed += 1
        continue
    new_lines.append(line)

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'Removed {removed} empty span lines.')