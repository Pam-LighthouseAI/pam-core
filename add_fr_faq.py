#!/usr/bin/env python3
"""Add French translations and FAQ to the index.html"""

# Read the file
with open(r'D:\source_extracted\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# French translations (compact version for insertion)
fr_code = '''
// French translations for My Civic Voice
const FR = {
  siteTitle: "Ma Voix Civique",
  siteSubtitle: "Canada",
  tagline: "Trouvez le bon niveau de gouvernement, vos représentants actuels, et envoyez-leur une lettre prête à l'emploi.",
  getStarted: "Commencer",
  step1Title: "Où habitez-vous?",
  step1Subtitle: "Entrez votre emplacement pour trouver vos représentants",
  step2Title: "Quel est votre enjeu?",
  step2Subtitle: "Sélectionnez la catégorie qui correspond à votre situation",
  step3Title: "Voici qui peut vous aider",
  resultsLabel: "Résultats",
  postalCode: "Code postal",
  city: "Ville",
  province: "Province",
  best: "MEILLEUR",
  detected: "Détecté :",
  noPostalWarning: "Sans code postal, les représentants spécifiques ne seront pas affichés.",
  searchPlaceholder: "Rechercher des enjeux (p. ex. nids-de-poule...)",
  allCategories: "Toutes les catégories",
  issues: "enjeux",
  primary: "Principal",
  alsoInvolved: "Aussi concerné",
  noIssuesFound: "Aucun enjeu trouvé.",
  generalGuidance: "Conseils généraux",
  enterLocationPrompt: "Entrez un code postal ou sélectionnez une ville pour voir vos représentants.",
  draftYourMessage: "Rédigez votre message",
  toLabel: "À :",
  yourFullName: "Votre nom complet",
  yourLocation: "Votre lieu de résidence",
  yourEmail: "Votre courriel",
  yourPhone: "Votre téléphone",
  yourExperience: "Votre expérience personnelle",
  experiencePlaceholder: "Décrivez comment cet enjeu vous touche personnellement...",
  preview: "Aperçu",
  subject: "Objet",
  copyToClipboard: "Copier dans le presse-papiers",
  copied: "Copié!",
  openInEmailApp: "Ouvrir dans l'application de courriel",
  tip: "Conseil : Personnalisez les sections surlignées pour un impact maximal.",
  differentIssue: "Autre enjeu",
  startOver: "Recommencer",
  back: "Retour",
  allCategoriesBtn: "← Toutes les catégories",
  loadingReps: "Chargement de vos représentants...",
  queryingAPI: "Interrogation de l'API Represent...",
  primaryLabel: "Principal :",
  alsoInvolvedLabel: "Aussi concerné :",
  otherRepresentatives: "Autres représentants",
  noRepFound: "Aucun représentant trouvé pour ce niveau.",
  footerText: "My Civic Voice Canada — Helping citizens connect with their government",
  helpFAQ: "Aide / FAQ",
  sendFeedback: "Envoyer des commentaires",
  feedbackTitle: "Envoyer des commentaires",
  feedbackSubtitle: "Vos commentaires nous aident à améliorer cet outil pour tous les Canadiens",
  yourName: "Votre nom",
  feedbackMessage: "Message",
  feedbackPlaceholder: "Partagez vos suggestions, signalez des problèmes...",
  send: "Envoyer",
  sending: "Envoi en cours...",
  thankYou: "Merci !",
  feedbackSuccess: "Vos commentaires ont été envoyés.",
  close: "Fermer",
  saveDraft: "Enregistrer le brouillon",
  draftSaved: "Brouillon enregistré !",
  restoreDraft: "Restaurer le brouillon",
  draftRestored: "Brouillon restauré !",
  clearDraft: "Effacer le brouillon",
  faqTitle: "Questions fréquentes",
  // Categories in French
  categories: {
    infrastructure: "Infrastructure et transports",
    healthcare: "Soins de santé",
    education: "Éducation",
    housing: "Logement et développement",
    environment: "Environnement et climat",
    safety: "Sécurité publique et justice",
    employment: "Emploi et travail",
    social: "Services sociaux et prestations",
    taxes: "Impôts et finances",
    immigration: "Immigration et citoyenneté",
    consumer: "Droits des consommateurs",
    indigenous: "Affaires autochtones",
    seniors: "Aînés et vieillissement",
    veterans: "Anciens combattants",
    disability: "Handicap et accessibilité",
    youth: "Jeunesse et étudiants",
    agriculture: "Agriculture et milieu rural",
    utilities: "Services publics",
    family: "Droit de la famille",
    arts: "Arts et culture"
  }
};

'''

# FAQ content
faq_code = '''
// FAQ content
const FAQ = [
  { q: "Why do I need to know which level of government handles my issue?", a: "Each level of government in Canada has different responsibilities. Municipal handles local matters like transit and zoning. Provincial manages education, healthcare, and highways. Federal deals with national issues like immigration and defence. Contacting the right level ensures your voice reaches decision-makers who can actually help." },
  { q: "What's the difference between municipal, provincial, and federal government?", a: "Municipal governments handle local matters like transit, garbage collection, and zoning. Provincial governments manage education, healthcare, highways, and other region-wide services. Federal government deals with national issues like immigration, defence, trade, and taxes that affect all Canadians." },
  { q: "How do I know if my issue is municipal, provincial, or federal?", a: "Think about the scope: if it's about your street, neighbourhood, or city services, it's likely municipal. If it involves schools, hospitals, or provincial laws, it's provincial. National concerns like passports, employment insurance, or international matters fall under federal jurisdiction. Our issue guide helps you figure it out quickly." },
  { q: "What if my issue involves multiple levels of government?", a: "Many issues cross boundaries—affordable housing involves all three levels. Start with the level that has the most direct responsibility, then consider reaching out to others. You can also mention in your message that you're contacting multiple representatives." },
  { q: "How do I contact my representative?", a: "Enter your postal code and we'll show you all your elected officials at every level. You'll see their contact information including email, phone, and sometimes social media. From there, you can reach out directly through your preferred method." },
  { q: "What should I include in my message?", a: "Be clear and concise: state your issue, explain why it matters to you, and suggest what action you'd like to see. Include your name and postal code so they know you're a constituent. A respectful, well-organized message is more likely to get a thoughtful response." },
  { q: "How long should I wait for a response?", a: "Response times vary, but most offices aim to reply within 2-4 weeks for written correspondence. Phone calls may get a quicker acknowledgment. If it's urgent, calling their office directly is often faster than email." },
  { q: "What if I don't get a response?", a: "Try following up with a polite email or phone call, or reach out through social media. You can also contact another representative at the same level, or reach out to your local MP or MPP's constituency office." },
  { q: "Is my data private?", a: "Yes. My Civic Voice only collects what's needed to help you find your representatives. We never sell your data or share it with third parties. Your draft letters are stored only in your browser's local storage." },
  { q: "Where does the representative information come from?", a: "We pull representative data from official government sources, including Elections Canada, provincial elections offices, and municipal websites. We update our database regularly. If you spot something out of date, please let us know." }
];

'''

# Find the position to insert (before the REPRESENT API comment)
marker = "// 📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊📊\n// REPRESENT API"

if marker in content:
    # Insert French and FAQ before the REPRESENT API section
    insert_pos = content.find(marker)
    content = content[:insert_pos] + fr_code + faq_code + "\n" + marker + content[insert_pos + len(marker):]
    print("Inserted French translations and FAQ")
else:
    print("Marker not found, trying alternative...")
    # Try alternative marker
    alt_marker = "// REPRESENT API (FREE, NO KEY NEEDED)"
    if alt_marker in content:
        insert_pos = content.find(alt_marker)
        content = content[:insert_pos] + fr_code + faq_code + "\n\n" + alt_marker + content[insert_pos + len(alt_marker):]
        print("Inserted French translations and FAQ (alternative)")
    else:
        print("Could not find insertion point")

# Write back
with open(r'D:\source_extracted\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"File updated. Size: {len(content)} bytes")