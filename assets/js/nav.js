// Mobile nav toggle, footer year, image lightbox.
(function () {

  /* ---------- Mobile nav ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') links.classList.remove('open');
    });
  }

  /* ---------- Footer year ---------- */
  var yr = document.getElementById('year');
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---------- Lightbox ---------- */
  // Auto-wires every <img> inside these selectors as a zoomable item.
  // Clicking opens an overlay at full size. Esc/click-outside/X closes.
  // ←/→ navigate within the page's image set.
  var SELECTORS = [
    '.case-hero-image img',
    '.gallery img',
    '.phone-strip .phone img'
  ];

  function collectTargets() {
    var nodes = document.querySelectorAll(SELECTORS.join(','));
    return Array.prototype.slice.call(nodes);
  }

  var targets = collectTargets();
  if (!targets.length) return;

  // Build overlay once
  var overlay = document.createElement('div');
  overlay.className = 'lightbox';
  overlay.setAttribute('role', 'dialog');
  overlay.setAttribute('aria-modal', 'true');
  overlay.setAttribute('aria-label', 'Image viewer');
  overlay.hidden = true;
  overlay.innerHTML = [
    '<button class="lightbox-close" type="button" aria-label="Close (Esc)">',
    '  <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/></svg>',
    '</button>',
    '<button class="lightbox-prev" type="button" aria-label="Previous (Left arrow)">',
    '  <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>',
    '</button>',
    '<button class="lightbox-next" type="button" aria-label="Next (Right arrow)">',
    '  <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>',
    '</button>',
    '<div class="lightbox-stage">',
    '  <img class="lightbox-img" alt="" />',
    '  <figcaption class="lightbox-caption"></figcaption>',
    '  <div class="lightbox-count" aria-live="polite"></div>',
    '</div>'
  ].join('');
  document.body.appendChild(overlay);

  var imgEl     = overlay.querySelector('.lightbox-img');
  var capEl     = overlay.querySelector('.lightbox-caption');
  var countEl   = overlay.querySelector('.lightbox-count');
  var btnClose  = overlay.querySelector('.lightbox-close');
  var btnPrev   = overlay.querySelector('.lightbox-prev');
  var btnNext   = overlay.querySelector('.lightbox-next');
  var stageEl   = overlay.querySelector('.lightbox-stage');

  var current = 0;
  var prevFocus = null;

  function captionFor(node) {
    // Prefer a sibling <figcaption>, then alt text.
    var parent = node.closest('figure');
    if (parent) {
      var fc = parent.querySelector('figcaption');
      if (fc) return fc.textContent.trim();
    }
    return node.getAttribute('alt') || '';
  }

  function bestSrcFor(node) {
    // Use currentSrc when available (handles <picture>/srcset). Fall back to src.
    return node.currentSrc || node.src;
  }

  function show(i) {
    if (i < 0) i = targets.length - 1;
    if (i >= targets.length) i = 0;
    current = i;
    var node = targets[i];
    imgEl.src = bestSrcFor(node);
    imgEl.alt = node.alt || '';
    var cap = captionFor(node);
    capEl.textContent = cap;
    capEl.hidden = !cap;
    countEl.textContent = (i + 1) + ' / ' + targets.length;
    countEl.hidden = targets.length < 2;
    btnPrev.hidden = targets.length < 2;
    btnNext.hidden = targets.length < 2;
  }

  function open(i) {
    prevFocus = document.activeElement;
    show(i);
    overlay.hidden = false;
    document.body.classList.add('lightbox-open');
    // Give focus to close button so Esc/Enter work immediately.
    setTimeout(function () { btnClose.focus(); }, 0);
    document.addEventListener('keydown', onKey);
  }

  function close() {
    overlay.hidden = true;
    document.body.classList.remove('lightbox-open');
    document.removeEventListener('keydown', onKey);
    imgEl.removeAttribute('src');
    if (prevFocus && prevFocus.focus) prevFocus.focus();
  }

  function onKey(e) {
    if (e.key === 'Escape') { e.preventDefault(); close(); }
    else if (e.key === 'ArrowLeft') { e.preventDefault(); show(current - 1); }
    else if (e.key === 'ArrowRight') { e.preventDefault(); show(current + 1); }
  }

  // Wire up targets
  targets.forEach(function (node, i) {
    node.classList.add('zoomable');
    node.setAttribute('tabindex', '0');
    node.setAttribute('role', 'button');
    node.setAttribute('aria-label', 'Open ' + (node.alt || 'image') + ' in lightbox');
    node.addEventListener('click', function (e) {
      e.preventDefault();
      open(i);
    });
    node.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(i); }
    });
  });

  // Overlay interactions
  btnClose.addEventListener('click', close);
  btnPrev .addEventListener('click', function () { show(current - 1); });
  btnNext .addEventListener('click', function () { show(current + 1); });
  overlay.addEventListener('click', function (e) {
    // Click on backdrop (anywhere outside the image/buttons) closes.
    if (e.target === overlay || e.target === stageEl) close();
  });

})();
