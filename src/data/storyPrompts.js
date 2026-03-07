// Story prompts for My Civic Voice

const STORY_PROMPTS = {
  infrastructure: [
    "How does this issue affect your daily commute or travel?",
    "Have you or someone you know been injured or put at risk?",
    "How long has this been a problem?",
    "What have you tried to do about it before?"
  ],
  healthcare: [
    "How has this affected your health or your family's health?",
    "Have you experienced delays or barriers to care?",
    "What would better access mean for you?",
    "How are others in your community affected?"
  ],
  education: [
    "How is this affecting your child's learning or your own education?",
    "What opportunities are being missed?",
    "How does this compare to other schools or regions?",
    "What would an ideal solution look like for your family?"
  ],
  housing: [
    "How is this housing situation affecting your daily life?",
    "Are you worried about losing your home or finding affordable housing?",
    "How much of your income goes to housing costs?",
    "Have you tried to resolve this with your landlord or the city?"
  ],
  environment: [
    "How does this environmental issue affect your health or quality of life?",
    "Are there places you can no longer enjoy because of this?",
    "How does this impact your children or future generations?",
    "What changes have you noticed over time?"
  ],
  safety: [
    "Have you or someone you know been directly affected?",
    "How has this changed your sense of safety in your community?",
    "What would make you feel safer?",
    "Have you reported this before? What happened?"
  ],
  employment: [
    "How has this workplace issue affected you personally?",
    "Are others at your workplace facing the same problem?",
    "Have you tried to address this internally? What happened?",
    "What would fair treatment look like?"
  ],
  social: [
    "How has this affected your ability to meet basic needs?",
    "What barriers have you encountered when seeking help?",
    "How would resolving this change your life?",
    "What would you want decision-makers to understand?"
  ],
  taxes: [
    "How does this tax issue affect your household budget?",
    "Are you facing penalties or disputes that seem unfair?",
    "What would a fair resolution look like?",
    "Have you tried to resolve this through normal channels?"
  ],
  immigration: [
    "What is your current situation and what are you hoping for?",
    "How has the wait or uncertainty affected your life and family?",
    "What would it mean for you to have this resolved?",
    "Have you encountered specific barriers in the process?"
  ],
  consumer: [
    "What did you purchase or sign up for, and what went wrong?",
    "How much money or time have you lost?",
    "Have you tried to resolve this with the company?",
    "What would a fair resolution look like?"
  ],
  indigenous: [
    "How does this issue affect you or your community?",
    "What would meaningful action look like?",
    "What historical context should decision-makers understand?",
    "What changes would make the biggest difference?"
  ],
  seniors: [
    "How has this issue affected your daily life or wellbeing?",
    "Are you able to access the services or support you need?",
    "What would help you live more independently or securely?",
    "Have you tried other programs or services?"
  ],
  veterans: [
    "What service did you provide and what are you seeking?",
    "How has this issue affected your transition to civilian life?",
    "What benefits or recognition are you entitled to?",
    "Have you encountered barriers in the system?"
  ],
  disability: [
    "How does this accessibility issue affect your daily life?",
    "What barriers do you face that others may not see?",
    "What would meaningful inclusion look like?",
    "Have you raised this before? What happened?"
  ],
  youth: [
    "How is this issue affecting your education or future?",
    "What opportunities are you missing out on?",
    "What would help you succeed?",
    "How are other young people in your situation affected?"
  ],
  agriculture: [
    "How is this affecting your farm or rural livelihood?",
    "What support would help you most?",
    "How does this compare to support in other regions?",
    "What would sustainable change look like?"
  ],
  utilities: [
    "How are these utility costs or issues affecting your household?",
    "Have you experienced service problems or billing disputes?",
    "What would fair and reliable service look like?",
    "Have you tried to resolve this with the provider?"
  ],
  family: [
    "How is this affecting your family's wellbeing?",
    "What outcome are you seeking for your children or family?",
    "Have you tried other avenues for resolution?",
    "What would stability look like for your family?"
  ],
  arts: [
    "How does this affect your ability to create or access culture?",
    "What opportunities are being lost?",
    "How would support for arts benefit your community?",
    "What programs or spaces do you need?"
  ],
  lgbtq: [
    "How has this issue affected your sense of safety or belonging?",
    "Have you experienced discrimination or barriers?",
    "What would meaningful support look like for you or your community?",
    "How does this impact your daily life or relationships?"
  ],
  women: [
    "How has this issue affected you or the women in your life?",
    "What barriers have you faced because of gender?",
    "What would equality or safety look like in this situation?",
    "Have you tried to address this through other channels?"
  ],
  mentalhealth: [
    "How has this affected your mental health or wellbeing?",
    "Have you been able to access the support you need?",
    "What would better mental health support mean for you?",
    "How are others in your community affected?"
  ],
  substance: [
    "How has substance use affected you or someone you care about?",
    "What barriers have you faced getting help?",
    "What kind of support would make a difference?",
    "How has this impacted your family or community?"
  ],
  transportation: [
    "How does this transportation issue affect your daily life?",
    "Are you able to get where you need to go?",
    "What would better transportation mean for you?",
    "Have you raised this before? What happened?"
  ],
  digital: [
    "How has this digital rights issue affected you?",
    "What happened to your data or privacy?",
    "What would fair treatment look like?",
    "Have you tried to resolve this with the company?"
  ],
  animals: [
    "How does this animal welfare issue affect you or your community?",
    "What have you witnessed or experienced?",
    "What would proper protection look like?",
    "Have you reported this before?"
  ],
  sports: [
    "How does this affect your ability to participate in sports or recreation?",
    "What opportunities are you or your family missing?",
    "What would better access look like?",
    "How does this impact your community?"
  ],
  religion: [
    "How has this affected your ability to practice your faith?",
    "Have you experienced discrimination or barriers?",
    "What would religious accommodation look like?",
    "How does this impact your community?"
  ],
  volunteer: [
    "How does this affect your ability to volunteer or participate?",
    "What community need are you trying to address?",
    "What support would help your volunteer efforts?",
    "What impact would better resources have?"
  ],
  legalaid: [
    "What legal issue are you facing?",
    "Have you been able to get legal help?",
    "What would access to justice mean for you?",
    "How is this affecting your life right now?"
  ],
  pensions: [
    "How is this pension or retirement issue affecting you?",
    "What benefits are you entitled to?",
    "Have you tried to resolve this through normal channels?",
    "What would a fair resolution look like?"
  ],
  childcare: [
    "How is the childcare situation affecting your family?",
    "What barriers have you faced finding care?",
    "What would affordable childcare mean for you?",
    "How does this impact your work or education?"
  ],
  food: [
    "How has food insecurity affected you or your family?",
    "What barriers do you face accessing healthy food?",
    "What would food security look like for you?",
    "How does this affect your daily life?"
  ],
  emergency: [
    "What emergency situation are you dealing with?",
    "How has the response been?",
    "What support do you need?",
    "How has this affected your sense of safety?"
  ],
  humanrights: [
    "How has this human rights issue affected you?",
    "What discrimination or violation did you experience?",
    "What would justice look like?",
    "Have you tried to address this elsewhere?"
  ]
};

// STORY PROMPTS - FRENCH

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

// OPENING LINES

export { STORY_PROMPTS, STORY_PROMPTS_FR };
