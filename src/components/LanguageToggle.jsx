function LanguageToggle({ isFrench, onToggle }) {
  return (
    <button className="language-toggle" onClick={onToggle}>
      {isFrench ? 'EN' : 'FR'}
    </button>
  );
}

export default LanguageToggle;