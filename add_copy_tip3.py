file_path = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Insert after line 4120 (the closing })}
# We want to add a new div after the prompts but before the closing </div>

new_line = '''                <div style={{marginTop:12,paddingTop:10,borderTop:'1px dashed rgba(242,140,56,0.3)',fontWeight:500,color:'#444'}}>• {isFrench ? 'Copiez la lettre, ajoutez votre nom et courriel, puis envoyez-la \u00e0 votre repr\u00e9sentant.' : 'Copy the letter to your email, add your name and email address, and send it to your representative.'}</div>
'''

# Insert after line 4120
lines.insert(4121, new_line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Added copy tip after line 4120')