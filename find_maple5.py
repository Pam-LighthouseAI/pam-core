# Find the full why-visual section
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

babel_start = content.find('<script type="text/babel">')
if babel_start > 0:
    jsx_content = content[babel_start:]
    
    # Find why-visual section and show more
    idx = jsx_content.find('why-visual')
    if idx > 0:
        start = idx
        end = min(len(jsx_content), idx + 1500)
        print("Full why-visual section:")
        print(jsx_content[start:end])