# Fix all double-encoded UTF-8 characters in the file
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

# Double-encoded UTF-8 fix
# When UTF-8 is double-encoded, characters like é (U+00E9) become:
# é -> \xc3\xa9 (UTF-8) -> \xc3\x83\xc2\xa9 (double-encoded)
# We need to decode the double-encoded bytes

# Common double-encoded patterns and their correct forms:
replacements = [
    # Double-encoded vowels with accents
    (b'\xc3\x83\xc2\xa0', b'\xc3\xa0'),  # à
    (b'\xc3\x83\xc2\xa1', b'\xc3\xa1'),  # á
    (b'\xc3\x83\xc2\xa2', b'\xc3\xa2'),  # â
    (b'\xc3\x83\xc2\xa3', b'\xc3\xa3'),  # ã
    (b'\xc3\x83\xc2\xa4', b'\xc3\xa4'),  # ä
    (b'\xc3\x83\xc2\xa7', b'\xc3\xa7'),  # ç
    (b'\xc3\x83\xc2\xa8', b'\xc3\xa8'),  # è
    (b'\xc3\x83\xc2\xa9', b'\xc3\xa9'),  # é
    (b'\xc3\x83\xc2\xaa', b'\xc3\xaa'),  # ê
    (b'\xc3\x83\xc2\xab', b'\xc3\xab'),  # ë
    (b'\xc3\x83\xc2\xae', b'\xc3\xae'),  # î
    (b'\xc3\x83\xc2\xaf', b'\xc3\xaf'),  # ï
    (b'\xc3\x83\xc2\xb4', b'\xc3\xb4'),  # ô
    (b'\xc3\x83\xc2\xb6', b'\xc3\xb6'),  # ö
    (b'\xc3\x83\xc2\xb9', b'\xc3\xb9'),  # ù
    (b'\xc3\x83\xc2\xbb', b'\xc3\xbb'),  # û
    (b'\xc3\x83\xc2\xbc', b'\xc3\xbc'),  # ü
    
    # Double-encoded capital letters
    (b'\xc3\x83\xe2\x80\xb0', b'\xc3\x89'),  # É (special case)
    (b'\xc3\x82\xc2\xa9', b'\xc2\xa9'),  # ©
    
    # Other common double-encoded chars
    (b'\xc3\x83\xc2\xbb', b'\xc3\xbb'),  # û
    (b'\xc3\x83\xc2\x82', b'\xc3\x82'),  # Â
]

for old, new in replacements:
    content = content.replace(old, new)

# Also fix the special É case (Étape)
content = content.replace(b'\xc3\x83\xe2\x80\xb0', b'\xc3\x89')

with open(r'D:\MyCivicVoice_Deploy\index.html', 'wb') as f:
    f.write(content)

print("Fixed all double-encoded characters")

# Count remaining issues
remaining = content.count(b'\xc3\x83\xc2')
print(f"Remaining double-encoded sequences: {remaining}")