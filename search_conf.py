import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all instances of Confidentialit
matches = list(re.finditer(r'Confidentialit[eé]', content))
with open('conf_results.txt', 'w', encoding='utf-8') as f:
    f.write(f'Found {len(matches)} matches:\n')
    for m in matches:
        start = max(0, m.start() - 30)
        end = min(len(content), m.end() + 30)
        f.write(f'  {m.group()}: ...{content[start:end]}...\n')