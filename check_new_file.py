#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

filepath = r'C:\nanobot\instance3\workspace\my Civic voice version 3\MyCivicVoicev3.html'

# Read file
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Read as bytes for encoding check
with open(filepath, 'rb') as f:
    content_bytes = f.read()

print("=" * 60)
print("FILE ANALYSIS REPORT")
print("=" * 60)

# 1. FILE SIZE
file_size = os.path.getsize(filepath)
print(f"\n[FILE SIZE] {file_size:,} bytes ({file_size/1024:.1f} KB)")
if file_size > 500000:
    print("   WARNING: File is large. Netlify may have issues with files > 500KB")

# 2. ENCODING CHECK
print(f"\n[ENCODING CHECK]")
has_bom = content_bytes.startswith(b'\xef\xbb\xbf')
print(f"   UTF-8 BOM: {'Present' if has_bom else 'Not present'}")
charset_declared = 'charset="UTF-8"' in content or "charset='UTF-8'" in content
print(f"   Charset declared: {'Yes' if charset_declared else 'No'}")

# 3. FRENCH CHARACTER CHECK
print(f"\n[FRENCH CHARACTER CHECK]")
french_chars = ['É', 'é', 'è', 'ê', 'ë', 'î', 'ô', 'û', 'à', 'ç', 'ù', 'â']
for char in french_chars:
    count = content.count(char)
    status = "OK" if count > 0 else "MISSING"
    print(f"   '{char}': {count} occurrences [{status}]")

# Check for corrupted patterns
corrupted_patterns = [
    ('\xc3\xa9', 'e acute (double-encoded)'),
    ('\xc3\xa8', 'e grave (double-encoded)'),
    ('\xc3\xa0', 'a grave (double-encoded)'),
    ('\xc3\xa7', 'c cedilla (double-encoded)'),
    ('\xc3\xb9', 'u grave (double-encoded)'),
    ('\xc3\xbb', 'u circumflex (double-encoded)'),
    ('\xc3\xb4', 'o circumflex (double-encoded)'),
    ('\xc3\xae', 'i circumflex (double-encoded)'),
    ('\xc3\xab', 'e umlaut (double-encoded)'),
    ('\xc3\x89', 'E acute (double-encoded)'),
]

print(f"\n[CORRUPTION CHECK]")
corruptions_found = []
for pattern, name in corrupted_patterns:
    if pattern.encode('latin-1') in content_bytes:
        count = content_bytes.count(pattern.encode('latin-1'))
        corruptions_found.append((pattern, name, count))
        print(f"   CORRUPTED: {name} found {count} times")

if not corruptions_found:
    print("   No corrupted characters found!")

# 4. CODE SYNTAX CHECK
print(f"\n[CODE SYNTAX CHECK]")

# Check for unclosed tags
open_scripts = content.count('<script')
close_scripts = content.count('</script>')
print(f"   Script tags: {open_scripts} open, {close_scripts} close {'OK' if open_scripts == close_scripts else 'MISMATCH'}")

open_styles = content.count('<style')
close_styles = content.count('</style>')
print(f"   Style tags: {open_styles} open, {close_styles} close {'OK' if open_styles == close_styles else 'MISMATCH'}")

open_divs = content.count('<div')
close_divs = content.count('</div>')
print(f"   Div tags: {open_divs} open, {close_divs} close {'OK' if open_divs == close_divs else 'MISMATCH'}")

# Check for common syntax errors
print(f"\n[SYNTAX ERROR CHECK]")

# Check for unmatched braces in JS
js_start = content.find('<script type="text/babel">')
js_end = content.find('</script>', js_start) + 9 if js_start > -1 else 0
js_section = content[js_start:js_end] if js_start > -1 else ''

if js_section:
    open_braces = js_section.count('{')
    close_braces = js_section.count('}')
    print(f"   JS Braces: {open_braces} open, {close_braces} close {'OK' if open_braces == close_braces else 'MISMATCH'}")
    
    open_parens = js_section.count('(')
    close_parens = js_section.count(')')
    print(f"   JS Parens: {open_parens} open, {close_parens} close {'OK' if open_parens == close_parens else 'MISMATCH'}")

# 5. TRANSLATION COMPLETENESS CHECK
print(f"\n[TRANSLATION CHECK]")

# Check FR object exists and has key translations
if 'const FR = {' in content:
    print("   FR object found")
    required_keys = ['siteTitle', 'step1Label', 'step2Label', 'step3Label', 'postalCode', 'getStarted']
    for key in required_keys:
        if f'{key}:' in content or f'{key} :' in content:
            print(f"   '{key}' translation exists")
        else:
            print(f"   '{key}' translation MISSING")
else:
    print("   FR object NOT FOUND")

# Check for untranslated text in French sections
print(f"\n[TRANSLATION STATISTICS]")
en_count = content.count('Step 1 of 3')
fr_count = content.count('Étape 1 sur 3')
print(f"   'Step 1' (EN): {en_count} occurrences")
print(f"   'Étape 1' (FR): {fr_count} occurrences")

# 6. NETLIFY COMPATIBILITY
print(f"\n[NETLIFY COMPATIBILITY]")

# Check for common Netlify issues
issues = []

if 'babel-standalone' in content:
    print("   Uses Babel standalone (slower, but works)")
    
if 'node_modules' in content:
    issues.append("References node_modules (won't work on Netlify)")

if issues:
    for issue in issues:
        print(f"   ISSUE: {issue}")
else:
    print("   No obvious Netlify issues")

# 7. SPECIFIC CHECKS FROM USER
print(f"\n[KEY FRENCH PHRASES]")
key_phrases = [
    ('Étape 1 sur 3', 'Step 1 label'),
    ('Où habitez-vous', 'Where do you live'),
    ('Quel est votre enjeu', 'What is your issue'),
    ('Voici qui peut vous aider', 'Here is who can help'),
    ('Commencer', 'Get Started'),
    ('Trouver mes représentants', 'Find representatives'),
]

for phrase, description in key_phrases:
    if phrase in content:
        print(f"   '{description}': '{phrase}' found")
    else:
        print(f"   '{description}': '{phrase}' NOT FOUND")

# SUMMARY
print(f"\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

errors = []
warnings = []

if corruptions_found:
    errors.append(f"{len(corruptions_found)} corrupted character patterns found")

if js_section and open_braces != close_braces:
    errors.append("Unmatched braces in JavaScript")

if js_section and open_parens != close_parens:
    errors.append("Unmatched parentheses in JavaScript")

if file_size > 500000:
    warnings.append("Large file size may cause Netlify issues")

if not has_bom:
    warnings.append("Missing UTF-8 BOM (may cause encoding issues)")

if errors:
    print(f"\nERRORS ({len(errors)}):")
    for e in errors:
        print(f"   - {e}")

if warnings:
    print(f"\nWARNINGS ({len(warnings)}):")
    for w in warnings:
        print(f"   - {w}")

if not errors and not warnings:
    print("\nNo errors or warnings found!")
else:
    print(f"\nStatus: {'NEEDS FIXING' if errors else 'WORKABLE WITH WARNINGS'}")