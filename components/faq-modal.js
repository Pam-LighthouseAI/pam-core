/**
 * FAQ Modal Component for My Civic Voice
 * 
 * A modal component that displays FAQ content with collapsible/expandable questions.
 * Styled to match the existing site aesthetic (clean, modern, accessible).
 * 
 * Props:
 *   - isOpen: boolean - controls modal visibility
 *   - onClose: function - callback when modal is closed
 * 
 * Usage:
 *   <FAQModal isOpen={showFAQ} onClose={() => setShowFAQ(false)} />
 */

import React, { useState, useEffect, useCallback } from 'react';

// FAQ Data Array
const FAQ = [
  { 
    q: "Why do I need to know which level of government handles my issue?", 
    a: "Each level of government in Canada has different responsibilities. Contacting the wrong level wastes your time and delays resolution. Municipal handles local services, provincial handles healthcare and education, federal handles national matters."
  },
  { 
    q: "What's the difference between municipal, provincial, and federal government?", 
    a: "Municipal: cities and towns — local services, bylaws, property tax. Provincial: provinces and territories — healthcare, education, driver's licenses. Federal: all of Canada — taxes, defense, immigration, pensions."
  },
  { 
    q: "Why do some issues involve multiple levels?", 
    a: "Many issues cross boundaries. Housing: federal sets policy, provincial sets tenant laws, municipal enforces bylaws. We show you all levels involved so you can contact the right people."
  },
  { 
    q: "How do I find my specific representative?", 
    a: "Enter your postal code for the most accurate results. We use the Represent API from Open North to match your location to your elected officials at all three levels."
  },
  { 
    q: "What if I don't know my postal code?", 
    a: "You can select your city or province, but you'll only see general representatives (like your MP for the province) rather than your specific local representative."
  },
  { 
    q: "Why should I contact my representative?", 
    a: "Elected officials represent YOU. They need to hear from constituents to understand what matters to their community. Your voice influences their decisions and priorities."
  },
  { 
    q: "How should I write my message?", 
    a: "Be clear, specific, and personal. Describe how the issue affects you directly. Be respectful but firm. Include your contact information so they can respond."
  },
  { 
    q: "What if my representative doesn't respond?", 
    a: "Follow up after 2-3 weeks. Contact other representatives involved in the issue. You can also contact the relevant government department directly."
  },
  { 
    q: "Is my information stored?", 
    a: "No. This tool runs entirely in your browser. We don't store your name, email, or any information you enter. Your draft is saved locally on your device only."
  },
  { 
    q: "How can I help improve this tool?", 
    a: "Use the 'Send Feedback' button in the footer to share suggestions, report issues, or tell us what's working. We read every message."
  }
];

// Styles object for the modal
const styles = {
  // Modal overlay - covers the entire screen
  overlay: {
    position: 'fixed',
    inset: 0,
    backgroundColor: 'rgba(0, 0, 0, 0.6)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    zIndex: 1000,
    padding: '20px',
    backdropFilter: 'blur(4px)',
    animation: 'fadeIn 0.2s ease-out',
  },
  
  // Modal container
  modal: {
    backgroundColor: '#ffffff',
    borderRadius: '12px',
    boxShadow: '0 20px 60px rgba(0, 0, 0, 0.3)',
    maxWidth: '680px',
    width: '100%',
    maxHeight: '85vh',
    display: 'flex',
    flexDirection: 'column',
    animation: 'slideUp 0.3s ease-out',
    overflow: 'hidden',
  },
  
  // Modal header
  header: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: '24px 28px',
    borderBottom: '1px solid #e5e7eb',
    backgroundColor: '#f9fafb',
  },
  
  // Modal title
  title: {
    fontSize: '22px',
    fontWeight: '600',
    color: '#111827',
    margin: 0,
    display: 'flex',
    alignItems: 'center',
    gap: '10px',
  },
  
  // Close button
  closeButton: {
    background: 'none',
    border: 'none',
    cursor: 'pointer',
    padding: '8px',
    borderRadius: '8px',
    color: '#6b7280',
    fontSize: '24px',
    lineHeight: 1,
    transition: 'all 0.15s ease',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  
  // Modal content area (scrollable)
  content: {
    flex: 1,
    overflow: 'auto',
    padding: '0',
  },
  
  // FAQ list container
  faqList: {
    padding: '8px 0',
  },
  
  // Individual FAQ item
  faqItem: {
    borderBottom: '1px solid #f3f4f6',
  },
  
  // FAQ question button
  questionButton: {
    width: '100%',
    background: 'none',
    border: 'none',
    padding: '20px 28px',
    textAlign: 'left',
    cursor: 'pointer',
    display: 'flex',
    alignItems: 'flex-start',
    justifyContent: 'space-between',
    gap: '16px',
    transition: 'background-color 0.15s ease',
  },
  
  // Question text
  questionText: {
    fontSize: '16px',
    fontWeight: '500',
    color: '#1f2937',
    lineHeight: '1.5',
    flex: 1,
  },
  
  // Chevron icon container
  chevron: {
    color: '#9ca3af',
    fontSize: '20px',
    transition: 'transform 0.2s ease',
    flexShrink: 0,
    marginTop: '2px',
  },
  
  // FAQ answer container
  answer: {
    padding: '0 28px 20px 28px',
    fontSize: '15px',
    lineHeight: '1.7',
    color: '#4b5563',
  },
  
  // Answer text
  answerText: {
    margin: 0,
    backgroundColor: '#f9fafb',
    padding: '16px 20px',
    borderRadius: '8px',
    borderLeft: '3px solid #3b82f6',
  },
  
  // Footer section
  footer: {
    padding: '20px 28px',
    borderTop: '1px solid #e5e7eb',
    backgroundColor: '#f9fafb',
    textAlign: 'center',
  },
  
  // Footer text
  footerText: {
    fontSize: '14px',
    color: '#6b7280',
    margin: 0,
  },
};

// Individual FAQ Item Component
function FAQItem({ question, answer, isOpen, onClick }) {
  return (
    <div style={styles.faqItem}>
      <button
        onClick={onClick}
        style={styles.questionButton}
        aria-expanded={isOpen}
        aria-controls={`faq-answer-${question.slice(0, 20).replace(/\s+/g, '-')}`}
      >
        <span style={styles.questionText}>{question}</span>
        <span 
          style={{
            ...styles.chevron,
            transform: isOpen ? 'rotate(180deg)' : 'rotate(0deg)',
          }}
        >
          ▼
        </span>
      </button>
      {isOpen && (
        <div 
          style={styles.answer}
          id={`faq-answer-${question.slice(0, 20).replace(/\s+/g, '-')}`}
          role="region"
        >
          <p style={styles.answerText}>{answer}</p>
        </div>
      )}
    </div>
  );
}

// Main FAQ Modal Component
function FAQModal({ isOpen, onClose }) {
  // Track which FAQ items are expanded
  const [expandedItems, setExpandedItems] = useState(new Set());
  
  // Handle keyboard events for accessibility
  const handleKeyDown = useCallback((event) => {
    if (event.key === 'Escape' && isOpen) {
      onClose();
    }
  }, [isOpen, onClose]);
  
  // Add/remove keyboard listener
  useEffect(() => {
    if (isOpen) {
      document.addEventListener('keydown', handleKeyDown);
      // Prevent body scroll when modal is open
      document.body.style.overflow = 'hidden';
    }
    return () => {
      document.removeEventListener('keydown', handleKeyDown);
      document.body.style.overflow = '';
    };
  }, [isOpen, handleKeyDown]);
  
  // Toggle a FAQ item's expanded state
  const toggleItem = (index) => {
    setExpandedItems(prev => {
      const newSet = new Set(prev);
      if (newSet.has(index)) {
        newSet.delete(index);
      } else {
        newSet.add(index);
      }
      return newSet;
    });
  };
  
  // Handle clicking outside the modal
  const handleOverlayClick = (event) => {
    if (event.target === event.currentTarget) {
      onClose();
    }
  };
  
  // Don't render if not open
  if (!isOpen) return null;
  
  return (
    <div 
      style={styles.overlay} 
      onClick={handleOverlayClick}
      role="dialog"
      aria-modal="true"
      aria-labelledby="faq-modal-title"
    >
      <div style={styles.modal}>
        {/* Header */}
        <div style={styles.header}>
          <h2 style={styles.title} id="faq-modal-title">
            <span role="img" aria-label="Question mark">❓</span>
            Frequently Asked Questions
          </h2>
          <button
            onClick={onClose}
            style={styles.closeButton}
            aria-label="Close FAQ modal"
            onMouseEnter={(e) => {
              e.currentTarget.style.backgroundColor = '#f3f4f6';
              e.currentTarget.style.color = '#111827';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.backgroundColor = 'transparent';
              e.currentTarget.style.color = '#6b7280';
            }}
          >
            ✕
          </button>
        </div>
        
        {/* FAQ Content */}
        <div style={styles.content}>
          <div style={styles.faqList}>
            {FAQ.map((item, index) => (
              <FAQItem
                key={index}
                question={item.q}
                answer={item.a}
                isOpen={expandedItems.has(index)}
                onClick={() => toggleItem(index)}
              />
            ))}
          </div>
        </div>
        
        {/* Footer */}
        <div style={styles.footer}>
          <p style={styles.footerText}>
            Can't find what you're looking for? Use the{' '}
            <strong>Send Feedback</strong> button in the footer to ask a question.
          </p>
        </div>
      </div>
      
      {/* Inline keyframe animations */}
      <style>{`
        @keyframes fadeIn {
          from {
            opacity: 0;
          }
          to {
            opacity: 1;
          }
        }
        
        @keyframes slideUp {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        
        /* Hover state for question buttons */
        .faq-question-button:hover {
          background-color: #f9fafb;
        }
        
        /* Focus styles for accessibility */
        .faq-question-button:focus {
          outline: 2px solid #3b82f6;
          outline-offset: -2px;
        }
        
        /* Scrollbar styling */
        .faq-content::-webkit-scrollbar {
          width: 8px;
        }
        
        .faq-content::-webkit-scrollbar-track {
          background: #f3f4f6;
        }
        
        .faq-content::-webkit-scrollbar-thumb {
          background: #d1d5db;
          border-radius: 4px;
        }
        
        .faq-content::-webkit-scrollbar-thumb:hover {
          background: #9ca3af;
        }
      `}</style>
    </div>
  );
}

// Export the component
export default FAQModal;

// Also export named for flexibility
export { FAQModal, FAQ };