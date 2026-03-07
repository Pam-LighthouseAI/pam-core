# Verify maple leaves in why-visual section
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Count maple leaf unicode escapes
maple_count = content.count("\\uD83C\\uDF41")
print(f"Maple leaf emojis found: {maple_count}")

# Find the why-visual JSX section
babel_idx = content.find('<script type="text/babel">')
if babel_idx > 0:
    jsx = content[babel_idx:]
    # Find the why-visual div in renderLanding
    idx = jsx.find('why-visual')
    if idx > 0:
        section = jsx[idx:idx+1500]
        print("\nWhy-visual section:")
        print(section[:1000])