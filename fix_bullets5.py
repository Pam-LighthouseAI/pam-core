# Fix second corrupted bullet point
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

# Find the second bullet area
marker = b'Copiez la lettre'
pos = content.find(marker)
if pos > 0:
    segment = content[pos-100:pos+200]
    print("Bytes around second corrupted area:")
    print(segment)
    print("\nHex:")
    print(segment.hex()[:400])