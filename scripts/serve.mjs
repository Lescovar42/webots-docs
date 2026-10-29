import { createServer } from 'node:http';
import { createReadStream, existsSync, statSync } from 'node:fs';
import { resolve, extname, sep } from 'node:path';

const base = resolve('out');
const mime = { '.html':'text/html; charset=utf-8', '.css':'text/css', '.js':'text/javascript', '.json':'application/json', '.wasm':'application/wasm', '.svg':'image/svg+xml', '.png':'image/png', '.woff2':'font/woff2', '.md':'text/plain; charset=utf-8', '.zip':'application/zip', '.pf_fragment':'application/octet-stream', '.pf_index':'application/octet-stream', '.pf_meta':'application/octet-stream' };
const port = Number(process.env.PORT || 4174);
if (!existsSync(base)) throw new Error('Build the site first: npm run build');
createServer((req, res) => {
  try {
    const pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    let file = resolve(base, '.' + pathname);
    if (file !== base && !file.startsWith(base + sep)) { res.writeHead(403); res.end(); return; }
    if (existsSync(file) && statSync(file).isDirectory()) file = resolve(file, 'index.html');
    if (!existsSync(file)) { res.writeHead(404, { 'Content-Type':'text/html' }); createReadStream(resolve(base, '404.html')).pipe(res); return; }
    res.writeHead(200, { 'Content-Type':mime[extname(file)] || 'application/octet-stream', 'Cache-Control':'no-cache' });
    createReadStream(file).pipe(res);
  } catch { res.writeHead(400); res.end('Bad request'); }
}).listen(port, '127.0.0.1', () => process.stdout.write(`Local: http://127.0.0.1:${port}/\n`));
