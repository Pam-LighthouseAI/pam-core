# Fix corrupted UTF-8 sequences in the file

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    content = f.read()

# The corrupted courthouse emoji bytes
corrupted_courthouse = b'\xc3\xb0\xc5\xb8\xc2\x8f\xe2\x80\xba\xc3\xaf\xc2\xb8\xc2\x8f'
# Replace with proper UTF-8 for 🏛️
courthouse_emoji = '🏛️'.encode('utf-8')

print(f"Corrupted bytes: {corrupted_courthouse}")
print(f"Correct bytes: {courthouse_emoji}")

# Count occurrences
count = content.count(corrupted_courthouse)
print(f"Found {count} occurrences of corrupted courthouse")

# Replace
content = content.replace(corrupted_courthouse, courthouse_emoji)
print(f"Replaced with courthouse emoji")

# Write back
with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'wb') as f:
    f.write(content)

print("File saved")

# Verify
with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    new_content = f.read()
    idx = new_content.find(b'className="why-visual"')
    if idx >= 0:
        print(f"\nVerification - bytes after fix:")
        print(new_content[idx:idx+400])