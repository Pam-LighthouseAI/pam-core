import { useState } from 'react';
import { FAQ_EN, FAQ_FR } from '../data/faq.js';

function FAQModal({ isOpen, onClose, isFrench }) {
  const [openIndex, setOpenIndex] = useState(null);
  const FAQ = isFrench ? FAQ_FR : FAQ_EN;
  const title = isFrench ? "Questions fréquemment posées" : "Frequently Asked Questions";
  if (!isOpen) return null;
  
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:24}}>
          <h2 style={{margin:0,fontSize:24}}>{title}</h2>
          <button onClick={onClose} style={{background:'none',border:'none',color:'#9CA3AF',fontSize:28,cursor:'pointer'}}>×</button>
        </div>
        <div style={{maxHeight:'60vh',overflowY:'auto'}}>
          {FAQ.map((item, i) => (
            <div key={i} className="faq-item">
              <button className="faq-question" onClick={() => setOpenIndex(openIndex === i ? null : i)}>
                <span>{item.q}</span>
                <span style={{transform:openIndex===i?'rotate(180deg)':'none',transition:'transform 0.2s'}}>▼</span>
              </button>
              {openIndex === i && <div className="faq-answer">{item.a}</div>}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default FAQModal;