# Fix corrupted bullet points - remove specific corrupted byte sequences
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

# Remove the corrupted bytes: \xc3\xa2\xe2\x82\xac\xc2\xa2
# This appears after the bullet character
corrupted_bytes = b'\xc3\xa2\xe2\x82\xac\xc2\xa2'
content = content.replace(corrupted_bytes, b'')

# Also check for other common corruption patterns
# Double-encoded bullet: \xe2\x80\xa2 followed by corruption
# Just remove the corruption part

with open(r'D:\MyCivicVoice_Deploy\index.html', 'wb') as f:
    f.write(content)

print("Removed corrupted bytes")

# Verify
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()
marker = b'return <div key={i}'
pos = content.find(marker)
if pos > 0:
    segment = content[pos:pos+150]
    print("\nVerification:")
    print(segment)