export function fromHash(hash, count) {
  const match = /^#slide-(\d+)$/.exec(hash);
  return match ? Math.max(0, Math.min(count - 1, Number(match[1]) - 1)) : 0;
}
export function nextSlide(current, key, count) {
  if (key === 'Home') return 0;
  if (key === 'End') return count - 1;
  if (['ArrowRight', 'ArrowDown', 'PageDown', ' '].includes(key)) return Math.min(count - 1, current + 1);
  if (['ArrowLeft', 'ArrowUp', 'PageUp'].includes(key)) return Math.max(0, current - 1);
  return current;
}
