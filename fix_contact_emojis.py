# Add phone and email emojis to representative cards
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add phone emoji (📞) before Phone:
content = content.replace(
    "{getText('phone','Phone:')}",
    "\U0001F4DE {getText('phone','Phone:')}"
)

# Add email emoji (✉️) before Email:
content = content.replace(
    "{getText('email','Email:')}",
    "\u2709 {getText('email','Email:')}"
)

with open(r'D:\MyCivicVoice_Deploy\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added phone and email emojis to representative cards")