with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoice-1.html', 'rb') as f:
    content = f.read()
    idx = content.find(b'className="why-visual"')
    if idx >= 0:
        print(content[idx:idx+400])