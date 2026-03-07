with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find and remove the empty span line
new_lines = []
for i, line in enumerate(lines):
    # Check if this line is the problematic empty span
    if '<span style={{fontSize:20}}></span>' in line and i > 3060 and i < 3080:
        print(f'Removing line {i+1}: {line.strip()}')
        continue  # Skip this line
    new_lines.append(line)

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'Done! Removed empty span line.')
