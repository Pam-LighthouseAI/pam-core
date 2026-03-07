#!/usr/bin/env python3
"""Fix French translation issues identified by Kevin."""

import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Remove duplicate keys in FR object
    # Remove the second occurrence of primary: "Principal", secondary: "Secondaire" (lines ~224-225)
    content = re.sub(
        r'(\n  primary: "Principal",\n  secondary: "Secondaire",)(.*?)(\n  primary: "Principal",\n  secondary: "Secondaire",)',
        r'\1\2',
        content,
        flags=re.DOTALL
    )
    
    # Remove the second occurrence of toneUrgent, toneConcerned, toneHopeful, toneFrustrated (lines ~265-268)
    content = re.sub(
        r'(\n  toneUrgent: "Urgent",\n  toneConcerned: "Préoccupé",\n  toneHopeful: "Espoir",\n  toneFrustrated: "Frustré",)(.*?)(\n  toneUrgent: "Urgent",\n  toneConcerned: "Préoccupé",\n  toneHopeful: "Espoir",\n  toneFrustrated: "Frustré",)',
        r'\1\2',
        content,
        flags=re.DOTALL
    )
    
    # 2. Fix accent issues
    # "donnee" → "données" and fix "a but non lucratif" → "à but non lucratif" and "accessibles a tous" → "accessibles à tous"
    content = content.replace(
        'Open North est un organisme a but non lucratif canadien qui rend les donnees gouvernementales accessibles a tous.',
        'Open North est un organisme à but non lucratif canadien qui rend les données gouvernementales accessibles à tous.'
    )
    
    # "Confidentialite" → "Confidentialité"
    content = content.replace('privacyTitle: "Confidentialite"', 'privacyTitle: "Confidentialité"')
    
    # "privee" → "privée" - check for instances
    content = content.replace('votre vie privee est notre priorite', 'votre vie privée est notre priorité')
    content = content.replace('Aucune donnee', 'Aucune donnée')
    content = content.replace('donnees stockees', 'données stockées')
    content = content.replace('sur nos serveurs', 'sur nos serveurs')  # already correct
    
    # "Telephone" → "Téléphone" - check for instances without accent
    content = content.replace('phone: "Telephone:"', 'phone: "Téléphone:"')
    
    # "A propos" → "À propos" - check for instances
    content = content.replace('aboutTitle: "A propos"', 'aboutTitle: "À propos"')
    
    # Fix "Représentants fédéraux" - check if first é is missing
    # Already has accent in federalRepresentatives: "Représentants fédéraux"
    # But check for any instances without the accent
    content = content.replace('Representants federaux', 'Représentants fédéraux')
    content = content.replace('Representants fédéraux', 'Représentants fédéraux')
    
    # Additional accent fixes from previous scan
    content = content.replace('nameFr:"Denigement"', 'nameFr:"Dénéigement"')
    content = content.replace('nameFr:"Eclairage des rues"', 'nameFr:"Éclairage des rues"')
    content = content.replace('nameFr:"Application des regles de stationnement"', 'nameFr:"Application des règles de stationnement"')
    content = content.replace('nameFr:"Acces a un medecin de famille"', 'nameFr:"Accès à un médecin de famille"')
    content = content.replace('nameFr:"Services d\'ambulance"', 'nameFr:"Services d\'ambulance"')  # already has accent
    
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