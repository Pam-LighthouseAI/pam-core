file_path = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the signature - replace uEmail || emailPlaceholder with just emailPlaceholder
old_sig = "${uEmail || \nemailPlaceholder}"
new_sig = "${emailPlaceholder}"
content = content.replace(old_sig, new_sig)

# Also try without the newline
old_sig2 = "${uEmail || emailPlaceholder}"
content = content.replace(old_sig2, new_sig)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed email signature')