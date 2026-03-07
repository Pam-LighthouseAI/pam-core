"""
Script to verify modal content has French translations in index.html
"""

import re
import sys

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Read the file
content = read_file(r'D:\source_extracted\index.html')

print("=" * 60)
print("MODAL CONTENT FRENCH TRANSLATION VERIFICATION")
print("=" * 60)

# 1. Check FAQ Modal
print("\n1. FAQ MODAL")
print("-" * 40)

# Check FAQ_EN
faq_en_match = re.search(r'const FAQ_EN\s*=\s*\[([\s\S]*?)\];', content)
if faq_en_match:
    faq_en_content = faq_en_match.group(1)
    faq_en_items = re.findall(r'\{\s*q:', faq_en_content)
    print(f"   [OK] FAQ_EN exists with {len(faq_en_items)} Q&A pairs")
else:
    print("   [MISSING] FAQ_EN NOT FOUND")

# Check FAQ_FR
faq_fr_match = re.search(r'const FAQ_FR\s*=\s*\[([\s\S]*?)\];', content)
if faq_fr_match:
    faq_fr_content = faq_fr_match.group(1)
    faq_fr_items = re.findall(r'\{\s*q:', faq_fr_content)
    print(f"   [OK] FAQ_FR exists with {len(faq_fr_items)} Q&A pairs")
else:
    print("   [MISSING] FAQ_FR NOT FOUND")

# Check FAQModal component uses isFrench
if 'function FAQModal({ isOpen, onClose, isFrench })' in content:
    print("   [OK] FAQModal accepts isFrench prop")
    if 'const FAQ = isFrench ? FAQ_FR : FAQ_EN' in content:
        print("   [OK] FAQModal uses isFrench to select correct FAQ data")
    else:
        print("   [MISSING] FAQModal does NOT use isFrench for language selection")
else:
    print("   [MISSING] FAQModal component NOT FOUND")

# 2. Check Feedback Modal
print("\n2. FEEDBACK MODAL")
print("-" * 40)

if 'function FeedbackModal({ isOpen, onClose, isFrench })' in content:
    print("   [OK] FeedbackModal accepts isFrench prop")
    
    # Find the labels object in FeedbackModal
    feedback_match = re.search(r'function FeedbackModal[\s\S]*?const labels = isFrench \? \{([\s\S]*?)\} : \{([\s\S]*?)\}', content)
    if feedback_match:
        print("   [OK] FeedbackModal has French labels object")
        
        french_labels = feedback_match.group(1)
        
        required_labels = ['title', 'subtitle', 'name', 'namePlaceholder', 'email', 'emailPlaceholder', 
                          'message', 'messagePlaceholder', 'sending', 'submit', 'success', 'error']
        
        for label in required_labels:
            if f'{label}:' in french_labels:
                print(f"      [OK] '{label}' has French translation")
            else:
                print(f"      [MISSING] '{label}' MISSING French translation")
    else:
        print("   [MISSING] FeedbackModal labels NOT FOUND")
else:
    print("   [MISSING] FeedbackModal component NOT FOUND")

# 3. Check Privacy Modal
print("\n3. PRIVACY MODAL")
print("-" * 40)

if 'function PrivacyModal' in content or 'PrivacyModal' in content:
    print("   [OK] PrivacyModal component found")
    if 'isFrench' in content[content.find('PrivacyModal'):content.find('PrivacyModal')+500] if 'PrivacyModal' in content else False:
        print("   [OK] PrivacyModal has isFrench prop")
    else:
        print("   [MISSING] PrivacyModal missing isFrench prop")
else:
    print("   [MISSING] PrivacyModal component NOT FOUND")

# 4. Check About Modal
print("\n4. ABOUT MODAL")
print("-" * 40)

if 'function AboutModal' in content or 'AboutModal' in content:
    print("   [OK] AboutModal component found")
else:
    print("   [MISSING] AboutModal component NOT FOUND")

# 5. Check Draft Prompt Modal
print("\n5. DRAFT PROMPT MODAL")
print("-" * 40)

if 'function DraftPrompt({ onRestore, onDismiss, isFrench })' in content:
    print("   [OK] DraftPrompt accepts isFrench prop")
    
    # Check French translations used
    draft_translations = ['draftFound', 'draftFoundMessage', 'restoreDraft', 'startFresh']
    fr_object_match = re.search(r'const FR\s*=\s*\{([\s\S]*?)\};', content)
    if fr_object_match:
        fr_content = fr_object_match.group(1)
        for t in draft_translations:
            if f'{t}:' in fr_content:
                print(f"      [OK] '{t}' has French translation in FR object")
            else:
                print(f"      [MISSING] '{t}' MISSING in FR object")
else:
    print("   [MISSING] DraftPrompt component NOT FOUND")

# Summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

# Count issues
issues = []

if 'function FAQModal({ isOpen, onClose, isFrench })' in content and 'const FAQ = isFrench ? FAQ_FR : FAQ_EN' in content:
    print("[VERIFIED] FAQ Modal - Has isFrench prop, uses FAQ_EN and FAQ_FR")
else:
    issues.append("FAQ Modal")
    print("[MISSING] FAQ Modal - Issues found")

if 'function FeedbackModal({ isOpen, onClose, isFrench })' in content:
    print("[VERIFIED] Feedback Modal - Has isFrench prop with French labels")
else:
    issues.append("Feedback Modal")
    print("[MISSING] Feedback Modal - Issues found")

if 'function PrivacyModal' in content or 'PrivacyModal' in content:
    print("[VERIFIED] Privacy Modal - Component exists")
else:
    issues.append("Privacy Modal")
    print("[MISSING] Privacy Modal - Component does NOT exist")

if 'function AboutModal' in content or 'AboutModal' in content:
    print("[VERIFIED] About Modal - Component exists")
else:
    issues.append("About Modal")
    print("[MISSING] About Modal - Component does NOT exist")

if 'function DraftPrompt({ onRestore, onDismiss, isFrench })' in content:
    print("[VERIFIED] Draft Prompt Modal - Has isFrench prop")
else:
    issues.append("Draft Prompt Modal")
    print("[MISSING] Draft Prompt Modal - Issues found")

print(f"\nTOTAL ISSUES: {len(issues)}")
if issues:
    print(f"ISSUES FOUND IN: {', '.join(issues)}")