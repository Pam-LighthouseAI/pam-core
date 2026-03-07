"""
Python script to fix French translations for letter drafting UI in index.html
"""

import re

def fix_french_translations():
    file_path = r'D:\source_extracted\index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes_made = []
    
    # 1. Add missing French translations to FR object
    # Find the FR object and add missing keys
    fr_additions = '''
  draftYourLetter: "Rédiger votre lettre",
  yourStory: "Votre histoire",
  selectTone: "Sélectionner le ton",
  previewLetter: "Prévisualiser la lettre",
  startNewLetter: "Commencer une nouvelle lettre",
  tipsForPowerfulLetter: "Conseils pour une lettre efficace :",
  tellYourStory: "Racontez votre histoire personnelle",
  toneUrgent: "Urgent",
  toneConcerned: "Préoccupé",
  toneHopeful: "Espoir",
  toneFrustrated: "Frustré",
'''
    
    # Check if these keys already exist, if not add them
    if 'draftYourLetter:' not in content:
        # Find the end of FR object (before the closing brace after toneFrustrated)
        pattern = r'(toneFrustrated: "Frustré",\n)'
        replacement = r'\1' + fr_additions
        content = re.sub(pattern, replacement, content)
        changes_made.append("Added missing FR translations: draftYourLetter, yourStory, selectTone, previewLetter, startNewLetter, tipsForPowerfulLetter, tellYourStory")
    
    # 2. Add French story prompts - STORY_PROMPTS_FR object
    story_prompts_fr = '''
// STORY PROMPTS - FRENCH VERSIONS
const STORY_PROMPTS_FR = {
  infrastructure: [
    "Comment ce problème affecte-t-il vos déplacements quotidiens?",
    "Avez-vous ou quelqu'un de votre connaissance été blessé ou mis en danger?",
    "Depuis combien de temps ce problème existe-t-il?",
    "Qu'avez-vous essayé de faire à ce sujet auparavant?"
  ],
  healthcare: [
    "Comment cela a-t-il affecté votre santé ou celle de votre famille?",
    "Avez-vous connu des délais ou des obstacles pour obtenir des soins?",
    "Que signifierait un meilleur accès pour vous?",
    "Comment les autres membres de votre communauté sont-ils touchés?"
  ],
  education: [
    "Comment cela affecte-t-il l'apprentissage de votre enfant ou votre propre éducation?",
    "Quelles opportunités sont manquées?",
    "Comment cela se compare-t-il à d'autres écoles ou régions?",
    "À quoi ressemblerait une solution idéale pour votre famille?"
  ],
  housing: [
    "Comment cette situation de logement affecte-t-elle votre vie quotidienne?",
    "Avez-vous peur de perdre votre logement ou de trouver un logement abordable?",
    "Quelle part de vos revenus va au logement?",
    "Avez-vous essayé de résoudre ce problème avec votre propriétaire ou la ville?"
  ],
  environment: [
    "Comment ce problème environnemental affecte-t-il votre santé ou votre qualité de vie?",
    "Y a-t-il des endroits que vous ne pouvez plus apprécier à cause de cela?",
    "Comment cela impacte-t-il vos enfants ou les générations futures?",
    "Quels changements avez-vous constatés au fil du temps?"
  ],
  safety: [
    "Avez-vous ou quelqu'un de votre connaissance été directement touché?",
    "Comment cela a-t-il changé votre sentiment de sécurité dans votre communauté?",
    "Qu'est-ce qui vous ferait vous sentir plus en sécurité?",
    "Avez-vous déjà signalé cela? Que s'est-il passé?"
  ],
  employment: [
    "Comment ce problème de travail vous affecte-t-il personnellement?",
    "D'autres personnes à votre travail rencontrent-elles le même problème?",
    "Avez-vous essayé d'aborder cela en interne? Que s'est-il passé?",
    "À quoi ressemblerait un traitement équitable?"
  ],
  social: [
    "Comment cela affecte-t-il votre capacité à subvenir à vos besoins essentiels?",
    "Quels obstacles avez-vous rencontrés en cherchant de l'aide?",
    "Comment la résolution de ce problème changerait-elle votre vie?",
    "Que voudriez-vous que les décideurs comprennent?"
  ],
  taxes: [
    "Comment ce problème fiscal affecte-t-il votre budget familial?",
    "Faites-vous face à des pénalités ou des litiges qui semblent injustes?",
    "À quoi ressemblerait une résolution équitable?",
    "Avez-vous essayé de résoudre cela par les voies normales?"
  ],
  immigration: [
    "Quelle est votre situation actuelle et qu'espérez-vous?",
    "Comment l'attente ou l'incertitude affecte-t-elle votre vie et votre famille?",
    "Que signifierait pour vous la résolution de ce problème?",
    "Avez-vous rencontré des obstacles spécifiques dans le processus?"
  ],
  consumer: [
    "Qu'avez-vous acheté ou à quoi vous êtes-vous inscrit, et qu'est-ce qui a mal tourné?",
    "Combien d'argent ou de temps avez-vous perdu?",
    "Avez-vous essayé de résoudre cela avec l'entreprise?",
    "À quoi ressemblerait une résolution équitable?"
  ],
  indigenous: [
    "Comment ce problème vous affecte-t-il, vous ou votre communauté?",
    "À quoi ressemblerait une action significative?",
    "Quel contexte historique les décideurs devraient-ils comprendre?",
    "Quels changements feraient la plus grande différence?"
  ],
  seniors: [
    "Comment ce problème affecte-t-il votre vie quotidienne ou votre bien-être?",
    "Pouvez-vous accéder aux services ou au soutien dont vous avez besoin?",
    "Qu'est-ce qui vous aiderait à vivre de manière plus indépendante ou sécuritaire?",
    "Avez-vous essayé d'autres programmes ou services?"
  ],
  veterans: [
    "Quel service avez-vous fourni et que recherchez-vous?",
    "Comment cela affecte-t-il votre transition vers la vie civile?",
    "À quels avantages ou quelle reconnaissance avez-vous droit?",
    "Avez-vous rencontré des obstacles dans le système?"
  ],
  disability: [
    "Comment ce problème d'accessibilité affecte-t-il votre vie quotidienne?",
    "Quels obstacles rencontrez-vous que d'autres pourraient ne pas voir?",
    "À quoi ressemblerait une inclusion significative?",
    "Avez-vous déjà soulevé cette question? Que s'est-il passé?"
  ],
  youth: [
    "Comment ce problème affecte-t-il votre éducation ou votre avenir?",
    "Quelles opportunités manquez-vous?",
    "Qu'est-ce qui vous aiderait à réussir?",
    "Comment d'autres jeunes dans votre situation sont-ils touchés?"
  ],
  agriculture: [
    "Comment cela affecte-t-il votre ferme ou vos moyens de subsistance ruraux?",
    "Quel soutien vous aiderait le plus?",
    "Comment cela se compare-t-il au soutien dans d'autres régions?",
    "À quoi ressemblerait un changement durable?"
  ],
  utilities: [
    "Comment ces coûts ou problèmes de services publics affectent-ils votre ménage?",
    "Avez-vous connu des problèmes de service ou des litiges de facturation?",
    "À quoi ressemblerait un service équitable et fiable?",
    "Avez-vous essayé de résoudre cela avec le fournisseur?"
  ],
  family: [
    "Comment cela affecte-t-il le bien-être de votre famille?",
    "Quel résultat recherchez-vous pour vos enfants ou votre famille?",
    "Avez-vous essayé d'autres voies de résolution?",
    "À quoi ressemblerait la stabilité pour votre famille?"
  ],
  arts: [
    "Comment cela affecte-t-il votre capacité à créer ou accéder à la culture?",
    "Quelles opportunités sont perdues?",
    "Comment le soutien aux arts profiterait-il à votre communauté?",
    "De quels programmes ou espaces avez-vous besoin?"
  ],
  lgbtq: [
    "Comment ce problème a-t-il affecté votre sentiment de sécurité ou d'appartenance?",
    "Avez-vous vécu de la discrimination ou des obstacles?",
    "À quoi ressemblerait un soutien significatif pour vous ou votre communauté?",
    "Comment cela impacte-t-il votre vie quotidienne ou vos relations?"
  ],
  women: [
    "Comment ce problème vous a-t-il affectée, vous ou les femmes de votre vie?",
    "Quels obstacles avez-vous rencontrés en raison de votre genre?",
    "À quoi ressemblerait l'égalité ou la sécurité dans cette situation?",
    "Avez-vous essayé d'aborder cela par d'autres voies?"
  ],
  mentalhealth: [
    "Comment cela a-t-il affecté votre santé mentale ou votre bien-être?",
    "Avez-vous pu accéder au soutien dont vous avez besoin?",
    "Que signifierait un meilleur soutien en santé mentale pour vous?",
    "Comment les autres membres de votre communauté sont-ils touchés?"
  ],
  substance: [
    "Comment la consommation de substances a-t-elle affecté vous ou quelqu'un qui vous est cher?",
    "Quels obstacles avez-vous rencontrés pour obtenir de l'aide?",
    "Quel type de soutien ferait une différence?",
    "Comment cela a-t-il impacté votre famille ou votre communauté?"
  ],
  transportation: [
    "Comment ce problème de transport affecte-t-il votre vie quotidienne?",
    "Pouvez-vous vous rendre où vous devez aller?",
    "Que signifierait un meilleur transport pour vous?",
    "Avez-vous déjà soulevé cette question? Que s'est-il passé?"
  ],
  digital: [
    "Comment ce problème de droits numériques vous a-t-il affecté?",
    "Qu'est-il arrivé à vos données ou à votre vie privée?",
    "À quoi ressemblerait un traitement équitable?",
    "Avez-vous essayé de résoudre cela avec l'entreprise?"
  ],
  animals: [
    "Comment ce problème de bien-être animal vous affecte-t-il, vous ou votre communauté?",
    "Qu'avez-vous observé ou vécu?",
    "À quoi ressemblerait une protection appropriée?",
    "Avez-vous déjà signalé cela?"
  ],
  sports: [
    "Comment cela affecte-t-il votre capacité à participer aux sports ou aux loisirs?",
    "Quelles opportunités manquez-vous, vous ou votre famille?",
    "À quoi ressemblerait un meilleur accès?",
    "Comment cela impacte-t-il votre communauté?"
  ],
  religion: [
    "Comment cela a-t-il affecté votre capacité à pratiquer votre foi?",
    "Avez-vous vécu de la discrimination ou des obstacles?",
    "À quoi ressemblerait un accommodement religieux?",
    "Comment cela impacte-t-il votre communauté?"
  ],
  volunteer: [
    "Comment cela affecte-t-il votre capacité à faire du bénévolat ou à participer?",
    "Quel besoin communautaire essayez-vous de répondre?",
    "Quel soutien aiderait vos efforts de bénévolat?",
    "Quel impact auraient de meilleures ressources?"
  ],
  legalaid: [
    "Quel problème juridique rencontrez-vous?",
    "Avez-vous pu obtenir de l'aide juridique?",
    "Que signifierait l'accès à la justice pour vous?",
    "Comment cela affecte-t-il votre vie en ce moment?"
  ],
  pensions: [
    "Comment ce problème de pension ou de retraite vous affecte-t-il?",
    "À quels avantages avez-vous droit?",
    "Avez-vous essayé de résoudre cela par les voies normales?",
    "À quoi ressemblerait une résolution équitable?"
  ],
  childcare: [
    "Comment la situation de garde d'enfants affecte-t-elle votre famille?",
    "Quels obstacles avez-vous rencontrés pour trouver une garde?",
    "Que signifierait une garde d'enfants abordable pour vous?",
    "Comment cela impacte-t-il votre travail ou votre éducation?"
  ],
  food: [
    "Comment l'insécurité alimentaire vous affecte-t-elle, vous ou votre famille?",
    "Quels obstacles rencontrez-vous pour accéder à une nourriture saine?",
    "À quoi ressemblerait la sécurité alimentaire pour vous?",
    "Comment cela affecte-t-il votre vie quotidienne?"
  ],
  emergency: [
    "De quelle situation d'urgence faites-vous face?",
    "Comment a été la réponse?",
    "De quel soutien avez-vous besoin?",
    "Comment cela a-t-il affecté votre sentiment de sécurité?"
  ],
  humanrights: [
    "Comment ce problème de droits de la personne vous a-t-il affecté?",
    "Quelle discrimination ou violation avez-vous vécue?",
    "À quoi ressemblerait la justice?",
    "Avez-vous essayé d'aborder cela ailleurs?"
  ]
};
'''
    
    # Find where to insert STORY_PROMPTS_FR (after STORY_PROMPTS definition ends)
    if 'STORY_PROMPTS_FR' not in content:
        # Find the end of STORY_PROMPTS object
        pattern = r'(const STORY_PROMPTS = \{[^}]+\};\n)'
        replacement = r'\1' + story_prompts_fr
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        changes_made.append("Added STORY_PROMPTS_FR with French translations for all 36 categories")
    
    # 3. Fix tone buttons to use FR translations
    # Find the tone buttons section and replace hardcoded English with dynamic translations
    old_tone_buttons = '''<div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
            <button onClick={()=>setUTone('urgent')} style={{padding:'10px 16px',borderRadius:20,border:uTone==='urgent'?'2px solid #EF4444':'2px solid transparent',background:uTone==='urgent'?'rgba(239,68,68,0.15)':'rgba(255,255,255,0.05)',color:uTone==='urgent'?'#F87171':'#9CA3AF',cursor:'pointer',transition:'all 0.15s'}}>🚨 Urgent</button>
            <button onClick={()=>setUTone('concerned')} style={{padding:'10px 16px',borderRadius:20,border:uTone==='concerned'?'2px solid #3B82F6':'2px solid transparent',background:uTone==='concerned'?'rgba(59,130,246,0.15)':'rgba(255,255,255,0.05)',color:uTone==='concerned'?'#60A5FA':'#9CA3AF',cursor:'pointer',transition:'all 0.15s'}}>😟 Concerned</button>
            <button onClick={()=>setUTone('hopeful')} style={{padding:'10px 16px',borderRadius:20,border:uTone==='hopeful'?'2px solid #10B981':'2px solid transparent',background:uTone==='hopeful'?'rgba(16,185,129,0.15)':'rgba(255,255,255,0.05)',color:uTone==='hopeful'?'#34D399':'#9CA3AF',cursor:'pointer',transition:'all 0.15s'}}>🌟 Hopeful</button>
            <button onClick={()=>setUTone('frustrated')} style={{padding:'10px 16px',borderRadius:20,border:uTone==='frustrated'?'2px solid #F59E0B':'2px solid transparent',background:uTone==='frustrated'?'rgba(245,158,11,0.15)':'rgba(255,255,255,0.05)',color:uTone==='frustrated'?'#FBBF24':'#9CA3AF',cursor:'pointer',transition:'all 0.15s'}}>😤 Frustrated</button>
          </div>'''
    
    new_tone_buttons = '''<div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
            <button onClick={()=>setUTone('urgent')} style={{padding:'10px 16px',borderRadius:20,border:uTone==='urgent'?'2px solid #EF4444':'2px solid transparent',background:uTone==='urgent'?'rgba(239,68,68,0.15)':'rgba(255,255,255,0.05)',color:uTone==='urgent'?'#F87171':'#9CA3AF',cursor:'pointer',transition:'all 0.15s'}}>🚨 {isFrench ? FR.toneUrgent : 'Urgent'}</button>
            <button onClick={()=>setUTone('concerned')} style={{padding:'10px 16px',borderRadius:20,border:uTone==='concerned'?'2px solid #3B82F6':'2px solid transparent',background:uTone==='concerned'?'rgba(59,130,246,0.15)':'rgba(255,255,255,0.05)',color:uTone==='concerned'?'#60A5FA':'#9CA3AF',cursor:'pointer',transition:'all 0.15s'}}>😟 {isFrench ? FR.toneConcerned : 'Concerned'}</button>
            <button onClick={()=>setUTone('hopeful')} style={{padding:'10px 16px',borderRadius:20,border:uTone==='hopeful'?'2px solid #10B981':'2px solid transparent',background:uTone==='hopeful'?'rgba(16,185,129,0.15)':'rgba(255,255,255,0.05)',color:uTone==='hopeful'?'#34D399':'#9CA3AF',cursor:'pointer',transition:'all 0.15s'}}>🌟 {isFrench ? FR.toneHopeful : 'Hopeful'}</button>
            <button onClick={()=>setUTone('frustrated')} style={{padding:'10px 16px',borderRadius:20,border:uTone==='frustrated'?'2px solid #F59E0B':'2px solid transparent',background:uTone==='frustrated'?'rgba(245,158,11,0.15)':'rgba(255,255,255,0.05)',color:uTone==='frustrated'?'#FBBF24':'#9CA3AF',cursor:'pointer',transition:'all 0.15s'}}>😤 {isFrench ? FR.toneFrustrated : 'Frustrated'}</button>
          </div>'''
    
    if old_tone_buttons in content:
        content = content.replace(old_tone_buttons, new_tone_buttons)
        changes_made.append("Fixed tone buttons to use French translations")
    
    # 4. Fix "Tips for a powerful letter:" to use FR translation
    old_tips = '''<div style={{fontWeight:600,color:'#FBBF24',marginBottom:8,fontSize:14}}>💡 Tips for a powerful letter:</div>'''
    new_tips = '''<div style={{fontWeight:600,color:'#FBBF24',marginBottom:8,fontSize:14}}>💡 {isFrench ? (FR.tipsForPowerfulLetter || "Conseils pour une lettre efficace :") : "Tips for a powerful letter:"}</div>'''
    
    if old_tips in content:
        content = content.replace(old_tips, new_tips)
        changes_made.append("Fixed 'Tips for a powerful letter' to use French translation")
    
    # 5. Fix story prompts to use French versions
    # Find the story prompts rendering and make it bilingual
    old_story_prompts_render = '''{STORY_PROMPTS[selCat.id].map((prompt, i) => (
                <div key={i} style={{marginBottom:i < STORY_PROMPTS[selCat.id].length - 1 ? 6 : 0}}>• {prompt}</div>
              ))}'''
    
    new_story_prompts_render = '''{((isFrench && STORY_PROMPTS_FR && STORY_PROMPTS_FR[selCat.id]) ? STORY_PROMPTS_FR[selCat.id] : STORY_PROMPTS[selCat.id]).map((prompt, i) => {
                const prompts = isFrench && STORY_PROMPTS_FR && STORY_PROMPTS_FR[selCat.id] ? STORY_PROMPTS_FR[selCat.id] : STORY_PROMPTS[selCat.id];
                return <div key={i} style={{marginBottom:i < prompts.length - 1 ? 6 : 0}}>• {prompt}</div>;
              })}'''
    
    if old_story_prompts_render in content:
        content = content.replace(old_story_prompts_render, new_story_prompts_render)
        changes_made.append("Fixed story prompts to use French translations")
    
    # Write the fixed content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return changes_made

if __name__ == '__main__':
    changes = fix_french_translations()
    print("Changes made:")
    for change in changes:
        print(f"  - {change}")
    print(f"\nTotal: {len(changes)} changes applied")