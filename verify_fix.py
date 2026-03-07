# Verify the fix by checking bytes
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

# Check the first bullet point
marker = b'return <div key={i}'
pos = content.find(marker)
if pos > 0:
    segment = content[pos:pos+150]
    print("First bullet area:")
    print(segment)
    print()

# Check the second bullet point
marker2 = b'Copiez la lettre'
pos2 = content.find(marker2)
if pos2 > 0:
    segment2 = content[pos2-50:pos2+150]
    print("Second bullet area:")
    print(segment2)
    print()
    
# Check for any remaining corrupted sequences
if b'\xc3\x83\xc2' in content:
    print("WARNING: Still have double-encoded characters")
else:
    print("No double-encoded characters found")

if b'\xc3\xa2\xe2\x82\xac\xc2' in content:
    print("WARNING: Still have corrupted emoji bytes")
else:
    print("No corrupted emoji bytes found")