#!/usr/bin/env python3
"""Add better error recovery to My Civic Voice"""

filepath = r"D:\source_extracted\my_civic_voice.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add error state after loading state
old_loading_state = """const [loading, setLoading] = React.useState(false);"""
new_loading_state = """const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState('');"""

content = content.replace(old_loading_state, new_loading_state)

# Add error translations to FR object (after toneFrustrated)
old_tone = """  toneFrustrated: "Frustré","""
new_tone = """  toneFrustrated: "Frustré",
  errorFetching: "Erreur lors de la récupération des représentants",
  errorTryAgain: "Veuillez réessayer ou utiliser les liens alternatifs ci-dessous.",
  errorPostalCode: "Code postal non trouvé",
  errorSuggestions: "Essayez un code postal voisin ou utilisez les liens de recherche officiels ci-dessous.",
  loadingReps: "Chargement de vos représentants...","""

content = content.replace(old_tone, new_tone)

# Add English error translations after toneFrustrated in the EN object
old_en_tone = """const EN = {
  tosTitle: "Terms of Service","""
new_en_tone = """const EN = {
  errorFetching: "Error fetching representatives",
  errorTryAgain: "Please try again or use the alternative links below.",
  errorPostalCode: "Postal code not found",
  errorSuggestions: "Try a nearby postal code or use the official search links below.",
  loadingReps: "Loading your representatives...",
  tosTitle: "Terms of Service","""

content = content.replace(old_en_tone, new_en_tone)

# Update the fetch error handling to show error state
old_fetch_catch = """.catch(() => setLoading(false));"""
new_fetch_catch = """.catch((err) => {
          console.error('API error:', err);
          setError('postal_code_not_found');
          setLoading(false);
        });"""

content = content.replace(old_fetch_catch, new_fetch_catch)

# Save the file
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Error recovery added!")