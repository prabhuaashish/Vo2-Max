import adapter from '@sveltejs/adapter-node';
import preprocess from 'svelte-preprocess';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: preprocess({
		scss: {
			prependData: '@use "src/styles/functions";@use "@unsass/breakpoint";'
		}
	}),

	kit: {
		adapter: adapter()
	}
};

export default config;