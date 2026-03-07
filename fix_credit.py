#!/usr/bin/env python3
"""Add French translation to LighthouseAI credit."""

filepath = r"D:\source_extracted\my_civic_voice.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the credit line
old_credit = '''        <p style={{color:'#6B7280',fontSize:12,marginTop:8}}>
          Made by <a href="https://lighthouseai.ca" target="_blank" rel="noopener noreferrer" style={{color:'#9CA3AF',textDecoration:'none'}}>Pam & Daniel at LighthouseAI</a>
        </p>'''

new_credit = '''        <p style={{color:'#6B7280',fontSize:12,marginTop:8}}>
          {isFrench ? 'Crée par ' : 'Made by '}<a href="https://lighthouseai.ca" target="_blank" rel="noopener noreferrer" style={{color:'#9CA3AF',textDecoration:'none'}}>{isFrench ? 'Pam et Daniel' : 'Pam & Daniel'}</a>{isFrench ? ' chez ' : ' at '}<a href="https://lighthouseai.ca" target="_blank" rel="noopener noreferrer" style={{color:'#9CA3AF',textDecoration:'none'}}>LighthouseAI</a>
        </p>'''

if old_credit in content:
    content = content.replace(old_credit, new_credit)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("French translation added!")
else:
    print("Pattern not found, searching for credit...")
    # Show what's there
    for i, line in enumerate(content.split('\n')):
        if 'LighthouseAI' in line or 'Made by' in line:
            print(f"Line {i}: {line.strip()}")