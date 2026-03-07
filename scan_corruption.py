import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    content = f.read()

# Look for common emoji patterns that might be corrupted
# Corrupted emojis often have \xc3\xb0 or \xc3\x83 patterns
patterns = [
    (b'\xc3\xb0', 'Possible corrupted emoji (ð)'),
    (b'\xc3\x83\xc2', 'Double-encoded character'),
]

for pattern, desc in patterns:
    count = content.count(pattern)
    if count > 0:
        print(f"Found {count} occurrences of: {desc}")
        # Show context
        idx = content.find(pattern)
        print(f"  Context: {content[idx:idx+50]}")

# Check for any remaining courthouse icons
courthouse = '🏛️'.encode('utf-8')
count = content.count(courthouse)
print(f"\nCourthouse icons 🏛️: {count}")

# Check for maple leaf
maple = '🍁'.encode('utf-8')
count = content.count(maple)
print(f"Maple leaves 🍁: {count}")