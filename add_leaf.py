import re

with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the ambient div and add one more maple-leaf
# Look for the pattern: </div></div></div> at the end of the ambient section
# We want to add before the last two closing </div> tags

# Find where the maple-leaf divs end
pattern = r'(<div class="maple-leaf">[^<]*</div>)(\s*</div>\s*</div>\s*</body>)'
new_content = re.sub(pattern, r'\1<div class="maple-leaf">🍁</div>\2', content, count=1)

with open(r'D:\source_extracted\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Added 19th leaf')