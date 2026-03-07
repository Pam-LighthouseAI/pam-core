import re

# Read the file
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# First, let's fix the corrupted icons from the previous run
# Remove any corrupted icon values (they'll look like icon:"???" or similar garbage)
content = re.sub(r', icon:"[^"]{1,10}",', ', icon:"",', content)

# How It Works emojis are already done correctly with surrogate pairs
# They should be: {"\uD83D\uDCDA"} for 📚, etc.

# For category icons, we need to use the actual Unicode escape sequences
# that will be interpreted by JavaScript in the browser

# The icon field is a JavaScript string, so we can use \uXXXX format
# But we need to write them as literal backslash-u sequences in the file

# Emoji to Unicode escape mapping (for JavaScript strings)
# Format: \uD83D\uDCDA for surrogate pairs, or \uXXXX for BMP characters

category_emoji_escapes = {
    'infrastructure': '\\uD83D\\uDE97',  # 🚗
    'healthcare': '\\uD83C\\uDFE5',  # 🏥
    'education': '\\uD83D\\uDCDA',  # 📚
    'housing': '\\uD83C\\uDFE0',  # 🏠
    'environment': '\\uD83C\\uDF33',  # 🌳
    'safety': '\\uD83D\\uDEA8',  # 🚨
    'employment': '\\uD83D\\uDCBC',  # 💼
    'social': '\\uD83E\\uDD1D',  # 🤝
    'taxes': '\\uD83D\\uDCB0',  # 💰
    'immigration': '\\u2708\\uFE0F',  # ✈️
    'consumer': '\\u2696\\uFE0F',  # ⚖️
    'indigenous': '\\uD83E\\uDD36',  # 🪶 (feather)
    'seniors': '\\uD83E\\uDDD3',  # 👴
    'veterans': '\\uD83C\\uDF96\\uFE0F',  # 🎖️
    'disability': '\\u267F',  # ♿
    'youth': '\\uD83D\\uDC66',  # 👦
    'agriculture': '\\uD83C\\uDF3E',  # 🌾
    'utilities': '\\uD83D\\uDCA1',  # 💡
    'family': '\\uD83D\\uDC68\\u200D\\uD83D\\uDC69\\u200D\\uD83D\\uDC67',  # 👨‍👩‍👧
    'arts': '\\uD83C\\uDFA8',  # 🎨
    'tenant': '\\uD83C\\uDFE1',  # 🏡
    'electoral': '\\uD83D\\uDFF3\\uFE0F',  # 🗳️ (ballot)
    'broadband': '\\uD83D\\uDCE1',  # 📡
    'fisheries': '\\uD83D\\uDC20',  # 🐠
    'languages': '\\uD83D\\uDDE3\\uFE0F',  # 🗣️
    'international': '\\uD83C\\uDF0D',  # 🌍
    'lgbtq': '\\uD83C\\uDFC3\\uFE0F\\u200D\\uD83C\\uDF08',  # 🏳️‍🌈
    'women': '\\uD83D\\uDC69',  # 👩
    'mental': '\\uD83E\\uDDE0',  # 🧠
    'substance': '\\uD83D\\uDEAB',  # 🚫
    'transportation': '\\uD83D\\uDE8C',  # 🚌
    'digital': '\\uD83D\\uDCBB',  # 💻
    'animals': '\\uD83D\\uDC15',  # 🐕
    'sports': '\\u26BD',  # ⚽
    'religion': '\\u26EA',  # ⛪
    'volunteer': '\\uD83E\\uDD1D',  # 🤝
    'legal': '\\u2696\\uFE0F',  # ⚖️
    'pensions': '\\uD83D\\uDCB5',  # 💵
    'childcare': '\\uD83D\\uDC76',  # 👶
    'food': '\\uD83C\\uDF4E',  # 🍎
    'emergency': '\\uD83D\\uDE92',  # 🚒
    'humanrights': '\\u270A',  # ✊
    'traffic': '\\uD83D\\uDED1',  # 🛑
}

# Update category icons
for cat_id, escape_seq in category_emoji_escapes.items():
    # The pattern is: { id:"category", icon:"",
    pattern = f'{{ id:"{cat_id}", icon:""'
    # We write the escape sequence literally (backslash-u) so JavaScript interprets it
    replacement = f'{{ id:"{cat_id}", icon:"{escape_seq}"'
    content = content.replace(pattern, replacement)

# Write back
with open(r'D:\MyCivicVoice_Deploy\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Categories updated with Unicode escapes.")