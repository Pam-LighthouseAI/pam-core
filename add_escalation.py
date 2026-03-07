# Replace the Escalation Component placeholder with the actual component
with open(r'D:\MyCivicVoice_Deploy\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the placeholder
old_placeholder = '''{/* Escalation Component Placeholder - Job 2/6 */}
        {/* 
        TODO: Job 3 - Wire up escalation lookup logic
        - Check if selIssue.primary === 'municipal'
        - Use reps.municipal[0]?.representative_set_name to lookup ESCALATION_DATA
        - Display 311/portal info for municipal issues
        - Show fallback message for rural users without 311
        */}'''

new_component = '''{/* Escalation Card - Show 311/portal info for municipal issues */}
        {selIssue && selIssue.primary === 'municipal' && reps.municipal && reps.municipal.length > 0 && reps.municipal[0].representativeSetName && (
          (() => {
            const escalationInfo = typeof getEscalationInfo === 'function' ? getEscalationInfo(reps.municipal[0].representativeSetName) : null;
            if (!escalationInfo) return null;
            
            return (
              <div style={{
                background: 'linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(6, 78, 59, 0.15) 100%)',
                border: '1px solid rgba(16, 185, 129, 0.3)',
                borderRadius: 12,
                padding: '16px 18px',
                marginBottom: 20
              }}>
                <div style={{ display: 'flex', alignItems: 'center', marginBottom: 12 }}>
                  <span style={{ fontSize: 20, marginRight: 10 }}>📞</span>
                  <h4 style={{ margin: 0, color: '#34D399', fontSize: 16, fontWeight: 600 }}>
                    {isFrench ? (FR.escalationTitle || 'Signaler directement \u00e0 votre ville') : 'Report Directly to Your City'}
                  </h4>
                </div>
                <p style={{ color: '#9CA3AF', fontSize: 13, marginBottom: 14, lineHeight: 1.5 }}>
                  {isFrench ? (FR.escalationSubtitle || 'Pour les questions municipales, vous pouvez souvent obtenir des r\u00e9sultats plus rapidement en signalant directement \u00e0 votre ville.') : 'For municipal issues, you can often get faster results by reporting directly to your city.'}
                </p>
                <div style={{ background: 'rgba(0,0,0,0.2)', borderRadius: 8, padding: 12 }}>
                  <div style={{ fontWeight: 600, color: '#10B981', marginBottom: 8, fontSize: 14 }}>
                    {isFrench ? (escalationInfo.nameFr || escalationInfo.name) : escalationInfo.name}
                  </div>
                  {escalationInfo.phone && (
                    <div style={{ marginBottom: 6 }}>
                      <span style={{ color: '#FBBF24', fontWeight: 500, fontSize: 13 }}>
                        {isFrench ? (FR.escalationPhone || 'T\u00e9l\u00e9phone') : 'Phone'}:
                      </span>
                      {' '}
                      <a href={`tel:${escalationInfo.phone}`} style={{ color: '#60A5FA', textDecoration: 'none', fontSize: 13 }}>
                        {escalationInfo.phone}
                      </a>
                    </div>
                  )}
                  {escalationInfo.url && (
                    <div style={{ marginBottom: 6 }}>
                      <span style={{ color: '#FBBF24', fontWeight: 500, fontSize: 13 }}>
                        {isFrench ? (FR.escalationWebsite || 'Site web') : 'Website'}:
                      </span>
                      {' '}
                      <a href={escalationInfo.url} target="_blank" rel="noopener noreferrer" style={{ color: '#60A5FA', textDecoration: 'none', fontSize: 13 }}>
                        {isFrench ? (FR.escalationReportOnline || 'Signaler en ligne') : 'Report Online'} \u2197
                      </a>
                    </div>
                  )}
                  <div style={{ marginTop: 8, fontSize: 12, color: '#6B7280', lineHeight: 1.5 }}>
                    {isFrench ? (escalationInfo.descriptionFr || escalationInfo.description) : escalationInfo.description}
                  </div>
                </div>
                <div style={{ marginTop: 10, fontSize: 12, color: '#6B7280', fontStyle: 'italic' }}>
                  \u2139\uFE0F {isFrench ? (FR.escalationBeforeRep || 'Avant de contacter votre repr\u00e9sentant') : 'Before contacting your representative, consider reporting directly to your city for faster resolution.'}
                </div>
              </div>
            );
          })()
        )}
        
        {/* Fallback for rural users without 311 */}
        {selIssue && selIssue.primary === 'municipal' && (!reps.municipal || reps.municipal.length === 0 || !reps.municipal[0].representativeSetName) && (
          <div style={{
            background: 'linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(180, 83, 9, 0.15) 100%)',
            border: '1px solid rgba(245, 158, 11, 0.3)',
            borderRadius: 12,
            padding: '16px 18px',
            marginBottom: 20
          }}>
            <div style={{ display: 'flex', alignItems: 'center', marginBottom: 8 }}>
              <span style={{ fontSize: 20, marginRight: 10 }}>\u26A0\uFE0F</span>
              <h4 style={{ margin: 0, color: '#FBBF24', fontSize: 16, fontWeight: 600 }}>
                {isFrench ? (FR.escalationRuralNote || 'Conseil pour les r\u00e9gions rurales') : 'Tip for Rural Areas'}
              </h4>
            </div>
            <p style={{ color: '#9CA3AF', fontSize: 13, lineHeight: 1.5, margin: 0 }}>
              {isFrench ? (FR.escalationRuralDesc || 'Les r\u00e9gions rurales n\'ont souvent pas de service 311. Contactez votre conseiller municipal ou le bureau municipal directement.') : 'Rural areas often don\'t have 311 service. Contact your municipal councillor or town office directly for local issues.'}
            </p>
          </div>
        )}'''

# Replace
if old_placeholder in content:
    new_content = content.replace(old_placeholder, new_component)
    with open(r'D:\MyCivicVoice_Deploy\index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Successfully replaced placeholder with EscalationCard component')
else:
    print('Placeholder not found')
    # Try to find a smaller match
    idx = content.find('Escalation Component Placeholder')
    if idx != -1:
        print(f'Found at index {idx}')
        print('Context:', content[idx-50:idx+100])