# Fix all remaining corruptions
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

print("Fixing corruptions...\n")

# 1. Corrupted arrows and buttons
# \xc3\xa2\xe2\x80\xa0\xe2\x80\x99 should be -> (right arrow)
count = content.count(b'\xc3\xa2\xe2\x80\xa0\xe2\x80\x99')
print(f"Fixing {count} corrupted right arrow")
content = content.replace(b'\xc3\xa2\xe2\x80\xa0\xe2\x80\x99', b'\xe2\x86\x92')

# \xc3\xa2\xe2\x80\xa0 should be <- (left arrow)
count = content.count(b'\xc3\xa2\xe2\x80\xa0')
print(f"Fixing {count} corrupted left arrow")
content = content.replace(b'\xc3\xa2\xe2\x80\xa0', b'\xe2\x86\x90')

# 2. Corrupted em dash
# \xc3\xa2\xe2\x82\xac\xe2\x80\x9d should be em dash
count = content.count(b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d')
print(f"Fixing {count} corrupted em dash")
content = content.replace(b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d', b'\xe2\x80\x94')

# 3. Corrupted quotes
count = content.count(b'\xc3\xa2\xe2\x80\x9c')
if count > 0:
    print(f"Fixing {count} corrupted left quote")
    content = content.replace(b'\xc3\xa2\xe2\x80\x9c', b'\xe2\x80\x9c')

count = content.count(b'\xc3\xa2\xe2\x80\x9d')
if count > 0:
    print(f"Fixing {count} corrupted right quote")
    content = content.replace(b'\xc3\xa2\xe2\x80\x9d', b'\xe2\x80\x9d')

# 4. Corrupted apostrophe
count = content.count(b'\xc3\xa2\xe2\x80\x99')
if count > 0:
    print(f"Fixing {count} corrupted apostrophe")
    content = content.replace(b'\xc3\xa2\xe2\x80\x99', b'\xe2\x80\x99')

# 5. Corrupted ellipsis
count = content.count(b'\xc3\xa2\xe2\x80\xa6')
if count > 0:
    print(f"Fixing {count} corrupted ellipsis")
    content = content.replace(b'\xc3\xa2\xe2\x80\xa6', b'\xe2\x80\xa6')

# Write back
with open(r'D:\MyCivicVoice_Deploy\index.html', 'wb') as f:
    f.write(content)

print("\nDone! Verifying...")

# Verify
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    verify = f.read()

# Check for remaining issues
print(f"\nRemaining double-encoded: {verify.count(b'\\xc3\\x83')}")
print(f"Remaining corrupted sequences: {verify.count(b'\\xc3\\xa2\\xe2\\x80') + verify.count(b'\\xc3\\xa2\\xe2\\x82')}")