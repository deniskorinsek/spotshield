/* SpotShield website — theme, menu, hero deck, compare slider, reveals, parallax. No dependencies. */
(function () {
  'use strict';

  var doc = document, root = doc.documentElement, body = doc.body;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var finePointer = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var raf = window.requestAnimationFrame || function (f) { return setTimeout(f, 16); };

  /* ---------- theme ---------- */
  var THEME_KEY = 'spotshield-theme';
  var themeBtn = doc.querySelector('.theme');
  var themeMeta = doc.querySelector('meta[name="theme-color"]');
  function applyTheme(t) {
    root.setAttribute('data-theme', t);
    if (themeMeta) themeMeta.setAttribute('content', t === 'light' ? '#F1EFE6' : '#0B1424');
    if (themeBtn) themeBtn.setAttribute('aria-label', themeBtn.getAttribute(t === 'light' ? 'data-label-light' : 'data-label-dark'));
  }
  applyTheme(root.getAttribute('data-theme') === 'light' ? 'light' : 'dark');
  if (themeBtn) themeBtn.addEventListener('click', function () {
    var t = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    applyTheme(t);
    try { localStorage.setItem(THEME_KEY, t); } catch (e) { /* storage unavailable */ }
  });

  /* ---------- nav ---------- */
  var nav = doc.querySelector('.nav');
  var menuBtn = doc.querySelector('.menu-btn');
  function closeMenu() {
    if (!nav || !menuBtn) return;
    nav.classList.remove('open');
    menuBtn.setAttribute('aria-expanded', 'false');
  }
  if (nav && menuBtn) {
    menuBtn.addEventListener('click', function () {
      var open = !nav.classList.contains('open');
      nav.classList.toggle('open', open);
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('.nav-links a').forEach(function (a) { a.addEventListener('click', closeMenu); });
    doc.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(); });
  }
  var scrolled = false;
  function onNavScroll() {
    var s = (window.scrollY || root.scrollTop) > 8;
    if (s !== scrolled && nav) { scrolled = s; nav.classList.toggle('scrolled', s); }
  }

  /* ---------- hero intro ---------- */
  if (reduce) body.classList.add('ready');
  else setTimeout(function () { body.classList.add('ready'); }, 70);

  /* ---------- hero deck ---------- */
  var deck = doc.getElementById('deck');
  var cards = deck ? Array.prototype.slice.call(deck.querySelectorAll('.card')) : [];
  var picks = Array.prototype.slice.call(doc.querySelectorAll('.picker [data-pick]'));
  var bars = Array.prototype.slice.call(doc.querySelectorAll('.deck-foot .bars span'));
  var counter = doc.getElementById('deck-n');
  var N = cards.length, sel = 0, holdUntil = 0, deckVisible = true, deckHover = false;
  function renderDeck() {
    cards.forEach(function (c, i) {
      var p = (i - sel + N) % N;
      c.className = 'card ' + (c.getAttribute('data-app') || '') + ' ' + (p === 0 ? 'pos-0' : p === 1 ? 'pos-1' : p === 2 ? 'pos-2' : 'pos-n');
      c.setAttribute('aria-hidden', p === 0 ? 'false' : 'true');
    });
    picks.forEach(function (b, i) { b.setAttribute('aria-pressed', i === sel ? 'true' : 'false'); });
    bars.forEach(function (b, i) { b.classList.toggle('on', i === sel); });
    if (counter) counter.textContent = (sel + 1 < 10 ? '0' : '') + (sel + 1);
  }
  function select(i, hold) {
    sel = (i + N) % N;
    if (hold) holdUntil = Date.now() + 9000;
    renderDeck();
  }
  if (N) {
    renderDeck();
    picks.forEach(function (b, i) { b.addEventListener('click', function () { select(i, true); }); });
    if (!reduce) {
      setInterval(function () {
        if (doc.hidden || !deckVisible || deckHover || Date.now() < holdUntil) return;
        select(sel + 1, false);
      }, 3600);
    }
    var stage = doc.querySelector('.hero-stage');
    if (stage) {
      stage.addEventListener('mouseenter', function () { deckHover = true; });
      stage.addEventListener('mouseleave', function () { deckHover = false; });
      if (finePointer && !reduce) {
        stage.addEventListener('mousemove', function (e) {
          var r = stage.getBoundingClientRect();
          var dx = (e.clientX - r.left) / r.width - 0.5, dy = (e.clientY - r.top) / r.height - 0.5;
          deck.style.setProperty('--ry', (dx * 7).toFixed(2) + 'deg');
          deck.style.setProperty('--rx', (-dy * 5).toFixed(2) + 'deg');
        });
        stage.addEventListener('mouseleave', function () { deck.style.removeProperty('--ry'); deck.style.removeProperty('--rx'); });
      }
    }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) { deckVisible = en[0].isIntersecting; }, { threshold: 0.05 }).observe(deck);
    }
    // swipe on touch screens
    var tx = null;
    deck.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
    deck.addEventListener('touchend', function (e) {
      if (tx === null) return;
      var d = e.changedTouches[0].clientX - tx; tx = null;
      if (Math.abs(d) > 40) select(sel + (d < 0 ? 1 : -1), true);
    }, { passive: true });
  }

  /* ---------- compare slider ---------- */
  var compare = doc.querySelector('.compare');
  var range = compare ? compare.querySelector('input[type="range"]') : null;
  var sweepDone = false;
  function setSplit(v) { compare.style.setProperty('--split', v + '%'); }
  if (compare && range) {
    setSplit(reduce ? range.value : 100);
    var onRange = function () { sweepDone = true; setSplit(range.value); };
    range.addEventListener('input', onRange);
    range.addEventListener('change', onRange);
  }
  function sweepCompare() {
    if (!compare || !range || sweepDone) return;
    sweepDone = true;
    if (reduce) { setSplit(range.value); return; }
    var from = 100, to = Number(range.value), t0 = null, dur = 1500;
    function ease(x) { return 1 - Math.pow(1 - x, 3); }
    function step(ts) {
      if (t0 === null) t0 = ts;
      var k = Math.min(1, (ts - t0) / dur);
      setSplit((from + (to - from) * ease(k)).toFixed(2));
      if (k < 1) raf(step);
    }
    setTimeout(function () { raf(step); }, 350);
  }

  /* ---------- scroll reveals ---------- */
  var sections = Array.prototype.slice.call(doc.querySelectorAll('[data-reveal]'));
  function revealAll() { sections.forEach(function (s) { s.classList.add('in'); }); sweepCompare(); }
  if (reduce || !('IntersectionObserver' in window)) {
    revealAll();
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add('in');
        if (en.target.id === 'demo') sweepCompare();
        io.unobserve(en.target);
      });
    }, { threshold: 0, rootMargin: '0px 0px -12% 0px' });
    sections.forEach(function (s) { io.observe(s); });
    window.addEventListener('beforeprint', revealAll);
  }

  /* ---------- parallax ---------- */
  var layers = Array.prototype.slice.call(doc.querySelectorAll('[data-parallax]')).map(function (el) {
    return { el: el, f: parseFloat(el.getAttribute('data-parallax')) || 0, ref: el.closest('[data-parallax-root]') || el.parentElement };
  });
  var ticking = false;
  function parallax() {
    ticking = false;
    var vh = window.innerHeight || root.clientHeight;
    layers.forEach(function (l) {
      var r = l.ref.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      var rel = (r.top + r.height / 2 - vh / 2) / vh;      // -1 … 1 across the viewport
      var y = Math.max(-220, Math.min(220, -rel * l.f * vh));
      l.el.style.setProperty('--py', y.toFixed(1) + 'px');
    });
  }
  function onScroll() {
    onNavScroll();
    if (reduce || !layers.length || ticking) return;
    ticking = true;
    raf(parallax);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  onScroll();
  if (!reduce) parallax();
})();
