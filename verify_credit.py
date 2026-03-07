#!/usr/bin/env python3
filepath = r"D:\source_extracted\my_civic_voice.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Check for French credit
if "Crée par" in content:
    print("SUCCESS: French credit 'Crée par' found")
elif "Cr" in content and "par" in content and "isFrench" in content:
    # Find the exact line
    for line in content.split('\n'):
        if 'isFrench' in line and 'par' in line:
            print(f"Found: {line.strip()[:100]}")
else:
    print("ERROR: French credit not found")
    
# Check for English credit  
if "Made by" in content:
    print("SUCCESS: English credit 'Made by' found")
else:
    print("ERROR: English credit not found")