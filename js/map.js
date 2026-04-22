/* Hello Media — Interactive world map
   Pins + tooltip on hover.
   Coordinates are percentage (x,y) inside a 1000×520 viewBox of the map SVG.
*/
(function () {
  'use strict';

  const HUBS = [
    { id: 'uae',    name: 'UAE (Headquarters)', addr: 'Dubai Media City, Dubai, United Arab Emirates', type: 'hub',    x: 640, y: 245, href: '/where-we-are/uae/' },
    { id: 'uk',     name: 'United Kingdom',     addr: 'London — Market Hub',                            type: 'hub',    x: 482, y: 170, href: '/where-we-are/uk/' },
    { id: 'usa',    name: 'United States',      addr: 'New York — Market Hub',                          type: 'hub',    x: 258, y: 205, href: '/where-we-are/usa/' },
    { id: 'brazil', name: 'Brazil',             addr: 'São Paulo — Market Hub',                         type: 'hub',    x: 360, y: 360, href: '/where-we-are/brazil/' },
    { id: 'china',  name: 'China',              addr: 'Shanghai — Market Hub',                          type: 'hub',    x: 820, y: 225, href: '/where-we-are/china/' },
    { id: 'egypt',  name: 'Egypt',              addr: 'Cairo — Market Hub',                             type: 'hub',    x: 552, y: 245, href: '/where-we-are/egypt/' },
    { id: 'india',  name: 'India',              addr: 'Mumbai — Production Studio',                     type: 'studio', x: 720, y: 260 },
    { id: 'pak',    name: 'Pakistan',           addr: 'Karachi — Production Studio',                    type: 'studio', x: 700, y: 245 },
  ];

  const stage = document.querySelector('.map-stage');
  if (!stage) return;

  const svg = stage.querySelector('svg');
  const tooltip = stage.querySelector('.map-tooltip');
  if (!svg || !tooltip) return;

  const NS = 'http://www.w3.org/2000/svg';
  let hideTimer = null;
  const cancelHide = () => { if (hideTimer) { clearTimeout(hideTimer); hideTimer = null; } };

  HUBS.forEach((h) => {
    if (h.type === 'hub') {
      const pulse = document.createElementNS(NS, 'circle');
      pulse.setAttribute('cx', h.x);
      pulse.setAttribute('cy', h.y);
      pulse.setAttribute('r', 7);
      pulse.setAttribute('class', 'map-pin-pulse');
      svg.appendChild(pulse);
    }
    const pin = document.createElementNS(NS, 'circle');
    pin.setAttribute('cx', h.x);
    pin.setAttribute('cy', h.y);
    pin.setAttribute('r', h.type === 'hub' ? 7 : 5);
    pin.setAttribute('class', 'map-pin map-pin--' + h.type);
    pin.setAttribute('data-id', h.id);
    pin.setAttribute('tabindex', '0');
    pin.setAttribute('role', 'button');
    pin.setAttribute('aria-label', `${h.name}. ${h.addr}`);
    svg.appendChild(pin);

    const show = () => {
      cancelHide();
      const rect = stage.getBoundingClientRect();
      const vb = svg.viewBox.baseVal;
      const sx = rect.width / vb.width;
      const sy = rect.height / vb.height;
      tooltip.style.left = (h.x * sx) + 'px';
      tooltip.style.top = (h.y * sy) + 'px';
      const visit = h.href
        ? `<a href="${h.href}" style="display:inline-block;margin-top:6px;color:#E6062F;font-family:var(--font-caps);font-weight:600;letter-spacing:0.2em;text-transform:uppercase;font-size:0.72rem;border-bottom:2px solid #E6062F;padding-bottom:2px;">Visit →</a>`
        : '';
      tooltip.innerHTML = `<strong>${h.name}</strong><span>${h.addr}</span>${visit}`;
      tooltip.classList.add('is-on');
    };
    const hide = () => {
      cancelHide();
      hideTimer = setTimeout(() => tooltip.classList.remove('is-on'), 180);
    };

    pin.addEventListener('mouseenter', show);
    pin.addEventListener('mouseleave', hide);
    pin.addEventListener('focus', show);
    pin.addEventListener('blur', hide);
    if (h.href) {
      pin.addEventListener('click', () => { location.href = h.href; });
      pin.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); location.href = h.href; }
      });
    }
  });

  // Tooltip should stay open while the user hovers it so the Visit link is clickable.
  tooltip.style.pointerEvents = 'auto';
  tooltip.addEventListener('mouseenter', cancelHide);
  tooltip.addEventListener('mouseleave', () => tooltip.classList.remove('is-on'));
})();
