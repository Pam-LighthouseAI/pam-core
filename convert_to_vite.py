#!/usr/bin/env python3
"""
Convert my_civic_voice.html to a Vite React project.
This script extracts the CSS and creates the necessary project structure.
"""

import os
import re

# Read the original file
with open(r"D:\source_extracted\my_civic_voice.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Extract CSS
css_match = re.search(r'<style>([\s\S]*?)</style>', content)
if css_match:
    css_content = css_match.group(1).strip()
    
    # Write CSS to index.css
    css_path = r"C:\nanobot\instance3\workspace\src\index.css"
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print(f"Created {css_path}")

# Create main.jsx entry point
main_jsx = '''import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
'''

main_path = r"C:\nanobot\instance3\workspace\src\main.jsx"
with open(main_path, 'w', encoding='utf-8') as f:
    f.write(main_jsx)
print(f"Created {main_path}")

# Create index.html for Vite
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Civic Voice Canada</title>
  <meta name="description" content="Find the right level of government and your actual representatives for any civic issue across Canada. Draft letters and connect with your elected officials.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@700;800;900&display=swap" rel="stylesheet">
</head>
<body>
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>
</html>
'''

html_path = r"C:\nanobot\instance3\workspace\index.html"
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(index_html)
print(f"Created {html_path}")

print("\nProject structure created!")
print("\nTo run the project:")
print("  cd C:\\nanobot\\instance3\\workspace")
print("  npm run dev")