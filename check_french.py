with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    content = f.read()

# Find 'isFrench ?' which should be near the French text
idx = content.find(b'isFrench ?')
if idx >= 0:
    print(f"Found 'isFrench ?' at byte {idx}")
    # Show a chunk
    print(content[idx:idx+300])