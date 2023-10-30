import { error, redirect } from '@sveltejs/kit';
import { STRAVA_APP_CLIENT_ID, STRAVA_APP_CLIENT_SECRET } from '$env/static/private';

export const GET = async ({ url, cookies, fetch }) => {
    const code = url.searchParams.get('code') || null;
    const state = url.searchParams.get('state') || null;
  
    const storedState = cookies.get('spotify_auth_state') || null;
  
    if (state === null || state !== storedState) {
      throw error(400, 'State Mismatch!');
    }
  
    const response = await fetch('https://www.strava.com/oauth/token', {
      method: 'POST',
      body: new URLSearchParams({
        code: code || '',
        grant_type: 'authorization_code',
        client_id: STRAVA_APP_CLIENT_ID,
        client_secret: STRAVA_APP_CLIENT_SECRET
      })
    });
  
    const responseJSON = await response.json();
    
  
    if (responseJSON.error) {
      throw error(400, responseJSON.error_description);
    }
  
    cookies.delete('spotify_auth_state');
    cookies.set('refresh_token', responseJSON.refresh_token, { path: '/' });
    cookies.set('access_token', responseJSON.access_token, { path: '/' });
  
    throw redirect(303, '/');
  };