// The "Suggest a correction" page: a form that sends a message by email without a GitHub account.
// It posts to Web3Forms (https://web3forms.com), which forwards the message to the address the key
// was made for. The key is not a secret: it can only send mail to that one address. Leave it empty
// and the form says it is not switched on and points to GitHub instead.
import '@fontsource/eb-garamond/latin-400.css';
import '@fontsource/eb-garamond/latin-500.css';
import '@fontsource/eb-garamond/latin-400-italic.css';
import '@fontsource/inter/latin-400.css';
import '@fontsource/inter/latin-600.css';
import './method.css';
import './suggest.css';

const ACCESS_KEY = '';
const ENDPOINT = 'https://api.web3forms.com/submit';
const REPO = 'https://github.com/PeerBlekelj/parismapexplorer';

const $ = <T extends HTMLElement>(sel: string) => document.querySelector(sel) as T;
const form = document.querySelector<HTMLFormElement>('#suggest');
if (!form) throw new Error('no #suggest form on this page');
const status = $('#status');
/* The start page carries the same form without a place. */
const send = $<HTMLButtonElement>('#send');

// The place card links here with ?p=L0006&n=Le+Pont+S.+Michel (a place to correct), or nothing.
const q = new URLSearchParams(location.search);
const placeId = (q.get('p') ?? '').replace(/[^A-Za-z0-9_-]/g, '').slice(0, 12);
const placeName = (q.get('n') ?? '').slice(0, 120);
if (placeId && document.querySelector('#place-line')) {
  const line = $('#place-line');
  line.textContent = `About: ${placeName || 'a place'} (${placeId})`;
  line.hidden = false;
  $('#about-place').textContent = 'Something wrong or missing about this place? Tell us. You do not need an account.';
  $('#gh').setAttribute('href', `${REPO}/issues/new?template=correction.yml&place_id=${encodeURIComponent(placeId)}`);
}

if (!ACCESS_KEY) {
  send.disabled = true;
  status.textContent = 'The form is not switched on yet. Please use GitHub below for now.';
}

function say(text: string, ok = false): void {
  status.textContent = text;
  status.className = ok ? 'ok' : 'bad';
}

form.addEventListener('submit', async (ev) => {
  ev.preventDefault();
  const f = new FormData(form);
  const message = String(f.get('message') ?? '').trim();
  const email = String(f.get('email') ?? '').trim();
  if (message.length < 5) { say('Please say what should be different.'); return; }
  if (email && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) { say('That email address does not look right. Leave it empty if you prefer.'); return; }
  if (f.get('botcheck')) return; // a bot ticked the trap; pretend nothing happened
  const kind = (form.querySelector('#f-kind') as HTMLSelectElement).selectedOptions[0].text;
  send.disabled = true;
  say('Sending…');
  try {
    const res = await fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({
        access_key: ACCESS_KEY,
        subject: placeId ? `Paris 1550 correction: ${placeId} ${placeName}`.trim() : 'Paris 1550: message from the site',
        from_name: 'Paris 1550 site',
        place: placeId ? `${placeName} (${placeId}) https://paris1550.vercel.app/place/${placeId}/` : '(none)',
        about: kind,
        message,
        source: String(f.get('source') ?? '').trim(),
        name: String(f.get('name') ?? '').trim(),
        ...(email ? { email } : {}),
        botcheck: '',
      }),
    });
    const body = await res.json().catch(() => ({}));
    if (res.ok && body.success) {
      form.reset();
      send.disabled = false;
      say('Thank you. It has been sent.', true);
    } else {
      send.disabled = false;
      say('It could not be sent. Please try again later, or use GitHub below.');
    }
  } catch {
    send.disabled = false;
    say('It could not be sent. Please check your connection, or use GitHub below.');
  }
});
