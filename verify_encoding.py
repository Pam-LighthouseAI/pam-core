# Verify the fixes worked
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

# Check specific areas
print("=== BUTTONS ===")
# Find Back button
idx = content.find(b'Back')
if idx > 0:
    print(content[idx:idx+100].decode('utf-8', errors='replace'))

print("\n=== FOOTER ===")
# Find OpenNorth
idx = content.find(b'OpenNorth')
if idx > 0:
    print(content[idx:idx+150].decode('utf-8', errors='replace'))

print("\n=== FRENCH LABELS ===")
# Find Étape
idx = content.find(b'tape 1')
if idx > 0:
    print(content[max(0,idx-5):idx+50].decode('utf-8', errors='replace'))

print("\n=== TRADEMARK ===")
# Find ©
idx = content.find(b'\xc2\xa9')
if idx > 0:
    print(content[idx:idx+50].decode('utf-8', errors='replace'))

print("\n=== DOUBLE-ENCODED CHECK ===")
remaining = content.count(b'\xc3\x83\xc2')
print(f"Remaining double-encoded sequences: {remaining}")