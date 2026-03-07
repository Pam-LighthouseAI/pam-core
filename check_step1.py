# Find Step 1 / lookup type selector
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find renderStep1
idx = content.find('renderStep1')
if idx > 0:
    section = content[idx:idx+5000]
    with open(r'C:\nanobot\instance3\workspace\step1_output.txt', 'w', encoding='utf-8') as f:
        f.write(section)
    print("Step 1 written to step1_output.txt")