# Find remaining double-encoded sequences
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

# Find all \xc3\x83 sequences
pos = 0
count = 0
while True:
    pos = content.find(b'\xc3\x83', pos)
    if pos == -1:
        break
    context = content[pos:pos+20]
    print(f"Position {pos}: {context}")
    count += 1
    pos += 1
    if count > 30:
        break

print(f"\nTotal found: {count}")