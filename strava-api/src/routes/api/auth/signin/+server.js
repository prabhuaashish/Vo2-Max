import { error, redirect } from '@sveltejs/kit';
import Cookies from 'js-cookie';

export const POST = async (request) => {
    const { email, password } = request.body;

    if (!email || !password) {
        throw error(400, 'Email and password are required');
    }

    const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        body: JSON.stringify({ username: email, password }),
        headers: {
            'Content-Type': 'application/json',
        },
    });

    const responseJSON = await response.json();

    if (responseJSON.error) {
        throw error(400, responseJSON.error_description);
    }

    // Ensure that 'Cookies' is properly imported and available for use
    Cookies.set('jwt_token', responseJSON.jwt_token, { path: '/' });

    return redirect(303, '/');
}
