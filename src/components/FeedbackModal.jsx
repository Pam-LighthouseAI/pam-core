import { useState } from 'react';

function FeedbackModal({ isOpen, onClose, isFrench }) {
  const [form, setForm] = useState({name:'',email:'',message:''});
  const [status, setStatus] = useState('idle'); // idle, sending, success, error
  
  const labels = isFrench ? {
    title: "Envoyer des commentaires",
    subtitle: "Vos commentaires nous aident à améliorer cet outil pour tous les Canadiens.",
    name: "Nom",
    namePlaceholder: "Votre nom",
    email: "Courriel",
    emailPlaceholder: "votre@courriel.com",
    message: "Message",
    messagePlaceholder: "Vos commentaires...",
    sending: "Envoi en cours...",
    submit: "Envoyer",
    success: "Merci pour vos commentaires!",
    error: "Une erreur s'est produite. Veuillez réessayer."
  } : {
    title: "Send Feedback",
    subtitle: "Your feedback helps us improve this tool for all Canadians.",
    name: "Name",
    namePlaceholder: "Your name",
    email: "Email",
    emailPlaceholder: "your@email.com",
    message: "Message",
    messagePlaceholder: "Your feedback...",
    sending: "Sending...",
    submit: "Send Feedback",
    success: "Thank you for your feedback!",
    error: "Something went wrong. Please try again."
  };
  
  if (!isOpen) return null;
  
  const handleSubmit = async () => {
    if (!form.name || !form.email || !form.message) return;
    setStatus('sending');
    try {
      const res = await fetch('/api/feedback', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({...form, timestamp: new Date().toISOString()})
      });
      if (res.ok) {
        setStatus('success');
        setTimeout(() => { setStatus('idle'); onClose(); }, 2000);
      } else {
        setStatus('error');
      }
    } catch(e) {
      setStatus('error');
    }
  };
  
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:16}}>
          <h2 style={{margin:0,fontSize:22}}>{labels.title}</h2>
          <button onClick={onClose} style={{background:'none',border:'none',color:'#9CA3AF',fontSize:28,cursor:'pointer'}}>×</button>
        </div>
        <p style={{color:'#9CA3AF',fontSize:14,marginBottom:20}}>{labels.subtitle}</p>
        {status === 'success' ? (
          <div style={{textAlign:'center',padding:40}}>
            <div style={{fontSize:48,color:'#10B981'}}>✓</div>
            <p style={{marginTop:16}}>{labels.success}</p>
          </div>
        ) : (
          <>
            <div style={{marginBottom:16}}>
              <label style={{display:'block',marginBottom:6,fontSize:14,fontWeight:500}}>{labels.name}</label>
              <input value={form.name} onChange={e => setForm({...form,name:e.target.value})} placeholder={labels.namePlaceholder} />
            </div>
            <div style={{marginBottom:16}}>
              <label style={{display:'block',marginBottom:6,fontSize:14,fontWeight:500}}>{labels.email}</label>
              <input type="email" value={form.email} onChange={e => setForm({...form,email:e.target.value})} placeholder={labels.emailPlaceholder} />
            </div>
            <div style={{marginBottom:20}}>
              <label style={{display:'block',marginBottom:6,fontSize:14,fontWeight:500}}>{labels.message}</label>
              <textarea value={form.message} onChange={e => setForm({...form,message:e.target.value})} placeholder={labels.messagePlaceholder} style={{minHeight:100}} />
            </div>
            {status === 'error' && <p style={{color:'#EF4444',marginBottom:12}}>{labels.error}</p>}
            <button className="btn-primary" onClick={handleSubmit} disabled={status==='sending'} style={{width:'100%'}}>
              {status === 'sending' ? labels.sending : labels.submit}
            </button>
          </>
        )}
      </div>
    </div>
  );
}

export default FeedbackModal;