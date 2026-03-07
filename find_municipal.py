# Find the Municipal section
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Municipal in the why-visual area
idx = content.find('Municipal')
count = 0
while idx >0 and count < 5:
    start = max(0, idx - 100)
    end = min(len(content), idx + 200)
    print(f"\n--- Found at position {idx} ---")
    print(content[start:end])
    idx = content.find('Municipal', idx + 1)
    count += 1