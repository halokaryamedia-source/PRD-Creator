(function(){
  const body = document.body;
  const modeControl = document.getElementById('viewModeSwitch');
  const themeControl = document.getElementById('themeModeSwitch');
  const modeLabels = Array.from(document.querySelectorAll('[data-mode-label]'));
  const groups = Array.from(document.querySelectorAll('.nav-group'));
  const navTargets = Array.from(document.querySelectorAll('[data-target]'));
  const phaseItems = Array.from(document.querySelectorAll('[data-phase-nav]'));
  const documentSheets = Array.from(document.querySelectorAll('section.sheet[id]'));

  function currentMode(){
    return body.classList.contains('view-clean') ? 'clean' : 'professional';
  }

  function updateThemeUI(theme){
    const dark = theme === 'dark';

    body.classList.toggle('theme-dark', dark);
    body.classList.toggle('theme-normal', !dark);
    themeControl.dataset.theme = theme;
    themeControl.setAttribute('aria-checked', String(dark));
    themeControl.setAttribute('aria-label', dark ? 'Disable dark mode' : 'Enable dark mode');
    themeControl.setAttribute('title', dark ? 'Switch to normal mode' : 'Switch to dark mode');

    document.documentElement.style.colorScheme = dark ? 'dark' : 'light';

    try {
      localStorage.setItem('aftershock-document-theme', theme);
    } catch(e) {}
  }

  function updateModeUI(mode){
    const professional = mode === 'professional';

    body.classList.toggle('view-clean', !professional);
    body.classList.toggle('view-professional', professional);
    modeControl.dataset.mode = mode;

    document.querySelectorAll('.nav-index[data-full-index]').forEach(function(index){
      index.textContent = professional
        ? index.dataset.fullIndex
        : index.dataset.overviewIndex;
    });

    modeLabels.forEach(function(label){
      const active = label.dataset.modeLabel === mode;
      label.classList.toggle('is-active', active);
      label.setAttribute('aria-pressed', String(active));
    });

    try {
      localStorage.setItem('aftershock-document-view', mode);
    } catch(e) {}

    if (!professional) {
      const currentHash = (location.hash || '#summary').slice(1);
      const currentSection = document.getElementById(currentHash);

      if (currentSection && currentSection.classList.contains('professional-only')) {
        const cleanTarget = currentSection.dataset.cleanTarget
          || (currentSection.dataset.phase
            ? currentSection.dataset.phase + '-experience'
            : 'summary');

        history.replaceState(null, '', '#' + cleanTarget);
        document.getElementById(cleanTarget)?.scrollIntoView({
          behavior:'smooth',
          block:'start'
        });
      }
    }

    requestAnimationFrame(updateActiveNavigation);
  }

  modeLabels.forEach(function(label){
    label.addEventListener('click', function(){
      updateModeUI(label.dataset.modeLabel);
    });
  });

  themeControl.addEventListener('click', function(){
    updateThemeUI(body.classList.contains('theme-dark') ? 'normal' : 'dark');
  });

  groups.forEach(function(group){
    const button = group.querySelector('.nav-group-toggle');
    if (!button) return;

    button.addEventListener('click', function(){
      const open = group.classList.toggle('is-open');
      button.setAttribute('aria-expanded', String(open));
    });
  });

  function setActivePhase(phase, pageId){
    const overviewMode = body.classList.contains('view-clean');

    phaseItems.forEach(function(item){
      const current = item.dataset.phaseNav === phase;
      item.classList.toggle('is-current', current);

      const mainLink = item.querySelector('.phase-nav-main');
      if (mainLink){
        mainLink.classList.toggle('is-active', current);
      }

      item.querySelectorAll('.phase-page-link').forEach(function(link){
        link.classList.toggle(
          'is-active',
          !overviewMode && current && link.dataset.target === pageId
        );
      });
    });
  }

  function activateSection(section){
    if (!section) return;

    const id = section.id;
    const phase = section.dataset.phase || '';

    navTargets.forEach(function(link){
      if (link.classList.contains('phase-nav-main')
          || link.classList.contains('phase-page-link')) {
        return;
      }
      link.classList.toggle('is-active', link.dataset.target === id);
    });

    groups.forEach(function(group){
      const activeChild = group.querySelector('[data-target="' + id + '"]');
      const gameplayChild = phase && group.querySelector('[data-phase-nav="' + phase + '"]');
      const active = Boolean(activeChild || gameplayChild);

      group.classList.toggle('has-active', active);

      if (active){
        group.classList.add('is-open');
        const button = group.querySelector('.nav-group-toggle');
        if (button) button.setAttribute('aria-expanded', 'true');
      }
    });

    if (phase){
      setActivePhase(phase, id);
    } else {
      phaseItems.forEach(function(item){
        item.classList.remove('is-current');
        item.querySelector('.phase-nav-main')?.classList.remove('is-active');
        item.querySelectorAll('.phase-page-link').forEach(function(link){
          link.classList.remove('is-active');
        });
      });
    }
  }

  function findCurrentSection(){
    const visible = documentSheets.filter(function(section){
      return section.offsetParent !== null;
    });

    let current = null;
    let bestScore = Infinity;

    visible.forEach(function(section){
      const rect = section.getBoundingClientRect();

      if (rect.bottom <= 92) return;

      const reference = 118;
      const score = rect.top <= reference
        ? Math.abs(rect.top - reference) * 0.35
        : Math.abs(rect.top - reference);

      if (score < bestScore){
        current = section;
        bestScore = score;
      }
    });

    return current;
  }

  function updateActiveNavigation(){
    activateSection(findCurrentSection());
  }

  navTargets.forEach(function(link){
    link.addEventListener('click', function(){
      const target = document.getElementById(link.dataset.target);
      if (!target) return;

      requestAnimationFrame(function(){
        activateSection(target);
      });
    });
  });

  document.querySelectorAll('[data-section-target]').forEach(function(link){
    link.addEventListener('click', function(event){
      const target = document.getElementById(link.dataset.sectionTarget);
      if (!target) return;

      event.preventDefault();

      if (body.classList.contains('view-clean')
          && target.classList.contains('professional-only')) {
        updateModeUI('professional');
      }

      history.replaceState(null, '', '#' + target.id);

      requestAnimationFrame(function(){
        target.scrollIntoView({behavior:'smooth', block:'start'});
        activateSection(target);
      });
    });
  });

  window.addEventListener('scroll', updateActiveNavigation, {passive:true});
  window.addEventListener('resize', updateActiveNavigation);

  let savedMode = 'professional';
  let savedTheme = 'normal';

  try {
    savedMode = localStorage.getItem('aftershock-document-view') || 'professional';
    savedTheme = localStorage.getItem('aftershock-document-theme') || 'normal';
  } catch(e) {}

  updateThemeUI(savedTheme === 'dark' ? 'dark' : 'normal');
  updateModeUI(savedMode === 'clean' ? 'clean' : 'professional');

  const initial = document.getElementById((location.hash || '#summary').slice(1))
    || document.getElementById('summary');
  activateSection(initial);

  /* V94 language switch */
  const languageControl = document.getElementById('languageSwitch');
  const languageOptions = Array.from(document.querySelectorAll('[data-language-option]'));
  const i18nNodes = Array.from(document.querySelectorAll('.i18n-text'));

  function updateLanguage(language){
    const selected = language === 'id' ? 'id' : 'en';
    document.documentElement.lang = selected === 'id' ? 'id' : 'en';
    languageControl.dataset.language = selected;
    languageOptions.forEach(function(button){
      const active = button.dataset.languageOption === selected;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    i18nNodes.forEach(function(node){
      const value = selected === 'id' ? node.dataset.id : node.dataset.en;
      if (typeof value === 'string') node.textContent = value;
    });
    try { localStorage.setItem('aftershock-document-language', selected); } catch(e) {}
  }

  languageOptions.forEach(function(button){
    button.addEventListener('click', function(){ updateLanguage(button.dataset.languageOption); });
  });

  let savedLanguage = 'en';
  try { savedLanguage = localStorage.getItem('aftershock-document-language') || 'en'; } catch(e) {}
  updateLanguage(savedLanguage);

})();
