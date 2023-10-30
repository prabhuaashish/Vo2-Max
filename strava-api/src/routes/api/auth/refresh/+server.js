import { STRAVA_APP_CLIENT_ID, STRAVA_APP_CLIENT_SECRET } from '$env/static/private';
import { error, json } from '@sveltejs/kit';

export const GET = async ({ cookies, fetch }) => {
	const refreshToken = cookies.get('refresh_token');

	const response = await fetch('https://www.strava.com/oauth/token', {
		method: 'POST',
		body: new URLSearchParams({
            client_id: STRAVA_APP_CLIENT_ID,
            client_secret: STRAVA_APP_CLIENT_SECRET,
			grant_type: 'refresh_token',
			refresh_token: refreshToken || ''
		})
	});

	const responseJSON = await response.json();
	if (responseJSON.error) {
		cookies.delete('refresh_token', { path: '/' });
		cookies.delete('access_token', { path: '/' });
		throw error(401, responseJSON.error_description);
	}

	cookies.set('refresh_token', responseJSON.refresh_token, { path: '/' });
	cookies.set('access_token', responseJSON.access_token, { path: '/' });

	return json(responseJSON);
};