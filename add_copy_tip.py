file_path = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the closing of the story prompts and add a final tip
old_text = '''return <div key={i} style={{marginBottom:i < prompts.length - 1 ? 6 : 0}}>• {prompt}</div>;
                })}
              </div>
            </div>
          )}'''

new_text = '''return <div key={i} style={{marginBottom:i < prompts.length - 1 ? 6 : 0}}>• {prompt}</div>;
                })}
                <div style={{marginTop:12,paddingTop:10,borderTop:'1px dashed rgba(242,140,56,0.3)',fontWeight:500,color:'#444'}}>• {isFrench ? 'Copiez la lettre, ajoutez votre nom et courriel, puis envoyez-la \u00e0 votre repr\u00e9sentant.' : 'Copy the letter to your email, add your name and email address, and send it to your representative.'}</div>
              </div>
            </div>
          )}'''

content = content.replace(old_text, new_text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Added copy tip')