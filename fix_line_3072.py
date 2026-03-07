with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if i == 3071:  # Line 3072 (0-indexed)
        print(f'Removing: {line.strip()}')
        continue
    new_lines.append(line)

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Fixed!')