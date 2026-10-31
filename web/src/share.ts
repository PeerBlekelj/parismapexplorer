// Putting a link somewhere useful: the clipboard, the phone's own share sheet, or a QR code for
// the visitor's other device. Every link is built from the page's own state; none of them is sent
// anywhere by this code.

import { qrcode } from 'qrcode-generator/qrcode.mjs';

/** Copy, falling back to the old selection trick where the clipboard API is refused. */
export async function copyText(text: string): Promise<boolean> {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch {
    /* no permission, or an insecure context */
  }
  try {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.cssText = 'position:fixed;top:0;left:0;opacity:0';
    document.body.append(ta);
    ta.select();
    const ok = document.execCommand('copy');
    ta.remove();
    return ok;
  } catch {
    return false;
  }
}

let flashEl: HTMLElement | null = null;
let flashTimer = 0;

/** A small label under `anchor` that fades by itself — no dialog to dismiss. */
export function flash(anchor: HTMLElement, message: string): void {
  flashEl?.remove();
  clearTimeout(flashTimer);
  const el = document.createElement('span');
  el.className = 'copied';
  el.setAttribute('role', 'status');
  el.textContent = message;
  document.body.append(el);
  const r = anchor.getBoundingClientRect();
  // Keep it on screen on a narrow phone, where the anchor can sit near either edge.
  const left = Math.min(Math.max(8, r.left), window.innerWidth - el.offsetWidth - 8);
  el.style.left = `${left}px`;
  el.style.top = `${r.bottom + 8}px`;
  el.style.setProperty('--arrow', `${Math.max(10, Math.min(r.left + r.width / 2 - left, el.offsetWidth - 18))}px`);
  flashEl = el;
  flashTimer = window.setTimeout(() => {
    el.classList.add('out');
    window.setTimeout(() => el.remove(), 300);
  }, 1800);
}

/**
 * Hand a link over. On a touch device that offers it, the system share sheet (which is what
 * someone reaches for to send a place to a friend); otherwise the clipboard.
 */
export async function shareLink(o: {
  url: string;
  title?: string;
  anchor: HTMLElement;
  copied: string;
  failed: string;
}): Promise<void> {
  const touch = window.matchMedia('(pointer: coarse)').matches;
  if (touch && typeof navigator.share === 'function') {
    try {
      await navigator.share({ title: o.title, url: o.url });
      return;
    } catch (err) {
      // The visitor dismissed the sheet: that is an answer, not a failure to work around.
      if (err instanceof DOMException && err.name === 'AbortError') return;
    }
  }
  flash(o.anchor, (await copyText(o.url)) ? o.copied : o.failed);
}

/**
 * The link as an inline SVG QR code. Drawn from the same string the copy button puts on the
 * clipboard, so the two can never disagree. Colours come from the page's tokens, so it keeps the
 * paper and ink of the rest of the site.
 */
export function qrSvg(text: string, label: string): string {
  const qr = qrcode(0, 'M');
  qr.addData(text);
  qr.make();
  const n = qr.getModuleCount();
  // The quiet zone is 4 modules, as the spec asks. Less than that, with the panel's border
  // right at the edge, is one of the things that stops a camera finding the symbol at all.
  const m = 4;
  let d = '';
  for (let r = 0; r < n; r++) {
    for (let c = 0; c < n; c++) {
      if (qr.isDark(r, c)) d += `M${c + m} ${r + m}h1v1h-1z`;
    }
  }
  const size = n + m * 2;
  return (
    `<svg class="qr" viewBox="0 0 ${size} ${size}" width="${size}" height="${size}" ` +
    `shape-rendering="crispEdges" role="img" aria-label="${label.replace(/"/g, '&quot;')}">` +
    `<rect width="${size}" height="${size}" fill="var(--card)"/>` +
    `<path d="${d}" fill="var(--ink)"/></svg>`
  );
}
