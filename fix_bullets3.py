# Fix corrupted bullet points - remove corrupted emoji bytes by finding and replacing the specific pattern
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

# Find the corrupted bytes pattern
# Looking for the sequence before " {prompt}" in the return statement
# The corrupted emoji bytes are likely 3-4 bytes that got mangled

# Find the position of "return <div key={i}"
marker = b'return <div key={i}'
pos = content.find(marker)
if pos > 0:
    # Show bytes around this area
    segment = content[pos:pos+200]
    print("Bytes around corrupted area:")
    print(segment)
    print("\nHex:")
    print(segment.hex()[:300])