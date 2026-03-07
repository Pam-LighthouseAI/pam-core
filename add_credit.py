#!/usr/bin/env python3
"""Add LighthouseAI credit to footer."""

def add_credit(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add credit line after footerText paragraph, before closing </footer>
    # Find the footerText paragraph and add credit after it
    old_text = '''        <p style={{color:'#6B7280',fontSize:13}}>{getText('footerText','Built for Canadians who want to be heard.')}</p>
        <p style={{margin:'0 8px'}}>·</span>
          <a href="https://opennorth.ca/" target="_blank" rel="noopener noreferrer" style={{color:'#6B7280',textDecoration:'none'}}>OpenNorth.ca</a>
        </p>
      </footer>'''
    
    new_text = '''        <p style={{color:'#6B7280',fontSize:13}}>{getText('footerText','Built for Canadians who want to be heard.')}</p>
        <p style={{color:'#6B7280',fontSize:12,marginTop:8}}>
          Made by <a href="https://lighthouseai.ca" target="_blank" rel="noopener noreferrer" style={{color:'#9CA3AF',textDecoration:'none'}}>Pam & Daniel at LighthouseAI</a>
        </p>
        <p style={{margin:'0 8px'}}>·</span>
          <a href="https://opennorth.ca/" target="_blank" rel="noopener noreferrer" style={{color:'#6B7280',textDecoration:'none'}}>OpenNorth.ca</a>
        </p>
      </footer>'''
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Credit added!")
    else:
        # Try alternative - just find and replace the footer closing
        print("Pattern not found, trying alternative...")
        # Just add before </footer>
        old_footer = "      </footer>"
        new_footer = '''        <p style={{color:'#6B7280',fontSize:12,marginTop:8}}>
          Made by <a href="https://lighthouseai.ca" target="_blank" rel="noopener noreferrer" style={{color:'#9CA3AF',textDecoration:'none'}}>Pam & Daniel at LighthouseAI</a>
        </p>
      </footer>'''
        if old_footer in content:
            content = content.replace(old_footer, new_footer)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Credit added via alternative method!")
        else:
            print("Could not find footer pattern")

if __name__ == "__main__":
    add_credit(r"D:\source_extracted\my_civic_voice.html")