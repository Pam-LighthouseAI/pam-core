#!/usr/bin/env python3
filepath = r"D:\source_extracted\my_civic_voice.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_credit = """        <p style={{color:'#6B7280',fontSize:12,marginTop:8}}>
          {isFrench ? 'Crée par ' : 'Made by '}<a href="https://lighthouseai.ca" target="_blank" rel="noopener noreferrer" style={{color:'#9CA3AF',textDecoration:'none'}}>{isFrench ? 'Pam et Daniel' : 'Pam & Daniel'}</a>{isFrench ? ' chez ' : ' at '}<a href="https://lighthouseai.ca" target="_blank" rel="noopener noreferrer" style={{color:'#9CA3AF',textDecoration:'none'}}>LighthouseAI</a>
        </p>"""

new_credit = """        <p style={{color:'#6B7280',fontSize:12,marginTop:8}}>
          {isFrench ? 'Créé par Pam et Daniel chez LighthouseAI' : 'Made by Pam & Daniel at LighthouseAI'}
        </p>"""

if old_credit in content:
    content = content.replace(old_credit, new_credit)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Link removed - now plain text!")
else:
    print("Pattern not found")