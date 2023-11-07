import { STRAVA_BASE_URL } from '$env/static/private';
import { redirect } from '@sveltejs/kit';


export const load = async ({ cookies, fetch, url }) => {
	const jwtToken = cookies.get('jwt_token');
	const accessToken = cookies.get('access_token');
    const refreshToken = cookies.get('refresh_token');
	const user_id = cookies.get('user_id');

	if (!accessToken && !jwtToken) {
		return {
			user: null
		};
	}

	let profileRes;

	if (accessToken) {
		profileRes = await fetch(`${STRAVA_BASE_URL}/athlete`, {
			method: 'GET',
			headers: {
				Authorization: `Bearer ${accessToken}`
			}
		});
	} else {
		profileRes = await fetch(`http://localhost:8000/user/${user_id}`, {
			method: 'GET'
		})
	}
    if (profileRes.ok) {
		// get the profile
		const profile = await profileRes.json();
		console.log(profile)
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