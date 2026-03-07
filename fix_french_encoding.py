# Fix double-encoded French characters
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

# Fix the double-encoded French characters
# \xc3\x83\xc2\xa0 should be \xc3\xa0 (à)
# \xc3\x83\xc2\xa9 should be \xc3\xa9 (é)

content = content.replace(b'\xc3\x83\xc2\xa0', b'\xc3\xa0')  # à
content = content.replace(b'\xc3\x83\xc2\xa9', b'\xc3\xa9')  # é

with open(r'D:\MyCivicVoice_Deploy\index.html', 'wb') as f:
    f.write(content)

print("Fixed French encoding")

# Verify
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()
marker = b'Copiez la lettre'
pos = content.find(marker)
if pos > 0:
    segment = content[pos:pos+150]
    print("\nVerification:")
    print(segment.decode('utf-8'))