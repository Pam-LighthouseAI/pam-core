import { useState, useEffect, useRef, useMemo } from 'react';
import { FR, EN } from './data/translations.js';
import { ISSUES } from './data/issues.js';
import { FAQ_EN, FAQ_FR } from './data/faq.js';
import { JURISDICTION_HEADERS, JURISDICTION_HEADERS_FR } from './data/jurisdiction.js';
import { STORY_PROMPTS, STORY_PROMPTS_FR } from './data/storyPrompts.js';
import { OPENING_LINES, OPENING_LINES_FR } from './data/openingLines.js';
import { CLOSING_LINES, CLOSING_LINES_FR } from './data/closingLines.js';
import { TEMPLATES } from './data/templates.js';
import { MUNICIPAL_BACKUP_LINKS, PROVINCIAL_BACKUP_LINKS, CITY_PROVINCE, PROVINCE_REPS } from './data/lookup.js';
import LanguageToggle from './components/LanguageToggle.jsx';
import FAQModal from './components/FAQModal.jsx';
import FeedbackModal from './components/FeedbackModal.jsx';
import DraftPrompt, { saveDraft, loadDraft, clearDraft, DRAFT_KEY } from './components/DraftPrompt.jsx';
import TermsModal from './components/TermsModal.jsx';
import PrivacyModal from './components/PrivacyModal.jsx';
import AboutModal from './components/AboutModal.jsx';
import './index.css';

function App() {
  const [step, setStep] = useState(1);
  const [isFrench, setIsFrench] = useState(() => {
    const saved = localStorage.getItem('myCivicVoice_language');
    if (saved) return saved === 'fr';
    return (navigator.language || '').startsWith('fr');
  });
  const [locType, setLocType] = useState('postal');
  const [postalCode, setPostalCode] = useState('');
  const [postalError, setPostalError] = useState('');
  const [city, setCity] = useState('');
  const [province, setProvince] = useState('');
  const [selCat, setSelCat] = useState(null);
  const [selIssue, setSelIssue] = useState(null);
  const [searchQ, setSearchQ] = useState('');
  const [reps, setReps] = useState({federal:[],provincial:[],municipal:[]});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [uName, setUName] = useState('');
  const [uEmail, setUEmail] = useState('');
  const [uPhone, setUPhone] = useState('');
  const [uDetail, setUDetail] = useState('');
  const [uTone, setUTone] = useState('concerned');
  const [copied, setCopied] = useState(false);
  const [showFAQ, setShowFAQ] = useState(false);
  const [showFeedback, setShowFeedback] = useState(false);
  const [showDraftPrompt, setShowDraftPrompt] = useState(false);
  const [showPrivacy, setShowPrivacy] = useState(false);
  const [showAbout, setShowAbout] = useState(false);
  const [showShare, setShowShare] = useState(false);
  const [showTerms, setShowTerms] = useState(false);
  const shareRef = useRef(null);
  
  // Close share dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (e) => {
      if (shareRef.current && !shareRef.current.contains(e.target)) {
        setShowShare(false);
      }
    };
    if (showShare) {
      document.addEventListener('mousedown', handleClickOutside);
      return () => document.removeEventListener('mousedown', handleClickOutside);
    }
  }, [showShare]);
  
  const t = isFrench ? FR : {};
  const getText = (key, en) => t[key] || en;
  
  // Validate Canadian postal code
  const validatePostalCode = (pc) => {
    if (!pc) return '';
    const clean = pc.replace(/\s/g, '').toUpperCase();
    const valid = /^[A-Z]\d[A-Z]\d[A-Z]\d$/.test(clean);
    if (!valid && clean.length >= 6) {
      return 'Invalid format. Use A1A 1A1 format.';
    }
    return '';
  };
  
  // Language toggle
  const handleLangToggle = () => {
    const newLang = !isFrench;
    setIsFrench(newLang);
    localStorage.setItem('myCivicVoice_language', newLang ? 'fr' : 'en');
  };
  
  // Draft restore
  const handleRestoreDraft = () => {
    const draft = loadDraft();
    if (draft) {
      setUName(draft.userName || '');
      setUEmail(draft.userEmail || '');
      setUPhone(draft.userPhone || '');
      setUDetail(draft.userDetail || '');
      if (draft.selectedCategory) setSelCat(ISSUES.find(c => c.id === draft.selectedCategory) || null);
      if (draft.selectedIssue) setSelIssue(draft.selectedIssue);
    }
    setShowDraftPrompt(false);
  };
  
  // Auto-save draft
  useEffect(() => {
    if (uName || uEmail || uPhone || uDetail || selIssue) {
      const timer = setTimeout(() => {
        saveDraft({userName:uName, userEmail:uEmail, userPhone:uPhone, userDetail:uDetail, selectedIssue:selIssue, selectedCategory:selCat?.id});
      }, 1000);
      return () => clearTimeout(timer);
    }
  }, [uName, uEmail, uPhone, uDetail, selIssue, selCat]);
  
  // Clear all data when user leaves the page
  useEffect(() => {
    const handleBeforeUnload = () => {
      localStorage.removeItem(DRAFT_KEY);
      localStorage.removeItem('mycivicvoice_language');
    };
    window.addEventListener('beforeunload', handleBeforeUnload);
    return () => window.removeEventListener('beforeunload', handleBeforeUnload);
  }, []);
  
  // Fetch reps
  useEffect(() => {
    if (step !== 3) return;
    
    // Postal code - full representative lookup
    if (locType === 'postal' && postalCode) {
      setLoading(true);
      const pc = postalCode.replace(/\s/g, '').toUpperCase();
      fetch(`https://represent.opennorth.ca/postcodes/${pc}/`)
        .then(r => r.json())
        .then(d => {
          const grouped = {federal:[],provincial:[],municipal:[]};
          const repsData = d.representatives_centroid || d.representatives_concordance || [];
          repsData.forEach(r => {
            const nm = r.name || 'Unknown';
            const em = r.email || '';
            const off = r.district_name || '';
            const party = r.party_name || '';
            const office = r.elected_office || '';
            let ph = '';
            if (r.offices && r.offices.length > 0) {
              const officeWithPhone = r.offices.find(o => o.tel);
              if (officeWithPhone) ph = officeWithPhone.tel;
            }
            const entry = {name:nm,email:em,phone:ph,office:off,party,officeType:office};
            if (office === 'MP' || office === 'Senator') {
              grouped.federal.push(entry);
            } else if (office === 'MPP' || office === 'MLA' || office === 'MNA' || office === 'MHA') {
              grouped.provincial.push(entry);
            } else if (office === 'Mayor' || office === 'Councillor' || office === 'Regional Councillor') {
              grouped.municipal.push(entry);
            } else if (r.representative_set_name && r.representative_set_name.includes('House of Commons')) {
              grouped.federal.push(entry);
            } else if (r.representative_set_name && (r.representative_set_name.includes('Legislative') || r.representative_set_name.includes('Assembly'))) {
              grouped.provincial.push(entry);
            } else if (r.representative_set_name && r.representative_set_name.includes('Council')) {
              grouped.municipal.push(entry);
            }
          });
          setReps(grouped);
          setLoading(false);
        })
        .catch((err) => {
          console.error('API error:', err);
          setError('postal_code_not_found');
          setLoading(false);
        });
    }
    // Province or City - fetch provincial and federal reps
    else if ((locType === 'province' && province) || (locType === 'city' && city)) {
      setLoading(true);
      const prov = locType === 'province' ? province : CITY_PROVINCE[city];
      if (!prov) {
        setLoading(false);
        return;
      }
      
      // Fetch federal MPs for this province
      Promise.all([
        fetch(`https://represent.opennorth.ca/representatives/house-of-commons/?limit=500`).then(r => r.json()),
        fetch(`https://represent.opennorth.ca/representatives/?limit=500`).then(r => r.json())
      ])
        .then(([federalData, allData]) => {
          const grouped = {federal:[],provincial:[],municipal:[]};
          
          // Filter federal MPs by province
          const federalReps = (federalData.objects || allData.objects || [])
            .filter(r => r.elected_office === 'MP' && (r.district_name?.includes(prov) || r.offices?.some(o => o.postal?.startsWith(prov.substring(0,2).toUpperCase()))));
          
          // Get province-specific reps
          const provSet = PROVINCE_REPS[prov];
          const provincialReps = (allData.objects || [])
            .filter(r => {
              const setName = r.representative_set_name || '';
              const isProvincial = setName.includes('Legislature') || setName.includes('Assembly') || setName.includes('House');
              const matchesProvince = setName.toLowerCase().includes(prov.toLowerCase().split(' ')[0]);
              return isProvincial && matchesProvince;
            });
          
          federalReps.slice(0, 10).forEach(r => {
            grouped.federal.push({
              name: r.name || 'Unknown',
              email: r.email || '',
              phone: r.offices?.[0]?.tel || '',
              office: r.district_name || r.elected_office || 'MP',
              party: r.party_name || '',
              officeType: 'MP'
            });
          });
          
          provincialReps.slice(0, 10).forEach(r => {
            grouped.provincial.push({
              name: r.name || 'Unknown',
              email: r.email || '',
              phone: r.offices?.[0]?.tel || '',
              office: r.district_name || '',
              party: r.party_name || '',
              officeType: r.elected_office || 'MLA'
            });
          });
          
          setReps(grouped);
          setLoading(false);
        })
        .catch(() => {
          // Fallback: show province name but no specific reps
          setReps({
            federal: [{name:`Your Federal MP (${prov})`,email:'',phone:'',office:'Contact Elections Canada',party:'',officeType:'MP'}],
            provincial: [{name:`Your ${prov} Representative`,email:'',phone:'',office:'Contact your provincial legislature',party:'',officeType:'MLA'}],
            municipal: []
          });
          setLoading(false);
        });
    }
  }, [step, locType, postalCode, province, city]);
  
  // Generate email
  const genEmail = () => {
    if (!selIssue || !selCat) return '';
    
    const catId = selCat.id;
    const openings = isFrench ? OPENING_LINES_FR : OPENING_LINES;
    const closings = isFrench ? CLOSING_LINES_FR : CLOSING_LINES;
    const opening = openings[uTone]?.[catId] || openings.concerned?.[catId] || (isFrench ? "Je vous écris au sujet d'une question importante." : "I'm writing to you about an important issue.");
    const closing = closings[uTone] || closings.concerned;
    
    // Build the story section
    const storyPlaceholder = isFrench 
      ? '[Votre expérience personnelle rendra votre lettre plus puissante. Décrivez comment cet enjeu vous affecte, vous, votre famille ou votre communauté.]'
      : '[Your personal experience will make your letter more powerful. Describe how this issue affects you, your family, or your community.]';
    const story = uDetail ? uDetail : storyPlaceholder;
    
    // Build context about the issue
    const issueName = isFrench && selIssue.nameFr ? selIssue.nameFr : selIssue.name;
    const issueDetail = isFrench && selIssue.detailFr ? selIssue.detailFr : selIssue.detail;
    const context = isFrench 
      ? `L'enjeu est : ${issueName}. ${issueDetail}`
      : `The issue is: ${issueName}. ${issueDetail}`;
    
    // Build signature
    const namePlaceholder = isFrench ? '[Votre nom]' : '[Your Name]';
    const locationPlaceholder = isFrench ? '[Votre lieu de résidence]' : '[Your Location]';
    const emailPlaceholder = isFrench ? '[Votre courriel]' : '[Your Email]';
    const signature = `${uName || namePlaceholder}
${postalCode || city || province || locationPlaceholder}
${uEmail || emailPlaceholder}`;
    
    // Representative name placeholder
    const repNamePlaceholder = isFrench ? '[Nom du représentant]' : '[Representative Name]';
    
    const tpl = TEMPLATES[catId] || TEMPLATES.infrastructure;
    const templateBody = isFrench && tpl.bodyFr ? tpl.bodyFr : tpl.body;
    let body = templateBody
      .replace(/{{REP_NAME}}/g, repNamePlaceholder)
      .replace(/{{OPENING}}/g, opening)
      .replace(/{{STORY}}/g, story)
      .replace(/{{CONTEXT}}/g, context)
      .replace(/{{CLOSING}}/g, closing)
      .replace(/{{SIGNATURE}}/g, signature);
    
    return body;
  };
  
  // Copy to clipboard
  const handleCopy = async () => {
    const text = genEmail();
    let success = false;
    // Try modern clipboard API first
    try {
      await navigator.clipboard.writeText(text);
      success = true;
    } catch (e) {
      // Fallback for older browsers or non-HTTPS contexts
      try {
        const textarea = document.createElement('textarea');
        textarea.value = text;
        textarea.style.position = 'fixed';
        textarea.style.left = '-9999px';
        document.body.appendChild(textarea);
        textarea.select();
        success = document.execCommand('copy');
        document.body.removeChild(textarea);
      } catch (e2) {
        console.error('Copy failed:', e2);
      }
    }
    if (success) {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } else {
      alert(getText('copyFailed', 'Copy failed. Please select and copy manually.'));
    }
  };
  
  // Filter issues
  const filteredIssues = useMemo(() => {
    if (!searchQ) return selCat ? selCat.items : [];
    const q = searchQ.toLowerCase();
    return ISSUES.flatMap(c => c.items).filter(i => 
      i.name.toLowerCase().includes(q) || 
      (i.nameFr && i.nameFr.toLowerCase().includes(q)) || 
      i.detail.toLowerCase().includes(q)
    );
  }, [searchQ, selCat]);

  // ... rest of the component will continue in part 2
  // For now, let me create the render functions

  const renderStep1 = () => (
    <div className="card fade-in">
      <p style={{color:'#9CA3AF',marginBottom:24,fontSize:15}}>{getText('step1Label','Step 1 of 3: Where do you live?')}</p>
      <div style={{display:'flex',gap:12,marginBottom:20}} className="flow-row">
        <button className={`loc-btn ${locType==='postal'?'active':''}`} onClick={()=>{setLocType('postal');setPostalError('');}}>{getText('postalCode','Postal Code')}</button>
        <button className={`loc-btn ${locType==='city'?'active':''}`} onClick={()=>{setLocType('city');setPostalError('');}}>{getText('city','City')}</button>
        <button className={`loc-btn ${locType==='province'?'active':''}`} onClick={()=>{setLocType('province');setPostalError('');}}>{getText('province','Province / Territory')}</button>
      </div>
      {locType === 'postal' && (
        <div>
          <input placeholder="A1A 1A1" value={postalCode} onChange={e=>{
            const val = e.target.value.toUpperCase();
            setPostalCode(val);
            setPostalError(validatePostalCode(val));
          }} maxLength={7} style={{fontFamily:'monospace',fontSize:18,textTransform:'uppercase'}} />
          {postalError && <span style={{display:'block',marginTop:8,fontSize:13,color:'#EF4444'}}>⚠️ {getText('postalError','Invalid format. Use A1A 1A1 format.')}</span>}
          {postalCode && !postalError && <span style={{display:'block',marginTop:8,fontSize:13,color:'#10B981'}}>✓ {getText('best','BEST')} — {getText('detected','Detected:')} {postalCode}</span>}
          <div style={{marginTop:16,padding:'12px 16px',background:'linear-gradient(135deg,#1e3a5f 0%,#0d1117 100%)',borderRadius:10,border:'1px solid #3b82f6'}}>
            <p style={{margin:0,fontSize:14,color:'#e5e7eb',lineHeight:1.5}}>📍 {getText('postalWhy','Your postal code is the most accurate way to find ALL your representatives — federal, provincial, AND municipal. City or province only gives you federal and provincial representatives.')}</p>
          </div>
        </div>
      )}
      {locType === 'city' && (
        <select value={city} onChange={e=>setCity(e.target.value)}>
          <option value="">{getText('city','Select city...')}</option>
          <option>Toronto</option><option>Montreal</option><option>Vancouver</option><option>Calgary</option>
          <option>Edmonton</option><option>Ottawa</option><option>Winnipeg</option><option>Mississauga</option>
          <option>Halifax</option><option>Quebec City</option><option>Hamilton</option><option>Brampton</option>
          <option>Surrey</option><option>Laval</option><option>London</option><option>Markham</option>
          <option>Vaughan</option><option>Gatineau</option><option>Saskatoon</option><option>Longueuil</option>
          <option>Kitchener</option><option>Burnaby</option><option>Windsor</option><option>Regina</option>
          <option>Richmond</option><option>Burlington</option><option>Richmond Hill</option><option>Oakville</option>
          <option>Sherbrooke</option><option>Saint John</option><option>St. John's</option><option>Victoria</option>
          <option>Fredericton</option><option>Charlottetown</option><option>Yellowknife</option><option>Whitehorse</option>
          <option>Iqaluit</option><option>Thunder Bay</option><option>Sudbury</option><option>Sault Ste. Marie</option>
          <option>North Bay</option><option>Trois-Rivières</option><option>Toronto (Scarborough)</option>
          <option>Toronto (North York)</option><option>Toronto (Etobicoke)</option><option>Montreal (Lachine)</option>
          <option>Montreal (Verdun)</option><option>Vancouver (Surrey)</option><option>Vancouver (Burnaby)</option>
        </select>
      )}
      {locType === 'province' && (
        <select value={province} onChange={e=>setProvince(e.target.value)}>
          <option value="">{getText('province','Select province...')}</option>
          <option>Ontario</option><option>British Columbia</option><option>Quebec</option><option>Alberta</option>
          <option>Manitoba</option><option>Saskatchewan</option><option>Nova Scotia</option><option>New Brunswick</option>
          <option>Newfoundland and Labrador</option><option>Prince Edward Island</option>
          <option>Yukon</option><option>Northwest Territories</option><option>Nunavut</option>
        </select>
      )}
      {locType !== 'postal' && <p style={{color:'#F59E0B',fontSize:13,marginTop:12}}>{getText('noPostalWarning','Provincial and federal representatives will be shown. For municipal reps, enter a postal code.')}</p>}
      <button className="btn-primary" style={{marginTop:28}} onClick={()=>setStep(2)} disabled={!(postalCode||city||province)||postalError}>{getText('getStarted','Get Started')} →</button>
    </div>
  );

  // Continue with renderStep2 and renderStep3...
  // Due to length, I'll create the rest in a separate file

  return (
    <div>
      {/* Draft prompt */}
      {showDraftPrompt && <DraftPrompt onRestore={handleRestoreDraft} onDismiss={()=>setShowDraftPrompt(false)} isFrench={isFrench} />}
      
      {/* Header */}
      <header style={{textAlign:'center',marginBottom:32,position:'relative'}}>
        {/* Share button - top right */}
        <div ref={shareRef} style={{position:'absolute',top:0,right:0,zIndex:10}}>
          <button 
            onClick={()=>setShowShare(!showShare)}
            style={{
              background:'rgba(255,255,255,0.05)',
              border:'1px solid rgba(255,255,255,0.1)',
              borderRadius:8,
              padding:'8px 12px',
              color:'#9CA3AF',
              fontSize:13,
              fontWeight:500,
              cursor:'pointer',
              display:'flex',
              alignItems:'center',
              gap:6,
              transition:'all 0.15s'
            }}
            onMouseOver={e=>{e.currentTarget.style.background='rgba(255,255,255,0.1)';e.currentTarget.style.color='#fff'}}
            onMouseOut={e=>{e.currentTarget.style.background='rgba(255,255,255,0.05)';e.currentTarget.style.color='#9CA3AF'}}
          >
            <span>📤</span>
            <span>{getText('shareBtn','Share')}</span>
          </button>
          {showShare && (
            <div style={{
              position:'absolute',
              top:'100%',
              right:0,
              marginTop:8,
              background:'#1A1A2E',
              border:'1px solid rgba(255,255,255,0.1)',
              borderRadius:12,
              padding:12,
              minWidth:200,
              boxShadow:'0 10px 40px rgba(0,0,0,0.5)'
            }}>
              <p style={{color:'#6B7280',fontSize:12,margin:'0 0 10px 0'}}>{getText('sharePrompt','Share this tool with friends and family')}</p>
              <button onClick={()=>{navigator.clipboard?.writeText(window.location.href).then(()=>alert(getText('linkCopied','Link copied!'))).catch(()=>{const ta=document.createElement('textarea');ta.value=window.location.href;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);alert(getText('linkCopied','Link copied!'));});setShowShare(false);}} style={{width:'100%',padding:'10px 14px',marginBottom:8,background:'linear-gradient(135deg,#3B82F6,#1D4ED8)',border:'none',borderRadius:8,color:'#fff',fontWeight:600,cursor:'pointer',display:'flex',alignItems:'center',justifyContent:'center',gap:8}}>
                <span>🔗</span> {getText('shareCopyLink','Copy Link')}
              </button>
              <a href={`https://twitter.com/intent/tweet?text=${encodeURIComponent(getText('shareText','Check out My Civic Voice — find your representatives and make your voice heard!'))}&url=${encodeURIComponent(window.location.href)}`} target="_blank" rel="noopener noreferrer" style={{width:'100%',padding:'10px 14px',marginBottom:8,background:'#1DA1F2',border:'none',borderRadius:8,color:'#fff',fontWeight:600,cursor:'pointer',display:'flex',alignItems:'center',justifyContent:'center',gap:8,textDecoration:'none'}}>
                <span>🐦</span> Twitter
              </a>
              <a href={`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(window.location.href)}`} target="_blank" rel="noopener noreferrer" style={{width:'100%',padding:'10px 14px',marginBottom:8,background:'#1877F2',border:'none',borderRadius:8,color:'#fff',fontWeight:600,cursor:'pointer',display:'flex',alignItems:'center',justifyContent:'center',gap:8,textDecoration:'none'}}>
                <span>📘</span> Facebook
              </a>
              <a href={`mailto:?subject=${encodeURIComponent(getText('shareSubject','My Civic Voice Canada'))}&body=${encodeURIComponent(getText('shareText','Check out My Civic Voice — find your representatives and make your voice heard!') + '\n\n' + window.location.href)}`} style={{width:'100%',padding:'10px 14px',marginBottom:8,background:'#10B981',border:'none',borderRadius:8,color:'#fff',fontWeight:600,cursor:'pointer',display:'flex',alignItems:'center',justifyContent:'center',gap:8,textDecoration:'none'}}>
                <span>✉️</span> {getText('shareEmail','Email')}
              </a>
              <a href={`https://wa.me/?text=${encodeURIComponent(getText('shareText','Check out My Civic Voice — find your representatives and make your voice heard!') + ' ' + window.location.href)}`} target="_blank" rel="noopener noreferrer" style={{width:'100%',padding:'10px 14px',background:'#25D366',border:'none',borderRadius:8,color:'#fff',fontWeight:600,cursor:'pointer',display:'flex',alignItems:'center',justifyContent:'center',gap:8,textDecoration:'none'}}>
                <span>💬</span> WhatsApp
              </a>
            </div>
          )}
        </div>
        
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:12}}>
          <h1 style={{fontFamily:'"Playfair Display",serif',fontSize:36,margin:0,background:'linear-gradient(135deg,#F59E0B,#EF4444)',WebkitBackgroundClip:'text',WebkitTextFillColor:'transparent'}}>
            {getText('siteTitle','My Civic Voice')}
          </h1>
          <LanguageToggle isFrench={isFrench} onToggle={handleLangToggle} />
        </div>
        <div style={{fontSize:28,fontWeight:700,color:'#9CA3AF',marginTop:4}}>{getText('siteSubtitle','Canada')}</div>
        <p style={{color:'#9CA3AF',maxWidth:480,margin:'16px auto 0',lineHeight:1.6}}>{getText('tagline','No accounts. No tracking. Just your voice.')}</p>
        <div style={{marginTop:20,padding:'14px 18px',background:'linear-gradient(135deg,rgba(16,185,129,0.1) 0%,rgba(6,78,59,0.2) 100%)',border:'1px solid rgba(16,185,129,0.25)',borderRadius:12,maxWidth:520,margin:'20px auto 0'}}>
          <p style={{margin:0,fontSize:14,color:'#A7F3D0',lineHeight:1.6}}>
            💡 <strong style={{color:'#34D399'}}>{isFrench ? 'Pourquoi ça compte :' : 'Why it matters:'}</strong> {isFrench ? 'Les représentants élus accordent la priorité aux messages venant de leur propre circonscription. Votre code postal prouve que vous êtes leur électeur — ce qui donne plus de poids à votre voix.' : 'Elected representatives prioritize messages from their own constituency. Your postal code proves you\'re their constituent — giving your voice more weight.'}
          </p>
        </div>
      </header>
      
      {/* Top navigation buttons */}
      {step === 2 && (
        <div style={{marginBottom:16,display:'flex',gap:8,flexWrap:'wrap'}}>
          <button className="btn-secondary" onClick={()=>setStep(1)}>{getText('back','← Back')}</button>
        </div>
      )}
      {step === 3 && (
        <div style={{marginBottom:16,display:'flex',gap:8,flexWrap:'wrap'}}>
          <button className="btn-secondary" onClick={()=>setStep(2)}>{getText('back','← Back')}</button>
          <button className="btn-secondary" onClick={()=>{setStep(2);setSelIssue(null);}}>{getText('differentIssue','Different Issue')}</button>
          <button className="btn-secondary" onClick={()=>{setStep(1);setPostalCode('');setCity('');setProvince('');setSelCat(null);setSelIssue(null);clearDraft();setPostalError('');}}>{getText('startOver','Start Over')}</button>
        </div>
      )}
      
      {/* Main content */}
      {step === 1 && renderStep1()}
      {step === 2 && renderStep2()}
      {step === 3 && renderStep3()}
      
      {/* Footer */}
      <footer style={{textAlign:'center',marginTop:40,paddingTop:20,borderTop:'1px solid rgba(255,255,255,0.06)'}}>
        <div style={{marginBottom:12}}>
          <button className="footer-btn" onClick={()=>setShowFAQ(true)}>{getText('helpFAQ','Help / FAQ')}</button>
          <button className="footer-btn" onClick={()=>setShowPrivacy(true)}>{getText('privacyTitle','Privacy')}</button>
          <button className="footer-btn" onClick={()=>setShowAbout(true)}>{getText('aboutTitle','About')}</button>
          <button className="footer-btn" onClick={()=>setShowTerms(true)}>{isFrench ? 'Conditions' : 'Terms'}</button>
          <button className="footer-btn" onClick={()=>setShowFeedback(true)}>{getText('sendFeedback','Send Feedback')}</button>
        </div>
        <p style={{color:'#6B7280',fontSize:13}}>{getText('footerText','Built for Canadians who want to be heard.')}</p>
        <p style={{color:'#4B5563',fontSize:11,marginTop:8}}>
          {isFrench ? 'Données des représentants : API Represent d\'OpenNorth' : 'Representative data: OpenNorth Represent API'} 
          <span style={{margin:'0 8px'}}>•</span>
          <a href="https://opennorth.ca/" target="_blank" rel="noopener noreferrer" style={{color:'#6B7280',textDecoration:'none'}}>OpenNorth.ca</a>
        </p>
        <p style={{color:'#6B7280',fontSize:12,marginTop:8}}>
          {isFrench ? 'Créé par Pam et Daniel chez LighthouseAI' : 'Made by Pam & Daniel at LighthouseAI'}
        </p>
      </footer>
      
      {/* Modals */}
      <FAQModal isOpen={showFAQ} onClose={()=>setShowFAQ(false)} isFrench={isFrench} />
      <FeedbackModal isOpen={showFeedback} onClose={()=>setShowFeedback(false)} isFrench={isFrench} />
      <PrivacyModal isOpen={showPrivacy} onClose={()=>setShowPrivacy(false)} isFrench={isFrench} />
      <AboutModal isOpen={showAbout} onClose={()=>setShowAbout(false)} isFrench={isFrench} />
      <TermsModal isOpen={showTerms} onClose={()=>setShowTerms(false)} isFrench={isFrench} />
    </div>
  );
}

// Export the renderStep2 and renderStep3 functions separately due to size
export default App;