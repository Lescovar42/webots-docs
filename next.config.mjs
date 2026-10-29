import nextra from 'nextra';

const withNextra = nextra({
  defaultShowCopyCode: true,
  mdxOptions: { rehypePrettyCodeOptions: { theme: 'tokyo-night' } }
});

export default withNextra({
  output: 'export',
  trailingSlash: true,
  images: { unoptimized: true },
  experimental: { cpus: 2 },
  webpack(config) { return config; }
});
