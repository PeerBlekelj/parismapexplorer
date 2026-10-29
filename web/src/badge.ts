// Simple Analytics' free plan requires a visible badge from 2026-11-01; without one they lock
// the dashboard (the collected data is kept). Tuned to the pages' own colours -- paper
// background, sepia ink, the site's red for the bars -- so it reads as part of the page
// rather than as a grey sticker. One place, since both the written pages (vite.config.ts,
// under the colophon) and the map's sidebar credits (main.ts) carry it.
const SITE_ID = 'paris1550.vercel.app';
const SRC = `https://simpleanalyticsbadges.com/${SITE_ID}?background=f4ecdc&amp;text=6b5a48&amp;logo=a63a1f`;
const HREF = `https://dashboard.simpleanalytics.com/${SITE_ID}?utm_source=${SITE_ID}&amp;utm_content=badge`;

/** The badge's markup. `cls` is the class that places it on the page. */
export const badge = (cls: string): string =>
  `<a class="${cls}" href="${HREF}" referrerpolicy="origin" target="_blank" rel="noopener">` +
  `<img src="${SRC}" width="210" height="50" loading="lazy" referrerpolicy="no-referrer"` +
  ` crossorigin="anonymous" alt="Simple Analytics"></a>`;
