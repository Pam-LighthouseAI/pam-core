# Find Step 3 sections in index.html
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find renderStep3 function
idx = content.find('renderStep3')
if idx > 0:
    # Get a chunk of it
    section = content[idx:idx+10000]
    with open(r'C:\nanobot\instance3\workspace\step3_output.txt', 'w', encoding='utf-8') as f:
        f.write(section)
    print("Written to step3_output.txt")