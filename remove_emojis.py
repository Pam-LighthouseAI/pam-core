import re

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Emoji pattern
emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\U0001F900-\U0001F9FF"  # supplemental
    "\U00002600-\U000026FF"  # misc symbols
    "\U00002700-\U000027BF"  # dingbats
    "]+", flags=re.UNICODE)

# Find all matches
matches = emoji_pattern.findall(content)
print(f'Found {len(matches)} emoji sequences')

# Remove emojis
cleaned = emoji_pattern.sub('', content)

# Also remove BOM if present
if cleaned.startswith('\ufeff'):
    cleaned = cleaned[1:]
    print('Removed BOM')

# Write back
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(cleaned)

print('Done! Emojis removed.')
