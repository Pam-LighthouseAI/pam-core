# Find the EN object in the file
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the EN object
idx = content.find('const EN = {')
if idx != -1:
    # Find the closing brace
    end_idx = content.find('};', idx)
    if end_idx != -1:
        print('EN object found at index', idx)
        print('Closing brace at index', end_idx)
        print('Content:')
        print(content[idx:end_idx+100])
else:
    print('EN object not found')
    # Try alternative
    idx = content.find('EN = {')
    if idx != -1:
        print('Found EN = { at index', idx)
        print('Context:', content[idx:idx+200])