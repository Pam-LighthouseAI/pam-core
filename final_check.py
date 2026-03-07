# Check for any remaining corruption

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    content = f.read()

# Look for double-encoded pattern \xc3\x83\xc2
pattern = b'\xc3\x83\xc2'
count = content.count(pattern)
print(f"Remaining double-encoded: {count}")

if count > 0:
    idx = 0
    while True:
        idx = content.find(pattern, idx)
        if idx == -1:
            break
        print(f"  At {idx}: {content[idx:idx+30]}")
        idx += 1