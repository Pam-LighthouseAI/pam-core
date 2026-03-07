#!/usr/bin/env python3
"""Add French translations to all TEMPLATES in my_civic_voice.html"""

import re

# French translations for all templates
french_translations = {
    'infrastructure': {
        'subject': "Préoccupation concernant l'infrastructure et les transports : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question d'infrastructure et de transport : {{ISSUE}}.

{{DETAILS}}

En tant que mon représentant élu, j'apprécierais vos conseils sur ce dossier et les mesures que vous pourriez prendre pour y remédier.

Merci de votre temps et de votre attention à ce dossier.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'healthcare': {
        'subject': "Préoccupation concernant les soins de santé : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de soins de santé : {{ISSUE}}.

{{DETAILS}}

L'accès à des soins de santé de qualité est essentiel pour tous les Canadiens. J'apprécierais votre soutien pour régler ce problème.

Merci de votre attention à cette question importante.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'education': {
        'subject': "Préoccupation concernant l'éducation : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question d'éducation : {{ISSUE}}.

{{DETAILS}}

Une éducation de qualité est vitale pour l'avenir de notre communauté. J'apprécierais votre aide pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'housing': {
        'subject': "Préoccupation concernant le logement et le développement : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de logement : {{ISSUE}}.

{{DETAILS}}

Un logement abordable et sécuritaire est un besoin fondamental. J'apprécierais votre aide pour résoudre ce problème.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'environment': {
        'subject': "Préoccupation concernant l'environnement et le climat : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question environnementale : {{ISSUE}}.

{{DETAILS}}

La protection de notre environnement est essentielle pour les générations actuelles et futures. J'apprécierais votre soutien sur ce dossier.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'safety': {
        'subject': "Préoccupation concernant la sécurité publique et la justice : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de sécurité publique : {{ISSUE}}.

{{DETAILS}}

La sécurité et la justice sont fondamentales pour notre communauté. J'apprécierais votre aide pour résoudre ce problème.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'employment': {
        'subject': "Préoccupation concernant l'emploi et le travail : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question d'emploi : {{ISSUE}}.

{{DETAILS}}

Des conditions de travail équitables sont essentielles pour tous les Canadiens. J'apprécierais votre aide pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'social': {
        'subject': "Préoccupation concernant les services sociaux et les prestations : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de services sociaux : {{ISSUE}}.

{{DETAILS}}

Les systèmes de soutien social sont vitaux pour le bien-être de la communauté. J'apprécierais votre aide avec ce dossier.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'taxes': {
        'subject': "Préoccupation concernant les impôts et les finances : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question fiscale : {{ISSUE}}.

{{DETAILS}}

Une fiscalité équitable et transparente est importante pour tous les Canadiens. J'apprécierais vos conseils sur ce dossier.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'immigration': {
        'subject': "Préoccupation concernant l'immigration et la citoyenneté : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question d'immigration : {{ISSUE}}.

{{DETAILS}}

L'immigration est vitale pour la croissance et la diversité du Canada. J'apprécierais votre aide avec ce dossier.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'consumer': {
        'subject': "Préoccupation concernant les droits des consommateurs : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de droits des consommateurs : {{ISSUE}}.

{{DETAILS}}

La protection des consommateurs est essentielle pour un marché équitable. J'apprécierais votre aide pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'indigenous': {
        'subject': "Préoccupation concernant les affaires autochtones : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question affectant les communautés autochtones : {{ISSUE}}.

{{DETAILS}}

La réconciliation et les droits autochtones sont des priorités importantes. J'apprécierais votre soutien pour régler ce problème.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'seniors': {
        'subject': "Préoccupation concernant les aînés : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question affectant les aînés : {{ISSUE}}.

{{DETAILS}}

Soutenir nos aînés est essentiel pour une société bienveillante. J'apprécierais votre aide pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'veterans': {
        'subject': "Préoccupation concernant les anciens combattants : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question affectant les vétérans : {{ISSUE}}.

{{DETAILS}}

Nos vétérans méritent notre soutien et notre reconnaissance. J'apprécierais votre aide pour résoudre ce problème.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'disability': {
        'subject': "Préoccupation concernant l'accessibilité et le handicap : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question d'accessibilité et de droits des personnes handicapées : {{ISSUE}}.

{{DETAILS}}

L'accessibilité et l'inclusion sont des droits fondamentaux. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'youth': {
        'subject': "Préoccupation concernant la jeunesse et les étudiants : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question affectant les jeunes et les étudiants : {{ISSUE}}.

{{DETAILS}}

Investir dans notre jeunesse, c'est investir dans l'avenir du Canada. J'apprécierais votre aide avec ce dossier.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'agriculture': {
        'subject': "Préoccupation concernant l'agriculture et le milieu rural : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question agricole : {{ISSUE}}.

{{DETAILS}}

L'agriculture et les communautés rurales sont essentielles au Canada. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'utilities': {
        'subject': "Préoccupation concernant les services publics : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de services publics : {{ISSUE}}.

{{DETAILS}}

Des services publics fiables et abordables sont essentiels pour tous les Canadiens. J'apprécierais votre aide avec ce dossier.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'family': {
        'subject': "Préoccupation concernant le droit de la famille : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de droit de la famille : {{ISSUE}}.

{{DETAILS}}

Les questions de droit de la famille touchent profondément les familles et les enfants. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'arts': {
        'subject': "Préoccupation concernant les arts et la culture : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question d'arts et de culture : {{ISSUE}}.

{{DETAILS}}

Les arts et la culture enrichissent nos communautés et notre société. J'apprécierais votre aide avec ce dossier.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'tenants': {
        'subject': "Préoccupation concernant les droits des locataires : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de droits des locataires : {{ISSUE}}.

{{DETAILS}}

Un logement équitable et des protections pour les locataires sont essentiels pour tous les locataires. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'electoral': {
        'subject': "Préoccupation concernant la réforme électorale : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question électorale et démocratique : {{ISSUE}}.

{{DETAILS}}

Un système électoral équitable et accessible est fondamental pour notre démocratie. J'apprécierais votre soutien sur ce dossier.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'women': {
        'subject': "Préoccupation concernant les droits des femmes : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de droits des femmes et d'égalité des genres : {{ISSUE}}.

{{DETAILS}}

L'égalité des genres profite à tous les Canadiens. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'lgbtq': {
        'subject': "Préoccupation concernant les droits LGBTQ2+ : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de droits LGBTQ2+ : {{ISSUE}}.

{{DETAILS}}

L'égalité et l'inclusion pour tous les Canadiens sont essentielles. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'animals': {
        'subject': "Préoccupation concernant le bien-être animal : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de bien-être animal : {{ISSUE}}.

{{DETAILS}}

Protéger les animaux contre la cruauté et la négligence est important pour moi. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'mentalhealth': {
        'subject': "Préoccupation concernant la santé mentale : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de santé mentale et de dépendances : {{ISSUE}}.

{{DETAILS}}

L'accès aux services de santé mentale est essentiel pour tous les Canadiens. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'poverty': {
        'subject': "Préoccupation concernant la pauvreté et l'itinérance : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de pauvreté et d'itinérance : {{ISSUE}}.

{{DETAILS}}

S'attaquer à la pauvreté et à l'itinérance est essentiel pour une société juste. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'humanrights': {
        'subject': "Préoccupation concernant les droits de la personne : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de droits de la personne : {{ISSUE}}.

{{DETAILS}}

La protection des droits de la personne et des libertés civiles est fondamentale pour notre société. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'smallbusiness': {
        'subject': "Préoccupation concernant les petites entreprises : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de petite entreprise : {{ISSUE}}.

{{DETAILS}}

Les petites entreprises sont vitales pour notre économie et nos communautés. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'science': {
        'subject': "Préoccupation concernant la science et la recherche : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de science et de recherche : {{ISSUE}}.

{{DETAILS}}

La recherche scientifique et l'intégrité sont essentielles pour des politiques fondées sur des données probantes. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'media': {
        'subject': "Préoccupation concernant les médias et la liberté de la presse : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de médias et de liberté de la presse : {{ISSUE}}.

{{DETAILS}}

Une presse libre et indépendante est essentielle à la démocratie. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'broadband': {
        'subject': "Préoccupation concernant le haut débit et la connectivité : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de haut débit et de connectivité : {{ISSUE}}.

{{DETAILS}}

Un accès fiable à Internet est essentiel pour participer à la société moderne. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'fisheries': {
        'subject': "Préoccupation concernant les pêches et les océans : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de pêches : {{ISSUE}}.

{{DETAILS}}

Des pêches durables et des océans en santé sont importants pour les Canadiens. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'food': {
        'subject': "Préoccupation concernant la sécurité alimentaire : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de sécurité alimentaire : {{ISSUE}}.

{{DETAILS}}

L'accès à une nourriture abordable et nutritive est essentiel pour tous les Canadiens. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'languages': {
        'subject': "Préoccupation concernant les langues officielles : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de langues officielles : {{ISSUE}}.

{{DETAILS}}

Le bilinguisme et les droits linguistiques sont fondamentaux au Canada. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'sports': {
        'subject': "Préoccupation concernant le sport et les loisirs : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de sport et de loisirs : {{ISSUE}}.

{{DETAILS}}

Les opportunités sportives et récréatives profitent à la santé et au bien-être de la communauté. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre attention.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    },
    'international': {
        'subject': "Préoccupation concernant le développement international : {{ISSUE}}",
        'body': '''Cher {{REP_NAME}},

Je vous écris en tant que constituant concernant une question de développement international : {{ISSUE}}.

{{DETAILS}}

Le rôle du Canada dans le développement international reflète nos valeurs à l'échelle mondiale. J'apprécierais votre soutien pour résoudre ce problème.

Merci de votre temps.

Cordialement,
{{USER_NAME}}
{{USER_LOCATION}}
{{USER_EMAIL}}'''
    }
}

def main():
    # Read the file
    filepath = r'C:\nanobot\instance3\workspace\my_civic_voice.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the TEMPLATES object
    templates_start = content.find('const TEMPLATES = {')
    if templates_start == -1:
        print("ERROR: Could not find TEMPLATES object")
        return
    
    # Find the end of TEMPLATES
    templates_end = content.find('\n};', templates_start)
    if templates_end == -1:
        print("ERROR: Could not find end of TEMPLATES")
        return
    
    templates_end += 2  # Include the };
    
    # Build new TEMPLATES object
    new_templates = 'const TEMPLATES = {\n'
    
    # Extract original templates
    original_templates_section = content[templates_start:templates_end]
    
    # Process each category
    for cat_id, fr_data in french_translations.items():
        # Find the original English template
        pattern = rf'{cat_id}:\s*\{{\s*subject:\s*"(.*?)",\s*body:\s*`(.*?)`\s*\}}'
        match = re.search(pattern, original_templates_section, re.DOTALL)
        
        if match:
            eng_subject = match.group(1)
            eng_body = match.group(2)
            
            # Escape quotes in subject
            fr_subject = fr_data['subject'].replace('"', '\\"')
            eng_subject_escaped = eng_subject.replace('"', '\\"')
            
            new_templates += f'''  {cat_id}: {{
    subject: "{eng_subject_escaped}",
    subjectFr: "{fr_subject}",
    body: `{eng_body}`,
    bodyFr: `{fr_data['body']}`
  }},
'''
        else:
            print(f"WARNING: Could not find template for {cat_id}")
    
    new_templates += '};'
    
    # Replace the old TEMPLATES
    new_content = content[:templates_start] + new_templates + content[templates_end:]
    
    # Write back
    filepath = r'C:\nanobot\instance3\workspace\my_civic_voice.html'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'Successfully translated {len(french_translations)} templates!')
    
    # Verify the changes
    with open(filepath, 'r', encoding='utf-8') as f:
        verify_content = f.read()
    
    subjectFr_count = verify_content.count('subjectFr:')
    bodyFr_count = verify_content.count('bodyFr:')
    print(f'Verification: Found {subjectFr_count} subjectFr and {bodyFr_count} bodyFr entries')

if __name__ == '__main__':
    main()