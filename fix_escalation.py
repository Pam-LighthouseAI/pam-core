import re

# Read the file
with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the EscalationCard usage
old_pattern = r'''(\{selIssue && selIssue\.primary === 'municipal' && reps\.municipal && reps\.municipal\.length > 0 && \(\s*<EscalationCard\s*repSetName=\{reps\.municipal\[0\]\?\.representativeSetName\}\s*issueId=\{selIssue\?\.name\?\.toLowerCase\(\)\}\s*isFrench=\{isFrench\}\s*/>\s*\)\})'''

new_text = '''{selIssue && selIssue.primary === 'municipal' && reps.municipal && reps.municipal.length > 0 && (
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

# Try to find and replace
match = re.search(r'\{selIssue && selIssue\.primary === \'municipal\' && reps\.municipal && reps\.municipal\.length > 0 && \(\s*<EscalationCard', content)
if match:
    # Find the end of this block
    start = match.start()
    # Find the closing )} after </EscalationCard>
    end_match = re.search(r'</EscalationCard>\s*\)\}', content[start:])
    if end_match:
        end = start + end_match.end()
        content = content[:start] + new_text + content[end:]
        print(f"Replaced EscalationCard usage from position {start} to {end}")
    else:
        print("Could not find end of EscalationCard block")
else:
    print("Could not find EscalationCard usage pattern")

# Write back
with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")