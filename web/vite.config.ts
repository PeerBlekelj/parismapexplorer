// The start page (/, /fr/, /sv/) is the page about the map, written by hand in each language; the
// app lives at /map/. After the build: one static page per place and language (/place/L0123/,
// /fr/place/L0123/, /sv/place/L0123/) with its own title, description and link-preview image, the
// app's /map/ page in each language, plus sitemap.xml and robots.txt. The pages are copies of the
// app's map/index.html with only the <head> meta block swapped, so the app itself is unchanged; it
// reads the language and the place id from the path. A #place= hash never reaches the server, so link previews need
// the path form. The texts come from src/strings.ts, the app's own strings.

import { readFileSync, mkdirSync, writeFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { defineConfig, type Plugin } from 'vite';
import { LANGS, localModernIn, STRINGS, type Lang } from './src/strings';

// The site's address, in one place: the HTML pages say %SITE% and get it from siteUrl() below.
const SITE = 'https://paris1550.vercel.app';
const NAME = 'Paris 1550';

/** Path of a page in language `l`; `path` is the English one without the leading slash. */
const langPath = (l: Lang, path: string) => (l === 'en' ? `/${path}` : `/${l}/${path}`);

// The texts on the map: static pages from scripts/make_texts_page.py (en, fr, sv).
const TEXTS = ['texts', 'fr/texts', 'sv/texts'];

interface Place {
  id: string;
  old: string;
  modern: string | null;
  status: string | null;
  summary: string | null;
  summary_fr?: string | null;
  summary_sv?: string | null;
}

const attr = (s: string) =>
  s.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

function clip(s: string, n: number): string {
  if (s.length <= n) return s;
  const cut = s.slice(0, n - 1);
  return `${cut.slice(0, Math.max(cut.lastIndexOf(' '), n - 20))}…`;
}

/** "LE PONT S. MICHEL" → "Le Pont S. Michel": the labels are cut in capitals. */
function tidy(old: string): string {
  if (old !== old.toUpperCase()) return old;
  return old.toLowerCase().replace(/(^|[\s'’.-])(\p{L})/gu, (_, a: string, b: string) => a + b.toUpperCase());
}

interface Meta { lang: Lang; title: string; desc: string; path: string; image: string; alt: string; type?: string }

/** canonical (the page itself) and one hreflang alternate per language, x-default = English. */
function altLinks(l: Lang, path: string): string[] {
  return [
    `<link rel="canonical" href="${SITE}${langPath(l, path)}" />`,
    ...LANGS.map((o) => `<link rel="alternate" hreflang="${o}" href="${SITE}${langPath(o, path)}" />`),
    `<link rel="alternate" hreflang="x-default" href="${SITE}${langPath('en', path)}" />`,
  ];
}

function metaBlock(m: Meta): string {
  const url = `${SITE}${langPath(m.lang, m.path)}`;
  return [
    `<title>${attr(m.title)}</title>`,
    `<meta name="description" content="${attr(m.desc)}" />`,
    ...altLinks(m.lang, m.path),
    `<meta property="og:type" content="${m.type ?? 'website'}" />`,
    `<meta property="og:site_name" content="${NAME}" />`,
    `<meta property="og:locale" content="${STRINGS[m.lang].ogLocale}" />`,
    ...LANGS.filter((o) => o !== m.lang).map((o) => `<meta property="og:locale:alternate" content="${STRINGS[o].ogLocale}" />`),
    `<meta property="og:title" content="${attr(m.title)}" />`,
    `<meta property="og:description" content="${attr(m.desc)}" />`,
    `<meta property="og:url" content="${url}" />`,
    `<meta property="og:image" content="${m.image}" />`,
    `<meta property="og:image:width" content="800" />`,
    `<meta property="og:image:height" content="420" />`,
    `<meta property="og:image:alt" content="${attr(m.alt)}" />`,
    `<meta name="twitter:card" content="summary_large_image" />`,
  ].map((l) => `    ${l}`).join('\n');
}

function siteUrl(): Plugin {
  return {
    name: 'site-url',
    transformIndexHtml: { order: 'pre', handler: (html) => html.replaceAll('%SITE%', SITE) },
  };
}

function sitePages(): Plugin {
  let outDir = '';
  return {
    name: 'site-pages',
    apply: 'build',
    configResolved(c) {
      outDir = resolve(c.root, c.build.outDir);
    },
    closeBundle() {
      const html = readFileSync(resolve(outDir, 'map/index.html'), 'utf8');
      const block = /(<!-- page-meta[^>]*-->\n)[\s\S]*?(\n\s*<!-- \/page-meta -->)/;
      if (!block.test(html)) throw new Error('site-pages: no page-meta block in map/index.html');
      const places: Place[] = JSON.parse(readFileSync(resolve(outDir, 'data/places.json'), 'utf8')).places;
      const haveOg = existsSync(resolve(outDir, 'og'));
      if (!haveOg) this.warn('no og/ images: run scripts/make_og_images.py (pages still get the site image)');

      // `path` is the English path without the leading slash ('' = the start page).
      const write = (m: Meta) => {
        const page = html
          .replace(/<html lang="[^"]*">/, `<html lang="${m.lang}">`)
          .replace(block, (_, a: string, b: string) => a + metaBlock(m) + b);
        const dir = resolve(outDir, langPath(m.lang, m.path).slice(1));
        mkdirSync(dir, { recursive: true });
        writeFileSync(resolve(dir, 'index.html'), page);
      };

      const paths = ['', 'map/', 'method/', 'texts/'];
      for (const l of LANGS) {
        const s = STRINGS[l];
        write({ lang: l, title: s.siteTitle, desc: s.siteDesc, path: 'map/', image: `${SITE}/og/site.jpg`, alt: s.siteImageAlt });
      }
      for (const p of places) {
        const old = tidy(p.old);
        const path = `place/${p.id}/`;
        const image = haveOg && existsSync(resolve(outDir, `og/${p.id}.jpg`)) ? `${SITE}/og/${p.id}.jpg` : `${SITE}/og/site.jpg`;
        for (const l of LANGS) {
          const s = STRINGS[l];
          const modern = p.modern ? localModernIn(p.modern, s) : null;
          const title = modern && modern.toLowerCase() !== old.toLowerCase()
            ? `${old} (${modern}) · ${NAME}`
            : `${old} · ${NAME}`;
          const lead = s.placeLead(p.old, p.status, modern);
          // The translated summary, or the English one where there is none yet.
          const summary = (l === 'fr' ? p.summary_fr : l === 'sv' ? p.summary_sv : null) || p.summary;
          const desc = clip(summary ? `${lead} ${summary}` : lead, 200);
          write({ lang: l, title, desc, path, image, alt: s.placeImageAlt(p.old) });
        }
        paths.push(path);
      }

      // Every language version is its own <url>, each listing all versions as alternates (the
      // sitemap form of hreflang; the pages carry the same links in their <head>).
      const day = new Date().toISOString().slice(0, 10);
      const entries = paths.flatMap((path) => LANGS.map((l) =>
        `  <url><loc>${SITE}${langPath(l, path)}</loc><lastmod>${day}</lastmod>\n` +
        [...LANGS.map((o) => [o, langPath(o, path)]), ['x-default', langPath('en', path)]]
          .map(([h, u]) => `    <xhtml:link rel="alternate" hreflang="${h}" href="${SITE}${u}" />`).join('\n') +
        '\n  </url>'));
      writeFileSync(resolve(outDir, 'sitemap.xml'),
        '<?xml version="1.0" encoding="UTF-8"?>\n' +
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' +
        entries.join('\n') + '\n</urlset>\n');
      writeFileSync(resolve(outDir, 'robots.txt'), `User-agent: *\nAllow: /\n\nSitemap: ${SITE}/sitemap.xml\n`);
      console.log(`site-pages: ${places.length} places × ${LANGS.length} languages, sitemap with ${entries.length} urls`);
    },
  };
}

export default defineConfig({
  plugins: [siteUrl(), sitePages()],
  build: {
    rollupOptions: {
      input: {
        map: resolve(import.meta.dirname, 'map/index.html'),
        home: resolve(import.meta.dirname, 'index.html'),
        homeFr: resolve(import.meta.dirname, 'fr/index.html'),
        homeSv: resolve(import.meta.dirname, 'sv/index.html'),
        method: resolve(import.meta.dirname, 'method/index.html'),
        methodFr: resolve(import.meta.dirname, 'fr/method/index.html'),
        methodSv: resolve(import.meta.dirname, 'sv/method/index.html'),
        ...Object.fromEntries(TEXTS.map((t) => [t.replace('/', '-'), resolve(import.meta.dirname, t, 'index.html')])),
      },
    },
  },
});
