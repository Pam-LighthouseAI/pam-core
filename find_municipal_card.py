# Find Municipal card in why-visual
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Municipal in the context of the visual cards
# Search for pattern near "Municipal" with empty span
idx = content.find("'Municipal'")
while idx > 0:
    start = max(0, idx - 300)
    end = min(len(content), idx + 100)
    section = content[start:end]
    if 'fontSize:24' in section or 'span' in section:
        print(f"Found at {idx}:")
        print(section)
        print("---")
    idx = content.find("'Municipal'", idx + 1)