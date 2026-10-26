// Render the phone mockups to PNG: node render.js (from this folder, Playwright installed).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1340, height: 1000 }, deviceScaleFactor: 1 });
  for (const f of process.argv.slice(2)) {
    await p.goto('file://' + path.resolve(__dirname, f));
    await p.waitForTimeout(400);
    await p.screenshot({ path: path.resolve(__dirname, f.replace('.html', '.png')), fullPage: true });
  }
  await b.close();
})();
