import re

with open(r'C:\nanobot\instance3\workspace\MyCivicVoice_v4\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where reps are rendered - look for representative cards
# Find the section that renders reps.municipal
match = re.search(r'reps\.municipal\.map', content)
if match:
    print('Found reps.municipal.map at:', match.start())
    print('---')
    print(content[match.start():match.start()+1500])