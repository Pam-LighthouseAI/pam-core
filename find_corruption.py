# Find all corrupted byte sequences in the file
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

# Search for common corruption patterns
import re

# Find all instances of double-encoded UTF-8
# Pattern: \xc3\x83\xc2 followed by another byte (double-encoded)
pattern = b'\xc3\x83\xc2'
positions = []
pos = 0
while True:
    pos = content.find(pattern, pos)
    if pos == -1:
        break
    positions.append(pos)
    pos += 1

print(f"Found {len(positions)} double-encoded sequences at positions:")
for p in positions[:20]:  # Show first 20
    context = content[max(0,p-30):p+50]
    print(f"\nPosition {p}:")
    print(context)