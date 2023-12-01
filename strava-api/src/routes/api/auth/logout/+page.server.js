import { redirect } from '@sveltejs/kit'

export const actions = {
	default({ cookies }) {
        cookies.delete('refresh_token', { path: '/' });
        cookies.delete('access_token', { path: '/' });
        cookies.delete('user_id', { path: '/' });
        cookies.delete('jwt_token', { path: '/' });

		// redirect the user
		throw redirect(302, '/')
	},
}