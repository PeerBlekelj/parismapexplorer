// After the build: one static page per place (/place/L0123/) with its own title, description
// and link-preview image, plus sitemap.xml and robots.txt. The pages are copies of the app's
// index.html with only the <head> meta block swapped, so the app itself is unchanged; it reads
// the place id from the path. A #place= hash never reaches the server, so link previews need
// the path form.

import { readFileSync, mkdirSync, writeFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { defineConfig, type Plugin } from 'vite';

// The site's address, in one place: the HTML pages say %SITE% and get it from siteUrl() below.
const SITE = 'https://paris1550.vercel.app';
const NAME = 'Paris 1550';

const STATUS: Record<string, string> = {
  standing: 'still standing',
  rebuilt: 'rebuilt',
  renamed: 'renamed',
  vanished: 'vanished',
};

interface Place {
  id: string;
  old: string;
  modern: string | null;
  status: string | null;
  summary: string | null;
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

function metaBlock(m: { title: string; desc: string; url: string; image: string; alt: string }): string {
  return [
    `<title>${attr(m.title)}</title>`,
    `<meta name="description" content="${attr(m.desc)}" />`,
    `<link rel="canonical" href="${m.url}" />`,
    `<meta property="og:type" content="website" />`,
    `<meta property="og:site_name" content="${NAME}" />`,
    `<meta property="og:title" content="${attr(m.title)}" />`,
    `<meta property="og:description" content="${attr(m.desc)}" />`,
    `<meta property="og:url" content="${m.url}" />`,
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
      const html = readFileSync(resolve(outDir, 'index.html'), 'utf8');
      const block = /(<!-- page-meta[^>]*-->\n)[\s\S]*?(\n\s*<!-- \/page-meta -->)/;
      if (!block.test(html)) throw new Error('site-pages: no page-meta block in index.html');
      const places: Place[] = JSON.parse(readFileSync(resolve(outDir, 'data/places.json'), 'utf8')).places;
      const haveOg = existsSync(resolve(outDir, 'og'));
      if (!haveOg) this.warn('no og/ images: run scripts/make_og_images.py (pages still get the site image)');

      const urls = [`${SITE}/`, `${SITE}/method/`];
      for (const p of places) {
        const old = tidy(p.old);
        const status = p.status ? STATUS[p.status] : null;
        const title = p.modern && p.modern.toLowerCase() !== old.toLowerCase()
          ? `${old} (${p.modern}) · Paris 1550`
          : `${old} · Paris 1550`;
        const lead = `“${p.old}” on the Truschet & Hoyau plan of Paris, c. 1550` +
          (status ? `: ${status}` : '') + (p.modern && p.status === 'renamed' ? ` as ${p.modern}` : '') + '.';
        const desc = clip(p.summary ? `${lead} ${p.summary}` : lead, 200);
        const url = `${SITE}/place/${p.id}/`;
        const image = haveOg && existsSync(resolve(outDir, `og/${p.id}.jpg`)) ? `${SITE}/og/${p.id}.jpg` : `${SITE}/og/site.jpg`;
        const page = html.replace(block, (_, a: string, b: string) =>
          a + metaBlock({ title, desc, url, image, alt: `The label “${p.old}” on the 1550 map` }) + b);
        const dir = resolve(outDir, 'place', p.id);
        mkdirSync(dir, { recursive: true });
        writeFileSync(resolve(dir, 'index.html'), page);
        urls.push(url);
      }

      const day = new Date().toISOString().slice(0, 10);
      writeFileSync(resolve(outDir, 'sitemap.xml'),
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        urls.map((u) => `  <url><loc>${u}</loc><lastmod>${day}</lastmod></url>`).join('\n') + '\n</urlset>\n');
      writeFileSync(resolve(outDir, 'robots.txt'), `User-agent: *\nAllow: /\n\nSitemap: ${SITE}/sitemap.xml\n`);
      console.log(`site-pages: ${places.length} place pages, sitemap with ${urls.length} urls`);
    },
  };
}

export default defineConfig({
  plugins: [siteUrl(), sitePages()],
  build: {
    rollupOptions: {
      input: { main: resolve(import.meta.dirname, 'index.html'), method: resolve(import.meta.dirname, 'method/index.html') },
    },
  },
});
