import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the FR object
fr_start = content.find('const FR = {')
if fr_start == -1:
    print('FR object not found')
else:
    fr_end = content.find('\nconst ', fr_start + 10)
    fr_section = content[fr_start:fr_end]
    
    # Find all lines with "education" in FR section
    lines = fr_section.split('\n')
    for i, line in enumerate(lines):
        if 'education' in line.lower():
            print(f'Line {i}: {line.strip()[:100]}')