import { FR } from '../data/translations.js';

function PrivacyModal({ isOpen, onClose, isFrench }) {
  const t = isFrench ? FR : {};
  const getText = (key, en) => t[key] || en;
  
  if (!isOpen) return null;
  
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:24}}>
          <h2 style={{margin:0,fontSize:22}}>{getText('privacyTitle','Privacy')}</h2>
          <button onClick={onClose} style={{background:'none',border:'none',color:'#9CA3AF',fontSize:28,cursor:'pointer'}}>×</button>
        </div>
        <div style={{color:'#9CA3AF',fontSize:14,lineHeight:1.7}}>
          <p style={{marginBottom:16}}>{getText('privacyIntro','My Civic Voice is a free tool. We collect no data. Your privacy is our priority.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('privacyDataTitle','What We Do NOT Do')}</h3>
          <ul style={{margin:0,paddingLeft:20}}>
            <li style={{marginBottom:8}}>{getText('privacyData1','No account required')}</li>
            <li style={{marginBottom:8}}>{getText('privacyData2','No tracking or analytics')}</li>
            <li style={{marginBottom:8}}>{getText('privacyData3','No data stored on our servers')}</li>
          </ul>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('privacyNoDataTitle','What Happens to Your Data')}</h3>
          <ul style={{margin:0,paddingLeft:20}}>
            <li style={{marginBottom:8}}>{getText('privacyNoData1','Your postal code is only used to find your representatives')}</li>
            <li style={{marginBottom:8}}>{getText('privacyNoData2','Your drafts are stored only in your browser')}</li>
            <li style={{marginBottom:8}}>{getText('privacyNoData3','Everything is automatically deleted when you close this page')}</li>
          </ul>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('privacyStorageTitle','Use This Tool Freely')}</h3>
          <p style={{marginBottom:16}}>{getText('privacyStorageText','This tool is free, ad-free, and collects no data. Use it to make your community better. Your voice matters.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('privacyApiTitle','Data Source')}</h3>
          <p style={{marginBottom:16}}>{getText('privacyApiText','Representative data comes from the OpenNorth Represent API, a non-profit organization.')}</p>
          
          <p style={{marginTop:20,fontSize:13}}>{getText('privacyContact','Questions? Use the feedback form on the site.')}</p>
        </div>
      </div>
    </div>
  );
}

export default PrivacyModal;