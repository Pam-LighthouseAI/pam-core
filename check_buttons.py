# Check specific areas after fix
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

print("=== BUTTONS (Back) ===")
# Find Back button
idx = content.find(b'Back')
if idx > 0:
    # Find all Back occurrences
    count = 0
    pos = 0
    while count < 5:
        pos = content.find(b'Back', pos)
        if pos == -1:
            break
        context = content[max(0,pos-30):pos+50]
        print(f"{count+1}. {context}")
        print()
        pos += 1
        count += 1

print("\n=== FRENCH À (should be À) ===")
idx = content.find(b'\xc3\x80')
if idx > 0:
    print(f"Found À at position {idx}")
    print(content[idx:idx+30])
else:
    print("No À found - checking for corrupted version")
    idx = content.find(b' propos')
    if idx > 0:
        print(content[max(0,idx-10):idx+30])

print("\n=== EM DASH ===")
idx = content.find(b'\xe2\x80\x94')
if idx > 0:
    print(f"Found em dash at position {idx}")
    print(content[max(0,idx-10):idx+30])
else:
    print("No em dash found")