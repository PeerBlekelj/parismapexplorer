// A first-visit card at the top of the sidebar pointing to the about page. Switch it off with
// WELCOME_CARD. It stays away once dismissed (×) or followed, remembered in this browser only.

import { esc } from './format';
import { langBase, t } from './i18n';

export const WELCOME_CARD = true;
const STORE_KEY = 'welcome-dismissed';

function dismissed(): boolean {
  try {
    return localStorage.getItem(STORE_KEY) === '1';
  } catch {
    return false; // storage blocked: show it, the × still hides it for this page view
  }
}

function dismiss(el: HTMLElement): void {
  el.hidden = true;
  try {
    localStorage.setItem(STORE_KEY, '1');
  } catch { /* storage blocked */ }
}

export function renderWelcome(el: HTMLElement): void {
  if (!WELCOME_CARD || dismissed()) {
    el.hidden = true;
    return;
  }
  el.hidden = false;
  el.innerHTML =
    `<p><strong>${esc(t.welcomeTitle)}</strong> ${esc(t.welcomeText)} ` +
    `<a href="${langBase()}about/">${esc(t.welcomeLink)}</a></p>` +
    `<button type="button" class="welcome-x" aria-label="${esc(t.welcomeDismiss)}" title="${esc(t.welcomeDismiss)}">×</button>`;
  el.querySelector('a')?.addEventListener('click', () => dismiss(el));
  el.querySelector('button')?.addEventListener('click', () => dismiss(el));
}
