// ── Business details: fill these in ─────────────────────────────
const PHONE = "";   // e.g. "+353 1 234 5678"
const EMAIL = "";   // e.g. "info@allsortedfencing.ie"
// ────────────────────────────────────────────────────────────────

if (PHONE) document.querySelectorAll('[data-phone]').forEach(a => { a.textContent = PHONE; a.href = 'tel:' + PHONE.replace(/[^+\d]/g, ''); });
if (EMAIL) document.querySelectorAll('[data-email]').forEach(a => { a.textContent = EMAIL; a.href = 'mailto:' + EMAIL; });
document.getElementById('yr').textContent = new Date().getFullYear();

const nav = document.getElementById('nav'), burger = document.getElementById('burger');
const onScroll = () => nav.classList.toggle('scrolled', scrollY > 30);
addEventListener('scroll', onScroll, { passive: true }); onScroll();
burger.addEventListener('click', () => burger.setAttribute('aria-expanded', nav.classList.toggle('open')));

const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .08 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

const lb = document.getElementById('lightbox');
document.querySelectorAll('[data-gallery] button').forEach(b => b.addEventListener('click', () => {
  const i = b.querySelector('img');
  lb.querySelector('img').src = i.src; lb.querySelector('img').alt = i.alt;
  lb.querySelector('p').textContent = b.querySelector('span').textContent;
  lb.classList.add('open');
}));
lb.addEventListener('click', () => lb.classList.remove('open'));
addEventListener('keydown', e => { if (e.key === 'Escape') lb.classList.remove('open'); });

const form = document.getElementById('form');
if (form) form.addEventListener('submit', e => {
  e.preventDefault();
  const d = new FormData(form);
  const body = `Name: ${d.get('name')}\nPhone: ${d.get('phone')}\nArea: ${d.get('area')}\nService: ${d.get('service')}\n\n${d.get('message')}`;
  location.href = `mailto:${EMAIL}?subject=${encodeURIComponent('Quote request – ' + d.get('service'))}&body=${encodeURIComponent(body)}`;
});
