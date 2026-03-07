# Fix remaining û characters

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    content = f.read()

# û should be \xc3\xbb but is \xc3\x83\xc2\xbb
old = b'\xc3\x83\xc2\xbb'
new = b'\xc3\xbb'

found = content.count(old)
if found > 0:
    content = content.replace(old, new)
    print(f"Fixed {found} occurrences of û")

# Write back
with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'wb') as f:
    f.write(content)

print("Done")