# Check escalation script tag
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find script tag for escalation
idx = content.find('escalation')
while idx > 0:
    start = max(0, idx - 50)
    end = min(len(content), idx + 50)
    print(f"Found at {idx}:")
    print(content[start:end])
    print("---")
    idx = content.find('escalation', idx + 1)