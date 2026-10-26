// Sortable table of places. Uses the same filtered result set as the sidebar list.

import { esc, statusClass, statusLabel, typeLabel } from './format';
import { t } from './i18n';
import { modernText, type Entry } from './model';
import { norm } from './search';

type SortKey = 'id' | 'old' | 'modern' | 'type' | 'status' | 'reading';

const COLS: { key: SortKey; label: () => string }[] = [
  { key: 'old', label: () => t.colOld },
  { key: 'modern', label: () => t.colModern },
  { key: 'type', label: () => t.colType },
  { key: 'status', label: () => t.colStatus },
  { key: 'reading', label: () => t.colReading },
  { key: 'id', label: () => t.colId },
];

export class PlaceTable {
  private el: HTMLElement;
  private sort: { key: SortKey; dir: 1 | -1 } | null = null; // null = relevance / alphabetical
  private rows: Entry[] = [];
  private selectedId: string | null = null;
  private onSelect: (id: string) => void;

  constructor(el: HTMLElement, onSelect: (id: string) => void) {
    this.el = el;
    this.onSelect = onSelect;
    el.addEventListener('click', (ev) => {
      const target = ev.target as HTMLElement;
      const th = target.closest('th[data-key]') as HTMLElement | null;
      if (th) {
        const key = th.dataset.key as SortKey;
        if (this.sort?.key === key) {
          this.sort = this.sort.dir === 1 ? { key, dir: -1 } : null;
        } else {
          this.sort = { key, dir: 1 };
        }
        this.render();
        return;
      }
      const tr = target.closest('tr[data-id]') as HTMLElement | null;
      if (tr?.dataset.id) this.onSelect(tr.dataset.id);
    });
  }

  update(rows: Entry[], selectedId: string | null, countText: string): void {
    this.rows = rows;
    this.selectedId = selectedId;
    this.countText = countText;
    this.render();
  }

  private countText = '';

  private value(e: Entry, key: SortKey): string {
    const p = e.place;
    switch (key) {
      case 'id': return p.id;
      case 'old': return norm(p.old);
      case 'modern': return p.modern ? norm(p.modern) : '￿'; // placeholders sort last
      case 'type': return typeLabel(p.type);
      case 'status': return p.status ? statusLabel(p.status) : '￿';
      case 'reading': return p.flag === 'unsure' ? '0' : '1';
    }
  }

  private render(): void {
    let rows = this.rows;
    if (this.sort) {
      const { key, dir } = this.sort;
      rows = [...rows].sort((a, b) => dir * this.value(a, key).localeCompare(this.value(b, key)) || a.place.id.localeCompare(b.place.id));
    }
    const head = COLS.map((c) => {
      const s = this.sort?.key === c.key ? (this.sort.dir === 1 ? ' ▲' : ' ▼') : '';
      return `<th data-key="${c.key}" class="col-${c.key}${s ? ' sorted' : ''}">${esc(c.label())}${s}</th>`;
    }).join('');
    const body = rows.map((e) => {
      const p = e.place;
      const m = modernText(p);
      return `<tr data-id="${esc(p.id)}"${p.id === this.selectedId ? ' class="sel"' : ''}>
        <td class="o">${esc(e.title)}</td>
        <td${m.placeholder ? ' class="placeholder"' : ''}>${esc(m.text)}</td>
        <td>${esc(typeLabel(p.type))}</td>
        <td><span class="badge ${statusClass(p.status)}">${esc(statusLabel(p.status))}</span></td>
        <td>${p.flag === 'unsure' ? `<span class="badge unsure">${esc(t.unsureBadge)}</span>` : ''}</td>
        <td class="id">${esc(p.id)}</td>
      </tr>`;
    }).join('');
    this.el.innerHTML = `
      <div class="table-head"><span>${esc(this.countText)}</span><span class="muted">${esc(t.tableHint)}</span></div>
      <div class="table-scroll"><table><thead><tr>${head}</tr></thead><tbody>${body}</tbody></table>
      ${rows.length ? '' : `<p class="empty">${esc(t.noResults)}</p>`}</div>`;
  }
}
