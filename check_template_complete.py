import re

with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find TEMPLATES object
templates_match = re.search(r'const TEMPLATES = \{([\s\S]*?)\n\};', content)
if templates_match:
    templates_content = templates_match.group(1)
    
    # Split into individual template entries
    # Each template looks like: infrastructure: { subject: "...", body: "...", subjectFr: "...", bodyFr: "..." },
    template_entries = re.split(r',\s*\n\s*(?=\w+:\s*\{)', templates_content)
    
    print(f"Found {len(template_entries)} template entries\n")
    
    for entry in template_entries:
        # Get the template ID
        id_match = re.match(r'(\w+):\s*\{', entry)
        if id_match:
            tid = id_match.group(1)
            has_subject = 'subject:' in entry
            has_body = 'body:' in entry
            has_subjectFr = 'subjectFr:' in entry
            has_bodyFr = 'bodyFr:' in entry
            
            if not (has_subject and has_body):
                print(f"INCOMPLETE: {tid}")
                print(f"  subject: {has_subject}, body: {has_body}, subjectFr: {has_subjectFr}, bodyFr: {has_bodyFr}")
            
            # Check for empty body
            body_match = re.search(r'body:\s*`([^`]*)`', entry)
            if body_match and len(body_match.group(1).strip()) < 50:
                print(f"SHORT BODY: {tid} - {len(body_match.group(1))} chars")