with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the empty span tag
content = content.replace(
    "        <span style={{fontSize:20}}></span>\n        <span style={{fontWeight:600,color:'#EA580C',fontSize:16}}>",
    "        <span style={{fontWeight:600,color:'#EA580C',fontSize:16}}>"
)

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed!")
