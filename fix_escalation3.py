# Read the file
with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the exact text to replace
old_text = '''          {selIssue && selIssue.primary === 'municipal' && reps.municipal && reps.municipal.length > 0 && (
            <EscalationCard 
              repSetName={reps.municipal[0]?.representativeSetName} 
              issueId={selIssue?.name?.toLowerCase()}
              isFrench={isFrench} 
            />
          )}'''

new_text = '''          {selIssue && selIssue.primary === 'municipal' && reps.municipal && reps.municipal.length > 0 && (
            <EscalationCard 
              repSetName={reps.municipal[0]?.representativeSetName} 
              cityName={city}
              issueId={selIssue?.name?.toLowerCase()}
              isFrench={isFrench} 
            />
          )}
          {selIssue && selIssue.primary === 'municipal' && (!reps.municipal || reps.municipal.length === 0) && city && (
            <EscalationCard 
              repSetName={null}
              cityName={city}
              issueId={selIssue?.name?.toLowerCase()}
              isFrench={isFrench} 
            />
          )}'''

if old_text in content:
    content = content.replace(old_text, new_text)
    print("Found and replaced EscalationCard usage")
    
    # Write back
    with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully saved changes")
else:
    print("Could not find exact text. Trying with different whitespace...")
    
    # Try with different line endings
    import re
    
    # Pattern with flexible whitespace
    pattern = r'\{selIssue && selIssue\.primary === \'municipal\' && reps\.municipal && reps\.municipal\.length > 0 && \(\s*<EscalationCard\s+repSetName=\{reps\.municipal\[0\]\?\.representativeSetName\}\s+issueId=\{selIssue\?\.name\?\.toLowerCase\(\)\}\s+isFrench=\{isFrench\}\s*/>\s*\)\}'
    
    if re.search(pattern, content):
        content = re.sub(pattern, new_text, content)
        print("Found and replaced using regex pattern")
        
        with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully saved changes")
    else:
        print("Could not find pattern with regex either")
        # Print the surrounding area
        idx = content.find('<EscalationCard')
        if idx != -1:
            print(f"Found EscalationCard at position {idx}")
            print("Context (500 chars):")
            print(content[max(0, idx-200):idx+300])