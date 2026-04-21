/* Hello Media — v2 site JS
   - Intro overlay (once per session)
   - Nav mobile toggle + active state
   - Scroll reveal
*/
(function () {
  'use strict';

  // ───── Intro overlay ───────────────────────────
  const intro = document.querySelector('.intro-overlay');
  if (intro) {
    const seen = sessionStorage.getItem('hm_intro_seen');
    if (seen) {
      intro.classList.add('is-done');
    } else {
      requestAnimationFrame(() => intro.classList.add('is-playing'));
      setTimeout(() => {
        intro.classList.add('is-done');
        sessionStorage.setItem('hm_intro_seen', '1');
      }, 1900);
    }
  }

  // ───── Mobile nav ──────────────────────────────
  const toggle = document.querySelector('.nav__toggle');
  const links  = document.querySelector('.nav__links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = toggle.classList.toggle('is-open');
      links.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
    });
    links.addEventListener('click', (e) => {
      if (e.target.matches('a')) {
        toggle.classList.remove('is-open');
        links.classList.remove('is-open');
      }
    });
  }

  // ───── Active nav link based on current path ──
  const path = location.pathname.replace(/\/$/, '') || '/';
  document.querySelectorAll('.nav__link').forEach((a) => {
    const href = a.getAttribute('href') || '';
    if (!href || href === '#') return;
    const normalized = href.replace(/\/$/, '').replace(/\.html$/, '');
    if (normalized && path.endsWith(normalized)) a.classList.add('is-active');
  });

  // ───── Scroll reveal ───────────────────────────
  const targets = document.querySelectorAll('[data-reveal]');
  if (targets.length && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    targets.forEach((t) => io.observe(t));
  } else {
    targets.forEach((t) => t.classList.add('is-in'));
  }
})();
