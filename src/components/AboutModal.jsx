import { FR } from '../data/translations.js';

function AboutModal({ isOpen, onClose, isFrench }) {
  const t = isFrench ? FR : {};
  const getText = (key, en) => t[key] || en;
  
  if (!isOpen) return null;
  
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:24}}>
          <h2 style={{margin:0,fontSize:22}}>{getText('aboutTitle','About')}</h2>
          <button onClick={onClose} style={{background:'none',border:'none',color:'#9CA3AF',fontSize:28,cursor:'pointer'}}>×</button>
        </div>
        <div style={{color:'#9CA3AF',fontSize:14,lineHeight:1.7}}>
          <p style={{marginBottom:16}}>{getText('aboutIntro','My Civic Voice Canada is a free, non-profit tool designed to help Canadian citizens connect with their elected representatives.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('aboutMissionTitle','Our Mission')}</h3>
          <p style={{marginBottom:16}}>{getText('aboutMissionText','We believe every citizen deserves to know who represents their interests and how to make their voice heard. Our mission is to make civic engagement accessible to all Canadians.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('aboutHowTitle','How It Works')}</h3>
          <ol style={{margin:0,paddingLeft:20}}>
            <li style={{marginBottom:8}}>{getText('aboutHow1','Enter your postal code or city to find your representatives')}</li>
            <li style={{marginBottom:8}}>{getText('aboutHow2','Describe your issue to get guidance on the right level of government')}</li>
            <li style={{marginBottom:8}}>{getText('aboutHow3','Draft a personal letter with our template')}</li>
            <li style={{marginBottom:8}}>{getText('aboutHow4','Contact your representatives directly by email or phone')}</li>
          </ol>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('aboutDataTitle','Data Sources')}</h3>
          <p style={{marginBottom:16}}>{getText('aboutDataText','Representative data comes from the OpenNorth Represent API, which consolidates data from Elections Canada, provincial elections offices, and municipal sources.')}</p>
          
          <p style={{marginTop:20,fontSize:13,color:'#6B7280'}}>{getText('aboutAccuracy','Federal and provincial data is generally current. Municipal data may occasionally be outdated after local elections.')}</p>
          
          <p style={{marginTop:16,fontSize:13}}>{getText('aboutOpen','This tool is an open source project. You can contribute on GitHub.')}</p>
          
          <h3 style={{color:'#fff',margin:'20px 0 12px 0',fontSize:16}}>{getText('aboutAttributionTitle','Data Attribution')}</h3>
          <p style={{fontSize:13,lineHeight:1.6}}>{getText('aboutAttributionText','Representative data is provided by the')} <a href="https://represent.opennorth.ca/" target="_blank" rel="noopener noreferrer" style={{color:'#FBBF24'}}>OpenNorth Represent API</a>, {isFrench ? 'sous licence MIT. Copyright © 2012 Open North Inc.' : 'licensed under the MIT License. Copyright © 2012 Open North Inc.'}</p>
          <p style={{fontSize:12,color:'#6B7280',marginTop:8}}>{getText('aboutAttributionNote','Open North is a Canadian non-profit organization that makes government data accessible to all.')}</p>
        </div>
      </div>
    </div>
  );
}

export default AboutModal;