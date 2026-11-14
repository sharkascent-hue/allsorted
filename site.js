// ── Business details: fill these in ─────────────────────────────
const PHONE = "";   // e.g. "+353 1 234 5678"
const EMAIL = "";   // e.g. "info@allsortedfencing.ie"
// ────────────────────────────────────────────────────────────────

const root = document.documentElement;
if (PHONE) document.querySelectorAll('[data-phone]').forEach(a => { a.textContent = PHONE; a.href = 'tel:' + PHONE.replace(/[^+\d]/g, ''); });
if (EMAIL) document.querySelectorAll('[data-email]').forEach(a => { a.textContent = EMAIL; a.href = 'mailto:' + EMAIL; });
document.getElementById('yr').textContent = new Date().getFullYear();

// Header + menus
const nav = document.getElementById('nav'), burger = document.getElementById('burger');
const onScroll = () => nav.classList.toggle('scrolled', scrollY > 30);
addEventListener('scroll', onScroll, { passive: true }); onScroll();
burger.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  burger.setAttribute('aria-expanded', open);
  root.classList.toggle('menu-open', open);
});
document.querySelectorAll('.sub-toggle').forEach(b => b.addEventListener('click', e => {
  e.stopPropagation();
  b.setAttribute('aria-expanded', b.parentElement.classList.toggle('open'));
}));
document.addEventListener('click', e => {
  document.querySelectorAll('.has-sub.open').forEach(li => {
    if (!li.contains(e.target)) { li.classList.remove('open'); li.querySelector('.sub-toggle').setAttribute('aria-expanded', false); }
  });
});

// Scroll reveal
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .08 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Page transitions: fence slats close before leaving, open on arrival (CSS)
const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
document.addEventListener('click', e => {
  const a = e.target.closest('a[href]');
  if (!a || still || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button || a.target) return;
  const url = new URL(a.href, location.href);
  if (url.origin !== location.origin || !/^(https?|file):$/.test(url.protocol)) return;
  if (url.pathname === location.pathname && url.hash) return;
  e.preventDefault();
  root.classList.remove('first', 'quick');
  root.classList.add('leaving');
  setTimeout(() => { location.href = a.href; }, 560);
});
addEventListener('pageshow', e => { if (e.persisted) { root.classList.remove('leaving', 'first'); root.classList.add('quick'); } });

// Gallery filter
document.querySelectorAll('.filters button').forEach(b => b.addEventListener('click', () => {
  document.querySelectorAll('.filters button').forEach(x => x.classList.toggle('on', x === b));
  const f = b.dataset.filter;
  document.querySelectorAll('.gallery.even button').forEach(t => { t.hidden = f !== 'all' && t.dataset.cat !== f; });
}));

// Gallery lightbox
const lb = document.getElementById('lightbox');
document.querySelectorAll('[data-gallery] button').forEach(b => b.addEventListener('click', () => {
  const i = b.querySelector('img');
  lb.querySelector('img').src = i.src; lb.querySelector('img').alt = i.alt;
  lb.querySelector('p').textContent = b.querySelector('span').textContent;
  lb.classList.add('open');
}));
lb.addEventListener('click', () => lb.classList.remove('open'));
addEventListener('keydown', e => { if (e.key === 'Escape') lb.classList.remove('open'); });

// Quote form
const form = document.getElementById('form');
if (form) form.addEventListener('submit', e => {
  e.preventDefault();
  const d = new FormData(form);
  const body = `Name: ${d.get('name')}\nPhone: ${d.get('phone')}\nArea: ${d.get('area')}\nService: ${d.get('service')}\n\n${d.get('message')}`;
  location.href = `mailto:${EMAIL}?subject=${encodeURIComponent('Quote request – ' + d.get('service'))}&body=${encodeURIComponent(body)}`;
});
