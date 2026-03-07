# Find all remaining corrupted sequences
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

print("=== LOOKING FOR CORRUPTION PATTERNS ===\n")

# Common corruption patterns in double-encoded UTF-8
patterns = [
    (b'\xc3\xa2\xe2\x80\xa0', 'â†'),  # corrupted arrow
    (b'\xc3\xa2\xe2\x82\xac', 'â€'),  # corrupted euro-related
    (b'\xc3\xa2\xe2\x80\x9c', 'â€'),  # corrupted quote
    (b'\xc3\xa2\xe2\x80\x9d', 'â€'),  # corrupted quote
    (b'\xc3\xa2\xe2\x80\x99', 'â€™'),  # corrupted apostrophe
    (b'\xc3\xa2\xe2\x80\x98', 'â€˜'),  # corrupted single quote
    (b'\xc3\xa2\xe2\x80\x93', 'â€“'),  # corrupted en dash
    (b'\xc3\xa2\xe2\x80\xa6', 'â€¦'),  # corrupted ellipsis
]

for pattern, name in patterns:
    count = content.count(pattern)
    if count > 0:
        print(f"Found {count} instances of {name}")
        # Find first occurrence
        idx = content.find(pattern)
        context = content[max(0,idx-20):idx+30]
        print(f"  Context: {context}\n")

# Also look for any remaining \xc3\x83 (double-encoded prefix)
remaining_83 = content.count(b'\xc3\x83')
print(f"\nRemaining \\xc3\\x83 sequences: {remaining_83}")

# Look for \xc3\xa2 followed by anything unusual
print("\n=== CHECKING FOR â CORRUPTIONS ===")
pos = 0
count = 0
while count < 20:
    pos = content.find(b'\xc3\xa2', pos)
    if pos == -1:
        break
    # Check what follows
    next_bytes = content[pos:pos+6]
    if next_bytes not in [b'\xc3\xa2\xe2\x80\x99', b'\xc3\xa2\xe2\x80\x98']:  # Skip valid â
        print(f"Position {pos}: {next_bytes}")
    pos += 1
    count += 1