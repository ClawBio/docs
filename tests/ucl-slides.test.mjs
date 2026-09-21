import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { fromHash, nextSlide } from '../docs/presentations/ucl-uk-dri-hackathon-2026/navigation.mjs';
test('deep links reject invalid values and clamp to the deck', () => {
  assert.equal(fromHash('#slide-7', 12), 6);
  for (const hash of ['', '#bogus', '#slide-NaN', '#slide-2x']) assert.equal(fromHash(hash, 12), 0);
  assert.equal(fromHash('#slide-99', 12), 11);
  assert.equal(fromHash('#slide-0', 12), 0);
});
test('keyboard navigation respects first and last slide', () => {
  assert.equal(nextSlide(0, 'ArrowLeft', 12), 0);
  assert.equal(nextSlide(11, ' ', 12), 11);
  assert.equal(nextSlide(4, 'ArrowRight', 12), 5);
  assert.equal(nextSlide(4, 'PageUp', 12), 3);
  assert.equal(nextSlide(4, 'Home', 12), 0);
  assert.equal(nextSlide(4, 'End', 12), 11);
  assert.equal(nextSlide(4, 'x', 12), 4);
});
test('all twelve slides and preserved downloads exist', () => {
  const base = new URL('../docs/presentations/ucl-uk-dri-hackathon-2026/', import.meta.url);
  const html = readFileSync(new URL('index.html', base), 'utf8');
  assert.equal((html.match(/class="slide"/g) || []).length, 12);
  for(let n=1;n<=12;n++) assert.ok(existsSync(new URL(`slides/slide-${String(n).padStart(2,'0')}.png`,base)));
  for(const ext of ['pdf','pptx']) {
    const name=`ClawBio-UK-DRI-15min-v1.${ext}`;
    assert.ok(html.includes(name)); assert.ok(existsSync(new URL(name,base)));
  }
  assert.ok(html.includes('aria-live="polite"'));
  assert.ok(html.includes('<noscript>'));
});
