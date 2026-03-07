# Check current city lookup implementation
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find different possible names
searches = ['selCity', 'cityDropdown', 'citySelect', 'lookupType', 'byCity', 'cities']
for search in searches:
    idx = content.find(search)
    if idx > 0:
        print(f"Found '{search}' at position {idx}")
        start = max(0, idx - 20)
        end = min(len(content), idx + 200)
        print(content[start:end])
        print("---")