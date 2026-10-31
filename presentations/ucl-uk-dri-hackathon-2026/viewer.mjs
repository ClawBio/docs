import { fromHash, nextSlide } from './navigation.mjs';
const slides = [...document.querySelectorAll('.slide')];
const previous = document.querySelector('#previous');
const next = document.querySelector('#next');
const fullscreen = document.querySelector('#fullscreen');
let current = fromHash(location.hash, slides.length);
function show(index) {
  current = Math.max(0, Math.min(slides.length - 1, index));
  slides.forEach((slide, i) => { slide.hidden = i !== current; });
  document.querySelector('#counter').textContent = `${current + 1} / ${slides.length}`;
  previous.disabled = current === 0;
  next.disabled = current === slides.length - 1;
  history.replaceState(null, '', `#slide-${current + 1}`);
  if (slides[current + 1]) slides[current + 1].querySelector('img').loading = 'eager';
}
async function toggleFullscreen() {
  try {
    if (document.fullscreenElement) await document.exitFullscreen();
    else await document.documentElement.requestFullscreen();
  } catch { fullscreen.textContent = 'Use browser fullscreen'; }
}
previous.addEventListener('click', () => show(current - 1));
next.addEventListener('click', () => show(current + 1));
fullscreen.addEventListener('click', toggleFullscreen);
fullscreen.hidden = !document.fullscreenEnabled;
document.addEventListener('fullscreenchange', () => {
  fullscreen.textContent = document.fullscreenElement ? 'Exit fullscreen' : 'Fullscreen';
});
document.addEventListener('keydown', event => {
  if (event.altKey || event.ctrlKey || event.metaKey || /INPUT|TEXTAREA|SELECT|BUTTON|A/.test(event.target.tagName)) return;
  if (event.key.toLowerCase() === 'f') { event.preventDefault(); toggleFullscreen(); return; }
  if (['ArrowRight','ArrowDown','PageDown',' ','ArrowLeft','ArrowUp','PageUp','Home','End'].includes(event.key)) {
    event.preventDefault(); show(nextSlide(current, event.key, slides.length));
  }
});
let touchStart;
const main = document.querySelector('main');
main.addEventListener('touchstart', event => { touchStart = event.changedTouches[0].clientX; }, {passive:true});
main.addEventListener('touchend', event => {
  const delta = event.changedTouches[0].clientX - touchStart;
  if (Math.abs(delta) > 60) show(current + (delta < 0 ? 1 : -1));
}, {passive:true});
window.addEventListener('hashchange', () => show(fromHash(location.hash, slides.length)));
document.body.classList.add('interactive');
document.querySelector('footer').hidden = false;
show(current);
