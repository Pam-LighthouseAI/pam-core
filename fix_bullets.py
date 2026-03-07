# Fix corrupted bullet points in Tips section
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and display the corrupted section
import re

# Find the tips section
idx = content.find("Tips for a powerful")
if idx > 0:
    segment = content[idx:idx+800]
    print("Found section:")
    print(segment[:500])
    
# Look for the pattern with corrupted bytes
# The bullet should be a simple dash or bullet character
# Pattern: }}> followed by corrupted emoji bytes then space

# Replace the corrupted bullets with simple dash
# Look for the return statement with the bullet
pattern = r'return <div key=\{i\} style=\{\{marginBottom:i < prompts\.length - 1 \? 6 : 0\}\}>[^<]*\{prompt\}'

# Find matches
matches = re.findall(pattern, content)
print(f"\nFound {len(matches)} matches")

# Simple replacement - find the corrupted area and fix
# The corrupted bytes are likely UTF-8 sequences for emoji that got mangled

# Just replace the specific corrupted patterns we can see
content = content.replace(
    "return <div key={i} style={{marginBottom:i < prompts.length - 1 ? 6 : 0}}>",
    "return <div key={i} style={{marginBottom:i < prompts.length - 1 ? 6 : 0}}>• "
)

# Fix the second bullet point line
content = content.replace(
    "<div style={{marginTop:12,paddingTop:10,borderTop:'1px dashed rgba(242,140,56,0.3)',fontWeight:500,color:'#444'}}>",
    "<div style={{marginTop:12,paddingTop:10,borderTop:'1px dashed rgba(242,140,56,0.3)',fontWeight:500,color:'#444'}}>• "
)

with open(r'D:\MyCivicVoice_Deploy\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nFixed corrupted bullet points with • character")