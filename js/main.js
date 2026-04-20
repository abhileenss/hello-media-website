/* =============================================
   HELLO MEDIA — Main JavaScript
   ============================================= */

(function () {
  'use strict';

  /* ─── Cache DOM ──────────────────────────── */
  const navbar      = document.getElementById('navbar');
  const navLinks    = document.querySelectorAll('.nav-link[href^="#"]');
  const hamburger   = document.getElementById('hamburger');
  const sections    = document.querySelectorAll('section[id]');

  // Inject mobile menu element after navbar
  let mobileMenu = document.getElementById('nav-mobile');
  if (!mobileMenu) {
    mobileMenu = document.createElement('div');
    mobileMenu.id = 'nav-mobile';
    mobileMenu.className = 'nav-mobile';
    // Mirror nav links into mobile menu
    const hrefs = [
      ['#who-we-are',   'WHO WE ARE'],
      ['#what-we-do',   'WHAT WE DO'],
      ['#whom-we-love', 'WHOM WE LOVE'],
      ['#how-we-do-it', 'HOW WE DO IT'],
      ['#where-we-are', 'WHERE WE ARE'],
    ];
    hrefs.forEach(([href, label]) => {
      const a = document.createElement('a');
      a.href = href;
      a.textContent = label;
      mobileMenu.appendChild(a);
    });
    navbar.insertAdjacentElement('afterend', mobileMenu);
  }

  /* ─── Throttled scroll handler ───────────── */
  let ticking = false;
  let lastScrollY = 0;

  function onScroll() {
    const scrollY = window.scrollY;
    lastScrollY = scrollY;

    // Scrolled class on nav
    navbar.classList.toggle('scrolled', scrollY > 50);

    // Hero parallax
    const hero = document.getElementById('hero');
    if (hero) {
      const heroBg = hero.querySelector('.hero-bg-img');
      if (heroBg && scrollY < window.innerHeight * 1.5) {
        heroBg.style.transform = `translateY(${scrollY * 0.22}px)`;
      }
    }

    updateScrollSpy();
    revealElements();
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(onScroll);
      ticking = true;
    }
  }, { passive: true });

  /* ─── Scroll-spy ─────────────────────────── */
  function updateScrollSpy() {
    const threshold = window.scrollY + window.innerHeight * 0.38;
    let currentId = '';

    sections.forEach(sec => {
      if (sec.offsetTop <= threshold) currentId = sec.id;
    });

    navLinks.forEach(link => {
      const id = (link.getAttribute('href') || '').replace('#', '');
      link.classList.toggle('active', id === currentId);
    });
  }

  /* ─── Smooth scroll helper ───────────────── */
  function smoothScrollTo(targetId) {
    const target = document.querySelector(targetId);
    if (!target) return;
    const offset = navbar ? navbar.offsetHeight : 0;
    const top = target.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top, behavior: 'smooth' });
  }

  /* ─── Bind smooth scroll ─────────────────── */
  function bindLinks(nodeList) {
    nodeList.forEach(link => {
      link.addEventListener('click', e => {
        const href = link.getAttribute('href');
        if (!href || !href.startsWith('#')) return;
        e.preventDefault();
        smoothScrollTo(href);
        closeMobileMenu();
      });
    });
  }

  bindLinks(navLinks);
  bindLinks(mobileMenu.querySelectorAll('a'));

  /* ─── Hamburger / mobile menu ────────────── */
  function openMobileMenu() {
    mobileMenu.classList.add('open');
    hamburger.setAttribute('aria-expanded', 'true');
    const bars = hamburger.querySelectorAll('span');
    if (bars[0]) bars[0].style.transform = 'translateY(7px) rotate(45deg)';
    if (bars[1]) bars[1].style.opacity = '0';
    if (bars[2]) bars[2].style.transform = 'translateY(-7px) rotate(-45deg)';
  }

  function closeMobileMenu() {
    if (!mobileMenu.classList.contains('open')) return;
    mobileMenu.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    const bars = hamburger.querySelectorAll('span');
    bars.forEach(b => { b.style.transform = ''; b.style.opacity = ''; });
  }

  if (hamburger) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.contains('open') ? closeMobileMenu() : openMobileMenu();
    });
  }

  document.addEventListener('click', e => {
    if (
      mobileMenu.classList.contains('open') &&
      !mobileMenu.contains(e.target) &&
      hamburger && !hamburger.contains(e.target)
    ) {
      closeMobileMenu();
    }
  });

  /* ─── Scroll reveal ──────────────────────── */
  function revealElements() {
    const trigger = window.innerHeight * 0.88;
    document.querySelectorAll('.reveal').forEach(el => {
      if (el.getBoundingClientRect().top < trigger) {
        el.classList.add('revealed');
      }
    });
  }

  /* ─── Add reveal classes to key elements ──── */
  function addRevealClasses() {
    // Only add reveal to cards (never block-text — that caused blank sections)
    const selectors = ['.service-card', '.love-card', '.philosophy-card'];
    selectors.forEach(sel => {
      document.querySelectorAll(sel).forEach((el, i) => {
        el.classList.add('reveal');
        el.style.transitionDelay = `${i * 0.06}s`;
      });
    });
  }

  /* ─── Subtle tilt on hover ───────────────── */
  function bindTilt() {
    document.querySelectorAll('.service-card').forEach(card => {
      card.addEventListener('mousemove', e => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width  - 0.5;
        const y = (e.clientY - r.top)  / r.height - 0.5;
        card.style.transform = `perspective(600px) rotateY(${x*3.5}deg) rotateX(${-y*3.5}deg) translateZ(4px)`;
      });
      card.addEventListener('mouseleave', () => { card.style.transform = ''; });
    });
  }

  /* ─── Init ───────────────────────────────── */
  function init() {
    addRevealClasses();
    revealElements();
    bindTilt();
    onScroll(); // run once on load

    window.addEventListener('resize', revealElements);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
