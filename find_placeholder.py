# Find the Escalation Component placeholder
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the placeholder
idx = content.find('Escalation Component Placeholder')
if idx != -1:
    print('Found at index', idx)
    # Show context
    start = max(0, idx - 100)
    end = min(len(content), idx + 500)
    print('Context:')
    print(content[start:end])
else:
    print('Placeholder not found')