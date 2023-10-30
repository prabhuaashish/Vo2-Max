import { STRAVA_BASE_URL } from '$env/static/private';
import { redirect } from '@sveltejs/kit';


export const load = async ({ cookies, fetch, url }) => {
	const accessToken = cookies.get('access_token');
    const refreshToken = cookies.get('refresh_token');

	if (!accessToken) {
		return {
			user: null
		};
	}
	const profileRes = await fetch(`${STRAVA_BASE_URL}/athlete`, {
        method: 'GET',
		headers: {
			Authorization: `Bearer ${accessToken}`
		}
	});
    if (profileRes.ok) {
		const profile = await profileRes.json();
		return {
			user: profile
		};
	} 
    if (profileRes.status === 401 && refreshToken) {
		// refresh the token and try again
		const refreshRes = await fetch('/api/auth/refresh');
		if (refreshRes.ok) {
			throw redirect(307, url.pathname);
		}
		return {
			user: null
		};
	} else {
		return {
			user: null
		};
	}
};