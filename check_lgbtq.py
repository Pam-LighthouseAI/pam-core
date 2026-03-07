# Fix the remaining LGBTQ+ flag

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    content = f.read()

# Show what's there
idx = content.find(b'\xc3\xb0\xc5\xb8\xc2\x8f\xc2\xb3')
if idx >= 0:
    print(f"Found at {idx}: {content[idx:idx+30]}")