# Fix double-encoded French text

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    content = f.read()

# Double-encoded sequences to fix
# é should be \xc3\xa9 but is \xc3\x83\xc2\xa9
# è should be \xc3\xa8 but is \xc3\x83\xc2\xa8
# à should be \xc3\xa0 but is \xc3\x83\xc2\xa0
# ô should be \xc3\xb4 but is \xc3\x83\xc2\xb4
# ç should be \xc3\xa7 but is \xc3\x83\xc2\xa7
# ê should be \xc3\xaa but is \xc3\x83\xc2\xaa
# ù should be \xc3\xb9 but is \xc3\x83\xc2\xb9
# î should be \xc3\xae but is \xc3\x83\xc2\xae

replacements = [
    (b'\xc3\x83\xc2\xa9', b'\xc3\xa9'),  # é
    (b'\xc3\x83\xc2\xa8', b'\xc3\xa8'),  # è
    (b'\xc3\x83\xc2\xa0', b'\xc3\xa0'),  # à
    (b'\xc3\x83\xc2\xb4', b'\xc3\xb4'),  # ô
    (b'\xc3\x83\xc2\xa7', b'\xc3\xa7'),  # ç
    (b'\xc3\x83\xc2\xaa', b'\xc3\xaa'),  # ê
    (b'\xc3\x83\xc2\xb9', b'\xc3\xb9'),  # ù
    (b'\xc3\x83\xc2\xae', b'\xc3\xae'),  # î
]

count = 0
for old, new in replacements:
    found = content.count(old)
    if found > 0:
        print(f"Found {found} occurrences of corrupted accent")
        content = content.replace(old, new)
        count += found

print(f"Fixed {count} total corrupted accents")

# Write back
with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'wb') as f:
    f.write(content)

print("File saved")