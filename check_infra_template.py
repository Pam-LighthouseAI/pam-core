import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the infrastructure template
templates_match = re.search(r'const TEMPLATES = \{([\s\S]*?)\n\};', content)
if templates_match:
    templates = templates_match.group(1)
    
    # Find infrastructure template - look for the full block
    infra_match = re.search(r'infrastructure:\s*\{[\s\S]*?subject:[\s\S]*?bodyFr:[^}]+\}', templates)
    if infra_match:
        print("Infrastructure template found:")
        print(infra_match.group(0)[:1000])
    else:
        print("Could not find infrastructure template with standard pattern")
        # Show what's around 'infrastructure:' in templates
        idx = templates.find('infrastructure:')
        if idx >= 0:
            print(f"\nContext around 'infrastructure:' position {idx}:")
            print(templates[max(0,idx-50):idx+200])