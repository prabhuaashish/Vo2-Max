import { json, redirect } from '@sveltejs/kit';

export const POST = ({ cookies, request }) => {
	cookies.delete('refresh_token', { path: '/' });
	cookies.delete('access_token', { path: '/' });
	cookies.delete('user_id', { path: '/' });
	cookies.delete('jwt_token', { path: '/' });

	if (request.headers.get('accept') === 'application/json') {
		return json({ success: true });
	}
	throw redirect(303, '/login');
};