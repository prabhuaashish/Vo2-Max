import {fail, redirect} from '@sveltejs/kit';

const signup = async ({request }) => {
    const data = await request.formData();
    const name = data.get('name');
    const email = data.get('email');
    const password = data.get('password');

    const response = await fetch('http://localhost:8000/user', {
        method: 'POST',
        body: JSON.stringify({ name, email, password }),
        headers: {
            'Content-Type': 'application/json',
        },
    });

    if (response.status === 400) {
        return fail(400, {user:true})
    }

    if (response.status === 201) {
        return {created:true}
    }

};

const login = async ({ request, cookies }) => {
    const data = await request.formData();
    const email = data.get('email');
    const password = data.get('password');

    const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify({ username: email, password: password }),
        headers: {
            'Content-Type': 'application/json',
        }

    });

    if (response.status === 404) {
        return fail(404, {credentials:true})
    }
    
    const setCookie = response.headers.get('set-cookie')

    cookies.set(setCookie)
    
    // Redirect to the home page
    throw redirect(303, '/');

};

export const actions = {
    signup,
    login,
};

