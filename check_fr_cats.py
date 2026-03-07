import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the FR object
fr_start = content.find('const FR = {')
if fr_start == -1:
    print('FR object not found')
else:
    # Find the end of FR object (next const or end of script)
    fr_end = content.find('\nconst ', fr_start + 10)
    fr_section = content[fr_start:fr_end]
    
    # The 16 categories that were missing
    missing_cats = ['lgbtq', 'women', 'mentalhealth', 'substance', 'transportation', 'digital', 'animals', 'sports', 'religion', 'volunteer', 'legalaid', 'pensions', 'childcare', 'food', 'emergency', 'humanrights']
    
    print('Checking FR.categories for missing translations:')
    for cat in missing_cats:
        pattern = f'{cat}: "'
        if pattern in fr_section:
            # Find the value
            idx = fr_section.find(pattern)
            start = idx + len(pattern)
            end = fr_section.find('"', start)
            value = fr_section[start:end]
            print(f'  {cat}: "{value}"')
        else:
            print(f'  {cat}: MISSING')