import { generateStaticParamsFor, importPage } from 'nextra/pages';
import { useMDXComponents as getMDXComponents } from '../../mdx-components';
import { PageTools } from '../../components/PageTools';
import routes from '../../content-routes.json';

export const generateStaticParams = generateStaticParamsFor('mdxPath');
export const dynamicParams = false;

export async function generateMetadata(props) {
  const params = await props.params;
  const { metadata } = await importPage(params.mdxPath);
  return metadata;
}

const Wrapper = getMDXComponents().wrapper;

export default async function Page(props) {
  const params = await props.params;
  const { default: MDXContent, toc, metadata, sourceCode } = await importPage(params.mdxPath);
  const route = '/' + (params.mdxPath || []).join('/');
  const original = Object.entries(routes).find(([, value]) => value === route)?.[0];
  return (
    <Wrapper toc={toc} metadata={metadata} sourceCode={sourceCode}>
      <PageTools original={original} />
      <MDXContent {...props} params={params} />
    </Wrapper>
  );
}
