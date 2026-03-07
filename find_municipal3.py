# Find Municipal in the JSX section
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Babel script
babel_idx = content.find('<script type="text/babel">')
if babel_idx > 0:
    jsx_content = content[babel_idx:]
    
    # Find the why-visual div in JSX (after return statement)
    # Search for the pattern with Municipal
    idx = jsx_content.find("'Municipal'")
    if idx > 0:
        start = max(0, idx - 200)
        end = min(len(jsx_content), idx + 200)
        print("Municipal in JSX:")
        print(jsx_content[start:end])