// Email templates for My Civic Voice

const TEMPLATES = {
  infrastructure: {
    subject: "Infrastructure & Transportation Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant l'infrastructure et les transports : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  healthcare: {
    subject: "Healthcare Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les soins de santé : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  education: {
    subject: "Education Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant l'éducation : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  housing: {
    subject: "Housing & Development Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant le logement et l'amenagement : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  environment: {
    subject: "Environment & Climate Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant l'environnement et le climat : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  safety: {
    subject: "Public Safety & Justice Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant la sécurité publique et la justice : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  employment: {
    subject: "Employment & Labour Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant l'emploi et le travail : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  social: {
    subject: "Social Services & Benefits Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les services sociaux et les prestations : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  taxes: {
    subject: "Taxes & Finance Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les impôts et les finances : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  immigration: {
    subject: "Immigration & Citizenship Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant l'immigration et la citoyenneté : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  consumer: {
    subject: "Consumer & Digital Rights Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les droits des consommateurs : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  indigenous: {
    subject: "Indigenous Affairs Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les affaires autochtones : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  seniors: {
    subject: "Seniors' Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les aînés : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  veterans: {
    subject: "Veterans Affairs Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les anciens combattants : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  disability: {
    subject: "Accessibility & Disability Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant l'accessibilité et le handicap : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  youth: {
    subject: "Youth & Student Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant la jeunesse et les etudiants : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  agriculture: {
    subject: "Agriculture & Rural Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant l'agriculture et le milieu rural : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  utilities: {
    subject: "Utilities Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les services publics : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  family: {
    subject: "Family Law Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant le droit de la famille : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  arts: {
    subject: "Arts & Culture Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les arts et la culture : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  lgbtq: {
    subject: "LGBTQ+ Rights Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les droits LGBTQ+ : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  women: {
    subject: "Women's Rights Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les droits des femmes : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  mentalhealth: {
    subject: "Mental Health Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant la santé mentale : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  substance: {
    subject: "Substance Use & Addiction Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant l'usage de substances et les dépendances : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  transportation: {
    subject: "Transportation Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les transports : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  digital: {
    subject: "Digital Rights Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les droits numeriques : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  animals: {
    subject: "Animal Welfare Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant le bien-etre animal : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  sports: {
    subject: "Sports & Recreation Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant le sport et les loisirs : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  religion: {
    subject: "Religion & Faith Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant la religion et la foi : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  volunteer: {
    subject: "Volunteer & Community Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant le bénévolat et la communauté : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  legalaid: {
    subject: "Legal Aid Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant l'aide juridique : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  pensions: {
    subject: "Pensions & Retirement Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les retraites et les pensions : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  childcare: {
    subject: "Childcare Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant la garde d'enfants : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  food: {
    subject: "Food Security Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant la sécurité alimentaire : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  emergency: {
    subject: "Emergency Services Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les services d'urgence : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  },
  humanrights: {
    subject: "Human Rights Concern: {{ISSUE}}",
    subjectFr: "Préoccupation concernant les droits de la personne : {{ISSUE}}",
    body: `Dear {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`,
    bodyFr: `Cher {{REP_NAME}},

{{OPENING}}

{{STORY}}

{{CONTEXT}}

{{CLOSING}}

{{SIGNATURE}}`
  }
};

// LANGUAGE TOGGLE

export default TEMPLATES;
