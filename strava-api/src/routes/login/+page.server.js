import { redirect, error } from '@sveltejs/kit';

let errorMessage = '';

// export const load = async ({}) => {
//     // todo
// };

const signup = async ({request }) => {
    const data = await request.formData();
    const name = data.get('name');
    const email = data.get('email');
    const password = data.get('password');

    try {
        const response = await fetch('http://localhost:8000/user', {
            method: 'POST',
            body: JSON.stringify({ name, email, password }),
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (response.status === 400) {
            return invalid(400,{user: true})
        }

        if (response.status === 201) {
            throw redirect(303, '/login');
        } else {
            const responseData = await response.json();
            throw error(response.status, responseData.detail);
        }
    } catch (error) {
        errorMessage = error.message;
    }
};

const login = async ({ request, cookies }) => {
    const data = await request.formData();
    const email = data.get('email');
    const password = data.get('password');

    try {
        const response = await fetch('http://localhost:8000/auth/login', {
            method: 'POST',
            body: JSON.stringify({ username: email, password: password }),
            headers: {
                'Content-Type': 'application/json',
            },
        });
        if (response.status === 404) {
            return invalid(404, { credentials: true });
        }

        const responseJSON = await response.json();

        cookies.set('jwt_token', responseJSON.access_token);
        cookies.set('user_id', responseJSON.user_id);

        throw redirect(303, '/');
    } catch (error) {
        errorMessage = error.message;
    }
};

export const actions = {
    signup,
    login,
};

