# Final verification - bytes only
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

print("=== CHECKING KEY PATTERNS ===")

# Check for proper French characters
checks = [
    (b'\xc3\x89tape', 'Étape (E acute)'),
    (b'O\xc3\xb9 habitez', 'Où'),
    (b'Con\xc3\xa7u', 'Conçu (c cedilla)'),
    (b'r\xc3\xa9serv\xc3\xa9s', 'réservés'),
    (b'\xc2\xa9 2026', 'Copyright symbol'),
    (b'\xe2\x86\x90', 'Left arrow'),
    (b'\xe2\x86\x92', 'Right arrow'),
    (b'\xe2\x80\x94', 'Em dash'),
]

for pattern, name in checks:
    count = content.count(pattern)
    status = "OK" if count > 0 else "MISSING"
    print(f"  {name}: {status} ({count} found)")

print("\n=== CHECKING FOR CORRUPTION ===")
corruptions = [
    (b'\xc3\x83', 'Double-encoded'),
    (b'\xc3\xa2\xe2\x80', 'Corrupted quote/arrow'),
    (b'\xc3\xa2\xe2\x82', 'Corrupted em dash'),
]

for pattern, name in corruptions:
    count = content.count(pattern)
    status = "CLEAN" if count == 0 else f"FOUND {count}"
    print(f"  {name}: {status}")

print("\n=== BUTTON CONTEXT ===")
# Find Back button context
idx = content.find(b'Back')
if idx > 0:
    context = content[max(0,idx-15):idx+30]
    print(f"Bytes: {context}")
    print(f"Hex: {context.hex()}")

print("\n=== FRENCH LABEL CONTEXT ===")
idx = content.find(b'step1Label')
if idx > 0:
    context = content[idx:idx+60]
    print(f"Bytes: {context}")