import re

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f'Total lines: {len(lines)}')

# Check line 2729
if len(lines) > 2728:
    print(f'Line 2729: {repr(lines[2728][:150])}')

# Find all emojis
emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\U0001F900-\U0001F9FF"  # supplemental
    "]+", flags=re.UNICODE)

count = 0
for i, line in enumerate(lines, 1):
    matches = emoji_pattern.findall(line)
    if matches:
        count += 1
        print(f'Line {i}: {matches}')

print(f'\nTotal lines with emojis: {count}')
