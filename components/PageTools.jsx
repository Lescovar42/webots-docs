'use client';

import { useState } from 'react';

export function PageTools({ original }) {
  const [copied, setCopied] = useState(false);
  async function copy() {
    try { await navigator.clipboard.writeText(location.href); setCopied(true); setTimeout(() => setCopied(false), 1800); }
    catch { setCopied(false); }
  }
  return <div className="page-tools" data-pagefind-ignore>
    <span>{original || 'Documentation'}</span>
    <div><button type="button" onClick={copy}>{copied ? 'Copied' : 'Copy link'}</button>{original && <a href={'/sources/' + original} download>Markdown ↓</a>}</div>
  </div>;
}
