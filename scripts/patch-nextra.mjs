// Nextra removes children before validating Layout props. Newer Zod versions
// correctly reject that missing field unless its schema is explicitly optional.
// Keep patched Zod, and make this one-field compatibility fix during install.
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const packageRoot = resolve('node_modules/nextra-theme-docs');
const pkg = JSON.parse(readFileSync(resolve(packageRoot, 'package.json'), 'utf8'));
if (pkg.version !== '4.6.1') throw new Error('Review the Nextra schema compatibility fix before updating nextra-theme-docs.');
const file = resolve(packageRoot, 'dist/schemas.js');
const source = readFileSync(file, 'utf8');
const original = '  children: reactNode,';
const corrected = '  children: reactNode.optional(),';
if (source.includes(original)) {
  writeFileSync(file, source.replace(original, corrected));
  process.stdout.write('Applied Nextra Layout schema compatibility fix.\n');
} else if (!source.includes(corrected)) {
  throw new Error('Nextra Layout schema changed; review scripts/patch-nextra.mjs.');
}
