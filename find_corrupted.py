with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    content = f.read()

# Fix remaining corrupted emojis
# The pattern \xc3\xb0\xc5\xb8 is corrupted UTF-8 for emoji start
# Let's find what emojis are corrupted

# Find all instances of \xc3\xb0\xc5\xb8
pattern = b'\xc3\xb0\xc5\xb8'
idx = 0
while True:
    idx = content.find(pattern, idx)
    if idx == -1:
        break
    # Show context
    print(f"Found at {idx}: {content[idx:idx+20]}")
    idx += 1