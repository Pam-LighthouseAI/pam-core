#!/usr/bin/env python3
"""Add error display to My Civic Voice"""

filepath = r"D:\source_extracted\my_civic_voice.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and update the loading/error display section in renderStep3
old_loading_display = """{loading ? (
          <div style={{textAlign:'center',padding:40}}><div className="spinner" /></div>
        ) : ("""
new_loading_display = """{loading ? (
          <div style={{textAlign:'center',padding:40}}>
            <div className="spinner" />
            <p style={{color:'#9CA3AF',marginTop:16,fontSize:14}}>{isFrench ? (FR.loadingReps || 'Chargement de vos représentants...') : 'Loading your representatives...'}</p>
          </div>
        ) : error ? (
          <div style={{textAlign:'center',padding:40}}>
            <div style={{fontSize:48,marginBottom:16}}>⚠️</div>
            <h3 style={{margin:'0 0 8px 0',color:'#F87171'}}>{isFrench ? (FR.errorFetching || 'Error fetching representatives') : 'Error fetching representatives'}</h3>
            <p style={{color:'#9CA3AF',marginBottom:20}}>{isFrench ? (FR.errorTryAgain || 'Please try again or use the alternative links below.') : 'Please try again or use the alternative links below.'}</p>
            <button className="btn-secondary" onClick={()=>{setError('');setStep(1);}} style={{marginBottom:20}}>{isFrench ? 'Réessayer' : 'Try Again'}</button>
          </div>
        ) : ("""

content = content.replace(old_loading_display, new_loading_display)

# Save the file
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Error display added!")