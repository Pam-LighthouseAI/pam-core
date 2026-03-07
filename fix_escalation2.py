# Read the file
with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line with EscalationCard usage
found_line = None
for i, line in enumerate(lines):
    if '<EscalationCard' in line and 'repSetName={reps.municipal[0]' in line:
        found_line = i
        print(f"Found EscalationCard at line {i}: {line.strip()}")
        break

if found_line:
    # Find the start of the block (should be 1-2 lines before)
    start = found_line - 1
    while start > 0 and '{selIssue' not in lines[start]:
        start -= 1
    
    # Find the end of the block (should be 1-2 lines after)
    end = found_line + 1
    while end < len(lines) and ')}' not in lines[end]:
        end += 1
    end += 1  # Include the closing line
    
    print(f"Block from line {start} to {end}")
    print("Old content:")
    for i in range(start, end):
        print(f"  {i}: {lines[i].rstrip()}")
    
    # New content
    new_lines = [
        "          {selIssue && selIssue.primary === 'municipal' && reps.municipal && reps.municipal.length > 0 && (\n",
        "            <EscalationCard \n",
        "              repSetName={reps.municipal[0]?.representativeSetName} \n",
        "              cityName={city}\n",
        "              issueId={selIssue?.name?.toLowerCase()}\n",
        "              isFrench={isFrench} \n",
        "            />\n",
        "          )}\n",
        "          {selIssue && selIssue.primary === 'municipal' && (!reps.municipal || reps.municipal.length === 0) && city && (\n",
        "            <EscalationCard \n",
        "              repSetName={null}\n",
        "              cityName={city}\n",
        "              issueId={selIssue?.name?.toLowerCase()}\n",
        "              isFrench={isFrench} \n",
        "            />\n",
        "          )}\n",
    ]
    
    # Replace the block
    lines = lines[:start] + new_lines + lines[end:]
    
    # Write back
    with open(r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("Successfully updated EscalationCard usage")
else:
    print("Could not find EscalationCard usage")