# Verify the file is now correct by decoding samples
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

print("=== FRENCH LABELS ===")
idx = content.find(b'step1Label')
if idx > 0:
    sample = content[idx:idx+200].decode('utf-8')
    print(sample)

print("\n=== FOOTER ===")
idx = content.find(b'footerText')
if idx > 0:
    sample = content[idx:idx+200].decode('utf-8')
    print(sample)

print("\n=== OPENNORTH ATTRIBUTION ===")
idx = content.find(b'OpenNorth')
if idx > 0:
    sample = content[idx:idx+200].decode('utf-8')
    print(sample)

print("\n=== COPYRIGHT ===")
idx = content.find(b'footerCopyright')
if idx > 0:
    sample = content[idx:idx+150].decode('utf-8')
    print(sample)

print("\n=== BUTTONS ===")
idx = content.find(b'Back to all categories')
if idx > 0:
    sample = content[max(0,idx-20):idx+100].decode('utf-8')
    print(sample)