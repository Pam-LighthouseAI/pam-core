# Find the maple leaf section
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the section with federal/provincial/municipal
idx = content.find('informed citizens')
if idx > 0:
    # Show context around it
    start = max(0, idx - 500)
    end = min(len(content), idx + 500)
    print(f"Context (position {idx}):")
    print(content[start:end])
else:
    print("Not found, searching for 'Federal'")
    idx = content.find('Federal')
    if idx > 0:
        start = max(0, idx - 200)
        end = min(len(content), idx + 200)
        print(content[start:end])