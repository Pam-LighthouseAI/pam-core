# Find the federal/provincial/municipal grid section
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the why-grid section
idx = content.find('why-grid')
if idx > 0:
    # Show more context
    start = idx
    end = min(len(content), idx + 2000)
    print("Why-grid section:")
    print(content[start:end])