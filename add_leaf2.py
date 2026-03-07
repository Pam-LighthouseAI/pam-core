with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find line 146 (index 145) and add one more maple-leaf
for i, line in enumerate(lines):
    if 'class="ambient"' in line and 'maple-leaf' in line:
        # Add one more maple-leaf before the closing </div></div>
        # The line ends with </div></div>
        new_line = line.replace('</div></div>', '<div class="maple-leaf">🍁</div></div></div>')
        lines[i] = new_line
        break

with open(r'D:\source_extracted\index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Done')