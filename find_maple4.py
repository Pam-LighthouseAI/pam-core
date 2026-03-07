# Find the visual section with federal/provincial/municipal
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find "why-visual" in JSX
babel_start = content.find('<script type="text/babel">')
if babel_start > 0:
    jsx_content = content[babel_start:]
    
    # Find why-visual section
    idx = jsx_content.find('why-visual')
    if idx > 0:
        # Show context
        start = max(0, idx - 50)
        end = min(len(jsx_content), idx + 800)
        print("Why-visual section:")
        print(jsx_content[start:end])