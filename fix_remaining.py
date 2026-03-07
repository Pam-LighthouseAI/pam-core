# Fix remaining double-encoded sequences
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

# Fix the remaining patterns:
# \xc3\x83\xe2\x82\xac = À (should be \xc3\x80)
# \xc3\x83\xe2\x80\xa6\xc3\xa2\xe2\x82\xac\xc5\x93 = œ (should be \xc5\x93) - but this is more complex
# \xc3\x83\xe2\x80\x94 = — (em dash, should be \xe2\x80\x94)

# À (capital A grave)
content = content.replace(b'\xc3\x83\xe2\x82\xac', b'\xc3\x80')

# — (em dash)
content = content.replace(b'\xc3\x83\xe2\x80\x94', b'\xe2\x80\x94')

# œ (oe ligature) - the corrupted sequence is \xc3\x83\xe2\x80\xa6\xc3\xa2\xe2\x82\xac\xc5\x93
# This should just be \xc5\x93 (œ)
# Let me check what the full context is
# "œuvre" should be "\xc5\x93uvre"
content = content.replace(b'\xc3\x83\xe2\x80\xa6\xc3\xa2\xe2\x82\xac\xc5\x93', b'\xc5\x93')

with open(r'D:\MyCivicVoice_Deploy\index.html', 'wb') as f:
    f.write(content)

print("Fixed remaining double-encoded sequences")

# Verify
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    verify = f.read()

remaining = verify.count(b'\xc3\x83')
print(f"Remaining \\xc3\\x83 sequences: {remaining}")

# Check specific fixes
print(f"À characters: {verify.count(b'\\xc3\\x80')}")
print(f"Em dashes: {verify.count(b'\\xe2\\x80\\x94')}")
print(f"œ ligatures: {verify.count(b'\\xc5\\x93')}")