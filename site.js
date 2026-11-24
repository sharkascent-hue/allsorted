
const root = document.documentElement;
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

// Gallery lightbox with previous / next
const lb = document.getElementById('lightbox');
const lbImg = lb.querySelector('img'), lbCap = lb.querySelector('.lb-cap'), lbCount = lb.querySelector('.lb-count');
let lbItems = [], lbIdx = 0, lbLast = null;
const visible = b => !b.hidden && b.offsetParent !== null;
function lbShow(i, dir) {
  lbIdx = (i + lbItems.length) % lbItems.length;
  const b = lbItems[lbIdx], im = b.querySelector('img');
  lbImg.classList.remove('slide-l', 'slide-r'); void lbImg.offsetWidth;
  if (dir) lbImg.classList.add(dir > 0 ? 'slide-l' : 'slide-r');
  lbImg.src = im.src; lbImg.alt = im.alt;
  lbCap.textContent = b.querySelector('span').textContent;
  lbCount.textContent = `${lbIdx + 1} / ${lbItems.length}`;
  const one = lbItems.length < 2;
  lb.querySelectorAll('.lb-nav').forEach(n => n.hidden = one);
  [lbIdx - 1, lbIdx + 1].forEach(k => { const n = lbItems[(k + lbItems.length) % lbItems.length]; if (n) new Image().src = n.querySelector('img').src; });
}
function lbOpen(b) {
  lbItems = [...b.closest('[data-gallery]').querySelectorAll('button')].filter(visible);
  lbLast = b; lb.hidden = false; root.classList.add('lb-open');
  requestAnimationFrame(() => lb.classList.add('open'));
  lbShow(lbItems.indexOf(b), 0); lb.querySelector('.lb-next').focus({ preventScroll: true });
}
function lbClose() {
  lb.classList.remove('open'); root.classList.remove('lb-open');
  setTimeout(() => { lb.hidden = true; }, 250); if (lbLast) lbLast.focus({ preventScroll: true });
}
document.querySelectorAll('[data-gallery] button').forEach(b => b.addEventListener('click', () => lbOpen(b)));
lb.querySelector('.lb-prev').addEventListener('click', e => { e.stopPropagation(); lbShow(lbIdx - 1, -1); });
lb.querySelector('.lb-next').addEventListener('click', e => { e.stopPropagation(); lbShow(lbIdx + 1, 1); });
lb.querySelector('.lb-close').addEventListener('click', lbClose);
lb.addEventListener('click', e => { if (e.target === lb || e.target.classList.contains('lb-stage')) lbClose(); });
addEventListener('keydown', e => {
  if (lb.hidden) return;
  if (e.key === 'Escape') lbClose();
  else if (e.key === 'ArrowRight') lbShow(lbIdx + 1, 1);
  else if (e.key === 'ArrowLeft') lbShow(lbIdx - 1, -1);
});
let tx = null, ty = 0;
lb.addEventListener('touchstart', e => { tx = e.touches[0].clientX; ty = e.touches[0].clientY; }, { passive: true });
lb.addEventListener('touchend', e => {
  if (tx === null) return;
  const dx = e.changedTouches[0].clientX - tx, dy = e.changedTouches[0].clientY - ty; tx = null;
  if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)) lbShow(lbIdx + (dx < 0 ? 1 : -1), dx < 0 ? 1 : -1);
  else if (dy > 90 && Math.abs(dy) > Math.abs(dx)) lbClose();
});

// Quote form: sent through Web3Forms to the business email, no page reload
const form = document.getElementById('form');
if (form) form.addEventListener('submit', async e => {
  e.preventDefault();
  const btn = form.querySelector('button[type=submit]'), status = form.querySelector('.form-status');
  btn.disabled = true; btn.textContent = 'Sending…'; status.className = 'form-status'; status.textContent = '';
  try {
    const res = await fetch(form.action, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) });
    const data = await res.json();
    if (!res.ok || !data.success) throw new Error(data.message || 'Send failed');
    form.reset(); status.classList.add('ok');
    status.textContent = "Thanks — your request has been sent. We'll be in touch soon.";
  } catch (err) {
    status.classList.add('err');
    status.innerHTML = 'Sorry, that didn\'t send. Please call <a href="tel:+353874972416">+353 87 497 2416</a> or email <a href="mailto:allsortedfencingandlandscaping@gmail.com">allsortedfencingandlandscaping@gmail.com</a>.';
  } finally { btn.disabled = false; btn.textContent = 'Send my request'; }
});
