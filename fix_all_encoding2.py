# Fix all double-encoded UTF-8 characters - READ AFTER WRITE
import codecs

# Read the file
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

print(f"File size: {len(content)} bytes")
print(f"Double-encoded sequences found: {content.count(b'\\xc3\\x83\\xc2')}")

# Double-encoded UTF-8 fix
# These are the byte sequences that got double-encoded
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
    (b'\xc3\x82\xc2\xa9', b'\xc2\xa9'),  # ©
]

for old, new in replacements:
    before_count = content.count(old)
    content = content.replace(old, new)
    if before_count > 0:
        print(f"Replaced {before_count} instances of {old} -> {new}")

# Special case for É (Étape) - this one is tricky
# \xc3\x83\xe2\x80\xb0 should be \xc3\x89
content = content.replace(b'\xc3\x83\xe2\x80\xb0', b'\xc3\x89')

# Write back
with open(r'D:\MyCivicVoice_Deploy\index.html', 'wb') as f:
    f.write(content)

print("\nFile written successfully")

# Verify by reading again
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    verify = f.read()

print(f"\nVerification:")
print(f"Remaining double-encoded: {verify.count(b'\\xc3\\x83\\xc2')}")

# Show sample of French text
idx = verify.find(b'tape 1')
if idx > 0:
    print(f"\nFrench label sample: {verify[max(0,idx-5):idx+50]}")