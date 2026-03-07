# Fix the remaining LGBTQ+ and other emojis

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    content = f.read()

# The corrupted sequence includes the flag plus the ZWJ sequence
# 🏳️‍🌈 = 🏳️ + ZWJ + 🌈
# The corrupted bytes are for the whole thing

# LGBTQ+ flag (full corrupted sequence)
old = b'\xc3\xb0\xc5\xb8\xc2\x8f\xc2\xb3\xc3\xaf\xc2\xb8\xc2\x8f\xc3\xa2\xe2\x82\xac\xc2\x8d\xf0\x9f\x91\xa9'
new = '🏳️‍🌈'.encode('utf-8')

found = content.count(old)
if found > 0:
    content = content.replace(old, new)
    print(f"Fixed {found} LGBTQ+ flag")

# Write back
with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'wb') as f:
    f.write(content)

print("Done")