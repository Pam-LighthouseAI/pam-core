# Check actual bytes to verify encoding is correct
with open(r'D:\MyCivicVoice_Deploy\index.html', 'rb') as f:
    content = f.read()

print("=== CHECKING É (Étape) ===")
idx = content.find(b'tape 1')
if idx > 0:
    bytes_before = content[idx-3:idx+20]
    print(f"Bytes: {bytes_before}")
    print(f"Expected É: \\xc3\\x89")
    print(f"Actual: {bytes_before[:2].hex()}")

print("\n=== CHECKING ç (Conçu) ===")
idx = content.find(b'Con')
if idx > 0:
    bytes_after = content[idx:idx+15]
    print(f"Bytes: {bytes_after}")
    # ç should be \xc3\xa7
    
print("\n=== CHECKING © (Copyright) ===")
idx = content.find(b'2026')
if idx > 0:
    bytes_before = content[idx-5:idx+10]
    print(f"Bytes: {bytes_before}")
    # © should be \xc2\xa9

print("\n=== CHECKING é (réservés) ===")
idx = content.find(b'rvi')
if idx > 0:
    bytes_before = content[idx-3:idx+10]
    print(f"Bytes: {bytes_before}")
    # é should be \xc3\xa9

print("\n=== OVERALL ENCODING CHECK ===")
# Check for any remaining double-encoded sequences
double_encoded_count = content.count(b'\xc3\x83')
print(f"Remaining \\xc3\\x83 sequences: {double_encoded_count}")

# Check for proper UTF-8 French characters
e_acute_count = content.count(b'\xc3\xa9')  # é
e_grave_count = content.count(b'\xc3\xa8')  # è
c_cedilla_count = content.count(b'\xc3\xa7')  # ç
print(f"é characters: {e_acute_count}")
print(f"è characters: {e_grave_count}")
print(f"ç characters: {c_cedilla_count}")