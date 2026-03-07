import { FR, EN } from '../data/translations.js';

function TermsModal({ isOpen, onClose, isFrench }) {
  const t = isFrench ? FR : EN;
  const getText = (key, en) => t[key] || en;
  
  if (!isOpen) return null;
  
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:24}}>
          <h2 style={{margin:0,fontSize:22}}>{getText('tosTitle','Terms of Service')}</h2>
          <button onClick={onClose} style={{background:'none',border:'none',color:'#9CA3AF',fontSize:28,cursor:'pointer'}}>×</button>
        </div>
        <div style={{color:'#9CA3AF',fontSize:14,lineHeight:1.7}}>
          <p style={{marginBottom:16}}>{getText('tosIntro','By using My Civic Voice, you agree to the following terms:')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('tosPurpose','Purpose of the Tool')}</h3>
          <p style={{marginBottom:16}}>{getText('tosPurposeText','My Civic Voice is a free tool designed to help Canadian citizens contact their elected representatives. The tool is provided "as is" without any warranty.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('tosUserContent','User Content')}</h3>
          <p style={{marginBottom:16}}>{getText('tosUserContentText','You are entirely responsible for the content of letters and messages you write. My Civic Voice is not responsible for the content, accuracy, or consequences of your communications.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('tosNoWarranty','No Warranty')}</h3>
          <p style={{marginBottom:16}}>{getText('tosNoWarrantyText','This tool is provided without warranty. Representative data comes from public sources and may not be current. Always verify information with official sources.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('tosLimitation','Limitation of Liability')}</h3>
          <p style={{marginBottom:16}}>{getText('tosLimitationText','My Civic Voice, its creators, and contributors are not liable for any damages resulting from the use of this tool.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('tosAttribution','Attribution')}</h3>
          <p style={{marginBottom:16}}>{getText('tosAttributionText','Representative data comes from the OpenNorth Represent API, licensed under MIT. Open North Inc. is not responsible for how this data is used.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('tosPrivacy','Privacy')}</h3>
          <p style={{marginBottom:16}}>{getText('tosPrivacyText','We collect no personal data. Your drafts are stored only in your browser and are deleted when you close this page.')}</p>
          
          <p style={{marginTop:20,fontSize:13,color:'#6B7280'}}>OpenNorth Represent API is licensed under the MIT License. Copyright © 2012 Open North Inc.</p>
        </div>
        <button className="btn-primary" style={{marginTop:20,width:'100%'}} onClick={onClose}>{getText('tosClose','Close')}</button>
      </div>
    </div>
  );
}

export default TermsModal;