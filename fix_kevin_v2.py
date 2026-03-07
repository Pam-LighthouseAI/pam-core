#!/usr/bin/env python3
"""Fix French translation issues identified by Kevin - Version 2."""

import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Remove duplicate keys in FR object - primary and secondary (lines ~224-225)
    # Find and remove the second occurrence after the tone definitions
    content = re.sub(
        r'(\n  federal: "Fédéral",\n  provincial: "Provincial",\n  municipal: "Municipal",\n  contactYour: "Contacter votre",\n  tosTitle: "Conditions d\'utilisation",)(\n  primary: "Principal",\n  secondary: "Secondaire",)',
        r'\1',
        content
    )
    
    # 2. Remove duplicate toneUrgent, toneConcerned, toneHopeful, toneFrustrated (lines ~265-268)
    content = re.sub(
        r'(\n  toneUrgent: "Urgent",\n  toneConcerned: "Préoccupé",\n  toneHopeful: "Espoir",\n  toneFrustrated: "Frustré",\n\n  draftYourLetter:)(\n  toneUrgent: "Urgent",\n  toneConcerned: "Préoccupé",\n  toneHopeful: "Espoir",\n  toneFrustrated: "Frustré",)',
        r'\1',
        content
    )
    
    # 3. Fix accent issues
    # "Confidentialite" → "Confidentialité"
    content = content.replace('privacyTitle: "Confidentialite"', 'privacyTitle: "Confidentialité"')
    
    # "donnee" → "données" and fix "a but non lucratif" → "à but non lucratif"
    content = content.replace(
        'Open North est un organisme a but non lucratif canadien qui rend les donnees gouvernementales accessibles a tous.',
        'Open North est un organisme à but non lucratif canadien qui rend les données gouvernementales accessibles à tous.'
    )
    
    # Write back if changes were made
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Changes made!")
        return True
    else:
        print("No changes needed.")
        return False

if __name__ == "__main__":
    filepath = r"D:\source_extracted\my_civic_voice.html"
    fix_file(filepath)