with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

start = c.find('<div class="ambient">')
print('Start position:', start)

# Find the end of ambient div - look for the container div after it
container_start = c.find('<div class="container"', start)
print('Container start:', container_start)

# The ambient div ends before container
ambient_end = c.rfind('</div></div>', start, container_start)
print('Ambient end:', ambient_end)

# Get the section (without printing emojis)
section = c[start:ambient_end + 12]  # include </div></div>
print('Section length:', len(section))

# Count maple-leaf divs
leaf_count = section.count('class="maple-leaf"')
print('Current leaf count:', leaf_count)

# Create new section with 18 maple leaves
new_section = '<div class="ambient"><div class="glow1"></div><div class="glow2"></div>'
for i in range(18):
    new_section += '<div class="maple-leaf">\U0001f341</div>'
new_section += '</div></div>'

print('New section length:', len(new_section))

# Replace
new_content = c[:start] + new_section + c[ambient_end + 12:]

with open(r'D:\source_extracted\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Done! Updated to 18 maple leaves.')