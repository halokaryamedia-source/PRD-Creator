(async function(){
  const root=document.getElementById('app');
  const parts=[];
  for(let i=1;i<=6;i++){
    const r=await fetch(`preview/content-${String(i).padStart(2,'0')}.html`);
    if(!r.ok) throw new Error('Missing preview fragment '+i);
    parts.push(await r.text());
  }
  root.innerHTML=parts.join('');
  function renderVoice(){
    document.querySelectorAll('article.voice-script-card').forEach(card=>{
      const p=card.querySelector('pre.voice-script-text'); if(!p)return;
      const w=document.createElement('div'); w.className='voice-script-display';
      (p.textContent||'').split(/\n/).forEach(line=>{
        const s=line.trim(),d=document.createElement('div');
        if(!s)d.className='voice-script-gap';
        else if(s.startsWith('[')&&s.endsWith(']')){
          d.className='voice-performance-cues';
          const t=document.createElement('span');t.className='voice-performance-tag';t.textContent=s;d.appendChild(t);
        }else{d.className='voice-script-line';d.textContent=line}
        w.appendChild(d);
      });
      card.appendChild(w);
    });
  }
  function fallbackCopy(text){
    const a=document.createElement('textarea');a.value=text;a.style.position='fixed';a.style.left='-9999px';
    document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(e){}a.remove();
  }
  document.addEventListener('click',e=>{
    const b=e.target.closest('[data-voice-copy],[data-pa-copy]');if(!b)return;
    const id=b.getAttribute('data-voice-copy')||b.getAttribute('data-pa-copy'),s=document.getElementById(id);if(!s)return;
    const text=s.textContent||'',l=b.querySelector('.voice-copy-label,.pa-copy-label'),old=l?l.textContent:b.textContent;
    if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(text).catch(()=>fallbackCopy(text));else fallbackCopy(text);
    if(l)l.textContent='Copied ✓';else b.textContent='Copied ✓';
    setTimeout(()=>{if(l)l.textContent=old;else b.textContent=old},1200);
  });
  renderVoice();
})().catch(err=>{
  document.getElementById('app').innerHTML='<div style="padding:24px;font-family:sans-serif">Preview failed to load: '+err.message+'</div>';
});