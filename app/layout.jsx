import { Layout, Navbar } from 'nextra-theme-docs';
import { Head } from 'nextra/components';
import { getPageMap } from 'nextra/page-map';
import 'nextra-theme-docs/style.css';
import './globals.css';

export const metadata = {
  title: { default: 'Robot documentation', template: '%s · Robot docs' },
  description: 'Reviewed documentation for Alphonse, Chronus, Orion, and their shared systems.'
};

function SnapshotDate() {
  return <span className="snapshot-date">Snapshot · 29 October 2026</span>;
}

export default async function RootLayout({ children }) {
  return (
    <html lang="en" dir="ltr" className="dark" suppressHydrationWarning>
      <Head color={{ hue: 221, saturation: 85, lightness: 72 }} backgroundColor={{ dark: '#1a1b26', light: '#1a1b26' }} />
      <body>
        <Layout
          pageMap={await getPageMap()}
          navbar={<Navbar logo={<span className="reader-title">Robot documentation</span>} projectLink="" />}
          footer={null}
          darkMode={false}
          copyPageButton={false}
          nextThemes={{ defaultTheme: 'dark', forcedTheme: 'dark' }}
          editLink={null}
          feedback={{ content: null }}
          lastUpdated={<SnapshotDate />}
          sidebar={{ autoCollapse: true, defaultMenuCollapseLevel: 1 }}
          toc={{ title: 'On this page', backToTop: 'Back to top' }}
        >
          {children}
        </Layout>
      </body>
    </html>
  );
}
