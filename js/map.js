/* Hello Media — Interactive world map
   Pins + tooltip on hover.
   Coordinates are percentage (x,y) inside a 1000×520 viewBox of the map SVG.
*/
(function () {
  'use strict';

  const HUBS = [
    { id: 'uae',    name: 'UAE (Headquarters)', addr: 'Dubai Media City, Dubai, United Arab Emirates', type: 'hub',    x: 640, y: 245 },
    { id: 'uk',     name: 'United Kingdom',     addr: 'London — Market Hub',                            type: 'hub',    x: 482, y: 170 },
    { id: 'usa',    name: 'United States',      addr: 'New York — Market Hub',                          type: 'hub',    x: 258, y: 205 },
    { id: 'brazil', name: 'Brazil',             addr: 'São Paulo — Market Hub',                         type: 'hub',    x: 360, y: 360 },
    { id: 'china',  name: 'China',              addr: 'Shanghai — Market Hub',                          type: 'hub',    x: 820, y: 225 },
    { id: 'egypt',  name: 'Egypt',              addr: 'Cairo — Market Hub',                             type: 'hub',    x: 552, y: 245 },
    { id: 'india',  name: 'India',              addr: 'Mumbai — Production Studio',                     type: 'studio', x: 720, y: 260 },
    { id: 'pak',    name: 'Pakistan',           addr: 'Karachi — Production Studio',                    type: 'studio', x: 700, y: 245 },
  ];

  const stage = document.querySelector('.map-stage');
  if (!stage) return;

  const svg = stage.querySelector('svg');
  const tooltip = stage.querySelector('.map-tooltip');
  if (!svg || !tooltip) return;

  const NS = 'http://www.w3.org/2000/svg';
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
      const rect = stage.getBoundingClientRect();
      const vb = svg.viewBox.baseVal;
      const sx = rect.width / vb.width;
      const sy = rect.height / vb.height;
      tooltip.style.left = (h.x * sx) + 'px';
      tooltip.style.top = (h.y * sy) + 'px';
      tooltip.innerHTML = `<strong>${h.name}</strong><span>${h.addr}</span>`;
      tooltip.classList.add('is-on');
    };
    const hide = () => tooltip.classList.remove('is-on');

    pin.addEventListener('mouseenter', show);
    pin.addEventListener('mouseleave', hide);
    pin.addEventListener('focus', show);
    pin.addEventListener('blur', hide);
  });
})();
