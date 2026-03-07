# Fix corrupted bullet points - remove corrupted emoji bytes
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the corrupted patterns and fix them
# Pattern 1: The bullet point line in the tips section
# The corrupted bytes appear as " ? " or similar

# Find the exact line and fix it
import re

# Fix the first bullet (in the map function)
# Pattern: }}> followed by corrupted bytes then space then {prompt}
# We want to replace with: }}>• {prompt}

# Find and fix the corrupted bullet in the return statement
old_pattern = r'>\s*\?\s*\{prompt\}'
content = re.sub(r'>\s*\?\s*\{prompt\}', '>• {prompt}', content)

# Also fix the second bullet (the copy tip line)
# Find lines with corrupted bullets before text
content = re.sub(r"'#444'}}>\s*\?\s*", "'#444'}}>• ", content)

with open(r'D:\MyCivicVoice_Deploy\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed corrupted bullets")

# Verify
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()
idx = content.find('return <div key={i}')
print("\nVerification:")
print(content[idx:idx+150])