# Fix mental health emoji
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the incorrect escape with correct one
content = content.replace('id:"mentalhealth", icon:"\\\\uD83E\\\\uDDE0"', 'id:"mentalhealth", icon:"\\uD83E\\uDDE0"')

with open(r'D:\MyCivicVoice_Deploy\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed mental health emoji")