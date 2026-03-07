/**
 * Feedback Modal Component for My Civic Voice
 * A clean, accessible feedback form modal
 */

import React, { useState, useEffect, useCallback } from 'react';

/**
 * FeedbackModal Component
 * 
 * @param {Object} props
 * @param {boolean} props.isOpen - Whether the modal is open
 * @param {Function} props.onClose - Callback to close the modal
 */
const FeedbackModal = ({ isOpen, onClose }) => {
  // Form state
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });
  
  // Submission state
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState(null); // 'success' | 'error' | null
  const [errorMessage, setErrorMessage] = useState('');
  
  // Validation errors
  const [validationErrors, setValidationErrors] = useState({});
  
  // Handle input changes
  const handleChange = useCallback((e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    
    // Clear validation error for this field
    if (validationErrors[name]) {
      setValidationErrors(prev => {
        const updated = { ...prev };
        delete updated[name];
        return updated;
      });
    }
  }, [validationErrors]);
  
  // Validate form
  const validateForm = useCallback(() => {
    const errors = {};
    
    if (!formData.name.trim()) {
      errors.name = 'Please enter your name';
    }
    
    if (!formData.email.trim()) {
      errors.email = 'Please enter your email address';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      errors.email = 'Please enter a valid email address';
    }
    
    if (!formData.message.trim()) {
      errors.message = 'Please enter your feedback';
    } else if (formData.message.trim().length < 10) {
      errors.message = 'Your message is too short (minimum 10 characters)';
    }
    
    setValidationErrors(errors);
    return Object.keys(errors).length === 0;
  }, [formData]);
  
  // Handle form submission
  const handleSubmit = useCallback(async (e) => {
    e.preventDefault();
    
    // Validate
    if (!validateForm()) {
      return;
    }
    
    setIsSubmitting(true);
    setSubmitStatus(null);
    setErrorMessage('');
    
    try {
      const response = await fetch('/api/feedback', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: formData.name.trim(),
          email: formData.email.trim(),
          message: formData.message.trim(),
          timestamp: new Date().toISOString(),
          source: 'My Civic Voice'
        }),
      });
      
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.message || `Server error: ${response.status}`);
      }
      
      // Success!
      setSubmitStatus('success');
      setFormData({ name: '', email: '', message: '' });
      
      // Auto-close after success
      setTimeout(() => {
        onClose();
        setSubmitStatus(null);
      }, 3000);
      
    } catch (error) {
      console.error('Feedback submission error:', error);
      setSubmitStatus('error');
      setErrorMessage(
        error.message || 'Something went wrong. Please try again later.'
      );
    } finally {
      setIsSubmitting(false);
    }
  }, [formData, validateForm, onClose]);
  
  // Handle escape key
  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === 'Escape' && isOpen && !isSubmitting) {
        onClose();
      }
    };
    
    if (isOpen) {
      document.addEventListener('keydown', handleEscape);
      document.body.style.overflow = 'hidden';
    }
    
    return () => {
      document.removeEventListener('keydown', handleEscape);
      document.body.style.overflow = '';
    };
  }, [isOpen, isSubmitting, onClose]);
  
  // Reset state when modal closes
  useEffect(() => {
    if (!isOpen) {
      setSubmitStatus(null);
      setErrorMessage('');
      setValidationErrors({});
    }
  }, [isOpen]);
  
  // Handle click outside modal
  const handleBackdropClick = useCallback((e) => {
    if (e.target === e.currentTarget && !isSubmitting) {
      onClose();
    }
  }, [isSubmitting, onClose]);
  
  // Don't render if not open
  if (!isOpen) return null;
  
  return (
    <div 
      className="feedback-modal-overlay" 
      onClick={handleBackdropClick}
      role="dialog"
      aria-modal="true"
      aria-labelledby="feedback-modal-title"
    >
      <div className="feedback-modal">
        {/* Close button */}
        <button
          type="button"
          className="feedback-modal-close"
          onClick={onClose}
          disabled={isSubmitting}
          aria-label="Close feedback form"
        >
          ×
        </button>
        
        {/* Header */}
        <div className="feedback-modal-header">
          <h2 id="feedback-modal-title">Send Feedback</h2>
          <p className="feedback-modal-note">
            Your feedback helps us improve this tool for all Canadians.
          </p>
        </div>
        
        {/* Content */}
        <div className="feedback-modal-content">
          {/* Success message */}
          {submitStatus === 'success' && (
            <div className="feedback-success" role="status">
              <div className="feedback-success-icon">✓</div>
              <h3>Thank you for your feedback!</h3>
              <p>We appreciate you taking the time to share your thoughts with us.</p>
            </div>
          )}
          
          {/* Error message */}
          {submitStatus === 'error' && (
            <div className="feedback-error" role="alert">
              <div className="feedback-error-icon">!</div>
              <h3>Something went wrong</h3>
              <p>{errorMessage}</p>
              <button
                type="button"
                className="feedback-retry-btn"
                onClick={() => setSubmitStatus(null)}
              >
                Try Again
              </button>
            </div>
          )}
          
          {/* Form */}
          {submitStatus !== 'success' && (
            <form onSubmit={handleSubmit} className="feedback-form" noValidate>
              {/* Name field */}
              <div className="feedback-field">
                <label htmlFor="feedback-name" className="feedback-label">
                  Name <span className="feedback-required">*</span>
                </label>
                <input
                  type="text"
                  id="feedback-name"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  className={`feedback-input ${validationErrors.name ? 'feedback-input-error' : ''}`}
                  placeholder="Your full name"
                  disabled={isSubmitting}
                  autoComplete="name"
                  required
                />
                {validationErrors.name && (
                  <span className="feedback-error-text" role="alert">
                    {validationErrors.name}
                  </span>
                )}
              </div>
              
              {/* Email field */}
              <div className="feedback-field">
                <label htmlFor="feedback-email" className="feedback-label">
                  Email <span className="feedback-required">*</span>
                </label>
                <input
                  type="email"
                  id="feedback-email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  className={`feedback-input ${validationErrors.email ? 'feedback-input-error' : ''}`}
                  placeholder="your.email@example.com"
                  disabled={isSubmitting}
                  autoComplete="email"
                  required
                />
                {validationErrors.email && (
                  <span className="feedback-error-text" role="alert">
                    {validationErrors.email}
                  </span>
                )}
              </div>
              
              {/* Message field */}
              <div className="feedback-field">
                <label htmlFor="feedback-message" className="feedback-label">
                  Message <span className="feedback-required">*</span>
                </label>
                <textarea
                  id="feedback-message"
                  name="message"
                  value={formData.message}
                  onChange={handleChange}
                  className={`feedback-textarea ${validationErrors.message ? 'feedback-input-error' : ''}`}
                  placeholder="Share your thoughts, suggestions, or report an issue..."
                  rows={5}
                  disabled={isSubmitting}
                  required
                />
                {validationErrors.message && (
                  <span className="feedback-error-text" role="alert">
                    {validationErrors.message}
                  </span>
                )}
              </div>
              
              {/* Submit button */}
              <button
                type="submit"
                className="feedback-submit-btn"
                disabled={isSubmitting}
              >
                {isSubmitting ? (
                  <>
                    <span className="feedback-spinner"></span>
                    Sending...
                  </>
                ) : (
                  'Send Feedback'
                )}
              </button>
            </form>
          )}
        </div>
      </div>
    </div>
  );
};

/**
 * FeedbackButton Component
 * Button that opens the feedback modal
 * 
 * @param {Object} props
 * @param {Function} props.onClick - Callback when button is clicked
 */
export const FeedbackButton = ({ onClick }) => (
  <button
    type="button"
    className="feedback-trigger-btn"
    onClick={onClick}
    aria-label="Send feedback about this website"
  >
    <svg 
      className="feedback-icon" 
      viewBox="0 0 24 24" 
      fill="none" 
      stroke="currentColor" 
      strokeWidth="2"
      aria-hidden="true"
    >
      <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
    </svg>
    Send Feedback
  </button>
);

/**
 * useFeedbackModal Hook
 * Custom hook to manage feedback modal state
 */
export const useFeedbackModal = () => {
  const [isOpen, setIsOpen] = useState(false);
  
  const openModal = useCallback(() => setIsOpen(true), []);
  const closeModal = useCallback(() => setIsOpen(false), []);
  const toggleModal = useCallback(() => setIsOpen(prev => !prev), []);
  
  return {
    isOpen,
    openModal,
    closeModal,
    toggleModal,
    Modal: FeedbackModal,
    Button: FeedbackButton
  };
};

export default FeedbackModal;

/* ============================================
   STYLES (include these in your CSS)
   ============================================

.feedback-modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(4px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    padding: 20px;
    animation: feedback-fade-in 0.2s ease;
}

@keyframes feedback-fade-in {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.feedback-modal {
    background: var(--bg-secondary, #ffffff);
    border-radius: 16px;
    max-width: 500px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
    animation: feedback-slide-up 0.3s ease;
}

@keyframes feedback-slide-up {
    from {
        opacity: 0;
        transform: translateY(20px) scale(0.95);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.feedback-modal-close {
    position: absolute;
    top: 16px;
    right: 16px;
    width: 36px;
    height: 36px;
    border: none;
    background: var(--bg-tertiary, #f5f5f5);
    border-radius: 50%;
    font-size: 24px;
    line-height: 1;
    color: var(--text-secondary, #666);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
}

.feedback-modal-close:hover {
    background: var(--accent-primary, #D96A1B);
    color: white;
}

.feedback-modal-close:focus {
    outline: 2px solid var(--accent-primary, #D96A1B);
    outline-offset: 2px;
}

.feedback-modal-header {
    padding: 28px 28px 16px;
    text-align: center;
}

.feedback-modal-header h2 {
    margin: 0 0 8px;
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--text-primary, #1a1a2e);
}

.feedback-modal-note {
    margin: 0;
    color: var(--text-secondary, #666);
    font-size: 0.9rem;
    line-height: 1.5;
}

.feedback-modal-content {
    padding: 0 28px 28px;
}

/* Form styles */
.feedback-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.feedback-field {
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.feedback-label {
    font-size: 0.9rem;
    font-weight: 500;
    color: var(--text-primary, #1a1a2e);
}

.feedback-required {
    color: #e74c3c;
}

.feedback-input,
.feedback-textarea {
    width: 100%;
    padding: 12px 16px;
    font-size: 1rem;
    font-family: inherit;
    border: 2px solid var(--border-color, #ddd);
    border-radius: 8px;
    background: var(--bg-primary, #fff);
    color: var(--text-primary, #1a1a2e);
    transition: all 0.2s ease;
}

.feedback-input:focus,
.feedback-textarea:focus {
    outline: none;
    border-color: var(--accent-primary, #D96A1B);
    box-shadow: 0 0 0 3px rgba(217, 106, 27, 0.15);
}

.feedback-input::placeholder,
.feedback-textarea::placeholder {
    color: var(--text-muted, #999);
}

.feedback-input-error {
    border-color: #e74c3c;
}

.feedback-input-error:focus {
    border-color: #e74c3c;
    box-shadow: 0 0 0 3px rgba(231, 76, 60, 0.15);
}

.feedback-textarea {
    resize: vertical;
    min-height: 120px;
}

.feedback-error-text {
    font-size: 0.8rem;
    color: #e74c3c;
}

/* Submit button */
.feedback-submit-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 100%;
    padding: 14px 24px;
    font-size: 1rem;
    font-weight: 600;
    font-family: inherit;
    color: white;
    background: linear-gradient(135deg, var(--accent-primary, #D96A1B), #B8560F);
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.feedback-submit-btn:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(217, 106, 27, 0.3);
}

.feedback-submit-btn:focus {
    outline: 2px solid var(--accent-primary, #D96A1B);
    outline-offset: 2px;
}

.feedback-submit-btn:disabled {
    opacity: 0.7;
    cursor: not-allowed;
    transform: none;
}

/* Spinner */
.feedback-spinner {
    width: 18px;
    height: 18px;
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-top-color: white;
    border-radius: 50%;
    animation: feedback-spin 0.8s linear infinite;
}

@keyframes feedback-spin {
    to {
        transform: rotate(360deg);
    }
}

/* Success message */
.feedback-success {
    text-align: center;
    padding: 40px 20px;
}

.feedback-success-icon {
    width: 60px;
    height: 60px;
    margin: 0 auto 16px;
    background: #27ae60;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    color: white;
    animation: feedback-success-pop 0.4s ease;
}

@keyframes feedback-success-pop {
    0% {
        transform: scale(0);
    }
    70% {
        transform: scale(1.1);
    }
    100% {
        transform: scale(1);
    }
}

.feedback-success h3 {
    margin: 0 0 8px;
    font-size: 1.25rem;
    color: var(--text-primary, #1a1a2e);
}

.feedback-success p {
    margin: 0;
    color: var(--text-secondary, #666);
}

/* Error message */
.feedback-error {
    text-align: center;
    padding: 40px 20px;
}

.feedback-error-icon {
    width: 60px;
    height: 60px;
    margin: 0 auto 16px;
    background: #e74c3c;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    font-weight: bold;
    color: white;
}

.feedback-error h3 {
    margin: 0 0 8px;
    font-size: 1.25rem;
    color: var(--text-primary, #1a1a2e);
}

.feedback-error p {
    margin: 0 0 20px;
    color: var(--text-secondary, #666);
}

.feedback-retry-btn {
    padding: 10px 24px;
    font-size: 0.9rem;
    font-weight: 500;
    font-family: inherit;
    color: var(--accent-primary, #D96A1B);
    background: transparent;
    border: 2px solid var(--accent-primary, #D96A1B);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.feedback-retry-btn:hover {
    background: var(--accent-primary, #D96A1B);
    color: white;
}

/* Trigger button */
.feedback-trigger-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    font-size: 0.9rem;
    font-weight: 500;
    font-family: inherit;
    color: var(--text-secondary, #666);
    background: var(--bg-secondary, #fff);
    border: 1px solid var(--border-color, #ddd);
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.feedback-trigger-btn:hover {
    background: var(--bg-hover, #f5f5f5);
    border-color: var(--accent-primary, #D96A1B);
    color: var(--accent-primary, #D96A1B);
}

.feedback-icon {
    width: 18px;
    height: 18px;
}

/* Responsive */
@media (max-width: 480px) {
    .feedback-modal {
        margin: 10px;
        max-height: 95vh;
    }
    
    .feedback-modal-header {
        padding: 20px 20px 12px;
    }
    
    .feedback-modal-content {
        padding: 0 20px 20px;
    }
    
    .feedback-modal-header h2 {
        font-size: 1.25rem;
    }
}

/* Dark mode support */
[data-theme="dark"] .feedback-modal {
    background: var(--bg-secondary, #162437);
}

[data-theme="dark"] .feedback-modal-header h2 {
    color: var(--text-primary, #e0e6ed);
}

[data-theme="dark"] .feedback-modal-note {
    color: var(--text-muted, #888);
}

[data-theme="dark"] .feedback-label {
    color: var(--text-primary, #e0e6ed);
}

[data-theme="dark"] .feedback-input,
[data-theme="dark"] .feedback-textarea {
    background: var(--bg-primary, #0E1A2B);
    border-color: var(--border-color, #2a3f5f);
    color: var(--text-primary, #e0e6ed);
}

[data-theme="dark"] .feedback-input::placeholder,
[data-theme="dark"] .feedback-textarea::placeholder {
    color: var(--text-muted, #888);
}

[data-theme="dark"] .feedback-modal-close {
    background: var(--bg-primary, #0E1A2B);
    color: var(--text-secondary, #aaa);
}

[data-theme="dark"] .feedback-modal-close:hover {
    background: var(--accent-primary, #00C2A8);
}

[data-theme="dark"] .feedback-success h3,
[data-theme="dark"] .feedback-error h3 {
    color: var(--text-primary, #e0e6ed);
}

[data-theme="dark"] .feedback-success p,
[data-theme="dark"] .feedback-error p {
    color: var(--text-secondary, #aaa);
}

[data-theme="dark"] .feedback-trigger-btn {
    background: var(--bg-secondary, #162437);
    border-color: var(--border-color, #2a3f5f);
    color: var(--text-secondary, #aaa);
}

[data-theme="dark"] .feedback-trigger-btn:hover {
    background: var(--bg-hover, #1e3a5f);
    border-color: var(--accent-primary, #00C2A8);
    color: var(--accent-primary, #00C2A8);
}

*/