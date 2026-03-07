import re

with open(r'D:\source_extracted\my_civic_voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix "ducation" -> "Éducation" in French content
fixes = [
    # In FR object
    ('education: "ducation",', 'education: "Éducation",'),
    
    # In labelFr
    ('labelFr:"ducation",', 'labelFr:"Éducation",'),
    
    # In nameFr
    ('nameFr:"ducation dans les', 'nameFr:"Éducation dans les'),
    
    # In subjectFr
    ('nameFr:"ducation', 'nameFr:"Éducation'),
    
    # Preoccupation without accent
    ('"Preoccupation concernant', '"Préoccupation concernant'),
    ("'Preoccupation concernant", "'Préoccupation concernant"),
]

fixes_applied = 0
for wrong, correct in fixes:
    if wrong in content:
        content = content.replace(wrong, correct)
        fixes_applied += 1

# Write the fixed content
with open(r'D:\source_extracted\my_civic_voice.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Total fixes applied: {fixes_applied}')