import { STRAVA_BASE_URL } from '$env/static/private';
import { redirect } from '@sveltejs/kit';
import { url } from '$app/environment';

export const handle = async ({ event, resolve }) => {
    const jwtToken = event.cookies.get('jwt_token');
    const accessToken = event.cookies.get('access_token');
    const refreshToken = event.cookies.get('refresh_token');
    const user_id = event.cookies.get('user_id');

    if (!accessToken && !jwtToken) {
        return await resolve(event);
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
        });
    }

    if (profileRes.ok) {
        // get the profile
        const profile = await profileRes.json();
        console.log(profile);
		

        event.locals.user = profile;
        return await resolve(event);
    }

    if (profileRes.status === 401 && refreshToken) {
        // refresh the token and try again
        const refreshRes = await fetch('/api/auth/refresh');
        if (refreshRes.ok) {
            const originalUrl = new URL(event.request.url);
            throw redirect(307, originalUrl.pathname); // Use originalUrl.pathname here
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
