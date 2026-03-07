# Fix all corrupted emojis in the file

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    content = f.read()

# Map of what the corrupted bytes should be replaced with
# These are category icons - I'll map them based on the label that follows

# Common corrupted emoji patterns and their correct forms
replacements = [
    # Infrastructure 🏗️
    (b'\xc3\xb0\xc5\xb8\xc5\xa1\xe2\x80\x94', '🏗️'.encode('utf-8')),
    # Health 🏥
    (b'\xc3\xb0\xc5\xb8\xc2\x8f\xc2\xa5', '🏥'.encode('utf-8')),
    # Education 🎓
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9c\xc5\xa1', '🎓'.encode('utf-8')),
    # Housing 🏠
    (b'\xc3\xb0\xc5\xb8\xc2\x8f\xc2\xa0', '🏠'.encode('utf-8')),
    # Environment 🌍
    (b'\xc3\xb0\xc5\xb8\xc5\x92\xc2\xbf', '🌍'.encode('utf-8')),
    # Employment 💼
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x99\xc2\xbc', '💼'.encode('utf-8')),
    # Social Services 🤝
    (b'\xc3\xb0\xc5\xb8\xc2\xa4\xc2\x9d', '🤝'.encode('utf-8')),
    # Taxes 💰
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x99\xc2\xb0', '💰'.encode('utf-8')),
    # Immigration ✈️
    (b'\xc3\xb0\xc5\xb8\xe2\x80\xba\xe2\x80\x99', '✈️'.encode('utf-8')),
    # Consumer Rights 🛡️
    (b'\xc3\xb0\xc5\xb8\xc2\xaa\xc2\xb6', '🛡️'.encode('utf-8')),
    # Sports 🏆
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x98\xc2\xb4', '🏆'.encode('utf-8')),
    # Safety 🚨
    (b'\xc3\xb0\xc5\xb8\xc5\xbd\xe2\x80\x93\xc3\xaf\xc2\xb8\xc2\x8f', '🚨'.encode('utf-8')),
    # Youth 👶
    (b'\xc3\xb0\xc5\xb8\xc5\xbd\xe2\x80\x9c', '👶'.encode('utf-8')),
    # Agriculture 🌾
    (b'\xc3\xb0\xc5\xb8\xc5\x92\xc2\xbe', '🌾'.encode('utf-8')),
    # Arts 🎨
    (b'\xc3\xb0\xc5\xb8\xc5\xbd\xc2\xa8', '🎨'.encode('utf-8')),
    # LGBTQ+ 🏳️‍🌈
    (b'\xc3\xb0\xc5\xb8\xc2\x8f\xc2\xb3\xc3\xaf\xc2\xb8\xc2\x8f\xc3\xa2\xe2\x82\xac\xc2\xad\xc3\xb0\xc5\xb8\xc5\x92\xc2\xbc', '🏳️‍🌈'.encode('utf-8')),
    # Women's Rights 👩
    (b'\xc3\xb0\xc5\xb8\xc5\x92\xcb\x86', '👩'.encode('utf-8')),
    # Mental Health 🧠
    (b'\xc3\xb0\xc5\xb8\xc2\xa7\xc2\xa0', '🧠'.encode('utf-8')),
    # Substance Use 💉
    (b'\xc3\xb0\xc5\xb8\xc2\xa7\xc2\xaa', '💉'.encode('utf-8')),
    # Transportation 🚗
    (b'\xc3\xb0\xc5\xb8\xc5\xa1\xc5\x92', '🚗'.encode('utf-8')),
    # Digital Rights 💻
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x99\xc2\xbb', '💻'.encode('utf-8')),
    # Animal Welfare 🐾
    (b'\xc3\xb0\xc5\xb8\xc2\x90\xc2\xbe', '🐾'.encode('utf-8')),
    # Volunteer 🤲
    (b'\xc3\xb0\xc5\xb8\xc2\xa4\xc2\xb2', '🤲'.encode('utf-8')),
    # Pensions 💵
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x99\xc2\xa1', '💵'.encode('utf-8')),
    # Childcare 👶
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9d\xc2\x8d', '👶'.encode('utf-8')),
    # Food Security 🍎
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9d\xe2\x80\x9e', '🍎'.encode('utf-8')),
    # Emergency 🚑
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9c\xc2\x8d', '🚑'.encode('utf-8')),
    # Human Rights ✊
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9c\xc5\xbe', '✊'.encode('utf-8')),
    # Legal ⚖️
    (b'\xc3\xb0\xc5\xb8\xe2\x80\x9d\xe2\x80\x94', '⚖️'.encode('utf-8')),
    # Utilities 💡
    (b'\xc3\xb0\xc5\xb8\xc5\xa1\xc2\xa8', '💡'.encode('utf-8')),
    # Family 👨‍👩‍👧
    (b'\xc3\xb0\xc5\xb8\xcb\x9c\xc5\xb8', '👨'.encode('utf-8')),
    # Broadband 📡
    (b'\xc3\xb0\xc5\xb8\xc5\x92\xc5\xb8', '📡'.encode('utf-8')),
    # Religion ⛪
    (b'\xc3\xb0\xc5\xb8\xcb\x9c\xc2\xa4', '⛪'.encode('utf-8')),
]

count = 0
for old, new in replacements:
    found = content.count(old)
    if found > 0:
        content = content.replace(old, new)
        count += found
        print(f"Fixed {found} occurrences")

# Also fix remaining double-encoded characters
double_encoded = [
    (b'\xc3\x83\xc2\xa2', b'\xc3\xa2'),  # â
    (b'\xc3\x83\xc2\xae', b'\xc3\xae'),  # î
    (b'\xc3\x83\xc2\xb4', b'\xc3\xb4'),  # ô
]

for old, new in double_encoded:
    found = content.count(old)
    if found > 0:
        content = content.replace(old, new)
        print(f"Fixed {found} double-encoded chars")

# Write back
with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'wb') as f:
    f.write(content)

print(f"\nTotal fixes: {count}")