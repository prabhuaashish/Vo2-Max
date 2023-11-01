import  { redirect } from '@sveltejs/kit';

import { STRAVA_APP_CLIENT_ID, BASE_URL } from '$env/static/private';

const generateRandomString = (length) => {
    let randomString = '';
    const possibleChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  
    for (let i = 0; i < length; i++) {
      randomString += possibleChars.charAt(Math.floor(Math.random() * possibleChars.length));
    }
    return randomString;
  };
  
  const state = generateRandomString(16);

const scope = "read,read_all,profile:read_all,profile:write,activity:read,activity:read_all,activity:write"

export const GET = ({ cookies }) => {
    cookies.set('spotify_auth_state', state);
    const queryParams = new URLSearchParams({
        response_type: 'code',
        client_id: STRAVA_APP_CLIENT_ID,
        approval_prompt: '',
        scope,
        redirect_uri: `${BASE_URL}/api/auth/callback`,
        state,
      });
    
    const url = `https://www.strava.com/oauth/authorize?${queryParams}`;

    throw redirect(307, url);
};