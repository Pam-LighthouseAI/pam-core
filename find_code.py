import re

with open(r'C:\nanobot\instance3\workspace\MyCivicVoice_v4\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find isFinder usage
matches = list(re.finditer(r'isFinder', content))
print(f'Found {len(matches)} isFinder references')

for m in matches:
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 200)
    print(f'\n--- At {m.start()} ---')
    print(content[start:end])