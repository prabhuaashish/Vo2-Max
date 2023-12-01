import { STRAVA_BASE_URL } from '$env/static/private';
import { redirect} from '@sveltejs/kit';

export const handle = async ({ event, resolve}) => {
    const jwtToken = event.cookies.get('jwt_token');
    const accessToken = event.cookies.get('access_token');
    const refreshToken = event.cookies.get('refresh_token');
    const user_id = event.cookies.get('user_id');

    if (!accessToken && !jwtToken) {
        return await resolve(event);
    }

    let profileRes;
    let userRes

    if (accessToken) {
        profileRes = await fetch(`${STRAVA_BASE_URL}/athlete`, {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${accessToken}`
            }
        });
        if (profileRes.ok) {
            // get the profile
            const profile = await profileRes.json();
            
            // save the profile
            const name = profile.firstname + ' ' + profile.lastname
            const strava_id = profile.id
        
            const response = await fetch('http://localhost:8000/strava-user', {
                method: 'POST',
                body: JSON.stringify({ name, strava_id }),
                headers: {
                    'Content-Type': 'application/json',
                },
            });
    
            const userData = await fetch(`http://localhost:8000/strava-user/${strava_id}`, {
                method: 'GET',
            });
    
            if (userData.ok) {
                const user = await userData.json();
                event.locals.user = user;
                return await resolve(event);
            }
        }

    } else {
        userRes = await fetch(`http://localhost:8000/user/${user_id}`, {
            method: 'GET'
        });
        if (userRes.ok) {
            const user = await userRes.json();
            event.locals.user = user;
            return await resolve(event);
        }
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
