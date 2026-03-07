import re

file_path = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the email input field in Step 3
# Find and remove the input line for email
content = re.sub(r'\s*<input type="email" placeholder={getText\(\'yourEmail\',\'Your email\'\)} value={uEmail} onChange={e=>setUEmail\(e\.target\.value\)} />', '', content)

# 2. Remove uEmail state declaration
content = re.sub(r"\s*const \[uEmail, setUEmail\] = React\.useState\(''\);", '', content)

# 3. Update signature to not use uEmail - just use placeholder
# Find the signature line and update it
old_signature = "const signature = `${namePlaceholder}\n${postalCode || city || province || locationPlaceholder}\n${uEmail || emailPlaceholder}`;"
new_signature = "const signature = `${namePlaceholder}\n${postalCode || city || province || locationPlaceholder}\n${emailPlaceholder}`;"
content = content.replace(old_signature, new_signature)

# 4. Remove the email input in the contact form section (if exists)
content = re.sub(r'\s*<input type="email" value={form\.email} onChange={e => setForm\(\{\.+?\}\)} placeholder={labels\.emailPlaceholder} />', '', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Removed email input field')