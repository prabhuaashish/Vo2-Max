import { redirect } from '@sveltejs/kit';

export const load = ({ data, url }) => {
	const { user } = data || {};
	if (user && url.pathname === '/login') {
		throw redirect(307, '/');
	}

	return {
		user
	};
};