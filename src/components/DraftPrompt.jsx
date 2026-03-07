import { FR } from '../data/translations.js';

// Draft storage functions
const DRAFT_KEY = 'mycivicvoice_draft';

function saveDraft(data) { 
  try { 
    localStorage.setItem(DRAFT_KEY, JSON.stringify({...data, savedAt: new Date().toISOString()})); 
    return true; 
  } catch(e) { 
    return false; 
  } 
}

function loadDraft() { 
  try { 
    const d = localStorage.getItem(DRAFT_KEY); 
    return d ? JSON.parse(d) : null; 
  } catch(e) { 
    return null; 
  } 
}

function DraftPrompt({ onRestore, onDismiss, isFrench }) {
  const draft = loadDraft();
  if (!draft) return null;
  
  const t = isFrench ? FR : {};
  const getText = (key, en) => t[key] || en;
  
  return (
    <div className="draft-prompt-overlay">
      <div className="draft-prompt-container">
        <h3 style={{margin:'0 0 8px 0'}}>📋 {getText('draftFound', 'Draft found')}</h3>
        <p style={{color:'#9CA3AF',marginBottom:20}}>{getText('draftFoundMessage', 'We found a saved draft. Would you like to restore it?')}</p>
        <div>
          <button className="draft-prompt-btn draft-prompt-restore" onClick={onRestore}>{getText('restoreDraft', 'Restore draft')}</button>
          <button className="draft-prompt-btn draft-prompt-dismiss" onClick={onDismiss}>{getText('startFresh', 'Start fresh')}</button>
        </div>
      </div>
    </div>
  );
}

export default DraftPrompt;
export { saveDraft, loadDraft, DRAFT_KEY };