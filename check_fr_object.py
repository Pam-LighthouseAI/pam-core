import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the FR object
fr_start = content.find('const FR = {')
if fr_start == -1:
    print('FR object not found')
else:
    fr_end = content.find('\nconst ', fr_start + 10)
    fr_section = content[fr_start:fr_end]
    
    # Check for common French words missing accents
    issues = [
        ('education', 'éducation'),
        ('Education', 'Éducation'),
        ('ecole', 'école'),
        ('Ecole', 'École'),
        ('preoccupation', 'préoccupation'),
        ('Preoccupation', 'Préoccupation'),
        ('securite', 'sécurité'),
        ('Securite', 'Sécurité'),
        ('sante', 'santé'),
        ('Sante', 'Santé'),
        ('Confidentialite', 'Confidentialité'),
        ('Telephone', 'Téléphone'),
        ('Representation', 'Représentation'),
    ]
    
    print('Checking FR object for accent issues:')
    found_issues = []
    for wrong, correct in issues:
        if wrong in fr_section:
            found_issues.append(f'  FOUND: "{wrong}" should be "{correct}"')
    
    if found_issues:
        print('\n'.join(found_issues))
    else:
        print('NO ISSUES FOUND!')