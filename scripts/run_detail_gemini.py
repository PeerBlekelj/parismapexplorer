"""Send a detail batch to Gemini through the local LiteLLM gateway.

    ../.venv/bin/python scripts/run_detail_gemini.py . work/detail/batch-01.json
    ../.venv/bin/python scripts/run_detail_gemini.py . work/detail/batch-01.json --model gemini/gemini-2.5-pro
    ../.venv/bin/python scripts/run_detail_gemini.py . work/detail/batch-01.json --limit 3   # smoke test

Reads data/research/DETAIL_BRIEF.md as the system prompt and the batch as the user message, and
writes the reply to work/detail/returned-NN.json for scripts/ingest_detail.py to check. The key
comes from ~/llm-gateway/.env and is never printed or put on a command line.

A reply that is empty, truncated or not JSON is saved as .raw.txt and reported: a model that burns
its budget thinking and returns an empty string still answers HTTP 200.
"""
import argparse, json, os, pathlib, re, sys, time, urllib.error, urllib.request

ap = argparse.ArgumentParser()
ap.add_argument('root', nargs='?', default='.')
ap.add_argument('batch')
ap.add_argument('--model', default='gemini/gemini-2.5-pro')
ap.add_argument('--limit', type=int, default=0, help='only the first N places (smoke test)')
ap.add_argument('--retry', help='work/detail/failed-NN.json: resend only those, with the reasons')
ap.add_argument('--endpoint', default='http://localhost:4000')
ap.add_argument('--temperature', type=float, default=0.2)
a = ap.parse_args()

root = pathlib.Path(a.root)
batch_p = pathlib.Path(a.batch)
brief = (root / 'data/research/DETAIL_BRIEF.md').read_text(encoding='utf-8')
batch = json.loads(batch_p.read_text(encoding='utf-8'))
places = batch['places'][:a.limit] if a.limit else batch['places']

retry_note = ''
if a.retry:
    failed = json.loads(pathlib.Path(a.retry).read_text(encoding='utf-8'))
    places = [p for p in places if p['id'] in failed]
    if not places:
        sys.exit(f'{a.retry}: none of those ids are in {batch_p.name}')
    lines = '\n'.join(f'- {i}: {"; ".join(w)}' for i, w in failed.items())
    retry_note = (
        '\n\nThis is a SECOND pass. Your previous answer for these places failed the checks:\n'
        f'{lines}\n\n'
        'Fix each one. A span in `used` must be copied character for character from that place\'s '
        '`source_fr` \u2014 do not retype it, do not correct its spelling, do not shorten it mid-word. '
        'A detail under 40 words is not worth showing next to a summary of similar length: either '
        'draw more from the source, or return null for that place.')

env = {}
for line in pathlib.Path(os.path.expanduser('~/llm-gateway/.env')).read_text().splitlines():
    m = re.match(r'^\s*([A-Z_]+)\s*=\s*(.*)$', line)
    if m:
        env[m.group(1)] = m.group(2).strip().strip('"\'')
key = env.get('LITELLM_MASTER_KEY')
if not key:
    sys.exit('no LITELLM_MASTER_KEY in ~/llm-gateway/.env')

user = ('Here is the batch. Return the JSON array described in the brief, and nothing else.\n\n'
        + json.dumps({'batch': batch['batch'], 'count': len(places), 'places': places},
                     ensure_ascii=False, indent=1) + retry_note)
body = {
    'model': a.model,
    'messages': [{'role': 'system', 'content': brief}, {'role': 'user', 'content': user}],
    'temperature': a.temperature,
    'max_tokens': 32000,
    # so the spend log attributes these calls (see the llm-gateway notes)
    'litellm_session_id': f'paris1550-detail-{batch_p.stem}',
}
print(f'{batch_p.name}: {len(places)} places -> {a.model}')
t0 = time.time()
req = urllib.request.Request(
    a.endpoint + '/v1/chat/completions',
    data=json.dumps(body).encode(),
    headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
try:
    res = json.load(urllib.request.urlopen(req, timeout=900))
except urllib.error.HTTPError as e:
    sys.exit(f'HTTP {e.code}: {e.read().decode()[:400]}')

choice = res['choices'][0]
text = (choice['message'].get('content') or '')
usage = res.get('usage', {})
print(f'  {time.time() - t0:.0f}s, finish_reason={choice.get("finish_reason")}, '
      f'in={usage.get("prompt_tokens")} out={usage.get("completion_tokens")}')
if not text.strip():
    sys.exit('  EMPTY reply with HTTP 200 — the model returned no content (thinking budget?).')
if choice.get('finish_reason') not in (None, 'stop'):
    print(f'  WARNING: finish_reason {choice.get("finish_reason")!r} — the reply may be cut short')

out_dir = root / 'work/detail'
stem = batch_p.stem.replace('batch', 'retried' if a.retry else 'returned')
# a model that wraps the array in a fence is right in substance, so unwrap rather than reject
clean = re.sub(r'^\s*```(?:json)?\s*|\s*```\s*$', '', text.strip())
try:
    parsed = json.loads(clean)
except json.JSONDecodeError as e:
    raw = out_dir / f'{stem}.raw.txt'
    raw.write_text(text, encoding='utf-8')
    sys.exit(f'  reply is not JSON ({e}); saved verbatim to {raw}')

out = out_dir / f'{stem}.json'
out.write_text(json.dumps(parsed, ensure_ascii=False, indent=1), encoding='utf-8')
n = len(parsed) if isinstance(parsed, list) else '?'
print(f'  wrote {n} entries to {out}')
print(f'  next: ../.venv/bin/python scripts/ingest_detail.py . {out}')
