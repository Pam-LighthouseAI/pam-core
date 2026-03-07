// Opening lines for My Civic Voice

const OPENING_LINES = {
  urgent: {
    infrastructure: "I'm reaching out because something needs to change — and soon.",
    healthcare: "I'm writing because my health — or my family's health — depends on this.",
    education: "I'm contacting you because our children's education can't wait.",
    housing: "I'm writing because my housing situation has become urgent.",
    environment: "I'm reaching out because this environmental issue is affecting my health and safety now.",
    safety: "I'm contacting you because I don't feel safe in my own community.",
    employment: "I'm writing because my livelihood is at stake.",
    social: "I'm reaching out because I'm struggling to meet basic needs.",
    taxes: "I'm writing because this tax situation is causing real hardship.",
    immigration: "I'm contacting you because my future — and my family's future — hangs in the balance.",
    consumer: "I'm writing because I've been treated unfairly and I need help.",
    indigenous: "I'm reaching out because this matter requires urgent attention.",
    seniors: "I'm writing because seniors in our community are being left behind.",
    veterans: "I'm contacting you because veterans deserve better than what we're receiving.",
    disability: "I'm writing because accessibility isn't optional — it's essential.",
    youth: "I'm reaching out because young people's futures are at stake.",
    agriculture: "I'm writing because farming families in our region are struggling.",
    utilities: "I'm contacting you because essential services shouldn't be this hard to access.",
    family: "I'm writing because my family is going through something difficult.",
    arts: "I'm reaching out because arts and culture in our community need support now."
  },
  concerned: {
    infrastructure: "I've been thinking about an issue that affects our whole community.",
    healthcare: "I want to share a healthcare concern that I think matters to many constituents.",
    education: "I'm writing about an education issue that affects families in our riding.",
    housing: "I'd like to bring a housing concern to your attention.",
    environment: "I'm writing about an environmental matter that I believe needs attention.",
    safety: "I want to raise a public safety concern that's been on my mind.",
    employment: "I'm writing about a workplace issue that affects workers in our community.",
    social: "I'd like to share a concern about social services that help vulnerable people.",
    taxes: "I'm writing about a tax matter that I think could be improved.",
    immigration: "I want to share my immigration experience and what would help.",
    consumer: "I'm writing about a consumer issue that I think needs attention.",
    indigenous: "I'd like to bring an Indigenous affairs matter to your attention.",
    seniors: "I'm writing about an issue that affects seniors in our community.",
    veterans: "I want to share a concern about services for veterans.",
    disability: "I'm writing about accessibility and inclusion in our community.",
    youth: "I'd like to raise an issue affecting young people in our riding.",
    agriculture: "I'm writing about challenges facing farmers and rural communities.",
    utilities: "I want to share a concern about utility services in our area.",
    family: "I'm writing about a family law matter that affects many families.",
    arts: "I'd like to share thoughts on arts and culture in our community."
  },
  hopeful: {
    infrastructure: "I believe we can make our community better, and I have an idea.",
    healthcare: "I'm writing because I believe we can improve healthcare for everyone.",
    education: "I'm sharing this because I believe in better education for all our children.",
    housing: "I'm reaching out because I believe affordable housing is achievable.",
    environment: "I'm writing because I believe we can protect what matters.",
    safety: "I'm contacting you because I believe we can make our community safer.",
    employment: "I'm writing because I believe workers deserve fair treatment.",
    social: "I'm reaching out because I believe we can do better for those in need.",
    taxes: "I'm writing because I believe tax fairness benefits everyone.",
    immigration: "I'm contacting you because I believe Canada can do better.",
    consumer: "I'm writing because I believe consumers deserve protection.",
    indigenous: "I'm reaching out because I believe in a better path forward.",
    seniors: "I'm writing because I believe we can better support our seniors.",
    veterans: "I'm contacting you because I believe we owe our veterans more.",
    disability: "I'm writing because I believe in a fully accessible Canada.",
    youth: "I'm reaching out because I believe in investing in young people.",
    agriculture: "I'm writing because I believe in supporting our agricultural communities.",
    utilities: "I'm contacting you because I believe reliable services are achievable.",
    family: "I'm writing because I believe families deserve support.",
    arts: "I'm reaching out because I believe arts and culture enrich all our lives."
  },
  frustrated: {
    infrastructure: "I'm writing because I've tried everything else and nothing changes.",
    healthcare: "I'm contacting you because the healthcare system is failing people like me.",
    education: "I'm writing because our education system isn't working for my family.",
    housing: "I'm reaching out because I'm fed up with this housing situation.",
    environment: "I'm writing because I'm tired of seeing this environmental damage ignored.",
    safety: "I'm contacting you because I've reported this before and nothing happened.",
    employment: "I'm writing because workers are being treated unfairly and it needs to stop.",
    social: "I'm reaching out because the system isn't working for people who need help.",
    taxes: "I'm writing because this tax situation is unfair and needs to be fixed.",
    immigration: "I'm contacting you because this immigration process is broken.",
    consumer: "I'm writing because companies shouldn't be allowed to treat people this way.",
    indigenous: "I'm reaching out because promises keep being made and broken.",
    seniors: "I'm writing because seniors are being neglected and it's unacceptable.",
    veterans: "I'm contacting you because veterans aren't getting what they were promised.",
    disability: "I'm writing because accessibility is still being treated as optional.",
    youth: "I'm reaching out because young people keep being overlooked.",
    agriculture: "I'm writing because farmers are struggling and no one is listening.",
    utilities: "I'm contacting you because utility companies have too much power.",
    family: "I'm writing because the family law system isn't protecting families.",
    arts: "I'm reaching out because arts and culture keep getting cut."
  }
};

// CLOSING LINES - Varied by tone
const CLOSING_LINES = {
  urgent: "I'm asking for your help because this can't wait. Please let me know what action you can take.",
  concerned: "I'd appreciate your thoughts on this matter and any steps you can take to address it.",
  hopeful: "I believe this is something we can improve together. I'd welcome the chance to discuss it further.",
  frustrated: "I expect better, and I'm asking you to take this seriously. Please respond with concrete action."
};

// CLOSING LINES - FRENCH VERSIONS
const CLOSING_LINES_FR = {
  urgent: "Je demande votre aide car cela ne peut pas attendre. Veuillez me dire quelle action vous pouvez entreprendre.",
  concerned: "J'apprécierais vos réflexions sur cette question et les mesures que vous pourriez prendre.",
  hopeful: "Je crois que nous pouvons améliorer cela ensemble. Je serais heureux d'en discuter davantage.",
  frustrated: "J'attends mieux, et je vous demande de prendre cela au sérieux. Veuillez répondre avec des actions concrètes."
};

// OPENING LINES - FRENCH



export { OPENING_LINES, OPENING_LINES_FR };
