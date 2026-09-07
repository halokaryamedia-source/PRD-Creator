(function(){
  function fallbackCopy(text){
    var area=document.createElement('textarea');
    area.value=text;
    area.setAttribute('readonly','');
    area.style.position='fixed';
    area.style.opacity='0';
    document.body.appendChild(area);
    area.select();
    try{document.execCommand('copy');}finally{document.body.removeChild(area);}
  }
  document.addEventListener('click',function(event){
    var button=event.target.closest('[data-pa-copy]');
    if(!button)return;
    var source=document.getElementById(button.getAttribute('data-pa-copy'));
    if(!source)return;
    var text=source.textContent||'';
    var label=button.querySelector('.pa-copy-label');
    var original=label?label.textContent:'Copy';
    var done=function(){
      button.classList.add('is-copied');
      if(label)label.textContent='Copied ✓';
      setTimeout(function(){
        button.classList.remove('is-copied');
        if(label)label.textContent=original;
      },1400);
    };
    if(navigator.clipboard&&navigator.clipboard.writeText){
      navigator.clipboard.writeText(text).then(done,function(){fallbackCopy(text);done();});
    }else{
      fallbackCopy(text);done();
    }
  });
})();
