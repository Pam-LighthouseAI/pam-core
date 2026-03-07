# Verify the Primary contact box was removed
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if "Primary contact" comment still exists
if 'Primary contact' in content:
    print("WARNING: 'Primary contact' still found in file")
    # Find location
    idx = content.find('{/* Primary contact')
    if idx > 0:
        print(f"Found at position {idx}")
        print(content[idx:idx+200])
else:
    print("CONFIRMED: 'Primary contact' section has been removed")

# Check that renderStep3 still exists
if 'renderStep3' in content:
    print("CONFIRMED: renderStep3 function still exists")
else:
    print("ERROR: renderStep3 function missing!")