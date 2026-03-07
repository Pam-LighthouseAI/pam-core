"""
Script to add Privacy Modal and About Modal with French translations to index.html
"""

import re

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Read the file
content = read_file(r'D:\source_extracted\index.html')

# Add French translations to FR object for Privacy and About modals
fr_additions = '''
  privacyTitle: "Confidentialite",
  privacyIntro: "Ma Voix Civique s'engage a proteger votre vie privee. Cette politique decrit quelles donnees nous collectons et comment nous les utilisons.",
  privacyDataTitle: "Donnees que nous collectons",
  privacyData1: "Code postal - utilise pour trouver vos representants elus",
  privacyData2: "Nom et coordonnees - fournis volontairement pour rediger des lettres",
  privacyData3: "Brouillons de lettres - stockes uniquement dans votre navigateur (stockage local)",
  privacyNoDataTitle: "Ce que nous ne faisons PAS",
  privacyNoData1: "Nous ne vendons jamais vos donnees",
  privacyNoData2: "Nous ne partageons pas vos informations avec des tiers",
  privacyNoData3: "Nous ne stockons pas vos donnees sur nos serveurs",
  privacyStorageTitle: "Stockage local",
  privacyStorageText: "Vos brouillons de lettres et preferences de langue sont stockes uniquement dans le stockage local de votre navigateur. Vous pouvez les effacer a tout moment en vidant les donnees de votre navigateur.",
  privacyApiTitle: "API Represent",
  privacyApiText: "Nous utilisons l'API Represent d'OpenNorth pour trouver vos representants. Cette API est exploitee par OpenNorth, une organisation independante a but non lucratif.",
  privacyContact: "Pour toute question concernant votre vie privee, contactez-nous a privacy@mycivicvoice.ca",
  aboutTitle: "A propos",
  aboutIntro: "Ma Voix Civique Canada est un outil gratuit et a but non lucratif concu pour aider les citoyens canadiens a entrer en contact avec leurs representants elus.",
  aboutMissionTitle: "Notre mission",
  aboutMissionText: "Nous croyons que chaque citoyen merite de savoir qui represente ses interets et comment faire entendre sa voix. Notre mission est de simplifier le processus d'engagement civique pour tous les Canadiens.",
  aboutHowTitle: "Comment ca fonctionne",
  aboutHow1: "Entrez votre code postal ou votre ville pour trouver vos representants",
  aboutHow2: "Decrivez votre enjeu pour obtenir des conseils sur le bon niveau de gouvernement",
  aboutHow3: "Redigez une lettre personnelle avec notre modele",
  aboutHow4: "Contactez vos representants directement par courriel ou par telephone",
  aboutDataTitle: "Sources des donnees",
  aboutDataText: "Les donnees sur les representants proviennent de l'API Represent d'OpenNorth, qui consolide les donnees d'Elections Canada, des bureaux electoraux provinciaux et des sources municipales.",
  aboutAccuracy: "Les donnees federales et provinciales sont generalement a jour. Les donnees municipales peuvent parfois etre obsoletes apres les elections locales.",
  aboutOpen: "Cet outil est un projet open source. Vous pouvez contribuer sur GitHub.",
'''

# Find the FR object and add new translations
fr_object_pattern = r'(const FR\s*=\s*\{[\s\S]*?categories:\s*\{)'
# Find the end of categories object
fr_end_pattern = r'(const FR\s*=\s*\{[\s\S]*?\}\s*;)'  

# Check if privacyTitle already exists in FR
if 'privacyTitle:' not in content:
    # Find where to insert - before the closing of FR object (before categories or at the end of categories)
    # Find the categories section
    categories_match = re.search(r'const FR\s*=\s*\{([\s\S]*?)categories:\s*\{', content)
    if categories_match:
        # Insert before categories
        insert_pos = categories_match.end() - len('categories:\s*\{')
        # Actually we need to insert before categories, after the existing content
        # Let's find the right place
        before_categories = content[:categories_match.start()] + 'const FR = {\n'
        after_categories_start = categories_match.group(1)
        
        # Find end of FR object
        fr_end = re.search(r'\}\s*;[\s\S]*?// FAQ DATA', content)
        if fr_end:
            # Insert before the closing brace
            insert_point = fr_end.start()
            new_content = content[:insert_point] + fr_additions + '\n' + content[insert_point:]
            content = new_content
            print("Added French translations to FR object")
        else:
            print("Could not find end of FR object")
    else:
        print("Could not find FR object")

# Now add the Privacy Modal and About Modal components
# Find the location after DraftPrompt and before the main App component

privacy_modal = '''
// PRIVACY MODAL COMPONENT
function PrivacyModal({ isOpen, onClose, isFrench }) {
  const t = isFrench ? FR : {};
  const getText = (key, en) => t[key] || en;
  
  if (!isOpen) return null;
  
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:24}}>
          <h2 style={{margin:0,fontSize:22}}>{getText('privacyTitle','Privacy')}</h2>
          <button onClick={onClose} style={{background:'none',border:'none',color:'#9CA3AF',fontSize:28,cursor:'pointer'}}>×</button>
        </div>
        <div style={{color:'#9CA3AF',fontSize:14,lineHeight:1.7}}>
          <p style={{marginBottom:16}}>{getText('privacyIntro','My Civic Voice is committed to protecting your privacy. This policy describes what data we collect and how we use it.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('privacyDataTitle','Data We Collect')}</h3>
          <ul style={{margin:0,paddingLeft:20}}>
            <li style={{marginBottom:8}}>{getText('privacyData1','Postal code - used to find your elected representatives')}</li>
            <li style={{marginBottom:8}}>{getText('privacyData2','Name and contact info - provided voluntarily to draft letters')}</li>
            <li style={{marginBottom:8}}>{getText('privacyData3','Letter drafts - stored only in your browser (local storage)')}</li>
          </ul>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('privacyNoDataTitle','What We Do NOT Do')}</h3>
          <ul style={{margin:0,paddingLeft:20}}>
            <li style={{marginBottom:8}}>{getText('privacyNoData1','We never sell your data')}</li>
            <li style={{marginBottom:8}}>{getText('privacyNoData2','We do not share your information with third parties')}</li>
            <li style={{marginBottom:8}}>{getText('privacyNoData3','We do not store your data on our servers')}</li>
          </ul>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('privacyStorageTitle','Local Storage')}</h3>
          <p style={{marginBottom:16}}>{getText('privacyStorageText','Your letter drafts and language preferences are stored only in your browser\'s local storage. You can clear them at any time by clearing your browser data.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('privacyApiTitle','Represent API')}</h3>
          <p style={{marginBottom:16}}>{getText('privacyApiText','We use the OpenNorth Represent API to find your representatives. This API is run by OpenNorth, an independent non-profit organization.')}</p>
          
          <p style={{marginTop:20,fontSize:13}}>{getText('privacyContact','For questions about your privacy, contact us at privacy@mycivicvoice.ca')}</p>
        </div>
      </div>
    </div>
  );
}

// ABOUT MODAL COMPONENT
function AboutModal({ isOpen, onClose, isFrench }) {
  const t = isFrench ? FR : {};
  const getText = (key, en) => t[key] || en;
  
  if (!isOpen) return null;
  
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:24}}>
          <h2 style={{margin:0,fontSize:22}}>{getText('aboutTitle','About')}</h2>
          <button onClick={onClose} style={{background:'none',border:'none',color:'#9CA3AF',fontSize:28,cursor:'pointer'}}>×</button>
        </div>
        <div style={{color:'#9CA3AF',fontSize:14,lineHeight:1.7}}>
          <p style={{marginBottom:16}}>{getText('aboutIntro','My Civic Voice Canada is a free, non-profit tool designed to help Canadian citizens connect with their elected representatives.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('aboutMissionTitle','Our Mission')}</h3>
          <p style={{marginBottom:16}}>{getText('aboutMissionText','We believe every citizen deserves to know who represents their interests and how to make their voice heard. Our mission is to make civic engagement accessible to all Canadians.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('aboutHowTitle','How It Works')}</h3>
          <ol style={{margin:0,paddingLeft:20}}>
            <li style={{marginBottom:8}}>{getText('aboutHow1','Enter your postal code or city to find your representatives')}</li>
            <li style={{marginBottom:8}}>{getText('aboutHow2','Describe your issue to get guidance on the right level of government')}</li>
            <li style={{marginBottom:8}}>{getText('aboutHow3','Draft a personal letter with our template')}</li>
            <li style={{marginBottom:8}}>{getText('aboutHow4','Contact your representatives directly by email or phone')}</li>
          </ol>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('aboutDataTitle','Data Sources')}</h3>
          <p style={{marginBottom:16}}>{getText('aboutDataText','Representative data comes from the OpenNorth Represent API, which consolidates data from Elections Canada, provincial elections offices, and municipal sources.')}</p>
          
          <p style={{marginTop:20,fontSize:13,color:'#6B7280'}}>{getText('aboutAccuracy','Federal and provincial data is generally current. Municipal data may occasionally be outdated after local elections.')}</p>
          
          <p style={{marginTop:16,fontSize:13}}>{getText('aboutOpen','This tool is an open source project. You can contribute on GitHub.')}</p>
        </div>
      </div>
    </div>
  );
}
'''

# Find the location after DraftPrompt and before the main App component
# Look for "// MAIN APP" comment
if '// MAIN APP' in content:
    insert_point = content.find('// MAIN APP')
    content = content[:insert_point] + privacy_modal + '\n' + content[insert_point:]
    print("Added PrivacyModal and AboutModal components")
else:
    # Alternative: find function App() 
    if 'function App()' in content:
        insert_point = content.find('function App()')
        content = content[:insert_point] + privacy_modal + '\n' + content[insert_point:]
        print("Added PrivacyModal and AboutModal components (before App)")

# Now add state and modal triggers in the App component
# Find the footer section and add Privacy and About buttons
footer_section = '''<footer style={{textAlign:'center',marginTop:40,paddingTop:20,borderTop:'1px solid rgba(255,255,255,0.06)'}}>
        <div style={{marginBottom:12}}>
          <button className="footer-btn" onClick={()=>setShowFAQ(true)}>{getText('helpFAQ','Help / FAQ')}</button>
          <button className="footer-btn" onClick={()=>setShowFeedback(true)}>{getText('sendFeedback','Send Feedback')}</button>
        </div>'''

# Check if Privacy button already exists
if 'Privacy' not in content or 'setShowPrivacy' not in content:
    # Replace the footer section with updated version including Privacy and About
    new_footer = '''<footer style={{textAlign:'center',marginTop:40,paddingTop:20,borderTop:'1px solid rgba(255,255,255,0.06)'}}>
        <div style={{marginBottom:12}}>
          <button className="footer-btn" onClick={()=>setShowFAQ(true)}>{getText('helpFAQ','Help / FAQ')}</button>
          <button className="footer-btn" onClick={()=>setShowPrivacy(true)}>{getText('privacyTitle','Privacy')}</button>
          <button className="footer-btn" onClick={()=>setShowAbout(true)}>{getText('aboutTitle','About')}</button>
          <button className="footer-btn" onClick={()=>setShowFeedback(true)}>{getText('sendFeedback','Send Feedback')}</button>
        </div>'''
    
    content = content.replace(footer_section, new_footer)
    print("Updated footer with Privacy and About buttons")

# Add state variables for Privacy and About modals
# Find the state declarations after showDraftPrompt
state_pattern = r'(const \[showDraftPrompt, setShowDraftPrompt\] = React\.useState\(false\);)'
if 'const [showPrivacy' not in content:
    state_addition = r'\1\n  const [showPrivacy, setShowPrivacy] = React.useState(false);\n  const [showAbout, setShowAbout] = React.useState(false);'
    content = re.sub(state_pattern, state_addition, content)
    print("Added state variables for Privacy and About modals")

# Add modal components at the end before closing of return statement
# Find the location of FAQModal and FeedbackModal
modal_location = '''      {/* Modals */}
      <FAQModal isOpen={showFAQ} onClose={()=>setShowFAQ(false)} isFrench={isFrench} />
      <FeedbackModal isOpen={showFeedback} onClose={()=>setShowFeedback(false)} isFrench={isFrench} />'''

new_modal_location = '''      {/* Modals */}
      <FAQModal isOpen={showFAQ} onClose={()=>setShowFAQ(false)} isFrench={isFrench} />
      <FeedbackModal isOpen={showFeedback} onClose={()=>setShowFeedback(false)} isFrench={isFrench} />
      <PrivacyModal isOpen={showPrivacy} onClose={()=>setShowPrivacy(false)} isFrench={isFrench} />
      <AboutModal isOpen={showAbout} onClose={()=>setShowAbout(false)} isFrench={isFrench} />'''

if 'PrivacyModal isOpen' not in content:
    content = content.replace(modal_location, new_modal_location)
    print("Added PrivacyModal and AboutModal to the render")

# Write the updated content
write_file(r'D:\source_extracted\index.html', content)
print("\nFile updated successfully!")