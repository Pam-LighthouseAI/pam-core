# Fix corrupted button characters
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

# The corrupted sequence \xc3\xa2\xe2\x80\xa0\xc2\x90 should be ← (\xe2\x86\x90)
# Or we can just use a simple dash or remove it

# Count how many instances
corrupted = b'\xc3\xa2\xe2\x80\xa0\xc2\x90'
count = content.count(corrupted)
print(f"Found {count} instances of corrupted button character")

# Replace with ← (left arrow)
content = content.replace(corrupted, b'\xe2\x86\x90')

with open(r'D:\MyCivicVoice_Deploy\index.html', 'wb') as f:
    f.write(content)

print("Fixed button characters")

# Verify
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    verify = f.read()

# Check buttons
idx = verify.find(b'Back')
if idx > 0:
    print(f"\nButton text now: {verify[max(0,idx-10):idx+20]}")

# Check for remaining corruption
remaining_corruption = verify.count(b'\xc3\xa2\xe2\x80\xa0')
print(f"\nRemaining corruption: {remaining_corruption}")