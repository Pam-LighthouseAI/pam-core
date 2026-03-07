# Final verification
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

print("=== BUTTONS ===")
# Find all button texts
import re
buttons = re.findall(b"getText\('back'[^)]+\)", content)
for b in buttons[:5]:
    print(f"  {b.decode('utf-8', errors='replace')}")

print("\n=== FRENCH TEXT SAMPLES ===")
# Check key French phrases
samples = [
    (b'\xc3\x89tape', 'Étape'),
    (b'O\xc3\xb9 habitez', 'Où habitez'),
    (b'Con\xc3\xa7u pour', 'Conçu pour'),
    (b'entendus', 'entendus'),
    (b'r\xc3\xa9serv\xc3\xa9s', 'réservés'),
    (b'\xe2\x80\x94', '— (em dash)'),
]

for pattern, name in samples:
    idx = content.find(pattern)
    if idx > 0:
        context = content[max(0,idx-5):idx+20].decode('utf-8', errors='replace')
        print(f"  {name}: OK - {context}")
    else:
        print(f"  {name}: NOT FOUND")

print("\n=== OPENNORTH ATTRIBUTION ===")
idx = content.find(b'OpenNorth')
if idx > 0:
    print(content[idx:idx+100].decode('utf-8', errors='replace'))

print("\n=== COPYRIGHT ===")
idx = content.find(b'\xc2\xa9 2026')
if idx > 0:
    print(content[idx-5:idx+50].decode('utf-8', errors='replace'))

print("\n=== ENCODING CHECK ===")
print(f"File size: {len(content)} bytes")
print(f"Double-encoded (\\xc3\\x83): {content.count(b'\\xc3\\x83')}")
print(f"Corrupted (\\xc3\\xa2\\xe2): {content.count(b'\\xc3\\xa2\\xe2')}")