(() => {
  const body = document.body;
  const desktopButton = document.getElementById('sidebarToggle');
  const mobileButton = document.getElementById('mobileSidebarButton');
  const scrim = document.getElementById('sidebarScrim');
  const sidebar = document.getElementById('docSidebar');
  const mobileQuery = window.matchMedia('(max-width: 980px)');

  function isMobile() {
    return mobileQuery.matches;
  }

  function updateDesktopButton() {
    if (!desktopButton) return;
    const collapsed = body.classList.contains('sidebar-collapsed');
    desktopButton.setAttribute('aria-expanded', String(!collapsed));
    desktopButton.setAttribute(
      'aria-label',
      collapsed ? 'Expand document navigation' : 'Collapse document navigation'
    );
  }

  function setMobileOpen(open) {
    body.classList.toggle('sidebar-mobile-open', open);
    if (mobileButton) mobileButton.setAttribute('aria-expanded', String(open));
    if (scrim) scrim.hidden = !open;
    if (sidebar) sidebar.setAttribute('aria-hidden', String(isMobile() && !open));
  }

  function restoreDesktopState() {
    let collapsed = false;
    try {
      collapsed = localStorage.getItem('aftershock-sidebar-collapsed') === 'true';
    } catch (_) {}
    body.classList.toggle('sidebar-collapsed', collapsed && !isMobile());
    updateDesktopButton();
  }

  desktopButton?.addEventListener('click', () => {
    if (isMobile()) return;
    const collapsed = !body.classList.contains('sidebar-collapsed');
    body.classList.toggle('sidebar-collapsed', collapsed);
    try {
      localStorage.setItem('aftershock-sidebar-collapsed', String(collapsed));
    } catch (_) {}
    updateDesktopButton();
  });

  mobileButton?.addEventListener('click', () => {
    setMobileOpen(!body.classList.contains('sidebar-mobile-open'));
  });

  scrim?.addEventListener('click', () => setMobileOpen(false));

  document.querySelectorAll('.doc-sidebar a[href^="#"]').forEach((link) => {
    link.addEventListener('click', () => {
      if (isMobile()) setMobileOpen(false);
    });
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && body.classList.contains('sidebar-mobile-open')) {
      setMobileOpen(false);
      mobileButton?.focus();
    }
  });

  mobileQuery.addEventListener?.('change', () => {
    if (isMobile()) {
      body.classList.remove('sidebar-collapsed');
      setMobileOpen(false);
    } else {
      setMobileOpen(false);
      restoreDesktopState();
      sidebar?.removeAttribute('aria-hidden');
    }
  });

  if (isMobile()) {
    body.classList.remove('sidebar-collapsed');
    setMobileOpen(false);
  } else {
    restoreDesktopState();
    sidebar?.removeAttribute('aria-hidden');
  }
})();
