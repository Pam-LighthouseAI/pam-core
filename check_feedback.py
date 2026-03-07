# Check feedback form implementation
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find feedback-related code
keywords = ['feedback', 'mailto', 'pam.lighthouseai', 'FeedbackForm']
for kw in keywords:
    idx = 0
    while True:
        idx = content.find(kw, idx)
        if idx == -1:
            break
        start = max(0, idx - 30)
        end = min(len(content), idx + 150)
        print(f"Found '{kw}' at {idx}:")
        print(content[start:end])
        print("---")
        idx += 1