import re

# Read the file
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the FR object closing
idx = content.find('aboutAttributionNote:')
if idx != -1:
    end_idx = content.find('};', idx)
    if end_idx != -1:
        # Get the text before the closing brace
        before_closing = content[:end_idx]
        after_closing = content[end_idx:]
        
        # New translations to add
        new_translations = ''',
  // Escalation Card translations
  escalationTitle: "Signaler directement \u00e0 votre ville",
  escalationSubtitle: "Pour les questions municipales, vous pouvez souvent obtenir des r\u00e9sultats plus rapidement en signalant directement \u00e0 votre ville.",
  escalationBeforeRep: "Avant de contacter votre repr\u00e9sentant",
  escalationReportOnline: "Signaler en ligne",
  escalationCall: "Appeler",
  escalationPhone: "T\u00e9l\u00e9phone",
  escalationWebsite: "Site web",
  escalationNoService: "Service 311 non disponible",
  escalationNoServiceDesc: "Votre municipalit\u00e9 n'a pas de service 311. Contactez directement votre conseiller municipal ou recherchez le portail de signalement de votre ville.",
  escalationRuralNote: "Conseil pour les r\u00e9gions rurales",
  escalationRuralDesc: "Les r\u00e9gions rurales n'ont souvent pas de service 311. Contactez votre conseiller municipal ou le bureau municipal directement."'''
        
        # Insert the new translations before the closing brace
        # First, remove trailing whitespace/newline from the last entry
        before_closing = before_closing.rstrip()
        # Remove trailing comma if present, then add comma and new translations
        if before_closing.endswith(','):
            before_closing = before_closing[:-1]
        
        new_content = before_closing + new_translations + '\n\n' + after_closing
        
        # Write back
        with open(r'D:\MyCivicVoice_Deploy\index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print('Successfully added escalation translations to FR object')
    else:
        print('Closing brace not found')
else:
    print('aboutAttributionNote not found')