import re

# Read the file
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# How It Works emojis - use JSX string expressions for Babel compatibility
# Surrogate pairs: 📚 = \uD83D\uDCDA, 🤝 = \uD83E\uDD1D, ✅ = \u2705

# Find and replace the how-card-icon divs
# The pattern is: <div className="how-card-icon"></div>
# We want to add: <span style={{fontSize:28}}>{"\uD83D\uDCDA"}</span>

how_card_replacements = [
    # Learn card - comes first
    ('<div className="how-card-icon"></div>\n                  <h3>{isFrench ? \'Apprendre\' : \'Learn\'}</h3>',
     '<div className="how-card-icon"><span style={{fontSize:28}}>{"\\uD83D\\uDCDA"}</span></div>\n                  <h3>{isFrench ? \'Apprendre\' : \'Learn\'}</h3>'),
    # Engage card - comes second
    ('<div className="how-card-icon"></div>\n                  <h3>{isFrench ? \'S\\\'engager\' : \'Engage\'}</h3>',
     '<div className="how-card-icon"><span style={{fontSize:28}}>{"\\uD83E\\uDD1D"}</span></div>\n                  <h3>{isFrench ? \'S\\\'engager\' : \'Engage\'}</h3>'),
    # Act card - comes third
    ('<div className="how-card-icon"></div>\n                  <h3>{isFrench ? \'Agir\' : \'Act\'}</h3>',
     '<div className="how-card-icon"><span style={{fontSize:28}}>{"\\u2705"}</span></div>\n                  <h3>{isFrench ? \'Agir\' : \'Act\'}</h3>'),
]

for old, new in how_card_replacements:
    content = content.replace(old, new)

# Category emojis - these are in string fields, so direct emoji should work
# But let's use the same surrogate pair format to be safe
category_emojis = {
    'infrastructure': '\\uD83D\\uDE97',  # 🚗
    'healthcare': '\\uD83D\\uDC3E5',  # 🏥 - wrong, let me recalculate
}

# Let me calculate correct surrogate pairs
# 🏥 = U+1F3E5 = \uD83C\uDFE5
# 🚗 = U+1F697 = \uD83D\uDE97
# 📚 = U+1F4DA = \uD83D\uDCDA
# 🏠 = U+1F3E0 = \uD83C\uDFE0
# 🌳 = U+1F333 = \uD83C\uDF33
# 🚨 = U+1F6A8 = \uD83D\uDEA8
# 💼 = U+1F4BC = \uD83D\uDCBC
# 🤝 = U+1F91D = \uD83E\uDD1D
# 💰 = U+1F4B0 = \uD83D\uDCB0
# ✈️ = U+2708 U+FE0F = \u2708\uFE0F
# ⚖️ = U+2696 U+FE0F = \u2696\uFE0F
# 🪶 = U+1FAB6 = \uD83E\uDD36... wait let me check

# Actually for simplicity, let me just use the emoji characters directly in the string field
# The icon field is just a JavaScript string, not JSX, so it should work

category_emoji_chars = {
    'infrastructure': '🚗',
    'healthcare': '🏥',
    'education': '📚',
    'housing': '🏠',
    'environment': '🌳',
    'safety': '🚨',
    'employment': '💼',
    'social': '🤝',
    'taxes': '💰',
    'immigration': '✈️',
    'consumer': '⚖️',
    'indigenous': '🪶',
    'seniors': '👴',
    'veterans': '🎖️',
    'disability': '♿',
    'youth': '👦',
    'agriculture': '🌾',
    'utilities': '💡',
    'family': '👨‍👩‍👧',
    'arts': '🎨',
    'tenant': '🏡',
    'electoral': '🗳️',
    'broadband': '📡',
    'fisheries': '🐠',
    'languages': '🗣️',
    'international': '🌍',
    'lgbtq': '🏳️‍🌈',
    'women': '👩',
    'mental': '🧠',
    'substance': '🚫',
    'transportation': '🚌',
    'digital': '💻',
    'animals': '🐕',
    'sports': '⚽',
    'religion': '⛪',
    'volunteer': '🤝',
    'legal': '⚖️',
    'pensions': '💵',
    'childcare': '👶',
    'food': '🍎',
    'emergency': '🚒',
    'humanrights': '✊',
    'traffic': '🛑',
}

# Update category icons
for cat_id, emoji in category_emoji_chars.items():
    pattern = f'{{ id:"{cat_id}", icon:""'
    replacement = f'{{ id:"{cat_id}", icon:"{emoji}"'
    content = content.replace(pattern, replacement)

# Write back
with open(r'D:\MyCivicVoice_Deploy\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! How It Works cards and categories updated.")