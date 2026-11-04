// The bar at the top of every written page (markup added by the build, see withTopbar in
// vite.config.ts): on a phone the section list opens from a "Contents" button, and the section being
// read is marked as the page scrolls.
const bar = document.querySelector<HTMLElement>('.topbar');
if (bar) {
  const menu = bar.querySelector<HTMLButtonElement>('.menu');
  const list = bar.querySelector<HTMLElement>('.sections');
  const close = (): void => { list?.classList.remove('open'); menu?.setAttribute('aria-expanded', 'false'); };
  menu?.addEventListener('click', () => {
    const open = list?.classList.toggle('open') ?? false;
    menu.setAttribute('aria-expanded', String(open));
  });
  list?.addEventListener('click', (ev) => { if ((ev.target as HTMLElement).closest('a')) close(); });
  document.addEventListener('keydown', (ev) => { if (ev.key === 'Escape') close(); });
  document.addEventListener('click', (ev) => { if (!bar.contains(ev.target as Node)) close(); });

  const links = [...bar.querySelectorAll<HTMLAnchorElement>('.sections a[href^="#"]')];
  const byId = new Map(links.map((a) => [a.getAttribute('href')!.slice(1), a]));
  const mark = (id: string): void => links.forEach((a) => a.toggleAttribute('aria-current', byId.get(id) === a));
  if (links.length && 'IntersectionObserver' in window) {
    const seen = new Set<string>();
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) (e.isIntersecting ? seen.add(e.target.id) : seen.delete(e.target.id));
      // the first section (in page order) that is in the reading band
      const first = links.map((a) => a.getAttribute('href')!.slice(1)).find((id) => seen.has(id));
      if (first) mark(first);
    }, { rootMargin: '-15% 0px -70% 0px' });
    byId.forEach((_, id) => { const el = document.getElementById(id); if (el) io.observe(el); });
  }
}
