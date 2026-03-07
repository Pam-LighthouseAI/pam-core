# Find the Municipal in why-visual section
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the why-visual section
idx = content.find('why-visual')
if idx > 0:
    # Search for Municipal within 2000 chars after why-visual
    section = content[idx:idx+2000]
    print("Why-visual section:")
    print(section)