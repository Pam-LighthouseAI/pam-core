file_path = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'prompts.length - 1' in line:
        print(f"Line {i}:")
        for j in range(5):
            print(f"  {i+j}: {lines[i+j].rstrip()}")