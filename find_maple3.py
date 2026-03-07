# Find the federal/provincial/municipal content section
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find "Federal" in the JSX section (after the Babel script starts)
babel_start = content.find('<script type="text/babel">')
if babel_start > 0:
    # Search after Babel starts
    jsx_content = content[babel_start:]
    
    # Find Federal in JSX
    idx = jsx_content.find('Federal')
    if idx > 0:
        # Show context
        start = max(0, idx - 100)
        end = min(len(jsx_content), idx + 400)
        print("Federal section in JSX:")
        print(jsx_content[start:end])