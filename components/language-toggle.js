/**
 * LanguageToggle Component for My Civic Voice
 * A clean, modern pill-shaped toggle button for switching between English and French
 */

import React, { useState, useEffect } from 'react';

/**
 * Detects browser language preference
 * @returns {boolean} true if French is preferred, false otherwise
 */
const detectBrowserLanguage = () => {
  // Check localStorage first
  const savedLanguage = localStorage.getItem('myCivicVoice_language');
  if (savedLanguage !== null) {
    return savedLanguage === 'fr';
  }
  
  // Detect from browser
  const browserLang = navigator.language || navigator.userLanguage || 'en';
  return browserLang.toLowerCase().startsWith('fr');
};

/**
 * LanguageToggle Component
 * @param {Object} props
 * @param {Function} props.onLanguageChange - Callback when language changes, receives boolean (true = French)
 */
const LanguageToggle = ({ onLanguageChange }) => {
  const [isFrench, setIsFrench] = useState(() => detectBrowserLanguage());

  // Initialize and notify parent of initial language
  useEffect(() => {
    const detectedFrench = detectBrowserLanguage();
    setIsFrench(detectedFrench);
    if (onLanguageChange) {
      onLanguageChange(detectedFrench);
    }
  }, []);

  /**
   * Toggles the current language between English and French
   */
  const toggleLanguage = () => {
    const newIsFrench = !isFrench;
    setIsFrench(newIsFrench);
    
    // Store preference in localStorage
    localStorage.setItem('myCivicVoice_language', newIsFrench ? 'fr' : 'en');
    
    // Notify parent component
    if (onLanguageChange) {
      onLanguageChange(newIsFrench);
    }
  };

  return (
    <button
      className="language-toggle"
      onClick={toggleLanguage}
      aria-label={isFrench ? 'Switch to English' : 'Switch to French'}
      title={isFrench ? 'Switch to English' : 'Switch to French'}
    >
      {isFrench ? 'EN' : 'FR'}
    </button>
  );
};

// CSS Styles for the Language Toggle
const styles = `
.language-toggle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 42px;
  height: 32px;
  padding: 0 12px;
  margin-left: 16px;
  
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.5px;
  color: #ffffff;
  
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
  border: none;
  border-radius: 16px;
  cursor: pointer;
  
  transition: all 0.2s ease-in-out;
  box-shadow: 0 2px 4px rgba(59, 130, 246, 0.3);
}

.language-toggle:hover {
  background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(59, 130, 246, 0.4);
}

.language-toggle:active {
  transform: translateY(0);
  box-shadow: 0 1px 2px rgba(59, 130, 246, 0.3);
}

.language-toggle:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .language-toggle {
    background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%);
    box-shadow: 0 2px 4px rgba(79, 70, 229, 0.3);
  }
  
  .language-toggle:hover {
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
    box-shadow: 0 4px 8px rgba(79, 70, 229, 0.4);
  }
  
  .language-toggle:focus {
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.5);
  }
}

/* Mobile responsive */
@media (max-width: 480px) {
  .language-toggle {
    min-width: 38px;
    height: 28px;
    padding: 0 10px;
    font-size: 13px;
    margin-left: 10px;
  }
}
`;

// Function to inject styles into the document
const injectStyles = () => {
  if (typeof document === 'undefined') return;
  
  const styleId = 'language-toggle-styles';
  if (!document.getElementById(styleId)) {
    const styleElement = document.createElement('style');
    styleElement.id = styleId;
    styleElement.textContent = styles;
    document.head.appendChild(styleElement);
  }
};

// Auto-inject styles when component is loaded
if (typeof window !== 'undefined') {
  injectStyles();
}

export { LanguageToggle, toggleLanguage, detectBrowserLanguage, styles };
export default LanguageToggle;