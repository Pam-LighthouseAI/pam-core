/**
 * Draft Saving Functionality for My Civic Voice
 * 
 * Provides localStorage-based draft management for form data,
 * including save, load, clear, and auto-save capabilities.
 */

const DRAFT_STORAGE_KEY = 'mycivicvoice_draft';
const AUTO_SAVE_DEBOUNCE_MS = 1000;

/**
 * Form field keys that are saved/loaded as drafts
 */
const DRAFT_FIELDS = [
  'userName',
  'userEmail',
  'userPhone',
  'userLocation',
  'userDetail',
  'selectedIssue',
  'selectedCategory'
];

/**
 * Saves the current form state to localStorage
 * @param {Object} formData - Object containing form field values
 * @returns {boolean} - True if save was successful
 */
function saveDraft(formData) {
  try {
    const draftData = {};
    
    // Extract only the fields we want to save
    DRAFT_FIELDS.forEach(field => {
      if (formData && formData[field] !== undefined) {
        draftData[field] = formData[field];
      }
    });
    
    // Add timestamp for when the draft was saved
    draftData.savedAt = new Date().toISOString();
    
    localStorage.setItem(DRAFT_STORAGE_KEY, JSON.stringify(draftData));
    console.log('Draft saved successfully');
    return true;
  } catch (error) {
    console.error('Error saving draft:', error);
    return false;
  }
}

/**
 * Loads a saved draft from localStorage
 * @returns {Object|null} - Returns the saved draft object or null if no draft exists
 */
function loadDraft() {
  try {
    const draftJson = localStorage.getItem(DRAFT_STORAGE_KEY);
    
    if (!draftJson) {
      return null;
    }
    
    const draftData = JSON.parse(draftJson);
    
    // Verify it's a valid draft with at least one field
    const hasValidFields = DRAFT_FIELDS.some(field => 
      draftData[field] !== undefined && draftData[field] !== ''
    );
    
    if (!hasValidFields) {
      return null;
    }
    
    return draftData;
  } catch (error) {
    console.error('Error loading draft:', error);
    return null;
  }
}

/**
 * Removes the draft from localStorage
 * @returns {boolean} - True if clear was successful
 */
function clearDraft() {
  try {
    localStorage.removeItem(DRAFT_STORAGE_KEY);
    console.log('Draft cleared successfully');
    return true;
  } catch (error) {
    console.error('Error clearing draft:', error);
    return false;
  }
}

/**
 * Checks if a saved draft exists
 * @returns {boolean} - True if a draft exists in localStorage
 */
function hasDraft() {
  try {
    const draftJson = localStorage.getItem(DRAFT_STORAGE_KEY);
    
    if (!draftJson) {
      return false;
    }
    
    const draftData = JSON.parse(draftJson);
    
    // Check if any of the tracked fields have content
    return DRAFT_FIELDS.some(field => 
      draftData[field] !== undefined && draftData[field] !== ''
    );
  } catch (error) {
    console.error('Error checking draft:', error);
    return false;
  }
}

/**
 * Creates a debounced auto-save function
 * @param {Function} getFormData - Function that returns current form data
 * @param {number} delay - Debounce delay in milliseconds
 * @returns {Function} - Debounced save function
 */
function createAutoSave(getFormData, delay = AUTO_SAVE_DEBOUNCE_MS) {
  let timeoutId = null;
  
  const debouncedSave = () => {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }
    
    timeoutId = setTimeout(() => {
      const formData = getFormData();
      if (formData) {
        saveDraft(formData);
      }
    }, delay);
  };
  
  // Return both the trigger and a cancel function
  return {
    trigger: debouncedSave,
    cancel: () => {
      if (timeoutId) {
        clearTimeout(timeoutId);
        timeoutId = null;
      }
    }
  };
}

/**
 * Gets form data from DOM elements
 * @returns {Object} - Object containing form field values
 */
function getFormDataFromDOM() {
  const formData = {};
  
  DRAFT_FIELDS.forEach(field => {
    const element = document.getElementById(field) || 
                    document.querySelector(`[name="${field}"]`);
    
    if (element) {
      formData[field] = element.value || '';
    }
  });
  
  return formData;
}

/**
 * Populates form fields from draft data
 * @param {Object} draftData - Draft data to populate
 */
function populateFormFromDraft(draftData) {
  if (!draftData) return;
  
  DRAFT_FIELDS.forEach(field => {
    if (draftData[field] !== undefined) {
      const element = document.getElementById(field) || 
                      document.querySelector(`[name="${field}"]`);
      
      if (element) {
        element.value = draftData[field];
        
        // Trigger change event for any listeners
        const event = new Event('change', { bubbles: true });
        element.dispatchEvent(event);
      }
    }
  });
}

// ============================================
// REACT COMPONENTS (if React is available)
// ============================================

/**
 * Save Draft Button Component
 * Renders a "Save Draft" button for the email template modal
 * 
 * Usage:
 * <SaveDraftButton formData={currentFormData} onSave={handleSave} />
 */
function createSaveDraftButton() {
  // This function returns JSX for React environments
  // For vanilla JS, use the button HTML directly
  return `
    <button type="button" class="save-draft-btn" onclick="handleSaveDraftClick()">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path>
        <polyline points="17 21 17 13 7 13 7 21"></polyline>
        <polyline points="7 3 7 8 15 8"></polyline>
      </svg>
      Save Draft
    </button>
  `;
}

/**
 * Draft Prompt Component
 * Shows on page load if a draft exists, asking user to restore or dismiss
 * 
 * @param {Object} props - Component props
 * @param {Function} props.onRestore - Callback when user clicks "Restore Draft"
 * @param {Function} props.onDismiss - Callback when user clicks "Start Fresh"
 */
class DraftPrompt {
  constructor(options = {}) {
    this.onRestore = options.onRestore || (() => {});
    this.onDismiss = options.onDismiss || (() => {});
    this.container = null;
  }
  
  /**
   * Creates and returns the prompt HTML element
   */
  render() {
    const promptHTML = `
      <div class="draft-prompt-overlay" id="draftPromptOverlay">
        <div class="draft-prompt-container">
          <div class="draft-prompt-icon">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
              <polyline points="14 2 14 8 20 8"></polyline>
              <line x1="16" y1="13" x2="8" y2="13"></line>
              <line x1="16" y1="17" x2="8" y2="17"></line>
              <polyline points="10 9 9 9 8 9"></polyline>
            </svg>
          </div>
          <h3 class="draft-prompt-title">Saved Draft Found</h3>
          <p class="draft-prompt-message">We found a saved draft. Would you like to restore it?</p>
          <div class="draft-prompt-timestamp" id="draftTimestamp"></div>
          <div class="draft-prompt-buttons">
            <button type="button" class="draft-prompt-btn draft-prompt-restore" id="restoreDraftBtn">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="1 4 1 10 7 10"></polyline>
                <path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"></path>
              </svg>
              Restore Draft
            </button>
            <button type="button" class="draft-prompt-btn draft-prompt-dismiss" id="dismissDraftBtn">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
              Start Fresh
            </button>
          </div>
        </div>
      </div>
    `;
    
    return promptHTML;
  }
  
  /**
   * Inserts the prompt into the DOM and attaches event listeners
   */
  show() {
    // Remove any existing prompt
    this.hide();
    
    // Create container
    const wrapper = document.createElement('div');
    wrapper.innerHTML = this.render();
    this.container = wrapper.firstElementChild;
    
    // Add timestamp if available
    const draft = loadDraft();
    if (draft && draft.savedAt) {
      const timestampEl = this.container.querySelector('#draftTimestamp');
      if (timestampEl) {
        const savedDate = new Date(draft.savedAt);
        timestampEl.textContent = `Last saved: ${savedDate.toLocaleString()}`;
      }
    }
    
    // Add to DOM
    document.body.appendChild(this.container);
    
    // Attach event listeners
    const restoreBtn = this.container.querySelector('#restoreDraftBtn');
    const dismissBtn = this.container.querySelector('#dismissDraftBtn');
    
    restoreBtn.addEventListener('click', () => {
      this.onRestore();
      this.hide();
    });
    
    dismissBtn.addEventListener('click', () => {
      clearDraft();
      this.onDismiss();
      this.hide();
    });
    
    // Animate in
    requestAnimationFrame(() => {
      this.container.classList.add('visible');
    });
  }
  
  /**
   * Removes the prompt from the DOM
   */
  hide() {
    const existing = document.getElementById('draftPromptOverlay');
    if (existing) {
      existing.classList.remove('visible');
      setTimeout(() => existing.remove(), 300);
    }
    this.container = null;
  }
}

/**
 * Check for draft on page load and show prompt if exists
 * @param {Function} onRestore - Callback when user restores draft
 * @param {Function} onDismiss - Callback when user dismisses draft
 */
function checkAndPromptDraft(onRestore, onDismiss) {
  if (hasDraft()) {
    const prompt = new DraftPrompt({
      onRestore: () => {
        const draft = loadDraft();
        if (draft) {
          populateFormFromDraft(draft);
        }
        if (onRestore) onRestore(draft);
      },
      onDismiss: onDismiss
    });
    
    // Show prompt after a brief delay for better UX
    setTimeout(() => prompt.show(), 500);
  }
}

// ============================================
// CSS STYLES (inject into document)
// ============================================

const draftSavingStyles = `
  /* Save Draft Button Styles */
  .save-draft-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 16px;
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 6px;
    color: #495057;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  
  .save-draft-btn:hover {
    background: #e9ecef;
    border-color: #adb5bd;
  }
  
  .save-draft-btn:active {
    background: #dee2e6;
  }
  
  .save-draft-btn svg {
    flex-shrink: 0;
  }
  
  /* Draft Prompt Overlay */
  .draft-prompt-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10000;
    opacity: 0;
    transition: opacity 0.3s ease;
  }
  
  .draft-prompt-overlay.visible {
    opacity: 1;
  }
  
  /* Draft Prompt Container */
  .draft-prompt-container {
    background: white;
    border-radius: 12px;
    padding: 32px;
    max-width: 400px;
    width: 90%;
    text-align: center;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
    transform: translateY(20px);
    transition: transform 0.3s ease;
  }
  
  .draft-prompt-overlay.visible .draft-prompt-container {
    transform: translateY(0);
  }
  
  .draft-prompt-icon {
    width: 64px;
    height: 64px;
    margin: 0 auto 16px;
    background: #e3f2fd;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #1976d2;
  }
  
  .draft-prompt-title {
    margin: 0 0 8px;
    font-size: 20px;
    font-weight: 600;
    color: #212529;
  }
  
  .draft-prompt-message {
    margin: 0 0 8px;
    font-size: 14px;
    color: #6c757d;
    line-height: 1.5;
  }
  
  .draft-prompt-timestamp {
    font-size: 12px;
    color: #adb5bd;
    margin-bottom: 20px;
  }
  
  .draft-prompt-buttons {
    display: flex;
    gap: 12px;
    justify-content: center;
  }
  
  .draft-prompt-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 10px 20px;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
    border: none;
  }
  
  .draft-prompt-restore {
    background: #1976d2;
    color: white;
  }
  
  .draft-prompt-restore:hover {
    background: #1565c0;
  }
  
  .draft-prompt-dismiss {
    background: #f8f9fa;
    color: #495057;
    border: 1px solid #dee2e6;
  }
  
  .draft-prompt-dismiss:hover {
    background: #e9ecef;
  }
  
  .draft-prompt-btn svg {
    flex-shrink: 0;
  }
  
  /* Toast notification for save confirmation */
  .draft-save-toast {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #2e7d32;
    color: white;
    padding: 12px 20px;
    border-radius: 8px;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    z-index: 10001;
    animation: slideIn 0.3s ease;
  }
  
  @keyframes slideIn {
    from {
      transform: translateX(100%);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }
`;

/**
 * Inject CSS styles into the document head
 */
function injectDraftSavingStyles() {
  if (document.getElementById('draft-saving-styles')) {
    return; // Already injected
  }
  
  const styleElement = document.createElement('style');
  styleElement.id = 'draft-saving-styles';
  styleElement.textContent = draftSavingStyles;
  document.head.appendChild(styleElement);
}

/**
 * Show a toast notification for draft save confirmation
 */
function showDraftSaveToast() {
  // Remove any existing toast
  const existingToast = document.querySelector('.draft-save-toast');
  if (existingToast) {
    existingToast.remove();
  }
  
  const toast = document.createElement('div');
  toast.className = 'draft-save-toast';
  toast.innerHTML = `
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <polyline points="20 6 9 17 4 12"></polyline>
    </svg>
    Draft saved successfully
  `;
  
  document.body.appendChild(toast);
  
  // Auto-remove after 3 seconds
  setTimeout(() => {
    toast.style.animation = 'slideIn 0.3s ease reverse';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

/**
 * Handle save draft button click (for vanilla JS implementation)
 */
function handleSaveDraftClick() {
  const formData = getFormDataFromDOM();
  if (saveDraft(formData)) {
    showDraftSaveToast();
  }
}

// ============================================
// REACT COMPONENT EXPORTS
// ============================================

// These are provided for React environments
// In vanilla JS, use the class-based DraftPrompt above

/**
 * React DraftPrompt Component
 * Usage:
 * <DraftPrompt onRestore={handleRestore} onDismiss={handleDismiss} />
 */
const DraftPromptReact = (typeof React !== 'undefined' ? {
  Component: class DraftPromptComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        visible: hasDraft(),
        savedAt: null
      };
    }
    
    componentDidMount() {
      const draft = loadDraft();
      if (draft && draft.savedAt) {
        this.setState({ savedAt: new Date(draft.savedAt) });
      }
    }
    
    handleRestore = () => {
      const draft = loadDraft();
      if (this.props.onRestore) {
        this.props.onRestore(draft);
      }
      this.setState({ visible: false });
    };
    
    handleDismiss = () => {
      clearDraft();
      if (this.props.onDismiss) {
        this.props.onDismiss();
      }
      this.setState({ visible: false });
    };
    
    render() {
      if (!this.state.visible) return null;
      
      const { savedAt } = this.state;
      
      return React.createElement('div', { className: 'draft-prompt-overlay visible' },
        React.createElement('div', { className: 'draft-prompt-container' },
          React.createElement('div', { className: 'draft-prompt-icon' },
            React.createElement('svg', { width: '48', height: '48', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', strokeWidth: '2' },
              React.createElement('path', { d: 'M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z' }),
              React.createElement('polyline', { points: '14 2 14 8 20 8' }),
              React.createElement('line', { x1: '16', y1: '13', x2: '8', y2: '13' }),
              React.createElement('line', { x1: '16', y1: '17', x2: '8', y2: '17' })
            )
          ),
          React.createElement('h3', { className: 'draft-prompt-title' }, 'Saved Draft Found'),
          React.createElement('p', { className: 'draft-prompt-message' }, 'We found a saved draft. Would you like to restore it?'),
          savedAt && React.createElement('div', { className: 'draft-prompt-timestamp' }, 
            'Last saved: ', savedAt.toLocaleString()
          ),
          React.createElement('div', { className: 'draft-prompt-buttons' },
            React.createElement('button', { 
              type: 'button', 
              className: 'draft-prompt-btn draft-prompt-restore',
              onClick: this.handleRestore
            },
              React.createElement('svg', { width: '16', height: '16', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', strokeWidth: '2' },
                React.createElement('polyline', { points: '1 4 1 10 7 10' }),
                React.createElement('path', { d: 'M3.51 15a9 9 0 1 0 2.13-9.36L1 10' })
              ),
              'Restore Draft'
            ),
            React.createElement('button', { 
              type: 'button', 
              className: 'draft-prompt-btn draft-prompt-dismiss',
              onClick: this.handleDismiss
            },
              React.createElement('svg', { width: '16', height: '16', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', strokeWidth: '2' },
                React.createElement('line', { x1: '18', y1: '6', x2: '6', y2: '18' }),
                React.createElement('line', { x1: '6', y1: '6', x2: '18', y2: '18' })
              ),
              'Start Fresh'
            )
          )
        )
      );
    }
  }
} : null);

/**
 * React SaveDraftButton Component
 * Usage:
 * <SaveDraftButton formData={currentFormData} onSave={handleSave} />
 */
const SaveDraftButtonReact = (typeof React !== 'undefined' ? {
  Component: class SaveDraftButtonComponent extends React.Component {
    handleClick = () => {
      const { formData, onSave } = this.props;
      if (saveDraft(formData)) {
        showDraftSaveToast();
        if (onSave) {
          onSave();
        }
      }
    };
    
    render() {
      return React.createElement('button', {
        type: 'button',
        className: 'save-draft-btn',
        onClick: this.handleClick
      },
        React.createElement('svg', { width: '16', height: '16', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', strokeWidth: '2' },
          React.createElement('path', { d: 'M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z' }),
          React.createElement('polyline', { points: '17 21 17 13 7 13 7 21' }),
          React.createElement('polyline', { points: '7 3 7 8 15 8' })
        ),
        'Save Draft'
      );
    }
  }
} : null);

// ============================================
// INITIALIZATION
// ============================================

/**
 * Initialize draft saving functionality
 * Call this on page load to set up auto-save and check for existing drafts
 * @param {Object} options - Configuration options
 * @param {Function} options.getFormData - Function to get current form data
 * @param {Function} options.onRestore - Callback when draft is restored
 * @param {Function} options.onDismiss - Callback when draft is dismissed
 * @param {boolean} options.autoSave - Enable auto-save (default: true)
 * @param {number} options.debounceMs - Auto-save debounce delay (default: 1000ms)
 */
function initDraftSaving(options = {}) {
  const {
    getFormData = getFormDataFromDOM,
    onRestore = null,
    onDismiss = null,
    autoSave = true,
    debounceMs = AUTO_SAVE_DEBOUNCE_MS
  } = options;
  
  // Inject styles
  injectDraftSavingStyles();
  
  // Check for existing draft and show prompt
  checkAndPromptDraft(onRestore, onDismiss);
  
  // Set up auto-save if enabled
  if (autoSave) {
    const autoSaver = createAutoSave(getFormData, debounceMs);
    
    // Attach change listeners to form fields
    DRAFT_FIELDS.forEach(field => {
      const element = document.getElementById(field) || 
                      document.querySelector(`[name="${field}"]`);
      
      if (element) {
        element.addEventListener('input', autoSaver.trigger);
        element.addEventListener('change', autoSaver.trigger);
      }
    });
    
    // Return cleanup function
    return () => {
      autoSaver.cancel();
      DRAFT_FIELDS.forEach(field => {
        const element = document.getElementById(field) || 
                        document.querySelector(`[name="${field}"]`);
        if (element) {
          element.removeEventListener('input', autoSaver.trigger);
          element.removeEventListener('change', autoSaver.trigger);
        }
      });
    };
  }
  
  return () => {};
}

// ============================================
// EXPORTS
// ============================================

// For ES6 module environments
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    // Core functions
    saveDraft,
    loadDraft,
    clearDraft,
    hasDraft,
    
    // Auto-save utilities
    createAutoSave,
    getFormDataFromDOM,
    populateFormFromDraft,
    
    // UI components (vanilla JS)
    DraftPrompt,
    createSaveDraftButton,
    showDraftSaveToast,
    injectDraftSavingStyles,
    
    // React components
    DraftPromptReact,
    SaveDraftButtonReact,
    
    // Initialization
    initDraftSaving,
    checkAndPromptDraft,
    
    // Constants
    DRAFT_STORAGE_KEY,
    DRAFT_FIELDS,
    AUTO_SAVE_DEBOUNCE_MS
  };
}

// For browser global scope
if (typeof window !== 'undefined') {
  window.MyCivicVoice = window.MyCivicVoice || {};
  window.MyCivicVoice.DraftSaving = {
    // Core functions
    saveDraft,
    loadDraft,
    clearDraft,
    hasDraft,
    
    // Auto-save utilities
    createAutoSave,
    getFormDataFromDOM,
    populateFormFromDraft,
    
    // UI components
    DraftPrompt,
    createSaveDraftButton,
    showDraftSaveToast,
    injectDraftSavingStyles,
    
    // React components
    DraftPromptReact,
    SaveDraftButtonReact,
    
    // Initialization
    initDraftSaving,
    checkAndPromptDraft,
    
    // Constants
    DRAFT_STORAGE_KEY,
    DRAFT_FIELDS,
    AUTO_SAVE_DEBOUNCE_MS
  };
}